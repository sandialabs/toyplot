# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import itertools
import numbers
import numpy
import toyplot.broadcast
import toyplot.color
import toyplot.data
import toyplot.format
import toyplot.layout
import toyplot.locator
import toyplot.mark
import toyplot.require

###############################################################################################
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

def _signed_log(x, base):
  """Return the log of a number, retaining its sign (e.g. return -3 for log-base-10 of -1000)."""
  return numpy.sign(x) * numpy.log10(numpy.abs(x)) / numpy.log10(base)

def _symmetric_log(x, base, threshold=1):
  if isinstance(x, numpy.ndarray):
    masked = numpy.ma.masked_inside(x, -threshold, threshold, copy=False)
    return numpy.where(masked.mask, x, numpy.sign(x) * (threshold + (numpy.ma.log10(numpy.abs(masked)) / numpy.log10(base))))
  if numpy.abs(x) < threshold:
    return x
  return numpy.sign(x) * (threshold + numpy.log10(numpy.abs(x)))

###############################################################################################
# Cartesian

class Cartesian(object):
  """Standard two-dimensional Cartesian coordinate system.

  Do not create Cartesian instances directly.  Use factory methods such
  as :meth:`toyplot.canvas.Canvas.axes` instead.
  """
  class AxisHelper(object):
    def __init__(self, show, label, label_style, min, max, tick_length, tick_locator, tick_angle, scale):
      self.spine = Cartesian.SpineHelper()
      self.ticks = Cartesian.TicksHelper(tick_length, tick_locator, tick_angle)
      self.label = Cartesian.LabelHelper(label, label_style)
      self.domain = Cartesian.DomainHelper(min, max)
      self._show = show
      self.scale = scale
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
      raise ValueError("""Scale must be "linear", "log", "log10", "log2" or a ("log", base) tuple.""")

  class CoordinatesHelper(object):
    def __init__(self, show, xmin_range, xmax_range, ymin_range, ymax_range, style):
      self._show = show
      self._xmin_range = xmin_range
      self._xmax_range = xmax_range
      self._ymin_range = ymin_range
      self._ymax_range = ymax_range
      self._style = toyplot.style.combine({"stroke":"none", "fill":"white", "opacity":0.75}, toyplot.require.style(style))
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
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))

  class CoordinatesLabelHelper(object):
    def __init__(self, style):
      self._style = toyplot.style.combine({"font-size":"10px", "font-weight":"normal", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle"}, toyplot.require.style(style))
    @property
    def style(self):
      return self._style
    @style.setter
    def style(self, value):
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))

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
      self._style = toyplot.style.combine({"font-weight":"bold", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle"}, toyplot.require.style(style))
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
    def __call__(self, index=None, value=None):
      if index is None and value is None:
        raise ValueError("Must specify tick index or value.")
      if index is not None and value is not None:
        raise ValueError("Must specify either index or value, not both.")
      if index is not None:
        return Cartesian.PerTickHelper.TickProxy(self._indices[index])
      elif value is not None:
        return Cartesian.PerTickHelper.TickProxy(self._values[value])
    def styles(self, values):
      results = [self._indices[index].get("style", None) if index in self._indices else None for index in range(len(values))]
      for value in self._values:
        deltas = numpy.abs(values - value)
        results[numpy.argmin(deltas)] = self._values[value].get("style", None)
      return results

  class TicksHelper(object):
    def __init__(self, length, locator, angle):
      self._locator = locator
      self._show = False
      self._length = length
      self._style = {}
      self.labels = Cartesian.TickLabelsHelper(angle)
      self.tick = Cartesian.PerTickHelper()
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
    def __init__(self, angle):
      self._show = True
      self._angle = angle
      self._style = {"font-size":"10px", "font-weight":"normal", "stroke":"none"}
      self.label = Cartesian.PerTickHelper()
    @property
    def show(self):
      return self._show
    @show.setter
    def show(self, value):
      self._show = value
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
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))

  def __init__(self, xmin_range, xmax_range, ymin_range, ymax_range, xmin, xmax, ymin, ymax, show, xshow, yshow, label, xlabel, ylabel, xticklocator, yticklocator, xscale, yscale, palette, padding, tick_length, parent):
    self._xmin_range = xmin_range
    self._xmax_range = xmax_range
    self._ymin_range = ymin_range
    self._ymax_range = ymax_range
    self._xmin_implicit = None
    self._xmax_implicit = None
    self._ymin_implicit = None
    self._ymax_implicit = None
    self._padding = padding

    if palette is None:
      palette = toyplot.color.Palette()
    self._palette = palette
    self._bar_colors = itertools.cycle(palette)
    self._fill_colors = itertools.cycle(palette)
    self._plot_colors = itertools.cycle(palette)
    self._scatterplot_colors = itertools.cycle(palette)
    self._rect_colors = itertools.cycle(palette)
    self._text_colors = itertools.cycle(palette)

    self._show = show
    self.coordinates = Cartesian.CoordinatesHelper(show=True, xmin_range=xmax_range - 100, xmax_range=xmax_range - 10, ymin_range = ymin_range + 10, ymax_range = ymin_range + 24, style={})
    self.label = Cartesian.LabelHelper(label=label, style={"font-size":"14px", "baseline-shift":"100%"})
    self.x = Cartesian.AxisHelper(show=xshow, label=xlabel, label_style={"baseline-shift":"-200%"}, min=xmin, max=xmax, tick_length=tick_length, tick_locator=xticklocator, tick_angle=0, scale=xscale)
    self.y = Cartesian.AxisHelper(show=yshow, label=ylabel, label_style={"baseline-shift":"200%"}, min=ymin, max=ymax, tick_length=tick_length, tick_locator=yticklocator, tick_angle=-90, scale=yscale)

    self._parent = parent
    self._children = []

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
    self._padding = value

  def _update_domain(self, x, y):
    x = _flat_non_null(x)
    y = _flat_non_null(y)

    if len(x):
      self._xmin_implicit = _null_min(x.min(), self._xmin_implicit)
      self._xmax_implicit = _null_max(x.max(), self._xmax_implicit)

    if len(y):
      self._ymin_implicit = _null_min(y.min(), self._ymin_implicit)
      self._ymax_implicit = _null_max(y.max(), self._ymax_implicit)

  def _finalize_domain(self):
    # Begin with the implicit domain defined by our children.
    xmin = self._xmin_implicit
    xmax = self._xmax_implicit
    ymin = self._ymin_implicit
    ymax = self._ymax_implicit

    # If there is no implicit domain (we don't have any children), default to the origin.
    if xmin is None:
      xmin = 0
    if xmax is None:
      xmax = 0
    if ymin is None:
      ymin = 0
    if ymax is None:
      ymax = 0

    # Allow users to override the domain.
    if self.x.domain._min is not None:
      xmin = self.x.domain._min
    if self.x.domain._max is not None:
      xmax = self.x.domain._max
    if self.y.domain._min is not None:
      ymin = self.y.domain._min
    if self.y.domain._max is not None:
      ymax = self.y.domain._max

    # Ensure that the domain is never empty.
    if xmin == xmax:
      xmin -= 0.5
      xmax += 0.5

    if ymin == ymax:
      ymin -= 0.5
      ymax += 0.5

    def _get_locator(locator, scale, domain_min, domain_max):
      if locator is not None:
        return locator
      if scale == "linear":
        return toyplot.locator.Extended()
      else:
        scale, base = scale
        if scale == "log":
          if domain_max < 0:
            return toyplot.locator.NegativeLog(base=base)
          elif 0 < domain_min:
            return toyplot.locator.PositiveLog(base=base)
          return toyplot.locator.SymmetricLog(base=base)

    # Calculate tick locations and labels.
    xlocator = _get_locator(self.x.ticks._locator, self.x._scale, xmin, xmax)
    ylocator = _get_locator(self.y.ticks._locator, self.y._scale, ymin, ymax)

    self._xtick_locations, self._xtick_labels, self._xtick_titles = xlocator.ticks(xmin, xmax)
    self._ytick_locations, self._ytick_labels, self._ytick_titles = ylocator.ticks(ymin, ymax)

    # Allow tick locations to grow (never shrink) the domain.
    if len(self._xtick_locations):
      xmin = min(xmin, self._xtick_locations[0])
      xmax = max(xmax, self._xtick_locations[-1])
    if len(self._ytick_locations):
      ymin = min(ymin, self._ytick_locations[0])
      ymax = max(ymax, self._ytick_locations[-1])

    self._xmin_computed = xmin
    self._xmax_computed = xmax
    self._ymin_computed = ymin
    self._ymax_computed = ymax

    def x_linear_projection(domain_min, domain_max, range_min, range_max):
      def implementation(x):
        return (x - domain_min) / (domain_max - domain_min) * (range_max - range_min) + range_min
      return implementation

    def x_log_projection(domain_min, domain_max, range_min, range_max, base):
      def implementation(x):
        return (_signed_log(x, base) - _signed_log(domain_min, base)) / (_signed_log(domain_max, base) - _signed_log(domain_min, base)) * (range_max - range_min) + range_min
      return implementation

    def x_symlog_projection(domain_min, domain_max, range_min, range_max, base):
      def implementation(x):
        return (_symmetric_log(x, base) - _symmetric_log(domain_min, base)) / (_symmetric_log(domain_max, base) - _symmetric_log(domain_min, base)) * (range_max - range_min) + range_min
      return implementation

    def y_linear_projection(domain_min, domain_max, range_min, range_max):
      def implementation(x):
        return (1 - ((x - domain_min) / (domain_max - domain_min))) * (range_max - range_min) + range_min
      return implementation

    def y_log_projection(domain_min, domain_max, range_min, range_max, base):
      def implementation(x):
        return (1 - ((_signed_log(x, base) - _signed_log(domain_min, base)) / (_signed_log(domain_max, base) - _signed_log(domain_min, base)))) * (range_max - range_min) + range_min
      return implementation

    def y_symlog_projection(domain_min, domain_max, range_min, range_max, base):
      def implementation(x):
        return (1 - ((_symmetric_log(x, base) - _symmetric_log(domain_min, base)) / (_symmetric_log(domain_max, base) - _symmetric_log(domain_min, base)))) * (range_max - range_min) + range_min
      return implementation

    if self.x._scale == "linear":
      self._xprojection = x_linear_projection(xmin, xmax, self._xmin_range + self._padding, self._xmax_range - self._padding)
    else:
      scale, base = self.x._scale
      if scale == "log":
        if xmax < 0 or 0 < xmin:
          self._xprojection = x_log_projection(xmin, xmax, self._xmin_range + self._padding, self._xmax_range - self._padding, base)
        else:
          self._xprojection = x_symlog_projection(xmin, xmax, self._xmin_range + self._padding, self._xmax_range - self._padding, base)

    if self.y._scale == "linear":
      self._yprojection = y_linear_projection(ymin, ymax, self._ymin_range + self._padding, self._ymax_range - self._padding)
    else:
      scale, base = self.y._scale
      if scale == "log":
        if ymax < 0 or 0 < ymin:
          self._yprojection = y_log_projection(ymin, ymax, self._ymin_range + self._padding, self._ymax_range - self._padding, base)
        else:
          self._yprojection = y_symlog_projection(ymin, ymax, self._ymin_range + self._padding, self._ymax_range - self._padding, base)

  def _project_x(self, x):
    return self._xprojection(x)

  def _project_y(self, y):
    return self._yprojection(y)

  def bars(self, a, b=None, c=None, along="x", baseline="stacked", fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None):
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
    fill: array-like set of colors, optional
      Specify a single color for all bars, one color per series, or one color per bar.
      Color values can be explicit toyplot colors, or scalar values to be mapped
      to colors using the `colormap` or `palette` parameter.
    colormap: :class:`toyplot.color.Map`, optional
      Colormap to be used for mapping scalar `fill` values to colors.  If
      unspecified, a default :class:`toyplot.color.LinearMap` is used.
    palette: :class:`toyplot.color.Palette`, optional
      Palette to be used for mapping scalar `fill` values to colors.  If
      unspecified, a default :class:`toyplot.color.Palette` is used.
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
          series = numpy.ma.column_stack((numpy.repeat(0, len(c)), c))
        elif c.ndim == 2:
          series = toyplot.require.scalar_matrix(c)
        position = numpy.ma.column_stack((a, b))
      elif a is not None and b is not None:
        a = toyplot.require.scalar_vector(a)
        b = toyplot.require.scalar_array(b)
        if b.ndim == 1:
          b = toyplot.require.scalar_vector(b, len(a))
          series = numpy.ma.column_stack((numpy.repeat(0, len(b)), b))
        elif b.ndim == 2:
          series = toyplot.require.scalar_matrix(b)
        position = numpy.concatenate((a[0:1] - (a[1:2] - a[0:1]) * 0.5, (a[:-1] + a[1:]) * 0.5, a[-1:] + (a[-1:] - a[-2:-1]) * 0.5))
        position = numpy.ma.column_stack((position[:-1], position[1:]))
      else:
        a = toyplot.require.scalar_array(a)
        if a.ndim == 1:
          a = toyplot.require.scalar_vector(a)
          series = numpy.ma.column_stack((numpy.repeat(0, len(a)), a))
        elif a.ndim == 2:
          series = toyplot.require.scalar_matrix(a)
        position = numpy.ma.column_stack((numpy.arange(series.shape[0]) - 0.5, numpy.arange(series.shape[0]) + 0.5))

      default_color = [next(self._bar_colors) for i in range(series.shape[1]-1)]
      fill = toyplot.color.broadcast(default_color if fill is None else fill, (series.shape[0], series.shape[1]-1), colormap=colormap, palette=palette)
      opacity = toyplot.broadcast.scalar(opacity, (series.shape[0], series.shape[1]-1))
      title = toyplot.broadcast.object(title, (series.shape[0], series.shape[1]-1))
      style = toyplot.style.combine({"stroke":"white", "stroke-width":1.0}, toyplot.require.style(style))

      if along == "x":
        self._update_domain(position, series)
      elif along == "y":
        self._update_domain(series, position)

      left_right_axis = along
      boundary_axis = "y" if along == "x" else "x"

      table = toyplot.data.Table()
      table["left"] = position.T[0]
      table["right"] = position.T[1]
      boundary_keys = []
      fill_keys = []
      opacity_keys = []
      title_keys = []

      boundary_keys.append(boundary_axis + "0")
      table[boundary_keys[-1]] = series.T[0]

      for index, (boundary_column, fill_column, opacity_column, title_column) in enumerate(zip(series.T[1:], fill.T, opacity.T, title.T)):
        boundary_keys.append("boundary" + str(index+1))
        fill_keys.append("fill" + str(index))
        opacity_keys.append("opacity" + str(index))
        title_keys.append("title" + str(index))
        table[boundary_keys[-1]] = boundary_column
        table[fill_keys[-1]] = fill_column
        table[opacity_keys[-1]] = opacity_column
        table[title_keys[-1]] = title_column

      self._children.append(toyplot.mark.BarBoundaries(table=table, left="left", right="right", left_right_axis=left_right_axis, boundaries=boundary_keys, boundary_axis=boundary_axis, fill=fill_keys, opacity=opacity_keys, title=title_keys, style=style))
      return self._children[-1]
    else: # baseline is not None
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
        position = numpy.concatenate((a[0:1] - (a[1:2] - a[0:1]) * 0.5, (a[:-1] + a[1:]) * 0.5, a[-1:] + (a[-1:] - a[-2:-1]) * 0.5))
        position = numpy.ma.column_stack((position[:-1], position[1:]))
      elif a is not None:
        if isinstance(a, tuple) and len(a) == 2:
          counts, edges = a
          position = numpy.ma.column_stack((edges[:-1], edges[1:]))
          series = numpy.ma.column_stack((toyplot.require.scalar_vector(counts, len(position)),))
        else:
          a = toyplot.require.scalar_array(a)
          if a.ndim == 1:
            series = numpy.ma.column_stack((a,))
          elif a.ndim == 2:
            series = a
          position = numpy.ma.column_stack((numpy.arange(series.shape[0]) - 0.5, numpy.arange(series.shape[0]) + 0.5))

      default_color = [next(self._bar_colors) for i in range(series.shape[1])]
      fill = toyplot.color.broadcast(default_color if fill is None else fill, series.shape, colormap=colormap, palette=palette)
      opacity = toyplot.broadcast.scalar(opacity, series.shape)
      title = toyplot.broadcast.object(title, series.shape)
      style = toyplot.style.combine({"stroke":"white", "stroke-width":1.0}, toyplot.require.style(style))

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

      boundaries = numpy.cumsum(numpy.column_stack((baseline, series)), axis=1)
      if along == "x":
        self._update_domain(position, boundaries)
      elif along == "y":
        self._update_domain(boundaries, position)

      left_right_axis = along
      magnitude_axis = "y" if along == "x" else "x"

      table = toyplot.data.Table()
      table["left"] = position.T[0]
      table["right"] = position.T[1]
      table["baseline"] = baseline
      magnitude_keys = []
      fill_keys = []
      opacity_keys = []
      title_keys = []
      for index, (magnitude_column, fill_column, opacity_column, title_column) in enumerate(zip(series.T, fill.T, opacity.T, title.T)):
        magnitude_keys.append("magnitude" + str(index))
        fill_keys.append("fill" + str(index))
        opacity_keys.append("opacity" + str(index))
        title_keys.append("title" + str(index))
        table[magnitude_keys[-1]] = magnitude_column
        table[fill_keys[-1]] = fill_column
        table[opacity_keys[-1]] = opacity_column
        table[title_keys[-1]] = title_column

      self._children.append(toyplot.mark.BarMagnitudes(table=table, left="left", right="right", left_right_axis=left_right_axis, baseline="baseline", magnitudes=magnitude_keys, magnitude_axis=magnitude_axis, fill=fill_keys, opacity=opacity_keys, title=title_keys, style=style))
      return self._children[-1]

  def colorbar(self, values=None, palette=None, colormap=None, label=None, min=None, max=None, tick_length=5, tick_locator=None, offset=0, width=10, style=None):
    if colormap is None:
      if palette is None:
        palette = toyplot.color.brewer("BlueGreen")
      colormap = toyplot.color.LinearMap(palette=palette)
    style = toyplot.require.style(style)

    mark = toyplot.mark.VColorBar(xmin_range=self._xmax_range + offset, xmax_range=self._xmax_range + offset + width, ymin_range=self._ymin_range, ymax_range=self._ymax_range, label=label, colormap=colormap, padding=self._padding, tick_length=tick_length, min=min, max=max, tick_locator=tick_locator, style=style)
    if values is not None:
      mark._update_domain(numpy.min(values), numpy.max(values))
    self._parent._children.append(mark)
    return mark

  def fill(self, a, b=None, c=None, along="x", baseline=None, fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None):
    """Fill multiple regions separated by curves.

    Parameters
    ----------
    a, b, c: array-like sets of coordinates
      If `a`, `b`, and `c` are provided, they specify the X coordinates, bottom
      coordinates, and top coordinates of the region respectively.  If only `a`
      and `b` are provided, they specify the top coordinates and bottom
      coordinates, with the X coordinates ranging from [0, N).  If only `a` is
      provided, it specifies the top of the region, with the bottom along the
      origin and the X coordinates ranging from [0, N).
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
        b = toyplot.require.scalar_vector(b, len(position))
        c = toyplot.require.scalar_vector(c, len(position))
        series = numpy.ma.column_stack((b, c))
      elif a is not None and b is not None:
        a = toyplot.require.scalar_vector(a)
        b = toyplot.require.scalar_array(b)
        if b.ndim == 1:
          b = toyplot.require.scalar_vector(b, len(a))
          series = numpy.ma.column_stack((a, b))
          position = numpy.ma.array(numpy.arange(series.shape[0]))
        elif b.ndim == 2:
          series = toyplot.require.scalar_matrix(b)
          position = toyplot.require.scalar_vector(a, series.shape[0]);
      else:
        a = toyplot.require.scalar_array(a)
        if a.ndim == 1:
          a = toyplot.require.scalar_vector(a)
          b = numpy.ma.repeat(0, len(a))
          series = numpy.ma.column_stack((b, a))
          position = numpy.ma.arange(series.shape[0])
        elif a.ndim == 2:
          series = toyplot.require.scalar_matrix(a)
          position = numpy.ma.arange(series.shape[0])

      default_color = [next(self._fill_colors) for i in range(series.shape[1]-1)]
      fill = toyplot.color.broadcast(default_color if fill is None else fill, series.shape[1]-1, colormap=colormap, palette=palette)
      opacity = toyplot.broadcast.scalar(opacity, series.shape[1]-1)
      title = toyplot.broadcast.object(title, series.shape[1]-1)
      style = toyplot.style.combine({"stroke":"none"}, toyplot.require.style(style))

      if along == "x":
        self._update_domain(position, series)
      elif along == "y":
        self._update_domain(series, position)

      position_axis = along
      boundary_axis = "y" if along == "x" else "x"

      table = toyplot.data.Table()
      table[position_axis] = position
      boundaries = []
      for index, column in enumerate(series.T):
        key = boundary_axis + str(index)
        table[key] = column
        boundaries.append(key)

      self._children.append(toyplot.mark.FillBoundaries(table=table, position=position_axis, position_axis=position_axis, boundaries=boundaries, boundary_axis=boundary_axis, fill=fill, opacity=opacity, title=title, style=style))
      return self._children[-1]
    else: # baseline is not None
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

      default_color = [next(self._fill_colors) for i in range(series.shape[1])]
      fill = toyplot.color.broadcast(default_color if fill is None else fill, series.shape[1], colormap=colormap, palette=palette)
      opacity = toyplot.broadcast.scalar(opacity, series.shape[1])
      title = toyplot.broadcast.object(title, series.shape[1])
      style = toyplot.style.combine({"stroke":"none"}, toyplot.require.style(style))

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

      boundaries = numpy.ma.cumsum(numpy.ma.column_stack((baseline, series)), axis=1)
      if along == "x":
        self._update_domain(position, boundaries)
      elif along == "y":
        self._update_domain(boundaries, position)

      position_axis = along
      magnitude_axis = "y" if along == "x" else "x"

      table = toyplot.data.Table()
      table[position_axis] = position
      table["baseline"] = baseline
      magnitudes = []
      for index, column in enumerate(series.T):
        key = magnitude_axis + str(index)
        table[key] = column
        magnitudes.append(key)

      self._children.append(toyplot.mark.FillMagnitudes(table=table, position=position_axis, position_axis=position_axis, baseline="baseline", magnitudes=magnitudes, magnitude_axis=magnitude_axis, fill=fill, opacity=opacity, title=title, style=style))
      return self._children[-1]

  def plot(self, a, b=None, along="x", stroke=None, stroke_colormap=None, stroke_palette=None, stroke_width=2.0, stroke_opacity=1.0, marker=None, size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style=None, mstyle=None, mlstyle=None):
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
      :class:`toyplot.mark.Plot` for a list of useful styles.

    Returns
    -------
    plot: :class:`toyplot.mark.Plot`
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
    stroke = toyplot.color.broadcast(default_color if stroke is None else stroke, series.shape[1], colormap=stroke_colormap, palette=stroke_palette)
    stroke_width = toyplot.broadcast.scalar(stroke_width, series.shape[1])
    stroke_opacity = toyplot.broadcast.scalar(stroke_opacity, series.shape[1])
    marker = toyplot.broadcast.object(marker, series.shape)
    size = toyplot.broadcast.scalar(size, series.shape)
    fill = toyplot.color.broadcast(default_color if fill is None else fill, series.shape, colormap=fill_colormap, palette=fill_palette)
    opacity = toyplot.broadcast.scalar(opacity, series.shape)
    title = toyplot.broadcast.object(title, series.shape[1])
    style = toyplot.style.combine({"fill":"none"}, toyplot.require.style(style))
    mstyle = toyplot.style.combine({"stroke":"none"}, toyplot.require.style(mstyle))
    mlstyle = toyplot.style.combine(toyplot.require.style(mlstyle))

    if along == "x":
      self._update_domain(position, series)
    elif along == "y":
      self._update_domain(series, position)

    coordinate_axes = along
    series_axis = "y" if along == "x" else "x"

    table = toyplot.data.Table()
    table[coordinate_axes] = position
    series_keys = []
    marker_keys = []
    size_keys = []
    fill_keys = []
    opacity_keys = []
    for index, (series_column, marker_column, size_column, fill_column, opacity_column) in enumerate(zip(series.T, marker.T, size.T, fill.T, opacity.T)):
      series_keys.append(series_axis + str(index))
      marker_keys.append("marker" + str(index))
      size_keys.append("size" + str(index))
      fill_keys.append("fill" + str(index))
      opacity_keys.append("opacity" + str(index))
      table[series_keys[-1]] = series_column
      table[marker_keys[-1]] = marker_column
      table[size_keys[-1]] = size_column
      table[fill_keys[-1]] = fill_column
      table[opacity_keys[-1]] = opacity_column

    self._children.append(toyplot.mark.Plot(table=table, coordinates=coordinate_axes, coordinate_axes=coordinate_axes, series=series_keys, series_axis=series_axis, show_stroke=True, stroke=stroke, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker_keys, size=size_keys, fill=fill_keys, opacity=opacity_keys, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle))
    return self._children[-1]

  def scatterplot(self, a, b=None, along="x", stroke=None, stroke_colormap=None, stroke_palette=None, stroke_width=2.0, stroke_opacity=1.0, marker="o", size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style=None, mstyle=None, mlstyle=None):
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

    default_color = [next(self._scatterplot_colors) for i in range(series.shape[1])]
    stroke = toyplot.color.broadcast(default_color if stroke is None else stroke, series.shape[1], colormap=stroke_colormap, palette=stroke_palette)
    stroke_width = toyplot.broadcast.scalar(stroke_width, series.shape[1])
    stroke_opacity = toyplot.broadcast.scalar(stroke_opacity, series.shape[1])
    marker = toyplot.broadcast.object(marker, series.shape)
    size = toyplot.broadcast.scalar(size, series.shape)
    fill = toyplot.color.broadcast(default_color if fill is None else fill, series.shape, colormap=fill_colormap, palette=fill_palette)
    opacity = toyplot.broadcast.scalar(opacity, series.shape)
    title = toyplot.broadcast.object(title, series.shape[1])
    style = toyplot.style.combine({"stroke":"none"}, toyplot.require.style(style))
    mstyle = toyplot.style.combine({"stroke":"none"}, toyplot.require.style(mstyle))
    mlstyle = toyplot.style.combine(toyplot.require.style(mlstyle))

    if along == "x":
      self._update_domain(position, series)
    elif along == "y":
      self._update_domain(series, position)

    coordinate_axes = along
    series_axis = "y" if along == "x" else "x"

    table = toyplot.data.Table()
    table[coordinate_axes] = position
    series_keys = []
    marker_keys = []
    size_keys = []
    fill_keys = []
    opacity_keys = []
    for index, (series_column, marker_column, size_column, fill_column, opacity_column) in enumerate(zip(series.T, marker.T, size.T, fill.T, opacity.T)):
      series_keys.append(series_axis + str(index))
      marker_keys.append("marker" + str(index))
      size_keys.append("size" + str(index))
      fill_keys.append("fill" + str(index))
      opacity_keys.append("opacity" + str(index))
      table[series_keys[-1]] = series_column
      table[marker_keys[-1]] = marker_column
      table[size_keys[-1]] = size_column
      table[fill_keys[-1]] = fill_column
      table[opacity_keys[-1]] = opacity_column

    self._children.append(toyplot.mark.Plot(table=table, coordinates=coordinate_axes, coordinate_axes=coordinate_axes, series=series_keys, series_axis=series_axis, show_stroke=False, stroke=stroke, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker_keys, size=size_keys, fill=fill_keys, opacity=opacity_keys, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle))
    return self._children[-1]

  def rect(self, a, b, c, d, along="x", fill=None, colormap=None, palette=None, opacity=1.0, title=None, style={"stroke":"none"}):
    table = toyplot.data.Table()
    table["left"] = toyplot.require.scalar_vector(a)
    table["right"] = toyplot.require.scalar_vector(b, length=table.shape[0])
    table["top"] = toyplot.require.scalar_vector(c, length=table.shape[0])
    table["bottom"] = toyplot.require.scalar_vector(d, length=table.shape[0])
    table["fill"] = toyplot.broadcast.object(fill, table.shape[0])
    table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
    table["title"] = toyplot.broadcast.object(title, table.shape[0])
    style = toyplot.style.combine(toyplot.require.style(style))

    default_color = next(self._rect_colors)
    table["toyplot:fill"] = toyplot.color.broadcast(default_color if fill is None else fill, table.shape[0], colormap=colormap, palette=palette)

    if along == "x":
      left_right_axis = "x"
      top_bottom_axis = "y"
      self._update_domain(numpy.concatenate((table["left"], table["right"])), numpy.concatenate((table["top"], table["bottom"])))
    elif along == "y":
      left_right_axis = "y"
      top_bottom_axis = "x"
      self._update_domain(numpy.concatenate((table["top"], table["bottom"])), numpy.concatenate((table["left"], table["right"])))

    self._children.append(toyplot.mark.Rect(table=table, left="left", right="right", left_right_axis=left_right_axis, top="top", bottom="bottom", top_bottom_axis=top_bottom_axis, fill="toyplot:fill", opacity="opacity", title="title", style=style))
    return self._children[-1]

  def text(self, a, b, text, angle=0, fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None):
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

    Returns
    -------
    text: :class:`toyplot.mark.Text`
    """
    table = toyplot.data.Table()
    table["x"] = toyplot.require.scalar_vector(a)
    table["y"] = toyplot.require.scalar_vector(b, table.shape[0])
    table["text"] = toyplot.broadcast.object(text, table.shape[0])
    table["angle"] = toyplot.broadcast.scalar(angle, table.shape[0])
    table["fill"] = toyplot.broadcast.object(fill, table.shape[0])
    table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
    table["title"] = toyplot.broadcast.object(title, table.shape[0])
    style = toyplot.style.combine({"font-weight":"normal", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle"}, toyplot.require.style(style))

    default_color = next(self._text_colors)
    table["toyplot:fill"] = toyplot.color.broadcast(default_color if fill is None else fill, table.shape[0], colormap=colormap, palette=palette)

    self._update_domain(table["x"], table["y"])

    self._children.append(toyplot.mark.Text(table=table, coordinates=["x", "y"], axes=["x", "y"], text="text", angle="angle", fill="toyplot:fill", opacity="opacity", title="title", style=style))
    return self._children[-1]

  def hlines(self, y, stroke=None, colormap=None, palette=None, opacity=1.0, title=None, style=None):
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

    Returns
    -------
    hlines: :class:`toyplot.mark.AxisLines`
    """
    table = toyplot.data.Table()
    table["y"] = toyplot.require.scalar_vector(y)
    table["stroke"] = toyplot.broadcast.object(stroke, table.shape[0])
    table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
    table["title"] = toyplot.broadcast.object(title, table.shape[0])
    style = toyplot.style.combine(toyplot.require.style(style))

    table["toyplot:stroke"] = toyplot.color.broadcast(toyplot.color.near_black if stroke is None else stroke, table.shape[0], colormap=colormap, palette=palette)

    self._update_domain(numpy.array([]), table["y"])
    self._children.append(toyplot.mark.AxisLines(table=table, coordinates=["y"], axes=["y"], stroke="toyplot:stroke", opacity="opacity", title="title", style=style))
    return self._children[-1]

  def vlines(self, x, stroke=None, colormap=None, palette=None, opacity=1.0, title=None, style=None):
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

    Returns
    -------
    hlines: :class:`toyplot.mark.AxisLines`
    """
    table = toyplot.data.Table()
    table["x"] = toyplot.require.scalar_vector(x)
    table["stroke"] = toyplot.broadcast.object(stroke, table.shape[0])
    table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
    table["title"] = toyplot.broadcast.object(title, table.shape[0])
    style = toyplot.style.combine(toyplot.require.style(style))

    table["toyplot:stroke"] = toyplot.color.broadcast(toyplot.color.near_black if stroke is None else stroke, table.shape[0], colormap=colormap, palette=palette)

    self._update_domain(table["x"], numpy.array([]))
    self._children.append(toyplot.mark.AxisLines(table=table, coordinates=["x"], axes=["x"], stroke="toyplot:stroke", opacity="opacity", title="title", style=style))
    return self._children[-1]

  def legend(self, marks, bounds=None, rect=None, corner=None, grid=None, gutter=50, style=None, label_style=None):
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

    xmin, xmax, ymin, ymax = toyplot.layout.region(self._xmin_range, self._xmax_range, self._ymin_range, self._ymax_range, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
    self._children.append(toyplot.mark.Legend(xmin, xmax, ymin, ymax, marks, style, label_style))
    return self._children[-1]

##########################################################################
# Table

class Table(object):
  """Experimental table coordinate system.
  """
  class HeaderCell(object):
    def __init__(self):
      self._content = None
      self._style = None
    @property
    def content(self):
      return self._content
    @content.setter
    def content(self, value):
      self._content = value
    @property
    def style(self):
      return self._style
    @style.setter
    def style(self, value):
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))

  class Column(object):
    def __init__(self, data):
      self._header = toyplot.axes.Table.HeaderCell()

      self._data = data
      self._width = None
      self._justify = "center"
      self._format = toyplot.format.DefaultFormatter()
      self._offset = 0
      self._style = None
    @property
    def header(self):
      return self._header
    @property
    def width(self):
      return self._width
    @width.setter
    def width(self, value):
      self._width = value
    @property
    def justify(self):
      return self._justify
    @justify.setter
    def justify(self, value):
      self._justify = value
    @property
    def format(self):
      return self._format
    @format.setter
    def format(self, value):
      self._format = value
    @property
    def offset(self):
      return self._offset
    @offset.setter
    def offset(self, value):
      self._offset = value
    @property
    def style(self):
      return self._style
    @style.setter
    def style(self, value):
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))
    @property
    def formatted(self):
      return self._format.format(self._data)

  class Row(object):
    def __init__(self):
      self._style = None
    @property
    def style(self):
      return self._style
    @style.setter
    def style(self, value):
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))

  class Cell(object):
    def __init__(self):
      self._content = None
      self._style = None
    @property
    def style(self):
      return self._style
    @style.setter
    def style(self, value):
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))

  class CellReference(object):
    def __init__(self, row, column, rowspan, colspan, parent):
      self._row = row
      self._column = column
      self._rowspan = rowspan
      self._colspan = colspan
      self._parent = parent

    def _set_content(self, value):
      for row in range(self._row, self._row + self._rowspan):
        for column in range(self._column, self._column + self._colspan):
          self._parent._cells[row, column]._content = value
    content = property(fset=_set_content)

    def _set_style(self, value):
      for row in range(self._row, self._row + self._rowspan):
        for column in range(self._column, self._column + self._colspan):
          self._parent._cells[row, column].style = value
    style = property(fset=_set_style)

    def axes(self, xmin=None, xmax=None, ymin=None, ymax=None, show=False, xshow=True, yshow=True, label=None, xlabel=None, ylabel=None, xticklocator=None, yticklocator=None, xscale="linear", yscale="linear", palette=None, padding=5, tick_length=5):
      x_boundaries, y_boundaries = self._parent._boundaries()
      axes = toyplot.axes.Cartesian(x_boundaries[self._column], x_boundaries[self._column+self._colspan], y_boundaries[self._row + 1], y_boundaries[self._row+1+self._rowspan], xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, show=show, xshow=xshow, yshow=yshow, label=label, xlabel=xlabel, ylabel=ylabel, xticklocator=xticklocator, yticklocator=yticklocator, xscale=xscale, yscale=yscale, palette=palette, padding=padding, tick_length=tick_length, parent=self._parent)
      axes.coordinates.show = False
      self._parent._children.append(axes)
      return axes

  class Grid(object):
    def __init__(self, rows, columns):
      self._hlines = numpy.empty((rows + 2, columns), dtype=object)
      self._vlines = numpy.empty((rows + 1, columns + 1), dtype=object)
      self._separation = 2
      self._style = {"stroke":toyplot.color.near_black, "stroke-width":0.5}
    @property
    def hlines(self):
      return self._hlines
    @property
    def vlines(self):
      return self._vlines
    @property
    def separation(self):
      return self._separation
    @separation.setter
    def separation(self, value):
      self._separation = value
    @property
    def style(self):
      return self._style
    @style.setter
    def style(self, value):
      self._style = toyplot.style.combine(self._style, toyplot.require.style(value))

  def __init__(self, xmin_range, xmax_range, ymin_range, ymax_range, data, parent):
    self._xmin_range = xmin_range
    self._xmax_range = xmax_range
    self._ymin_range = ymin_range
    self._ymax_range = ymax_range
    self._parent = parent
    self._children = []
    self._style = {"font-size":"12px", "stroke":"none", "fill":toyplot.color.near_black, "alignment-baseline":"middle"}
    self._hstyle = {"font-size":"12px", "stroke":"none", "fill":toyplot.color.near_black, "alignment-baseline":"middle", "font-weight":"bold"}

    self._keys = data.keys()
    self._columns = numpy.array([toyplot.axes.Table.Column(data=column) for column in data.values()])
    self._rows = numpy.array([toyplot.axes.Table.Row() for row in range(data.shape[0])])
    self._cells = numpy.array([[toyplot.axes.Table.Cell() for column in range(data.shape[1])] for row in range(data.shape[0])])
    self._grid = toyplot.axes.Table.Grid(data.shape[0], data.shape[1])

    self._grid.hlines[1,...] = "single"

    for column in self._columns:
      if issubclass(column._data.dtype.type, numpy.floating):
        column.format = toyplot.format.FloatFormatter()
        column.justify = "separator"
      elif issubclass(column._data.dtype.type, numpy.character):
        column.justify = "left"
      elif issubclass(column._data.dtype.type, numpy.integer):
        column.justify = "right"

  def _boundaries(self):
    column_widths = numpy.zeros(len(self._columns))
    for index, column in enumerate(self._columns):
      if column.width is not None:
        column_widths[index] = column.width

    table_width = self._xmax_range - self._xmin_range
    available_width = table_width - numpy.sum(column_widths[column_widths != 0])
    default_width = available_width / numpy.count_nonzero(column_widths == 0)
    column_widths[column_widths == 0] = default_width

    x_boundaries = self._xmin_range + numpy.concatenate(([0], numpy.cumsum(column_widths)))
    y_boundaries = numpy.linspace(self._ymin_range, self._ymax_range, len(self._rows) + 2, endpoint=True)
    return x_boundaries, y_boundaries

  @property
  def grid(self):
    return self._grid

  def row(self, index):
    return self._rows[index]

  def column(self, key):
    if isinstance(key, numbers.Integral):
      return self._columns[key]
    return self._columns[self._keys.index(key)]

  def cell(self, row, column, rowspan=1, colspan=1):
    return toyplot.axes.Table.CellReference(row, column, rowspan, colspan, self)
