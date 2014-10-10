# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import numpy
import toyplot.require


###############################################################################################
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
  def __init__(self, table, coordinates, axes, stroke, opacity, title, style):
    table = toyplot.require.instance(table, toyplot.data.Table)
    coordinates = toyplot.require.table_keys(table, coordinates, length=1)
    axes = toyplot.require.string_vector(axes, len(coordinates))
    stroke = toyplot.require.table_keys(table, stroke, length=1)
    opacity = toyplot.require.table_keys(table, opacity, length=1)
    title = toyplot.require.table_keys(table, title, length=1)
    style = toyplot.require.style(style)

    Mark.__init__(self)
    self._table = table
    self._coordinates = coordinates # 1 coordinate column
    self._axes = axes               # 1 axis identifier
    self._stroke = stroke           # 1 stroke color column
    self._opacity = opacity         # 1 opacity column
    self._title = title             # 1 title column
    self._style = style             # Line style

class BarBoundaries(Mark):
  """Render multiple stacked bars defined by bar boundaries.

  Do not create BarBoundaries instances directly.  Use factory methods such as
  :func:`toyplot.bars` or :meth:`toyplot.axes.Cartesian.bars` instead.
  """
  def __init__(self, table, left, right, left_right_axis, boundaries, boundary_axis, fill, opacity, title, style):
    table = toyplot.require.instance(table, toyplot.data.Table)
    left = toyplot.require.table_keys(table, left, length=1)
    right = toyplot.require.table_keys(table, right, length=1)
    left_right_axis = toyplot.require.string_vector(left_right_axis, length=1)
    boundaries = toyplot.require.table_keys(table, boundaries, min_length=2)
    boundary_axis = toyplot.require.string_vector(boundary_axis, length=1)
    fill = toyplot.require.table_keys(table, fill, length=len(boundaries)-1)
    opacity = toyplot.require.table_keys(table, opacity, length=len(boundaries)-1)
    title = toyplot.require.table_keys(table, title, length=len(boundaries)-1)
    style = toyplot.require.style(style)

    Mark.__init__(self)
    self._table = table
    self._left = left         # 1 coordinate column
    self._right = right       # 1 coordinate column
    self._left_right_axis = left_right_axis # 1 axis identifier
    self._boundaries = boundaries # N bar boundary columns
    self._boundary_axis = boundary_axis # 1 axis identifier
    self._fill = fill         #  N-1 fill color columns
    self._opacity = opacity   #  N-1 opacity columns
    self._title = title       #  N-1 title columns
    self._style = toyplot.style.combine({"stroke":"none"}, style) # Bar style

class BarMagnitudes(Mark):
  """Render multiple stacked bars defined by bar magnitudes.

  Do not create BarMagnitudes instances directly.  Use factory methods such as
  :func:`toyplot.bars` or :meth:`toyplot.axes.Cartesian.bars` instead.
  """
  def __init__(self, table, left, right, left_right_axis, baseline, magnitudes, magnitude_axis, fill, opacity, title, style):
    table = toyplot.require.instance(table, toyplot.data.Table)
    left = toyplot.require.table_keys(table, left, length=1)
    right = toyplot.require.table_keys(table, right, length=1)
    left_right_axis = toyplot.require.string_vector(left_right_axis, length=1)
    baseline = toyplot.require.table_keys(table, baseline, length=1)
    magnitudes = toyplot.require.table_keys(table, magnitudes, min_length=1)
    magnitude_axis = toyplot.require.string_vector(magnitude_axis, length=1)
    fill = toyplot.require.table_keys(table, fill, length=len(magnitudes))
    opacity = toyplot.require.table_keys(table, opacity, length=len(magnitudes))
    title = toyplot.require.table_keys(table, title, length=len(magnitudes))
    style = toyplot.require.style(style)

    Mark.__init__(self)
    self._table = table
    self._left = left         # 1 coordinate column
    self._right = right       # 1 coordinate column
    self._left_right_axis = left_right_axis # 1 axis identifier
    self._baseline = baseline # 1 baseline column
    self._magnitudes = magnitudes # N bar magnitude columns
    self._magnitude_axis = magnitude_axis # 1 axis identifier
    self._fill = fill         #  N fill color columns
    self._opacity = opacity   #  N opacity columns
    self._title = title       #  N title columns
    self._style = toyplot.style.combine({"stroke":"none"}, style) # Bar style

