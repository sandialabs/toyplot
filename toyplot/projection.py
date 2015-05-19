# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numpy

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

