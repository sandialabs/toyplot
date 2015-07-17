# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import numbers
import numpy
import toyplot.axes
import toyplot.broadcast
import toyplot.color
import toyplot.compatibility
import toyplot.config
import toyplot.layout
import toyplot.style
import toyplot.units


class AnimationFrame(object):

    """Used to specify modifications to a `toyplot.canvas.Canvas` during animation.

    Do not create AnimationFrame instances yourself, an instance of
    AnimationFrame is automatically created by :meth:`toyplot.canvas.Canvas.animate`
    or :meth:`toyplot.canvas.Canvas.time` and passed to your callback.
    """

    def __init__(self, index, begin, end, changes):
        self._index = index
        self._begin = begin
        self._end = end
        self._changes = changes

        # Pre-initialize storage for this frame
        self._changes[self._begin]
        self._changes[self._end]

    def __repr__(self):
        return "<toyplot.canvas.AnimationFrame %s %.2f %.2f>" % (
            self._index, self._begin, self._end)

    def index(self):
        """Return the current animation frame index.
        """
        return self._index

    def time(self):
        """Return the current animation time, in seconds.
        """
        return self._begin

    def duration(self):
        """Return the duration of the current animation frame, in seconds.
        """
        return self._end - self._begin

    def set_mark_style(self, mark, style):
        """Change the style of a mark.

        Parameters
        ----------
        mark: :class:`toyplot.mark.Mark` instance
        style: dict containing CSS style information
        """
        if not isinstance(mark, toyplot.mark.Mark):
            raise ValueError(
                "Mark style can only be set on toyplot.mark.Mark instances.")
        self._changes[self._begin]["set-mark-style"].append((mark, style))

    def set_datum_style(self, mark, series, datum, style):
        """Change the style of one datum in a :class:`toyplot.mark.Mark` at the current frame.

        Parameters
        ----------
        mark: :class:`toyplot.mark.Mark` instance
        index: zero-based index of the datum to modify
        style: dict containing CSS style information
        """
        if not isinstance(
            mark,
            (toyplot.mark.BarBoundaries,
             toyplot.mark.BarMagnitudes,
             toyplot.mark.Plot,
             toyplot.mark.Text)):
            raise ValueError("Cannot set datum style for %s." % type(mark))
        self._changes[self._begin][
            "set-datum-style"].append((mark, series, datum, style))

    def set_datum_text(self, mark, series, datum, text):
        """Change the text in a :class:`toyplot.mark.Text` at the current frame.

        Parameters
        ----------
        mark: :class:`toyplot.mark.Text` instance
        value: string
        """
        if not isinstance(mark, toyplot.mark.Text):
            raise ValueError(
                "Mark text can only be set for toyplot.mark.Text instances.")
        self._changes[self._begin][
            "set-datum-text"].append((mark, series, datum, text))

##########################################################################
# Canvas


