# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numbers

def points(value):
  """Convert a quantity with real-world units to points (72nds of an inch).

  Parameters
  ----------
  value : number or (number, string) tuple
    Value to be converted.  Pass a (value, units) tuple, or the units will be
    assumed to be "points".  Supported units include: centimeter, centimeters,
    cm, decimeter, decimeters, dm, in, inch, inches, m, meter, meters, pica,
    picas, point, points, and pt.
  """
  if isinstance(value, numbers.Number):
    value = (value, "points")
  if not (isinstance(value, tuple) and len(value) == 2 and isinstance(value[0], numbers.Number) and isinstance(value[1], basestring)):
    raise ValueError("Value must be a number or a (number, string) tuple.")
  value, units = value
  if units.lower() not in points._conversions:
    raise ValueError("Unknown unit of measure: %s" % units)
  return value * points._conversions[units.lower()]
points._conversions = {
  "centimeter":28.3464567,
  "centimeters":28.3464567,
  "cm":28.3464567,
  "decimeter":283.464567,
  "decimeters":283.464567,
  "dm":283.464567,
  "in":72.0,
  "inch":72.0,
  "inches":72.0,
  "m":2834.64567,
  "meter":2834.64567,
  "meters":2834.64567,
  "pica":12.0,
  "picas":12.0,
  "point":1.0,
  "points":1.0,
  "pt":1.0,
  }
