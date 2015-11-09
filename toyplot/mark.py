# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import numpy
import toyplot.require


##########################################################################
# Basic Toyplot marks

class Mark(object):

    """Base class for all Toyplot marks.
    """

    def __init__(self):
        pass


class AxisLines(Mark):

    """Render multiple lines parallel to an axis.

    Do not create AxisLines instances directly.  Use factory methods such as
    :meth:`toyplot.axes.Cartesian.hlines` and :meth:`toyplot.axes.Cartesian.vlines` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            coordinates,
            stroke,
            opacity,
            title,
            style,
        ):
        Mark.__init__(self)

        # 1 axis identifier
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=1)

        self._table = toyplot.require.instance(table, toyplot.data.Table)
        # 1 coordinate column
        self._coordinates = toyplot.require.table_keys(table, coordinates, length=1)
        # 1 stroke color column
        self._stroke = toyplot.require.table_keys(table, stroke, length=1)
        # 1 opacity column
        self._opacity = toyplot.require.table_keys(table, opacity, length=1)
        # 1 title column
        self._title = toyplot.require.table_keys(table, title, length=1)
        # Line style
        self._style = toyplot.require.style(style)



class BarBoundaries(Mark):

    """Render multiple stacked bars defined by bar boundaries.

    Do not create BarBoundaries instances directly.  Use factory methods such as
    :func:`toyplot.bars` or :meth:`toyplot.axes.Cartesian.bars` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            left,
            right,
            boundaries,
            fill,
            opacity,
            title,
            style,
            filename,
        ):
        Mark.__init__(self)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # 1 coordinate column
        self._left = toyplot.require.table_keys(table, left, length=1)
        # 1 coordinate column
        self._right = toyplot.require.table_keys(table, right, length=1)
        # N bar boundary columns
        self._boundaries = toyplot.require.table_keys(table, boundaries, min_length=2)
        # N-1 fill color columns
        self._fill = toyplot.require.table_keys(table, fill, length=len(boundaries) - 1)
        # N-1 opacity columns
        self._opacity = toyplot.require.table_keys(table, opacity, length=len(boundaries) - 1)
        # N-1 title columns
        self._title = toyplot.require.table_keys(table, title, length=len(boundaries) - 1)
        # Bar style
        self._style = toyplot.style.combine({"stroke": "none"}, toyplot.require.style(style))
        # Export filename
        self._filename = toyplot.require.filename(filename)


class BarMagnitudes(Mark):

    """Render multiple stacked bars defined by bar magnitudes.

    Do not create BarMagnitudes instances directly.  Use factory methods such as
    :func:`toyplot.bars` or :meth:`toyplot.axes.Cartesian.bars` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            left,
            right,
            baseline,
            magnitudes,
            fill,
            opacity,
            title,
            style,
            filename,
        ):
        Mark.__init__(self)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)
        # 1 coordinate column
        self._left = toyplot.require.table_keys(table, left, length=1)
        # 1 coordinate column
        self._right = toyplot.require.table_keys(table, right, length=1)
        # 1 baseline column
        self._baseline = toyplot.require.table_keys(table, baseline, length=1)
        # N bar magnitude columns
        self._magnitudes = toyplot.require.table_keys(table, magnitudes, min_length=1)
        # N fill color columns
        self._fill = toyplot.require.table_keys(table, fill, length=len(magnitudes))
        # N opacity columns
        self._opacity = toyplot.require.table_keys(table, opacity, length=len(magnitudes))
        # N title columns
        self._title = toyplot.require.table_keys(table, title, length=len(magnitudes))
        # Bar style
        self._style = toyplot.style.combine({"stroke": "none"}, toyplot.require.style(style))
        # Export filename
        self._filename = toyplot.require.filename(filename)


class FillBoundaries(Mark):

    """Render multiple stacked fill regions defined by boundaries.

    Do not create FillBoundaries instances directly.  Use factory methods such
    as :func:`toyplot.fill` or :meth:`toyplot.axes.Cartesian.fill` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            position,
            boundaries,
            fill,
            opacity,
            title,
            style,
            filename,
        ):
        Mark.__init__(self)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)
        # 1 coordinate column
        self._position = toyplot.require.table_keys(table, position, length=1)
        # N fill boundary columns
        self._boundaries = toyplot.require.table_keys(table, boundaries, min_length=2)
        # N-1 fill colors
        self._fill = toyplot.require.vector(fill, length=len(boundaries) - 1)
        # N-1 opacities
        self._opacity = toyplot.require.scalar_vector(opacity, length=len(boundaries) - 1)
        # N-1 titles
        #self._title = toyplot.require.object_vector(title, length=len(boundaries) - 1)
        self._title = title
        # Fill style
        self._style = toyplot.require.style(style)
        # Export filename
        self._filename = toyplot.require.filename(filename)


