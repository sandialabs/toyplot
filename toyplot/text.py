# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

def extents(x, y, text, style):
  """Compute (inexact) extents for a text string, based on the given coordinates and style.
  """
  font_size = style["font-size"].strip()
  if font_size[-2:] == "px":
    font_size = float(font_size[:-2])
  else:
    raise ValueError("font-size must use pixel units")

  anchor_shift = float(style["-toyplot-anchor-shift"])

  # Because we don't have any metrics for the font, assume that the average
  # character width and height match the font size.
  width = float(font_size * len(text))
  height = float(font_size)

  x += float(anchor_shift)

  text_anchor = style["text-anchor"]
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

  baseline_shift = style["baseline-shift"]
  if baseline_shift[-1] == "%":
    y -= float(baseline_shift[:-1]) * 0.01 * font_size
  else:
    y -= float(baseline_shift)

  alignment_baseline = style["alignment-baseline"]
  if alignment_baseline == "middle":
    top = y - height / 2
    bottom = y + height / 2
  else:
    raise ValueError("Unknown alignment-baseline value: %s" % alignment_baseline)

  return (left, right, top, bottom)

