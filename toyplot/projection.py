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

    class Segment(object):

        class Container(object):
            pass

        def __init__(
                self,
                scale,
                domain_min,
                domain_max,
                range_min,
                range_max,
                domain_bounds_min,
                domain_bounds_max,
                range_bounds_min,
                range_bounds_max):
            self.scale = scale
            self.domain = Piecewise.Segment.Container()
            self.domain.min = domain_min
            self.domain.max = domain_max
            self.domain.bounds = Piecewise.Segment.Container()
            self.domain.bounds.min = domain_bounds_min
            self.domain.bounds.max = domain_bounds_max
            self.range = Piecewise.Segment.Container()
            self.range.min = range_min
            self.range.max = range_max
            self.range.bounds = Piecewise.Segment.Container()
            self.range.bounds.min = range_bounds_min
            self.range.bounds.max = range_bounds_max

    def __init__(self, segments):
        self._segments = segments

    def __call__(self, domain_values):
        """Transform values from the domain to the range."""
        domain_values = numpy.ma.array(domain_values, dtype="float64")
        range_values = numpy.empty_like(domain_values)
        for segment in self._segments:
            indices = _in_range(
                segment.domain.bounds.min,
                domain_values,
                segment.domain.bounds.max)
            if segment.scale == "linear":
                amount = (domain_values[
                          indices] - segment.domain.min) / (segment.domain.max - segment.domain.min)
                range_values[indices] = _mix(
                    segment.range.min, segment.range.max, amount)
            else:
                scale, base = segment.scale
                if scale == "log":
                    amount = (_log(domain_values[indices],
                                   base) - _log(segment.domain.min,
                                                base)) / (_log(segment.domain.max,
                                                               base) - _log(segment.domain.min,
                                                                            base))
                    range_values[indices] = _mix(
                        segment.range.min, segment.range.max, amount)
                else:
                    raise Exception("Unknown scale: %s" % (scale,)) # pragma: no cover

        if range_values.shape == ():
            range_values = numpy.asscalar(range_values)
        return range_values

    def inverse(self, range_values):
        """Transform values from the range to the domain."""
        range_values = numpy.ma.array(range_values, dtype="float64")
        domain_values = numpy.empty_like(range_values)
        for segment in self._segments:
            indices = _in_range(
                segment.range.bounds.min,
                range_values,
                segment.range.bounds.max)
            if segment.scale == "linear":
                amount = (range_values[
                          indices] - segment.range.min) / (segment.range.max - segment.range.min)
                domain_values[indices] = _mix(
                    segment.domain.min, segment.domain.max, amount)
            else:
                scale, base = segment.scale
                if scale == "log":
                    amount = (range_values[
                              indices] - segment.range.min) / (segment.range.max - segment.range.min)
                    domain_values[indices] = numpy.sign(
                        segment.domain.min) * numpy.power(
                        base, _mix(
                            _log(
                                segment.domain.min, base), _log(
                                segment.domain.max, base), amount))
                else:
                    raise Exception("Unknown scale: %s" % (scale,)) # pragma: no cover

        if domain_values.shape == ():
            domain_values = numpy.asscalar(domain_values)
        return domain_values


def linear(domain_min, domain_max, range_min, range_max):
    return Piecewise([
        Piecewise.Segment("linear", domain_min, domain_max, range_min,
                          range_max, -numpy.inf, numpy.inf, -numpy.inf, numpy.inf),
    ])


def log(
        base,
        domain_min,
        domain_max,
        range_min,
        range_max,
        linear_domain_min=-1,
        linear_domain_max=1):
    # Negative domain
    if domain_max < 0:
        return Piecewise([
            Piecewise.Segment(("log", base), domain_min, domain_max, range_min,
                              range_max, -numpy.inf, numpy.inf, -numpy.inf, numpy.inf),
        ])

    # Positive domain
    if 0 < domain_min:
        return Piecewise([
            Piecewise.Segment(("log", base), domain_min, domain_max, range_min,
                              range_max, -numpy.inf, numpy.inf, -numpy.inf, numpy.inf),
        ])

    # Mixed negative / positive domain
    if domain_min < linear_domain_min and linear_domain_max < domain_max:
        linear_range_min = _mix(range_min, range_max, 0.4)
        linear_range_max = _mix(range_min, range_max, 0.6)
        return Piecewise([
            Piecewise.Segment(("log", base), domain_min, linear_domain_min, range_min,
                              linear_range_min, -numpy.inf, linear_domain_min, -numpy.inf, linear_range_min),
            Piecewise.Segment("linear", linear_domain_min, linear_domain_max, linear_range_min,
                              linear_range_max, linear_domain_min, linear_domain_max, linear_range_min, linear_range_max),
            Piecewise.Segment(("log", base), linear_domain_max, domain_max, linear_range_max,
                              range_max, linear_domain_max, numpy.inf, linear_range_max, numpy.inf),
        ])

    if domain_min < linear_domain_min:
        linear_range_min = _mix(range_min, range_max, 0.8)
        return Piecewise([
            Piecewise.Segment(("log", base), domain_min, linear_domain_min, range_min,
                              linear_range_min, -numpy.inf, linear_domain_min, -numpy.inf, linear_range_min),
            Piecewise.Segment("linear", linear_domain_min, linear_domain_max, linear_range_min,
                              range_max, linear_domain_min, numpy.inf, linear_range_min, numpy.inf),
        ])

    if linear_domain_max < domain_max:
        linear_range_max = _mix(range_min, range_max, 0.2)
        return Piecewise([
            Piecewise.Segment("linear", domain_min, linear_domain_max, range_min,
                              linear_range_max, -numpy.inf, linear_domain_max, -numpy.inf, linear_range_max),
            Piecewise.Segment(("log", base), linear_domain_max, domain_max, linear_range_max,
                              range_max, linear_domain_max, numpy.inf, linear_range_max, numpy.inf),
        ])

    return Piecewise([
        Piecewise.Segment("linear", domain_min, domain_max, range_min,
                          range_max, -numpy.inf, numpy.inf, -numpy.inf, numpy.inf),
    ])
