# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Classes and functions for projecting coordinates between spaces."""


import custom_inherit
import numpy


def _mix(a, b, amount):
    return ((1.0 - amount) * a) + (amount * b)


def _log(x, base):
    return numpy.log10(numpy.abs(x)) / numpy.log10(base)


def _in_range(a, x, b):
    left = min(a, b)
    right = max(a, b)
    old_settings = numpy.seterr(invalid="ignore")
    result = numpy.logical_and(left <= x, x <= right)
    numpy.seterr(**old_settings)
    return result


class Projection(object, metaclass=custom_inherit.DocInheritMeta(style="numpy_napoleon")):
    """Abstract interface for objects that can map between one-dimensional domain and range spaces.

    .. automethod:: __call__
    """
    def __call__(self, domain_values):
        """Map domain values to range values.

        Parameters
        ----------
        domain_values: :class:`numpy.ndarray` or compatible.
            The domain values to convert.

        Returns
        -------
        range_values: :class:`numpy.ndarray`
            The domain values projected into range values.

        Examples
        --------

        >>> projection = toyplot.projection.linear(0, 1, -1, 1)
        >>> projection(0.75)
        0.5
        """
        raise NotImplementedError() # pragma: no cover

    def inverse(self, range_values):
        """Map range values to domain values.

        Parameters
        ----------
        range_values: :class:`numpy.ndarray` or compatible.
            The range values to convert.

        Returns
        -------
        domain_values: :class:`numpy.ndarray`
            The range values projected into domain values.

        Examples
        --------

        >>> projection = toyplot.projection.linear(0, 1, -1, 1)
        >>> projection.inverse(-0.5)
        0.25
        """
        raise NotImplementedError() # pragma: no cover


class Piecewise(Projection):
    """Projects between domain and range data using a piecewise collection of linear and log segments.

    Parameters
    ----------
    segments: sequence of :class:`toyplot.projection.Piecewise.Segment` objects, required
        Callers must supply one-to-many segments, each of which defines a
        mapping between bounded, non-overlapping regions of the domain
        and range spaces.

    .. automethod:: __call__
    """
    class Segment(object):
        """Defines a mapping between bounded regions of domain-space and range-space.

        Parameters
        ----------
        scale: "linear" or ("log", base) tuple, required

        domain_bounds_min, domain_bounds_max: number, required
            These values define the bounds of this segment in domain space, and
            may include positive or negative infinity.

        domain_min, domain_max: number, required
            These values are mapped to `range_min` and `range_max`, respectively.

        range_min, range_max: number, required
            These values are mapped to `domain_min` and `domain_max`, respectively.

        range_bounds_min, range_bounds_max: number, required
            These values define the bounds of this segment in range space, and
            may include positive or negative infinity.
        """
        class _Container(object):
            pass

        def __init__(
                self,
                scale,
                domain_bounds_min,
                domain_min,
                domain_max,
                domain_bounds_max,
                range_bounds_min,
                range_min,
                range_max,
                range_bounds_max,
            ):
            self.scale = scale
            self.domain = Piecewise.Segment._Container()
            self.domain.bounds = Piecewise.Segment._Container()
            self.domain.bounds.min = domain_bounds_min
            self.domain.min = domain_min
            self.domain.max = domain_max
            self.domain.bounds.max = domain_bounds_max
            self.range = Piecewise.Segment._Container()
            self.range.bounds = Piecewise.Segment._Container()
            self.range.bounds.min = range_bounds_min
            self.range.min = range_min
            self.range.max = range_max
            self.range.bounds.max = range_bounds_max

    def __init__(self, segments):
        self._segments = segments

    def __call__(self, domain_values):
        domain_values = numpy.ma.array(domain_values, dtype="float64")
        range_values = numpy.empty_like(domain_values)
        for segment in self._segments:
            indices = _in_range(
                segment.domain.bounds.min,
                domain_values,
                segment.domain.bounds.max)
            if segment.scale == "linear":
                amount = (domain_values[indices] - segment.domain.min) / (segment.domain.max - segment.domain.min)
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
            range_values = range_values.item()
        return range_values

    def inverse(self, range_values):
        range_values = numpy.ma.array(range_values, dtype="float64")
        domain_values = numpy.empty_like(range_values)
        for segment in self._segments:
            indices = _in_range(
                segment.range.bounds.min,
                range_values,
                segment.range.bounds.max)
            if segment.scale == "linear":
                amount = (range_values[indices] - segment.range.min) / (segment.range.max - segment.range.min)
                domain_values[indices] = _mix(
                    segment.domain.min, segment.domain.max, amount)
            else:
                scale, base = segment.scale
                if scale == "log":
                    amount = (range_values[indices] - segment.range.min) / (segment.range.max - segment.range.min)
                    domain_values[indices] = numpy.sign(
                        segment.domain.min) * numpy.power(base, _mix(
                            _log(segment.domain.min, base),
                            _log(segment.domain.max, base),
                            amount))
                else:
                    raise Exception("Unknown scale: %s" % (scale,)) # pragma: no cover

        if domain_values.shape == ():
            domain_values = domain_values.item()
        return domain_values


