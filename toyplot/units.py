# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for performing unit conversions.
"""


import numbers
import re

def convert(value, target, default=None, reference=None):
    """Convert quantities using real-world units.

      Supported unit abbreviations include: centimeter, centimeters, cm,
      decimeter, decimeters, dm, in, inch, inches, m, meter, meters, mm,
      millimeter, millimeters, pc, pica, picas, point, points, pt, pixel, pixels,
      and px.

      Relative quantities can be specified using %.

    Parameters
    ----------
    value: number, string or (number, string) tuple
      Value to be converted.  The value may be a number (in which case the
      `default` parameter must specify the default unit of measure), a string
      containing a number and unit abbreviation, or a (value, units) tuple.
    target: string
      Unit of measure to convert to.
    default: optional string
      Default unit of measure to use when `value` is a plain number, or when
      `reference` has been specified.
    reference: optional number
      When the caller specifies a relative measure using % as the unit abbreviation,
      the returned value will equal `value` * 0.01 * `reference`.  Note that the
      reference *must* be specified in `target` units.

    Returns
    -------
    Returns `value` converted to the `target` units, as a floating point number.
    """
    if isinstance(value, numbers.Number):
        if value == 0:
            return 0
        if default is None:
            raise ValueError("Value doesn't contain units, and no default units specified.")
        value = (value, default)
    elif isinstance(value, str):
        if value == "0":
            return 0
        value, units = re.match(r"([^a-zA-Z%]+)([a-zA-Z%]+)\Z", value).groups()
        value = (float(value), units)

    if not isinstance(value, tuple):
        raise ValueError("Value must be a number, string or (number, string) tuple.")
    if not len(value) == 2:
        raise ValueError("Value must be a number, string or (number, string) tuple.")
    if not isinstance(value[0], numbers.Number):
        raise ValueError("Value must be a number, string or (number, string) tuple.")
    if not isinstance(value[1], str):
        raise ValueError("Value must be a number, string or (number, string) tuple.")

    value, units = value
    units = units.lower()
    if units == "%":
        if reference is None:
            raise ValueError("Relative values require a reference.")
        return value * 0.01 * reference
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
    "millimeter": 2.83464567,
    "millimeters": 2.83464567,
    "mm": 2.83464567,
    "pc": 12.0,
    "pica": 12.0,
    "picas": 12.0,
    "pixel": 72.0 / 96.0,
    "pixels": 72.0 / 96.0,
    "point": 1.0,
    "points": 1.0,
    "pt": 1.0,
    "px": 72.0 / 96.0,
}
