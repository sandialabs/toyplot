# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numpy
import toyplot.broadcast
import toyplot.require
import toyplot.units

def extents(text, style):
  """Compute (inexact) extents for a text string, based on the given coordinates and style.
  """
  text = toyplot.require.string_vector(text)
  lengths = numpy.array([len(string) for string in text])

  font_size = toyplot.units.convert(style["font-size"], target="px")
  anchor_shift = toyplot.units.convert(style.get("-toyplot-anchor-shift", "0px"), target="px", reference=font_size)
  text_anchor = style["text-anchor"]
  baseline_shift = toyplot.units.convert(style.get("baseline-shift", "0px"), target="px", reference=font_size)
  alignment_baseline = style["alignment-baseline"]

  x = toyplot.broadcast.scalar(anchor_shift, text.shape)
  y = toyplot.broadcast.scalar(-baseline_shift, text.shape)

  # Because we don't have any metrics for the font, assume that the average
  # character width and height match the font size.
  width = font_size * lengths
  height = font_size

  if text_anchor == "start":
    left = x
    right = x + width
  elif text_anchor == "middle":
    left = x - width / 2
    right = x + width / 2
  elif text_anchor == "end":
    left = x - width
    right = x
  else:
    raise ValueError("Unknown text-anchor value: %s" % text_anchor)

  if alignment_baseline == "hanging":
    top = y
    bottom = y + height
  elif alignment_baseline == "middle" or alignment_baseline == "central":
    top = y - height / 2
    bottom = y + height / 2
  elif alignment_baseline == "alpha":
    top = y - height
    bottom = y
  else:
    raise ValueError("Unknown alignment-baseline value: %s" % alignment_baseline)

  return (left, right, top, bottom)

