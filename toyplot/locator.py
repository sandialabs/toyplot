# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numpy
import toyplot.broadcast


def _log_format(base, exponent, location, format):
    if format is not None:
        return format.format(location, base=base, exponent=exponent)

    exponent_str = "".join(
        [_log_format.superscript[character] for character in str(int(exponent))])
    result = u"%s\u200a%s" % (base, exponent_str)
    return result

_log_format.superscript = {
    "-": u"\u207b\u200a",
    "0": u"\u2070",
    "1": u"\u00b9",
    "2": u"\u00b2",
    "3": u"\u00b3",
    "4": u"\u2074",
    "5": u"\u2075",
    "6": u"\u2076",
    "7": u"\u2077",
    "8": u"\u2078",
    "9": u"\u2079",
}


class TickLocator(object):

    """Base class for tick locators - objects that compute the position and format of axis tick labels."""

    def ticks(self, domain_min, domain_max):
        """Return a set of ticks for the given domain.

        Parameters
        ----------
        domain_min, domain_max: number

        Returns
        -------
        locations : sequence of numbers
          Axis locations where ticks should be displayed.
        labels : sequence of strings
          Labels for each tick location.
        titles : sequence of strings
          Titles for each tick location.  Typically, backends render titles as tooltips.
        """
        raise NotImplementedError()


class Basic(TickLocator):

    """Generate N evenly spaced ticks that include the minimum and maximum values of a domain.

    Parameters
    ----------
    count: number, optional
      Number of ticks to generate.
    format : string, optional
      Format string used to generate labels from tick locations.
    """

    def __init__(self, count=5, format="{:g}"):
        self._count = count
        self._format = format

    def ticks(self, domain_min, domain_max):
        """Return a set of ticks for the given domain.

        Parameters
        ----------
        domain_min, domain_max: number

        Returns
        -------
        locations : sequence of numbers
          The axis locations where ticks should be positioned.
        labels : sequence of strings
          Labels for each tick location.
        titles : sequence of strings
          Titles for each tick location.  Typically, backends render titles as tooltips.
        """
        locations = numpy.linspace(
            domain_min, domain_max, self._count, endpoint=True)
        labels = [self._format.format(location) for location in locations]
        titles = numpy.repeat(None, len(labels))
        return locations, labels, titles


class Explicit(TickLocator):

    """Explicitly specify a collection of tick locations and labels for an axis.

    You must specify the set of locations, the set of labels, or both.  If you
    only specify locations, the labels will be generated using a formatting
    string.  If you only specify labels, the locations will default to integers
    in the range :math:`[0, n)`.  The latter behavior is especially useful for
    categorical axes.

    Parameters
    ----------
    locations : sequence numbers, optional
      Axis locations where ticks should be displayed.
    labels : sequence of strings, optional
      Labels for each tick location.
    titles : sequence of strings, optional
      Titles for each tick location.  Typically, backends render titles as tooltips.
    format : string, optional
      Format string used to generate labels from tick locations.
    """

    def __init__(
            self,
            locations=None,
            labels=None,
            titles=None,
            format="{:g}"):
        if locations is not None and labels is not None:
            locations = numpy.array(locations).astype("float64")
            labels = toyplot.broadcast.string(labels, len(locations))
        elif locations is not None:
            locations = numpy.array(locations).astype("float64")
            labels = [format.format(location) for location in locations]
        elif labels is not None:
            labels = numpy.array(labels).astype("str")
            locations = numpy.arange(len(labels))
        else:
            raise ValueError("Must supply locations, labels, or both.")
        titles = toyplot.broadcast.object(titles, len(locations))

        self._locations = locations
        self._labels = labels
        self._titles = titles

    def ticks(self, domain_min, domain_max):
        """Return a set of ticks for the given domain.

        Parameters
        ----------
        domain_min, domain_max: number

        Returns
        -------
        locations : sequence of numbers
          The axis locations where ticks / labels should be positioned.
        labels : sequence of strings
          Labels for each tick location.
        titles : sequence of strings
          Titles for each tick location.  Typically, backends render titles as tooltips.
        """
        return self._locations, self._labels, self._titles