def linear(domain_min, domain_max, range_min, range_max):
    """Return an instance of :class:`toyplot.projection.Piecewise` that performs a linear projection.

    Parameters
    -----------
    domain_min, domain_max : number
        Defines a closed interval of domain values that will be mapped to the range.
    range_min, range_max : number
        Defines a closed interval of range values that will be mapped to the domain.

    Returns
    -------
    projection : :class:`toyplot.projection.Piecewise`
    """

    return Piecewise([
        Piecewise.Segment(
            "linear",
            -numpy.inf,
            domain_min,
            domain_max,
            numpy.inf,
            -numpy.inf,
            range_min,
            range_max,
            numpy.inf,
            ),
        ])


def log(
        base,
        domain_min,
        domain_max,
        range_min,
        range_max,
        linear_domain_min=-1,
        linear_domain_max=1,
    ):
    """Return an instance of :class:`toyplot.projection.Piecewise` that performs a log projection.

    The returned projection will work correctly with both positive, negative,
    and zero domain values.  To support mapping zero, the projection will
    switch from log projection to a linear projection within a user-defined
    region around the origin.

    Parameters
    -----------
    base : number
        Logarithmic base used to map from domain values to range values.
    domain_min, domain_max : number
        Defines a closed interval of domain values that will be mapped to the range.
    range_min, range_max : number
        Defines a closed interval of range values that will be mapped to the domain.
    linear_domain_min, linear_domain_max : number, optional
        Defines an interval of domain values around the origin that will be mapped linearly.

    Returns
    -------
    projection : :class:`toyplot.projection.Piecewise`
    """

    # Domain is all positive.
    if 0 < domain_min:
        return Piecewise([
            Piecewise.Segment(
                "linear",
                -numpy.inf,
                domain_min - (domain_max - domain_min),
                domain_min,
                domain_min,
                -numpy.inf,
                range_min - (range_max - range_min),
                range_min,
                range_min,
                ),
            Piecewise.Segment(
                ("log", base),
                domain_min,
                domain_min,
                domain_max,
                numpy.inf,
                range_min,
                range_min,
                range_max,
                numpy.inf,
                ),
            ])

    # Domain is all negative.
    if domain_max < 0:
        return Piecewise([
            Piecewise.Segment(
                ("log", base),
                -numpy.inf,
                domain_min,
                domain_max,
                domain_max,
                -numpy.inf,
                range_min,
                range_max,
                range_max,
                ),
            Piecewise.Segment(
                "linear",
                domain_max,
                domain_max,
                domain_max + (domain_max - domain_min),
                numpy.inf,
                range_max,
                range_max,
                range_max + (range_max - range_min),
                numpy.inf,
                ),
            ])

    # Mixed negative / positive domain
    if domain_min < linear_domain_min and linear_domain_max < domain_max:
        linear_range_min = _mix(range_min, range_max, 0.4)
        linear_range_max = _mix(range_min, range_max, 0.6)
        return Piecewise([
            Piecewise.Segment(
                ("log", base),
                -numpy.inf,
                domain_min,
                linear_domain_min,
                linear_domain_min,
                -numpy.inf,
                range_min,
                linear_range_min,
                linear_range_min,
                ),
            Piecewise.Segment(
                "linear",
                linear_domain_min,
                linear_domain_min,
                linear_domain_max,
                linear_domain_max,
                linear_range_min,
                linear_range_min,
                linear_range_max,
                linear_range_max,
                ),
            Piecewise.Segment(
                ("log", base),
                linear_domain_max,
                linear_domain_max,
                domain_max,
                numpy.inf,
                linear_range_max,
                linear_range_max,
                range_max,
                numpy.inf,
                ),
            ])

    if domain_min < linear_domain_min:
        linear_range_min = _mix(range_min, range_max, 0.8)
        return Piecewise([
            Piecewise.Segment(
                ("log", base),
                -numpy.inf,
                domain_min,
                linear_domain_min,
                linear_domain_min,
                -numpy.inf,
                range_min,
                linear_range_min,
                linear_range_min,
                ),
            Piecewise.Segment(
                "linear",
                linear_domain_min,
                linear_domain_min,
                linear_domain_max,
                numpy.inf,
                linear_range_min,
                linear_range_min,
                range_max,
                numpy.inf,
                ),
            ])

    if linear_domain_max < domain_max:
        linear_range_max = _mix(range_min, range_max, 0.2)
        return Piecewise([
            Piecewise.Segment(
                "linear",
                -numpy.inf,
                domain_min,
                linear_domain_max,
                linear_domain_max,
                -numpy.inf,
                range_min,
                linear_range_max,
                linear_range_max,
                ),
            Piecewise.Segment(
                ("log", base),
                linear_domain_max,
                linear_domain_max,
                domain_max,
                numpy.inf,
                linear_range_max,
                linear_range_max,
                range_max,
                numpy.inf,
                ),
            ])

    return Piecewise([
        Piecewise.Segment(
            "linear",
            -numpy.inf,
            domain_min,
            domain_max,
            numpy.inf,
            -numpy.inf,
            range_min,
            range_max,
            numpy.inf),
        ])