class FillMagnitudes(Mark):

    """Render multiple stacked fill regions defined by magnitudes.

    Do not create FillMagnitudes instances directly.  Use factory methods such
    as :func:`toyplot.fill` or :meth:`toyplot.axes.Cartesian.fill` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            position,
            baseline,
            magnitudes,
            fill,
            opacity,
            title,
            style,
            filename,
        ):
        Mark.__init__(self)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # 1 coordinate column
        self._position = toyplot.require.table_keys(table, position, length=1)
        # 1 baseline column
        self._baseline = toyplot.require.table_keys(table, baseline, length=1)
        # N fill magnitude columns
        self._magnitudes = toyplot.require.table_keys(table, magnitudes)
        # N fill colors
        self._fill = toyplot.require.vector(fill, length=len(magnitudes))
        # N opacities
        self._opacity = toyplot.require.scalar_vector(opacity, length=len(magnitudes))
        # N titles
        #self._title = toyplot.require.object_vector(title, length=len(magnitudes))
        self._title = title
        # Fill style
        self._style = toyplot.require.style(style)
        # Export filename
        self._filename = toyplot.require.filename(filename)


class Graph(Mark): # pragma: no cover

    """Plot a graph (collection of vertices and edges).

    Do not create Graph instances directly.  Use factory methods such as
    :meth:`toyplot.axes.Cartesian.graph` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            vtable,
            vid,
            vlabel,
            vcoordinates,
            vmarker,
            vsize,
            vcolor,
            vopacity,
            vtitle,
            vstyle,
            vlstyle,
            vlshow,
            etable,
            esource,
            etarget,
            eshape,
            ecoordinates,
            ecolor,
            ewidth,
            eopacity,
            estyle,
        ):
        Mark.__init__(self)

        # D axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, min_length=1)

        self._vtable = toyplot.require.instance(vtable, toyplot.data.Table)
        # 1 vertex id column
        self._vid = toyplot.require.table_keys(vtable, vid, length=1)
        # 1 vertex label column
        self._vlabel = toyplot.require.table_keys(vtable, vlabel, length=1)
        # D coordinate columns
        self._vcoordinates = toyplot.require.table_keys(vtable, vcoordinates, length=len(self._coordinate_axes))
        # 1 vertex marker column
        self._vmarker = toyplot.require.table_keys(vtable, vmarker, length=1)
        # 1 vertex marker size column
        self._vsize = toyplot.require.table_keys(vtable, vsize, length=1)
        # 1 vertex marker color column
        self._vcolor = toyplot.require.table_keys(vtable, vcolor, length=1)
        # 1 marker opacity column
        self._vopacity = toyplot.require.table_keys(vtable, vopacity, length=1)
        # 1 vertex titles column
        self._vtitle = toyplot.require.table_keys(vtable, vtitle, length=1)
        # Vertex marker style
        self._vstyle = toyplot.require.style(vstyle)
        # Vertex marker label style
        self._vlstyle = toyplot.require.style(vlstyle)
        # Draw vertex labels
        self._vlshow = vlshow

        self._etable = toyplot.require.instance(etable, toyplot.data.Table)
        # 1 edge source column
        self._esource = toyplot.require.table_keys(etable, esource, length=1)
        # 1 edge target column
        self._etarget = toyplot.require.table_keys(etable, etarget, length=1)
        # 1 edge shape column
        self._eshape = toyplot.require.table_keys(etable, eshape, length=1)

        ecoordinate_count = 0
        for shape in self._etable[self._eshape[0]]:
            for segment in shape:
                if segment == "M":
                    ecoordinate_count += 1
                elif segment == "L":
                    ecoordinate_count += 1
                elif segment == "Q":
                    ecoordinate_count += 2
                elif segment == "C":
                    ecoordinate_count += 3
                else:
                    raise ValueError("Unknown edge shape segment: %s" % segment)

        # C x D edge coordinate columns
        self._ecoordinates = toyplot.require.scalar_matrix(ecoordinates, rows=ecoordinate_count, columns=len(self._coordinate_axes))

        # 1 edge color column
        self._ecolor = toyplot.require.table_keys(etable, ecolor, length=1)
        # 1 edge width column
        self._ewidth = toyplot.require.table_keys(etable, ewidth, length=1)
        # 1 edge opacity column
        self._eopacity = toyplot.require.table_keys(etable, eopacity, length=1)
        # Edge style
        self._estyle = toyplot.require.style(estyle)

    @property
    def vcount(self):
        """Return the number of vertices in the graph."""
        return len(self._vtable)

    @property
    def vids(self):
        """Returns the graph vertex identifiers."""
        return self._vtable[self._vid[0]]

    @property
    def vcoordinates(self):
        """Return the graph vertex coordinates."""
        return numpy.column_stack([self._vtable[column] for column in self._vcoordinates])

    @property
    def ecount(self):
        """Return the number of edges in the graph."""
        return len(self._etable)

    @property
    def esources(self):
        return self._etable[self._esource[0]]

    @property
    def etargets(self):
        return self._etable[self._etarget[0]]

    @property
    def eshapes(self):
        return self._etable[self._eshape[0]]

    @property
    def ecoordinates(self):
        return self._ecoordinates

    @property
    def edges(self):
        """Return the graph edges as a :math:`E \\times 2` matrix of source, target indices."""
        return numpy.column_stack((self._etable[self._esource[0]], self._etable[self._etarget[0]]))

