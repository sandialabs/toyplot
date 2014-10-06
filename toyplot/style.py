# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

def combine(*styles):
  """Combine multiple style specifications into one.
  """
  computed_style = {}
  for style in styles:
    if style is not None:
      computed_style.update(style)
  return computed_style