class Canvas(object):

    """Top-level container for Toyplot drawings.

    Parameters
    ----------
    width: number, string, or (number, string) tuple, optional
      Width of the canvas.  Assumes CSS pixels if units aren't provided.
      Defaults to 600px (6.25") if unspecified.  See :ref:`units` for details on
      how Toyplot handles real world units.
    height: number, string, or (number, string) tuple, optional
      Height of the canvas.  Assumes CSS pixels if units aren't provided.
      Defaults to the canvas width if unspecified.  See :ref:`units` for details
      on how Toyplot handles real world units.
    style: dict, optional
      Collection of CSS styles to apply to the canvas.
    autorender: boolean, optional
      Turn autorendering on / off for this canvas.  Default:
      use the global autorender flag.

    Examples
    --------

    The following would create a Canvas 8 inches wide and 6 inches tall, with a yellow background:

    >>> canvas = toyplot.Canvas("8in", "6in", style={"background-color":"yellow"})
    """

    def __init__(self, width=None, height=None, style=None, autorender=None):
        self._width = toyplot.units.convert(
            width, "px", default="px") if width is not None else 600
        self._height = toyplot.units.convert(
            height, "px", default="px") if height is not None else self._width
        self._style = toyplot.style.combine(
            {
                "background-color": "transparent",
                "fill": toyplot.color.near_black,
                "fill-opacity": 1.0,
                "font-family": "helvetica",
                "font-size": "12px",
                "opacity": 1.0,
                "stroke": toyplot.color.near_black,
                "stroke-opacity": 1.0,
                "stroke-width": 1.0},
            style)
        self._animation = collections.defaultdict(
            lambda: collections.defaultdict(list))
        self._children = []

        self.autorender(
            autorender if autorender is not None else toyplot.config.autorender)

    def _repr_html_(self):
        import toyplot.html
        import xml.etree.ElementTree as xml
        return toyplot.compatibility.unicode_type(
            xml.tostring(
                toyplot.html.render(self),
                encoding="utf-8",
                method="html"),
            encoding="utf-8")

    def animate(self, frames, callback=None):
        """Generate a collection of animation frames, calling a callback to store an explicit representation of what changes at each frame.

        Parameters
        ----------
        frames: integer, tuple, or sequence
          Pass a sequence of values that specify the time (in seconds) of the
          beginning / end of each frame.  Note that the number of frames will be the
          length of the sequence minus one.  Alternatively, you can pass a 2-tuple
          containing the number of frames and the frame rate in frames-per-second.
          Finally, you may simply specify the number of frames, in which case the
          rate will default to 30 frames-per-second.
        callback: function
          The callback function will be called once per frame, and will receive an
          instance of :class:`toyplot.canvas.AnimationFrame` as its sole argument.  The
          callback function can access the frame number, time, and duration from the
          state object, and should use the other methods provided by the state object
          to make changes to the canvas.
        """
        if isinstance(frames, numbers.Integral):
            frames = (frames, 30.0)

        if isinstance(frames, tuple):
            frame_count, frame_rate = frames
            frames = numpy.linspace(
                0, frame_count / frame_rate, frame_count + 1, endpoint=True)

        for index in range(0, len(frames) - 1):
            frame = AnimationFrame(
                index, frames[index], frames[index + 1], self._animation)
            if callback:
                callback(frame)

        # Record the end-time of the last frame, so backends can calculate
        # frame durations.
        self._animation[frames[-1]]

    def autorender(self, enable):
        """Enable / disable canvas autorendering.

        Autorendering - which is enabled by default when a canvas is created -
        controls how the canvas should be displayed automatically without
        caller intervention in certain interactive environments, such as Jupyter
        notebooks.

        Note that autorendering is disabled when a canvas is explicitly
        shown using any of the rendering backends.

        Parameters
        ----------
        enable: boolean
          Turn autorendering on / off.
        """
        if enable:
            if self not in Canvas._autorender_list:
                Canvas._autorender_list.append(self)
        else:
            if self in Canvas._autorender_list:
                Canvas._autorender_list.remove(self)

    def axes(
            self,
            bounds=None,
            rect=None,
            corner=None,
            grid=None,
            gutter=50,
            xmin=None,
            xmax=None,
            ymin=None,
            ymax=None,
            show=True,
            xshow=True,
            yshow=True,
            label=None,
            xlabel=None,
            ylabel=None,
            xticklocator=None,
            yticklocator=None,
            xscale="linear",
            yscale="linear",
            palette=None,
            padding=10,
            tick_length=5):
        """Add a set of 2D axes to the canvas.

        Parameters
        ----------
        xmin, xmax, ymin, ymax: float, optional
          Used to explicitly override the axis domain (normally, the domain is
          implicitly defined by any marks added to the axes).
        show: bool, optional
          Set to `False` to hide both axes (the axes contents will still be visible).
        xshow, yshow: bool, optional
          Set to `False` to hide either axis.
        label: string, optional
          Human-readable label placed above the axes.
        xlabel, ylabel: string, optional
          Human-readable axis label.
        xticklocator, yticklocator: :class:`toyplot.locator.TickLocator`, optional
          Controls the placement and formatting of axis ticks and tick labels.
        xscale, yscale: "linear", "log", "log10", "log2", or a ("log", <base>) tuple, optional
          Specifies the mapping from data to canvas coordinates along an axis.
        palette: :class:`toyplot.color.Palette`, optional
          Color palette used to automatically select per-series colors for plotted data.
        padding: number, string, or (number, string) tuple,  optional
          Distance between the axes and plotted data.  Assumes CSS pixels if units aren't provided.
          See :ref:`units` for details on how Toyplot handles real-world units.
        tick_length: :ref:`units`, optional
          Length of axes ticks, defaults to CSS pixel units.

        Returns
        -------
        axes: :class:`toyplot.axes.Cartesian`
        """
        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
        self._children.append(
            toyplot.axes.Cartesian(
                xmin_range,
                xmax_range,
                ymin_range,
                ymax_range,
                xmin=xmin,
                xmax=xmax,
                ymin=ymin,
                ymax=ymax,
                show=show,
                xshow=xshow,
                yshow=yshow,
                label=label,
                xlabel=xlabel,
                ylabel=ylabel,
                xticklocator=xticklocator,
                yticklocator=yticklocator,
                xscale=xscale,
                yscale=yscale,
                palette=palette,
                padding=padding,
                tick_length=tick_length,
                parent=self))
        return self._children[-1]

    def legend(
            self,
            marks,
            bounds=None,
            rect=None,
            corner=None,
            grid=None,
            gutter=50,
            style=None,
            label_style=None):
        """Add a legend to the canvas.

        Parameters
        ----------
        marks: sequence of marks to add to the legend
          Each mark to be displayed in the legend should be specified using either
          a (label, mark) tuple or a (label, mark, style) tuple.  Each label should
          be the human-readable text to be displayed next to the mark.  The mark
          can be a string value "line" or "rect", a marker string "o", "s", "^",
          or an actual intance of :class:`toyplot.mark.Mark`.
        bounds: (xmin, xmax, ymin, ymax) tuple, optional
          Use the bounds property to position / size the legend by specifying the
          position of each of its boundaries.  The boundaries may be specified in
          absolute drawing units, or as a percentage of the canvas width / height
          using strings that end with "%".
        rect: (x, y, width, height) tuple, optional
          Use the rect property to position / size the legend by specifying its
          upper-left-hand corner, width, and height.  Each parameter may be specified
          in absolute drawing units, or as a percentage of the canvas width / height
          using strings that end with "%".
        corner: (corner, width, height, inset) tuple, optional
          Use the corner property to position / size the legend by specifying its
          width and height, plus an inset from a corner of the canvas.  Allowed
          corner values are "top-left", "top", "top-right", "right",
          "bottom-right", "bottom", "bottom-left", and "left".  The width and
          height may be specified in absolute drawing units, or as a percentage of
          the canvas width / height using strings that end with "%".  The inset is
          specified in absolute drawing units.
        grid: (rows, columns, index) tuple, or (rows, columns, i, j) tuple, or (rows, columns, i, rowspan, j, columnspan) tuple, optional
          Use the grid property to position / size the legend using a collection of
          grid cells filling the canvas.  Specify the number of rows and columns in
          the grid, then specify either a zero-based cell index (which runs in
          left-ot-right, top-to-bottom order), a pair of i, j cell coordinates, or
          a set of i, column-span, j, row-span coordinates so the legend can cover
          more than one cell.
        gutter: size of the gutter around grid cells, optional
          Specifies the amount of empty space to leave between grid cells When using the
          `grid` parameter to position the legend.
        style: dict, optional
        id: string, optional

        Returns
        -------
        legend: :class:`toyplot.mark.Legend`
        """
        gutter = toyplot.require.scalar(gutter)
        style = toyplot.style.combine(toyplot.require.style(style))
        label_style = toyplot.style.combine(toyplot.require.style(label_style))

        xmin, xmax, ymin, ymax = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
        self._children.append(
            toyplot.mark.Legend(
                xmin,
                xmax,
                ymin,
                ymax,
                marks,
                style,
                label_style))
        return self._children[-1]

    def matrix(
            self,
            matrix,
            label=None,
            step=1,
            colormap=None,
            palette=None,
            bounds=None,
            rect=None,
            corner=None,
            grid=None,
            gutter=50):
        """Add a matrix visualization to the canvas.

        Parameters
        ----------

        Returns
        -------
        axes: :class:`toyplot.axes.Table`
        """
        matrix = toyplot.require.scalar_matrix(matrix)

        if colormap is None:
            if palette is None:
                palette = toyplot.color.brewer("BlueRed")
            colormap = toyplot.color.LinearMap(
                palette, matrix.min(), matrix.max())

        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
        table = toyplot.axes.Table(
            xmin_range,
            xmax_range,
            ymin_range,
            ymax_range,
            trows=1,
            brows=0,
            lcols=1,
            rcols=0,
            rows=matrix.shape[0],
            columns=matrix.shape[1],
            label=label,
            parent=self)

        table.top.row(0).height = 20
        table.left.column(0).width = 20

        table.left.column(0).align = "right"
        for i, label, title in zip(
                *toyplot.locator.Integer(step=step).ticks(0, matrix.shape[0] - 1)):
            table.left.cell(i, 0).data = label
            #table.left.cell(i, 0).title = title

        for j, label, title in zip(
                *toyplot.locator.Integer(step=step).ticks(0, matrix.shape[1] - 1)):
            table.top.cell(0, j).data = label
            #table.top.cell(0, j).title = title

        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                cell = table.body.cell(i, j)
                cell.bstyle = {"stroke": "none", "fill": colormap.css(value)}
                cell.title = value

        self._children.append(table)
        return table

    def table(
            self,
            data=None,
            rows=None,
            columns=None,
            hrows=None,
            brows=None,
            lcols=None,
            rcols=None,
            label=None,
            bounds=None,
            rect=None,
            corner=None,
            grid=None,
            gutter=50):
        """Add a set of table axes to the canvas.

        Parameters
        ----------

        Returns
        -------
        axes: :class:`toyplot.axes.Table`
        """
        if data is not None:
            data = toyplot.data.Table(data)
            rows = data.shape[0] if rows is None else max(rows, data.shape[0])
            columns = data.shape[1] if columns is None else max(
                columns, data.shape[1])
            if hrows is None:
                hrows = 1
        if rows is None or columns is None:
            raise ValueError("You must specify data, or rows and columns.")
        if hrows is None:
            hrows = 0
        if brows is None:
            brows = 0
        if lcols is None:
            lcols = 0
        if rcols is None:
            rcols = 0

        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
        table = toyplot.axes.Table(
            xmin_range,
            xmax_range,
            ymin_range,
            ymax_range,
            rows=rows,
            columns=columns,
            label=label,
            trows=hrows,
            brows=brows,
            lcols=lcols,
            rcols=rcols,
            parent=self)

        if data is not None:
            for index, (key, column) in enumerate(data.items()):
                if hrows:
                    table.header.cell(hrows - 1, index).data = key
                table.body.column(index).data = column
                if issubclass(column._data.dtype.type, numpy.floating):
                    if hrows:
                        table.header.cell(0, index).align = "center"
                    table.body.column(
                        index).format = toyplot.format.FloatFormatter()
                    table.body.column(index).align = "separator"
                elif issubclass(column._data.dtype.type, numpy.character):
                    table.column(index).align = "left"
                elif issubclass(column._data.dtype.type, numpy.integer):
                    table.column(index).align = "right"

        # Enable a single horizontal line between header and body.
        if hrows:
            table.grid.hlines[hrows] = "single"

        self._children.append(table)
        return table

    def text(
            self,
            x,
            y,
            text,
            angle=0.0,
            fill=None,
            colormap=None,
            palette=None,
            opacity=1.0,
            title=None,
            style=None):
        """Add text to the canvas.

        Parameters
        ----------
        x, y: float
          Coordinates of the text anchor in canvas drawing units.  Note that canvas
          Y coordinates increase from top-to-bottom.
        text: string
          The text to be displayed.
        title: string, optional
          Human-readable title for the mark.  The SVG / HTML backends render the
          title as a tooltip.
        style: dict, optional
          Collection of CSS styles to apply to the mark.  See
          :class:`toyplot.mark.Text` for a list of useful styles.

        Returns
        -------
        text: :class:`toyplot.mark.Text`
        """
        table = toyplot.data.Table()
        table["x"] = toyplot.require.scalar_vector(x)
        table["y"] = toyplot.require.scalar_vector(y, table.shape[0])
        table["text"] = toyplot.broadcast.object(text, table.shape[0])
        table["angle"] = toyplot.broadcast.scalar(angle, table.shape[0])
        table["fill"] = toyplot.broadcast.object(fill, table.shape[0])
        table["toyplot:fill"] = toyplot.color.broadcast(
            toyplot.color.near_black if fill is None else fill,
            table.shape[0],
            colormap=colormap,
            palette=palette)
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.object(title, table.shape[0])
        style = toyplot.style.combine(
            {
                "font-weight": "normal",
                "stroke": "none",
                "text-anchor": "middle",
                "alignment-baseline": "middle"},
            toyplot.require.style(style))

        self._children.append(
            toyplot.mark.Text(
                table=table,
                coordinates=[
                    "x",
                    "y"],
                axes=[
                    "x",
                    "y"],
                text="text",
                angle="angle",
                fill="toyplot:fill",
                opacity="opacity",
                title="title",
                style=style))
        return self._children[-1]

    def time(self, begin, end, index=None):
        """Return a :class:`toyplot.canvas.AnimationFrame` with the given start and end time, ready to store animated canvas modifications.

        Parameters
        ----------
        begin: scalar
          Specify the frame start time (in seconds).
        end: scalar
          Specify the frame end time (in seconds).
        index: integer, optional
          Specify an index for this frame.  Note that the index is simply a
          convenience for code that depends on accessing the index from the
          result AnimationFrame.

        Returns
        -------
        frame: :class:`toyplot.canvas.AnimationFrame` instance.
        """
        if index is None:
            index = 0
        return AnimationFrame(index, begin, end, self._animation)

    def _pixel_scale(self, width=None, height=None, scale=None):
        """Return a scale factor to convert this canvas to a target width or height in pixels."""
        if numpy.count_nonzero(
                [width is not None, height is not None, scale is not None]) > 1:
            raise ValueError("Specify only one of width, height, or scale.")
        if width is not None:
            scale = width / self._width
        elif height is not None:
            scale = height / self._height
        elif scale is None:
            scale = 1.0
        return scale

    def _point_scale(self, width=None, height=None, scale=None):
        """Return a scale factor to convert this canvas to a target width or height in points."""
        if numpy.count_nonzero(
                [width is not None, height is not None, scale is not None]) > 1:
            raise ValueError("Specify only one of width, height, or scale.")

        if width is not None:
            scale = toyplot.units.convert(
                width, "pt") / toyplot.units.convert((self._width, "px"), "pt")
        elif height is not None:
            scale = toyplot.units.convert(
                height, "pt") / toyplot.units.convert((self._height, "px"), "pt")
        elif scale is None:
            scale = 1.0
        scale *= 72.0 / 96.0
        return scale

    @staticmethod
    def _ipython_post_execute():  # pragma: no cover
        try:
            import IPython.display
            for canvas in [canvas for canvas in Canvas._autorender_list]:
                IPython.display.display(canvas)
        except:
            pass

    @staticmethod
    def _ipython_register():  # pragma: no cover
        try:
            import IPython
            if IPython.get_ipython():
                IPython.get_ipython().events.register(
                    "post_execute", Canvas._ipython_post_execute)
        except:
            pass

Canvas._autorender_list = []
Canvas._ipython_register()