class FillBoundaries(Mark):
  """Render multiple stacked fill regions defined by boundaries.

  Do not create FillBoundaries instances directly.  Use factory methods such
  as :func:`toyplot.fill` or :meth:`toyplot.axes.Cartesian.fill` instead.
  """
  def __init__(self, table, position, position_axis, boundaries, boundary_axis, fill, opacity, title, style):
    table = toyplot.require.instance(table, toyplot.data.Table)
    position = toyplot.require.table_keys(table, position, length=1)
    position_axis = toyplot.require.string_vector(position_axis, length=1)
    boundaries = toyplot.require.table_keys(table, boundaries)
    boundary_axis = toyplot.require.string_vector(boundary_axis, length=1)
    style = toyplot.require.style(style)

    Mark.__init__(self)
    self._table = table
    self._position = position # 1 coordinate column
    self._position_axis = position_axis # 1 axis identifier
    self._boundaries = boundaries # N fill boundary columns
    self._boundary_axis = boundary_axis # 1 axis identifier
    self._fill = fill         # N-1 fill colors
    self._opacity = opacity   # N-1 opacities
    self._title = title       # N-1 titles
    self._style = style       # Fill style

class FillMagnitudes(Mark):
  """Render multiple stacked fill regions defined by magnitudes.

  Do not create FillMagnitudes instances directly.  Use factory methods such
  as :func:`toyplot.fill` or :meth:`toyplot.axes.Cartesian.fill` instead.
  """
  def __init__(self, table, position, position_axis, baseline, magnitudes, magnitude_axis, fill, opacity, title, style):
    table = toyplot.require.instance(table, toyplot.data.Table)
    position = toyplot.require.table_keys(table, position, length=1)
    position_axis = toyplot.require.string_vector(position_axis, length=1)
    baseline = toyplot.require.table_keys(table, baseline, length=1)
    magnitudes = toyplot.require.table_keys(table, magnitudes)
    magnitude_axis = toyplot.require.string_vector(magnitude_axis, length=1)
    style = toyplot.require.style(style)

    Mark.__init__(self)
    self._table = table
    self._position = position     # 1 coordinate column
    self._position_axis = position_axis # 1 axis identifier
    self._baseline = baseline     # 1 baseline column
    self._magnitudes = magnitudes # N fill magnitude columns
    self._magnitude_axis = magnitude_axis # 1 axis identifier
    self._fill = fill             # N fill colors
    self._opacity = opacity       # N opacities
    self._title = title           # N titles
    self._style = style           # Fill style

class Plot(Mark):
  """Plot multiple bivariate data series using lines and/or markers.

  Do not create Plot instances directly.  Use factory methods such as
  :func:`toyplot.plot`, :func:`toyplot.scatterplot`,
  :meth:`toyplot.axes.Cartesian.plot` and
  :meth:`toyplot.axes.Cartesian.scatterplot` instead.
  """
  def __init__(self, table, coordinates, coordinate_axes, series, series_axis, show_stroke, stroke, stroke_width, stroke_opacity, marker, size, fill, opacity, title, style, mstyle, mlstyle):
    table = toyplot.require.instance(table, toyplot.data.Table)
    coordinates = toyplot.require.table_keys(table, coordinates, min_length=1)
    coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=len(coordinates))
    series = toyplot.require.table_keys(table, series, min_length=1)
    series_axis = toyplot.require.string_vector(series_axis, length=1)
    # show_stroke
    # stroke
    # stroke_width
    # stroke_opacity
    marker = toyplot.require.table_keys(table, marker, length=len(series))
    size = toyplot.require.table_keys(table, size, length=len(series))
    fill = toyplot.require.table_keys(table, fill, length=len(series))
    opacity = toyplot.require.table_keys(table, opacity, length=len(series))
    # title
    style = toyplot.require.style(style)
    mstyle = toyplot.require.style(mstyle)
    mlstyle = toyplot.require.style(mlstyle)

    Mark.__init__(self)
    self._table = table
    self._coordinates = coordinates       # D-1 coordinate columns
    self._coordinate_axes = coordinate_axes # D-1 axis identifiers
    self._series = series                 # N coordinate columns
    self._series_axis = series_axis       # 1 axis identifier
    self._show_stroke = show_stroke       # Boolean
    self._stroke = stroke                 # N stroke colors
    self._stroke_width = stroke_width     # N stroke widths
    self._stroke_opacity = stroke_opacity # N stroke opacities
    self._marker = marker                 # N marker columns
    self._size = size                     # N marker size columns
    self._fill = fill                     # N marker fill color columns
    self._opacity = opacity               # N marker opacity columns
    self._title = title                   # N titles
    self._style = style                   # Line style
    self._mstyle = mstyle                 # Marker style
    self._mlstyle = mlstyle               # Marker label style