# An alpha version of the Talbot, Lin, Hanrahan tick mark generator for matplotlib.
# Described in "An Extension of Wilkinson's Algorithm for Positioning Tick Labels on Axes"
# by Justin Talbot, Sharon Lin, and Pat Hanrahan, InfoVis 2010.

# Implementation by Justin Talbot
# This implementation is in the public domain.
# Report bugs to jtalbot@stanford.edu

# A shortcoming:
# The weights used in the paper were designed for static plots where the extent of
# the tick marks unioned with the extent of the data defines the extent of the plot.
# In a plot where the extent of the plot is defined by the user (e.g. an interactive
# plot supporting panning and zooming), the weights don't work as well. In particular,
# you would want to retune them assuming that the tick labels must be inside
# the provided view range. You probably want higher weighting on simplicity and lower
# on coverage and possibly density. But I haven't experimented in any detail with this.
#
# If you do intend on using this for static plots in matplotlib, you should set
# only_inside to False in the call to Extended.extended. And then you should
# manually set your view extent to include the min and max ticks if they are outside
# the data range. This should produce the same results as the paper.


class Extended(TickLocator):

    """Generate ticks using "An Extension of Wilkinson's Algorithm for Positioning Tick Labels on Axes" by Talbot, Lin, and Hanrahan.

    Parameters
    ----------
    count: number, optional
      Desired number of ticks.  Note that the algorithm may produce fewer ticks
      than requested.
    steps: sequence of numbers, optional
      Prioritized list of "nice" values to use for generating ticks.
    only_inside: boolean
      If set to `True`, only ticks inside the axis domain will be generated.
    """

    def __init__(self, count=5, steps=None, weights=None, only_inside=False):
        self._count = count
        self._steps = steps if steps is not None else [1, 5, 2, 2.5, 4, 3]
        self._weights = weigths if weights is not None else [
            0.25, 0.2, 0.5, 0.05]
        self._only_inside = only_inside

    def ticks(self, domain_min, domain_max):
        """Return a set of ticks for the given domain.

        Parameters
        ----------
        domain_min, domain_max: number

        Returns
        -------
        locations : sequence of numbers
          The axis locations where ticks should be positioned.
        labels : sequence of strings
          Labels for each tick location.
        titles : sequence of strings
          Titles for each tick location.  Typically, backends render titles as tooltips.
        """
        def coverage(dmin, dmax, lmin, lmax):
            range = dmax - dmin
            return 1 - 0.5 * (numpy.power(dmax - lmax,
                                          2) + numpy.power(dmin - lmin,
                                                           2)) / numpy.power(0.1 * range,
                                                                             2)

        def coverage_max(dmin, dmax, span):
            range = dmax - dmin
            if span > range:
                half = (span - range) / 2.0
                return 1 - numpy.power(half, 2) / numpy.power(0.1 * range, 2)
            else:
                return 1

        def density(k, m, dmin, dmax, lmin, lmax):
            r = (k - 1.0) / (lmax - lmin)
            rt = (m - 1.0) / (max(lmax, dmax) - min(lmin, dmin))
            return 2 - max(r / rt, rt / r)

        def density_max(k, m):
            if k >= m:
                return 2 - (k - 1.0) / (m - 1.0)
            else:
                return 1

        def simplicity(q, Q, j, lmin, lmax, lstep):
            eps = 1e-10
            n = len(Q)
            i = Q.index(q) + 1
            v = 1 if ((lmin % lstep < eps or (lstep - lmin % lstep)
                       < eps) and lmin <= 0 and lmax >= 0) else 0
            return (n - i) / (n - 1.0) + v - j

        def simplicity_max(q, Q, j):
            n = len(Q)
            i = Q.index(q) + 1
            v = 1
            return (n - i) / (n - 1.0) + v - j

        def legibility(lmin, lmax, lstep):
            return 1

        def legibility_max(lmin, lmax, lstep):
            return 1  # pragma: no cover

        def extended(dmin, dmax, m, Q, only_inside, w):
            n = len(Q)
            best_score = -2.0

            j = 1.0
            while j < float('infinity'):
                for q in Q:
                    sm = simplicity_max(q, Q, j)

                    if w[0] * sm + w[1] + w[2] + w[3] < best_score:
                        j = float('infinity')
                        break

                    k = 2.0
                    while k < float('infinity'):
                        dm = density_max(k, m)

                        if w[0] * sm + w[1] + w[2] * dm + w[3] < best_score:
                            break

                        delta = (dmax - dmin) / (k + 1.0) / j / q
                        z = numpy.ceil(numpy.log10(delta))

                        while z < float('infinity'):
                            step = j * q * numpy.power(10, z)
                            cm = coverage_max(dmin, dmax, step * (k - 1.0))

                            if w[0] * sm + w[1] * cm + \
                                    w[2] * dm + w[3] < best_score:
                                break

                            min_start = numpy.floor(
                                dmax / step) * j - (k - 1.0) * j
                            max_start = numpy.ceil(dmin / step) * j

                            if min_start > max_start:
                                z = z + 1
                                break

                            for start in range(
                                    int(min_start),
                                    int(max_start) + 1):
                                lmin = start * (step / j)
                                lmax = lmin + step * (k - 1.0)
                                lstep = step

                                s = simplicity(q, Q, j, lmin, lmax, lstep)
                                c = coverage(dmin, dmax, lmin, lmax)
                                d = density(k, m, dmin, dmax, lmin, lmax)
                                l = legibility(lmin, lmax, lstep)

                                score = w[0] * s + w[1] * \
                                    c + w[2] * d + w[3] * l

                                if score > best_score and (
                                    not only_inside or (
                                        lmin >= dmin and lmax <= dmax)):
                                    best_score = score
                                    best = (lmin, lmax, lstep, q, k)
                            z = z + 1
                        k = k + 1
                j = j + 1
            return best

        lmin, lmax, lstep, q, k = extended(
            domain_min, domain_max, self._count - 1, self._steps, self._only_inside, self._weights)
        locations = numpy.arange(k) * lstep + lmin
        digits = int(numpy.max(-numpy.floor(numpy.log10(lstep)), 0))
        labels = ["%.*f" % (digits, location) for location in locations]
        titles = numpy.repeat(None, len(labels))
        return locations, labels, titles