class Plot(Mark):

    """Plot multiple bivariate data series using lines and/or markers.

    Do not create Plot instances directly.  Use factory methods such as
    :func:`toyplot.plot`, :func:`toyplot.scatterplot`,
    :meth:`toyplot.axes.Cartesian.plot` and
    :meth:`toyplot.axes.Cartesian.scatterplot` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            coordinates,
            series,
            stroke,
            stroke_width,
            stroke_opacity,
            stroke_title,
            marker,
            msize,
            mfill,
            mstroke,
            mopacity,
            mtitle,
            style,
            mstyle,
            mlstyle,
            filename,
        ):
        Mark.__init__(self)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # 1 coordinate column
        self._coordinates = toyplot.require.table_keys(table, coordinates, length=1)
        # N coordinate columns
        self._series = toyplot.require.table_keys(table, series, min_length=1)
        # N stroke colors
        self._stroke = toyplot.require.vector(stroke, length=len(series))
        # N stroke widths
        self._stroke_width = toyplot.require.scalar_vector(stroke_width, length=len(series))
        # N stroke opacities
        self._stroke_opacity = toyplot.require.scalar_vector(stroke_opacity, length=len(series))
        # N stroke titles
        self._stroke_title = stroke_title
        # N marker columns
        self._marker = toyplot.require.table_keys(table, marker, length=len(series))
        # N marker size columns
        self._msize = toyplot.require.table_keys(table, msize, length=len(series))
        # N marker fill color columns
        self._mfill = toyplot.require.table_keys(table, mfill, length=len(series))
        # N marker stroke color columns
        self._mstroke = toyplot.require.table_keys(table, mstroke, length=len(series))
        # N marker opacity columns
        self._mopacity = toyplot.require.table_keys(table, mopacity, length=len(series))
        # N marker title columns
        self._mtitle = toyplot.require.table_keys(table, mtitle, length=len(series))
        # Line style
        self._style = toyplot.require.style(style)
        # Marker style
        self._mstyle = toyplot.require.style(mstyle)
        # Marker label style
        self._mlstyle = toyplot.require.style(mlstyle)
        # Export filename
        self._filename = toyplot.require.filename(filename)


class Rect(Mark):

    """Plot axis-aligned rectangles.

    Do not create Rect instances directly.  Use factory methods such as
    :meth:`toyplot.axes.Cartesian.rect` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            left,
            right,
            top,
            bottom,
            fill,
            opacity,
            title,
            style,
            filename,
        ):
        Mark.__init__(self)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # 1 coordinate column
        self._left = toyplot.require.table_keys(table, left, length=1)
        # 1 coordinate column
        self._right = toyplot.require.table_keys(table, right, length=1)
        # 1 coordinate column
        self._top = toyplot.require.table_keys(table, top, length=1)
        # 1 coordinate column
        self._bottom = toyplot.require.table_keys(table, bottom, length=1)
        # 1 fill color column
        self._fill = toyplot.require.table_keys(table, fill, length=1)
        # 1 opacity column
        self._opacity = toyplot.require.table_keys(table, opacity, length=1)
        # 1 title column
        self._title = toyplot.require.table_keys(table, title, length=1)
        # Rectangle style
        self._style = toyplot.require.style(style)
        # Export filename
        self._filename = toyplot.require.filename(filename)


