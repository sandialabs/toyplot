# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numpy

def _mix(a, b, amount):
  return ((1.0 - amount) * a) + (amount * b)

def _log(x, base):
  return numpy.log10(numpy.abs(x)) / numpy.log10(base)

def _signed_log(x, base):
  """Return the log of a number, retaining its sign (e.g. return -3 for log-base-10 of -1000)."""
  return numpy.sign(x) * numpy.log10(numpy.abs(x)) / numpy.log10(base)

def _symmetric_log(x, base, threshold=1):
  if isinstance(x, numpy.ndarray):
    x = numpy.ma.array(x, copy=True, dtype="float64")
    i = numpy.logical_and(~numpy.ma.getmaskarray(x), numpy.logical_or(x.data < -threshold, x.data > threshold))
    x[i] = numpy.sign(x[i]) * (threshold + numpy.log10(numpy.abs(x[i])) / numpy.log10(base))
    return x
  return x if numpy.abs(x) < threshold else numpy.sign(x) * (threshold + numpy.log10(numpy.abs(x)) / numpy.log10(base))

class Piecewise(object):
  """Compute a projection from an arbitrary collection of linear and log segments."""
  def __init__(self, segments):
    self._segments = [(scale, float(domain_min), float(domain_max), float(range_min), float(range_max)) for scale, domain_min, domain_max, range_min, range_max in segments]

  def __call__(self, domain_values):
    """Transform values from the domain to the range."""
    domain_values = numpy.array(domain_values, dtype="float64")
    range_values = numpy.empty_like(domain_values)
    for scale, domain_min, domain_max, range_min, range_max in self._segments:
      segment = numpy.logical_and(domain_min <= domain_values, domain_values <= domain_max)
      if scale == "linear":
        amount = (domain_values[segment] - domain_min) / (domain_max - domain_min)
        range_values[segment] = _mix(range_min, range_max, amount)
      else:
        scale, base = scale
        if scale == "log":
          amount = (_log(domain_values, base) - _log(domain_min, base)) / (_log(domain_max, base) - _log(domain_min, base))
          range_values[segment] = _mix(range_min, range_max, amount)
        else:
          raise Exception("Unknown scale: %s" % (scale,))
    return range_values

  def inverse(self, range_values):
    """Transform values from the range to the domain."""
    range_values = numpy.array(range_values, dtype="float64")
    domain_values = numpy.empty_like(range_values)
    for scale, domain_min, domain_max, range_min, range_max in self._segments:
      segment = numpy.logical_and(range_min <= range_values, range_values <= range_max)
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

class Linear(object):
  """Compute linear projections between a domain and a range."""
  def __init__(self, domain_min, domain_max, range_min, range_max):
    self._domain_min = domain_min
    self._domain_max = domain_max
    self._range_min = range_min
    self._range_max = range_max

  def __call__(self, domain_values):
    """Transform values from the domain to the range."""
    return (domain_values - self._domain_min) / (self._domain_max - self._domain_min) * (self._range_max - self._range_min) + self._range_min

  def inverse(self, range_values):
    """Transform values from the range to the domain."""
    return (range_values - self._range_min) / (self._range_max - self._range_min) * (self._domain_max - self._domain_min) + self._domain_min

class Log(object):
  def __init__(self, domain_min, domain_max, range_min, range_max, base):
    self._domain_min = domain_min
    self._domain_max = domain_max
    self._range_min = range_min
    self._range_max = range_max
    self._base = base

  def __call__(self, domain_values):
    return (_signed_log(domain_values, self._base) - _signed_log(self._domain_min, self._base)) / (_signed_log(self._domain_max, self._base) - _signed_log(self._domain_min, self._base)) * (self._range_max - self._range_min) + self._range_min

class SymmetricLog(object):
  def __init__(self, domain_min, domain_max, range_min, range_max, base):
    self._domain_min = domain_min
    self._domain_max = domain_max
    self._range_min = range_min
    self._range_max = range_max
    self._base = base

  def __call__(self, domain_values):
    return (_symmetric_log(domain_values, self._base) - _symmetric_log(self._domain_min, self._base)) / (_symmetric_log(self._domain_max, self._base) - _symmetric_log(self._domain_min, self._base)) * (self._range_max - self._range_min) + self._range_min

