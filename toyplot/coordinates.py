# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Classes and functions for working with coordinate systems.
"""


import collections
import itertools
import warnings

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

##########################################################################
# Helpers

def _mark_exportable(table, column, exportable=True):
    table.metadata(column)["toyplot:exportable"] = exportable


def _opposite_location(location):
    return "above" if location == "below" else "below"


def _create_far_property():
    def getter(self):
        """Specifies the distance from the axis, in the opposite direction as `location`.
        """
        return self._far

    def setter(self, value):
        if value is None:
            self._far = None
        else:
            self._far = toyplot.units.convert(value, target="px", default="px")

    return property(getter, setter)


def _create_line_style_property():
    def getter(self):
        """Dictionary of CSS property-value pairs.

        Use the *style* property to control the appearance of the line.  The
        following CSS properties are allowed:

        * opacity
        * stroke
        * stroke-dasharray
        * stroke-opacity
        * stroke-width

        Note that when assigning to the *style* property, the properties you
        supply are merged with the existing properties.
        """
        return self._style

    def setter(self, value):
        self._style = toyplot.style.combine(
            self._style,
            toyplot.style.require(value, allowed=toyplot.style.allowed.line),
            )

    return property(getter, setter)


def _create_location_property():
    def getter(self):
        return self._location

    def setter(self, value):
        self._location = toyplot.require.value_in(value, [None, "above", "below"])

    return property(getter, setter)


def _create_near_property():
    def getter(self):
        """Specifies the distance from the axis, in the same direction as `location`.
        """
        return self._near

    def setter(self, value):
        if value is None:
            self._near = None
        else:
            self._near = toyplot.units.convert(value, target="px", default="px")

    return property(getter, setter)


def _create_offset_property():
    def getter(self):
        """Specifies the position relative to the axis.  Increasing values of
        *offset* move the position further away from the axis, whether the
        location is "above" or "below".

        :getter: Returns the offset in CSS pixels.

        :setter: Sets the offset using a number, string, or (number, string) tuple.  Assumes CSS pixels if units aren't provided.  See :ref:`units` for details.
        """
        return self._offset

    def setter(self, value):
        if value is None:
            self._offset = value
        else:
            self._offset = toyplot.units.convert(value, target="px", default="px")

    return property(getter, setter)


def _create_show_property():
    def getter(self):
        return self._show

    def setter(self, value):
        if not isinstance(value, bool):
            raise ValueError("A boolean value is required.")
        self._show = value

    return property(getter, setter)


def _create_text_property():
    def getter(self):
        """The text to be displayed, or None.
        """
        return self._text

    def setter(self, value):
        self._text = value

    return property(getter, setter)


def _create_text_style_property():
    def getter(self):
        """Dictionary of CSS property-value pairs.

        Use the *style* property to control the text appearance.  The
        following CSS properties are allowed:

        * alignment-baseline
        * baseline-shift
        * fill
        * fill-opacity
        * font-size
        * font-weight
        * opacity
        * stroke
        * stroke-opacity
        * stroke-width
        * text-anchor
        * -toyplot-anchor-shift

        Note that when assigning to the *style* property, the properties you
        supply are merged with the existing properties.
        """
        return self._style

    def setter(self, value):
        self._style = toyplot.style.combine(
            self._style,
            toyplot.style.require(value, allowed=toyplot.style.allowed.text),
            )

    return property(getter, setter)


def _create_projection(scale, domain_min, domain_max, range_min, range_max):
    if isinstance(scale, toyplot.projection.Projection):
        return scale
    if scale == "linear":
        return toyplot.projection.linear(domain_min, domain_max, range_min, range_max)
    scale, base = scale
    return toyplot.projection.log(base, domain_min, domain_max, range_min, range_max)


##########################################################################
# Axis

class Axis(object):
    """One dimensional axis that can be used to create coordinate systems.
    """
    class DomainHelper(object):
        """Controls domain related behavior for this axis."""
        def __init__(self, domain_min, domain_max):
            self._min = domain_min
            self._max = domain_max
            self._show = True

        @property
        def min(self):
            """Specify an explicit domain minimum for this axis.  By default
            the implicit domain minimum is computed from visible data.
            """
            return self._min

        @min.setter
        def min(self, value):
            self._min = value

        @property
        def max(self):
            """Specify an explicit domain maximum for this axis.  By default
            the implicit domain maximum is computed from visible data.
            """
            return self._max

        @max.setter
        def max(self, value):
            self._max = value

        @property
        def show(self):
            """Control whether the domain should be made visible using the
            axis spine.
            """
            return self._show

        @show.setter
        def show(self, value):
            toyplot.log.warning("Altering <axis>.domain.show is experimental.")
            self._show = True if value else False


    class InteractiveCoordinatesLabelHelper(object):
        """Controls the appearance and behavior of interactive coordinate labels."""
        def __init__(self):
            self._show = True
            self._style = {
                "fill": "slategray",
                "font-size": "10px",
                "font-weight": "normal",
                "stroke": "none",
                "text-anchor": "middle",
                }

        show = _create_show_property()
        style = _create_text_style_property()


    class InteractiveCoordinatesTickHelper(object):
        """Controls the appearance and behavior of interactive coordinate ticks."""
        def __init__(self):
            self._show = True
            self._style = {
                "stroke":"slategray",
                "stroke-width": 1.0,
                }

        show = _create_show_property()
        style = _create_line_style_property()


    class InteractiveCoordinatesHelper(object):
        """Controls the appearance and behavior of interactive coordinates."""
        def __init__(self):
            self._label = toyplot.coordinates.Axis.InteractiveCoordinatesLabelHelper()
            self._location = None
            self._show = True
            self._tick = toyplot.coordinates.Axis.InteractiveCoordinatesTickHelper()

        @property
        def label(self):
            """:class:`toyplot.coordinates.Axis.InteractiveCoordinatesLabelHelper` instance."""
            return self._label

        location = _create_location_property()
        """Controls the position of interactive coordinates relative to the axis.

        Allowed values are "above" (force coordinates to appear above the axis), "below"
        (the opposite), or `None` (the default - display interactive coordinates opposite
        tick labels).
        """
        show = _create_show_property()
        """Set `False` to disable showing interactive coordinates for this axis."""

        @property
        def tick(self):
            """:class:`toyplot.coordinates.Axis.InteractiveCoordinatesTickHelper` instance."""
            return self._tick


    class InteractiveHelper(object):
        """Controls interactive behavior for this axis."""
        def __init__(self):
            self._coordinates = toyplot.coordinates.Axis.InteractiveCoordinatesHelper()

        @property
        def coordinates(self):
            """:class:`toyplot.coordinates.Axis.InteractiveCoordinatesHelper` instance."""
            return self._coordinates


    class LabelHelper(object):
        """Controls the appearance and behavior of an axis label."""
        def __init__(self, text, style):
            self._location = None
            self._offset = None
            self._style = {}
            self._text = None

            self.style = {
                "font-size": "12px",
                "font-weight": "bold",
                "stroke": "none",
                "text-anchor":"middle",
                }
            self.style = style
            self.text = text

        location = _create_location_property()
        offset = _create_offset_property()
        style = _create_text_style_property()
        text = _create_text_property()


    class SpineHelper(object):
        """Controls the appearance and behavior of an axis spine."""
        def __init__(self):
            self._position = "low"
            self._show = True
            self._style = {}

        @property
        def position(self):
            return self._position

        @position.setter
        def position(self, value):
            self._position = value

        show = _create_show_property()
        style = _create_line_style_property()


    class PerTickHelper(object):
        """Controls the appearanace and behavior of individual axis ticks."""
        class TickProxy(object):
            def __init__(self, tick, allowed):
                self._tick = tick
                self._allowed = allowed

            @property
            def style(self):
                return self._tick.get("style", {})

            @style.setter
            def style(self, value):
                self._tick["style"] = toyplot.style.combine(
                    self._tick.get("style"),
                    toyplot.style.require(value, allowed=self._allowed),
                    )

        def __init__(self, allowed):
            self._indices = collections.defaultdict(dict)
            self._values = collections.defaultdict(dict)
            self._allowed = allowed

        def __call__(self, index=None, value=None):
            if index is None and value is None:
                raise ValueError("Must specify tick index or value.") # pragma: no cover
            if index is not None and value is not None:
                raise ValueError("Must specify either index or value, not both.") # pragma: no cover
            if index is not None:
                return Axis.PerTickHelper.TickProxy(self._indices[index], self._allowed)
            elif value is not None:
                return Axis.PerTickHelper.TickProxy(self._values[value], self._allowed)

        def styles(self, values):
            results = [self._indices[index].get("style", None) if index in self._indices else None for index in range(len(values))]
            for value in self._values:
                deltas = numpy.abs(values - value)
                results[numpy.argmin(deltas)] = self._values[value].get("style", None)
            return results


    class TicksHelper(object):
        """Controls the appearance and behavior of axis ticks."""
        def __init__(self, locator, angle):
            self._far = None
            self._labels = Axis.TickLabelsHelper(angle)
            self._location = None
            self._locator = locator
            self._near = None
            self._show = False
            self._style = {}
            self._tick = Axis.PerTickHelper(toyplot.style.allowed.line)

        far = _create_far_property()
        location = _create_location_property()
        """Controls the position of ticks (and labels) relative to the axis.

        Allowed values are "above" (force labels to appear above the axis), "below"
        (the opposite), or `None` (use default, context-sensitive behavior).
        """
        near = _create_near_property()
        show = _create_show_property()
        style = _create_line_style_property()

        @property
        def labels(self):
            return self._labels

        @property
        def locator(self):
            return self._locator

        @locator.setter
        def locator(self, value):
            self._locator = value

        @property
        def tick(self):
            return self._tick


    class TickLabelsHelper(object):
        """Controls the appearance and behavior of axis tick labels."""
        def __init__(self, angle):
            self._angle = angle
            self._label = Axis.PerTickHelper(toyplot.style.allowed.text)
            self._offset = None
            self._show = True
            self._style = {
                "font-size": "10px",
                "font-weight": "normal",
                "stroke": "none",
                }

        style = _create_text_style_property()
        offset = _create_offset_property()
        show = _create_show_property()

        @property
        def angle(self):
            return self._angle

        @angle.setter
        def angle(self, value):
            self._angle = value

        @property
        def label(self):
            return self._label

    def __init__(
            self,
            label=None,
            domain_min=None,
            domain_max=None,
            scale="linear",
            show=True,
            tick_angle=0,
            tick_locator=None,
        ):
        self._finalized = None
        self._data_max = None
        self._data_min = None
        self._display_max = None
        self._display_min = None
        self._domain = Axis.DomainHelper(domain_min, domain_max)
        self._interactive = Axis.InteractiveHelper()
        self._label = Axis.LabelHelper(label, style={})
        self._scale = None
        self._show = show
        self._spine = Axis.SpineHelper()
        self._tick_labels = []
        self._tick_locations = []
        self._tick_titles = []
        self._ticks = Axis.TicksHelper(tick_locator, tick_angle)
        self.scale = scale

    show = _create_show_property()

    @property
    def interactive(self):
        """:class:`toyplot.coordinates.Axis.InteractiveHelper` instance."""
        return self._interactive

    @property
    def domain(self):
        """:class:`toyplot.coordinates.Axis.DomainHelper` instance."""
        return self._domain

    @property
    def label(self):
        """:class:`toyplot.coordinates.Axis.LabelHelper` instance."""
        return self._label

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

    @property
    def spine(self):
        """:class:`toyplot.coordinates.Axis.SpineHelper` instance."""
        return self._spine

    @property
    def ticks(self):
        """:class:`toyplot.coordinates.Axis.TicksHelper` instance."""
        return self._ticks

    def _update_domain(self, values, display=True, data=True):
        if display:
            self._display_min, self._display_max = toyplot.data.minimax(itertools.chain([self._display_min, self._display_max], values))

        if data:
            self._data_min, self._data_max = toyplot.data.minimax(itertools.chain([self._data_min, self._data_max], values))

    def _locator(self):
        if self.ticks.locator is not None:
            return self.ticks.locator
        if self.scale == "linear":
            return toyplot.locator.Extended()
        if isinstance(self.scale, toyplot.projection.Projection):
            return toyplot.locator.Null()
        else:
            scale, base = self.scale
            if scale == "log":
                return toyplot.locator.Log(base=base)
        raise RuntimeError("Unable to create an appropriate locator.") # pragma: no cover

    def _finalize(
            self,
            x1,
            x2,
            y1,
            y2,
            offset,
            domain_min,
            domain_max,
            tick_locations,
            tick_labels,
            tick_titles,
            default_tick_location,
            default_ticks_near,
            default_ticks_far,
            default_label_location,
        ):
        if self._finalized is None:
            self._x1 = x1
            self._x2 = x2
            self._y1 = y1
            self._y2 = y2
            self._offset = offset
            self._domain_min = domain_min
            self._domain_max = domain_max
            self._tick_locations = tick_locations
            self._tick_labels = tick_labels
            self._tick_titles = tick_titles
            self._tick_location = self.ticks.location if self.ticks.location is not None else default_tick_location
            self._ticks_near = self.ticks.near if self.ticks.near is not None else default_ticks_near
            self._ticks_far = self.ticks.far if self.ticks.far is not None else default_ticks_far
            self._tick_labels_location = self._tick_location
            self._tick_labels_offset = self.ticks.labels.offset if self.ticks.labels.offset is not None else 6
            self._label_location = self.label.location if self.label.location is not None else default_label_location
            self._label_offset = self.label.offset if self.label.offset is not None else 22
            self._interactive_coordinates_location = self.interactive.coordinates.location if self.interactive.coordinates.location is not None else _opposite_location(self._tick_labels_location)

            endpoints = numpy.row_stack(((x1, y1), (x2, y2)))
            length = numpy.linalg.norm(endpoints[1] - endpoints[0])
            self.projection = _create_projection(
                scale=self.scale,
                domain_min=domain_min,
                domain_max=domain_max,
                range_min=0.0,
                range_max=length,
                )

            self._finalized = self
        return self._finalized


##########################################################################
# Cartesian

class Cartesian(object):
    """Standard two-dimensional Cartesian coordinate system.

    Do not create Cartesian instances directly.  Use factory methods such
    as :meth:`toyplot.canvas.Canvas.cartesian` instead.
    """

    class LabelHelper(object):
        """Controls the appearance and behavior of a Cartesian coordinate system label."""
        def __init__(self, text, style):
            self._style = {}
            self._text = None

            self.style = {
                "font-size": "14px",
                "font-weight": "bold",
                "stroke": "none",
                "text-anchor":"middle",
                "-toyplot-vertical-align":"bottom",
                }
            self.style = style
            self.text = text
            self.offset = 8

        style = _create_text_style_property()
        text = _create_text_property()
        offset = _create_offset_property()

    def __init__(
            self,
            aspect,
            hyperlink,
            label,
            padding,
            palette,
            scenegraph,
            show,
            xaxis,
            xlabel,
            xmax,
            xmax_range,
            xmin,
            xmin_range,
            xscale,
            xshow,
            xticklocator,
            yaxis,
            ylabel,
            ymax,
            ymax_range,
            ymin,
            ymin_range,
            yscale,
            yshow,
            yticklocator,
            ):

        if palette is None:
            palette = toyplot.color.Palette()

        self._finalized = None

        self._xmin_range = xmin_range
        self._xmax_range = xmax_range
        self._ymin_range = ymin_range
        self._ymax_range = ymax_range

        self._aspect = None
        self.aspect = aspect

        self._hyperlink = None
        self.hyperlink = hyperlink

        self._expand_domain_range_x = None
        self._expand_domain_range_y = None
        self._expand_domain_range_left = None
        self._expand_domain_range_right = None
        self._expand_domain_range_top = None
        self._expand_domain_range_bottom = None
        self._padding = toyplot.units.convert(padding, target="px", default="px")

        self._palette = palette
        self._bar_colors = itertools.cycle(self._palette)
        self._ellipse_colors = itertools.cycle(self._palette)
        self._fill_colors = itertools.cycle(self._palette)
        self._graph_colors = itertools.cycle(self._palette)
        self._plot_colors = itertools.cycle(self._palette)
        self._scatterplot_colors = itertools.cycle(self._palette)
        self._rect_colors = itertools.cycle(self._palette)
        self._text_colors = itertools.cycle(self._palette)

        self._show = show

        self.label = Cartesian.LabelHelper(
            text=label,
            style={},
            )

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

        self._scenegraph = scenegraph

    @property
    def aspect(self):
        """Control the mapping from domains to ranges.

        By default, each axis maps its domain to its range separately, which is
        what is usually expected from a plot.  Sometimes, both axes have the same
        domain.  In this case, it is desirable that both axes are mapped to a consistent
        range to avoid "squashing" or "stretching" the data.  To do so, set `aspect`
        to "fit-range".
        """
        return self._aspect

    @aspect.setter
    def aspect(self, value):
        if value not in [None, "fit-range"]:
            raise ValueError("Unknown aspect value: %s" % value) # pragma: no cover
        self._aspect = value

    @property
    def hyperlink(self):
        """Specify a URI that will be hyperlinked from the axes range."""
        return self._hyperlink

    @hyperlink.setter
    def hyperlink(self, value):
        self._hyperlink = toyplot.require.hyperlink(value)

    @property
    def show(self):
        """Control axis visibility.

        Use the `show` property to hide all visible parts of the axes: labels,
        spines, ticks, tick labels, etc.  Note that this does not affect
        visibility of the axes contents, just the axes themselves.
        """
        return self._show

    @show.setter
    def show(self, value):
        self._show = value

    @property
    def padding(self):
        """Control the default distance between axis spines and data.

        By default, axis spines are offset slightly from the data, to avoid
        visual clutter and overlap.  Use `padding` to change this offset.
        The default units are CSS pixels, but you may specify the padding
        using any :ref:`units` you like.
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = toyplot.units.convert(value, target="px", default="px")

    def _set_xmin_range(self, value):
        self._xmin_range = value
    xmin_range = property(fset=_set_xmin_range)

    def _set_xmax_range(self, value):
        self._xmax_range = value
    xmax_range = property(fset=_set_xmax_range)

    def _set_ymin_range(self, value):
        self._ymin_range = value
    ymin_range = property(fset=_set_ymin_range)

    def _set_ymax_range(self, value):
        self._ymax_range = value
    ymax_range = property(fset=_set_ymax_range)

    def _finalize(self):
        if self._finalized is None:
            # Begin with the implicit domain defined by our children.
            for child in self._scenegraph.targets(self.x, "map"):
                child = child._finalize()
                if child is not None:
                    self.x._update_domain(child.domain("x"), display=True, data=not child.annotation)

                    (x, y), (left, right, top, bottom) = child.extents(["x", "y"])
                    self._expand_domain_range_x = x if self._expand_domain_range_x is None else numpy.concatenate((self._expand_domain_range_x, x))
                    self._expand_domain_range_left = left if self._expand_domain_range_left is None else numpy.concatenate((self._expand_domain_range_left, left))
                    self._expand_domain_range_right = right if self._expand_domain_range_right is None else numpy.concatenate((self._expand_domain_range_right, right))

            for child in self._scenegraph.targets(self.y, "map"):
                child = child._finalize()
                if child is not None:
                    self.y._update_domain(child.domain("y"), display=True, data=not child.annotation)

                    (x, y), (left, right, top, bottom) = child.extents(["x", "y"])
                    self._expand_domain_range_y = y if self._expand_domain_range_y is None else numpy.concatenate((self._expand_domain_range_y, y))
                    self._expand_domain_range_top = top if self._expand_domain_range_top is None else numpy.concatenate((self._expand_domain_range_top, top))
                    self._expand_domain_range_bottom = bottom if self._expand_domain_range_bottom is None else numpy.concatenate((self._expand_domain_range_bottom, bottom))

            # Begin with the implicit domain defined by our data.
            xdomain_min = self.x._display_min
            xdomain_max = self.x._display_max
            ydomain_min = self.y._display_min
            ydomain_max = self.y._display_max

            # If there is no implicit domain (we don't have any data), default
            # to the origin.
            if xdomain_min is None:
                xdomain_min = 0
            if xdomain_max is None:
                xdomain_max = 0
            if ydomain_min is None:
                ydomain_min = 0
            if ydomain_max is None:
                ydomain_max = 0

            # Ensure that the domain is never empty.
            if xdomain_min == xdomain_max:
                xdomain_min -= 0.5
                xdomain_max += 0.5
            if ydomain_min == ydomain_max:
                ydomain_min -= 0.5
                ydomain_max += 0.5

            # Optionally expand the domain in range-space (used to make room for text).
            if self._expand_domain_range_x is not None:
                x_projection = _create_projection(
                    self.x.scale,
                    domain_min=xdomain_min,
                    domain_max=xdomain_max,
                    range_min=self._xmin_range,
                    range_max=self._xmax_range,
                    )

                range_x = x_projection(self._expand_domain_range_x)
                range_left = range_x + self._expand_domain_range_left
                range_right = range_x + self._expand_domain_range_right

                domain_left = x_projection.inverse(range_left)
                domain_right = x_projection.inverse(range_right)

                xdomain_min, xdomain_max = toyplot.data.minimax([xdomain_min, xdomain_max, domain_left, domain_right])

            if self._expand_domain_range_y is not None:
                y_projection = _create_projection(
                    self.y.scale,
                    domain_min=ydomain_min,
                    domain_max=ydomain_max,
                    range_min=self._ymax_range,
                    range_max=self._ymin_range,
                    )

                range_y = y_projection(self._expand_domain_range_y)
                range_top = range_y + self._expand_domain_range_top
                range_bottom = range_y + self._expand_domain_range_bottom

                domain_top = y_projection.inverse(range_top)
                domain_bottom = y_projection.inverse(range_bottom)

                ydomain_min, ydomain_max = toyplot.data.minimax([ydomain_min, ydomain_max, domain_top, domain_bottom])

            # Optionally expand the domain to match the aspect ratio of the range.
            if self._aspect == "fit-range":
                dwidth = (xdomain_max - xdomain_min)
                dheight = (ydomain_max - ydomain_min)
                daspect = dwidth / dheight
                raspect = (self._xmax_range - self._xmin_range) / (self._ymax_range - self._ymin_range)

                if daspect < raspect:
                    offset = ((dwidth * (raspect / daspect)) - dwidth) * 0.5
                    xdomain_min -= offset
                    xdomain_max += offset
                elif daspect > raspect:
                    offset = ((dheight * (daspect / raspect)) - dheight) * 0.5
                    ydomain_min -= offset
                    ydomain_max += offset

            # Allow users to override the domain.
            if self.x.domain.min is not None:
                xdomain_min = self.x.domain.min
            if self.x.domain.max is not None:
                xdomain_max = self.x.domain.max
            if self.y.domain.min is not None:
                ydomain_min = self.y.domain.min
            if self.y.domain.max is not None:
                ydomain_max = self.y.domain.max

            # Ensure that the domain is never empty.
            if xdomain_min == xdomain_max:
                xdomain_min -= 0.5
                xdomain_max += 0.5
            if ydomain_min == ydomain_max:
                ydomain_min -= 0.5
                ydomain_max += 0.5

            # Calculate tick locations and labels.
            xtick_locations = []
            xtick_labels = []
            xtick_titles = []
            if self.show and self.x.show:
                xtick_locations, xtick_labels, xtick_titles = self.x._locator().ticks(xdomain_min, xdomain_max)
            ytick_locations = []
            ytick_labels = []
            ytick_titles = []
            if self.show and self.y.show:
                ytick_locations, ytick_labels, ytick_titles = self.y._locator().ticks(ydomain_min, ydomain_max)

            # Allow tick locations to grow (never shrink) the domain.
            if len(xtick_locations):
                xdomain_min = numpy.amin((xdomain_min, xtick_locations[0]))
                xdomain_max = numpy.amax((xdomain_max, xtick_locations[-1]))
            if len(ytick_locations):
                ydomain_min = numpy.amin((ydomain_min, ytick_locations[0]))
                ydomain_max = numpy.amax((ydomain_max, ytick_locations[-1]))

            # Create projections for each axis.
            self._x_projection = _create_projection(
                scale=self.x.scale,
                domain_min=xdomain_min,
                domain_max=xdomain_max,
                range_min=self._xmin_range,
                range_max=self._xmax_range,
                )
            self._y_projection = _create_projection(
                scale=self.y.scale,
                domain_min=ydomain_min,
                domain_max=ydomain_max,
                range_min=self._ymax_range,
                range_max=self._ymin_range,
                )

            # Finalize positions for all axis components.
            if self.x.spine.position == "low":
                x_offset = self.padding
                x_spine_y = self._ymax_range
                x_ticks_near = 0
                x_ticks_far = 5
                x_tick_location = "below"
                x_label_location = "below"
            elif self.x.spine.position == "high":
                x_offset = -self.padding # pylint: disable=invalid-unary-operand-type
                x_spine_y = self._ymin_range
                x_ticks_near = 5
                x_ticks_far = 0
                x_tick_location = "above"
                x_label_location = "above"
            else:
                x_offset = 0
                x_spine_y = self._y_projection(self.x.spine.position)
                x_ticks_near = 3
                x_ticks_far = 3
                x_tick_location = "below"
                x_label_location = "below"

            if self.y.spine._position == "low":
                y_offset = -self.padding # pylint: disable=invalid-unary-operand-type
                y_spine_x = self._xmin_range
                y_ticks_near = 0
                y_ticks_far = 5
                y_tick_location = "above"
                y_label_location = "above"
            elif self.y.spine._position == "high":
                y_offset = self.padding
                y_spine_x = self._xmax_range
                y_ticks_near = 0
                y_ticks_far = 5
                y_tick_location = "below"
                y_label_location = "below"
            else:
                y_offset = 0
                y_spine_x = self._x_projection(self.y.spine._position)
                y_ticks_near = 3
                y_ticks_far = 3
                y_tick_location = "below"
                y_label_location = "below"

            # Finalize the axes.
            self.x._finalize(
                x1=self._xmin_range,
                x2=self._xmax_range,
                y1=x_spine_y,
                y2=x_spine_y,
                offset=x_offset,
                domain_min=xdomain_min,
                domain_max=xdomain_max,
                tick_locations=xtick_locations,
                tick_labels=xtick_labels,
                tick_titles=xtick_titles,
                default_tick_location=x_tick_location,
                default_ticks_far=x_ticks_far,
                default_ticks_near=x_ticks_near,
                default_label_location=x_label_location,
                )
            self.y._finalize(
                x1=y_spine_x,
                x2=y_spine_x,
                y1=self._ymax_range,
                y2=self._ymin_range,
                offset=y_offset,
                domain_min=ydomain_min,
                domain_max=ydomain_max,
                tick_locations=ytick_locations,
                tick_labels=ytick_labels,
                tick_titles=ytick_titles,
                default_tick_location=y_tick_location,
                default_ticks_far=y_ticks_far,
                default_ticks_near=y_ticks_near,
                default_label_location=y_label_location,
                )
            self._finalized = self

        return self._finalized

    def project(self, axis, values):
        """Project a set of domain values to coordinate system range values.

        Note that this API is intended for advanced users creating their own
        custom marks, end-users should never need to use it.

        Parameters
        ----------
        axis: "x" or "y", required
            The axis to be projected
        values: array-like, required
            The values to be projected

        Returns
        -------
        projected: :class:`numpy.ndarray`
            The projected values.
        """
        if axis == "x":
            return self._x_projection(values)
        elif axis == "y":
            return self._y_projection(values)
        raise ValueError("Unexpected axis: %s" % axis)

    def add_mark(self, mark):
        """Add a mark to the axes.

        This is only of use when creating your own custom Toyplot marks.  It is
        not intended for end-users.

        Example
        -------
        To add your own custom mark to a set of axes::

            mark = axes.add(MyCustomMark())

        Parameters
        ----------
        mark: :class:`toyplot.mark.Mark`, required

        Returns
        -------
        mark: :class:`toyplot.mark.Mark`
        """

        self._scenegraph.add_edge(self, "render", mark)
        self._scenegraph.add_edge(self.x, "map", mark)
        self._scenegraph.add_edge(self.y, "map", mark)

        return mark

    def bars(
            self,
            a,
            b=None,
            c=None,
            along="x",
            baseline="stacked",
            color=None,
            filename=None,
            hyperlink=None,
            opacity=1.0,
            style=None,
            title=None,
            ):
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
        hyperlink: array-like set of strings, optional
          Specify a single hyperlink, one hyperlink per series, or one hyperlink per bar.
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
            title = toyplot.broadcast.pyobject(
                title, (series.shape[0], series.shape[1] - 1))
            hyperlink = toyplot.broadcast.pyobject(
                hyperlink, (series.shape[0], series.shape[1] - 1))
            style = toyplot.style.combine(
                {"stroke": "white", "stroke-width": 1.0},
                toyplot.style.require(style, allowed=toyplot.style.allowed.fill),
                )

            if along == "x":
                coordinate_axes = ["x", "y"]
            elif along == "y":
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
            hyperlink_keys = []

            boundary_keys.append("boundary0")
            table[boundary_keys[-1]] = series.T[0]

            for index, (boundary_column, fill_column, opacity_column, title_column, hyperlink_column) in enumerate(
                    zip(series.T[1:], color.T, opacity.T, title.T, hyperlink.T)):
                boundary_keys.append("boundary" + str(index + 1))
                fill_keys.append("fill" + str(index))
                opacity_keys.append("opacity" + str(index))
                title_keys.append("title" + str(index))
                hyperlink_keys.append("hyperlink" + str(index))
                table[boundary_keys[-1]] = boundary_column
                _mark_exportable(table, boundary_keys[-1])
                table[fill_keys[-1]] = fill_column
                table[opacity_keys[-1]] = opacity_column
                table[title_keys[-1]] = title_column
                table[hyperlink_keys[-1]] = hyperlink_column

            return self.add_mark(
                toyplot.mark.BarBoundaries(
                    coordinate_axes=coordinate_axes,
                    table=table,
                    left="left",
                    right="right",
                    boundaries=boundary_keys,
                    fill=fill_keys,
                    opacity=opacity_keys,
                    title=title_keys,
                    hyperlink=hyperlink_keys,
                    style=style,
                    filename=filename,
                    ))
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
            title = toyplot.broadcast.pyobject(title, series.shape)
            hyperlink = toyplot.broadcast.pyobject(hyperlink, series.shape)
            style = toyplot.style.combine(
                {"stroke": "white", "stroke-width": 1.0},
                toyplot.style.require(style, allowed=toyplot.style.allowed.fill),
                )

            if isinstance(baseline, str):
                baseline = toyplot.require.value_in(baseline, ["stacked", "symmetric", "wiggle"])
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

            if along == "x":
                coordinate_axes = ["x", "y"]
            elif along == "y":
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
            hyperlink_keys = []
            for index, (magnitude_column, fill_column, opacity_column, title_column, hyperlink_column) in enumerate(
                    zip(series.T, color.T, opacity.T, title.T, hyperlink.T)):
                magnitude_keys.append("magnitude" + str(index))
                fill_keys.append("fill" + str(index))
                opacity_keys.append("opacity" + str(index))
                title_keys.append("title" + str(index))
                hyperlink_keys.append("hyperlink" + str(index))
                table[magnitude_keys[-1]] = magnitude_column
                _mark_exportable(table, magnitude_keys[-1])
                table[fill_keys[-1]] = fill_column
                table[opacity_keys[-1]] = opacity_column
                table[title_keys[-1]] = title_column
                table[hyperlink_keys[-1]] = hyperlink_column

            return self.add_mark(
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
                    hyperlink=hyperlink_keys,
                    style=style,
                    filename=filename,
                    ))

    def color_scale(
            self,
            colormap,
            label=None,
            tick_locator=None,
            width=10,
            padding=10,
        ):
        """Add a color scale to the axes.

        The color scale displays a mapping from scalar values to colors, for
        the given colormap.  Note that the supplied colormap must have an
        explicitly defined domain (specified when the colormap was created),
        otherwise the mapping would be undefined.

        Parameters
        ----------
        colormap: :class:`toyplot.color.Map`, required
          Colormap to be displayed.
        label: string, optional
          Human-readable label placed below the axis.
        ticklocator: :class:`toyplot.locator.TickLocator`, optional
          Controls the placement and formatting of axis ticks and tick labels.

        Returns
        -------
        axes: :class:`toyplot.coordinates.Numberline`
        """

        axis = self._scenegraph.source("render", self).color_scale(
            colormap=colormap,
            x1=self._xmax_range + width + self._padding,
            x2=self._xmax_range + width + self._padding,
            y1=self._ymax_range,
            y2=self._ymin_range,
            width=width,
            padding=padding,
            show=True,
            label=label,
            ticklocator=tick_locator,
            scale="linear",
            )
        return axis

    def ellipse(
            self,
            x,
            y,
            rx,
            ry,
            angle=None,
            color=None,
            opacity=1.0,
            title=None,
            style=None,
            filename=None,
        ):
        """Add ellipses to the axes.

        This command creates a single series of one-or-more ellipses.  To create
        one ellipse, pass scalar values for the center and x and y radiuses:

        >>> axes.ellipse(xcenter, ycenter, xradius, yradius)

        You may also specify an optional angle, measured in degrees, that will
        be used to rotate the ellipse counter-clockwise around its center:

        >>> axes.ellipse(xcenter, ycenter, xradius, yradius, angle)

        To create :math:`M` ellipses, pass size-:math:`M` vectors for each
        of the parameters:

        >>> axes.ellipse(xcenters, ycenters, xradiuses, yradiuses)
        >>> axes.ellipse(xcenters, ycenters, xradiuses, yradiuses, angles)

        Parameters
        ----------
        x, y: array-like series of center coordinates.
        rx, ry: array-like series of x and y radiuses.
        angle: array-like series of rotation angles, optional.
        color: array-like series of colors, optional.
            Specify a single color for all ellipses, or one color per ellipse.
            Color values can be explicit Toyplot colors, scalar values to be
            mapped to colors with a default colormap, or a (scalar, colormap)
            tuple containing scalar values to be mapped to colors with the given
            colormap.
        opacity: array-like set of opacities, optional.
            Specify a single opacity for all ellipses, or one opacity per ellipse.
        title: array like set of strings, optional.
            Specify a single title for all ellipses, or one title per ellipse.
        style: dict, optional
            Collection of CSS styles to be applied to every ellipse.
        filename: string, optional
            Specify a default filename to be used if the end-viewer decides to export
            the plot data.

        Returns
        -------
        mark: :class:`toyplot.mark.Ellipse` containing the mark data.
        """

        if angle is None:
            angle = numpy.zeros_like(x)

        table = toyplot.data.Table()
        table["x"] = toyplot.require.scalar_vector(x)
        table["y"] = toyplot.require.scalar_vector(y, length=table.shape[0])
        table["rx"] = toyplot.require.scalar_vector(rx, length=table.shape[0])
        table["ry"] = toyplot.require.scalar_vector(ry, length=table.shape[0])
        table["angle"] = toyplot.require.scalar_vector(angle, length=table.shape[0])
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.pyobject(title, table.shape[0])
        style = toyplot.style.combine(
            {"stroke": "none"},
            toyplot.style.require(style, allowed=toyplot.style.allowed.fill),
            )

        default_color = [next(self._rect_colors)]
        table["toyplot:fill"] = toyplot.color.broadcast(
            colors=color,
            shape=(table.shape[0], 1),
            default=default_color,
            )[:, 0]

        coordinate_axes = ["x", "y"]

        return self.add_mark(
            toyplot.mark.Ellipse(
                coordinate_axes,
                table=table,
                x=["x"],
                y=["y"],
                rx=["rx"],
                ry=["ry"],
                angle=["angle"],
                fill=["toyplot:fill"],
                opacity=["opacity"],
                title=["title"],
                style=style,
                filename=filename,
                ))

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
            annotation=False,
            filename=None,
        ):
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
        annotation: boolean, optional
          Set to True if this mark should be considered an annotation.

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
            title = toyplot.broadcast.pyobject(title, series.shape[1] - 1)
            style = toyplot.style.combine(
                {"stroke": "none"},
                toyplot.style.require(style, allowed=toyplot.style.allowed.fill),
                )

            if along == "x":
                coordinate_axes = ["x", "y"]
            elif along == "y":
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

            return self.add_mark(
                toyplot.mark.FillBoundaries(
                    coordinate_axes=coordinate_axes,
                    table=table,
                    position=[coordinate_axes[0]],
                    boundaries=boundaries,
                    fill=color,
                    opacity=opacity,
                    title=title,
                    style=style,
                    annotation=annotation,
                    filename=filename,
                    ))
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
            title = toyplot.broadcast.pyobject(title, series.shape[1])
            style = toyplot.style.combine(
                {"stroke": "none"},
                toyplot.style.require(style, allowed=toyplot.style.allowed.fill),
                )

            if isinstance(baseline, str):
                baseline = toyplot.require.value_in(baseline, ["stacked", "symmetric", "wiggle"])
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

            if along == "x":
                coordinate_axes = ["x", "y"]
            elif along == "y":
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

            return self.add_mark(
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
                    annotation=annotation,
                    filename=filename,
                    ))

    def graph(
            self,
            a,
            b=None,
            c=None,
            olayout=None,
            layout=None,
            along="x",
            ecolor=None,
            efilename=None,
            eopacity=1.0,
            estyle=None,
            ewidth=1.0,
            hmarker=None,
            mmarker=None,
            mposition=0.5,
            tmarker=None,
            varea=None,
            vcolor=None,
            vcoordinates=None,
            vfilename=None,
            vlabel=None,
            vlshow=True,
            vlstyle=None,
            vmarker="o",
            vopacity=1.0,
            vsize=None,
            vstyle=None,
            vtitle=None,
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
        elif vlabel == False:
            vlabel = [""] * layout.vcount

        default_color = [next(self._graph_colors)]
        vcolor = toyplot.color.broadcast(
            colors=vcolor,
            shape=layout.vcount,
            default=default_color,
            )

        vmarker = toyplot.broadcast.pyobject(vmarker, layout.vcount)

        if varea is None and vsize is None:
            vsize = toyplot.broadcast.scalar(4, layout.vcount)
        elif varea is None and vsize is not None:
            vsize = toyplot.broadcast.scalar(vsize, layout.vcount)
        elif varea is not None and vsize is None:
            vsize = numpy.sqrt(toyplot.broadcast.scalar(varea, layout.vcount))
        else:
            toyplot.log.warning("Graph vsize parameter overrides varea.")
            vsize = toyplot.broadcast.scalar(vsize, layout.vcount)

        vopacity = toyplot.broadcast.scalar(vopacity, layout.vcount)
        vtitle = toyplot.broadcast.pyobject(vtitle, layout.vcount)
        vstyle = toyplot.style.require(vstyle, allowed=toyplot.style.allowed.marker)
        vlstyle = toyplot.style.combine(
            {
                "font-size": "12px",
                "font-weight": "normal",
                "stroke": "none",
                "text-anchor": "middle",
                "-toyplot-vertical-align": "middle",
            },
            toyplot.style.require(vlstyle, allowed=toyplot.style.allowed.text),
            )

        ecolor = toyplot.color.broadcast(
            colors=ecolor,
            shape=layout.ecount,
            default=default_color,
            )
        ewidth = toyplot.broadcast.scalar(ewidth, layout.ecount)
        eopacity = toyplot.broadcast.scalar(eopacity, layout.ecount)
        estyle = toyplot.style.require(estyle, allowed=toyplot.style.allowed.line)

        hmarker = toyplot.broadcast.pyobject(hmarker, layout.ecount)
        mmarker = toyplot.broadcast.pyobject(mmarker, layout.ecount)
        mposition = toyplot.broadcast.scalar(mposition, layout.ecount)
        tmarker = toyplot.broadcast.pyobject(tmarker, layout.ecount)

        if along == "x":
            coordinate_axes = ["x", "y"]
        elif along == "y":
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
        etable["hmarker"] = hmarker
        etable["mmarker"] = mmarker
        etable["mposition"] = mposition
        etable["tmarker"] = tmarker

        return self.add_mark(
            toyplot.mark.Graph(
                coordinate_axes=coordinate_axes,
                ecolor=["color"],
                ecoordinates=layout.ecoordinates,
                efilename=efilename,
                eopacity=["opacity"],
                eshape=["shape"],
                esource=["source"],
                estyle=estyle,
                etable=etable,
                etarget=["target"],
                ewidth=["width"],
                hmarker=["hmarker"],
                mmarker=["mmarker"],
                mposition=["mposition"],
                tmarker=["tmarker"],
                vcolor=["color"],
                vcoordinates=coordinate_axes,
                vfilename=vfilename,
                vid=["id"],
                vlabel=["label"],
                vlshow=vlshow,
                vlstyle=vlstyle,
                vmarker=["marker"],
                vopacity=["opacity"],
                vsize=["size"],
                vstyle=vstyle,
                vtable=vtable,
                vtitle=["title"],
                ))

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
        _mark_exportable(table, "y")
        color = toyplot.color.broadcast(
            colors=color,
            shape=(table.shape[0], 1),
            default=toyplot.color.black,
            )
        table["color"] = color[:, 0]
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.pyobject(title, table.shape[0])
        style = toyplot.style.require(style, allowed=toyplot.style.allowed.line)

        return self.add_mark(
            toyplot.mark.AxisLines(
                coordinate_axes=["y"],
                table=table,
                coordinates=["y"],
                stroke=["color"],
                opacity=["opacity"],
                title=["title"],
                style=style,
                annotation=annotation,
                ))

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
            area=None,
            size=None,
            mfill=None,
            mopacity=1.0,
            mtitle=None,
            style=None,
            mstyle=None,
            mlstyle=None,
            filename=None,
        ):
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

        default_color = [next(self._plot_colors) for i in range(series.shape[1])]
        stroke = toyplot.color.broadcast(
            colors=color,
            shape=(series.shape[1],),
            default=default_color,
            )
        stroke_width = toyplot.broadcast.scalar(stroke_width, series.shape[1])
        stroke_opacity = toyplot.broadcast.scalar(
            opacity, series.shape[1])
        stroke_title = toyplot.broadcast.pyobject(title, series.shape[1])
        marker = toyplot.broadcast.pyobject(marker, series.shape)

        if area is None and size is None:
            msize = toyplot.broadcast.scalar(4, series.shape)
        elif area is None and size is not None:
            msize = toyplot.broadcast.scalar(size, series.shape)
        elif area is not None and size is None:
            msize = numpy.sqrt(toyplot.broadcast.scalar(area, series.shape))
        else:
            toyplot.log.warning("Plot size parameter overrides area.")
            msize = toyplot.broadcast.scalar(size, series.shape)

        mfill = toyplot.color.broadcast(
            colors=mfill,
            shape=series.shape,
            default=stroke,
            )
        mstroke = toyplot.color.broadcast(colors=mfill, shape=series.shape)
        mopacity = toyplot.broadcast.scalar(mopacity, series.shape)
        mtitle = toyplot.broadcast.pyobject(mtitle, series.shape)
        style = toyplot.style.require(style, allowed=toyplot.style.allowed.line)
        mstyle = toyplot.style.require(mstyle, allowed=toyplot.style.allowed.marker)
        mlstyle = toyplot.style.require(mlstyle, allowed=toyplot.style.allowed.text)

        if along == "x":
            coordinate_axes = ["x", "y"]
        elif along == "y":
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

        return self.add_mark(
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
                filename=filename,
                ))


    def rectangle(
            self,
            a,
            b,
            c,
            d,
            along="x",
            color=None,
            filename=None,
            opacity=1.0,
            style=None,
            title=None,
        ):
        table = toyplot.data.Table()
        table["left"] = toyplot.require.scalar_vector(a)
        table["right"] = toyplot.require.scalar_vector(
            b, length=table.shape[0])
        table["top"] = toyplot.require.scalar_vector(c, length=table.shape[0])
        table["bottom"] = toyplot.require.scalar_vector(
            d, length=table.shape[0])
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.pyobject(title, table.shape[0])
        style = toyplot.style.combine(
            {"stroke": "none"},
            toyplot.style.require(style, allowed=toyplot.style.allowed.fill),
            )

        default_color = [next(self._rect_colors)]
        table["toyplot:fill"] = toyplot.color.broadcast(
            colors=color,
            shape=(table.shape[0], 1),
            default=default_color,
            )[:, 0]

        if along == "x":
            coordinate_axes = ["x", "y"]
        elif along == "y":
            coordinate_axes = ["y", "x"]

        return self.add_mark(
            toyplot.mark.Range(
                coordinate_axes=coordinate_axes,
                coordinates=["left", "right", "top", "bottom"],
                filename=filename,
                fill=["toyplot:fill"],
                opacity=["opacity"],
                style=style,
                table=table,
                title=["title"],
                ))


    def scatterplot(
            self,
            a,
            b=None,
            along="x",
            area=None,
            color=None,
            filename=None,
            hyperlink=None,
            marker="o",
            mlstyle=None,
            mstyle=None,
            opacity=1.0,
            size=None,
            title=None,
        ):
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
          Collection of CSS styles to apply across all datums.

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

        default_color = [next(self._scatterplot_colors) for i in range(series.shape[1])]
        mfill = toyplot.color.broadcast(
            colors=color,
            shape=series.shape,
            default=default_color,
            )
        marker = toyplot.broadcast.pyobject(marker, series.shape)

        if area is None and size is None:
            msize = toyplot.broadcast.scalar(4, series.shape)
        elif area is None and size is not None:
            msize = toyplot.broadcast.scalar(size, series.shape)
        elif area is not None and size is None:
            msize = numpy.sqrt(toyplot.broadcast.scalar(area, series.shape))
        else:
            toyplot.log.warning("Size parameter overrides area.")
            msize = toyplot.broadcast.scalar(size, series.shape)

        mstroke = toyplot.color.broadcast(colors=mfill, shape=series.shape)
        mopacity = toyplot.broadcast.scalar(opacity, series.shape)
        mtitle = toyplot.broadcast.pyobject(title, series.shape)
        mhyperlink = toyplot.broadcast.pyobject(hyperlink, series.shape)
        mstyle = toyplot.style.require(mstyle, allowed=toyplot.style.allowed.marker)
        mlstyle = toyplot.style.require(mlstyle, allowed=toyplot.style.allowed.text)

        if along == "x":
            coordinate_axes = ["x", "y"]
        elif along == "y":
            coordinate_axes = ["y", "x"]

        table = toyplot.data.Table()
        table[coordinate_axes[0]] = position
        _mark_exportable(table, coordinate_axes[0])
        coordinate_keys = []
        marker_keys = []
        msize_keys = []
        mfill_keys = []
        mstroke_keys = []
        mopacity_keys = []
        mtitle_keys = []
        mhyperlink_keys = []
        for index, (series_column, marker_column, msize_column, mfill_column, mstroke_column, mopacity_column, mtitle_column, mhyperlink_column) in enumerate(
                zip(series.T, marker.T, msize.T, mfill.T, mstroke.T, mopacity.T, mtitle.T, mhyperlink.T)):
            coordinate_keys.append(coordinate_axes[0])
            coordinate_keys.append(coordinate_axes[1] + str(index))
            marker_keys.append("marker" + str(index))
            msize_keys.append("size" + str(index))
            mfill_keys.append("fill" + str(index))
            mstroke_keys.append("stroke" + str(index))
            mopacity_keys.append("opacity" + str(index))
            mtitle_keys.append("title" + str(index))
            mhyperlink_keys.append("hyperlink" + str(index))
            table[coordinate_keys[-1]] = series_column
            _mark_exportable(table, coordinate_keys[-1])
            table[marker_keys[-1]] = marker_column
            table[msize_keys[-1]] = msize_column
            table[mfill_keys[-1]] = mfill_column
            table[mstroke_keys[-1]] = mstroke_column
            table[mopacity_keys[-1]] = mopacity_column
            table[mtitle_keys[-1]] = mtitle_column
            table[mhyperlink_keys[-1]] = mhyperlink_column

        return self.add_mark(
            toyplot.mark.Point(
                coordinate_axes=coordinate_axes,
                coordinates=coordinate_keys,
                filename=filename,
                marker=marker_keys,
                mfill=mfill_keys,
                mhyperlink=mhyperlink_keys,
                mlstyle=mlstyle,
                mopacity=mopacity_keys,
                msize=msize_keys,
                mstroke=mstroke_keys,
                mstyle=mstyle,
                mtitle=mtitle_keys,
                table=table,
                ))

    def share(
            self,
            axis="x",
            hyperlink=None,
            palette=None,
            xlabel=None,
            xmax=None,
            xmin=None,
            xscale="linear",
            xticklocator=None,
            ylabel=None,
            ymax=None,
            ymin=None,
            yscale="linear",
            yticklocator=None,
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

        Returns
        -------
        axes: :class:`toyplot.coordinates.Cartesian`
        """

        shared = Cartesian(
            aspect=self._aspect,
            hyperlink=hyperlink,
            label=None,
            padding=self._padding,
            palette=palette,
            scenegraph=self._scenegraph,
            show=True,
            xaxis=self.x if axis == "x" else None,
            xlabel=xlabel,
            xmax=xmax,
            xmax_range=self._xmax_range,
            xmin=xmin,
            xmin_range=self._xmin_range,
            xscale=xscale,
            xshow=True,
            xticklocator=xticklocator,
            yaxis=self.y if axis == "y" else None,
            ylabel=ylabel,
            ymax=ymax,
            ymax_range=self._ymax_range,
            ymin=ymin,
            ymin_range=self._ymin_range,
            yscale=yscale,
            yshow=True,
            yticklocator=yticklocator,
            )

        shared.x.spine.position = "high" if axis == "y" else "low"
        shared.y.spine.position = "high" if axis == "x" else "low"

        self.hyperlink = None

        for parent in self._scenegraph.sources("render", self):
            self._scenegraph.add_edge(parent, "render", shared)

        return shared

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
            annotation=True,
        ):
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
        _mark_exportable(table, "x")
        table["y"] = toyplot.require.scalar_vector(b, table.shape[0])
        _mark_exportable(table, "y")
        table["text"] = toyplot.broadcast.pyobject(text, table.shape[0])
        _mark_exportable(table, "text")
        table["angle"] = toyplot.broadcast.scalar(angle, table.shape[0])
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.pyobject(title, table.shape[0])
        style = toyplot.style.require(style, allowed=toyplot.style.allowed.text)

        default_color = [next(self._text_colors)]

        color = toyplot.color.broadcast(
            colors=color,
            shape=(table.shape[0], 1),
            default=default_color,
            )
        table["fill"] = color[:, 0]

        return self.add_mark(
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
                annotation=annotation,
                filename=filename,
                ))

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
        mark: :class:`toyplot.mark.AxisLines`
        """
        table = toyplot.data.Table()
        table["x"] = toyplot.require.scalar_vector(x)
        _mark_exportable(table, "x")
        color = toyplot.color.broadcast(
            colors=color,
            shape=(table.shape[0], 1),
            default=toyplot.color.black,
            )
        table["color"] = color[:, 0]
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.pyobject(title, table.shape[0])
        style = toyplot.style.require(style, allowed=toyplot.style.allowed.line)

        return self.add_mark(
            toyplot.mark.AxisLines(
                coordinate_axes=["x"],
                table=table,
                coordinates=["x"],
                stroke=["color"],
                opacity=["opacity"],
                title=["title"],
                style=style,
                annotation=annotation,
                ))


##########################################################################
# Numberline

class Numberline(object):
    """Standard one-dimensional coordinate system / numberline.

    Do not create Numberline instances directly.  Use factory methods such
    as :meth:`toyplot.canvas.Canvas.numberline` instead.
    """
    def __init__(
            self,
            x1,
            y1,
            x2,
            y2,
            padding,
            palette,
            spacing,
            min,
            max,
            show,
            label,
            ticklocator,
            scale,
            scenegraph,
        ):

        if palette is None:
            palette = toyplot.color.Palette()

        self._finalized = None

        self._axis = Axis(
            show=show,
            label=label,
            domain_min=min,
            domain_max=max,
            tick_locator=ticklocator,
            tick_angle=0,
            scale=scale,
            )
        self._child_offset = {}
        self._palette = palette
        self._scenegraph = scenegraph
        self._scatterplot_colors = itertools.cycle(self._palette)
        self._range_colors = itertools.cycle(self._palette)
        self._child_style = {}
        self._child_width = {}
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        self.padding = padding
        self.spacing = spacing

    @property
    def axis(self):
        """:class:`toyplot.coordinates.Axis` instance that provides the numberline
        coordinate system."""
        return self._axis

    @property
    def show(self):
        """Control axis visibility.

        Use the `show` property to hide all visible parts of the axis: label,
        spine, ticks, tick labels, etc.  Note that this does not affect
        visibility of the numberline contents, just the axis.
        """
        return self.axis.show

    @show.setter
    def show(self, value):
        self.axis.show = value

    @property
    def padding(self):
        """Control the default distance between the axis spine and data.

        By default, the axis spine is offset slightly from the data, to avoid
        visual clutter and overlap.  Use `padding` to change this offset.
        The default units are CSS pixels, but you may specify the padding
        using any :ref:`units` you like.
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = toyplot.units.convert(value, target="px", default="px")

    @property
    def spacing(self):
        """Control the default distance between data added to the numberline.

        The default units are CSS pixels, but you may specify the spacing
        using any :ref:`units` you like.
        """
        return self._spacing

    @spacing.setter
    def spacing(self, value):
        self._spacing = toyplot.units.convert(value, target="px", default="px")

    def _update_domain(self, values, display=True, data=True):
        self.axis._update_domain([values], display=display, data=data)

    def add_mark(self, mark):
        """Add a mark to the axes.

        This is only of use when creating your own custom Toyplot marks.  It is
        not intended for end-users.

        Example
        -------
        To add your own custom mark to a set of axes::

            mark = axes.add(MyCustomMark())

        Parameters
        ----------
        mark: :class:`toyplot.mark.Mark`, required

        Returns
        -------
        mark: :class:`toyplot.mark.Mark`
        """

        if not isinstance(mark, toyplot.mark.Mark):
            raise ValueError("Expected toyplot.mark.Mark, received %s" % type(mark))
        self._scenegraph.add_edge(self, "render", mark)
        return mark


    def _default_offset(self, offset):
        if offset is None:
            offset = len(self._scenegraph.targets(self, "render")) * self._spacing
        return offset


    def colormap(self, colormap, offset=None, width=10, style=None):
        if not isinstance(colormap, toyplot.color.Map):
            raise ValueError("A toyplot.color.Map instance is required.") # pragma: no cover
        if colormap.domain.min is None or colormap.domain.max is None:
            raise ValueError("Cannot create color scale without explicit colormap domain.") # pragma: no cover

        offset = self._default_offset(offset)

        self._update_domain(numpy.array([colormap.domain.min, colormap.domain.max]), display=True, data=True)
        self._child_offset[colormap] = offset
        self._child_width[colormap] = width
        self._child_style[colormap] = style

        self._scenegraph.add_edge(self, "render", colormap)


    def range(
            self,
            start,
            end,
            color=None,
            filename=None,
            offset=None,
            opacity=1.0,
            style=None,
            title=None,
            width=10,
        ):

        offset = self._default_offset(offset)

        table = toyplot.data.Table()
        table["start"] = toyplot.require.scalar_vector(start)
        table["end"] = toyplot.require.scalar_vector(
            end, length=table.shape[0])
        table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
        table["title"] = toyplot.broadcast.pyobject(title, table.shape[0])
        style = toyplot.style.combine(
            {"stroke": "none"},
            toyplot.style.require(style, allowed=toyplot.style.allowed.fill),
            )

        default_color = [next(self._range_colors)]
        table["toyplot:fill"] = toyplot.color.broadcast(
            colors=color,
            shape=(table.shape[0], 1),
            default=default_color,
            )[:, 0]

        mark = self.add_mark(
            toyplot.mark.Range(
                coordinate_axes=["axis"],
                coordinates=["start", "end"],
                filename=filename,
                fill=["toyplot:fill"],
                opacity=["opacity"],
                style=style,
                table=table,
                title=["title"],
                ))

        self._child_offset[mark] = offset
        self._child_width[mark] = width

        self._update_domain(numpy.column_stack((table["start"], table["end"])), display=True, data=True)

        return mark


    def scatterplot(
            self,
            coordinates,
            area=None,
            color=None,
            filename=None,
            hyperlink=None,
            marker="o",
            mlstyle=None,
            mstyle=None,
            offset=None,
            opacity=1.0,
            size=None,
            title=None,
            ):
        """Add a univariate plot to the axes.

        Parameters
        ----------
        coordinate: array-like one-dimensional coordinates
        title: string, optional
          Human-readable title for the mark.  The SVG / HTML backends render the
          title as a tooltip.
        style: dict, optional
          Collection of CSS styles to apply across all datums.

        Returns
        -------
        plot: :class:`toyplot.mark.Plot`
        """
        coordinates = numpy.ma.array(coordinates).astype("float64")
        if coordinates.ndim == 1:
            coordinates = numpy.ma.column_stack((coordinates,))
        elif coordinates.ndim == 2:
            pass

        default_color = [next(self._scatterplot_colors) for i in range(coordinates.shape[1])]
        mfill = toyplot.color.broadcast(
            colors=color,
            shape=coordinates.shape,
            default=default_color,
            )
        marker = toyplot.broadcast.pyobject(marker, coordinates.shape)

        if area is None and size is None:
            msize = toyplot.broadcast.scalar(4, coordinates.shape)
        elif area is None and size is not None:
            msize = toyplot.broadcast.scalar(size, coordinates.shape)
        elif area is not None and size is None:
            msize = numpy.sqrt(toyplot.broadcast.scalar(area, coordinates.shape))
        else:
            toyplot.log.warning("Size parameter overrides area.")
            msize = toyplot.broadcast.scalar(size, coordinates.shape)

        mstroke = toyplot.color.broadcast(colors=mfill, shape=coordinates.shape)
        mopacity = toyplot.broadcast.scalar(opacity, coordinates.shape)
        mtitle = toyplot.broadcast.pyobject(title, coordinates.shape)
        mhyperlink = toyplot.broadcast.pyobject(hyperlink, coordinates.shape)
        mstyle = toyplot.style.require(mstyle, allowed=toyplot.style.allowed.marker)
        mlstyle = toyplot.style.require(mlstyle, allowed=toyplot.style.allowed.text)

        self._update_domain(coordinates)
        coordinate_axes = ["x"]

        table = toyplot.data.Table()
        coordinate_keys = []
        marker_keys = []
        msize_keys = []
        mfill_keys = []
        mstroke_keys = []
        mopacity_keys = []
        mtitle_keys = []
        mhyperlink_keys = []
        for index, (coordinate_column, marker_column, msize_column, mfill_column, mstroke_column, mopacity_column, mtitle_column, mhyperlink_column) in enumerate(
                zip(coordinates.T, marker.T, msize.T, mfill.T, mstroke.T, mopacity.T, mtitle.T, mhyperlink.T)):
            coordinate_keys.append(coordinate_axes[0] + str(index))
            marker_keys.append("marker" + str(index))
            msize_keys.append("size" + str(index))
            mfill_keys.append("fill" + str(index))
            mstroke_keys.append("stroke" + str(index))
            mopacity_keys.append("opacity" + str(index))
            mtitle_keys.append("title" + str(index))
            mhyperlink_keys.append("hyperlink" + str(index))
            table[coordinate_keys[-1]] = coordinate_column
            _mark_exportable(table, coordinate_keys[-1])
            table[marker_keys[-1]] = marker_column
            table[msize_keys[-1]] = msize_column
            table[mfill_keys[-1]] = mfill_column
            table[mstroke_keys[-1]] = mstroke_column
            table[mopacity_keys[-1]] = mopacity_column
            table[mtitle_keys[-1]] = mtitle_column
            table[mhyperlink_keys[-1]] = mhyperlink_column

        offset = self._default_offset(offset)

        mark = toyplot.mark.Point(
            coordinate_axes=coordinate_axes,
            coordinates=coordinate_keys,
            filename=filename,
            marker=marker_keys,
            mfill=mfill_keys,
            mhyperlink=mhyperlink_keys,
            mlstyle=mlstyle,
            mopacity=mopacity_keys,
            msize=msize_keys,
            mstroke=mstroke_keys,
            mstyle=mstyle,
            mtitle=mtitle_keys,
            table=table,
            )

        self.add_mark(mark)
        self._child_offset[mark] = offset

        return mark

    def _finalize(self):
        if self._finalized is None:
            # Begin with the implicit domain defined by our data.
            domain_min = self.axis._display_min
            domain_max = self.axis._display_max

            # If there is no implicit domain (we don't have any data), default
            # to the origin.
            if domain_min is None:
                domain_min = 0
            if domain_max is None:
                domain_max = 0

            # Ensure that the domain is never empty.
            if domain_min == domain_max:
                domain_min -= 0.5
                domain_max += 0.5

            # Allow users to override the domain.
            if self.axis.domain.min is not None:
                domain_min = self.axis.domain.min
            if self.axis.domain.max is not None:
                domain_max = self.axis.domain.max

            # Ensure that the domain is never empty.
            if domain_min == domain_max:
                domain_min -= 0.5
                domain_max += 0.5

            # Calculate tick locations and labels.
            tick_locations = []
            tick_labels = []
            tick_titles = []
            if self.axis.show:
                tick_locations, tick_labels, tick_titles = self.axis._locator().ticks(domain_min, domain_max)

            # Allow tick locations to grow (never shrink) the domain.
            if len(tick_locations):
                domain_min = numpy.amin((domain_min, tick_locations[0]))
                domain_max = numpy.amax((domain_max, tick_locations[-1]))

            # Finalize the axis.
            self.axis._finalize(
                x1=self._x1,
                x2=self._x2,
                y1=self._y1,
                y2=self._y2,
                offset=self.padding,
                domain_min=domain_min,
                domain_max=domain_max,
                tick_locations=tick_locations,
                tick_labels=tick_labels,
                tick_titles=tick_titles,
                default_tick_location="below",
                default_ticks_near=3,
                default_ticks_far=3,
                default_label_location="below",
                #label_baseline_shift="-200%",
                )
            self._finalized = self

        return self._finalized


##########################################################################
# Table

class Table(object):
    """Row and column-based table coordinate system.

    Do not create Table instances directly.  Use factory methods such
    as :meth:`toyplot.canvas.Canvas.table` instead.
    """
    class Label(object):
        """Controls the appearance and behavior of the table label."""
        def __init__(self, text, style):

            self._style = {}
            self._text = None

            self.text = text

            self.style = {
                "font-weight": "bold",
                }
            self.style = style

        style = _create_text_style_property()
        text = _create_text_property()


    class CellMark(object):
        """Abstract interface for objects that embed other Toyplot visualizations in table cells."""
        def __init__(self, table, axes, series):
            self._table = table
            self._axes = axes
            self._series = toyplot.require.value_in(series, ["columns", "rows"])
            self._finalized = None

        def _finalize(self):
            raise NotImplementedError() # pragma: no cover

    class CellBarMark(CellMark):
        def __init__(
                self,
                table,
                axes,
                baseline,
                color,
                filename,
                opacity,
                padding,
                series,
                style,
                title,
                width,
            ):
            Table.CellMark.__init__(self, table, axes, series)

            self._baseline = baseline
            self._color = color
            self._filename = filename
            self._opacity = opacity
            self._padding = toyplot.units.convert(padding, "px", "px")
            self._style = style
            self._title = title
            self._width = toyplot.require.scalar(width)

        def _finalize(self):
            if self._finalized is None:
                rows, columns = numpy.nonzero(self._table._cell_axes == self._axes)
                row_min = rows.min()
                row_max = rows.max()
                column_min = columns.min()
                column_max = columns.max()

                if self._series == "columns":
                    shape = (row_max + 1 - row_min, column_max + 1 - column_min)
                    cell_begin = self._table._cell_top
                    cell_end = self._table._cell_bottom
                    cell_indices = numpy.unique(rows)
                    along = "y"
                    along_axis = self._axes.y
                    series = self._table._cell_data[self._table._cell_axes == self._axes].reshape(shape).astype("float64")
                elif self._series == "rows":
                    shape = (column_max + 1 - column_min, row_max + 1 - row_min)
                    cell_begin = self._table._cell_left
                    cell_end = self._table._cell_right
                    cell_indices = numpy.unique(columns)
                    along = "x"
                    along_axis = self._axes.x
                    series = self._table._cell_data[self._table._cell_axes == self._axes].reshape(shape).astype("float64")[:, ::-1]

                width = min(0.5 - numpy.finfo("float32").eps, 0.5 * self._width)
                begin = numpy.arange(shape[0]) - width
                end = numpy.arange(shape[0]) + width

                segments = []
                for index, cell_index in enumerate(cell_indices):
                    segments.append(toyplot.projection.Piecewise.Segment(
                        "linear",
                        index - 0.5,
                        index - 0.5,
                        index + 0.5,
                        index + 0.5,
                        cell_begin[cell_index] + self._padding,
                        cell_begin[cell_index] + self._padding,
                        cell_end[cell_index] - self._padding,
                        cell_end[cell_index] - self._padding,
                        ))
                projection = toyplot.projection.Piecewise(segments)
                along_axis._scale = projection

                color = self._color
                if color == "datum":
                    color = series
                elif isinstance(color, tuple) and len(color) == 2 and color[0] == "datum":
                    color = (series, color[1])

                self._finalized = self._axes.bars(
                    begin,
                    end,
                    series,
                    along=along,
                    baseline=self._baseline,
                    color=color,
                    filename=self._filename,
                    opacity=self._opacity,
                    style=self._style,
                    title=self._title,
                    )

                self._axes._scenegraph.remove_edge(self._axes, "render", self._finalized)

            return self._finalized

    class CellPlotMark(CellMark):
        def __init__(
                self,
                table,
                axes,
                area,
                color,
                filename,
                marker,
                mfill,
                mlstyle,
                mopacity,
                mstyle,
                mtitle,
                opacity,
                series,
                size,
                stroke_width,
                style,
                title,
            ):
            Table.CellMark.__init__(self, table, axes, series)
            self._area = area
            self._color = color
            self._filename = filename
            self._marker = marker
            self._mfill = mfill
            self._mlstyle = mlstyle
            self._mopacity = mopacity
            self._mstyle = mstyle
            self._mtitle = mtitle
            self._opacity = opacity
            self._size = size
            self._stroke_width = stroke_width
            self._style = style
            self._title = title

        def _finalize(self):
            if self._finalized is None:
                rows, columns = numpy.nonzero(self._table._cell_axes == self._axes)
                row_min = rows.min()
                row_max = rows.max()
                column_min = columns.min()
                column_max = columns.max()

                if self._series == "columns":
                    shape = (row_max + 1 - row_min, column_max + 1 - column_min)
                    cell_begin = self._table._cell_top
                    cell_end = self._table._cell_bottom
                    cell_indices = numpy.unique(rows)
                    along = "y"
                    along_axis = self._axes.y
                    series = self._table._cell_data[self._table._cell_axes == self._axes].reshape(shape).astype("float64")
                elif self._series == "rows":
                    shape = (column_max + 1 - column_min, row_max + 1 - row_min)
                    cell_begin = self._table._cell_left
                    cell_end = self._table._cell_right
                    cell_indices = numpy.unique(columns)
                    along = "x"
                    along_axis = self._axes.x
                    series = self._table._cell_data[self._table._cell_axes == self._axes].reshape(shape).astype("float64")[:, ::-1]

                segments = []
                for index, cell_index in enumerate(cell_indices):
                    segments.append(toyplot.projection.Piecewise.Segment(
                        "linear",
                        index - 0.5,
                        index - 0.5,
                        index + 0.5,
                        index + 0.5,
                        cell_begin[cell_index],
                        cell_begin[cell_index],
                        cell_end[cell_index],
                        cell_end[cell_index],
                        ))
                projection = toyplot.projection.Piecewise(segments)
                along_axis._scale = projection

                color = self._color
                if color == "datum":
                    color = series
                elif isinstance(color, tuple) and len(color) == 2 and color[0] == "datum":
                    color = (series, color[1])

                mfill = self._mfill
                if mfill == "datum":
                    mfill = series
                elif isinstance(mfill, tuple) and len(mfill) == 2 and mfill[0] == "datum":
                    mfill = (series, mfill[1])

                self._finalized = self._axes.plot(
                    series,
                    along=along,
                    area=self._area,
                    color=color,
                    filename=self._filename,
                    marker=self._marker,
                    mfill=mfill,
                    mlstyle=self._mlstyle,
                    mopacity=self._mopacity,
                    mstyle=self._mstyle,
                    mtitle=self._mtitle,
                    opacity=self._opacity,
                    size=self._size,
                    stroke_width=self._stroke_width,
                    style=self._style,
                    title=self._title,
                    )

                self._axes._scenegraph.remove_edge(self._axes, "render", self._finalized)

            return self._finalized

    class EmbeddedCartesian(Cartesian):
        def __init__(self, table, *args, **kwargs):
            toyplot.coordinates.Cartesian.__init__(self, *args, xmin_range=0, xmax_range=1, ymin_range=0, ymax_range=1, **kwargs)
            self._table = table

        def cell_bars(
                self,
                baseline="stacked",
                color=None,
                filename=None,
                opacity=1.0,
                padding=0,
                series="columns",
                style=None,
                title=None,
                width=0.5,
            ):

            return self.add_mark(
                toyplot.coordinates.Table.CellBarMark(
                    table=self._table,
                    axes=self,
                    baseline=baseline,
                    color=color,
                    filename=filename,
                    opacity=opacity,
                    padding=padding,
                    series=series,
                    style=style,
                    title=title,
                    width=width,
                    ))


        def cell_plot(
                self,
                area=None,
                color=None,
                filename=None,
                marker=None,
                mfill=None,
                mlstyle=None,
                mopacity=1.0,
                mstyle=None,
                mtitle=None,
                opacity=1.0,
                series="columns",
                size=None,
                stroke_width=2.0,
                style=None,
                title=None,
            ):

            return self.add_mark(
                toyplot.coordinates.Table.CellPlotMark(
                    table=self._table,
                    axes=self,
                    area=area,
                    color=color,
                    filename=filename,
                    marker=marker,
                    mfill=mfill,
                    mlstyle=mlstyle,
                    mopacity=mopacity,
                    mstyle=mstyle,
                    mtitle=mtitle,
                    opacity=opacity,
                    series=series,
                    size=size,
                    stroke_width=stroke_width,
                    style=style,
                    title=title,
                    ))


    class CellReference(object):
        def __init__(self, table, selection):
            self._table = table
            self._selection = selection

        def _set_align(self, value):
            self._table._cell_align[self._selection] = value
        align = property(fset=_set_align)

        def _set_angle(self, value):
            self._table._cell_angle[self._selection] = value
        angle = property(fset=_set_angle)

        def _set_data(self, value):
            self._table._cell_data[self._selection] = numpy.array(value).flat
        data = property(fset=_set_data)

        def _set_format(self, value):
            self._table._cell_format[self._selection] = value
        format = property(fset=_set_format)

        def _set_height(self, value):
            row_indices, column_indices = self._table._selection_coordinates(self._selection)
            self._table._row_heights[row_indices] = toyplot.units.convert(value, "px", "px")
        height = property(fset=_set_height)

        def _set_lstyle(self, value):
            value = toyplot.style.require(value, allowed=toyplot.style.allowed.text)
            value = [toyplot.style.combine(style, value) for style in self._table._cell_lstyle[self._selection]]
            self._table._cell_lstyle[self._selection] = value
        lstyle = property(fset=_set_lstyle)

        def _set_show(self, value):
            self._table._cell_show[self._selection] = True if value else False
        show = property(fset=_set_show)

        def _set_style(self, value):
            value = toyplot.style.require(value, allowed=toyplot.style.allowed.fill)
            value = [toyplot.style.combine(style, value) for style in self._table._cell_style[self._selection]]
            self._table._cell_style[self._selection] = value
        style = property(fset=_set_style)

        def _set_title(self, value):
            self._table._cell_title[self._selection] = str(value)
        title = property(fset=_set_title)

        def _set_hyperlink(self, value):
            self._table._cell_hyperlink[self._selection] = str(value)
        hyperlink = property(fset=_set_hyperlink)

        def _set_width(self, value):
            row_indices, column_indices = self._table._selection_coordinates(self._selection)
            self._table._column_widths[column_indices] = toyplot.units.convert(value, "px", "px")
        width = property(fset=_set_width)

        def cartesian(
                self,
                aspect=None,
                hyperlink=None,
                cell_padding=3,
                label=None,
                padding=3,
                palette=None,
                show=True,
                xlabel=None,
                xmax=None,
                xmin=None,
                xscale="linear",
                xshow=False,
                xticklocator=None,
                ylabel=None,
                ymax=None,
                ymin=None,
                yscale="linear",
                yshow=False,
                yticklocator=None,
            ):

            axes = toyplot.coordinates.Table.EmbeddedCartesian(
                aspect=aspect,
                hyperlink=hyperlink,
                label=label,
                padding=padding,
                palette=palette,
                scenegraph=self._table._scenegraph,
                show=show,
                xaxis=None,
                xlabel=xlabel,
                xmax=xmax,
                xmin=xmin,
                xscale=xscale,
                xshow=xshow,
                xticklocator=xticklocator,
                yaxis=None,
                ylabel=ylabel,
                ymax=ymax,
                ymin=ymin,
                yscale=yscale,
                yshow=yshow,
                yticklocator=yticklocator,
                table=self._table,
                )

            self._table._merge_cells(self._selection)
            self._table._cell_format[self._selection] = toyplot.format.NullFormatter()
            self._table._cell_axes[self._selection] = axes
            self._table._axes.append(axes)
            self._table._axes_padding.append(cell_padding)

            return axes

        def merge(self):
            self._table._merge_cells(self._selection)
            self._table._cell_data[self._selection] = self._table._cell_data[self._selection][0]
            return self

    class ColumnCellReference(CellReference):
        def __init__(self, table, selection):
            Table.CellReference.__init__(self, table, selection)

        def delete(self):
            row_indices, column_indices = self._table._selection_coordinates(self._selection)
            self._table._delete_cells(column_indices, axis=1)

    class RowCellReference(CellReference):
        def __init__(self, table, selection):
            Table.CellReference.__init__(self, table, selection)

        def delete(self):
            row_indices, column_indices = self._table._selection_coordinates(self._selection)
            self._table._delete_cells(row_indices, axis=0)

    class DistanceArrayReference(object):
        def __init__(self, array):
            self._array = array

        def __getitem__(self, key):
            return self._array[key]

        def __setitem__(self, key, value):
            self._array[key] = toyplot.units.convert(value, "px", "px")

    class GapReference(object):
        def __init__(self, row_gaps, column_gaps):
            self._row_gaps = row_gaps
            self._column_gaps = column_gaps

        @property
        def rows(self):
            return Table.DistanceArrayReference(self._row_gaps)

        @property
        def columns(self):
            return Table.DistanceArrayReference(self._column_gaps)

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
                self._table._gstyle,
                toyplot.style.require(value, toyplot.style.allowed.line),
                )

    class Region(object):
        class ColumnAccessor(object):
            def __init__(self, region):
                self._region = region

            def __getitem__(self, selection):
                table, region = self._region._selection()
                region[Ellipsis, selection] = True
                return Table.ColumnCellReference(self._region._table, table)

            def insert(self, before=None, after=None):
                if (before is None) + (after is None) != 1:
                    raise ValueError("Specify either before or after.")
                if before is not None:
                    table, region = self._region._selection()
                    region[Ellipsis, before] = True
                    rows, columns = numpy.nonzero(table)
                    before = numpy.unique(columns)
                if after is not None:
                    table, region = self._region._selection()
                    region[Ellipsis, after] = True
                    rows, columns = numpy.nonzero(table)
                    after = numpy.unique(columns)
                self._region._table._insert_cells(before=before, after=after, axis=1)

        class RowAccessor(object):
            def __init__(self, region):
                self._region = region

            def __getitem__(self, selection):
                table, region = self._region._selection()
                region[selection, Ellipsis] = True
                return Table.RowCellReference(self._region._table, table)

            def insert(self, before=None, after=None):
                if (before is None) + (after is None) != 1:
                    raise ValueError("Specify either before or after.")
                if before is not None:
                    table, region = self._region._selection()
                    region[before, Ellipsis] = True
                    rows, columns = numpy.nonzero(table)
                    before = numpy.unique(rows)
                if after is not None:
                    table, region = self._region._selection()
                    region[after, Ellipsis] = True
                    rows, columns = numpy.nonzero(table)
                    after = numpy.unique(rows)
                self._region._table._insert_cells(before=before, after=after, axis=0)

        class CellAccessor(object):
            def __init__(self, region):
                self._region = region

            def __getitem__(self, selection):
                table, region = self._region._selection()
                region[selection] = True
                return Table.CellReference(self._region._table, table)

        def __init__(self, table, row_begin, row_end, column_begin, column_end):
            self._table = table
            self._row_begin = row_begin
            self._row_end = row_end
            self._column_begin = column_begin
            self._column_end = column_end

        def _selection(self):
            table = numpy.zeros(self._table._shape, dtype="bool")
            region = table[self._row_begin:self._row_end, self._column_begin:self._column_end]
            return table, region

        @property
        def cell(self):
            return Table.Region.CellAccessor(self)

        @property
        def cells(self):
            region_selection = numpy.zeros(self._table._shape, dtype="bool")
            region_selection[self._row_begin:self._row_end, self._column_begin:self._column_end] = True
            return Table.CellReference(self._table, region_selection)

        @property
        def column(self):
            return Table.Region.ColumnAccessor(self)

        @property
        def gaps(self):
            return Table.GapReference(self._table._row_gaps[self._row_begin:self._row_end-1], self._table._column_gaps[self._column_begin: self._column_end-1])

        @property
        def grid(self):
            return Table.GridReference(
                self._table,
                self._table._hlines[self._row_begin:self._row_end+1, self._column_begin:self._column_end],
                self._table._vlines[self._row_begin:self._row_end, self._column_begin:self._column_end+1],
                )

        @property
        def row(self):
            return Table.Region.RowAccessor(self)

        @property
        def shape(self):
            return (self._row_end - self._row_begin, self._column_end - self._column_begin)

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
            lcolumns,
            rcolumns,
            label,
            scenegraph,
            annotation,
            filename,
        ):
        self._finalized = None

        self._xmin_range = xmin_range
        self._xmax_range = xmax_range
        self._ymin_range = ymin_range
        self._ymax_range = ymax_range
        self._scenegraph = scenegraph
        self._annotation = False
        self.annotation = annotation
        self._filename = toyplot.require.filename(filename)

        self._shape = (trows + rows + brows, lcolumns + columns + rcolumns)

        self._cell_align = numpy.empty(self._shape, dtype="object")
        self._cell_angle = numpy.zeros(self._shape, dtype="float")
        self._cell_axes = numpy.empty(self._shape, dtype="object")
        self._cell_data = numpy.empty(self._shape, dtype="object")
        self._cell_format = numpy.tile(toyplot.format.BasicFormatter(), self._shape)
        self._cell_group = numpy.arange(self._shape[0] * self._shape[1]).reshape(self._shape)
        self._cell_lstyle = numpy.empty(self._shape, dtype="object")

        self._cell_region = numpy.zeros(self._shape, dtype="int")
        self._cell_region[:trows, :lcolumns] = 0
        self._cell_region[:trows, lcolumns:lcolumns+columns] = 1
        self._cell_region[:trows, lcolumns+columns:] = 2
        self._cell_region[trows:trows+rows, :lcolumns] = 3
        self._cell_region[trows:trows+rows, lcolumns:lcolumns+columns] = 4
        self._cell_region[trows:trows+rows, lcolumns+columns:] = 5
        self._cell_region[trows+rows:, :lcolumns] = 6
        self._cell_region[trows+rows:, lcolumns:lcolumns+columns] = 7
        self._cell_region[trows+rows:, lcolumns+columns:] = 8

        self._cell_show = numpy.ones(self._shape, dtype="bool")
        self._cell_style = numpy.empty(self._shape, dtype="object")
        self._cell_title = numpy.empty(self._shape, dtype="object")
        self._cell_hyperlink = numpy.empty(self._shape, dtype="object")

        self._hlines = numpy.empty((self._shape[0] + 1, self._shape[1]), dtype="object")
        self._hlines_show = numpy.ones((self._shape[0] + 1, self._shape[1]), dtype="bool")
        self._vlines = numpy.empty((self._shape[0], self._shape[1] + 1), dtype="object")
        self._vlines_show = numpy.ones((self._shape[0], self._shape[1] + 1), dtype="bool")

        self._row_heights = numpy.zeros(self._shape[0], dtype="float")
        self._row_gaps = numpy.zeros(self._shape[0] - 1, dtype="float")
        self._column_widths = numpy.zeros(self._shape[1], dtype="float")
        self._column_gaps = numpy.zeros(self._shape[1] - 1, dtype="float")

        self._axes = []
        self._axes_padding = []

        self._label = Table.Label(
            label, style={"font-size": "14px", "baseline-shift": "100%"})

        self._separation = 2
        self._gstyle = {"stroke": toyplot.color.black, "stroke-width": 0.5}

        lstyle = {
            }
        self._cell_lstyle[...] = lstyle
        self._cell_align[...] = "center"

    @property
    def annotation(self):
        return self._annotation

    @annotation.setter
    def annotation(self, value):
        self._annotation = True if value else False

    def _region_bounds(self, region):
        rows, columns = numpy.nonzero(self._cell_region == region)
        if len(rows) and len(columns):
            return (rows.min(), rows.max() + 1, columns.min(), columns.max() + 1)
        return (0, 0, 0, 0)

    def _selection_coordinates(self, selection):
        table_selection = numpy.zeros(self._shape, dtype="bool")
        table_selection[selection] = True
        return numpy.nonzero(table_selection)

    def _merge_cells(self, selection):
        self._cell_group[selection] = numpy.unique(self._cell_group).max() + 1 # pylint: disable=no-member

        # TODO: Handle non-rectangular shapes here
        row_indices, column_indices = self._selection_coordinates(selection)
        if row_indices.max() - row_indices.min() > 0:
            self._hlines_show[row_indices.min() + 1 : row_indices.max() + 1, column_indices.min() : column_indices.max() + 1] = False
        if column_indices.max() - column_indices.min() > 0:
            self._vlines_show[row_indices.min() : row_indices.max() + 1, column_indices.min() + 1 : column_indices.max() + 1] = False

    def _delete_cells(self, indices, axis):
        indices = numpy.unique(indices)

        self._cell_align = numpy.delete(self._cell_align, indices, axis=axis)
        self._cell_angle = numpy.delete(self._cell_angle, indices, axis=axis)
        self._cell_axes = numpy.delete(self._cell_axes, indices, axis=axis)
        self._cell_data = numpy.delete(self._cell_data, indices, axis=axis)
        self._cell_format = numpy.delete(self._cell_format, indices, axis=axis)
        self._cell_group = numpy.delete(self._cell_group, indices, axis=axis)
        self._cell_lstyle = numpy.delete(self._cell_lstyle, indices, axis=axis)
        self._cell_region = numpy.delete(self._cell_region, indices, axis=axis)
        self._cell_show = numpy.delete(self._cell_show, indices, axis=axis)
        self._cell_style = numpy.delete(self._cell_style, indices, axis=axis)
        self._cell_title = numpy.delete(self._cell_title, indices, axis=axis)
        self._cell_hyperlink = numpy.delete(self._cell_hyperlink, indices, axis=axis)

        self._hlines = numpy.delete(self._hlines, indices, axis=axis)
        self._hlines_show = numpy.delete(self._hlines_show, indices, axis=axis)

        self._vlines = numpy.delete(self._vlines, indices, axis=axis)
        self._vlines_show = numpy.delete(self._vlines_show, indices, axis=axis)

        if axis == 0:
            self._row_heights = numpy.delete(self._row_heights, indices)
        if axis == 1:
            self._column_widths = numpy.delete(self._column_widths, indices)

        # TODO: handle this better
        if axis == 0:
            self._row_gaps = self._row_gaps[len(indices):]
        if axis == 1:
            self._column_gaps = self._column_gaps[len(indices):]

        self._shape = self._cell_align.shape

    def _insert_cells(self, before, after, axis):
        # Create a selection for the source row / column.
        source = numpy.zeros(self.shape[axis], dtype="bool")
        if before is not None:
            source[before] = True
        if after is not None:
            source[after] = True
        source = numpy.flatnonzero(source)
        if axis == 0:
            source = (source, Ellipsis)
        if axis == 1:
            source = (Ellipsis, source)

        # Numpy always inserts *before* a given row / column, so convert everything into strictly "before" indices.
        position = numpy.zeros(self.shape[axis] + 1, dtype="bool")
        if before is not None:
            position[before] = True
        if after is not None:
            position[1:][after] = True
        position = numpy.flatnonzero(position)

        self._cell_align = numpy.insert(self._cell_align, position, None, axis=axis)
        self._cell_angle = numpy.insert(self._cell_angle, position, 0, axis=axis)
        self._cell_axes = numpy.insert(self._cell_axes, position, None, axis=axis)
        self._cell_data = numpy.insert(self._cell_data, position, None, axis=axis)
        self._cell_format = numpy.insert(self._cell_format, position, toyplot.format.BasicFormatter(), axis=axis)
        self._cell_group = numpy.insert(self._cell_group, position, -1, axis=axis)
        self._cell_group[self._cell_group == -1] = numpy.unique(self._cell_group).max() + 1 + numpy.arange(numpy.count_nonzero(self._cell_group == -1)) # pylint: disable=no-member
        self._cell_lstyle = numpy.insert(self._cell_lstyle, position, None, axis=axis)
        self._cell_region = numpy.insert(self._cell_region, position, self._cell_region[source], axis=axis)
        self._cell_show = numpy.insert(self._cell_show, position, True, axis=axis)
        self._cell_style = numpy.insert(self._cell_style, position, self._cell_style[source], axis=axis)
        self._cell_title = numpy.insert(self._cell_title, position, None, axis=axis)
        self._cell_hyperlink = numpy.insert(self._cell_hyperlink, position, None, axis=axis)

        self._hlines = numpy.insert(self._hlines, position, self._hlines[source], axis=axis)
        self._hlines_show = numpy.insert(self._hlines_show, position, True, axis=axis)

        self._vlines = numpy.insert(self._vlines, position, self._vlines[source], axis=axis)
        self._vlines_show = numpy.insert(self._vlines_show, position, True, axis=axis)

        if axis == 0:
            self._row_heights = numpy.insert(self._row_heights, position, 0)
        if axis == 1:
            self._column_widths = numpy.insert(self._column_widths, position, 0)

        # TODO: handle this better
        if axis == 0:
            self._row_gaps = numpy.concatenate((self._row_gaps, numpy.zeros(len(position))))
        if axis == 1:
            self._column_gaps = numpy.concatenate((self._column_gaps, numpy.zeros(len(position))))

        self._shape = self._cell_align.shape

    @property
    def body(self):
        region = Table.Region(self, *self._region_bounds(4))
        return region

    @property
    def bottom(self):
        region = Table.Region(self, *self._region_bounds(7))
        region.left = Table.Region(self, *self._region_bounds(6))
        region.right = Table.Region(self, *self._region_bounds(8))
        return region

    @property
    def cells(self):
        return Table.Region(self, 0, self.shape[0], 0, self.shape[1])

    @property
    def label(self):
        return self._label

    @property
    def left(self):
        region = Table.Region(self, *self._region_bounds(3))
        return region

    @property
    def right(self):
        region = Table.Region(self, *self._region_bounds(5))
        return region

    @property
    def shape(self):
        return self._shape

    @property
    def top(self):
        region = Table.Region(self, *self._region_bounds(1))
        region.left = Table.Region(self, *self._region_bounds(0))
        region.right = Table.Region(self, *self._region_bounds(2))
        return region

    def _finalize(self):
        if self._finalized is None:
            # Collect explicit row heights, column widths, and gaps.
            row_heights = numpy.zeros(len(self._row_heights) + len(self._row_gaps))
            row_heights[0::2] = self._row_heights
            row_heights[1::2] = self._row_gaps

            column_widths = numpy.zeros(len(self._column_widths) + len(self._column_gaps))
            column_widths[0::2] = self._column_widths
            column_widths[1::2] = self._column_gaps

            # Compute implicit heights and widths for the remaining rows and columns.
            table_height = self._ymax_range - self._ymin_range
            available_height = table_height - numpy.sum(row_heights)
            default_height = available_height / numpy.count_nonzero(row_heights[0::2] == 0)
            row_heights[0::2][row_heights[0::2] == 0] = default_height

            table_width = self._xmax_range - self._xmin_range
            available_width = table_width - numpy.sum(column_widths)
            default_width = available_width / numpy.count_nonzero(column_widths[0::2] == 0)
            column_widths[0::2][column_widths[0::2] == 0] = default_width

            row_boundaries = self._ymin_range + numpy.cumsum(numpy.concatenate(([0], row_heights)))
            column_boundaries = self._xmin_range + numpy.cumsum(numpy.concatenate(([0], column_widths)))

            # Compute cell boundaries.
            self._cell_top = row_boundaries[0::2]
            self._cell_bottom = row_boundaries[1::2]
            self._cell_left = column_boundaries[0::2]
            self._cell_right = column_boundaries[1::2]

            # Compute grid boundaries.
            self._row_boundaries = numpy.concatenate((
                row_boundaries[0:1],
                (row_boundaries[1:-1:2] + row_boundaries[2:-1:2]) / 2,
                row_boundaries[-1:],
                ))
            self._column_boundaries = numpy.concatenate((
                column_boundaries[0:1],
                (column_boundaries[1:-1:2] + column_boundaries[2:-1:2]) / 2,
                column_boundaries[-1:],
                ))

            # Assign ranges and finalize embedded coordinate systems.
            for axes, padding in zip(self._axes, self._axes_padding):
                axes_rows, axes_columns = numpy.nonzero(self._cell_axes == axes)
                row_min = axes_rows.min()
                row_max = axes_rows.max()
                column_min = axes_columns.min()
                column_max = axes_columns.max()

                if isinstance(axes, toyplot.coordinates.Cartesian):
                    axes.xmin_range = self._cell_left[column_min] + padding
                    axes.xmax_range = self._cell_right[column_max] - padding
                    axes.ymin_range = self._cell_top[row_min] + padding
                    axes.ymax_range = self._cell_bottom[row_max] - padding
                else:
                    raise NotImplementedError("Unknown coordinate system: %s" % axes) # pragma: no cover

            self._finalized = self
        return self._finalized