class Scatterplot(Mark):

    """Plot multiple bivariate data series using markers.

    Do not create Scatterplot instances directly.  Use factory methods such as
    :func:`toyplot.scatterplot` and :meth:`toyplot.axes.Cartesian.scatterplot`
    instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            coordinates,
            series,
            marker,
            msize,
            mfill,
            mstroke,
            mopacity,
            mtitle,
            style,
            mstyle,
            mlstyle,
            filename,
        ):
        Mark.__init__(self)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # 1 coordinate column
        self._coordinates = toyplot.require.table_keys(table, coordinates, length=1)
        # N coordinate columns
        self._series = toyplot.require.table_keys(table, series, min_length=1)
        # N marker columns
        self._marker = toyplot.require.table_keys(table, marker, length=len(series))
        # N marker size columns
        self._msize = toyplot.require.table_keys(table, msize, length=len(series))
        # N marker fill color columns
        self._mfill = toyplot.require.table_keys(table, mfill, length=len(series))
        # N marker stroke color columns
        self._mstroke = toyplot.require.table_keys(table, mstroke, length=len(series))
        # N marker opacity columns
        self._mopacity = toyplot.require.table_keys(table, mopacity, length=len(series))
        # N marker title columns
        self._mtitle = toyplot.require.table_keys(table, mtitle, length=len(series))
        # Global style
        self._style = toyplot.require.style(style)
        # Marker style
        self._mstyle = toyplot.require.style(mstyle)
        # Marker label style
        self._mlstyle = toyplot.require.style(mlstyle)
        # Export filename
        self._filename = toyplot.require.filename(filename)


class Text(Mark):

    """Render text.

    Do not create Text instances directly.  Use factory methods such as
    :meth:`toyplot.canvas.Canvas.text` or :meth:`toyplot.axes.Cartesian.text` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            coordinates,
            text,
            angle,
            fill,
            opacity,
            title,
            style,
            filename,
        ):
        Mark.__init__(self)

        # D axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, min_length=1)

        self._table = toyplot.require.instance(table, toyplot.data.Table)
        # D coordinate columns
        self._coordinates = toyplot.require.table_keys(table, coordinates, length=len(self._coordinate_axes))
        # 1 text column
        self._text = toyplot.require.table_keys(table, text, length=1)
        # 1 angle column
        self._angle = toyplot.require.table_keys(table, angle, length=1)
        # 1 fill color column
        self._fill = toyplot.require.table_keys(table, fill, length=1)
        # 1 opacity column
        self._opacity = toyplot.require.table_keys(table, opacity, length=1)
        # 1 title column
        self._title = toyplot.require.table_keys(table, title, length=1)
        # Text style
        self._style = toyplot.require.style(style)
        # Export filename
        self._filename = toyplot.require.filename(filename)