class Rect(Mark):
  """Plot axis-aligned rectangles.

  Do not create Rect instances directly.  Use factory methods such as
  :meth:`toyplot.axes.Cartesian.rect` instead.
  """
  def __init__(self, table, left, right, left_right_axis, top, bottom, top_bottom_axis, fill, opacity, title, style):
    table = toyplot.require.instance(table, toyplot.data.Table)
    left = toyplot.require.table_keys(table, left, length=1)
    right = toyplot.require.table_keys(table, right, length=1)
    left_right_axis = toyplot.require.string_vector(left_right_axis, length=1)
    top = toyplot.require.table_keys(table, top, length=1)
    bottom = toyplot.require.table_keys(table, bottom, length=1)
    top_bottom_axis = toyplot.require.string_vector(top_bottom_axis, length=1)
    fill = toyplot.require.table_keys(table, fill, length=1)
    opacity = toyplot.require.table_keys(table, opacity, length=1)
    title = toyplot.require.table_keys(table, title, length=1)
    style = toyplot.require.style(style)

    Mark.__init__(self)
    self._table = table
    self._left = left       # 1 coordinate column
    self._right = right     # 1 coordinate column
    self._left_right_axis = left_right_axis # 1 axis identifier
    self._top = top         # 1 coordinate column
    self._bottom = bottom   # 1 coordinate column
    self._top_bottom_axis = top_bottom_axis # 1 axis identifier
    self._fill = fill       # 1 fill color column
    self._opacity = opacity # 1 opacity column
    self._title = title     # 1 title column
    self._style = style     # Rectangle style

class Text(Mark):
  """Render text.

  Do not create Text instances directly.  Use factory methods such as
  :meth:`toyplot.canvas.Canvas.text` or :meth:`toyplot.axes.Cartesian.text` instead.
  """
  def __init__(self, table, coordinates, axes, text, angle, fill, opacity, title, style):
    table = toyplot.require.instance(table, toyplot.data.Table)
    coordinates = toyplot.require.table_keys(table, coordinates)
    axes = toyplot.require.string_vector(axes, length=len(coordinates))
    text = toyplot.require.table_keys(table, text, length=1)
    angle = toyplot.require.table_keys(table, angle, length=1)
    fill = toyplot.require.table_keys(table, fill, length=1)
    opacity = toyplot.require.table_keys(table, opacity, length=1)
    title = toyplot.require.table_keys(table, title, length=1)
    style = toyplot.require.style(style)

    Mark.__init__(self)
    self._table = table
    self._coordinates = coordinates # D coordinate columns
    self._axes = axes               # D axis identifiers
    self._text = text               # 1 text column
    self._angle = angle             # 1 angle column
    self._fill = fill               # 1 fill color column
    self._opacity = opacity         # 1 opacity column
    self._title = title             # 1 title column
    self._style = style             # Text style

###############################################################################################
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
    self._style = toyplot.style.combine({"fill":"none", "stroke":"none"}, style) # Styles the box surrounding the legend
    self._lstyle = lstyle # Styles the legend labels

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
      self._style = toyplot.style.combine({"font-size":"12px", "font-weight":"bold", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle", "baseline-shift":"-200%"}, toyplot.require.style(style))
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
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))

  class PerTickHelper(object):
    class TickProxy(object):
      def __init__(self, tick):
        self._tick = tick
      @property
      def style(self):
        return self._tick.get("style", {})
      @style.setter
      def style(self, value):
        self._tick["style"] = toyplot.style.combine(self._tick.get("style"), toyplot.require.style(value))
    def __init__(self):
      self._indices = collections.defaultdict(dict)
      self._values = collections.defaultdict(dict)
    def __call__(self, index=None, value=None, style=None):
      if index is None and value is None:
        raise ValueError("Must specify tick index or value.")
      if index is not None and value is not None:
        raise ValueError("Must specify either index or value, not both.")
      if index is not None:
        return VColorBar.PerTickHelper.TickProxy(self._indices[index])
      if value is not None:
        return VColorBar.PerTickHelper.TickProxy(self._values[value])
    def styles(self, values):
      results = [self._indices[index].get("style", None) if index in self._indices else None for index in range(len(values))]
      for value in self._values:
        deltas = numpy.abs(values - value)
        results[numpy.argmin(deltas)] = self._values[value].get("style", None)
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
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))

  class TickLabelsHelper(object):
    def __init__(self):
      self._show = True
      self._style = {"font-size":"10px", "font-weight":"normal", "stroke":"none"}
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
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))

  def __init__(self, xmin_range, xmax_range, ymin_range, ymax_range, label, colormap, padding, tick_length, min, max, tick_locator, style):
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
    self._vmin_implicit = vmin if self._vmin_implicit is None else self._vmin_implicit if vmin is None else min(vmin, self._vmin_implicit)
    self._vmax_implicit = vmax if self._vmax_implicit is None else self._vmax_implicit if vmin is None else max(vmax, self._vmax_implicit)

  def _finalize_domain(self):
    # Begin with the implicit domain defined by any explicitly-specified data.
    vmin = self._vmin_implicit
    vmax = self._vmax_implicit

    # If there is no implicit domain (we don't have any data), default to the origin.
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

    self._tick_locations, self._tick_labels, self._tick_titles = locator.ticks(vmin, vmax)

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
      self._projection = linear_projection(vmin, vmax, self._ymin_range + self._padding, self._ymax_range - self._padding)

  def _project_y(self, v):
    return self._projection(v)

  def _project_color(self, v):
    return self._colormap.colors(v, self._vmin_computed, self._vmax_computed)

