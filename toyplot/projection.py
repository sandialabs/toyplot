# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numpy

def _mix(a, b, amount):
  return ((1.0 - amount) * a) + (amount * b)

def _log(x, base):
  return numpy.log10(numpy.abs(x)) / numpy.log10(base)

def _in_range(a, x, b):
  left = min(a, b)
  right = max(a, b)
  return numpy.logical_and(left <= x, x <= right)

class Piecewise(object):
  """Compute a projection from an arbitrary collection of linear and log segments."""
  def __init__(self, segments):
    self._segments = [(scale, float(domain_min), float(domain_max), float(range_min), float(range_max)) for scale, domain_min, domain_max, range_min, range_max in segments]

  def __call__(self, domain_values):
    """Transform values from the domain to the range."""
    domain_values = numpy.array(domain_values, dtype="float64")
    range_values = numpy.empty_like(domain_values)
    for scale, domain_min, domain_max, range_min, range_max in self._segments:
      segment = _in_range(domain_min, domain_values, domain_max)
      if scale == "linear":
        amount = (domain_values[segment] - domain_min) / (domain_max - domain_min)
        range_values[segment] = _mix(range_min, range_max, amount)
      else:
        scale, base = scale
        if scale == "log":
          amount = (_log(domain_values[segment], base) - _log(domain_min, base)) / (_log(domain_max, base) - _log(domain_min, base))
          range_values[segment] = _mix(range_min, range_max, amount)
        else:
          raise Exception("Unknown scale: %s" % (scale,))

    if range_values.shape == ():
      range_values = numpy.asscalar(range_values)
    return range_values

  def inverse(self, range_values):
    """Transform values from the range to the domain."""
    range_values = numpy.array(range_values, dtype="float64")
    domain_values = numpy.empty_like(range_values)
    for scale, domain_min, domain_max, range_min, range_max in self._segments:
      segment = _in_range(range_min, range_values, range_max)
      if scale == "linear":
        amount = (range_values[segment] - range_min) / (range_max - range_min)
        domain_values[segment] = _mix(domain_min, domain_max, amount)
      else:
        scale, base = scale
        if scale == "log":
          amount = (range_values[segment] - range_min) / (range_max - range_min)
          domain_values[segment] = numpy.sign(domain_min) * numpy.power(base, _mix(_log(domain_min, base), _log(domain_max, base), amount))
        else:
          raise Exception("Unknown scale: %s" % (scale,))

    if domain_values.shape == ():
      domain_values = numpy.asscalar(domain_values)
    return domain_values

def linear(domain_min, domain_max, range_min, range_max):
  return Piecewise([("linear", domain_min, domain_max, range_min, range_max)])

def log(base, domain_min, domain_max, range_min, range_max, linear_domain_min=-1, linear_domain_max=1):
  # Negative domain
  if domain_max < 0:
    return Piecewise([(("log", base), domain_min, domain_max, range_min, range_max)])

  # Positive domain
  if 0 < domain_min:
    return Piecewise([(("log", base), domain_min, domain_max, range_min, range_max)])

  # Mixed negative / positive domain
  if domain_min < linear_domain_min and linear_domain_max < domain_max:
    linear_range_min = _mix(range_min, range_max, 0.4)
    linear_range_max = _mix(range_min, range_max, 0.6)
    return Piecewise([
      (("log", base), domain_min, linear_domain_min, range_min, linear_range_min),
      ("linear", linear_domain_min, linear_domain_max, linear_range_min, linear_range_max),
      (("log", base), linear_domain_max, domain_max, linear_range_max, range_max),
      ])

  if domain_min < linear_domain_min:
    linear_range_min = _mix(range_min, range_max, 0.8)
    return Piecewise([
      (("log", base), domain_min, linear_domain_min, range_min, linear_range_min),
      ("linear", linear_domain_min, linear_domain_max, linear_range_min, range_max),
      ])

  if linear_domain_max < domain_max:
    linear_range_max = _mix(range_min, range_max, 0.2)
    return Piecewise([
      ("linear", domain_min, linear_domain_max, range_min, linear_range_max),
      (("log", base), linear_domain_max, domain_max, linear_range_max, range_max),
      ])

  return Piecewise([("linear", domain_min, domain_max, range_min, range_max)])

