# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numbers
import toyplot.compatibility

def region(xmin, xmax, ymin, ymax, bounds=None, rect=None, corner=None, grid=None, gutter=40):
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