class Heckbert(TickLocator):

    """Generate ticks using the "Nice numbers for graph labels" algorithm by Paul Heckbert.

    Note that this locator can produce ticks outside the minimum / maximum axis
    domain.

    Parameters
    ----------
    count: number of ticks to generate
    """

    def __init__(self, count=5):
        self._count = count

    def ticks(self, domain_min, domain_max):
        """Return a set of ticks for the given domain.

        Parameters
        ----------
        domain_min, domain_max: number

        Returns
        -------
        locations : sequence of numbers
          The axis locations where ticks should be positioned.
        labels : sequence of strings
          Labels for each tick location.
        titles : sequence of strings
          Titles for each tick location.  Typically, backends render titles as tooltips.
        """
        def nicenum(x, rounding):
            exponent = numpy.floor(numpy.log10(x))
            fraction = x / numpy.power(10, exponent)
            if rounding:  # pragma: no cover
                if fraction < 1.5:
                    nice_fraction = 1
                elif fraction < 3:
                    nice_fraction = 2
                elif fraction < 7:
                    nice_fraction = 5
                else:
                    nice_fraction = 10
            else:  # pragma: no cover
                if fraction <= 1:
                    nice_fraction = 1
                elif fraction <= 2:
                    nice_fraction = 2
                elif fraction <= 5:
                    nice_fraction = 5
                else:
                    nice_fraction = 10
            return nice_fraction * numpy.power(10, exponent)

        tick_range = nicenum(domain_max - domain_min, rounding=False)
        tick_spacing = nicenum(tick_range / (self._count - 1), rounding=True)
        tick_min = numpy.floor(domain_min / tick_spacing) * tick_spacing
        tick_max = numpy.ceil(domain_max / tick_spacing) * tick_spacing
        locations = numpy.linspace(tick_min, tick_max, self._count)
        digits = int(numpy.max(-numpy.floor(numpy.log10(tick_spacing)), 0))
        labels = ["%.*f" % (digits, location) for location in locations]
        titles = numpy.repeat(None, len(labels))
        return locations, labels, titles


