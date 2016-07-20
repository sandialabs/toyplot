# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import numbers
import numpy
import toyplot.coordinates
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
        if not isinstance(mark, (
                toyplot.mark.BarBoundaries,
                toyplot.mark.BarMagnitudes,
                toyplot.mark.Plot,
                toyplot.mark.Scatterplot,
                toyplot.mark.Text,
            )):
            raise ValueError("Cannot set datum style for %s." % type(mark))
        self._changes[self._begin][
            "set-datum-style"].append((mark, series, datum, style))


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

    class _AnimationFrames(collections.defaultdict):
        def __init__(self):
            collections.defaultdict.__init__(self, lambda: collections.defaultdict(list))

    def __init__(self, width=None, height=None, style=None, autorender=None, autoformat=None):
        self._width = toyplot.units.convert(
            width, "px", default="px") if width is not None else 600
        self._height = toyplot.units.convert(
            height, "px", default="px") if height is not None else self._width
        self._style = {
            "background-color": "transparent",
            "fill": toyplot.color.near_black,
            "fill-opacity": 1.0,
            "font-family": "Helvetica",
            "font-size": "12px",
            "opacity": 1.0,
            "stroke": toyplot.color.near_black,
            "stroke-opacity": 1.0,
            "stroke-width": 1.0,
        }
        self.style = style

        self._animation = toyplot.Canvas._AnimationFrames()
        self._children = []
        self.autorender(autorender, autoformat)

    def _repr_html_(self):
        import toyplot.html
        import xml.etree.ElementTree as xml
        return toyplot.compatibility.unicode_type(
            xml.tostring(
                toyplot.html.render(self),
                encoding="utf-8",
                method="html"),
            encoding="utf-8")

    def _repr_png_(self):
        import toyplot.png
        return toyplot.png.render(self)

    @property
    def height(self):
        """Height of the canvas in CSS pixels."""
        return self._height

    @property
    def style(self):
        """Canvas style."""
        return self._style

    @style.setter
    def style(self, value):
        self._style = toyplot.style.combine(
            self._style,
            toyplot.require.style(value, allowed=set(["background-color", "border"])),
            )

    @property
    def width(self):
        """Width of the canvas in CSS pixels."""
        return self._width

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

    def autorender(self, enable=None, autoformat=None):
        """Enable / disable canvas autorendering.

        Autorendering - which is enabled by default when a canvas is created -
        controls how the canvas should be displayed automatically without
        caller intervention in certain interactive environments, such as Jupyter
        notebooks.

        Note that autorendering is disabled when a canvas is explicitly
        shown using any of the rendering backends.

        Parameters
        ----------
        enable: boolean, optional
            Turn autorendering on / off.  Defaults to the value at toyplot.config.autorender.
        format: string, optional
            Specify the format ("html" or "png") to be used for autorendering.  Defaults to the value at toyplot.config.autoformat.
        """
        if enable is None:
            enable = toyplot.config.autorender
        if autoformat is None:
            autoformat = toyplot.config.autoformat

        Canvas._autorender = [entry for entry in Canvas._autorender if entry[0] != self]
        if enable:
            Canvas._autorender.append((self, autoformat))

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
            aspect=None,
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
            padding=10,
        ):

        toyplot.log.warning("toyplot.canvas.Canvas.axes() is deprecated, use toyplot.canvas.Canvas.cartesian() instead.")

        return self.cartesian(
            bounds=bounds,
            rect=rect,
            corner=corner,
            grid=grid,
            gutter=gutter,
            xmin=xmin,
            xmax=xmax,
            ymin=ymin,
            ymax=ymax,
            aspect=aspect,
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
            padding=padding,
            )

    def cartesian(
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
            aspect=None,
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
            padding=10,
        ):
        """Add a set of Cartesian axes to the canvas.

        Parameters
        ----------
        bounds: (xmin, xmax, ymin, ymax) tuple, optional
          Use the bounds property to position / size the axes by specifying the
          position of each of its boundaries.  Assumes CSS pixels if units
          aren't provided, and supports all units described in :ref:`units`,
          including percentage of the canvas width / height.
        rect: (x, y, width, height) tuple, optional
          Use the rect property to position / size the axes by specifying its
          upper-left-hand corner, width, and height.  Assumes CSS pixels if
          units aren't provided, and supports all units described in
          :ref:`units`, including percentage of the canvas width / height.
        corner: (corner, inset, width, height) tuple, optional
          Use the corner property to position / size the axes by specifying its
          width and height, plus an inset from a corner of the canvas.  Allowed
          corner values are "top-left", "top", "top-right", "right",
          "bottom-right", "bottom", "bottom-left", and "left".  The width and
          height may be specified using absolute units as described in
          :ref:`units`, or as a percentage of the canvas width / height.  The
          inset only supports absolute drawing units.  All units default to CSS
          pixels if unspecified.
        grid: (rows, columns, index) tuple, or (rows, columns, i, j) tuple, or (rows, columns, i, rowspan, j, columnspan) tuple, optional
          Use the grid property to position / size the axes using a collection of
          grid cells filling the canvas.  Specify the number of rows and columns in
          the grid, then specify either a zero-based cell index (which runs in
          left-ot-right, top-to-bottom order), a pair of i, j cell coordinates, or
          a set of i, column-span, j, row-span coordinates so the legend can cover
          more than one cell.
        gutter: size of the gutter around grid cells, optional
          Specifies the amount of empty space to leave between grid cells When using the
          `grid` parameter for positioning.  Assumes CSS pixels by default, and supports
          all of the absolute units described in :ref:`units`.
        xmin, xmax, ymin, ymax: float, optional
          Used to explicitly override the axis domain (normally, the domain is
          implicitly defined by any marks added to the axes).
        aspect: string, optional
          Set to "fit-range" to automatically expand the domain so that its
          aspect ratio matches the aspect ratio of the range.
        show: bool, optional
          Set to `False` to hide the axes (the axes contents will still be visible).
        xshow, yshow: bool, optional
          Set to `False` to hide individual axes.
        label: string, optional
          Human-readable axes label.
        xlabel, ylabel: string, optional
          Human-readable axis labels.
        xticklocator, yticklocator: :class:`toyplot.locator.TickLocator`, optional
          Controls the placement and formatting of axis ticks and tick labels.
        xscale, yscale: "linear", "log", "log10", "log2", or a ("log", <base>) tuple, optional
          Specifies the mapping from data to canvas coordinates along an axis.
        padding: number, string, or (number, string) tuple,  optional
          Distance between the axes and plotted data.  Assumes CSS pixels if units aren't provided.
          See :ref:`units` for details on how Toyplot handles real-world units.

        Returns
        -------
        axes: :class:`toyplot.coordinates.Cartesian`
        """
        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
        self._children.append(
            toyplot.coordinates.Cartesian(
                xmin_range,
                xmax_range,
                ymin_range,
                ymax_range,
                aspect=aspect,
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
                padding=padding,
                parent=self))

        return self._children[-1]

    def legend(
            self,
            entries,
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
        entries: sequence of entries to add to the legend Each entry to be
            displayed in the legend must be either a (label, mark) tuple or a
            (label, marker) tuple.  Labels are human-readable text, markers are
            specified using the syntax described in :ref:`markers`, and marks can
            be any instance of :class:`toyplot.mark.Mark`.
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
        corner: (corner, inset, width, height) tuple, optional
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
        style = toyplot.require.style(style, allowed=toyplot.require.style.fill)
        label_style = toyplot.require.style(label_style, allowed=toyplot.require.style.text)

        xmin, xmax, ymin, ymax = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
        self._children.append(
            toyplot.mark.Legend(
                xmin,
                xmax,
                ymin,
                ymax,
                entries,
                style,
                label_style))
        return self._children[-1]

    def matrix(
            self,
            data,
            label=None,
            tlabel=None,
            llabel=None,
            rlabel=None,
            blabel=None,
            step=1,
            tshow=None,
            lshow=None,
            rshow=None,
            bshow=None,
            tlocator=None,
            llocator=None,
            rlocator=None,
            blocator=None,
            colorshow=False,
            bounds=None,
            rect=None,
            corner=None,
            grid=None,
            gutter=50,
            filename=None,
            ):
        """Add a matrix visualization to the canvas.

        Parameters
        ----------

        Returns
        -------
        axes: :class:`toyplot.coordinates.Table`
        """
        if isinstance(data, tuple):
            matrix = toyplot.require.scalar_matrix(data[0])
            colormap = toyplot.require.instance(data[1], toyplot.color.Map)
        else:
            matrix = toyplot.require.scalar_matrix(data)
            palette = toyplot.color.brewer.palette("BlueRed")
            colormap = toyplot.color.LinearMap(
                palette=palette,
                domain_min=matrix.min(),
                domain_max=matrix.max(),
                )

        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)

        table = toyplot.coordinates.Table(
            xmin_range,
            xmax_range,
            ymin_range,
            ymax_range,
            trows=2,
            brows=2,
            lcolumns=2,
            rcolumns=2,
            rows=matrix.shape[0],
            columns=matrix.shape[1],
            label=label,
            parent=self,
            filename=filename,
            )

        table.top.row[[0, 1]].height = 20
        table.bottom.row[[0, 1]].height = 20
        table.left.column[[0, 1]].width = 20
        table.right.column[[0, 1]].width = 20

        table.left.column[1].align = "right"
        table.right.column[0].align = "left"

        table.cells.column[[0, -1]].lstyle = {"font-weight":"bold"}
        table.cells.row[[0, -1]].lstyle = {"font-weight":"bold"}

        if tlabel is not None:
            cell = table.top.row[0].merge()
            cell.data = tlabel

        if llabel is not None:
            cell = table.left.column[0].merge()
            cell.data = llabel
            cell.angle = 90

        if rlabel is not None:
            cell = table.right.column[1].merge()
            cell.data = rlabel
            cell.angle = 90

        if blabel is not None:
            cell = table.bottom.row[1].merge()
            cell.data = blabel

        if tshow is None:
            tshow = True
        if tshow:
            if tlocator is None:
                tlocator = toyplot.locator.Integer(step=step)
            for j, label, title in zip(*tlocator.ticks(0, matrix.shape[1] - 1)):
                table.top.cell[1, j].data = label
                #table.top.cell[1, j].title = title

        if lshow is None:
            lshow = True
        if lshow:
            if llocator is None:
                llocator = toyplot.locator.Integer(step=step)
            for i, label, title in zip(*llocator.ticks(0, matrix.shape[0] - 1)):
                table.left.cell[i, 1].data = label
                #table.left.cell[i, 1].title = title

        if rshow is None and rlocator is not None:
            rshow = True
        if rshow:
            if rlocator is None:
                rlocator = toyplot.locator.Integer(step=step)
            for i, label, title in zip(*rlocator.ticks(0, matrix.shape[0] - 1)):
                table.right.cell[i, 0].data = label
                #table.right.cell[i, 0].title = title

        if bshow is None and blocator is not None:
            bshow = True
        if bshow:
            if blocator is None:
                blocator = toyplot.locator.Integer(step=step)
            for j, label, title in zip(*blocator.ticks(0, matrix.shape[1] - 1)):
                table.bottom.cell[0, j].data = label
                #table.bottom.cell[0, j].title = title

        table.body.cells.data = matrix
        table.body.cells.format = toyplot.format.NullFormatter()

        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                cell = table.body.cell[i, j]
                cell.style = {"stroke": "none", "fill": colormap.css(value)}
                cell.title = value

        self._children.append(table)

        if colorshow:
            axis = self.color_scale(
                colormap=colormap,
                x1=xmax_range,
                y1=ymax_range,
                x2=xmax_range,
                y2=ymin_range,
                width=10,
                padding=10,
                show=True,
                label="",
                ticklocator=None,
                scale="linear",
                )

        return table

    def color_scale(
            self,
            colormap,
            x1=None,
            y1=None,
            x2=None,
            y2=None,
            width=10,
            bounds=None,
            rect=None,
            corner=None,
            grid=None,
            gutter=50,
            min=None,
            max=None,
            show=True,
            label=None,
            ticklocator=None,
            scale="linear",
            padding=10,
        ):
        """Add a color scale to the canvas.

        The color scale displays a mapping from scalar values to colors, for
        the given colormap.  Note that the supplied colormap must have an
        explicitly defined domain (specified when the colormap was created),
        otherwise the mapping would be undefined.

        Parameters
        ----------
        colormap: :class:`toyplot.color.Map`, required
          Colormap to be displayed.
        min, max: float, optional
          Used to explicitly override the domain that will be shown.
        show: bool, optional
          Set to `False` to hide the axis (the color bar will still be visible).
        label: string, optional
          Human-readable label placed below the axis.
        ticklocator: :class:`toyplot.locator.TickLocator`, optional
          Controls the placement and formatting of axis ticks and tick labels.
        scale: "linear", "log", "log10", "log2", or a ("log", <base>) tuple, optional
          Specifies the mapping from data to canvas coordinates along an axis.

        Returns
        -------
        axes: :class:`toyplot.coordinates.Numberline`
        """
        axes = self.numberline(
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            bounds=bounds,
            rect=rect,
            corner=corner,
            grid=grid,
            gutter=gutter,
            min=min,
            max=max,
            show=show,
            label=label,
            ticklocator=ticklocator,
            scale=scale,
            padding=padding,
            )

        axes.colormap(colormap)

        return axes

    def numberline(
            self,
            x1=None,
            y1=None,
            x2=None,
            y2=None,
            bounds=None,
            rect=None,
            corner=None,
            grid=None,
            gutter=50,
            min=None,
            max=None,
            show=True,
            label=None,
            ticklocator=None,
            scale="linear",
            spacing=None,
            padding=None,
        ):
        """Add a 1D numberline to the canvas.

        Parameters
        ----------
        min, max: float, optional
          Used to explicitly override the numberline domain (normally, the domain is
          implicitly defined by any marks added to the numberline).
        show: bool, optional
          Set to `False` to hide the numberline (the numberline contents will still be visible).
        label: string, optional
          Human-readable label placed below the numberline axis.
        ticklocator: :class:`toyplot.locator.TickLocator`, optional
          Controls the placement and formatting of axis ticks and tick labels.  See :ref:`tick-locators`.
        scale: "linear", "log", "log10", "log2", or a ("log", <base>) tuple, optional
          Specifies the mapping from data to canvas coordinates along the axis.  See :ref:`log-scales`.
        spacing: number, string, or (number, string) tuple,  optional
          Distance between plotted data added to the numberline.  Assumes CSS
          pixels if units aren't provided.  See :ref:`units` for details on how
          Toyplot handles real-world units.
        padding: number, string, or (number, string) tuple,  optional
          Distance between the numberline axis and plotted data.  Assumes CSS
          pixels if units aren't provided.  See :ref:`units` for details on how
          Toyplot handles real-world units.  Defaults to the same value as
          `spacing`.

        Returns
        -------
        axes: :class:`toyplot.coordinates.Cartesian`
        """
        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)

        if x1 is None:
            x1 = xmin_range
        else:
            x1 = toyplot.units.convert(x1, target="px", default="px", reference=self._width)
            if x1 < 0:
                x1 = self._width + x1

        if y1 is None:
            y1 = 0.5 * (ymin_range + ymax_range)
        else:
            y1 = toyplot.units.convert(y1, target="px", default="px", reference=self._height)
            if y1 < 0:
                y1 = self._height + y1

        if x2 is None:
            x2 = xmax_range
        else:
            x2 = toyplot.units.convert(x2, target="px", default="px", reference=self._width)
            if x2 < 0:
                x2 = self._width + x2

        if y2 is None:
            y2 = 0.5 * (ymin_range + ymax_range)
        else:
            y2 = toyplot.units.convert(y2, target="px", default="px", reference=self._height)
            if y2 < 0:
                y2 = self._height + y2

        if spacing is None:
            spacing = 20

        if padding is None:
            padding = spacing

        axes = toyplot.coordinates.Numberline(
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            padding=padding,
            spacing=spacing,
            min=min,
            max=max,
            show=show,
            label=label,
            ticklocator=ticklocator,
            scale=scale,
            parent=self)
        self._children.append(axes)
        return axes

    def table(
            self,
            data=None,
            rows=None,
            columns=None,
            trows=None,
            brows=None,
            lcolumns=None,
            rcolumns=None,
            label=None,
            bounds=None,
            rect=None,
            corner=None,
            grid=None,
            gutter=50,
            filename=None,
            ):
        """Add a set of table axes to the canvas.

        Parameters
        ----------

        Returns
        -------
        axes: :class:`toyplot.coordinates.Table`
        """
        if data is not None:
            data = toyplot.data.Table(data)
            rows = data.shape[0] if rows is None else max(rows, data.shape[0])
            columns = data.shape[1] if columns is None else max(
                columns, data.shape[1])
            if trows is None:
                trows = 1
        if rows is None or columns is None: # pragma: no cover
            raise ValueError("You must specify data, or rows and columns.")
        if trows is None:
            trows = 0
        if brows is None:
            brows = 0
        if lcolumns is None:
            lcolumns = 0
        if rcolumns is None:
            rcolumns = 0

        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
        table = toyplot.coordinates.Table(
            xmin_range,
            xmax_range,
            ymin_range,
            ymax_range,
            rows=rows,
            columns=columns,
            label=label,
            trows=trows,
            brows=brows,
            lcolumns=lcolumns,
            rcolumns=rcolumns,
            parent=self,
            filename=filename,
            )

        if data is not None:
            for j, (key, column) in enumerate(data.items()):
                if trows:
                    table.top.cell[trows - 1, j].data = key
                for i, (value, mask) in enumerate(zip(column, numpy.ma.getmaskarray(column))):
                    if not mask:
                        table.body.cell[i, j].data = value
                if issubclass(column._data.dtype.type, numpy.floating):
                    if trows:
                        table.top.cell[0, j].align = "center"
                    table.body.cell[:,j].format = toyplot.format.FloatFormatter()
                    table.body.cell[:,j].align = "separator"
                elif issubclass(column._data.dtype.type, numpy.character):
                    table.cells.cell[:,j].align = "left"
                elif issubclass(column._data.dtype.type, numpy.integer):
                    table.cells.cell[:,j].align = "right"

            if trows:
                # Format top cells for use as a header
                table.top.cells.lstyle = {"font-weight": "bold"}
                # Enable a single horizontal line between top and body.
                table.cells.grid.hlines[trows] = "single"

        self._children.append(table)
        return table

    def image(
            self,
            data,
            bounds=None,
            rect=None,
            corner=None,
            grid=None,
            gutter=50,
        ):
        """Add an image to the canvas.

        Parameters
        ----------
        data: image, or (image, colormap) tuple
        bounds: (xmin, xmax, ymin, ymax) tuple, optional
          Use the bounds property to position / size the image by specifying the
          position of each of its boundaries.  Assumes CSS pixels if units
          aren't provided, and supports all units described in :ref:`units`,
          including percentage of the canvas width / height.
        rect: (x, y, width, height) tuple, optional
          Use the rect property to position / size the image by specifying its
          upper-left-hand corner, width, and height.  Assumes CSS pixels if
          units aren't provided, and supports all units described in
          :ref:`units`, including percentage of the canvas width / height.
        corner: (corner, inset, width, height) tuple, optional
          Use the corner property to position / size the image by specifying its
          width and height, plus an inset from a corner of the canvas.  Allowed
          corner values are "top-left", "top", "top-right", "right",
          "bottom-right", "bottom", "bottom-left", and "left".  The width and
          height may be specified using absolute units as described in
          :ref:`units`, or as a percentage of the canvas width / height.  The
          inset only supports absolute drawing units.  All units default to CSS
          pixels if unspecified.
        grid: (rows, columns, index) tuple, or (rows, columns, i, j) tuple, or (rows, columns, i, rowspan, j, columnspan) tuple, optional
          Use the grid property to position / size the image using a collection of
          grid cells filling the canvas.  Specify the number of rows and columns in
          the grid, then specify either a zero-based cell index (which runs in
          left-ot-right, top-to-bottom order), a pair of i, j cell coordinates, or
          a set of i, column-span, j, row-span coordinates so the legend can cover
          more than one cell.
        gutter: size of the gutter around grid cells, optional
          Specifies the amount of empty space to leave between grid cells When using the
          `grid` parameter for positioning.  Assumes CSS pixels by default, and supports
          all of the absolute units described in :ref:`units`.
        """
        colormap = None
        palette = None
        if isinstance(data, tuple):
            data, colormap = data
            if not isinstance(colormap, toyplot.color.Map):
                raise ValueError("Expected toyplot.color.Map, received %s." % colormap)
            data = numpy.atleast_3d(data)
            if data.shape[2] != 1:
                raise ValueError("Expected an image with one channel.")
            data = colormap.colors(data)

        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)

        self._children.append(
            toyplot.mark.Image(
                xmin_range,
                xmax_range,
                ymin_range,
                ymax_range,
                data=data,
                ))
        return self._children[-1]

    def text(
            self,
            x,
            y,
            text,
            angle=0.0,
            fill=None,
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
            colors=fill,
            shape=(table.shape[0],),
            default=toyplot.color.near_black,
            )
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.object(title, table.shape[0])
        style = toyplot.require.style(style, allowed=toyplot.require.style.text)

        self._children.append(
            toyplot.mark.Text(
                coordinate_axes=["x", "y"],
                table=table,
                coordinates=["x", "y"],
                text=["text"],
                angle=["angle"],
                fill=["toyplot:fill"],
                opacity=["opacity"],
                title=["title"],
                style=style,
                annotation=True,
                filename=None,
                ))
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

    def _point_scale(self, width=None, height=None, scale=None):
        """Return a scale factor to convert this canvas to a target width or height in points."""
        if numpy.count_nonzero(
                [width is not None, height is not None, scale is not None]) > 1:
            raise ValueError("Specify only one of width, height, or scale.") # pragma: no cover

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
            for canvas, autoformat in Canvas._autorender:
                if autoformat == "html":
                    IPython.display.display_html(canvas)
                elif autoformat == "png":
                    IPython.display.display_png(canvas)
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

Canvas._autorender = []
Canvas._ipython_register()
