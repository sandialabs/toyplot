# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Implements the :class:`toyplot.canvas.Canvas` class, which defines the space that is available for creating plots.
"""


import collections
import numbers

import numpy
import toyplot.coordinates
import toyplot.broadcast
import toyplot.color
import toyplot.config
import toyplot.layout
import toyplot.scenegraph
import toyplot.style
import toyplot.units


class AnimationFrame(object):
    """Used to specify modifications to a `toyplot.canvas.Canvas` for animation.

    Do not create AnimationFrame instances yourself, use
    :meth:`toyplot.canvas.Canvas.frame` and
    :meth:`toyplot.canvas.Canvas.frames` instead.
    """
    def __init__(self, changes, count, number, begin, end):
        self._changes = changes
        self._count = count
        self._number = number
        self._begin = begin
        self._end = end

    @property
    def count(self):
        """Total number of frames in the current animation.
        """
        return self._count

    @property
    def number(self):
        """Current animation frame number (zero-based).
        """
        return self._number

    @property
    def begin(self):
        """Beginning of the current frame in seconds.
        """
        return self._begin

    @property
    def end(self):
        """End of the current frame in seconds.
        """
        return self._end

    @property
    def length(self):
        """Duration of the current frame in seconds.
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

        self._changes.add(self._begin, self._end, "set-mark-style", dict(mark=mark, style=style))

    def set_datum_style(self, mark, series, datum, style):
        """Change the style of one datum in a :class:`toyplot.mark.Mark` at the current frame.

        Parameters
        ----------
        mark: :class:`toyplot.mark.Mark`, required
            Mark containing the datum to modify.
        series: int, required
            Zero-based index of the series containing the datum to modify.
        datum: int, required
            Zero-based index of the datum to modify.
        style: dict, required
            Python dict containing CSS style information to be assigned to the datum.
        """
        if not isinstance(mark, (
                toyplot.mark.BarBoundaries,
                toyplot.mark.BarMagnitudes,
                toyplot.mark.Plot,
                toyplot.mark.Point,
            )):
            raise ValueError("Cannot set datum style for %s." % type(mark))

        self._changes.add(self._begin, self._end, "set-datum-style", dict(mark=mark, series=series, datum=datum, style=style))

    def set_text(self, mark, text, style=None):
        self.set_datum_text(mark, 0, 0, text, style)

    def set_datum_text(self, mark, series, datum, text, style=None):
        """Change the text in a :class:`toyplot.mark.Text` at the current frame.

        Note
        ----
        Currently, animated text completely overwrites the original - thus, it
        cannot inherit style (including color) information, which you will have
        to re-specify explicitly.

        Parameters
        ----------
        mark: :class:`toyplot.mark.Text`, required
            Mark containing the text to modify.
        series: int, required
            Zero-based index of the series containing the datum to modify.
        datum: int, required
            Zero-based index of the datum to modify.
        text: str, required
            String containing the new text to be assigned to the datum.
        style: dict, optional
            Python dict containing CSS style information to be assigned to the datum.
        angle: float, optional
            Angle for the new text.
        """
        if not isinstance(mark, toyplot.mark.Text):
            raise ValueError("mark must be an instance of toyplot.mark.Text.")
        if not isinstance(series, int):
            raise ValueError("series must be an integer index.")
        if not isinstance(datum, int):
            raise ValueError("datum must be an integer index.")
        if not isinstance(text, str):
            raise ValueError("text must be a string.")
        if not isinstance(style, (dict, type(None))):
            raise ValueError("style must be a dict or None.")

        self._changes.add(self._begin, self._end, "set-datum-text", dict(mark=mark, series=series, datum=datum, text=text, style=style))


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
    hyperlink: string, optional
        When specified, the entire canvas is hyperlinked to the given URI.
        Note that hyperlinks set on other entities (such as axes, marks, or
        text) will override this.
    autorender: boolean, optional
        Turn autorendering on / off for this canvas.  Defaults to the value in
        :data:`toyplot.config.autorender`.
    autoformat: string, optional
        Specify the format ("html" or "png") to be used for autorendering this
        canvas.  Defaults to the value in :data:`toyplot.config.autoformat`.

    Examples
    --------

    The following would create a Canvas 8 inches wide and 6 inches tall, with a yellow background:

    >>> canvas = toyplot.Canvas("8in", "6in", style={"background-color":"yellow"})
    """

    class _AnimationChanges(object):
        def __init__(self):
            self._begin = []
            self._end = []
            self._change = []
            self._state = []

        def add(self, begin, end, change, state):
            self._begin.append(begin)
            self._end.append(end)
            self._change.append(change)
            self._state.append(state)

    def __init__(self, width=None, height=None, style=None, hyperlink=None, autorender=None, autoformat=None):
        if width is None:
            width = toyplot.config.width
        if height is None:
            height = toyplot.config.height
        self._width = toyplot.units.convert(width, "px", default="px") if width is not None else 600
        self._height = toyplot.units.convert(height, "px", default="px") if height is not None else self._width
        self._hyperlink = None
        self._style = {
            "background-color": "transparent",
            "border-color": toyplot.color.black,
            "border-style": "none",
            "border-width": 1.0,
            "fill": toyplot.color.black,
            "fill-opacity": 1.0,
            "font-family": "Helvetica",
            "font-size": "12px",
            "opacity": 1.0,
            "stroke": toyplot.color.black,
            "stroke-opacity": 1.0,
            "stroke-width": 1.0,
        }

        self.hyperlink = hyperlink
        self.style = style

        self._changes = toyplot.Canvas._AnimationChanges()
        self._scenegraph = toyplot.scenegraph.SceneGraph()
        self.autorender(autorender, autoformat)

    def _repr_html_(self):
        from . import html
        return toyplot.html.tostring(self, style={"text-align":"center"})

    def _repr_png_(self):
        from . import png
        return toyplot.png.render(self)

    @property
    def height(self):
        """Height of the canvas in CSS pixels."""
        return self._height

    @height.setter
    def height(self, value):
        self._height = toyplot.units.convert(value, "px", default="px")

    @property
    def hyperlink(self):
        """URI that will be hyperlinked from the entire canvas."""
        return self._hyperlink

    @hyperlink.setter
    def hyperlink(self, value):
        self._hyperlink = toyplot.require.hyperlink(value)

    @property
    def style(self):
        """Collection of CSS styles that will be applied to the canvas."""
        return self._style

    @style.setter
    def style(self, value):
        self._style = toyplot.style.combine(
            self._style,
            toyplot.style.require(value, allowed=set(["background-color", "border-color", "border-style", "border-width"])),
            )

    @property
    def width(self):
        """Width of the canvas in CSS pixels."""
        return self._width

    @width.setter
    def width(self, value):
        self._width = toyplot.units.convert(value, "px", default="px")


    def frame(self, begin, end=None, number=None, count=None):
        """Return a single animation frame that can be used to animate the canvas contents.

        Parameters
        ----------
        begin: float
          Specify the frame start time (in seconds).
        end: float, optional
          Specify the frame end time (in seconds).
        number: integer, optional
          Specify a number for this frame.
        count: integer, optional
          Specify the total number of frames of which this frame is one.

        Returns
        -------
        frame: :class:`toyplot.canvas.AnimationFrame` instance.
        """
        if end is None:
            end = begin + (1.0 / 30.0)
        if number is None:
            number = 0
        if count is None:
            count = 1
        return AnimationFrame(changes=self._changes, count=count, number=number, begin=begin, end=end)


    def frames(self, frames):
        """Return a sequence of animation frames that can be used to animate the canvas contents.

        Parameters
        ----------
        frames: integer, tuple, or sequence
          Pass a sequence of values that specify the time (in seconds) of the
          beginning / end of each frame.  Note that the number of frames will be the
          length of the sequence minus one.  Alternatively, you can pass a 2-tuple
          containing the number of frames and the frame rate in frames-per-second.
          Finally, you may simply specify the number of frames, in which case the
          rate will default to 30 frames-per-second.

        Yields
        ------
        frames: :class:`toyplot.canvas.AnimationFrame`
            Use the methods and properties of each frame object to modify the
            state of the canvas over time.
        """
        if isinstance(frames, numbers.Integral):
            frames = (frames, 30.0)

        if isinstance(frames, tuple):
            frame_count, frame_rate = frames
            times = numpy.linspace(0, frame_count / frame_rate, frame_count + 1, endpoint=True)

        for index, (begin, end) in enumerate(zip(times[:-1], times[1:])):
            yield AnimationFrame(changes=self._changes, count=frame_count, number=index, begin=begin, end=end)


    def animation(self):
        """Return a summary of the canvas animation state.

        Returns
        -------
        begin: float
            Start-time of the animation in seconds.
        end: float
            End-time of the animation in seconds.
        changes: object
            Opaque collection of data structures that describe changes to the
            canvas state during animation (if any).
        """

        begin = 0.0
        end = numpy.max(self._changes._end) if self._changes._end else 0.0
        changes = collections.defaultdict(lambda: collections.defaultdict(list))
        for begin, change, state in zip(self._changes._begin, self._changes._change, self._changes._state):
            changes[begin][change].append(state)

        return begin, end, changes


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
            Turn autorendering on / off for this canvas.  Defaults to the value
            in :data:`toyplot.config.autorender`.
        format: string, optional
            Specify the format ("html" or "png") to be used for autorendering
            this canvas.  Defaults to the value in
            :data:`toyplot.config.autoformat`.
        """
        if enable is None:
            enable = toyplot.config.autorender
        if autoformat is None:
            autoformat = toyplot.config.autoformat

        Canvas._autorender = [entry for entry in Canvas._autorender if entry[0] != self]
        if enable:
            Canvas._autorender.append((self, autoformat))

    def cartesian(
            self,
            aspect=None,
            bounds=None,
            corner=None,
            grid=None,
            hyperlink=None,
            label=None,
            margin=50,
            padding=10,
            palette=None,
            rect=None,
            show=True,
            xlabel=None,
            xmax=None,
            xmin=None,
            xscale="linear",
            xshow=True,
            xticklocator=None,
            ylabel=None,
            ymax=None,
            ymin=None,
            yscale="linear",
            yshow=True,
            yticklocator=None,
        ):
        """Add a set of Cartesian axes to the canvas.

        See Also
        --------
        :ref:`cartesian-coordinates`

        Parameters
        ----------
        aspect: string, optional
            Set to "fit-range" to automatically expand the domain so that its
            aspect ratio matches the aspect ratio of the range.
        bounds: (xmin, xmax, ymin, ymax) tuple, optional
            Use the bounds property to position / size the axes by specifying the
            position of each of its boundaries.  Assumes CSS pixels if units
            aren't provided, and supports all units described in :ref:`units`,
            including percentage of the canvas width / height.
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
        hyperlink: string, optional
            When specified, the range (content area of the axes) is hyperlinked
            to the given URI.  Note that this overrides the canvas hyperlink,
            if any, and is overridden by hyperlinks set on other entities such
            as marks or text.
        label: string, optional
            Human-readable axes label.
        margin: number, (top, side) tuple, (top, side, bottom) tuple, or (top, right, bottom, left) tuple, optional
            Specifies the amount of empty space to leave between the axes
            contents and the containing grid cell When using the `grid`
            parameter for positioning.  Assumes CSS pixels by default, and
            supports all of the absolute units described in :ref:`units`.
        padding: number, string, or (number, string) tuple,  optional
            Distance between the axes and plotted data.  Assumes CSS pixels if units aren't provided.
            See :ref:`units` for details on how Toyplot handles real-world units.
        palette: :class:`toyplot.color.Palette`, optional
            Specifies a palette to be used when automatically assigning per-series colors.
        rect: (x, y, width, height) tuple, optional
            Use the rect property to position / size the axes by specifying its
            upper-left-hand corner, width, and height.  Assumes CSS pixels if
            units aren't provided, and supports all units described in
            :ref:`units`, including percentage of the canvas width / height.
        show: bool, optional
            Set to `False` to hide the axes (the axes contents will still be visible).
        xmin, xmax, ymin, ymax: float, optional
            Used to explicitly override the axis domain (normally, the domain is
            implicitly defined by the marks added to the axes).
        xshow, yshow: bool, optional
            Set to `False` to hide individual axes.
        xlabel, ylabel: string, optional
            Human-readable axis labels.
        xticklocator, yticklocator: :class:`toyplot.locator.TickLocator`, optional
            Controls the placement and formatting of axis ticks and tick labels.
        xscale, yscale: "linear", "log", "log10", "log2", or a ("log", <base>) tuple, optional
            Specifies the mapping from data to canvas coordinates along an
            axis.  See :ref:`log-scales` for examples.

        Returns
        -------
        axes: :class:`toyplot.coordinates.Cartesian`
        """
        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height,
            bounds=bounds,
            rect=rect,
            corner=corner,
            grid=grid,
            margin=margin,
            )

        axes = toyplot.coordinates.Cartesian(
            aspect=aspect,
            hyperlink=hyperlink,
            label=label,
            padding=padding,
            palette=palette,
            scenegraph=self._scenegraph,
            show=show,
            xaxis=None,
            xlabel=xlabel,
            xmax=xmax,
            xmax_range=xmax_range,
            xmin=xmin,
            xmin_range=xmin_range,
            xscale=xscale,
            xshow=xshow,
            xticklocator=xticklocator,
            ylabel=ylabel,
            yaxis=None,
            ymax=ymax,
            ymax_range=ymax_range,
            ymin=ymin,
            ymin_range=ymin_range,
            yscale=yscale,
            yshow=yshow,
            yticklocator=yticklocator,
            )

        self._scenegraph.add_edge(self, "render", axes)

        return axes

    def legend(
            self,
            entries,
            bounds=None,
            corner=None,
            grid=None,
            label=None,
            margin=50,
            rect=None,
            ):
        """Add a legend to the canvas.

        See Also
        --------
        :ref:`labels-and-legends`

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
        label: str, optional
            Optional human-readable label for the legend.
        margin: number, (top, side) tuple, (top, side, bottom) tuple, or (top, right, bottom, left) tuple, optional
            Specifies the amount of empty space to leave between legend and the
            containing grid cell when using the `grid` parameter for positioning.
        rect: (x, y, width, height) tuple, optional
            Use the rect property to position / size the legend by specifying its
            upper-left-hand corner, width, and height.  Each parameter may be specified
            in absolute drawing units, or as a percentage of the canvas width / height
            using strings that end with "%".

        Returns
        -------
        legend: :class:`toyplot.coordinates.Table`
        """

        xmin, xmax, ymin, ymax = toyplot.layout.region(
            0, self._width, 0, self._height,
            bounds=bounds,
            corner=corner,
            grid=grid,
            margin=margin,
            rect=rect,
            )

        table = toyplot.coordinates.Table(
            annotation=True,
            brows=0,
            columns=2,
            filename=None,
            label=label,
            lcolumns=0,
            scenegraph=self._scenegraph,
            rcolumns=0,
            rows=len(entries),
            trows=0,
            xmax_range=xmax,
            xmin_range=xmin,
            ymax_range=ymax,
            ymin_range=ymin,
            )

        table.cells.column[0].align = "right"
        table.cells.column[1].align = "left"

        for index, (label, spec) in enumerate(entries): # pylint: disable=redefined-argument-from-local
            if isinstance(spec, toyplot.mark.Mark):
                markers = spec.markers
            else:
                markers = [toyplot.marker.convert(spec)]
            text = ""
            for marker in markers:
                if text:
                    text = text + " "
                text = text + marker

            table.cells.cell[index, 0].data = text
            table.cells.cell[index, 1].data = label

        self._scenegraph.add_edge(self, "render", table)

        return table

    def matrix(
            self,
            data,
            blabel=None,
            blocator=None,
            bounds=None,
            bshow=None,
            colorshow=False,
            corner=None,
            filename=None,
            grid=None,
            label=None,
            llabel=None,
            llocator=None,
            lshow=None,
            margin=50,
            rect=None,
            rlabel=None,
            rlocator=None,
            rshow=None,
            step=1,
            tlabel=None,
            tlocator=None,
            tshow=None,
        ):
        """Add a matrix visualization to the canvas.

        See Also
        --------
        :ref:`matrix-visualization`

        Parameters
        ----------
        data: matrix, or (matrix, :class:`toyplot.color.Map`) tuple, required
            The given data will be used to populate the visualization, using either the
            given colormap or a default.
        blabel: str, optional
            Human readable label along the bottom of the matrix.
        blocator: :class:`toyplot.locator.TickLocator`, optional
            Supplies column labels along the bottom of the matrix.
        bounds: (xmin, xmax, ymin, ymax) tuple, optional
            Use the bounds property to position / size the legend by specifying the
            position of each of its boundaries.  The boundaries may be specified in
            absolute drawing units, or as a percentage of the canvas width / height
            using strings that end with "%".
        bshow: bool, optional
            Set to `False` to hide column labels along the bottom of the matrix.
        colorshow: bool, optional
            Set to `True` to add a color scale to the visualization.
        corner: (corner, inset, width, height) tuple, optional
            Use the corner property to position / size the legend by specifying its
            width and height, plus an inset from a corner of the canvas.  Allowed
            corner values are "top-left", "top", "top-right", "right",
            "bottom-right", "bottom", "bottom-left", and "left".  The width and
            height may be specified in absolute drawing units, or as a percentage of
            the canvas width / height using strings that end with "%".  The inset is
            specified in absolute drawing units.
        filename: str, optional
            Supplies a default filename for users who choose to download the
            matrix contents.  Note that users and web browsers are free to
            ignore or override this.
        grid: (rows, columns, index) tuple, or (rows, columns, i, j) tuple, or (rows, columns, i, rowspan, j, columnspan) tuple, optional
            Use the grid property to position / size the legend using a collection of
            grid cells filling the canvas.  Specify the number of rows and columns in
            the grid, then specify either a zero-based cell index (which runs in
            left-ot-right, top-to-bottom order), a pair of i, j cell coordinates, or
            a set of i, column-span, j, row-span coordinates so the legend can cover
            more than one cell.
        label: str, optional
            Optional human-readable label for the matrix.
        llabel: str, optional
            Human readable label along the left side of the matrix.
        llocator: :class:`toyplot.locator.TickLocator`, optional
            Supplies row labels along the left side of the matrix.
        lshow: bool, optional
            Set to `False` to hide row labels along the left side of the matrix.
        margin: number, (top, side) tuple, (top, side, bottom) tuple, or (top, right, bottom, left) tuple, optional
            Specifies the amount of empty space to leave between the matrix and
            the containing grid cell when using the `grid` parameter for
            positioning.
        rect: (x, y, width, height) tuple, optional
            Use the rect property to position / size the legend by specifying its
            upper-left-hand corner, width, and height.  Each parameter may be specified
            in absolute drawing units, or as a percentage of the canvas width / height
            using strings that end with "%".
        rlabel: str, optional
            Human readable label along the right side of the matrix.
        rlocator: :class:`toyplot.locator.TickLocator`, optional
            Supplies row labels along the right side of the matrix.
        rshow: bool, optional
            Set to `False` to hide row labels along the right side of the matrix.
        step: integer, optional
            Specifies the number of rows or columns to skip between indices.
            This is useful when the matrix cells become too small relative to
            the index text.
        tlabel: str, optional
            Human readable label along the top of the matrix.
        tlocator: :class:`toyplot.locator.TickLocator`, optional
            Supplies column labels along the top of the matrix.
        tshow: bool, optional
            Set to `False` to hide column labels along the top of the matrix.

        Returns
        -------
        axes: :class:`toyplot.coordinates.Table`
        """
        if isinstance(data, tuple):
            matrix = toyplot.require.scalar_matrix(data[0])
            colormap = toyplot.require.instance(data[1], toyplot.color.Map)
        else:
            matrix = toyplot.require.scalar_matrix(data)
            colormap = toyplot.color.brewer.map("BlueRed", domain_min=matrix.min(), domain_max=matrix.max())

        colors = colormap.colors(matrix)

        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, margin=margin)

        table = toyplot.coordinates.Table(
            annotation=False,
            brows=2,
            columns=matrix.shape[1],
            filename=filename,
            label=label,
            lcolumns=2,
            scenegraph=self._scenegraph,
            rcolumns=2,
            rows=matrix.shape[0],
            trows=2,
            xmax_range=xmax_range,
            xmin_range=xmin_range,
            ymax_range=ymax_range,
            ymin_range=ymin_range,
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
            for j, label, title in zip(*tlocator.ticks(0, matrix.shape[1] - 1)): # pylint: disable=redefined-argument-from-local
                table.top.cell[1, int(j)].data = label
                #table.top.cell[1, j].title = title

        if lshow is None:
            lshow = True
        if lshow:
            if llocator is None:
                llocator = toyplot.locator.Integer(step=step)
            for i, label, title in zip(*llocator.ticks(0, matrix.shape[0] - 1)): # pylint: disable=redefined-argument-from-local
                table.left.cell[int(i), 1].data = label
                #table.left.cell[i, 1].title = title

        if rshow is None and rlocator is not None:
            rshow = True
        if rshow:
            if rlocator is None:
                rlocator = toyplot.locator.Integer(step=step)
            for i, label, title in zip(*rlocator.ticks(0, matrix.shape[0] - 1)): # pylint: disable=redefined-argument-from-local
                table.right.cell[int(i), 0].data = label
                #table.right.cell[i, 0].title = title

        if bshow is None and blocator is not None:
            bshow = True
        if bshow:
            if blocator is None:
                blocator = toyplot.locator.Integer(step=step)
            for j, label, title in zip(*blocator.ticks(0, matrix.shape[1] - 1)): # pylint: disable=redefined-argument-from-local
                table.bottom.cell[0, int(j)].data = label
                #table.bottom.cell[0, j].title = title

        table.body.cells.data = matrix
        table.body.cells.format = toyplot.format.NullFormatter()

        for i in numpy.arange(matrix.shape[0]):
            for j in numpy.arange(matrix.shape[1]):
                cell = table.body.cell[i, j]
                cell.style = {"stroke": "none", "fill": toyplot.color.to_css(colors[i, j])}
                cell.title = "%.6f" % matrix[i, j]

        self._scenegraph.add_edge(self, "render", table)

        if colorshow:
            self.color_scale(
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
            bounds=None,
            corner=None,
            grid=None,
            label=None,
            margin=50,
            max=None,
            min=None,
            offset=None,
            padding=10,
            rect=None,
            scale="linear",
            show=True,
            ticklocator=None,
            width=10,
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
            bounds=bounds,
            corner=corner,
            grid=grid,
            label=label,
            margin=margin,
            max=max,
            min=min,
            padding=padding,
            palette=None,
            rect=rect,
            scale=scale,
            show=show,
            ticklocator=ticklocator,
            x1=x1,
            x2=x2,
            y1=y1,
            y2=y2,
            )

        axes.colormap(
            colormap=colormap,
            width=width,
            offset=offset,
        )

        return axes

    def numberline(
            self,
            x1=None,
            y1=None,
            x2=None,
            y2=None,
            bounds=None,
            corner=None,
            grid=None,
            label=None,
            margin=50,
            max=None,
            min=None,
            padding=None,
            palette=None,
            rect=None,
            scale="linear",
            show=True,
            spacing=None,
            ticklocator=None,
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
            0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, margin=margin)

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
            label=label,
            max=max,
            min=min,
            padding=padding,
            palette=palette,
            scenegraph=self._scenegraph,
            scale=scale,
            show=show,
            spacing=spacing,
            ticklocator=ticklocator,
            x1=x1,
            x2=x2,
            y1=y1,
            y2=y2,
            )

        self._scenegraph.add_edge(self, "render", axes)

        return axes

    def table(
            self,
            data=None,
            rows=None,
            columns=None,
            annotation=False,
            bounds=None,
            brows=None,
            corner=None,
            filename=None,
            grid=None,
            label=None,
            lcolumns=None,
            margin=50,
            rcolumns=None,
            rect=None,
            trows=None,
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
            0, self._width, 0, self._height,
            bounds=bounds,
            rect=rect,
            corner=corner,
            grid=grid,
            margin=margin,
            )
        table = toyplot.coordinates.Table(
            annotation=annotation,
            brows=brows,
            columns=columns,
            filename=filename,
            label=label,
            lcolumns=lcolumns,
            scenegraph=self._scenegraph,
            rcolumns=rcolumns,
            rows=rows,
            trows=trows,
            xmax_range=xmax_range,
            xmin_range=xmin_range,
            ymax_range=ymax_range,
            ymin_range=ymin_range,
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
                    table.body.cell[:, j].format = toyplot.format.FloatFormatter()
                    table.body.cell[:, j].align = "separator"
                elif issubclass(column._data.dtype.type, numpy.character):
                    table.cells.cell[:, j].align = "left"
                elif issubclass(column._data.dtype.type, numpy.integer):
                    table.cells.cell[:, j].align = "right"

            if trows:
                # Format top cells for use as a header
                table.top.cells.lstyle = {"font-weight": "bold"}
                # Enable a single horizontal line between top and body.
                table.cells.grid.hlines[trows] = "single"

        self._scenegraph.add_edge(self, "render", table)

        return table

    def image(
            self,
            data,
            bounds=None,
            corner=None,
            grid=None,
            margin=50,
            rect=None,
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
        margin: size of the margin around grid cells, optional
          Specifies the amount of empty space to leave between grid cells When using the
          `grid` parameter for positioning.  Assumes CSS pixels by default, and supports
          all of the absolute units described in :ref:`units`.
        """
        colormap = None
        if isinstance(data, tuple):
            data, colormap = data
            if not isinstance(colormap, toyplot.color.Map):
                raise ValueError("Expected toyplot.color.Map, received %s." % colormap) # pragma: no cover
            data = numpy.atleast_3d(data)
            if data.shape[2] != 1:
                raise ValueError("Expected an image with one channel.") # pragma: no cover
            data = colormap.colors(data)

        xmin_range, xmax_range, ymin_range, ymax_range = toyplot.layout.region(
            0, self._width, 0, self._height,
            bounds=bounds,
            rect=rect,
            corner=corner,
            grid=grid,
            margin=margin,
            )

        mark = toyplot.mark.Image(
            xmin_range,
            xmax_range,
            ymin_range,
            ymax_range,
            data=data,
            )

        self._scenegraph.add_edge(self, "render", mark)

        return mark

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
        table["text"] = toyplot.broadcast.pyobject(text, table.shape[0])
        table["angle"] = toyplot.broadcast.scalar(angle, table.shape[0])
        table["fill"] = toyplot.broadcast.pyobject(fill, table.shape[0])
        table["toyplot:fill"] = toyplot.color.broadcast(
            colors=fill,
            shape=(table.shape[0],),
            default=toyplot.color.black,
            )
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.pyobject(title, table.shape[0])
        style = toyplot.style.require(style, allowed=toyplot.style.allowed.text)

        mark = toyplot.mark.Text(
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
            )

        self._scenegraph.add_edge(self, "render", mark)

        return mark

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
