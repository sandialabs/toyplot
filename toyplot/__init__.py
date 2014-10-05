# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import itertools
import numbers
import numpy.ma
import toyplot.color.css
import toyplot.compatibility
import toyplot.data
import toyplot.locator
import toyplot.mark
import toyplot.require
import toyplot.units

__version__ = "0.3"

###############################################################################################
# Style Helpers

def combine_styles(*styles):
  """Combine zero-to-many styles, returning a dict."""
  computed_style = {}
  for style in styles:
    if style is not None:
      computed_style.update(style)
  return computed_style

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

def _broadcast_scalar(value, shape):
  array = numpy.array(value).astype("float64")
  # As a special-case, allow a vector with shape M to be matched-up with an M x 1 matrix.
  if array.ndim == 1 and isinstance(shape, tuple) and len(shape) == 2 and array.shape[0] == shape[0] and shape[1] == 1:
    return numpy.reshape(array, shape)
  return numpy.broadcast_arrays(array, numpy.empty(shape))[0]

def _broadcast_string(value, shape):
  array = numpy.array(value).astype("str")
  # As a special-case, allow a vector with shape M to be matched-up with an M x 1 matrix.
  if array.ndim == 1 and isinstance(shape, tuple) and len(shape) == 2 and array.shape[0] == shape[0] and shape[1] == 1:
    return numpy.reshape(array, shape)
  return numpy.broadcast_arrays(array, numpy.empty(shape))[0]

def _broadcast_object(value, shape):
  array = numpy.array(value)
  # As a special-case, allow a vector with shape M to be matched-up with an M x 1 matrix.
  if array.ndim == 1 and isinstance(shape, tuple) and len(shape) == 2 and array.shape[0] == shape[0] and shape[1] == 1:
    return numpy.reshape(array, shape)
  return numpy.broadcast_arrays(array, numpy.empty(shape))[0]

def _region(xmin, xmax, ymin, ymax, bounds=None, rect=None, corner=None, grid=None, gutter=40):
  def length(min, max, value):
    if isinstance(value, numbers.Number):
      return value
    if isinstance(value, toyplot.compatibility.string_type):
      value = value.strip()
      if value[-1] == "%":
        value = float(value[:-1]) * 0.01
        return ((1.0 - value) * min) + (value * max)
      else:
        return float(value)

  # Specify explicit bounds for the region
  if bounds is not None:
    if isinstance(bounds, tuple) and len(bounds) == 4:
      return (length(xmin, xmax, bounds[0]), length(xmin, xmax, bounds[1]), length(ymin, ymax, bounds[2]), length(ymin, ymax, bounds[3]))
    raise ValueError("Unrecognized bounds type")
  # Specify an explicit rectangle for the region
  if rect is not None:
    if isinstance(rect, tuple) and len(rect) == 4:
      x = length(xmin, xmax, rect[0])
      y = length(ymin, ymax, rect[1])
      width = length(xmin, xmax, rect[2])
      height = length(ymin, ymax, rect[3])
      return (x, x + width, y, y + height)
    raise ValueError("Unrecognized rect type")
  # Offset a rectangle from a corner
  if corner is not None:
    if isinstance(corner, tuple) and len(corner) == 4:
      position = corner[0]
      width = length(xmin, xmax, corner[1])
      height = length(ymin, ymax, corner[2])
      inset = float(corner[3])
    else:
      raise ValueError("Unrecognized corner type")
    if position == "top":
      return ((xmin + xmax - width) / 2, (xmin + xmax + width) / 2, ymin + inset, ymin + inset + height)
    elif position == "top-right":
      return (xmax - width - inset, xmax - inset, ymin + inset, ymin + inset + height)
    elif position == "right":
      return (xmax - width - inset, xmax - inset, (ymin + ymax - height) / 2, (ymin + ymax + height) / 2)
    elif position == "bottom-right":
      return (xmax - width - inset, xmax - inset, ymax - inset - height, ymax - inset)
    elif position == "bottom":
      return ((xmin + xmax - width) / 2, (xmin + xmax + width) / 2, ymax - inset - height, ymax - inset)
    elif position == "bottom-left":
      return (xmin + inset, xmin + inset + width, ymax - inset - height, ymax - inset)
    elif position == "left":
      return (xmin + inset, xmin + inset + width, (ymin + ymax - height) / 2, (ymin + ymax + height) / 2)
    elif position == "top-left":
      return (xmin + inset, xmin + inset + width, ymin + inset, ymin + inset + height)
    else:
      raise ValueError("Unrecognized corner")
  # Choose a cell from an MxN grid, with optional column/row spanning.
  if grid is not None:
    if len(grid) == 3: # Cell n (in left-to-right, top-to-bottom order) of an M x N grid
      M, N, n = grid
      i = n // N
      j = n % N
      rowspan, colspan = (1, 1)
    elif len(grid) == 4: # Cell i,j of an M x N grid
      M, N, i, j = grid
      rowspan, colspan = (1, 1)
    elif len(grid) == 6: # Cells [i, i+rowspan), [j, j+colspan) of an M x N grid
      M, N, i, rowspan, j, colspan = grid

    cell_width = (xmax - xmin) / N
    cell_height = (ymax - ymin) / M

    return (
      (j * cell_width) + gutter,
      ((j + colspan) * cell_width) - gutter,
      (i * cell_height) + gutter,
      ((i + rowspan) * cell_height) - gutter,
      )
  # If nothing else fits, consume the entire region
  return (xmin + gutter, xmax - gutter, ymin + gutter, ymax - gutter)

