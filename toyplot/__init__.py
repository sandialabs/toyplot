# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import itertools
import numbers
import numpy.ma
import toyplot.color.css
import toyplot.units

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

def _require_instance(value, types):
  if not isinstance(value, types):
    raise ValueError("Expected %s, received %s." % (types, type(value)))

def _require_scalar(value):
  if not isinstance(value, numbers.Number):
    raise ValueError("Expected a number, received %s." % value)
  return value

def _require_scalar_array(value):
  array = numpy.ma.array(value).astype("float64")
  array.mask = numpy.ma.mask_or(array.mask, ~numpy.isfinite(array))
  return array

def _require_scalar_vector(value, length=None):
  array = _require_scalar_array(value)
  if array.shape == ():
    array = numpy.ma.repeat(array, 1 if length is None else length)
  if array.ndim != 1:
    raise ValueError("Expected a vector.")
  if length is not None:
    if len(array) != length:
      raise ValueError("Expected %s values, received %s." % (length, len(array)))
  return array

def _require_scalar_matrix(value, rows=None, columns=None):
  array = _require_scalar_array(value)
  if array.ndim != 2:
    raise ValueError("Expected a matrix.")
  if rows is not None:
    if array.shape[0] != rows:
      raise ValueError("Expected %s rows, received %s." % (rows, array.shape[0]))
  if columns is not None:
    if array.shape[1] != columns:
      raise ValueError("Expected %s columns, received %s." % (columns, array.shape[1]))
  return array

def _require_string(value):
  if not isinstance(value, basestring):
    raise ValueError("Expected a string, received %s." % value)
  return value

def _require_optional_string(value):
  if not isinstance(value, (basestring, type(None))):
    raise ValueError("Expected a string value or None, received %s." % value)
  return value

def _require_marker_array(value, length=None):
  if isinstance(value, (basestring, tuple)):
    array = [value] * (1 if length is None else length)
  else:
    array = value
  if length is not None:
    if len(array) != length:
      raise ValueError("Expected %s values, received %s." % (length, len(array)))
  return array

def _require_style(style):
  if not isinstance(style, dict):
    raise ValueError("Expected a dictionary of CSS styles, received %s." % style)
  return style

def _require_optional_id(id):
  return _require_optional_string(id)

def _broadcast_scalar(value, shape):
  array = numpy.array(value).astype("float64")
  # As a special-case, allow a vector with shape M to be matched-up with an M x 1 matrix.
  if array.ndim == 1 and isinstance(shape, tuple) and len(shape) == 2 and array.shape[0] == shape[0] and shape[1] == 1:
    return numpy.reshape(array, shape)
  return numpy.broadcast_arrays(array, numpy.empty(shape))[0]

def _broadcast_string(value, shape):
  array = numpy.array(value).astype("string")
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
    if isinstance(value, basestring):
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
# Basic Toyplot marks

class Mark(object):
  def __init__(self, *styles, **kwargs):
    self._style = {}
    for style in styles:
      self._style.update(style)
    self._id = kwargs.get("id", None)

class LegendMark(Mark):
  """Render a figure legend (a collection of markers and labels).

  Do not create LegendMark instances directly.  Use factory methods such as
  :meth:`toyplot.Canvas.legend` or :meth:`toyplot.Axes2D.legend` instead.
  """
  def __init__(self, xmin, xmax, ymin, ymax, marks, style, label_style, id):
    Mark.__init__(self, {"fill":"none", "stroke":"none"}, style, id=id)
    self._xmin = xmin
    self._xmax = xmax
    self._ymin = ymin
    self._ymax = ymax
    self._gutter = 10
    self._marks = marks
    self._label_style = label_style