##########################################################################
# More specialized marks


class Legend(Mark):

    """Render a figure legend (a collection of markers and labels).

    Do not create Legend instances directly.  Use factory methods such as
    :meth:`toyplot.canvas.Canvas.legend` or :meth:`toyplot.axes.Cartesian.legend` instead.
    """

    def __init__(self, xmin, xmax, ymin, ymax, marks, style, lstyle):
        Mark.__init__(self)
        self._xmin = xmin
        self._xmax = xmax
        self._ymin = ymin
        self._ymax = ymax
        self._gutter = 10
        self._marks = marks
        # Styles the box surrounding the legend
        self._style = toyplot.style.combine(
            {"fill": "none", "stroke": "none"}, style)
        self._lstyle = lstyle  # Styles the legend labels


class VColorBar(Mark):

    """Displays a one-dimensional mapping from values to colors.

    Do not create VColorbarMark instances directly.  Use factory methods such
    as :meth:`toyplot.axes.Cartesian.colorbar` instead.
    """
    class DomainHelper(object):

        def __init__(self, min, max):
            self._min = min
            self._max = max

        @property
        def min(self):
            return self._min

        @min.setter
        def min(self, value):
            self._min = value

        @property
        def max(self):
            return self._max

        @max.setter
        def max(self, value):
            self._max = value

    class LabelHelper(object):

        def __init__(self, label, style):
            self._text = label
            self._style = toyplot.style.combine(
                {
                    "font-size": "12px",
                    "font-weight": "bold",
                    "stroke": "none",
                    "text-anchor": "middle",
                    "alignment-baseline": "middle",
                    "baseline-shift": "-200%"},
                toyplot.require.style(style))

        @property
        def text(self):
            return self._text

        @text.setter
        def text(self, value):
            self._text = value

        @property
        def style(self):
            return self._style

        @style.setter
        def style(self, value):
            self._style = toyplot.style.combine(
                self._style, toyplot.require.style(value))

    class PerTickHelper(object):

        class TickProxy(object):

            def __init__(self, tick):
                self._tick = tick

            @property
            def style(self):
                return self._tick.get("style", {})

            @style.setter
            def style(self, value):
                self._tick["style"] = toyplot.style.combine(
                    self._tick.get("style"), toyplot.require.style(value))

        def __init__(self):
            self._indices = collections.defaultdict(dict)
            self._values = collections.defaultdict(dict)

        def __call__(self, index=None, value=None, style=None):
            if index is None and value is None:
                raise ValueError("Must specify tick index or value.") # pragma: no cover
            if index is not None and value is not None:
                raise ValueError(
                    "Must specify either index or value, not both.") # pragma: no cover
            if index is not None:
                return VColorBar.PerTickHelper.TickProxy(self._indices[index])
            if value is not None:
                return VColorBar.PerTickHelper.TickProxy(self._values[value])

        def styles(self, values):
            results = [self._indices[index].get("style", None) if index in self._indices else None for index in range(len(values))]
            for value in self._values:
                deltas = numpy.abs(values - value)
                results[numpy.argmin(deltas)] = self._values[
                    value].get("style", None)
            return results

    class TicksHelper(object):

        def __init__(self, length, locator):
            self._locator = locator
            self._show = False
            self._length = length
            self._style = {}
            self.labels = VColorBar.TickLabelsHelper()
            self.tick = VColorBar.PerTickHelper()

        @property
        def locator(self):
            return self._locator

        @locator.setter
        def locator(self, value):
            self._locator = value

        @property
        def show(self):
            return self._show

        @show.setter
        def show(self, value):
            self._show = value

        @property
        def length(self):
            return self._length

        @length.setter
        def length(self, value):
            self._length = value

        @property
        def style(self):
            return self._style

        @style.setter
        def style(self, value):
            self._style = toyplot.style.combine(
                self._style, toyplot.require.style(value))

    class TickLabelsHelper(object):

        def __init__(self):
            self._show = True
            self._style = {
                "font-size": "10px", "font-weight": "normal", "stroke": "none"}
            self.label = VColorBar.PerTickHelper()

        @property
        def show(self):
            return self._show

        @show.setter
        def show(self, value):
            self._show = value

        @property
        def style(self):
            return self._style

        @style.setter
        def style(self, value):
            self._style = toyplot.style.combine(
                self._style, toyplot.require.style(value))

    def __init__(
            self,
            xmin_range,
            xmax_range,
            ymin_range,
            ymax_range,
            label,
            colormap,
            padding,
            tick_length,
            min,
            max,
            tick_locator,
            style):
        Mark.__init__(self)

        self._xmin_range = xmin_range
        self._xmax_range = xmax_range
        self._ymin_range = ymin_range
        self._ymax_range = ymax_range
        self._scale = "linear"
        self._colormap = colormap
        self._vmin_implicit = None
        self._vmax_implicit = None
        self._padding = padding
        self.domain = VColorBar.DomainHelper(min, max)
        self.label = VColorBar.LabelHelper(label=label, style=None)
        self.ticks = VColorBar.TicksHelper(tick_length, tick_locator)
        self._style = style

    def _update_domain(self, vmin, vmax):
        self._vmin_implicit = vmin if self._vmin_implicit is None else self._vmin_implicit if vmin is None else min(
            vmin,
            self._vmin_implicit)
        self._vmax_implicit = vmax if self._vmax_implicit is None else self._vmax_implicit if vmin is None else max(
            vmax,
            self._vmax_implicit)

    def _finalize_domain(self):
        # Begin with the implicit domain defined by any explicitly-specified
        # data.
        vmin = self._vmin_implicit
        vmax = self._vmax_implicit

        # If there is no implicit domain (we don't have any data), default to
        # the origin.
        if vmin is None:
            vmin = 0
        if vmax is None:
            vmax = 0

        # Allow users to override the domain.
        if self.domain._min is not None:
            vmin = self.domain._min
        if self.domain._max is not None:
            vmax = self.domain._max

        # Ensure that the domain is never empty.
        if vmin == vmax:
            vmin -= 0.5
            vmax += 0.5

        def get_locator(locator, scale, domain_min, domain_max):
            if locator is not None:
                return locator
            if scale == "linear":
                return toyplot.locator.Extended()

        # Calculate tick locations and labels.
        locator = get_locator(self.ticks._locator, self._scale, vmin, vmax)

        self._tick_locations, self._tick_labels, self._tick_titles = locator.ticks(
            vmin, vmax)

        # Allow tick locations to grow (never shrink) the domain.
        if len(self._tick_locations):
            vmin = min(vmin, self._tick_locations[0])
            vmax = max(vmax, self._tick_locations[-1])

        self._vmin_computed = vmin
        self._vmax_computed = vmax

        def linear_projection(domain_min, domain_max, range_min, range_max):
            def implementation(x):
                return (1 - ((x - domain_min) / (domain_max - domain_min))) * (range_max - range_min) + range_min
            return implementation

        if self._scale == "linear":
            self._projection = linear_projection(
                vmin,
                vmax,
                self._ymin_range +
                self._padding,
                self._ymax_range -
                self._padding)

    def _project_y(self, v):
        return self._projection(v)

    def _project_color(self, v):
        return self._colormap.colors(
            v,
            self._vmin_computed,
            self._vmax_computed)