class Integer(TickLocator):

    """Generate evenly-spaced integer ticks

    Parameters
    ----------
    step: integer, optional
      Number of integer values to skip between labels.
    """

    def __init__(self, step=1):
        self._step = step

    def ticks(self, domain_min, domain_max):
        """Return a set of ticks for the given domain.

        Parameters
        ----------
        domain_min, domain_max: number

        Returns
        -------
        locations : sequence of integers
          The axis locations where ticks should be positioned.
        labels : sequence of strings
          Labels for each tick location.
        titles : sequence of strings
          Titles for each tick location.  Typically, backends render titles as tooltips.
        """
        locations = numpy.arange(
            domain_min, domain_max + 1, self._step, dtype="int64")
        labels = [repr(location) for location in locations]
        titles = numpy.repeat(None, len(locations))
        return locations, labels, titles


class Log(TickLocator):

    """Generate ticks that are evenly spaced on a logarithmic scale

    Parameters
    ----------
    base : number, optional
      Logarithm base.
    format : string, optional
      Python format string, see
      `Format String Syntax <https://docs.python.org/2/library/string.html#format-string-syntax>`_
      for the syntax.  The format string will be called with a single positional
      argument containing the locator value, and two keyword arguments `base`
      and `exponent`.  If omitted, the locator will generate high-quality
      labels using superscript notation.

    Examples
    --------

    Generate locator labels using fixed decimal point notation and two significant digits:

    >>> locator = toyplot.locator.Log(format="{:.2g}")

    Generate locator labels using scientific notation and three significant digits:

    >>> locator = toyplot.locator.Log(format="{:.3e}")

    Generate locator labels using mixed scientific and decimal notation and four significant digits:

    >>> locator = toyplot.locator.Log(format="{:.4g}")

    Generate locator labels using "carat" notation:

    >>> locator = toyplot.locator.Log(format="{base}^{exponent}")

    """

    def __init__(self, base=10, format=None):
        self._base = base
        self._format = format

    def ticks(self, domain_min, domain_max):
        """Return a set of ticks for the given domain.

        Parameters
        ----------
        domain_min, domain_max: number

        Returns
        -------
        locations : sequence of numbers
          The axis locations where ticks should be positioned.
        labels : sequence of strings
          Labels for each tick location.
        titles : sequence of strings
          Titles for each tick location.  Typically, backends render titles as tooltips.
        """
        if domain_min < 0 and domain_max < 0:
            negative_exponents = numpy.arange(
                numpy.ceil(
                    numpy.log10(
                        numpy.abs(domain_min)) / numpy.log10(
                        self._base)), numpy.floor(
                    numpy.log10(
                        numpy.abs(domain_max)) / numpy.log10(
                            self._base)) - 1, -1)
        elif domain_min < 0:
            negative_exponents = numpy.arange(
                numpy.ceil(numpy.log10(numpy.abs(domain_min)) / numpy.log10(self._base)), -1, -1)
        else:
            negative_exponents = []
        negative_locations = -numpy.power(self._base, negative_exponents)

        if domain_max == 0 or domain_min == 0 or domain_min < 0 and domain_max > 0:
            linear_locations = [0]
        else:
            linear_locations = []

        if domain_min > 0 and domain_max > 0:
            positive_exponents = numpy.arange(
                numpy.floor(
                    numpy.log10(domain_min) /
                    numpy.log10(
                        self._base)),
                numpy.ceil(
                    numpy.log10(domain_max) /
                    numpy.log10(
                        self._base)) +
                1)
        elif domain_max > 0:
            positive_exponents = numpy.arange(
                0,
                numpy.ceil(
                    numpy.log10(domain_max) /
                    numpy.log10(
                        self._base)) +
                1) if domain_max != 0 else []
        else:
            positive_exponents = []
        positive_locations = numpy.power(self._base, positive_exponents)

        # print domain_min, negative_exponents, linear_locations,
        # positive_exponents, domain_max

        negative_labels = [
            "-" +
            _log_format(
                self._base,
                int(exponent),
                location,
                self._format) for exponent,
            location in zip(
                negative_exponents,
                negative_locations)]
        linear_labels = [str(location) for location in linear_locations]
        positive_labels = [
            _log_format(
                self._base,
                int(exponent),
                location,
                self._format) for exponent,
            location in zip(
                positive_exponents,
                positive_locations)]

        locations = numpy.concatenate(
            (negative_locations, linear_locations, positive_locations))
        labels = negative_labels + linear_labels + positive_labels
        titles = numpy.repeat(None, len(labels))
        return locations, labels, titles