###############################################################################################
# Axes (projections)

class Axes2D(object):
  """Standard two-dimensional Cartesian coordinate system.

  Do not create Axes2D instances directly.  Use factory methods such
  as :meth:`toyplot.canvas.Canvas.axes` instead.
  """
  class AxisHelper(object):
    def __init__(self, show, label, label_style, min, max, tick_length, tick_locator, tick_angle, scale):
      self.spine = Axes2D.SpineHelper()
      self.ticks = Axes2D.TicksHelper(tick_length, tick_locator, tick_angle)
      self.label = Axes2D.LabelHelper(label, label_style)
      self.domain = Axes2D.DomainHelper(min, max)
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
      self._style = combine_styles({"stroke":"none", "fill":"white", "opacity":0.75}, toyplot.require.style(style))
      self.label = Axes2D.CoordinatesLabelHelper(style={})
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
      self._style = combine_styles(self._style, toyplot.require.style(value))

  class CoordinatesLabelHelper(object):
    def __init__(self, style):
      self._style = combine_styles({"font-size":"10px", "font-weight":"normal", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle"}, toyplot.require.style(style))
    @property
    def style(self):
      return self._style
    @style.setter
    def style(self, value):
      self._style = combine_styles(self._style, toyplot.require.style(value))

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
      self._style = combine_styles({"font-weight":"bold", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle"}, toyplot.require.style(style))
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
      self._style = combine_styles(self._style, toyplot.require.style(value))

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
      self._style = combine_styles(self._style, toyplot.require.style(value))

  class PerTickHelper(object):
    class TickProxy(object):
      def __init__(self, tick):
        self._tick = tick
      @property
      def style(self):
        return self._tick.get("style", {})
      @style.setter
      def style(self, value):
        self._tick["style"] = combine_styles(self._tick.get("style"), toyplot.require.style(value))
    def __init__(self):
      self._indices = collections.defaultdict(dict)
      self._values = collections.defaultdict(dict)
    def __call__(self, index=None, value=None):
      if index is None and value is None:
        raise ValueError("Must specify tick index or value.")
      if index is not None and value is not None:
        raise ValueError("Must specify either index or value, not both.")
      if index is not None:
        return Axes2D.PerTickHelper.TickProxy(self._indices[index])
      elif value is not None:
        return Axes2D.PerTickHelper.TickProxy(self._values[value])
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
      self.labels = Axes2D.TickLabelsHelper(angle)
      self.tick = Axes2D.PerTickHelper()
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
      self._style = combine_styles(self._style, toyplot.require.style(value))

  class TickLabelsHelper(object):
    def __init__(self, angle):
      self._show = True
      self._angle = angle
      self._style = {"font-size":"10px", "font-weight":"normal", "stroke":"none"}
      self.label = Axes2D.PerTickHelper()
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
      self._style = combine_styles(self._style, toyplot.require.style(value))

  def __init__(self, xmin_range, xmax_range, ymin_range, ymax_range, xmin, xmax, ymin, ymax, show, xshow, yshow, label, xlabel, ylabel, xticklocator, yticklocator, xscale, yscale, palette, padding, tick_length, parent, id):
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
    self.coordinates = Axes2D.CoordinatesHelper(show=True, xmin_range=xmax_range - 100, xmax_range=xmax_range - 10, ymin_range = ymin_range + 10, ymax_range = ymin_range + 24, style={})
    self.label = Axes2D.LabelHelper(label=label, style={"font-size":"14px", "baseline-shift":"100%"})
    self.x = Axes2D.AxisHelper(show=xshow, label=xlabel, label_style={"baseline-shift":"-200%"}, min=xmin, max=xmax, tick_length=tick_length, tick_locator=xticklocator, tick_angle=0, scale=xscale)
    self.y = Axes2D.AxisHelper(show=yshow, label=ylabel, label_style={"baseline-shift":"200%"}, min=ymin, max=ymax, tick_length=tick_length, tick_locator=yticklocator, tick_angle=-90, scale=yscale)

    self._parent = parent
    self._id = id

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

  def bars(self, a, b=None, c=None, along="x", baseline="stacked", fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None, id=None):
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
    id: string, optional

    Returns
    -------
    bars: :class:`toyplot.mark.BarBoundaries` or :class:`toyplot.mark.BarMagnitudes`
    """

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
      fill = toyplot.color._broadcast_color(default_color if fill is None else fill, (series.shape[0], series.shape[1]-1), colormap=colormap, palette=palette)
      opacity = _broadcast_scalar(opacity, (series.shape[0], series.shape[1]-1))
      title = _broadcast_object(title, (series.shape[0], series.shape[1]-1))
      style = combine_styles({"stroke":"white", "stroke-width":1.0}, toyplot.require.style(style))
      id = toyplot.require.optional_id(id)

      if along == "x":
        self._update_domain(position, series)
      elif along == "y":
        self._update_domain(series, position)

      self._children.append(toyplot.mark.BarBoundaries(along=along, position=position, series=series, fill=fill, opacity=opacity, title=title, style=style, id=id))
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
      fill = toyplot.color._broadcast_color(default_color if fill is None else fill, series.shape, colormap=colormap, palette=palette)
      opacity = _broadcast_scalar(opacity, series.shape)
      title = _broadcast_object(title, series.shape)
      style = combine_styles({"stroke":"white", "stroke-width":1.0}, toyplot.require.style(style))
      id = toyplot.require.optional_id(id)

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

      self._children.append(toyplot.mark.BarMagnitudes(along=along, position=position, baseline=baseline, series=series, fill=fill, opacity=opacity, title=title, style=style, id=id))
      return self._children[-1]

  def colorbar(self, values=None, palette=None, colormap=None, label=None, min=None, max=None, id=None, tick_length=5, tick_locator=None, offset=0, width=10, style=None):
    if colormap is None:
      if palette is None:
        palette = toyplot.color.brewer("BlueGreen")
      colormap = toyplot.color.LinearMap(palette=palette)
    style = toyplot.require.style(style)

    mark = toyplot.mark.VColorBar(xmin_range=self._xmax_range + offset, xmax_range=self._xmax_range + offset + width, ymin_range=self._ymin_range, ymax_range=self._ymax_range, label=label, colormap=colormap, padding=self._padding, tick_length=tick_length, min=min, max=max, tick_locator=tick_locator, style=style, id=id)
    if values is not None:
      mark._update_domain(numpy.min(values), numpy.max(values))
    self._parent._children.append(mark)
    return mark

  def fill(self, a, b=None, c=None, along="x", baseline=None, fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None, id=None):
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
    id: string, optional

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
      fill = toyplot.color._broadcast_color(default_color if fill is None else fill, series.shape[1]-1, colormap=colormap, palette=palette)
      opacity = _broadcast_scalar(opacity, series.shape[1]-1)
      title = _broadcast_object(title, series.shape[1]-1)
      style = combine_styles({"stroke":"none"}, toyplot.require.style(style))
      id = toyplot.require.optional_id(id)

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

      self._children.append(toyplot.mark.FillBoundaries(table=table, position=position_axis, position_axis=position_axis, boundaries=boundaries, boundary_axis=boundary_axis, fill=fill, opacity=opacity, title=title, style=style, id=id))
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
      fill = toyplot.color._broadcast_color(default_color if fill is None else fill, series.shape[1], colormap=colormap, palette=palette)
      opacity = _broadcast_scalar(opacity, series.shape[1])
      title = _broadcast_object(title, series.shape[1])
      style = combine_styles({"stroke":"none"}, toyplot.require.style(style))
      id = toyplot.require.optional_id(id)

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

      self._children.append(toyplot.mark.FillMagnitudes(table=table, position=position_axis, position_axis=position_axis, baseline="baseline", magnitudes=magnitudes, magnitude_axis=magnitude_axis, fill=fill, opacity=opacity, title=title, style=style, id=id))
      return self._children[-1]

  def plot(self, a, b=None, along="x", stroke=None, stroke_colormap=None, stroke_palette=None, stroke_width=2.0, stroke_opacity=1.0, marker=None, size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style=None, mstyle=None, mlstyle=None, id=None):
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
    id: string, optional

    Returns
    -------
    plot: :class:`toyplot.mark.Plot`
    """
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
    stroke = toyplot.color._broadcast_color(default_color if stroke is None else stroke, series.shape[1], colormap=stroke_colormap, palette=stroke_palette)
    stroke_width = _broadcast_scalar(stroke_width, series.shape[1])
    stroke_opacity = _broadcast_scalar(stroke_opacity, series.shape[1])
    marker = _broadcast_object(marker, series.shape)
    size = _broadcast_scalar(size, series.shape)
    fill = toyplot.color._broadcast_color(default_color if fill is None else fill, series.shape, colormap=fill_colormap, palette=fill_palette)
    opacity = _broadcast_scalar(opacity, series.shape)
    title = _broadcast_object(title, series.shape[1])
    style = combine_styles({"fill":"none"}, toyplot.require.style(style))
    mstyle = combine_styles({"stroke":"none"}, toyplot.require.style(mstyle))
    mlstyle = combine_styles(toyplot.require.style(mlstyle))
    id = toyplot.require.optional_id(id)

    if along == "x":
      self._update_domain(position, series)
    elif along == "y":
      self._update_domain(series, position)

    self._children.append(toyplot.mark.Plot(along=along, show_stroke=True, position=position, series=series, stroke=stroke, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker, size=size, fill=fill, opacity=opacity, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle, id=id))
    return self._children[-1]

  def scatterplot(self, a, b=None, along="x", stroke=None, stroke_colormap=None, stroke_palette=None, stroke_width=2.0, stroke_opacity=1.0, marker="o", size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style=None, mstyle=None, mlstyle=None, id=None):
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
    id: string, optional

    Returns
    -------
    plot: :class:`toyplot.mark.Plot`
    """
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
    stroke = toyplot.color._broadcast_color(default_color if stroke is None else stroke, series.shape[1], colormap=stroke_colormap, palette=stroke_palette)
    stroke_width = _broadcast_scalar(stroke_width, series.shape[1])
    stroke_opacity = _broadcast_scalar(stroke_opacity, series.shape[1])
    marker = _broadcast_object(marker, series.shape)
    size = _broadcast_scalar(size, series.shape)
    fill = toyplot.color._broadcast_color(default_color if fill is None else fill, series.shape, colormap=fill_colormap, palette=fill_palette)
    opacity = _broadcast_scalar(opacity, series.shape)
    title = _broadcast_object(title, series.shape[1])
    style = combine_styles({"stroke":"none"}, toyplot.require.style(style))
    mstyle = combine_styles({"stroke":"none"}, toyplot.require.style(mstyle))
    mlstyle = combine_styles(toyplot.require.style(mlstyle))
    id = toyplot.require.optional_id(id)

    if along == "x":
      self._update_domain(position, series)
    elif along == "y":
      self._update_domain(series, position)

    self._children.append(toyplot.mark.Plot(along=along, show_stroke=False, position=position, series=series, stroke=stroke, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker, size=size, fill=fill, opacity=opacity, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle, id=id))
    return self._children[-1]

  def rect(self, a, b, c, d, along="x", fill=None, colormap=None, palette=None, opacity=1.0, title=None, style={"stroke":"none"}, id=None):
    table = toyplot.data.Table()
    table["left"] = toyplot.require.scalar_vector(a)
    table["right"] = toyplot.require.scalar_vector(b, length=table.shape[0])
    table["top"] = toyplot.require.scalar_vector(c, length=table.shape[0])
    table["bottom"] = toyplot.require.scalar_vector(d, length=table.shape[0])
    table["fill"] = _broadcast_object(fill, table.shape[0])
    table["opacity"] = _broadcast_scalar(opacity, table.shape[0])
    table["title"] = _broadcast_object(title, table.shape[0])
    style = combine_styles(toyplot.require.style(style))
    id = toyplot.require.optional_id(id)

    default_color = next(self._rect_colors)
    table["toyplot:fill"] = toyplot.color._broadcast_color(default_color if fill is None else fill, table.shape[0], colormap=colormap, palette=palette)

    if along == "x":
      left_right_axis = "x"
      top_bottom_axis = "y"
      self._update_domain(numpy.concatenate((table["left"], table["right"])), numpy.concatenate((table["top"], table["bottom"])))
    elif along == "y":
      left_right_axis = "y"
      top_bottom_axis = "x"
      self._update_domain(numpy.concatenate((table["top"], table["bottom"])), numpy.concatenate((table["left"], table["right"])))

    self._children.append(toyplot.mark.Rect(table=table, left="left", right="right", left_right_axis=left_right_axis, top="top", bottom="bottom", top_bottom_axis=top_bottom_axis, fill="toyplot:fill", opacity="opacity", title="title", style=style, id=id))
    return self._children[-1]

  def text(self, a, b, text, angle=0, fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None, id=None):
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
    table["text"] = _broadcast_object(text, table.shape[0])
    table["angle"] = _broadcast_scalar(angle, table.shape[0])
    table["fill"] = _broadcast_object(fill, table.shape[0])
    table["opacity"] = _broadcast_scalar(opacity, table.shape[0])
    table["title"] = _broadcast_object(title, table.shape[0])
    style = combine_styles({"font-weight":"normal", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle"}, toyplot.require.style(style))
    id = toyplot.require.optional_id(id)

    default_color = next(self._text_colors)
    table["toyplot:fill"] = toyplot.color._broadcast_color(default_color if fill is None else fill, table.shape[0], colormap=colormap, palette=palette)

    self._update_domain(table["x"], table["y"])

    self._children.append(toyplot.mark.Text(table=table, coordinates=["x", "y"], axes=["x", "y"], text="text", angle="angle", fill="toyplot:fill", opacity="opacity", title="title", style=style, id=id))
    return self._children[-1]

  def hlines(self, y, stroke=None, colormap=None, palette=None, opacity=1.0, title=None, style=None, id=None):
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
    id: string, optional

    Returns
    -------
    hlines: :class:`toyplot.mark.AxisLines`
    """
    table = toyplot.data.Table()
    table["y"] = toyplot.require.scalar_vector(y)
    table["stroke"] = _broadcast_object(stroke, table.shape[0])
    table["opacity"] = _broadcast_scalar(opacity, table.shape[0])
    table["title"] = _broadcast_object(title, table.shape[0])
    style = combine_styles(toyplot.require.style(style))
    id = toyplot.require.optional_id(id)

    table["toyplot:stroke"] = toyplot.color._broadcast_color(toyplot.color.near_black if stroke is None else stroke, table.shape[0], colormap=colormap, palette=palette)

    self._update_domain(numpy.array([]), table["y"])
    self._children.append(toyplot.mark.AxisLines(table=table, coordinates=["y"], axes=["y"], stroke="toyplot:stroke", opacity="opacity", title="title", style=style, id=id))
    return self._children[-1]

  def vlines(self, x, stroke=None, colormap=None, palette=None, opacity=1.0, title=None, style=None, id=None):
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
    id: string, optional

    Returns
    -------
    hlines: :class:`toyplot.mark.AxisLines`
    """
    table = toyplot.data.Table()
    table["x"] = toyplot.require.scalar_vector(x)
    table["stroke"] = _broadcast_object(stroke, table.shape[0])
    table["opacity"] = _broadcast_scalar(opacity, table.shape[0])
    table["title"] = _broadcast_object(title, table.shape[0])
    style = combine_styles(toyplot.require.style(style))
    id = toyplot.require.optional_id(id)

    table["toyplot:stroke"] = toyplot.color._broadcast_color(toyplot.color.near_black if stroke is None else stroke, table.shape[0], colormap=colormap, palette=palette)

    self._update_domain(table["x"], numpy.array([]))
    self._children.append(toyplot.mark.AxisLines(table=table, coordinates=["x"], axes=["x"], stroke="toyplot:stroke", opacity="opacity", title="title", style=style, id=id))
    return self._children[-1]

  def legend(self, marks, bounds=None, rect=None, corner=None, grid=None, gutter=50, style=None, label_style=None, id=None):
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
    id: string, optional

    Returns
    -------
    legend: :class:`toyplot.mark.Legend`
    """
    gutter = toyplot.require.scalar(gutter)
    style = combine_styles(toyplot.require.style(style))
    label_style = combine_styles(toyplot.require.style(label_style))
    id = toyplot.require.optional_id(id)

    xmin, xmax, ymin, ymax = _region(self._xmin_range, self._xmax_range, self._ymin_range, self._ymax_range, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
    self._children.append(toyplot.mark.Legend(xmin, xmax, ymin, ymax, marks, style, label_style, id))
    return self._children[-1]

from toyplot.canvas import Canvas

def bars(a, b=None, c=None, along="x", baseline="stacked", fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None, id=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style=None):
  """Convenience function for creating a bar plot in a single call.

  See :meth:`toyplot.Axes2D.bars`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.Axes2D`
    A new set of 2D axes that fill the canvas.
  mark: :class:`toyplot.mark.BarMagnitudes` or :class:`toyplot.mark.BarBoundaries`
    The new bar mark.
  """
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.bars(a=a, b=b, c=c, along=along, baseline=baseline, fill=fill, colormap=colormap, palette=palette, opacity=opacity, title=title, style=style, id=id)
  return canvas, axes, mark

def fill(a, b=None, c=None, along="x", baseline=None, fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None, id=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style=None):
  """Convenience function for creating a fill plot in a single call.

  See :meth:`toyplot.Axes2D.fill`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.Axes2D`
    A new set of 2D axes that fill the canvas.
  mark: :class:`toyplot.mark.FillBoundaries` or :class:`toyplot.mark.FillMagnitudes`
    The new bar mark.
  """
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.fill(a=a, b=b, c=c, along=along, baseline=baseline, fill=fill, colormap=colormap, palette=palette, opacity=opacity, title=title, style=style, id=id)
  return canvas, axes, mark

def plot(a, b=None, along="x", stroke=None, stroke_colormap=None, stroke_palette=None, stroke_width=2.0, stroke_opacity=1.0, marker=None, size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style=None, mstyle=None, mlstyle=None, id=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style=None):
  """Convenience function for creating a line plot in a single call.

  See :meth:`toyplot.Axes2D.plot`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.Axes2D`
    A new set of 2D axes that fill the canvas.
  mark: :class:`toyplot.mark.Plot`
    The new plot mark.
  """
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.plot(a=a, b=b, along=along, stroke=stroke, stroke_colormap=stroke_colormap, stroke_palette=stroke_palette, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker, size=size, fill=fill, fill_colormap=fill_colormap, fill_palette=fill_palette, opacity=opacity, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle, id=id)
  return canvas, axes, mark

def scatterplot(a, b=None, along="x", stroke=None, stroke_colormap=None, stroke_palette=None, stroke_width=2.0, stroke_opacity=1.0, marker="o", size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style=None, mstyle=None, mlstyle=None, id=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style=None):
  """Convenience function for creating a scatter plot in a single call.

  See :meth:`toyplot.Axes2D.scatterplot`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.Axes2D`
    A new set of 2D axes that fill the canvas.
  mark: :class:`toyplot.mark.Plot`
    The new scatter plot mark.
  """
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.scatterplot(a=a, b=b, along=along, stroke=stroke, stroke_colormap=stroke_colormap, stroke_palette=stroke_palette, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker, size=size, fill=fill, fill_colormap=fill_colormap, fill_palette=fill_palette, opacity=opacity, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle, id=id)
  return canvas, axes, mark