class VColorBarMark(Mark):
  """Displays a one-dimensional mapping from values to colors.

  Do not create VColorbarMark instances directly.  Use factory methods such
  as :meth:`toyplot.Axes2D.colorbar` instead.
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
      self._style = {"font-size":"12px", "font-weight":"bold", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle", "baseline-shift":"-200%"}
      self._style.update(style)
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
      self._style.update(value)

  class PerTickHelper(object):
    class TickProxy(object):
      def __init__(self, tick):
        self._tick = tick
      @property
      def style(self):
        return self._tick.get("style", {})
      @style.setter
      def style(self, value):
        style = self._tick.get("style", {})
        style.update(value)
        self._tick["style"] = style
    def __init__(self):
      self._indices = collections.defaultdict(dict)
      self._values = collections.defaultdict(dict)
    def __call__(self, index=None, value=None, style=None):
      if index is None and value is None:
        raise ValueError("Must specify tick index or value.")
      if index is not None and value is not None:
        raise ValueError("Must specify either index or value, not both.")
      if index is not None:
        return VColorBarMark.PerTickHelper.TickProxy(self._indices[index])
      if value is not None:
        return VColorBarMark.PerTickHelper.TickProxy(self._values[value])
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
      self.labels = VColorBarMark.TickLabelsHelper()
      self.tick = VColorBarMark.PerTickHelper()
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
      self._style.update(value)

  class TickLabelsHelper(object):
    def __init__(self):
      self._show = True
      self._style = {"font-size":"10px", "font-weight":"normal", "stroke":"none"}
      self.label = VColorBarMark.PerTickHelper()
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
      self._style.update(value)

  def __init__(self, xmin_range, xmax_range, ymin_range, ymax_range, label, colormap, padding, tick_length, min, max, tick_locator, style, id):
    Mark.__init__(self, style)

    self._xmin_range = xmin_range
    self._xmax_range = xmax_range
    self._ymin_range = ymin_range
    self._ymax_range = ymax_range
    self._scale = "linear"
    self._colormap = colormap
    self._vmin_implicit = None
    self._vmax_implicit = None
    self._padding = padding
    self.domain = VColorBarMark.DomainHelper(min, max)
    self.label = VColorBarMark.LabelHelper(label=label)
    self.ticks = VColorBarMark.TicksHelper(tick_length, tick_locator)
    self._id = id

  def _update_domain(self, vmin, vmax):
    self._vmin_implicit = _null_min(vmin, self._vmin_implicit)
    self._vmax_implicit = _null_max(vmax, self._vmax_implicit)

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
        return ExtendedTickLocator()

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

###############################################################################################
# Table

class Table(object):
  def __init__(self, xmin_range, xmax_range, ymin_range, ymax_range, rows, columns, id):
    self._xmin_range = xmin_range
    self._xmax_range = xmax_range
    self._ymin_range = ymin_range
    self._ymax_range = ymax_range
    self._rows = rows
    self._columns = columns
    self._id = id

###############################################################################################
# Higher-level marks

class AxisLinesMark(Mark):
  """Render multiple lines parallel to an axis.

  Do not create AxisLinesMark instances directly.  Use factory methods such as
  :meth:`toyplot.Axes2D.hlines` and :meth:`toyplot.Axes2D.vlines` instead.
  """
  def __init__(self, along, position, stroke, opacity, title, style, id):
    Mark.__init__(self, style, id=id)
    self._along = along
    self._position = position # M coordinates
    self._stroke = stroke     # M stroke colors
    self._opacity = opacity   # M opacities
    self._title = title       # M titles

class BarBoundariesMark(Mark):
  """Render multiple stacked bars defined by bar boundaries.

  Do not create BarBoundariesMark instances directly.  Use factory methods such as
  :meth:`toyplot.Axes2D.bars` instead.
  """
  def __init__(self, along, position, series, fill, opacity, title, style, id):
    Mark.__init__(self, {"stroke":"none"}, style, id=id)
    self._along = along
    self._position = position # M x 2 coordinates
    self._series = series     # M x N bar boundaries
    self._fill = fill         # M x N-1 fill colors
    self._opacity = opacity   # M x N-1 opacities
    self._title = title       # M x N-1 titles

class BarMagnitudesMark(Mark):
  """Render multiple stacked bars defined by bar magnitudes.

  Do not create BarMagnitudesMark instances directly.  Use factory methods such as
  :meth:`toyplot.Axes2D.bars` instead.
  """
  def __init__(self, along, position, baseline, series, fill, opacity, title, style, id):
    Mark.__init__(self, {"stroke":"none"}, style, id=id)
    self._along = along
    self._position = position # M x 2 coordinates
    self._baseline = baseline # M baseline coordinates
    self._series = series     # M x N bar magnitudes
    self._fill = fill         # M x N fill colors
    self._opacity = opacity   # M x N opacities
    self._title = title       # M x N titles

class FillBoundariesMark(Mark):
  """Render multiple stacked fill regions defined by boundaries.

  Do not create FillBoundariesMark instances directly.  Use factory methods such
  as :meth:`toyplot.Axes2D.fill` instead.
  """
  def __init__(self, along, position, series, fill, opacity, title, style, id):
    Mark.__init__(self, style, id=id)
    self._along = along
    self._position = position # M coordinates
    self._series = series     # M x N fill boundaries
    self._fill = fill         # N-1 fill colors
    self._opacity = opacity   # N-1 opacities
    self._title = title       # N-1 titles

class FillMagnitudesMark(Mark):
  """Render multiple stacked fill regions defined by magnitudes.

  Do not create FillMagnitudesMark instances directly.  Use factory methods such
  as :meth:`toyplot.Axes2D.fill` instead.
  """
  def __init__(self, along, position, baseline, series, fill, opacity, title, style, id):
    Mark.__init__(self, style, id=id)
    self._along = along
    self._position = position # M coordinates
    self._baseline = baseline # M baseline coordinates
    self._series = series     # M x N fill magnitudes
    self._fill = fill         # N fill colors
    self._opacity = opacity   # N opacities
    self._title = title       # N titles

class PlotMark(Mark):
  """Plot multiple bivariate data series using lines and/or markers.

  Do not create PlotMark instances directly.  Use factory methods such as
  :meth:`toyplot.Axes2D.plot` and :meth:`toyplot.Axes2D.scatterplot` instead.
  """
  def __init__(self, along, show_stroke, position, series, stroke, stroke_width, stroke_opacity, marker, size, fill, opacity, title, style, mstyle, mlstyle, id):
    _require_instance(position, numpy.ma.MaskedArray)
    _require_instance(series, numpy.ma.MaskedArray)

    Mark.__init__(self, style, id=id)
    self._along = along
    self._show_stroke = show_stroke
    self._position = position             # M coordinates
    self._series = series                 # M x N coordinates
    self._stroke = stroke                 # N stroke colors
    self._stroke_width = stroke_width     # N stroke widths
    self._stroke_opacity = stroke_opacity # N stroke opacities
    self._marker = marker                 # M x N markers
    self._size = size                     # M x N marker sizes
    self._fill = fill                     # M x N marker fill colors
    self._opacity = opacity               # M x N marker opacities
    self._title = title                   # N titles
    self._mstyle = mstyle
    self._mlstyle = mlstyle

class RectMark(Mark):
  """Plot axis-aligned rectangles.

  Do not create RectMark instances directly.  Use factory methods such as
  :meth:`toyplot.Axes2D.rect` instead.
  """
  def __init__(self, along, series, fill, opacity, title, style, id):
    Mark.__init__(self, style, id=id)
    self._along = along
    self._series = series   # M x 4 boundaries
    self._fill = fill       # M fill colors
    self._opacity = opacity # M opacities
    self._title = title     # M titles

class TextMark(Mark):
  """Render text.

  Do not create TextMark instances directly.  Use factory methods such as
  :meth:`toyplot.Canvas.text` or :meth:`toyplot.Axes2D.text` instead.
  """
  def __init__(self, along, series, text, angle, fill, opacity, title, style, id):
    Mark.__init__(self, style, id=id)
    self._along = along
    self._series = series   # M x 2 coordinates
    self._text = text       # M strings
    self._angle = angle     # M angles
    self._fill = fill       # M fill colors
    self._opacity = opacity # M opacities
    self._title = title     # M titles

###############################################################################################
# Tick Locators

class ExplicitTickLocator(object):
  """Explicitly specify a collection of tick locations and labels for an axis.

  You must specify the set of locations, the set of labels, or both.  If you
  only specify locations, the labels will be generated using a formatting
  string.  If you only specify labels, the locations will default to integers
  in the range $[0, n)$.  The latter behavior is especially useful for
  categorical axes.

  Parameters
  ----------
  locations : sequence of tick locations (numbers), optional
  labels : sequence of tick labels (strings), optional
  titles : sequence of tick titles (strings), optional
  format : format string used to generate labels from tick locations, optional
  """
  def __init__(self, locations=None, labels=None, titles=None, format="{:g}"):
    if locations is not None and labels is not None:
      locations = numpy.array(locations).astype("float64")
      labels = _broadcast_string(labels, len(locations))
    elif locations is not None:
      locations = numpy.array(locations).astype("float64")
      labels = [format.format(location) for location in locations]
    elif labels is not None:
      labels = numpy.array(labels).astype("string")
      locations = numpy.arange(len(labels))
    else:
      raise ValueError("Must supply locations, labels, or both.")
    titles = _broadcast_object(titles, len(locations))

    self._locations = locations
    self._labels = labels
    self._titles = titles

  def ticks(self, domain_min, domain_max):
    return self._locations, self._labels, self._titles

class BasicTickLocator(object):
  """Generate N evenly spaced ticks that include the minimum and maximum values of a domain.

  Parameters
  ----------
  count : number of ticks to generate, optional
  format : format string used to generate labels from tick locations, optional
  """
  def __init__(self, count=5, format="{:g}"):
    self._count = count
    self._format = format
  def ticks(self, domain_min, domain_max):
    locations = numpy.linspace(domain_min, domain_max, self._count, endpoint=True)
    labels = [self._format.format(location) for location in locations]
    titles = numpy.repeat(None, len(labels))
    return locations, labels, titles

class PositiveLogTickLocator(object):
  """Generate ticks that are evenly spaced on a logarithmic scale, when the entire domain is positive.
  """
  def __init__(self, base=10):
    self._base = base
  def ticks(self, domain_min, domain_max):
    exponents = numpy.arange(numpy.floor(numpy.log10(domain_min) / numpy.log10(self._base)), numpy.ceil(numpy.log10(domain_max) / numpy.log10(self._base)) + 1)
    locations = numpy.power(self._base, exponents)
    labels = ["%se%s" % (self._base, int(exponent)) for exponent in exponents]
    titles = numpy.repeat(None, len(labels))
    return locations, labels, titles

class NegativeLogTickLocator(object):
  """Generate ticks that are evenly spaced on a logarithmic scale, when the entire domain is negative.
  """
  def __init__(self, base=10):
    self._base = base
  def ticks(self, domain_min, domain_max):
    exponents = numpy.arange(numpy.ceil(numpy.log10(numpy.abs(domain_min)) / numpy.log10(self._base)), numpy.floor(numpy.log10(numpy.abs(domain_max)) / numpy.log10(self._base)) -1, -1)
    locations = -numpy.power(self._base, exponents)
    labels = ["-%se%s" % (self._base, int(exponent)) for exponent in exponents]
    titles = numpy.repeat(None, len(labels))
    return locations, labels, titles

class SymmetricLogTickLocator(object):
  """Generate ticks that are evenly spaced on a logarithmic scale, when the domain straddles zero.
  """
  def __init__(self, base=10):
    self._base = base
  def ticks(self, domain_min, domain_max):
    negative_exponents = numpy.arange(numpy.ceil(numpy.log10(numpy.abs(domain_min)) / numpy.log10(self._base)), -1, -1) if domain_min != 0 else []
    linear_locations = [0]
    positive_exponents = numpy.arange(0, numpy.ceil(numpy.log10(domain_max) / numpy.log10(self._base)) + 1) if domain_max != 0 else []

    locations = numpy.concatenate((-numpy.power(self._base, negative_exponents), linear_locations, numpy.power(self._base, positive_exponents)))
    labels = ["-%se%s" % (self._base, int(exponent)) for exponent in negative_exponents] + [str(location) for location in linear_locations] + ["%se%s" % (self._base, int(exponent)) for exponent in positive_exponents]
    titles = numpy.repeat(None, len(labels))
    return locations, labels, titles

class HeckbertTickLocator(object):
  """Generate ticks using the "Nice numbers for graph labels" algorithm by Paul Heckbert.

  Note that this locator can produce ticks outside the minimum / maximum axis
  domain.

  Parameters
  ----------
  count : number of ticks to generate
  """
  def __init__(self, count=5):
    self._count = count
  def ticks(self, domain_min, domain_max):
    def nicenum(x, rounding):
      exponent = numpy.floor(numpy.log10(x))
      fraction = x / numpy.power(10, exponent)
      if rounding: # pragma: no cover
        if fraction < 1.5:
          nice_fraction = 1
        elif fraction < 3:
          nice_fraction = 2
        elif fraction < 7:
          nice_fraction = 5
        else:
          nice_fraction = 10
      else: # pragma: no cover
        if fraction <= 1:
          nice_fraction = 1
        elif fraction <= 2:
          nice_fraction = 2
        elif fraction <= 5:
          nice_fraction = 5
        else:
          nice_fraction = 10
      return nice_fraction * numpy.power(10, exponent);

    tick_range = nicenum(domain_max - domain_min, rounding=False)
    tick_spacing = nicenum(tick_range / (self._count - 1), rounding=True)
    tick_min = numpy.floor(domain_min / tick_spacing) * tick_spacing
    tick_max = numpy.ceil(domain_max / tick_spacing) * tick_spacing
    locations = numpy.linspace(tick_min, tick_max, self._count)
    digits = int(numpy.max(-numpy.floor(numpy.log10(tick_spacing)), 0))
    labels = ["%.*f" % (digits, location) for location in locations]
    titles = numpy.repeat(None, len(labels))
    return locations, labels, titles

# An alpha version of the Talbot, Lin, Hanrahan tick mark generator for matplotlib.
# Described in "An Extension of Wilkinson's Algorithm for Positioning Tick Labels on Axes"
# by Justin Talbot, Sharon Lin, and Pat Hanrahan, InfoVis 2010.

# Implementation by Justin Talbot
# This implementation is in the public domain.
# Report bugs to jtalbot@stanford.edu

# A shortcoming:
# The weights used in the paper were designed for static plots where the extent of
# the tick marks unioned with the extent of the data defines the extent of the plot.
# In a plot where the extent of the plot is defined by the user (e.g. an interactive
# plot supporting panning and zooming), the weights don't work as well. In particular,
# you would want to retune them assuming that the tick labels must be inside
# the provided view range. You probably want higher weighting on simplicity and lower
# on coverage and possibly density. But I haven't experimented in any detail with this.
#
# If you do intend on using this for static plots in matplotlib, you should set
# only_inside to False in the call to Extended.extended. And then you should
# manually set your view extent to include the min and max ticks if they are outside
# the data range. This should produce the same results as the paper.

class ExtendedTickLocator(object):
  """Generate ticks using "An Extension of Wilkinson's Algorithm for Positioning Tick Labels on Axes" by Talbot, Lin, and Hanrahan.

  Parameters
  ----------
  count : desired number of ticks
    Note that the algorithm may produce fewer ticks than requested.
  steps : prioritized list of "nice" values to use for generating ticks.
  only_inside : boolean
    If set to `True`, only ticks inside the axis domain will be generated.
  """
  def __init__(self, count=5, steps=None, weights=None, only_inside=False):
    self._count = count
    self._steps = steps if steps is not None else [1, 5, 2, 2.5, 4, 3]
    self._weights = weigths if weights is not None else [0.25, 0.2, 0.5, 0.05]
    self._only_inside = only_inside

  def ticks(self, domain_min, domain_max):
    def coverage(dmin, dmax, lmin, lmax):
      range = dmax-dmin
      return 1 - 0.5 * (numpy.power(dmax-lmax, 2)+numpy.power(dmin-lmin, 2)) / numpy.power(0.1 * range, 2)

    def coverage_max(dmin, dmax, span):
      range = dmax-dmin
      if span > range:
        half = (span-range)/2.0
        return 1 - numpy.power(half, 2) / numpy.power(0.1*range, 2)
      else:
        return 1

    def density(k, m, dmin, dmax, lmin, lmax):
      r = (k-1.0) / (lmax-lmin)
      rt = (m-1.0) / (max(lmax, dmax) - min(lmin, dmin))
      return 2 - max( r/rt, rt/r )

    def density_max(k, m):
      if k >= m:
        return 2 - (k-1.0)/(m-1.0)
      else:
        return 1

    def simplicity(q, Q, j, lmin, lmax, lstep):
      eps = 1e-10
      n = len(Q)
      i = Q.index(q)+1
      v = 1 if ((lmin % lstep < eps or (lstep - lmin % lstep) < eps) and lmin <= 0 and lmax >= 0) else 0
      return (n-i)/(n-1.0) + v - j

    def simplicity_max(q, Q, j):
      n = len(Q)
      i = Q.index(q)+1
      v = 1
      return (n-i)/(n-1.0) + v - j


    def legibility(lmin, lmax, lstep):
      return 1

    def legibility_max(lmin, lmax, lstep):
      return 1 # pragma: no cover

    def extended(dmin, dmax, m, Q, only_inside, w):
      n = len(Q)
      best_score = -2.0

      j = 1.0
      while j < float('infinity'):
        for q in Q:
          sm = simplicity_max(q, Q, j)

          if w[0] * sm + w[1] + w[2] + w[3] < best_score:
            j = float('infinity')
            break

          k = 2.0
          while k < float('infinity'):
            dm = density_max(k, m)

            if w[0] * sm + w[1] + w[2] * dm + w[3] < best_score:
              break

            delta = (dmax-dmin)/(k+1.0)/j/q
            z = numpy.ceil(numpy.log10(delta))

            while z < float('infinity'):
              step = j*q*numpy.power(10,z)
              cm = coverage_max(dmin, dmax, step*(k-1.0))

              if w[0] * sm + w[1] * cm + w[2] * dm + w[3] < best_score:
                break

              min_start = numpy.floor(dmax/step)*j - (k-1.0)*j
              max_start = numpy.ceil(dmin/step)*j

              if min_start > max_start:
                z = z+1
                break

              for start in range(int(min_start), int(max_start)+1):
                lmin = start * (step/j)
                lmax = lmin + step*(k-1.0)
                lstep = step

                s = simplicity(q, Q, j, lmin, lmax, lstep)
                c = coverage(dmin, dmax, lmin, lmax)
                d = density(k, m, dmin, dmax, lmin, lmax)
                l = legibility(lmin, lmax, lstep)

                score = w[0] * s + w[1] * c + w[2] * d + w[3] * l

                if score > best_score and (not only_inside or (lmin >= dmin and lmax <= dmax)):
                  best_score = score
                  best = (lmin, lmax, lstep, q, k)
              z = z+1
            k = k+1
        j = j+1
      return best

    lmin, lmax, lstep, q, k = extended(domain_min, domain_max, self._count - 1, self._steps, self._only_inside, self._weights)
    locations = numpy.arange(k) * lstep + lmin
    digits = int(numpy.max(-numpy.floor(numpy.log10(lstep)), 0))
    labels = ["%.*f" % (digits, location) for location in locations]
    titles = numpy.repeat(None, len(labels))
    return locations, labels, titles


###############################################################################################
# Axes (projections)

class Axes2D(object):
  """Standard two-dimensional Cartesian coordinate system.

  Do not create Axes2D instances directly.  Use factory methods such
  as :meth:`toyplot.Canvas.axes` instead.
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
      self._style = {"stroke":"none", "fill":"white", "opacity":0.75}
      self._style.update(style)
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
      self._style.update(value)

  class CoordinatesLabelHelper(object):
    def __init__(self, style):
      self._style = {"font-size":"10px", "font-weight":"normal", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle"}
      self._style.update(style)
    @property
    def style(self):
      return self._style
    @style.setter
    def style(self, value):
      self._style.update(value)

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
      self._style = {"font-weight":"bold", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle"}
      self._style.update(style)
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
      self._style.update(value)

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
      self._style.update(value)

  class PerTickHelper(object):
    class TickProxy(object):
      def __init__(self, tick):
        self._tick = tick
      @property
      def style(self):
        return self._tick.get("style", {})
      @style.setter
      def style(self, value):
        style = self._tick.get("style", {})
        style.update(value)
        self._tick["style"] = style
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
      self._style.update(value)

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
      self._style.update(value)

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
        return ExtendedTickLocator()
      else:
        scale, base = scale
        if scale == "log":
          if domain_max < 0:
            return NegativeLogTickLocator(base=base)
          elif 0 < domain_min:
            return PositiveLogTickLocator(base=base)
          return SymmetricLogTickLocator(base=base)

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

  def bars(self, a, b=None, c=None, along="x", baseline="stacked", fill=None, colormap=None, palette=None, opacity=1.0, title=None, style={}, id=None):
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
    a, b, c : array-like series data.
    along : string, "x" or "y", optional
      Specify "x" (the default) for vertical bars, or "y" for horizontal bars.
    baseline: array-like, "stacked", "symmetrical", "wiggle", or None
    fill : array-like set of colors, optional
      Specify a single color for all bars, one color per series, or one color per bar.
      Color values can be explicit toyplot colors, or scalar values to be mapped
      to colors using the `colormap` or `palette` parameter.
    colormap : :class:`toyplot.color.Map`, optional
      Colormap to be used for mapping scalar `fill` values to colors.  If
      unspecified, a default :class:`toyplot.color.LinearMap` is used.
    palette : :class:`toyplot.color.Palette`, optional
      Palette to be used for mapping scalar `fill` values to colors.  If
      unspecified, a default :class:`toyplot.color.Palette` is used.
    opacity : array-like set of opacities, optional
      Specify a single opacity for all bars, one opacity per series, or one opacity per bar.
    title : array-like set of strings, optional
      Specify a single title, one title per series, or one title per bar.
    style : dict, optional
      Collection of CSS styles to be applied globally.
    id : string, optional

    Returns
    -------
    bars : :class:`toyplot.BarBoundariesMark` or :class:`toyplot.BarMagnitudesMark`
    """

    if baseline is None:
      if a is not None and b is not None and c is not None:
        a = _require_scalar_vector(a)
        b = _require_scalar_vector(b, len(a))
        c = _require_scalar_array(c)
        if c.ndim == 1:
          c = _require_scalar_vector(c, len(a))
          series = numpy.ma.column_stack((numpy.repeat(0, len(c)), c))
        elif c.ndim == 2:
          series = _require_scalar_matrix(c)
        position = numpy.ma.column_stack((a, b))
      elif a is not None and b is not None:
        a = _require_scalar_vector(a)
        b = _require_scalar_array(b)
        if b.ndim == 1:
          b = _require_scalar_vector(b, len(a))
          series = numpy.ma.column_stack((numpy.repeat(0, len(b)), b))
        elif b.ndim == 2:
          series = _require_scalar_matrix(b)
        position = numpy.concatenate((a[0:1] - (a[1:2] - a[0:1]) * 0.5, (a[:-1] + a[1:]) * 0.5, a[-1:] + (a[-1:] - a[-2:-1]) * 0.5))
        position = numpy.ma.column_stack((position[:-1], position[1:]))
      else:
        a = _require_scalar_array(a)
        if a.ndim == 1:
          a = _require_scalar_vector(a)
          series = numpy.ma.column_stack((numpy.repeat(0, len(a)), a))
        elif a.ndim == 2:
          series = _require_scalar_matrix(a)
        position = numpy.ma.column_stack((numpy.arange(series.shape[0]) - 0.5, numpy.arange(series.shape[0]) + 0.5))

      default_color = [next(self._bar_colors) for i in range(series.shape[1]-1)]
      fill = toyplot.color._broadcast_color(default_color if fill is None else fill, (series.shape[0], series.shape[1]-1), colormap=colormap, palette=palette)
      opacity = _broadcast_scalar(opacity, (series.shape[0], series.shape[1]-1))
      title = _broadcast_object(title, (series.shape[0], series.shape[1]-1))
      style = _require_style(style)
      id = _require_optional_id(id)

      computed_style = {"stroke":"white", "stroke-width":1.0}
      computed_style.update(style)

      if along == "x":
        self._update_domain(position, series)
      elif along == "y":
        self._update_domain(series, position)

      self._children.append(BarBoundariesMark(along=along, position=position, series=series, fill=fill, opacity=opacity, title=title, style=computed_style, id=id))
      return self._children[-1]
    else: # baseline is not None
      if a is not None and b is not None and c is not None:
        a = _require_scalar_vector(a)
        b = _require_scalar_vector(b, len(a))
        c = _require_scalar_array(c)
        if c.ndim == 1:
          c = _require_scalar_vector(c, len(a))
          series = numpy.ma.column_stack((c,))
        elif c.ndim == 2:
          series = _require_scalar_matrix(c, rows=len(a))
        position = numpy.ma.column_stack((a, b))
      elif a is not None and b is not None:
        a = _require_scalar_vector(a)
        b = _require_scalar_array(b)
        if b.ndim == 1:
          b = _require_scalar_vector(b, len(a))
          series = numpy.ma.column_stack((b,))
        elif b.ndim == 2:
          series = _require_scalar_matrix(b, rows=len(a))
        position = numpy.concatenate((a[0:1] - (a[1:2] - a[0:1]) * 0.5, (a[:-1] + a[1:]) * 0.5, a[-1:] + (a[-1:] - a[-2:-1]) * 0.5))
        position = numpy.ma.column_stack((position[:-1], position[1:]))
      elif a is not None:
        if isinstance(a, tuple) and len(a) == 2:
          counts, edges = a
          position = numpy.ma.column_stack((edges[:-1], edges[1:]))
          series = numpy.ma.column_stack((_require_scalar_vector(counts, len(position)),))
        else:
          a = _require_scalar_array(a)
          if a.ndim == 1:
            series = numpy.ma.column_stack((a,))
          elif a.ndim == 2:
            series = a
          position = numpy.ma.column_stack((numpy.arange(series.shape[0]) - 0.5, numpy.arange(series.shape[0]) + 0.5))

      default_color = [next(self._bar_colors) for i in range(series.shape[1])]
      fill = toyplot.color._broadcast_color(default_color if fill is None else fill, series.shape, colormap=colormap, palette=palette)
      opacity = _broadcast_scalar(opacity, series.shape)
      title = _broadcast_object(title, series.shape)
      style = _require_style(style)
      id = _require_optional_id(id)

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

      computed_style = {"stroke":"white", "stroke-width":1.0}
      computed_style.update(style)

      boundaries = numpy.cumsum(numpy.column_stack((baseline, series)), axis=1)

      if along == "x":
        self._update_domain(position, boundaries)
      elif along == "y":
        self._update_domain(boundaries, position)

      self._children.append(BarMagnitudesMark(along=along, position=position, baseline=baseline, series=series, fill=fill, opacity=opacity, title=title, style=computed_style, id=id))
      return self._children[-1]

  def colorbar(self, values=None, palette=None, colormap=None, label=None, min=None, max=None, id=None, tick_length=5, tick_locator=None, offset=0, width=10, style={}):
    if colormap is None:
      if palette is None:
        palette = toyplot.color.brewer("BlueGreen")
      colormap = toyplot.color.LinearMap(palette=palette)
    style = _require_style(style)

    mark = VColorBarMark(xmin_range=self._xmax_range + offset, xmax_range=self._xmax_range + offset + width, ymin_range=self._ymin_range, ymax_range=self._ymax_range, label=label, colormap=colormap, padding=self._padding, tick_length=tick_length, min=min, max=max, tick_locator=tick_locator, style=style, id=id)
    if values is not None:
      mark._update_domain(numpy.min(values), numpy.max(values))
    self._parent._children.append(mark)
    return mark

  def fill(self, a, b=None, c=None, along="x", baseline=None, fill=None, colormap=None, palette=None, opacity=1.0, title=None, style={}, id=None):
    """Fill multiple regions separated by curves.

    Parameters
    ----------
    a, b, c : array-like sets of coordinates
      If `a`, `b`, and `c` are provided, they specify the X coordinates, bottom
      coordinates, and top coordinates of the region respectively.  If only `a`
      and `b` are provided, they specify the top coordinates and bottom
      coordinates, with the X coordinates ranging from [0, N).  If only `a` is
      provided, it specifies the top of the region, with the bottom along the
      origin and the X coordinates ranging from [0, N).
    title : string, optional
      Human-readable title for the mark.  The SVG / HTML backends render the
      title as a tooltip.
    style : dict, optional
      Collection of CSS styles to apply to the mark.  See
      :class:`toyplot.FillBoundariesMark` for a list of useful styles.
    id : string, optional

    Returns
    -------
    mark : :class:`toyplot.FillBoundariesMark` or :class:`toyplot.FillMagnitudesMark`
    """
    if baseline is None:
      if a is not None and b is not None and c is not None:
        position = _require_scalar_vector(a)
        b = _require_scalar_vector(b, len(position))
        c = _require_scalar_vector(c, len(position))
        series = numpy.ma.column_stack((b, c))
      elif a is not None and b is not None:
        a = _require_scalar_vector(a)
        b = _require_scalar_array(b)
        if b.ndim == 1:
          b = _require_scalar_vector(b, len(a))
          series = numpy.ma.column_stack((a, b))
          position = numpy.ma.array(numpy.arange(series.shape[0]))
        elif b.ndim == 2:
          series = _require_scalar_matrix(b)
          position = _require_scalar_vector(a, series.shape[0]);
      else:
        a = _require_scalar_array(a)
        if a.ndim == 1:
          a = _require_scalar_vector(a)
          b = numpy.ma.repeat(0, len(a))
          series = numpy.ma.column_stack((b, a))
          position = numpy.ma.arange(series.shape[0])
        elif a.ndim == 2:
          series = _require_scalar_matrix(a)
          position = numpy.ma.arange(series.shape[0])

      default_color = [next(self._fill_colors) for i in range(series.shape[1]-1)]
      fill = toyplot.color._broadcast_color(default_color if fill is None else fill, series.shape[1]-1, colormap=colormap, palette=palette)
      opacity = _broadcast_scalar(opacity, series.shape[1]-1)
      title = _broadcast_object(title, series.shape[1]-1)
      style = _require_style(style)
      id = _require_optional_id(id)

      computed_style = {"stroke":"none"}
      computed_style.update(style)

      if along == "x":
        self._update_domain(position, series)
      elif along == "y":
        self._update_domain(series, position)

      self._children.append(FillBoundariesMark(along=along, position=position, series=series, fill=fill, opacity=opacity, title=title, style=computed_style, id=id))
      return self._children[-1]
    else: # baseline is not None
      if a is not None and b is not None:
        b = _require_scalar_array(b)
        if b.ndim == 1:
          series = numpy.ma.column_stack((b,))
        elif b.ndim == 2:
          series = b
        position = _require_scalar_vector(a, series.shape[0])
      else:
        a = _require_scalar_array(a)
        if a.ndim == 1:
          series = numpy.ma.column_stack((a,))
        elif a.ndim == 2:
          series = a
        position = numpy.ma.arange(series.shape[0])

      default_color = [next(self._fill_colors) for i in range(series.shape[1])]
      fill = toyplot.color._broadcast_color(default_color if fill is None else fill, series.shape[1], colormap=colormap, palette=palette)
      opacity = _broadcast_scalar(opacity, series.shape[1])
      title = _broadcast_object(title, series.shape[1])
      style = _require_style(style)
      id = _require_optional_id(id)

      computed_style = {"stroke":"none"}
      computed_style.update(style)

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

      self._children.append(FillMagnitudesMark(along=along, position=position, baseline=baseline, series=series, fill=fill, opacity=opacity, title=title, style=computed_style, id=id))
      return self._children[-1]

  def plot(self, a, b=None, along="x", stroke=None, stroke_colormap=None, stroke_palette=None, stroke_width=2.0, stroke_opacity=1.0, marker=None, size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style={}, mstyle={"stroke":"none"}, mlstyle={}, id=None):
    """Add a bivariate plot to the axes.

    Parameters
    ----------
    a, b : array-like sets of coordinates
      If `a` and `b` are provided, they specify the X coordinates and Y
      coordinates of each point in the plot.  If only `a` is provided, it
      specifies the Y coordinates, and the X coordinates will range from [0, N).
    title : string, optional
      Human-readable title for the mark.  The SVG / HTML backends render the
      title as a tooltip.
    style : dict, optional
      Collection of CSS styles to apply across all datums.  See
      :class:`toyplot.PlotMark` for a list of useful styles.
    id : string, optional

    Returns
    -------
    plot : :class:`toyplot.PlotMark`
    """
    if a is not None and b is not None:
      position = _require_scalar_vector(a)
      b = _require_scalar_array(b)
      if b.ndim == 1:
        b = _require_scalar_vector(b, len(position))
        series = numpy.ma.column_stack((b,))
      elif b.ndim == 2:
        series = _require_scalar_matrix(b, rows=len(position))
    else:
      a = _require_scalar_array(a)
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
    style = _require_style(style)
    mstyle = _require_style(mstyle)
    mlstyle = _require_style(mlstyle)
    id = _require_optional_id(id)

    computed_style = {"fill":"none"}
    computed_style.update(style)

    if along == "x":
      self._update_domain(position, series)
    elif along == "y":
      self._update_domain(series, position)

    self._children.append(PlotMark(along=along, show_stroke=True, position=position, series=series, stroke=stroke, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker, size=size, fill=fill, opacity=opacity, title=title, style=computed_style, mstyle=mstyle, mlstyle=mlstyle, id=id))
    return self._children[-1]

  def scatterplot(self, a, b=None, along="x", stroke=None, stroke_colormap=None, stroke_palette=None, stroke_width=2.0, stroke_opacity=1.0, marker="o", size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style={"stroke":"none"}, mstyle={"stroke":"none"}, mlstyle={}, id=None):
    """Add a bivariate plot to the axes.

    Parameters
    ----------
    a, b : array-like sets of coordinates
      If `a` and `b` are provided, they specify the X coordinates and Y
      coordinates of each point in the plot.  If only `a` is provided, it
      specifies the Y coordinates, and the X coordinates will range from [0, N).
    title : string, optional
      Human-readable title for the mark.  The SVG / HTML backends render the
      title as a tooltip.
    style : dict, optional
      Collection of CSS styles to apply across all datums.  See
      :class:`toyplot.PlotMark` for a list of useful styles.
    id : string, optional

    Returns
    -------
    plot : :class:`toyplot.PlotMark`
    """
    if a is not None and b is not None:
      position = _require_scalar_vector(a)
      b = numpy.ma.array(b).astype("float64")
      if b.ndim == 0:
        b = _require_scalar_vector(b, len(position))
        series = numpy.ma.column_stack((b,))
      elif b.ndim == 1:
        b = _require_scalar_vector(b, len(position))
        series = numpy.ma.column_stack((b,))
      elif b.ndim == 2:
        series = _require_scalar_matrix(b, rows=len(position))
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
    style = _require_style(style)
    mstyle = _require_style(mstyle)
    mlstyle = _require_style(mlstyle)
    id = _require_optional_id(id)

    computed_style = {"fill":"none"}
    computed_style.update(style)

    if along == "x":
      self._update_domain(position, series)
    elif along == "y":
      self._update_domain(series, position)

    self._children.append(PlotMark(along=along, show_stroke=False, position=position, series=series, stroke=stroke, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker, size=size, fill=fill, opacity=opacity, title=title, style=computed_style, mstyle=mstyle, mlstyle=mlstyle, id=id))
    return self._children[-1]

  def rect(self, a, b, c, d, along="x", fill=None, colormap=None, palette=None, opacity=1.0, title=None, style={"stroke":"none"}, id=None):
    a = _require_scalar_vector(a)
    b = _require_scalar_vector(b, len(a))
    c = _require_scalar_vector(c, len(a))
    d = _require_scalar_vector(d, len(a))
    series = numpy.column_stack((a, b, c, d))

    default_color = next(self._rect_colors)
    fill = toyplot.color._broadcast_color(default_color if fill is None else fill, series.shape[0], colormap=colormap, palette=palette)
    opacity = _broadcast_scalar(opacity, series.shape[0])
    title = _broadcast_object(title, series.shape[0])
    style = _require_style(style)
    id = _require_optional_id(id)

    if along == "x":
      self._update_domain(numpy.concatenate((a, b)), numpy.concatenate((c, d)))
    elif along == "y":
      self._update_domain(numpy.concatenate((c, d)), numpy.concatenate((a, b)))

    self._children.append(RectMark(along=along, series=series, fill=fill, opacity=opacity, title=title, style=style, id=id))
    return self._children[-1]

  def text(self, a, b, text, along="x", angle=0, fill=None, colormap=None, palette=None, opacity=1.0, title=None, style={}, id=None):
    """Add text to the axes.

    Parameters
    ----------
    a, b : float
      Coordinates of the text anchor.
    text : string
      The text to be displayed.
    title : string, optional
      Human-readable title for the mark.  The SVG / HTML backends render the
      title as a tooltip.
    style : dict, optional
      Collection of CSS styles to apply to the mark.  See
      :class:`toyplot.TextMark` for a list of useful styles.

    Returns
    -------
    text : :class:`toyplot.TextMark`
    """
    a = _require_scalar_vector(a)
    b = _require_scalar_vector(b, len(a))
    series = numpy.column_stack((a, b))

    text = _broadcast_object(text, series.shape[0])
    angle = _broadcast_scalar(angle, series.shape[0])
    default_color = next(self._text_colors)
    fill = toyplot.color._broadcast_color(default_color if fill is None else fill, series.shape[0], colormap=colormap, palette=palette)
    opacity = _broadcast_scalar(opacity, series.shape[0])
    title = _broadcast_object(title, series.shape[0])
    style = _require_style(style)
    id = _require_optional_id(id)

    computed_style = {"font-weight":"normal", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle"}
    computed_style.update(style)

    if along == "x":
      self._update_domain(a, b)
    elif along == "y":
      self._update_domain(b, a)

    self._children.append(TextMark(along=along, series=series, text=text, angle=angle, fill=fill, opacity=opacity, title=title, style=computed_style, id=id))
    return self._children[-1]

  def hlines(self, y, stroke=None, colormap=None, palette=None, opacity=1.0, title=None, style={}, id=None):
    """Add horizontal line(s) to the axes.

    Horizontal lines are convenient because they're guaranteed to fill the axes from
    left to right regardless of the axes size.

    Parameters
    ----------
    y : array-like set of Y coordinates
      One horizontal line will be drawn through each Y coordinate provided.
    title : string, optional
      Human-readable title for the mark.  The SVG / HTML backends render the
      title as a tooltip.
    style : dict, optional
      Collection of CSS styles to apply to the mark.  See
      :class:`toyplot.AxisLinesMark` for a list of useful styles.
    id : string, optional

    Returns
    -------
    hlines : :class:`toyplot.AxisLinesMark`
    """
    position = _require_scalar_vector(y)

    default_color = "black"
    stroke = toyplot.color._broadcast_color(default_color if stroke is None else stroke, position.shape[0], colormap=colormap, palette=palette)
    opacity = _broadcast_scalar(opacity, position.shape[0])
    title = _broadcast_object(title, position.shape[0])
    style = _require_style(style)
    id = _require_optional_id(id)

    self._update_domain(numpy.array([]), position)
    self._children.append(AxisLinesMark(along="y", position=position, stroke=stroke, opacity=opacity, title=title, style=style, id=id))
    return self._children[-1]

  def vlines(self, x, stroke=None, colormap=None, palette=None, opacity=1.0, title=None, style={}, id=None):
    """Add vertical line(s) to the axes.

    Vertical lines are convenient because they're guaranteed to fill the axes from
    top to bottom regardless of the axes size.

    Parameters
    ----------
    y : array-like set of Y coordinates
      One horizontal line will be drawn through each Y coordinate provided.
    title : string, optional
      Human-readable title for the mark.  The SVG / HTML backends render the
      title as a tooltip.
    style : dict, optional
      Collection of CSS styles to apply to the mark.  See
      :class:`toyplot.AxisLinesMark` for a list of useful styles.
    id : string, optional

    Returns
    -------
    hlines : :class:`toyplot.AxisLinesMark`
    """
    position = _require_scalar_vector(x)

    default_color = "black"
    stroke = toyplot.color._broadcast_color(default_color if stroke is None else stroke, position.shape[0], colormap=colormap, palette=palette)
    opacity = _broadcast_scalar(opacity, position.shape[0])
    title = _broadcast_object(title, position.shape[0])
    style = _require_style(style)
    id = _require_optional_id(id)

    self._update_domain(position, numpy.array([]))
    self._children.append(AxisLinesMark(along="x", position=position, stroke=stroke, opacity=opacity, title=title, style=style, id=id))
    return self._children[-1]











  def legend(self, marks, bounds=None, rect=None, corner=None, grid=None, gutter=50, style={}, label_style={}, id=None):
    """Add a legend to the axes.

    Parameters
    ----------
    marks : sequence of marks to add to the legend
      Each mark to be displayed in the legend should be specified using either
      a (label, mark) tuple or a (label, mark, style) tuple.  Each label should
      be the human-readable text to be displayed next to the mark.  The mark
      can be a string value "line" or "rect", a marker string "o", "s", "^",
      or an actual intance of :class:`toyplot.Mark`.
    bounds : (xmin, xmax, ymin, ymax) tuple, optional
      Use the bounds property to position / size the legend by specifying the
      position of each of its boundaries.  The boundaries may be specified in
      absolute drawing units, or as a percentage of the axes width / height
      using strings that end with "%".
    rect : (x, y, width, height) tuple, optional
      Use the rect property to position / size the legend by specifying its
      upper-left-hand corner, width, and height.  Each parameter may be specified
      in absolute drawing units, or as a percentage of the axes width / height
      using strings that end with "%".
    corner : (corner, width, height, inset) tuple, optional
      Use the corner property to position / size the legend by specifying its
      width and height, plus an inset from a corner of the axes.  Allowed
      corner values are "top-left", "top", "top-right", "right",
      "bottom-right", "bottom", "bottom-left", and "left".  The width and
      height may be specified in absolute drawing units, or as a percentage of
      the axes width / height using strings that end with "%".  The inset is
      specified in absolute drawing units.
    grid : (rows, columns, index) tuple, or (rows, columns, i, j) tuple, or (rows, columns, i, rowspan, j, columnspan) tuple, optional
      Use the grid property to position / size the legend using a collection of
      grid cells filling the axes.  Specify the number of rows and columns in
      the grid, then specify either a zero-based cell index (which runs in
      left-ot-right, top-to-bottom order), a pair of i, j cell coordinates, or
      a set of i, column-span, j, row-span coordinates so the legend can cover
      more than one cell.
    gutter : size of the gutter around grid cells, optional
      Specifies the amount of empty space to leave between grid cells When using the
      `grid` parameter to position the legend.
    style : dict, optional
    id : string, optional

    Returns
    -------
    legend : :class:`toyplot.LegendMark`
    """
    gutter = _require_scalar(gutter)
    style = _require_style(style)
    id = _require_optional_id(id)

    xmin, xmax, ymin, ymax = _region(self._xmin_range, self._xmax_range, self._ymin_range, self._ymax_range, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
    self._children.append(LegendMark(xmin, xmax, ymin, ymax, marks, style, label_style, id))
    return self._children[-1]

###############################################################################################
# Animation

class AnimationFrame(object):
  """Used to specify modifications to a `toyplot.Canvas` during animation.

  Do not create AnimationFrame instances yourself, an instance of
  AnimationFrame is automatically created by :meth:`toyplot.Canvas.animate`
  or :meth:`toyplot.Canvas.time` and passed to your callback.
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
    return "<toyplot.AnimationFrame %s %.2f %.2f>" % (self._index, self._begin, self._end)

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
    mark : :class:`toyplot.Mark` instance
    style : dict containing CSS style information
    """
    if not isinstance(mark, Mark):
      raise ValueError("Mark style can only be set on toyplot.Mark instances.")
    self._changes[self._begin]["set-mark-style"].append((mark, style))

  def set_datum_style(self, mark, series, datum, style):
    """Change the style of one datum in a :class:`toyplot.Mark` at the current frame.

    Parameters
    ----------
    mark : :class:`toyplot.Mark` instance
    index : zero-based index of the datum to modify
    style : dict containing CSS style information
    """
    if not isinstance(mark, (BarBoundariesMark, BarMagnitudesMark, PlotMark, TextMark)):
      raise ValueError("Cannot set datum style for %s." % type(mark))
    self._changes[self._begin]["set-datum-style"].append((mark, series, datum, style))

  def set_datum_text(self, mark, series, datum, text):
    """Change the text in a :class:`toyplot.TextMark` at the current frame.

    Parameters
    ----------
    mark : :class:`toyplot.TextMark` instance
    value : string
    """
    if not isinstance(mark, TextMark):
      raise ValueError("Mark text can only be set for toyplot.TextMark instances.")
    self._changes[self._begin]["set-datum-text"].append((mark, series, datum, text))

###############################################################################################
# Canvas

class Canvas(object):
  """Top-level container for Toyplot drawings.

  Parameters
  ----------
  width : integer, optional
    Width of the canvas in drawing units.  Defaults to 600 if unspecified.
  height : integer, optional
    Height of the canvas in drawing units.  Defaults to the canvas width if unspecified.
  style : dict, optional
    Collection of CSS styles to apply to the canvas.
  autorender : boolean, optional
    Turn autorendering on / off for this canvas.  Default:
    use the global autorender flag.

  Examples
  --------

  The following would create a Canvas 800 units wide, 600 units tall, with a yellow background:

  >>> canvas = toyplot.Canvas(800, 600, style={"background-color":"yellow"})
  """
  def __init__(self, width=None, height=None, style={}, id=None, autorender=None):
    self._width = width if width is not None else 600
    self._height = height if height is not None else self._width
    self._style = {"background-color" : "transparent", "fill" : "#343434", "fill-opacity" : 1.0, "font-family":"helvetica", "font-size" : "12px", "opacity" : 1.0, "stroke" : "#343434", "stroke-opacity" : 1.0, "stroke-width" : 1.0}
    self._style.update(style)
    self._id = id
    self._animation = collections.defaultdict(lambda : collections.defaultdict(list))
    self._children = []

    self.autorender(autorender if autorender is not None else toyplot.autorender)

  def _repr_html_(self):
    import toyplot.html
    import xml.etree.ElementTree as xml
    return xml.tostring(toyplot.html.render(self), method="html")

  def animate(self, frames, callback=None):
    """Generate a collection of animation frames, calling a callback to store an explicit representation of what changes at each frame.

    Parameters
    ----------
    frames : integer, tuple, or sequence
      Pass a sequence of values that specify the time (in seconds) of the
      beginning / end of each frame.  Note that the number of frames will be the
      length of the sequence minus one.  Alternatively, you can pass a 2-tuple
      containing the number of frames and the frame rate in frames-per-second.
      Finally, you may simply specify the number of frames, in which case the
      rate will default to 30 frames-per-second.
    callback : function
      The callback function will be called once per frame, and will receive an
      instance of :class:`toyplot.AnimationFrame` as its sole argument.  The
      callback function can access the frame number, time, and duration from the
      state object, and should use the other methods provided by the state object
      to make changes to the canvas.
    """
    if isinstance(frames, numbers.Integral):
      frames = (frames, 30.0)

    if isinstance(frames, tuple):
      frame_count, frame_rate = frames
      frames = numpy.linspace(0, frame_count / frame_rate, frame_count + 1, endpoint=True)

    for index in range(0, len(frames) - 1):
      frame = AnimationFrame(index, frames[index], frames[index + 1], self._animation)
      if callback:
        callback(frame)

    # Record the end-time of the last frame, so backends can calculate frame durations.
    self._animation[frames[-1]]

  def autorender(self, enable):
    """Enable / disable canvas autorendering.

    Autorendering - which is enabled by default when a canvas is created -
    controls how the canvas should be displayed automatically without
    caller intervention in certain interactive environments, such as IPython
    notebooks.

    Note that autorendering is disabled when a canvas is explicitly
    shown using any of the rendering backends.

    Parameters
    ----------
    enable : boolean
      Turn autorendering on / off.
    """
    if enable:
      if self not in Canvas._autorender_list:
        Canvas._autorender_list.append(self)
    else:
      if self in Canvas._autorender_list:
        Canvas._autorender_list.remove(self)

  def axes(self, bounds=None, rect=None, corner=None, grid=None, gutter=50, xmin=None, xmax=None, ymin=None, ymax=None, show=True, xshow=True, yshow=True, label=None, xlabel=None, ylabel=None, xticklocator=None, yticklocator=None, xscale="linear", yscale="linear", palette=None, padding=10, tick_length=5, id=None):
    """Add a set of 2D axes to the canvas.

    Parameters
    ----------
    xlabel : string, optional
      Human-readable label for the X axis.
    ylabel : string, optional
      Human-readable label for the Y axis.
    xmin, xmax, ymin, ymax : float, optional
      Used to explicitly override the axis domain (normally, the domain is
      implicitly defined by any marks added to the axes).

    Returns
    -------
    axes : :class:`toyplot.Axes2D`
    """
    xmin_range, xmax_range, ymin_range, ymax_range = _region(0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
    self._children.append(Axes2D(xmin_range, xmax_range, ymin_range, ymax_range, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, show=show, xshow=xshow, yshow=yshow, label=label, xlabel=xlabel, ylabel=ylabel, xticklocator=xticklocator, yticklocator=yticklocator, xscale=xscale, yscale=yscale, palette=palette, padding=padding, tick_length=tick_length, parent=self, id=id))
    return self._children[-1]

  def table(self, rows, columns, bounds=None, rect=None, corner=None, grid=None, gutter=50, id=None):
    xmin_range, xmax_range, ymin_range, ymax_range = _region(0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
    self._children.append(Table(xmin_range=xmin_range, xmax_range=xmax_range, ymin_range=ymin_range, ymax_range=ymax_range, rows=rows, columns=columns, id=id))
    return self._children[-1]

  def legend(self, marks, bounds=None, rect=None, corner=None, grid=None, gutter=50, style={}, label_style={}, id=None):
    """Add a legend to the canvas.

    Parameters
    ----------
    marks : sequence of marks to add to the legend
      Each mark to be displayed in the legend should be specified using either
      a (label, mark) tuple or a (label, mark, style) tuple.  Each label should
      be the human-readable text to be displayed next to the mark.  The mark
      can be a string value "line" or "rect", a marker string "o", "s", "^",
      or an actual intance of :class:`toyplot.Mark`.
    bounds : (xmin, xmax, ymin, ymax) tuple, optional
      Use the bounds property to position / size the legend by specifying the
      position of each of its boundaries.  The boundaries may be specified in
      absolute drawing units, or as a percentage of the canvas width / height
      using strings that end with "%".
    rect : (x, y, width, height) tuple, optional
      Use the rect property to position / size the legend by specifying its
      upper-left-hand corner, width, and height.  Each parameter may be specified
      in absolute drawing units, or as a percentage of the canvas width / height
      using strings that end with "%".
    corner : (corner, width, height, inset) tuple, optional
      Use the corner property to position / size the legend by specifying its
      width and height, plus an inset from a corner of the canvas.  Allowed
      corner values are "top-left", "top", "top-right", "right",
      "bottom-right", "bottom", "bottom-left", and "left".  The width and
      height may be specified in absolute drawing units, or as a percentage of
      the canvas width / height using strings that end with "%".  The inset is
      specified in absolute drawing units.
    grid : (rows, columns, index) tuple, or (rows, columns, i, j) tuple, or (rows, columns, i, rowspan, j, columnspan) tuple, optional
      Use the grid property to position / size the legend using a collection of
      grid cells filling the canvas.  Specify the number of rows and columns in
      the grid, then specify either a zero-based cell index (which runs in
      left-ot-right, top-to-bottom order), a pair of i, j cell coordinates, or
      a set of i, column-span, j, row-span coordinates so the legend can cover
      more than one cell.
    gutter : size of the gutter around grid cells, optional
      Specifies the amount of empty space to leave between grid cells When using the
      `grid` parameter to position the legend.
    style : dict, optional
    id : string, optional

    Returns
    -------
    legend : :class:`toyplot.LegendMark`
    """
    gutter = _require_scalar(gutter)
    style = _require_style(style)
    id = _require_optional_id(id)

    xmin, xmax, ymin, ymax = _region(0, self._width, 0, self._height, bounds=bounds, rect=rect, corner=corner, grid=grid, gutter=gutter)
    self._children.append(LegendMark(xmin, xmax, ymin, ymax, marks, style, label_style, id))
    return self._children[-1]

  def text(self, x, y, text, angle=0.0, fill=None, colormap=None, palette=None, opacity=1.0, title=None, style={}, id=None):
    """Add text to the canvas.

    Parameters
    ----------
    x, y : float
      Coordinates of the text anchor in canvas drawing units.  Note that canvas
      Y coordinates increase from top-to-bottom.
    text : string
      The text to be displayed.
    title : string, optional
      Human-readable title for the mark.  The SVG / HTML backends render the
      title as a tooltip.
    style : dict, optional
      Collection of CSS styles to apply to the mark.  See
      :class:`toyplot.TextMark` for a list of useful styles.

    Returns
    -------
    text : :class:`toyplot.TextMark`
    """
    x = _require_scalar_vector(x)
    y = _require_scalar_vector(y, len(x))
    series = numpy.column_stack((x, y))

    text = _broadcast_object(text, series.shape[0])
    angle = _broadcast_scalar(angle, series.shape[0])
    fill = toyplot.color._broadcast_color("black" if fill is None else fill, series.shape[0], colormap=colormap, palette=palette)
    opacity = _broadcast_scalar(opacity, series.shape[0])
    title = _broadcast_object(title, series.shape[0])
    style = _require_style(style)
    id = _require_optional_id(id)

    computed_style = {"font-weight":"normal", "stroke":"none", "text-anchor":"middle", "alignment-baseline":"middle"}
    computed_style.update(style)

    self._children.append(TextMark(along="x", series=series, text=text, angle=angle, fill=fill, opacity=opacity, title=title, style=computed_style, id=id))
    return self._children[-1]

  def time(self, begin, end, index=None):
    """Return a :class:`toyplot.AnimationFrame` with the given start and end time, ready to store animated canvas modifications.

    Parameters
    ----------
    begin : scalar
      Specify the frame start time (in seconds).
    end : scalar
      Specify the frame end time (in seconds).
    index : integer, optional
      Specify an index for this frame.  Note that the index is simply a
      convenience for code that depends on accessing the index from the
      result AnimationFrame.

    Returns
    -------
    frame : :class:`toyplot.AnimationFrame` instance.
    """
    if index is None:
      index = 0
    return AnimationFrame(index, begin, end, self._animation)

  def _pixel_scale(self, width=None, height=None, scale=None):
    """Return a scale factor to convert this canvas to a target width or height in pixels."""
    if numpy.count_nonzero([width is not None, height is not None, scale is not None]) > 1:
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
    if numpy.count_nonzero([width is not None, height is not None, scale is not None]) > 1:
      raise ValueError("Specify only one of width, height, or scale.")

    if width is not None:
      scale = toyplot.units.points(width) / self._width
    elif height is not None:
      scale = toyplot.units.points(height) / self._height
    elif scale is None:
      scale = 1.0
    return scale

  @staticmethod
  def _ipython_post_execute(): # pragma: no cover
    try:
      import IPython.display
      for canvas in [canvas for canvas in Canvas._autorender_list]:
        IPython.display.display(canvas)
    except:
      pass

  @staticmethod
  def _ipython_register(): # pragma: no cover
    try:
      import IPython
      if IPython.get_ipython():
        IPython.get_ipython().events.register("post_execute", Canvas._ipython_post_execute)
    except:
      pass

Canvas._autorender_list = []
Canvas._ipython_register()
toyplot.autorender = True

def bars(a, b=None, c=None, along="x", baseline="stacked", fill=None, colormap=None, palette=None, opacity=1.0, title=None, style={}, id=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style={}):
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.bars(a=a, b=b, c=c, along=along, baseline=baseline, fill=fill, colormap=colormap, palette=palette, opacity=opacity, title=title, style=style, id=id)
  return canvas, axes, mark

def fill(a, b=None, c=None, along="x", baseline=None, fill=None, colormap=None, palette=None, opacity=1.0, title=None, style={}, id=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style={}):
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.fill(a=a, b=b, c=c, along=along, baseline=baseline, fill=fill, colormap=colormap, palette=palette, opacity=opacity, title=title, style=style, id=id)
  return canvas, axes, mark

def plot(a, b=None, along="x", stroke=None, stroke_colormap=None, stroke_palette=None, stroke_width=2.0, stroke_opacity=1.0, marker=None, size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style={}, mstyle={"stroke":"none"}, mlstyle={}, id=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style={}):
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.plot(a=a, b=b, along=along, stroke=stroke, stroke_colormap=stroke_colormap, stroke_palette=stroke_palette, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker, size=size, fill=fill, fill_colormap=fill_colormap, fill_palette=fill_palette, opacity=opacity, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle, id=id)
  return canvas, axes, mark

def scatterplot(a, b=None, along="x", stroke=None, stroke_colormap=None, stroke_palette=None, stroke_width=2.0, stroke_opacity=1.0, marker="o", size=20, fill=None, fill_colormap=None, fill_palette=None, opacity=1.0, title=None, style={"stroke":"none"}, mstyle={"stroke":"none"}, mlstyle={}, id=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style={}):
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.scatterplot(a=a, b=b, along=along, stroke=stroke, stroke_colormap=stroke_colormap, stroke_palette=stroke_palette, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker, size=size, fill=fill, fill_colormap=fill_colormap, fill_palette=fill_palette, opacity=opacity, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle, id=id)
  return canvas, axes, mark

