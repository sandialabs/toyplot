# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numbers
import re
import toyplot.compatibility

def convert(value, target, default=None):
  """Convert quantities using real-world units.

    Supported units include: centimeter, centimeters, cm, decimeter,
    decimeters, dm, in, inch, inches, m, meter, meters, pica, picas, point,
    points, pt, pixel, pixels, and px.

  Parameters
  ----------
  value: number, string or (number, string) tuple
    Value to be converted.  The value may be a number (in which case the
    `default` parameter must specify the default unit of measure), a string
    containing a number and unit suffix (such as a CSS length), or a (value,
    units) tuple.
  target: string
    Unit of measure to convert to.
  default: optional string
    Default unit of measure to use when `value` is a plain number.

  Returns
  -------
  Returns `value` converted to the `target` units, as a floating point number.
  """
  if isinstance(value, numbers.Number):
    if default is None:
      raise ValueError("Value doesn't contain units, and no default units specified.")
    value = (value, default)
  elif isinstance(value, toyplot.compatibility.string_type):
    value, units = re.match(r"([^a-zA-Z]+)([a-zA-Z]+)\Z", value).groups()
    value = (float(value), units)
  if not (isinstance(value, tuple) and len(value) == 2 and isinstance(value[0], numbers.Number) and isinstance(value[1], toyplot.compatibility.string_type)):
    raise ValueError("Value must be a number, string or (number, string) tuple.")
  value, units = value
  units = units.lower()
  if units not in convert._conversions:
    raise ValueError("Unknown unit of measure: %s" % units)
  target = target.lower()
  if target not in convert._conversions:
    raise ValueError("Unknown unit of measure: %s" % target)
  return value * convert._conversions[units] / convert._conversions[target]
convert._conversions = {
  "centimeter": 28.3464567,
  "centimeters": 28.3464567,
  "cm": 28.3464567,
  "decimeter": 283.464567,
  "decimeters": 283.464567,
  "dm": 283.464567,
  "in": 72.0,
  "inch": 72.0,
  "inches": 72.0,
  "m": 2834.64567,
  "meter": 2834.64567,
  "meters": 2834.64567,
  "pica": 12.0,
  "picas": 12.0,
  "point": 1.0,
  "points": 1.0,
  "pt": 1.0,
  "px": 72.0 / 96.0,
  "pixel": 72.0 / 96.0,
  "pixels": 72.0 / 96.0,
  }

