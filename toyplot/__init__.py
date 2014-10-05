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

from toyplot.canvas import Canvas

def bars(a, b=None, c=None, along="x", baseline="stacked", fill=None, colormap=None, palette=None, opacity=1.0, title=None, style=None, id=None, xmin=None, xmax=None, ymin=None, ymax=None, label=None, xlabel=None, ylabel=None, xscale="linear", yscale="linear", padding=10, width=None, height=None, canvas_style=None):
  """Convenience function for creating a bar plot in a single call.

  See :meth:`toyplot.axes.Cartesian2.bars`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.axes.Cartesian2`
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

  See :meth:`toyplot.axes.Cartesian2.fill`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.axes.Cartesian2`
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

  See :meth:`toyplot.axes.Cartesian2.plot`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.axes.Cartesian2`
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

  See :meth:`toyplot.axes.Cartesian2.scatterplot`, :meth:`toyplot.canvas.Canvas.axes`, and :class:`toyplot.canvas.Canvas` for parameter descriptions.

  Returns
  -------
  canvas: :class:`toyplot.canvas.Canvas`
    A new canvas object.
  axes: :class:`toyplot.axes.Cartesian2`
    A new set of 2D axes that fill the canvas.
  mark: :class:`toyplot.mark.Plot`
    The new scatter plot mark.
  """
  canvas = Canvas(width=width, height=height, style=canvas_style)
  axes = canvas.axes(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, label=label, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, padding=padding)
  mark = axes.scatterplot(a=a, b=b, along=along, stroke=stroke, stroke_colormap=stroke_colormap, stroke_palette=stroke_palette, stroke_width=stroke_width, stroke_opacity=stroke_opacity, marker=marker, size=size, fill=fill, fill_colormap=fill_colormap, fill_palette=fill_palette, opacity=opacity, title=title, style=style, mstyle=mstyle, mlstyle=mlstyle, id=id)
  return canvas, axes, mark

