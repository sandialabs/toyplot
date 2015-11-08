# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import itertools
import numpy
import toyplot.broadcast
import toyplot.color
import toyplot.data
import toyplot.format
import toyplot.layout
import toyplot.locator
import toyplot.mark
import toyplot.projection
import toyplot.require
import toyplot.text
import time

##########################################################################
# Helpers

def _null_min(a, b):
    """Return the minimum of two values, with special logic to handle None."""
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def _null_max(a, b):
    """Return the maximum of two values, with special logic to handle None."""
    if a is None:
        return b
    if b is None:
        return a
    return max(a, b)


def _flat_non_null(array):
    if isinstance(array, numpy.ma.MaskedArray):
        array = array.compressed()
    elif isinstance(array, numpy.ndarray):
        array = array.ravel()
    array = array[numpy.invert(numpy.isnan(array))]
    return array


def _mark_exportable(table, column, exportable=True):
    table.metadata(column)["toyplot:exportable"] = exportable


class OrderedSet(collections.MutableSet):

    """Python recipe from http://code.activestate.com/recipes/576694-orderedset
    """

    def __init__(self, iterable=None):
        self.end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)


class Axis(object):
    """One dimensional axis that can be used to create coordinate systems.
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

        def __init__(self, label, style={}):
            self._text = label
            self._offset = 0
            self._style = toyplot.style.combine(
                {
                    "font-weight": "bold",
                    "stroke": "none",
                    "text-anchor": "middle",
                    "alignment-baseline": "middle",
                },
                toyplot.require.style(style))

        @property
        def text(self):
            return self._text

        @text.setter
        def text(self, value):
            self._text = value

        @property
        def offset(self):
            return self._offset

        @offset.setter
        def offset(self, value):
            self._offset = toyplot.units.convert(
                value, target="px", default="px")

        @property
        def style(self):
            return self._style

        @style.setter
        def style(self, value):
            self._style = toyplot.style.combine(
                self._style, toyplot.require.style(value))

    class SpineHelper(object):

        def __init__(self):
            self._show = True
            self._position = "low"
            self._style = {}

        @property
        def show(self):
            return self._show

        @show.setter
        def show(self, value):
            self._show = value

        @property
        def position(self):
            return self._position

        @position.setter
        def position(self, value):
            self._position = value

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

        def __call__(self, index=None, value=None):
            if index is None and value is None:
                raise ValueError("Must specify tick index or value.")
            if index is not None and value is not None:
                raise ValueError(
                    "Must specify either index or value, not both.")
            if index is not None:
                return Axis.PerTickHelper.TickProxy(self._indices[index])
            elif value is not None:
                return Axis.PerTickHelper.TickProxy(self._values[value])

        def styles(self, values):
            results = [self._indices[index].get("style", None) if index in self._indices else None for index in range(len(values))]
            for value in self._values:
                deltas = numpy.abs(values - value)
                results[numpy.argmin(deltas)] = self._values[value].get("style", None)
            return results

    class TicksHelper(object):

        def __init__(self, locator, angle):
            self._locator = locator
            self._show = False
            self._above = None
            self._below = None
            self._style = {}
            self.labels = Axis.TickLabelsHelper(angle)
            self.tick = Axis.PerTickHelper()

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
        def above(self):
            return self._above

        @above.setter
        def above(self, value):
            if value is None:
                self._above = None
            else:
                self._above = toyplot.units.convert(value, target="px", default="px")

        @property
        def below(self):
            return self._below

        @below.setter
        def below(self, value):
            if value is None:
                self._below = None
            else:
                self._below = toyplot.units.convert(value, target="px", default="px")

        @property
        def style(self):
            return self._style

        @style.setter
        def style(self, value):
            self._style = toyplot.style.combine(
                self._style, toyplot.require.style(value))

    class TickLabelsHelper(object):

        def __init__(self, angle):
            self._show = True
            self._offset = 0
            self._angle = angle
            self._style = {
                "font-size": "10px", "font-weight": "normal", "stroke": "none"}
            self.label = Axis.PerTickHelper()

        @property
        def show(self):
            return self._show

        @show.setter
        def show(self, value):
            self._show = value

        @property
        def offset(self):
            return self._offset

        @offset.setter
        def offset(self, value):
            self._offset = toyplot.units.convert(
                value, target="px", default="px")

        @property
        def angle(self):
            return self._angle

        @angle.setter
        def angle(self, value):
            self._angle = value

        @property
        def style(self):
            return self._style

        @style.setter
        def style(self, value):
            self._style = toyplot.style.combine(
                self._style, toyplot.require.style(value))

    def __init__(
            self,
            label=None,
            max=None,
            min=None,
            scale="linear",
            show=True,
            tick_angle=0,
            tick_locator=None,
        ):
        self.scale = scale # This calls the property setter
        self._show = show
        self._tick_labels = []
        self._tick_locations = []
        self._tick_titles = []

        self._data_min = None
        self._data_max = None
        self._display_min = None
        self._display_max = None

        self.domain = Axis.DomainHelper(min, max)
        self.label = Axis.LabelHelper(label)
        self.spine = Axis.SpineHelper()
        self.ticks = Axis.TicksHelper(tick_locator, tick_angle)

    @property
    def show(self):
        return self._show

    @show.setter
    def show(self, value):
        self._show = value

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        if value == "linear":
            self._scale = "linear"
            return
        elif value in ["log", "log10"]:
            self._scale = ("log", 10)
            return
        elif value == "log2":
            self._scale = ("log", 2)
            return
        elif isinstance(value, tuple) and len(value) == 2:
            scale, base = value
            if scale == "log":
                self._scale = ("log", base)
                return
        raise ValueError(
            """Scale must be "linear", "log", "log10", "log2" or a ("log", base) tuple.""")

    def update_domain(self, values, display=True, data=True):
        values = _flat_non_null(values)

        if len(values) and display:
            self._display_min = _null_min(
                values.min(), self._display_min)
            self._display_max = _null_max(
                values.max(), self._display_max)

        if len(values) and data:
            self._data_min = _null_min(
                values.min(), self._data_min)
            self._data_max = _null_max(
                values.max(), self._data_max)

    def projection(self, domain_min=None, domain_max=None, range_min=None, range_max=None):
        if domain_min is None:
            domain_min = self._domain_min
        if domain_max is None:
            domain_max = self._domain_max
        if range_min is None:
            range_min = 0.0
        if range_max is None:
            range_max = 1.0

        if self._scale == "linear":
            return toyplot.projection.linear(domain_min, domain_max, range_min, range_max)

        scale, base = self._scale
        return toyplot.projection.log(base, domain_min, domain_max, range_min, range_max)

    def locator(self):
        if self.ticks.locator is not None:
            return self.ticks.locator
        if self.scale == "linear":
            return toyplot.locator.Extended()
        else:
            scale, base = self.scale
            if scale == "log":
                return toyplot.locator.Log(base=base)
        raise RuntimeError("Unable to create an appropriate locator.")

    def _finalize(self, domain_min, domain_max, tick_locations, tick_labels, tick_titles):
        self._domain_min = domain_min
        self._domain_max = domain_max
        self._tick_locations = tick_locations
        self._tick_labels = tick_labels
        self._tick_titles = tick_titles


class NumberLine(object):
    """Standard one-dimensional number line.

    Do not create NumberLine instances directly.  Use factory methods such
    as :meth:`toyplot.canvas.Canvas.number_line` instead.
    """
    def __init__(
            self,
            x1,
            y1,
            x2,
            y2,
            min,
            max,
            show,
            label,
            ticklocator,
            scale,
            palette,
            parent,
        ):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2


        if palette is None:
            palette = toyplot.color.Palette()
        self._palette = palette
#        self._bar_colors = itertools.cycle(palette)
#        self._fill_colors = itertools.cycle(palette)
#        self._graph_colors = itertools.cycle(palette)
#        self._plot_colors = itertools.cycle(palette)
#        self._scatterplot_colors = itertools.cycle(palette)
#        self._rect_colors = itertools.cycle(palette)
#        self._text_colors = itertools.cycle(palette)

#        self.label = Axis.LabelHelper(
#            label=label, style={"font-size": "14px", "baseline-shift": "100%"})

        self.axis = Axis(
            show=show,
            label=label,
            min=min,
            max=max,
            tick_locator=ticklocator,
            tick_angle=0,
            scale=scale,
            )

        self._parent = parent
        self._children = []

    @property
    def show(self):
        return self.axis.show

    @show.setter
    def show(self, value):
        self.axis.show = value

    def update_domain(self, values, display=True, data=True):
        self.axis.update_domain(values, display=display, data=data)

    def _finalize(self):
        # Begin with the implicit domain defined by our data.
        min = self.axis._display_min
        max = self.axis._display_max

        # If there is no implicit domain (we don't have any data), default
        # to the origin.
        if min is None:
            min = 0
        if max is None:
            max = 0

        # Ensure that the domain is never empty.
        if min == max:
            min -= 0.5
            max += 0.5

        # Allow users to override the domain.
        if self.axis.domain.min is not None:
            min = self.axis.domain.min
        if self.axis.domain.max is not None:
            max = self.axis.domain.max

        # Ensure that the domain is never empty.
        if min == max:
            min -= 0.5
            max += 0.5

        # Calculate tick locations and labels.
        tick_locations = []
        tick_labels = []
        tick_titles = []
        if self.axis.show:
            tick_locations, tick_labels, tick_titles = self.axis.locator().ticks(min, max)

        # Allow tick locations to grow (never shrink) the domain.
        if len(tick_locations):
            min = numpy.amin((min, tick_locations[0]))
            max = numpy.amax((max, tick_locations[-1]))

        self.axis._finalize(min, max, tick_locations, tick_labels, tick_titles)


class Cartesian(object):

    """Standard two-dimensional Cartesian coordinate system.

    Do not create Cartesian instances directly.  Use factory methods such
    as :meth:`toyplot.canvas.Canvas.axes` instead.
    """
    class CoordinatesHelper(object):

        def __init__(
                self,
                show,
                xmin_range,
                xmax_range,
                ymin_range,
                ymax_range,
                style):

            self._show = show
            self._xmin_range = xmin_range
            self._xmax_range = xmax_range
            self._ymin_range = ymin_range
            self._ymax_range = ymax_range

            self._style = toyplot.style.combine(
                {"stroke": "none", "fill": "white", "opacity": 0.75}, toyplot.require.style(style))
            self.label = Cartesian.CoordinatesLabelHelper(style={})

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

    class CoordinatesLabelHelper(object):

        def __init__(self, style):
            self._style = toyplot.style.combine(
                {
                    "font-size": "10px",
                    "font-weight": "normal",
                    "stroke": "none",
                    "text-anchor": "middle",
                    "alignment-baseline": "middle"},
                toyplot.require.style(style))

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
            aspect,
            xmin,
            xmax,
            ymin,
            ymax,
            show,
            xshow,
            yshow,
            label,
            xlabel,
            ylabel,
            xticklocator,
            yticklocator,
            xscale,
            yscale,
            palette,
            padding,
            parent,
            xaxis=None,
            yaxis=None):
        self._xmin_range = xmin_range
        self._xmax_range = xmax_range
        self._ymin_range = ymin_range
        self._ymax_range = ymax_range
        self._aspect = aspect
        self._expand_domain_range_x = None
        self._expand_domain_range_y = None
        self._expand_domain_range_left = None
        self._expand_domain_range_right = None
        self._expand_domain_range_top = None
        self._expand_domain_range_bottom = None
        self._padding = toyplot.units.convert(padding, target="px", default="px")

        if palette is None:
            palette = toyplot.color.Palette()
        self._palette = palette
        self._bar_colors = itertools.cycle(palette)
        self._fill_colors = itertools.cycle(palette)
        self._graph_colors = itertools.cycle(palette)
        self._plot_colors = itertools.cycle(palette)
        self._scatterplot_colors = itertools.cycle(palette)
        self._rect_colors = itertools.cycle(palette)
        self._text_colors = itertools.cycle(palette)

        self._show = show

        self.coordinates = Cartesian.CoordinatesHelper(
            show=True,
            xmin_range=xmax_range - 100,
            xmax_range=xmax_range - 10,
            ymin_range=ymin_range + 10,
            ymax_range=ymin_range + 24,
            style={})
        self.label = Axis.LabelHelper(
            label=label, style={"font-size": "14px", "baseline-shift": "100%"})

        if xaxis is None:
            xaxis = Axis()
        xaxis.show = xshow
        xaxis.label.text = xlabel
        xaxis.domain.min = xmin
        xaxis.domain.max = xmax
        xaxis.ticks.locator = xticklocator
        xaxis.scale = xscale

        if yaxis is None:
            yaxis = Axis()
        yaxis.show = yshow
        yaxis.label.text = ylabel
        yaxis.domain.min = ymin
        yaxis.domain.max = ymax
        yaxis.ticks.locator = yticklocator
        yaxis.scale = yscale

        self.x = xaxis
        self.y = yaxis

        self._parent = parent
        self._children = []

    @property
    def aspect(self):
        return self._aspect

    @aspect.setter
    def aspect(self, value):
        if value not in [None, "fit-range"]:
            raise ValueError("Unknown aspect value: %s" % value)
        self._aspect = value

    @property
    def show(self):
        return self._show

    @show.setter
    def show(self, value):
        self._show = value

    @property
    def padding(self):
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = toyplot.units.convert(value, target="px", default="px")

    def _update_domain(self, x, y, display=True, data=True):
        self.x.update_domain(x, display=display, data=data)
        self.y.update_domain(y, display=display, data=data)

    def _expand_domain_range(self, x, y, extents):
        left, right, top, bottom = extents

        self._expand_domain_range_x = x if self._expand_domain_range_x is None else numpy.concatenate(
            (self._expand_domain_range_x, x))
        self._expand_domain_range_y = y if self._expand_domain_range_y is None else numpy.concatenate(
            (self._expand_domain_range_y, y))
        self._expand_domain_range_left = left if self._expand_domain_range_left is None else numpy.concatenate(
            (self._expand_domain_range_left, left))
        self._expand_domain_range_right = right if self._expand_domain_range_right is None else numpy.concatenate(
            (self._expand_domain_range_right, right))
        self._expand_domain_range_top = top if self._expand_domain_range_top is None else numpy.concatenate(
            (self._expand_domain_range_top, top))
        self._expand_domain_range_bottom = bottom if self._expand_domain_range_bottom is None else numpy.concatenate(
            (self._expand_domain_range_bottom, bottom))

    def _finalize(self):
        # Begin with the implicit domain defined by our data.
        xmin = self.x._display_min
        xmax = self.x._display_max
        ymin = self.y._display_min
        ymax = self.y._display_max

        # If there is no implicit domain (we don't have any data), default
        # to the origin.
        if xmin is None:
            xmin = 0
        if xmax is None:
            xmax = 0
        if ymin is None:
            ymin = 0
        if ymax is None:
            ymax = 0

        # Ensure that the domain is never empty.
        if xmin == xmax:
            xmin -= 0.5
            xmax += 0.5
        if ymin == ymax:
            ymin -= 0.5
            ymax += 0.5

        # Optionally expand the domain in range-space (used to make room for text).
        if self._expand_domain_range_x is not None:
            x_projection = self.x.projection(
                domain_min=xmin,
                domain_max=xmax,
                range_min=self._xmin_range,
                range_max=self._xmax_range,
                )
            y_projection = self.y.projection(
                domain_min=ymin,
                domain_max=ymax,
                range_min=self._ymax_range,
                range_max=self._ymin_range,
                )

            range_x = x_projection(self._expand_domain_range_x)
            range_y = y_projection(self._expand_domain_range_y)
            range_left = range_x + self._expand_domain_range_left
            range_right = range_x + self._expand_domain_range_right
            range_top = range_y + self._expand_domain_range_top
            range_bottom = range_y + self._expand_domain_range_bottom

            domain_left = x_projection.inverse(range_left)
            domain_right = x_projection.inverse(range_right)
            domain_top = y_projection.inverse(range_top)
            domain_bottom = y_projection.inverse(range_bottom)

            xmin = _null_min(domain_left.min(), xmin)
            xmax = _null_max(domain_right.max(), xmax)
            ymin = _null_min(domain_bottom.min(), ymin)
            ymax = _null_max(domain_top.max(), ymax)

        # Optionally expand the domain to match the aspect ratio of the range.
        if self._aspect == "fit-range":
            dwidth = (xmax - xmin)
            dheight = (ymax - ymin)
            daspect = dwidth / dheight
            raspect = (self._xmax_range - self._xmin_range) / (self._ymax_range - self._ymin_range)

            if daspect < raspect:
                offset = ((dwidth * (raspect / daspect)) - dwidth) * 0.5
                xmin -= offset
                xmax += offset
            elif daspect > raspect:
                offset = ((dheight * (daspect / raspect)) - dheight) * 0.5
                ymin -= offset
                ymax += offset

        # Allow users to override the domain.
        if self.x.domain.min is not None:
            xmin = self.x.domain.min
        if self.x.domain.max is not None:
            xmax = self.x.domain.max
        if self.y.domain.min is not None:
            ymin = self.y.domain.min
        if self.y.domain.max is not None:
            ymax = self.y.domain.max

        # Ensure that the domain is never empty.
        if xmin == xmax:
            xmin -= 0.5
            xmax += 0.5
        if ymin == ymax:
            ymin -= 0.5
            ymax += 0.5

        # Calculate tick locations and labels.
        xtick_locations = []
        xtick_labels = []
        xtick_titles = []
        if self.x.show:
            xtick_locations, xtick_labels, xtick_titles = self.x.locator().ticks(xmin, xmax)
        ytick_locations = []
        ytick_labels = []
        ytick_titles = []
        if self.y.show:
            ytick_locations, ytick_labels, ytick_titles = self.y.locator().ticks(ymin, ymax)

        # Allow tick locations to grow (never shrink) the domain.
        if len(xtick_locations):
            xmin = numpy.amin((xmin, xtick_locations[0]))
            xmax = numpy.amax((xmax, xtick_locations[-1]))
        if len(ytick_locations):
            ymin = numpy.amin((ymin, ytick_locations[0]))
            ymax = numpy.amax((ymax, ytick_locations[-1]))

        self.x._finalize(xmin, xmax, xtick_locations, xtick_labels, xtick_titles)
        self.y._finalize(ymin, ymax, ytick_locations, ytick_labels, ytick_titles)

        self._x_projection = self.x.projection(range_min=self._xmin_range, range_max=self._xmax_range)
        self._y_projection = self.y.projection(range_min=self._ymax_range, range_max=self._ymin_range)

    def _project_x(self, x):
        return self._x_projection(x)

    def _project_y(self, y):
        return self._y_projection(y)

    def bars(
            self,
            a,
            b=None,
            c=None,
            along="x",
            baseline="stacked",
            color=None,
            opacity=1.0,
            title=None,
            style=None,
            filename=None):
        """Add stacked bars to the axes.

        This command generates one-or-more series of stacked bars.  For
        convenience, you can call it with many different types of input.  To
        generate a single series of :math:`M` bars, pass an optional vector of
        :math:`M` bar positions plus a vector of :math:`M` bar magnitudes:

        >>> axes.bars(magnitudes)
        >>> axes.bars(centers, magnitudes)
        >>> axes.bars(minpos, maxpos, magnitudes)

        To generate :math:`N` stacked series of :math:`M` bars, pass an optional
        vector of :math:`M` bar positions plus an :math:`M \\times N` matrix of
        bar magnitudes:

        >>> axes.bars(magnitudes)
        >>> axes.bars(centers, magnitudes)
        >>> axes.bars(minpos, maxpos, magnitudes)

        As a convenience for working with :func:`numpy.histogram`, you may pass
        a 2-tuple containing :math:`M` counts and :math:`M+1` bin edges:

        >>> axes.bars((counts, edges))

        Alternatively, you can generate :math:`N-1` stacked series of :math:`M`
        bars by passing an optional vector of :math:`M` bar positions plus an
        :math:`M \\times N` matrix of bar *boundaries*:

        >>> axes.bars(boundaries, baseline=None)
        >>> axes.bars(centers, boundaries, baseline=None)
        >>> axes.bars(minpos, maxpos, boundaries, baseline=None)

        Parameters
        ----------
        a, b, c: array-like series data.
        along: string, "x" or "y", optional
          Specify "x" (the default) for vertical bars, or "y" for horizontal bars.
        baseline: array-like, "stacked", "symmetrical", "wiggle", or None
        color: array-like set of colors, optional
          Specify a single color for all bars, one color per series, or one color per bar.
          Color values can be explicit toyplot colors, or scalar values to be mapped
          to colors using the `colormap` or `palette` parameter.
        opacity: array-like set of opacities, optional
          Specify a single opacity for all bars, one opacity per series, or one opacity per bar.
        title: array-like set of strings, optional
          Specify a single title, one title per series, or one title per bar.
        style: dict, optional
          Collection of CSS styles to be applied globally.

        Returns
        -------
        bars: :class:`toyplot.mark.BarBoundaries` or :class:`toyplot.mark.BarMagnitudes`
        """
        along = toyplot.require.value_in(along, ["x", "y"])

        if baseline is None:
            if a is not None and b is not None and c is not None:
                a = toyplot.require.scalar_vector(a)
                b = toyplot.require.scalar_vector(b, len(a))
                c = toyplot.require.scalar_array(c)
                if c.ndim == 1:
                    c = toyplot.require.scalar_vector(c, len(a))
                    series = numpy.ma.column_stack(
                        (numpy.repeat(0, len(c)), c))
                elif c.ndim == 2:
                    series = toyplot.require.scalar_matrix(c)
                position = numpy.ma.column_stack((a, b))
            elif a is not None and b is not None:
                a = toyplot.require.scalar_vector(a)
                b = toyplot.require.scalar_array(b)
                if b.ndim == 1:
                    b = toyplot.require.scalar_vector(b, len(a))
                    series = numpy.ma.column_stack(
                        (numpy.repeat(0, len(b)), b))
                elif b.ndim == 2:
                    series = toyplot.require.scalar_matrix(b)
                position = numpy.concatenate(
                    (a[0:1] - (a[1:2] - a[0:1]) * 0.5, (a[:-1] + a[1:]) * 0.5, a[-1:] + (a[-1:] - a[-2:-1]) * 0.5))
                position = numpy.ma.column_stack((position[:-1], position[1:]))
            else:
                a = toyplot.require.scalar_array(a)
                if a.ndim == 1:
                    a = toyplot.require.scalar_vector(a)
                    series = numpy.ma.column_stack(
                        (numpy.repeat(0, len(a)), a))
                elif a.ndim == 2:
                    series = toyplot.require.scalar_matrix(a)
                position = numpy.ma.column_stack((numpy.arange(series.shape[0]) - 0.5, numpy.arange(series.shape[0]) + 0.5))

            default_color = [next(self._bar_colors)
                             for i in range(series.shape[1] - 1)]
            color = toyplot.color.broadcast(
                colors=color,
                shape=(series.shape[0], series.shape[1] - 1),
                default=default_color,
                )
            opacity = toyplot.broadcast.scalar(
                opacity, (series.shape[0], series.shape[1] - 1))
            title = toyplot.broadcast.object(
                title, (series.shape[0], series.shape[1] - 1))
            style = toyplot.style.combine(
                {"stroke": "white", "stroke-width": 1.0}, toyplot.require.style(style))

            if along == "x":
                self._update_domain(position, series)
                coordinate_axes = ["x", "y"]
            elif along == "y":
                self._update_domain(series, position)
                coordinate_axes = ["y", "x"]

            table = toyplot.data.Table()
            table["left"] = position.T[0]
            _mark_exportable(table, "left")
            table["right"] = position.T[1]
            _mark_exportable(table, "right")
            boundary_keys = []
            fill_keys = []
            opacity_keys = []
            title_keys = []

            boundary_keys.append("boundary0")
            table[boundary_keys[-1]] = series.T[0]

            for index, (boundary_column, fill_column, opacity_column, title_column) in enumerate(
                    zip(series.T[1:], color.T, opacity.T, title.T)):
                boundary_keys.append("boundary" + str(index + 1))
                fill_keys.append("fill" + str(index))
                opacity_keys.append("opacity" + str(index))
                title_keys.append("title" + str(index))
                table[boundary_keys[-1]] = boundary_column
                _mark_exportable(table, boundary_keys[-1])
                table[fill_keys[-1]] = fill_column
                table[opacity_keys[-1]] = opacity_column
                table[title_keys[-1]] = title_column

            self._children.append(
                toyplot.mark.BarBoundaries(
                    coordinate_axes=coordinate_axes,
                    table=table,
                    left="left",
                    right="right",
                    boundaries=boundary_keys,
                    fill=fill_keys,
                    opacity=opacity_keys,
                    title=title_keys,
                    style=style,
                    filename=filename))
            return self._children[-1]
        else:  # baseline is not None
            if a is not None and b is not None and c is not None:
                a = toyplot.require.scalar_vector(a)
                b = toyplot.require.scalar_vector(b, len(a))
                c = toyplot.require.scalar_array(c)
                if c.ndim == 1:
                    c = toyplot.require.scalar_vector(c, len(a))
                    series = numpy.ma.column_stack((c,))
                elif c.ndim == 2:
                    series = toyplot.require.scalar_matrix(c, rows=len(a))
                position = numpy.ma.column_stack((a, b))
            elif a is not None and b is not None:
                a = toyplot.require.scalar_vector(a)
                b = toyplot.require.scalar_array(b)
                if b.ndim == 1:
                    b = toyplot.require.scalar_vector(b, len(a))
                    series = numpy.ma.column_stack((b,))
                elif b.ndim == 2:
                    series = toyplot.require.scalar_matrix(b, rows=len(a))
                position = numpy.concatenate(
                    (a[0:1] - (a[1:2] - a[0:1]) * 0.5, (a[:-1] + a[1:]) * 0.5, a[-1:] + (a[-1:] - a[-2:-1]) * 0.5))
                position = numpy.ma.column_stack((position[:-1], position[1:]))
            elif a is not None:
                if isinstance(a, tuple) and len(a) == 2:
                    counts, edges = a
                    position = numpy.ma.column_stack((edges[:-1], edges[1:]))
                    series = numpy.ma.column_stack((toyplot.require.scalar_vector(counts, len(position)), ))
                else:
                    a = toyplot.require.scalar_array(a)
                    if a.ndim == 1:
                        series = numpy.ma.column_stack((a,))
                    elif a.ndim == 2:
                        series = a
                    position = numpy.ma.column_stack((numpy.arange(series.shape[0]) - 0.5, numpy.arange(series.shape[0]) + 0.5))

            default_color = [next(self._bar_colors)
                             for i in range(series.shape[1])]
            color = toyplot.color.broadcast(
                colors=color,
                shape=series.shape,
                default=default_color,
                )
            opacity = toyplot.broadcast.scalar(opacity, series.shape)
            title = toyplot.broadcast.object(title, series.shape)
            style = toyplot.style.combine(
                {"stroke": "white", "stroke-width": 1.0}, toyplot.require.style(style))

            if baseline == "stacked":
                baseline = numpy.zeros(series.shape[0])
            elif baseline == "symmetric":
                baseline = -0.5 * numpy.sum(series, axis=1)
            elif baseline == "wiggle":
                n = series.shape[1]
                baseline = numpy.zeros(series.shape[0])
                for i in range(n):
                    for j in range(i):
                        baseline += series.T[j]
                baseline *= -(1.0 / (n + 1))

            boundaries = numpy.cumsum(
                numpy.column_stack((baseline, series)), axis=1)
            if along == "x":
                self._update_domain(position, boundaries)
                coordinate_axes = ["x", "y"]
            elif along == "y":
                self._update_domain(boundaries, position)
                coordinate_axes = ["y", "x"]

            table = toyplot.data.Table()
            table["left"] = position.T[0]
            _mark_exportable(table, "left")
            table["right"] = position.T[1]
            _mark_exportable(table, "right")
            table["baseline"] = baseline
            _mark_exportable(table, "baseline")
            magnitude_keys = []
            fill_keys = []
            opacity_keys = []
            title_keys = []
            for index, (magnitude_column, fill_column, opacity_column, title_column) in enumerate(
                    zip(series.T, color.T, opacity.T, title.T)):
                magnitude_keys.append("magnitude" + str(index))
                fill_keys.append("fill" + str(index))
                opacity_keys.append("opacity" + str(index))
                title_keys.append("title" + str(index))
                table[magnitude_keys[-1]] = magnitude_column
                _mark_exportable(table, magnitude_keys[-1])
                table[fill_keys[-1]] = fill_column
                table[opacity_keys[-1]] = opacity_column
                table[title_keys[-1]] = title_column

            self._children.append(
                toyplot.mark.BarMagnitudes(
                    coordinate_axes=coordinate_axes,
                    table=table,
                    left="left",
                    right="right",
                    baseline="baseline",
                    magnitudes=magnitude_keys,
                    fill=fill_keys,
                    opacity=opacity_keys,
                    title=title_keys,
                    style=style,
                    filename=filename))
            return self._children[-1]

    def colorbar(
            self,
            values=None,
            palette=None,
            colormap=None,
            label=None,
            min=None,
            max=None,
            tick_length=5,
            tick_locator=None,
            offset=0,
            width=10,
            style=None):
        if colormap is None:
            if palette is None:
                palette = toyplot.color.brewer("BlueGreen")
            colormap = toyplot.color.LinearMap(palette=palette)
        style = toyplot.require.style(style)

        mark = toyplot.mark.VColorBar(
            xmin_range=self._xmax_range +
            offset,
            xmax_range=self._xmax_range +
            offset +
            width,
            ymin_range=self._ymin_range,
            ymax_range=self._ymax_range,
            label=label,
            colormap=colormap,
            padding=self._padding,
            tick_length=tick_length,
            min=min,
            max=max,
            tick_locator=tick_locator,
            style=style)
        if values is not None:
            mark._update_domain(numpy.min(values), numpy.max(values))
        self._parent._children.append(mark)
        return mark

    def fill(
            self,
            a,
            b=None,
            c=None,
            along="x",
            baseline=None,
            color=None,
            opacity=1.0,
            title=None,
            style=None,
            filename=None):
        """Fill multiple regions separated by curves.

        Parameters
        ----------
        a, b, c: array-like sets of coordinates
          If `a`, `b`, and `c` are provided, they specify the X coordinates, bottom
          coordinates, and top coordinates of the region respectively.  If only `a`
          and `b` are provided, they specify the X coordinates and top
          coordinates, with the bottom coordinates lying on the X axis.  If only `a` is
          provided, it specifies the top coordinates, with the bottom coordinates lying
          on the X axis and the X coordinates ranging from [0, N).
        title: string, optional
          Human-readable title for the mark.  The SVG / HTML backends render the
          title as a tooltip.
        style: dict, optional
          Collection of CSS styles to apply to the mark.  See
          :class:`toyplot.mark.FillBoundaries` for a list of useful styles.

        Returns
        -------
        mark: :class:`toyplot.mark.FillBoundaries` or :class:`toyplot.mark.FillMagnitudes`
        """
        along = toyplot.require.value_in(along, ["x", "y"])

        if baseline is None:
            if a is not None and b is not None and c is not None:
                position = toyplot.require.scalar_vector(a)
                bottom = toyplot.require.scalar_vector(b, len(position))
                top = toyplot.require.scalar_vector(c, len(position))
                series = numpy.ma.column_stack((bottom, top))
            elif a is not None and b is not None:
                position = toyplot.require.scalar_vector(a)
                b = toyplot.require.scalar_array(b)
                if b.ndim == 1:
                    bottom = numpy.ma.repeat(0, len(a))
                    top = toyplot.require.scalar_vector(b, len(a))
                    series = numpy.ma.column_stack((bottom, top))
                elif b.ndim == 2:
                    series = toyplot.require.scalar_matrix(b)
            else:
                a = toyplot.require.scalar_array(a)
                if a.ndim == 1:
                    bottom = numpy.ma.repeat(0, len(a))
                    top = toyplot.require.scalar_vector(a)
                    series = numpy.ma.column_stack((bottom, top))
                    position = numpy.ma.arange(series.shape[0])
                elif a.ndim == 2:
                    series = toyplot.require.scalar_matrix(a)
                    position = numpy.ma.arange(series.shape[0])

            default_color = [next(self._fill_colors)
                             for i in range(series.shape[1] - 1)]
            color = toyplot.color.broadcast(
                colors=color,
                shape=(series.shape[1] - 1,),
                default=default_color,
                )
            opacity = toyplot.broadcast.scalar(opacity, series.shape[1] - 1)
            title = toyplot.broadcast.object(title, series.shape[1] - 1)
            style = toyplot.style.combine(
                {"stroke": "none"}, toyplot.require.style(style))

            if along == "x":
                self._update_domain(position, series)
                coordinate_axes = ["x", "y"]
            elif along == "y":
                self._update_domain(series, position)
                coordinate_axes = ["y", "x"]

            table = toyplot.data.Table()
            table[coordinate_axes[0]] = position
            _mark_exportable(table, coordinate_axes[0])
            boundaries = []
            for index, column in enumerate(series.T):
                key = coordinate_axes[1] + str(index)
                table[key] = column
                _mark_exportable(table, key)
                boundaries.append(key)

            self._children.append(
                toyplot.mark.FillBoundaries(
                    coordinate_axes=coordinate_axes,
                    table=table,
                    position=[coordinate_axes[0]],
                    boundaries=boundaries,
                    fill=color,
                    opacity=opacity,
                    title=title,
                    style=style,
                    filename=filename))
            return self._children[-1]
        else:  # baseline is not None
            if a is not None and b is not None:
                b = toyplot.require.scalar_array(b)
                if b.ndim == 1:
                    series = numpy.ma.column_stack((b,))
                elif b.ndim == 2:
                    series = b
                position = toyplot.require.scalar_vector(a, series.shape[0])
            else:
                a = toyplot.require.scalar_array(a)
                if a.ndim == 1:
                    series = numpy.ma.column_stack((a,))
                elif a.ndim == 2:
                    series = a
                position = numpy.ma.arange(series.shape[0])

            default_color = [next(self._fill_colors)
                             for i in range(series.shape[1])]
            color = toyplot.color.broadcast(
                colors=color,
                shape=(series.shape[1],),
                default=default_color,
                )
            opacity = toyplot.broadcast.scalar(opacity, series.shape[1])
            title = toyplot.broadcast.object(title, series.shape[1])
            style = toyplot.style.combine(
                {"stroke": "none"}, toyplot.require.style(style))

            if isinstance(baseline, toyplot.compatibility.string_type):
                baseline = toyplot.require.value_in(
                    baseline, ["stacked", "symmetric", "wiggle"])
                if baseline == "stacked":
                    baseline = numpy.ma.zeros(series.shape[0])
                elif baseline == "symmetric":
                    baseline = -0.5 * numpy.ma.sum(series, axis=1)
                elif baseline == "wiggle":
                    n = series.shape[1]
                    baseline = numpy.ma.zeros(series.shape[0])
                    for i in range(n):
                        for j in range(i):
                            baseline += series.T[j]
                    baseline *= -(1.0 / (n + 1))

            boundaries = numpy.ma.cumsum(
                numpy.ma.column_stack((baseline, series)), axis=1)
            if along == "x":
                self._update_domain(position, boundaries)
                coordinate_axes = ["x", "y"]
            elif along == "y":
                self._update_domain(boundaries, position)
                coordinate_axes = ["y", "x"]

            table = toyplot.data.Table()
            table[coordinate_axes[0]] = position
            _mark_exportable(table, coordinate_axes[0])
            table["baseline"] = baseline
            magnitudes = []
            for index, column in enumerate(series.T):
                key = coordinate_axes[1] + str(index)
                table[key] = column
                _mark_exportable(table, key)
                magnitudes.append(key)

            self._children.append(
                toyplot.mark.FillMagnitudes(
                    coordinate_axes=coordinate_axes,
                    table=table,
                    position=[coordinate_axes[0]],
                    baseline=["baseline"],
                    magnitudes=magnitudes,
                    fill=color,
                    opacity=opacity,
                    title=title,
                    style=style,
                    filename=filename))
            return self._children[-1]

    def graph(
            self,
            a,
            b=None,
            c=None,
            olayout=None,
            layout=None,
            along="x",
            vlabel=None,
            vcoordinates=None,
            vcolor=None,
            vmarker="o",
            varea=None,
            vsize=None,
            vopacity=1.0,
            vtitle=None,
            vstyle=None,
            vlstyle=None,
            vlshow=True,
            ecolor=None,
            ewidth=1.0,
            eopacity=1.0,
            estyle=None,
        ): # pragma: no cover
        """Add a graph plot to the axes.

        Parameters
        ----------

        Returns
        -------
        plot: :class:`toyplot.mark.Graph`
        """
        layout = toyplot.layout.graph(a, b, c, olayout=olayout, layout=layout, vcoordinates=vcoordinates)

        along = toyplot.require.value_in(along, ["x", "y"])

        if vlabel is None:
            vlabel = layout.vids

        default_color = [next(self._graph_colors)]
        vcolor = toyplot.color.broadcast(
            colors=vcolor,
            shape=layout.vcount,
            default=default_color,
            )

        vmarker = toyplot.broadcast.object(vmarker, layout.vcount)

        if varea is None and vsize is None:
            vsize = numpy.sqrt(toyplot.broadcast.scalar(20, layout.vcount))
        elif varea is None and vsize is not None:
            vsize = toyplot.broadcast.scalar(vsize, layout.vcount)
        elif varea is not None and vsize is None:
            vsize = numpy.sqrt(toyplot.broadcast.scalar(varea, layout.vcount))
        elif varea is not None and vsize is not None:
            toyplot.log.warning("Graph vsize parameter overrides varea.")
            vsize = toyplot.broadcast.scalar(vsize, layout.vcount)

        vopacity = toyplot.broadcast.scalar(vopacity, layout.vcount)
        vtitle = toyplot.broadcast.object(vtitle, layout.vcount)
        vstyle = toyplot.style.combine({}, toyplot.require.style(vstyle))
        vlstyle = toyplot.style.combine(
            {
                "font-size": "12px",
                "font-weight": "normal",
                "stroke": "none",
                "text-anchor": "middle",
                "alignment-baseline": "middle",
            },
            toyplot.require.style(vlstyle),
            )

        ecolor = toyplot.color.broadcast(
            colors=ecolor,
            shape=layout.ecount,
            default=default_color,
            )
        ewidth = toyplot.broadcast.scalar(ewidth, layout.ecount)
        eopacity = toyplot.broadcast.scalar(eopacity, layout.ecount)
        estyle = toyplot.style.combine(
            {}, toyplot.require.style(estyle))

        if along == "x":
            self._update_domain(layout.vcoordinates.T[0], layout.vcoordinates.T[1])
            self._update_domain(layout.ecoordinates.T[0], layout.ecoordinates.T[1])
            coordinate_axes = ["x", "y"]
        elif along == "y":
            self._update_domain(layout.vcoordinates.T[1], layout.vcoordinates.T[0])
            self._update_domain(layout.ecoordinates.T[1], layout.ecoordinates.T[0])
            coordinate_axes = ["y", "x"]

        vtable = toyplot.data.Table()
        vtable["id"] = layout.vids
        for axis, coordinates in zip(coordinate_axes, layout.vcoordinates.T):
            vtable[axis] = coordinates
            _mark_exportable(vtable, axis)
        vtable["label"] = vlabel
        vtable["marker"] = vmarker
        vtable["size"] = vsize
        vtable["color"] = vcolor
        vtable["opacity"] = vopacity
        vtable["title"] = vtitle

        etable = toyplot.data.Table()
        etable["source"] = layout.edges.T[0]
        _mark_exportable(etable, "source")
        etable["target"] = layout.edges.T[1]
        _mark_exportable(etable, "target")
        etable["shape"] = layout.eshapes
        etable["color"] = ecolor
        etable["width"] = ewidth
        etable["opacity"] = eopacity

        self._children.append(
            toyplot.mark.Graph(
                coordinate_axes=coordinate_axes,
                vtable=vtable,
                vid=["id"],
                vlabel=["label"],
                vcoordinates=coordinate_axes,
                vmarker=["marker"],
                vsize=["size"],
                vcolor=["color"],
                vopacity=["opacity"],
                vtitle=["title"],
                vstyle=vstyle,
                vlstyle=vlstyle,
                vlshow=vlshow,
                etable=etable,
                esource=["source"],
                etarget=["target"],
                eshape=["shape"],
                ecoordinates=layout.ecoordinates,
                ecolor=["color"],
                ewidth=["width"],
                eopacity=["opacity"],
                estyle=estyle))
        return self._children[-1]

    def hlines(
            self,
            y,
            color=None,
            opacity=1.0,
            title=None,
            style=None,
            annotation=True,
        ):
        """Add horizontal line(s) to the axes.

        Horizontal lines are convenient because they're guaranteed to fill the axes from
        left to right regardless of the axes size.

        Parameters
        ----------
        y: array-like set of Y coordinates
          One horizontal line will be drawn through each Y coordinate provided.
        title: string, optional
          Human-readable title for the mark.  The SVG / HTML backends render the
          title as a tooltip.
        style: dict, optional
          Collection of CSS styles to apply to the mark.  See
          :class:`toyplot.mark.AxisLines` for a list of useful styles.
        annotation: boolean, optional
          Set to True if this mark should be considered an annotation.

        Returns
        -------
        hlines: :class:`toyplot.mark.AxisLines`
        """
        table = toyplot.data.Table()
        table["y"] = toyplot.require.scalar_vector(y)
        _mark_exportable(table, "y", not annotation)
        color = toyplot.color.broadcast(
            colors=color,
            shape=(table.shape[0], 1),
            default=toyplot.color.near_black,
            )
        table["color"] = color[:, 0]
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.object(title, table.shape[0])
        style = toyplot.style.combine(toyplot.require.style(style))

        self._update_domain(numpy.array([]), table["y"], display=True, data=not annotation)

        self._children.append(
            toyplot.mark.AxisLines(
                coordinate_axes=["y"],
                table=table,
                coordinates=["y"],
                stroke=["color"],
                opacity=["opacity"],
                title=["title"],
                style=style))
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
        """Add a legend to the axes.

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
          absolute drawing units, or as a percentage of the axes width / height
          using strings that end with "%".
        rect: (x, y, width, height) tuple, optional
          Use the rect property to position / size the legend by specifying its
          upper-left-hand corner, width, and height.  Each parameter may be specified
          in absolute drawing units, or as a percentage of the axes width / height
          using strings that end with "%".
        corner: (corner, width, height, inset) tuple, optional
          Use the corner property to position / size the legend by specifying its
          width and height, plus an inset from a corner of the axes.  Allowed
          corner values are "top-left", "top", "top-right", "right",
          "bottom-right", "bottom", "bottom-left", and "left".  The width and
          height may be specified in absolute drawing units, or as a percentage of
          the axes width / height using strings that end with "%".  The inset is
          specified in absolute drawing units.
        grid: (rows, columns, index) tuple, or (rows, columns, i, j) tuple, or (rows, columns, i, rowspan, j, columnspan) tuple, optional
          Use the grid property to position / size the legend using a collection of
          grid cells filling the axes.  Specify the number of rows and columns in
          the grid, then specify either a zero-based cell index (which runs in
          left-ot-right, top-to-bottom order), a pair of i, j cell coordinates, or
          a set of i, column-span, j, row-span coordinates so the legend can cover
          more than one cell.
        gutter: size of the gutter around grid cells, optional
          Specifies the amount of empty space to leave between grid cells When using the
          `grid` parameter to position the legend.
        style: dict, optional

        Returns
        -------
        legend: :class:`toyplot.mark.Legend`
        """
        gutter = toyplot.require.scalar(gutter)
        style = toyplot.style.combine(toyplot.require.style(style))
        label_style = toyplot.style.combine(toyplot.require.style(label_style))

        xmin, xmax, ymin, ymax = toyplot.layout.region(
            self._xmin_range, self._xmax_range, self._ymin_range, self._ymax_range, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
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

    def plot(
            self,
            a,
            b=None,
            along="x",
            color=None,
            stroke_width=2.0,
            opacity=1.0,
            title=None,
            marker=None,
            size=20,
            mfill=None,
            mopacity=1.0,
            mtitle=None,
            style=None,
            mstyle=None,
            mlstyle=None,
            filename=None):
        """Add bivariate line plots to the axes.

        Parameters
        ----------
        a, b: array-like sets of coordinates
          If `a` and `b` are provided, they specify the first and second
          coordinates respectively of each point in the plot.  If only `a` is provided, it
          provides second coordinates, and the first coordinates will range from [0, N).
        along: string, optional
          Controls the mapping from coordinates to axes.  When set to "x" (the default),
          first and second coordinates map to the X and Y axes.  When set to "y", the
          coordinates are reversed.
        color: array-like, optional
          Overrides the default per-series colors provided by the axis palette.  Specify
          one color, or one-color-per-series.  Colors may be CSS colors, toyplot colors,
          or scalar values that will be mapped to colors using `colormap` or `palette`.
        stroke_width: array-like, optional
          Overrides the default stroke width of the plots.  Specify one width in drawing
          units, or one-width-per-series.
        stroke_opacity: array-like, optional
          Overrides the default opacity of the plots.  Specify one opacity, or one-opacity-per-series.
        marker: array-like, optional
          Allows markers to be rendered for each plot datum. Specify one marker,
          one-marker-per-series, or one-marker-per-datum.  Markers can use the
          string marker type as a shortcut, or a full marker specification.
        size: array-like, optional
          Controls marker sizes.  Specify one size, one-size-per-series, or one-size-per-datum.
        fill: array-like, optional
          Override the fill color for markers, which defaults to the per-series color specified
          by `color`.  Specify one color, one-color-per-series, or one-color-per-datum.  Colors
          may be CSS colors, toyplot colors, or scalar values that will be mapped to colors using
          `fill_colormap` or `fill_palette`.
        opacity: array-like, optional
          Overrides the default opacity of the markers.  Specify one opacity, one-opacity-per-series,
          or one-opacity-per-datum.
        title: array-like, optional
          Human-readable title for the data series.  The SVG / HTML backends render the
          title using tooltips.  Specify one title or one-title-per-series.
        style: dict, optional
          Collection of CSS styles applied to all plots.
        mstyle: dict, optional
          Collection of CSS styles applied to all markers.
        mlstyle: dict, optional
          Collection of CSS styles applied to all marker labels.

        Returns
        -------
        mark: :class:`toyplot.mark.Plot`
        """
        along = toyplot.require.value_in(along, ["x", "y"])

        if a is not None and b is not None:
            position = toyplot.require.scalar_vector(a)
            b = toyplot.require.scalar_array(b)
            if b.ndim == 1:
                b = toyplot.require.scalar_vector(b, len(position))
                series = numpy.ma.column_stack((b,))
            elif b.ndim == 2:
                series = toyplot.require.scalar_matrix(b, rows=len(position))
        else:
            a = toyplot.require.scalar_array(a)
            if a.ndim == 1:
                series = numpy.ma.column_stack((a,))
                position = numpy.ma.arange(series.shape[0])
            elif a.ndim == 2:
                series = a
                position = numpy.ma.arange(series.shape[0])

        default_color = [next(self._plot_colors)
                         for i in range(series.shape[1])]
        stroke = toyplot.color.broadcast(
            colors=color,
            shape=(series.shape[1],),
            default=default_color,
            )
        stroke_width = toyplot.broadcast.scalar(stroke_width, series.shape[1])
        stroke_opacity = toyplot.broadcast.scalar(
            opacity, series.shape[1])
        stroke_title = toyplot.broadcast.object(title, series.shape[1])
        marker = toyplot.broadcast.object(marker, series.shape)
        msize = toyplot.broadcast.scalar(size, series.shape)
        mfill = toyplot.color.broadcast(
            colors=mfill,
            shape=series.shape,
            default=stroke,
            )
        mstroke = toyplot.color.broadcast(colors=mfill, shape=series.shape)
        mopacity = toyplot.broadcast.scalar(mopacity, series.shape)
        mtitle = toyplot.broadcast.object(mtitle, series.shape)
        style = toyplot.style.combine(
            {"fill": "none"}, toyplot.require.style(style))
        mstyle = toyplot.style.combine({}, toyplot.require.style(mstyle))
        mlstyle = toyplot.style.combine(toyplot.require.style(mlstyle))

        if along == "x":
            self._update_domain(position, series)
            coordinate_axes = ["x", "y"]
        elif along == "y":
            self._update_domain(series, position)
            coordinate_axes = ["y", "x"]

        table = toyplot.data.Table()
        table[coordinate_axes[0]] = position
        _mark_exportable(table, coordinate_axes[0])
        series_keys = []
        marker_keys = []
        msize_keys = []
        mfill_keys = []
        mstroke_keys = []
        mopacity_keys = []
        mtitle_keys = []
        for index, (series_column, marker_column, msize_column, mfill_column, mstroke_column, mopacity_column, mtitle_column) in enumerate(
                zip(series.T, marker.T, msize.T, mfill.T, mstroke.T, mopacity.T, mtitle.T)):
            series_keys.append(coordinate_axes[1] + str(index))
            marker_keys.append("marker" + str(index))
            msize_keys.append("size" + str(index))
            mfill_keys.append("fill" + str(index))
            mstroke_keys.append("stroke" + str(index))
            mopacity_keys.append("opacity" + str(index))
            mtitle_keys.append("title" + str(index))
            table[series_keys[-1]] = series_column
            _mark_exportable(table, series_keys[-1])
            table[marker_keys[-1]] = marker_column
            table[msize_keys[-1]] = msize_column
            table[mfill_keys[-1]] = mfill_column
            table[mstroke_keys[-1]] = mstroke_column
            table[mopacity_keys[-1]] = mopacity_column
            table[mtitle_keys[-1]] = mtitle_column

        self._children.append(
            toyplot.mark.Plot(
                coordinate_axes=coordinate_axes,
                table=table,
                coordinates=[coordinate_axes[0]],
                series=series_keys,
                stroke=stroke,
                stroke_width=stroke_width,
                stroke_opacity=stroke_opacity,
                stroke_title=stroke_title,
                marker=marker_keys,
                msize=msize_keys,
                mfill=mfill_keys,
                mstroke=mstroke_keys,
                mopacity=mopacity_keys,
                mtitle=mtitle_keys,
                style=style,
                mstyle=mstyle,
                mlstyle=mlstyle,
                filename=filename))
        return self._children[-1]

    def rects(
            self,
            a,
            b,
            c,
            d,
            along="x",
            color=None,
            opacity=1.0,
            title=None,
            style={"stroke": "none"},
            filename=None,
        ):
        table = toyplot.data.Table()
        table["left"] = toyplot.require.scalar_vector(a)
        table["right"] = toyplot.require.scalar_vector(
            b, length=table.shape[0])
        table["top"] = toyplot.require.scalar_vector(c, length=table.shape[0])
        table["bottom"] = toyplot.require.scalar_vector(
            d, length=table.shape[0])
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.object(title, table.shape[0])
        style = toyplot.style.combine(toyplot.require.style(style))

        default_color = [next(self._rect_colors)]
        table["toyplot:fill"] = toyplot.color.broadcast(
            colors=color,
            shape=(table.shape[0], 1),
            default=default_color,
            )[:, 0]

        if along == "x":
            coordinate_axes = ["x", "y"]
            self._update_domain(
                numpy.concatenate((table["left"], table["right"])),
                numpy.concatenate((table["top"], table["bottom"])),
            )
        elif along == "y":
            coordinate_axes = ["y", "x"]
            self._update_domain(
                numpy.concatenate((table["top"], table["bottom"])),
                numpy.concatenate((table["left"], table["right"])),
            )

        self._children.append(
            toyplot.mark.Rect(
                coordinate_axes,
                table=table,
                left=["left"],
                right=["right"],
                top=["top"],
                bottom=["bottom"],
                fill=["toyplot:fill"],
                opacity=["opacity"],
                title=["title"],
                style=style,
                filename=filename))
        return self._children[-1]

    def scatterplot(
            self,
            a,
            b=None,
            along="x",
            color=None,
            marker="o",
            size=20,
            opacity=1.0,
            title=None,
            style=None,
            mstyle=None,
            mlstyle=None,
            filename=None):
        """Add a bivariate plot to the axes.

        Parameters
        ----------
        a, b: array-like sets of coordinates
          If `a` and `b` are provided, they specify the X coordinates and Y
          coordinates of each point in the plot.  If only `a` is provided, it
          specifies the Y coordinates, and the X coordinates will range from [0, N).
        title: string, optional
          Human-readable title for the mark.  The SVG / HTML backends render the
          title as a tooltip.
        style: dict, optional
          Collection of CSS styles to apply across all datums.  See
          :class:`toyplot.toyplot.Plot` for a list of useful styles.

        Returns
        -------
        plot: :class:`toyplot.mark.Plot`
        """
        along = toyplot.require.value_in(along, ["x", "y"])

        if a is not None and b is not None:
            position = toyplot.require.scalar_vector(a)
            b = numpy.ma.array(b).astype("float64")
            if b.ndim == 0:
                b = toyplot.require.scalar_vector(b, len(position))
                series = numpy.ma.column_stack((b,))
            elif b.ndim == 1:
                b = toyplot.require.scalar_vector(b, len(position))
                series = numpy.ma.column_stack((b,))
            elif b.ndim == 2:
                series = toyplot.require.scalar_matrix(b, rows=len(position))
        else:
            a = numpy.ma.array(a).astype("float64")
            if a.ndim == 1:
                series = numpy.ma.column_stack((a,))
                position = numpy.ma.arange(series.shape[0])
            elif a.ndim == 2:
                series = a
                position = numpy.ma.arange(series.shape[0])

        default_color = [next(self._scatterplot_colors)
                         for i in range(series.shape[1])]
        mfill = toyplot.color.broadcast(
            colors=color,
            shape=series.shape,
            default=default_color,
            )
        marker = toyplot.broadcast.object(marker, series.shape)
        msize = toyplot.broadcast.scalar(size, series.shape)
        mstroke = toyplot.color.broadcast(colors=mfill, shape=series.shape)
        mopacity = toyplot.broadcast.scalar(opacity, series.shape)
        mtitle = toyplot.broadcast.object(title, series.shape)
        style = toyplot.style.combine(
            {"stroke": "none"}, toyplot.require.style(style))
        mstyle = toyplot.style.combine({}, toyplot.require.style(mstyle))
        mlstyle = toyplot.style.combine(toyplot.require.style(mlstyle))

        if along == "x":
            self._update_domain(position, series)
            coordinate_axes = ["x", "y"]
        elif along == "y":
            self._update_domain(series, position)
            coordinate_axes = ["y", "x"]

        table = toyplot.data.Table()
        table[coordinate_axes[0]] = position
        _mark_exportable(table, coordinate_axes[0])
        series_keys = []
        marker_keys = []
        msize_keys = []
        mfill_keys = []
        mstroke_keys = []
        mopacity_keys = []
        mtitle_keys = []
        for index, (series_column, marker_column, msize_column, mfill_column, mstroke_column, mopacity_column, mtitle_column) in enumerate(
                zip(series.T, marker.T, msize.T, mfill.T, mstroke.T, mopacity.T, mtitle.T)):
            series_keys.append(coordinate_axes[1] + str(index))
            marker_keys.append("marker" + str(index))
            msize_keys.append("size" + str(index))
            mfill_keys.append("fill" + str(index))
            mstroke_keys.append("stroke" + str(index))
            mopacity_keys.append("opacity" + str(index))
            mtitle_keys.append("title" + str(index))
            table[series_keys[-1]] = series_column
            _mark_exportable(table, series_keys[-1])
            table[marker_keys[-1]] = marker_column
            table[msize_keys[-1]] = msize_column
            table[mfill_keys[-1]] = mfill_column
            table[mstroke_keys[-1]] = mstroke_column
            table[mopacity_keys[-1]] = mopacity_column
            table[mtitle_keys[-1]] = mtitle_column

        self._children.append(
            toyplot.mark.Scatterplot(
                table=table,
                coordinate_axes=coordinate_axes,
                coordinates=[coordinate_axes[0]],
                series=series_keys,
                marker=marker_keys,
                msize=msize_keys,
                mfill=mfill_keys,
                mstroke=mstroke_keys,
                mopacity=mopacity_keys,
                mtitle=mtitle_keys,
                style=style,
                mstyle=mstyle,
                mlstyle=mlstyle,
                filename=filename))
        return self._children[-1]

    def share(
            self,
            axis="x",
            xmin=None,
            xmax=None,
            ymin=None,
            ymax=None,
            xlabel=None,
            ylabel=None,
            xticklocator=None,
            yticklocator=None,
            xscale="linear",
            yscale="linear",
            palette=None,
        ):
        """Create a Cartesian coordinate system with a shared axis.

        Parameters
        ----------
        axis: string, optional
            The axis that will be shared.  Allowed values are "x" and "y".
        xmin, xmax, ymin, ymax: float, optional
          Used to explicitly override the axis domain (normally, the domain is
          implicitly defined by any marks added to the axes).
        xlabel, ylabel: string, optional
          Human-readable axis labels.
        xticklocator, yticklocator: :class:`toyplot.locator.TickLocator`, optional
          Controls the placement and formatting of axis ticks and tick labels.
        xscale, yscale: "linear", "log", "log10", "log2", or a ("log", <base>) tuple, optional
          Specifies the mapping from data to canvas coordinates along an axis.
        palette: :class:`toyplot.color.Palette`, optional
          Color palette used to automatically select per-series colors for plotted data.

        Returns
        -------
        axes: :class:`toyplot.axes.Cartesian`
        """

        shared = Cartesian(
            xmin_range=self._xmin_range,
            xmax_range=self._xmax_range,
            ymin_range=self._ymin_range,
            ymax_range=self._ymax_range,
            aspect=self._aspect,
            xmin=xmin,
            xmax=xmax,
            ymin=ymin,
            ymax=ymax,
            show=True,
            xshow=True,
            yshow=True,
            label=None,
            xlabel=xlabel,
            ylabel=ylabel,
            xticklocator=xticklocator,
            yticklocator=yticklocator,
            xscale=xscale,
            yscale=yscale,
            palette=palette,
            padding=self._padding,
            parent=self._parent,
            xaxis=self.x if axis == "x" else None,
            yaxis=self.y if axis == "y" else None,
            )

        shared.x.spine.position = "high" if axis == "y" else "low"
        shared.y.spine.position = "high" if axis == "x" else "low"

        self._parent._children.append(shared)
        return self._parent._children[-1]

    def text(
            self,
            a,
            b,
            text,
            angle=0,
            color=None,
            opacity=1.0,
            title=None,
            style=None,
            filename=None,
            annotation=True):
        """Add text to the axes.

        Parameters
        ----------
        a, b: float
          Coordinates of the text anchor.
        text: string
          The text to be displayed.
        title: string, optional
          Human-readable title for the mark.  The SVG / HTML backends render the
          title as a tooltip.
        style: dict, optional
          Collection of CSS styles to apply to the mark.  See
          :class:`toyplot.mark.Text` for a list of useful styles.
        annotation: boolean, optional
          Set to True if this mark should be considered an annotation.

        Returns
        -------
        text: :class:`toyplot.mark.Text`
        """
        table = toyplot.data.Table()
        table["x"] = toyplot.require.scalar_vector(a)
        _mark_exportable(table, "x", not annotation)
        table["y"] = toyplot.require.scalar_vector(b, table.shape[0])
        _mark_exportable(table, "y", not annotation)
        table["text"] = toyplot.broadcast.object(text, table.shape[0])
        _mark_exportable(table, "text", not annotation)
        table["angle"] = toyplot.broadcast.scalar(angle, table.shape[0])
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.object(title, table.shape[0])
        style = toyplot.style.combine({"font-size": "12px",
                                       "font-weight": "normal",
                                       "stroke": "none",
                                       "text-anchor": "middle",
                                       "alignment-baseline": "middle"},
                                      toyplot.require.style(style))

        default_color = [next(self._text_colors)]

        color = toyplot.color.broadcast(
            colors=color,
            shape=(table.shape[0], 1),
            default=default_color,
            )
        table["fill"] = color[:, 0]

        self._update_domain(
            table["x"], table["y"], display=True, data=not annotation)
        self._expand_domain_range(table["x"], table["y"], toyplot.text.extents(
            table["text"], table["angle"], style))

        self._children.append(
            toyplot.mark.Text(
                coordinate_axes=["x", "y"],
                table=table,
                coordinates=["x", "y"],
                text=["text"],
                angle=["angle"],
                fill=["fill"],
                opacity=["opacity"],
                title=["title"],
                style=style,
                filename=filename))
        return self._children[-1]

    def vlines(
            self,
            x,
            color=None,
            opacity=1.0,
            title=None,
            style=None,
            annotation=True,
        ):
        """Add vertical line(s) to the axes.

        Vertical lines are convenient because they're guaranteed to fill the axes from
        top to bottom regardless of the axes size.

        Parameters
        ----------
        x: array-like set of X coordinates
          One vertical line will be drawn through each X coordinate provided.
        title: string, optional
          Human-readable title for the mark.  The SVG / HTML backends render the
          title as a tooltip.
        style: dict, optional
          Collection of CSS styles to apply to the mark.  See
          :class:`toyplot.mark.AxisLines` for a list of useful styles.
        annotation: boolean, optional
          Set to True if this mark should be considered an annotation.

        Returns
        -------
        hlines: :class:`toyplot.mark.AxisLines`
        """
        table = toyplot.data.Table()
        table["x"] = toyplot.require.scalar_vector(x)
        _mark_exportable(table, "x", not annotation)
        color = toyplot.color.broadcast(
            colors=color,
            shape=(table.shape[0], 1),
            default=toyplot.color.near_black,
            )
        table["color"] = color[:, 0]
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.object(title, table.shape[0])
        style = toyplot.style.combine(toyplot.require.style(style))

        self._update_domain(table["x"], numpy.array([]), display=True, data=not annotation)

        self._children.append(
            toyplot.mark.AxisLines(
                coordinate_axes=["x"],
                table=table,
                coordinates=["x"],
                stroke=["color"],
                opacity=["opacity"],
                title=["title"],
                style=style))
        return self._children[-1]

##########################################################################
# Table


class Table(object):
    """Experimental table coordinate system.
    """
    class Label(object):

        def __init__(self, label, style):
            self._text = label
            self._style = toyplot.style.combine(
                {
                    "font-weight": "bold",
                    "stroke": "none",
                    "text-anchor": "middle",
                    "alignment-baseline": "middle"},
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

    class Cell(object):

        def __init__(self, row=None, column=None, align=None, style=None):
            self._row = row
            self._column = column
            self._format = Table.Cell.default_format
            self._align = align
            self._angle = 0
            self._style = style
            self._bstyle = None
            self._data = None
            self._title = None
            self._width = None
            self._height = None
            self._left = None
            self._right = None
            self._top = None
            self._bottom = None
            self._column_offset = 0
            self._row_offset = 0
            self._parents = None

        @property
        def left(self):
            if self._left is None and self._parents is not None:
                self._left = numpy.min(
                    [parent._left for parent in self._parents.flat])
            return self._left

        @property
        def right(self):
            if self._right is None and self._parents is not None:
                self._right = numpy.max(
                    [parent._right for parent in self._parents.flat])
            return self._right

        @property
        def top(self):
            if self._top is None and self._parents is not None:
                self._top = numpy.min(
                    [parent._top for parent in self._parents.flat])
            return self._top

        @property
        def bottom(self):
            if self._bottom is None and self._parents is not None:
                self._bottom = numpy.max(
                    [parent._bottom for parent in self._parents.flat])
            return self._bottom

        default_format = toyplot.format.DefaultFormatter()

    class CellReference(object):

        def __init__(self, table, cells):
            self._table = table
            self._cells = cells

        def _set_show(self, value):
            if value:
                for cell in self._cells.flat:
                    self._table._visible_cells.add(cell)
            else:
                for cell in self._cells.flat:
                    self._table._visible_cells.remove(cell)
        show = property(fset=_set_show)

        def _set_data(self, value):
            for left, right in numpy.nditer(
                    [self._cells, value], flags=["refs_ok"], op_flags=[["readwrite"], ["readonly"]]):
                left[()]._data = right[()]
        data = property(fset=_set_data)

        def _set_title(self, value):
            for left, right in numpy.nditer(
                    [self._cells, value], flags=["refs_ok"], op_flags=[["readwrite"], ["readonly"]]):
                left[()]._title = right[()]
        title = property(fset=_set_title)

        def _set_format(self, value):
            for cell in self._cells.flat:
                cell._format = value
        format = property(fset=_set_format)

        def _set_align(self, value):
            for cell in self._cells.flat:
                cell._align = value
        align = property(fset=_set_align)

        def _set_angle(self, value):
            for cell in self._cells.flat:
                cell._angle = value
        angle = property(fset=_set_angle)

        def _set_style(self, value):
            value = toyplot.require.style(value)
            for cell in self._cells.flat:
                cell._style = toyplot.style.combine(cell._style, value)
        style = property(fset=_set_style)

        def _set_bstyle(self, value):
            value = toyplot.require.style(value)
            for cell in self._cells.flat:
                cell._bstyle = toyplot.style.combine(cell._bstyle, value)
        bstyle = property(fset=_set_bstyle)

        def _set_width(self, value):
            if self._table._finalized:
                raise ValueError("Cannot set cell widths after inserting axes into the table.")
            for cell in self._cells.flat:
                cell._width = toyplot.units.convert(value, "px", "px")
        width = property(fset=_set_width)

        def _set_height(self, value):
            if self._table._finalized:
                raise ValueError("Cannot set cell heights after inserting axes into the table.")
            for cell in self._cells.flat:
                cell._height = toyplot.units.convert(value, "px", "px")
        height = property(fset=_set_height)

        def _set_column_offset(self, value):
            for cell in self._cells.flat:
                cell._column_offset = value
        column_offset = property(fset=_set_column_offset)

        def _set_row_offset(self, value):
            for cell in self._cells.flat:
                cell._row_offset = value
        row_offset = property(fset=_set_row_offset)

        def axes(
                self,
                xmin=None,
                xmax=None,
                ymin=None,
                ymax=None,
                aspect=None,
                show=False,
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
                padding=5,
                cell_padding=0,
            ):
            self._table._finalize()
            left = numpy.min([cell.left for cell in self._cells.flat]) + cell_padding
            right = numpy.max([cell.right for cell in self._cells.flat]) - cell_padding
            top = numpy.min([cell.top for cell in self._cells.flat]) + cell_padding
            bottom = numpy.max([cell.bottom for cell in self._cells.flat]) - cell_padding

            axes = toyplot.axes.Cartesian(
                left,
                right,
                top,
                bottom,
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
                palette=palette,
                padding=padding,
                parent=self._table._parent,
                )
            axes.coordinates.show = False
            self._table._children.append(axes)
            return axes

        def merge(self):
            source = self._cells.flat[0]
            merged_cell = Table.Cell(align=source._align, style=source._style)
            merged_cell._parents = self._cells

            rows = numpy.unique([cell._row for cell in self._cells.flat])
            columns = numpy.unique([cell._column for cell in self._cells.flat])

            if len(rows) > 1:
                self._table._hmask[rows[1:], columns] = True
            if len(columns) > 1:
                self._table._vmask[rows, columns[1:]] = True

            for cell in self._cells.flat:
                self._table._visible_cells.remove(cell)
            self._table._visible_cells.add(merged_cell)
            return Table.CellReference(self._table, numpy.array(merged_cell))

    class GapReference(object):

        def __init__(self, rgaps, cgaps):
            self._rgaps = rgaps
            self._cgaps = cgaps

        @property
        def rows(self):
            return self._rgaps

        @property
        def columns(self):
            return self._cgaps

    class GridReference(object):

        def __init__(self, table, hlines, vlines):
            self._table = table
            self._hlines = hlines
            self._vlines = vlines

        @property
        def hlines(self):
            return self._hlines

        @property
        def vlines(self):
            return self._vlines

        @property
        def separation(self):
            return self._table._separation

        @separation.setter
        def separation(self, value):
            self._table._separation = value

        @property
        def style(self):
            return self._table._gstyle

        @style.setter
        def style(self, value):
            self._table._gstyle = toyplot.style.combine(
                self._table._gstyle, toyplot.require.style(value))

    class Region(object):

        def __init__(self, table, cells, hlines, vlines, rgaps, cgaps):
            self._table = table
            self._cells = cells
            self._hlines = hlines
            self._vlines = vlines
            self._rgaps = rgaps
            self._cgaps = cgaps

        @property
        def gaps(self):
            return Table.GapReference(self._rgaps, self._cgaps)

        @property
        def grid(self):
            return Table.GridReference(self._table, self._hlines, self._vlines)

        def column(self, column):
            return Table.CellReference(self._table, self._cells.T[column])

        def row(self, row):
            return Table.CellReference(self._table, self._cells[row])

        def cell(self, row, column, rowspan=1, colspan=1):
            return Table.CellReference(
                self._table,
                self._cells[
                    row: row +
                    rowspan,
                    column: column +
                    colspan])

        @property
        def shape(self):
            return self._cells.shape

        @property
        def rows(self):
            return self._cells.shape[0]

        @property
        def columns(self):
            return self._cells.shape[1]

        @property
        def cells(self):
            return Table.CellReference(self._table, self._cells)

    def __init__(
            self,
            xmin_range,
            xmax_range,
            ymin_range,
            ymax_range,
            rows,
            columns,
            trows,
            brows,
            lcols,
            rcols,
            label,
            parent):
        self._xmin_range = xmin_range
        self._xmax_range = xmax_range
        self._ymin_range = ymin_range
        self._ymax_range = ymax_range
        self._rows = rows
        self._columns = columns
        self._trows = trows
        self._brows = brows
        self._lcols = lcols
        self._rcols = rcols
        self._parent = parent
        self._children = []

        self._label = Table.Label(
            label, style={"font-size": "14px", "baseline-shift": "100%"})

        self._hlines = numpy.empty(
            (trows +
             rows +
             brows +
             1,
             lcols +
             columns +
             rcols +
             0),
            dtype=object)
        self._vlines = numpy.empty(
            (trows +
             rows +
             brows +
             0,
             lcols +
             columns +
             rcols +
             1),
            dtype=object)
        self._hmask = numpy.zeros(
            (trows +
             rows +
             brows +
             1,
             lcols +
             columns +
             rcols +
             0),
            dtype=bool)
        self._vmask = numpy.zeros(
            (trows +
             rows +
             brows +
             0,
             lcols +
             columns +
             rcols +
             1),
            dtype=bool)
        self._separation = 2
        self._gstyle = {
            "stroke": toyplot.color.near_black, "stroke-width": 0.5}

        self._rgaps = numpy.zeros(trows + rows + brows + 1)
        self._cgaps = numpy.zeros(lcols + columns + rcols + 1)

        hstyle = {
            "font-size": "12px",
            "stroke": "none",
            "fill": toyplot.color.near_black,
            "alignment-baseline": "middle",
            "font-weight": "bold"}
        style = {"font-size": "12px", "stroke": "none", "fill":
                 toyplot.color.near_black, "alignment-baseline": "middle"}

        self._cells = numpy.empty(
            (trows + rows + brows, lcols + columns + rcols), dtype="object")
        for row in range(trows + rows + brows):
            for column in range(lcols + columns + rcols):
                if row < trows or row >= trows + \
                        rows or column < lcols or column >= lcols + columns:
                    self._cells[row, column] = Table.Cell(
                        row, column, "center", hstyle)
                else:
                    self._cells[row, column] = Table.Cell(
                        row, column, "left", style)

        self._visible_cells = OrderedSet(numpy.ravel(self._cells))

        self._finalized = False

    @property
    def label(self):
        return self._label

    @property
    def shape(self):
        return self._cells.shape

    @property
    def rows(self):
        return self._cells.shape[0]

    @property
    def columns(self):
        return self._cells.shape[1]

    @property
    def header(self):
        return self.top

    @property
    def footer(self):
        return self.bottom

    @property
    def top(self):
        region = Table.Region(
            self,
            self._cells[
                0: self._trows, self._lcols: self._lcols + self._columns],
            self._hlines[
                0: self._trows + 1, self._lcols: self._lcols + self._columns],
            self._vlines[
                0: self._trows, self._lcols: self._lcols + self._columns + 1],
            self._rgaps[0: self._trows + 1],
            self._cgaps[self._lcols: self._lcols + self._columns],
        )

        region.left = Table.Region(
            self,
            self._cells[0: self._trows, 0: self._lcols],
            self._hlines[0: self._trows + 1, 0: self._lcols],
            self._vlines[0: self._trows, 0: self._lcols + 1],
            self._rgaps[0: self._trows + 1],
            self._cgaps[0: self._lcols],
        )

        region.right = Table.Region(
            self,
            self._cells[0: self._trows, self._lcols + self._columns:],
            self._hlines[0: self._trows + 1, self._lcols + self._columns:],
            self._vlines[0: self._trows, self._lcols + self._columns:],
            self._rgaps[0: self._trows + 1],
            self._cgaps[self._lcols + self._columns:],
        )

        return region

    @property
    def left(self):
        return Table.Region(
            self,
            self._cells[self._trows: self._trows + self._rows, 0: self._lcols],
            self._hlines[
                self._trows: self._trows + self._rows + 1, 0: self._lcols],
            self._vlines[
                self._trows: self._trows + self._rows, 0: self._lcols + 1],
            self._rgaps[self._trows: self._trows + self._rows + 1],
            self._cgaps[0: self._lcols],
        )

    @property
    def body(self):
        return Table.Region(
            self,
            self._cells[self._trows: self._trows + self._rows,
                        self._lcols: self._lcols + self._columns],
            self._hlines[self._trows: self._trows + self._rows +
                         1, self._lcols: self._lcols + self._columns],
            self._vlines[self._trows: self._trows + self._rows,
                         self._lcols: self._lcols + self._columns + 1],
            self._rgaps[self._trows: self._trows + self._rows],
            self._cgaps[self._lcols: self._lcols + self._columns],
        )

    @property
    def right(self):
        return Table.Region(
            self,
            self._cells[
                self._trows: self._trows +
                self._rows,
                self._lcols +
                self._columns:],
            self._hlines[
                self._trows: self._trows +
                self._rows +
                1,
                self._lcols +
                self._columns:],
            self._vlines[
                self._trows: self._trows +
                self._rows,
                self._lcols +
                self._columns:],
            self._rgaps[
                self._trows: self._trows +
                self._rows +
                1],
            self._cgaps[
                self._lcols +
                self._columns:],
        )

    @property
    def bottom(self):
        region = Table.Region(
            self,
            self._cells[
                self._trows +
                self._rows:,
                self._lcols: self._lcols +
                self._columns],
            self._hlines[
                self._trows +
                self._rows:,
                self._lcols: self._lcols +
                self._columns],
            self._vlines[
                self._trows +
                self._rows:,
                self._lcols: self._lcols +
                self._columns +
                1],
            self._rgaps[
                self._trows +
                self._rows:],
            self._cgaps[
                self._lcols: self._lcols +
                self._columns],
        )

        region.left = Table.Region(
            self,
            self._cells[self._trows + self._rows:, 0: self._lcols],
            self._hlines[self._trows + self._rows:, 0: self._lcols],
            self._vlines[self._trows + self._rows:, 0: self._lcols + 1],
            self._rgaps[self._trows + self._rows:],
            self._cgaps[0: self._lcols],
        )

        region.right = Table.Region(
            self,
            self._cells[
                self._trows + self._rows:, self._lcols + self._columns:],
            self._hlines[
                self._trows + self._rows:, self._lcols + self._columns:],
            self._vlines[
                self._trows + self._rows:, self._lcols + self._columns:],
            self._rgaps[self._trows + self._rows:],
            self._cgaps[self._lcols + self._columns:],
        )

        return region

    @property
    def gaps(self):
        return Table.GapReference(self._rgaps, self._cgaps)

    @property
    def grid(self):
        return Table.GridReference(self, self._hlines, self._vlines)

    def column(self, column):
        return Table.CellReference(self, self._cells.T[column])

    def row(self, row):
        return Table.CellReference(self, self._cells[row])

    def cell(self, row, column, rowspan=1, colspan=1):
        return Table.CellReference(
            self,
            self._cells[
                row: row +
                rowspan,
                column: column +
                colspan])

    def _finalize(self):
        if self._finalized:
            return
        self._finalized = True

        # Collect explicit column widths and row heights.
        column_widths = numpy.zeros(self._cells.shape[1])
        for cell in self._cells.flat:
            if cell._width is not None:
                column_widths[cell._column] = max(
                    column_widths[cell._column], cell._width)

        row_heights = numpy.zeros(self._cells.shape[0])
        for cell in self._cells.flat:
            if cell._height is not None:
                row_heights[cell._row] = max(
                    row_heights[cell._row], cell._height)

        # Compute implicit column widths and row heights for the remaining
        # cells.
        table_width = self._xmax_range - self._xmin_range
        available_width = table_width - \
            numpy.sum(column_widths) - numpy.sum(self._cgaps)
        default_width = available_width / \
            numpy.count_nonzero(column_widths == 0)
        column_widths[column_widths == 0] = default_width

        table_height = self._ymax_range - self._ymin_range
        available_height = table_height - \
            numpy.sum(row_heights) - numpy.sum(self._rgaps)
        default_height = available_height / \
            numpy.count_nonzero(row_heights == 0)
        row_heights[row_heights == 0] = default_height

        # Compute cell-gap boundaries (cumulative sums of gaps and cells).
        gap_cell_widths = numpy.empty(2 * len(self._cgaps))
        gap_cell_widths[0] = self._xmin_range
        gap_cell_widths[1::2] = self._cgaps
        gap_cell_widths[2::2] = column_widths
        gap_cell_column_boundaries = numpy.cumsum(gap_cell_widths)

        gap_cell_heights = numpy.empty(2 * len(self._rgaps))
        gap_cell_heights[0] = self._ymin_range
        gap_cell_heights[1::2] = self._rgaps
        gap_cell_heights[2::2] = row_heights
        gap_cell_row_boundaries = numpy.cumsum(gap_cell_heights)

        # Assign coordinates to grid cells.
        for cell in self._cells.flat:
            cell._left = gap_cell_column_boundaries[cell._column * 2 + 1]
            cell._right = gap_cell_column_boundaries[cell._column * 2 + 2]
            cell._top = gap_cell_row_boundaries[cell._row * 2 + 1]
            cell._bottom = gap_cell_row_boundaries[cell._row * 2 + 2]

        # Compute grid boundaries.
        self._column_boundaries = (
            gap_cell_column_boundaries[0::2] + gap_cell_column_boundaries[1::2]) / 2
        self._row_boundaries = (
            gap_cell_row_boundaries[0::2] + gap_cell_row_boundaries[1::2]) / 2
