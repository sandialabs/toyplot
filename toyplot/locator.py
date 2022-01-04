# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Strategy objects that compute the position and format of axis ticks and labels."""


import datetime

try:
    import arrow
except: # pragma: no cover
    pass
import custom_inherit
import numpy

import toyplot.broadcast


class TickLocator(object, metaclass=custom_inherit.DocInheritMeta(style="numpy_napoleon")):
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
        raise NotImplementedError() # pragma: no cover


class Null(TickLocator):
    """Do-nothing tick locator that generates no ticks.

    Use :class:`toyplot.locator.Null` when you want to display an axis, but
    omit any ticks.
    """
    def ticks(self, domain_min, domain_max):
        return [], [], []


class Uniform(TickLocator):
    """Generate :math:`N` evenly spaced ticks that include the minimum and maximum values of a domain.

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
            labels = numpy.array(labels).astype("unicode")
            if len(locations) != len(labels):
                raise ValueError("Location and label counts must match.") # pragma: no cover
        elif locations is not None:
            locations = numpy.array(locations).astype("float64")
            labels = [format.format(location) for location in locations]
        elif labels is not None:
            labels = numpy.array(labels).astype("str")
            locations = numpy.arange(len(labels))
        else:
            raise ValueError("Must supply locations, labels, or both.") # pragma: no cover
        titles = toyplot.broadcast.pyobject(titles, len(locations))

        self._locations = locations
        self._labels = labels
        self._titles = titles

    def ticks(self, domain_min, domain_max):
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
    format : string, optional
      Format string used to generate labels from tick locations.
    """
    def __init__(self, count=5, steps=None, weights=None, only_inside=False, format="{0:.{digits}f}"):
        self._count = count
        self._steps = steps if steps is not None else [1, 5, 2, 2.5, 4, 3]
        self._weights = weights if weights is not None else [0.25, 0.2, 0.5, 0.05]
        self._only_inside = only_inside
        self._format = format

    def ticks(self, domain_min, domain_max):
        def coverage(dmin, dmax, lmin, lmax):
            range_ = dmax - dmin
            return 1 - 0.5 * (numpy.power(dmax - lmax,
                                          2) + numpy.power(dmin - lmin,
                                                           2)) / numpy.power(0.1 * range_,
                                                                             2)

        def coverage_max(dmin, dmax, span):
            range_ = dmax - dmin
            if span > range_:
                half = (span - range_) / 2.0
                return 1 - numpy.power(half, 2) / numpy.power(0.1 * range_, 2)
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

                                if score > best_score and (not only_inside or (lmin >= dmin and lmax <= dmax)):
                                    best_score = score
                                    best = (lmin, lmax, lstep, q, k)
                            z = z + 1
                        k = k + 1
                j = j + 1
            return best

        lmin, lmax, lstep, q, k = extended(
            domain_min, domain_max, self._count - 1, self._steps, self._only_inside, self._weights)
        locations = numpy.arange(k) * lstep + lmin
        digits = max(0, int(numpy.max(-numpy.floor(numpy.log10(lstep)), 0)))
        labels = [self._format.format(location, digits=digits) for location in locations]
        titles = numpy.repeat(None, len(labels))
        return locations, labels, titles


class Heckbert(TickLocator):
    """Generate ticks using the "Nice numbers for graph labels" algorithm by Paul Heckbert.

    Note that this locator can produce ticks outside the minimum / maximum axis
    domain.

    Parameters
    ----------
    count: number of ticks to generate
    format : string, optional
      Format string used to generate labels from tick locations.
    """
    def __init__(self, count=5, format="{0:.{digits}f}"):
        self._count = count
        self._format = format

    def ticks(self, domain_min, domain_max):
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
        digits = max(0, int(numpy.max(-numpy.floor(numpy.log10(tick_spacing)), 0)))
        labels = [self._format.format(location, digits=digits) for location in locations]
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
    def __init__(self, base=10, format="{base}<sup> {exponent}</sup>"):
        self._base = base
        self._format = format

    def ticks(self, domain_min, domain_max):
        if domain_min < 0 and domain_max < 0:
            negative_exponents = numpy.arange(
                numpy.ceil(numpy.log10(numpy.abs(domain_min)) / numpy.log10(self._base)),
                numpy.floor(numpy.log10(numpy.abs(domain_max)) / numpy.log10(self._base)) - 1, -1)
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

        negative_labels = []
        for exponent, location in zip(negative_exponents, negative_locations):
            negative_labels.append(
                "-" + self._format.format(location, base=self._base, exponent=int(exponent))
                )

        linear_labels = [str(location) for location in linear_locations]

        positive_labels = []
        for exponent, location in zip(positive_exponents, positive_locations):
            positive_labels.append(
                self._format.format(location, base=self._base, exponent=int(exponent))
                )

        locations = numpy.concatenate(
            (negative_locations, linear_locations, positive_locations))
        labels = negative_labels + linear_labels + positive_labels
        titles = numpy.repeat(None, len(labels))
        return locations, labels, titles


def _year_generator(years):
    def implementation(domain_min, domain_max, timezone):
        start = domain_min.to(timezone)
        end = domain_max.to(timezone)
        for year in numpy.arange(start.year - (start.year % years), end.year + 1, years):
            value = arrow.Arrow(year=year, month=1, day=1, tzinfo=timezone)
            if value >= domain_min and value <= domain_max:
                yield value.timestamp()
    return implementation


def _month_generator(months):
    def implementation(domain_min, domain_max, timezone):
        start = domain_min.to(timezone)
        end = domain_max.to(timezone)
        for year in numpy.arange(start.year, end.year + 1):
            for month in numpy.arange(0, 12, months):
                value = arrow.Arrow(year=year, month=month + 1, day=1, tzinfo=timezone)
                if value >= domain_min and value <= domain_max:
                    yield value.timestamp()
    return implementation


def _day_generator(days):
    def implementation(domain_min, domain_max, timezone):
        start = domain_min.to(timezone)
        value = arrow.Arrow(year=start.year, month=start.month, day=start.day, tzinfo=timezone)
        while value <= domain_max:
            if value >= domain_min:
                yield value.timestamp()
            value += datetime.timedelta(days=days)
    return implementation


def _hour_generator(hours):
    def implementation(domain_min, domain_max, timezone):
        start = domain_min.to(timezone)
        value = arrow.Arrow(year=start.year, month=start.month, day=start.day, tzinfo=timezone)
        while value <= domain_max:
            if value >= domain_min:
                yield value.timestamp()
            value += datetime.timedelta(hours=hours)
    return implementation


def _minute_generator(minutes):
    def implementation(domain_min, domain_max, timezone):
        start = domain_min.to(timezone)
        value = arrow.Arrow(year=start.year, month=start.month, day=start.day, tzinfo=timezone)
        while value <= domain_max:
            if value >= domain_min:
                yield value.timestamp()
            value += datetime.timedelta(minutes=minutes)
    return implementation


def _second_generator(seconds):
    def implementation(domain_min, domain_max, timezone):
        start = domain_min.to(timezone)
        value = arrow.Arrow(year=start.year, month=start.month, day=start.day, tzinfo=timezone)
        while value <= domain_max:
            if value >= domain_min:
                yield value.timestamp()
            value += datetime.timedelta(seconds=seconds)
    return implementation


_intervals = [
    dict(duration=datetime.timedelta(days=365 * 1000), generator=_year_generator(1000), format="{0:YYYY}"),
    dict(duration=datetime.timedelta(days=365 * 100), generator=_year_generator(100), format="{0:YYYY}"),
    dict(duration=datetime.timedelta(days=365 * 10), generator=_year_generator(10), format="{0:YYYY}"),
    dict(duration=datetime.timedelta(days=365 * 5), generator=_year_generator(5), format="{0:YYYY}"),
    dict(duration=datetime.timedelta(days=365), generator=_year_generator(1), format="{0:YYYY}"),
    dict(duration=datetime.timedelta(days=90), generator=_month_generator(3), format="{0:MMMM} {0:YYYY}"),
    dict(duration=datetime.timedelta(days=30), generator=_month_generator(1), format="{0:MMMM} {0:YYYY}"),
    dict(duration=datetime.timedelta(days=7), generator=_day_generator(7), format="{0:ddd}, {0:MMM} {0:D}, {0:YYYY}"),
    dict(duration=datetime.timedelta(days=1), generator=_day_generator(1), format="{0:ddd}, {0:MMM} {0:D}"),
    dict(duration=datetime.timedelta(hours=12), generator=_hour_generator(12), format="{0:M}/{0:D} {0:HH}:{0:mm}"),
    dict(duration=datetime.timedelta(hours=6), generator=_hour_generator(6), format="{0:M}/{0:D} {0:HH}:{0:mm}"),
    dict(duration=datetime.timedelta(hours=4), generator=_hour_generator(4), format="{0:M}/{0:D} {0:HH}:{0:mm}"),
    dict(duration=datetime.timedelta(hours=1), generator=_hour_generator(1), format="{0:M}/{0:D} {0:HH}:{0:mm}"),
    dict(duration=datetime.timedelta(minutes=15), generator=_minute_generator(15), format="{0:M}/{0:D} {0:HH}:{0:mm}"),
    dict(duration=datetime.timedelta(minutes=10), generator=_minute_generator(10), format="{0:M}/{0:D} {0:HH}:{0:mm}"),
    dict(duration=datetime.timedelta(minutes=5), generator=_minute_generator(5), format="{0:M}/{0:D} {0:HH}:{0:mm}"),
    dict(duration=datetime.timedelta(minutes=1), generator=_minute_generator(1), format="{0:M}/{0:D} {0:HH}:{0:mm}"),
    dict(duration=datetime.timedelta(seconds=15), generator=_second_generator(15), format="{0:HH}:{0:mm}:{0:ss}"),
    dict(duration=datetime.timedelta(seconds=10), generator=_second_generator(10), format="{0:HH}:{0:mm}:{0:ss}"),
    dict(duration=datetime.timedelta(seconds=5), generator=_second_generator(5), format="{0:HH}:{0:mm}:{0:ss}"),
    dict(duration=datetime.timedelta(seconds=1), generator=_second_generator(1), format="{0:HH}:{0:mm}:{0:ss}"),
    ]


class Timestamp(TickLocator):
    """Generate ticks when the domain is UTC timestamps relative to the Unix epoch.

    Callers may explicitly specify the desired time interval as a string:

    >>> toyplot.locator.Timestamp(interval="hours")

    or as a tuple containing a quantity of units:

    >>> toyplot.locator.Timestamp(interval=(3, "days"))

    Instead of specifying an interval, the caller may supply the desired number
    of ticks, and the interval that produces the closest number of ticks will
    be used (note that the number of ticks produced may not match exactly):

    >>> toyplot.locator.Timestamp(count=4)

    If the count is not specified, it defaults to `7`.

    Parameters
    ----------
    count: number, optional
        Specifies the desired number of ticks.
    interval: string or (integer, string) tuple, optional
        Specifies the desired tick interval in anthropomorphic time units.
        Allowed units are "millenium", "millenia", "century", "centuries",
        "decade", "decades", "year", "years", "quarter", "quarters", "month",
        "months", "week", "weeks", "day", "days", "hour", "hours", "minute",
        "minutes", "second", and "seconds".
    timezone: string, optional
        Specifies a local timezone to be used for label generation.  Defaults
        to "utc".  Supports any timezone code allowed by :class:`arrow.arrow.Arrow`.
    format: string, optional
        Format string used to generate labels from tick locations.  The
        formatted value will be a :class:`arrow.arrow.Arrow` object, so any of the
        attributes and formatting provided by https://arrow.readthedocs.org may
        be used in the format.  For example, to display the full day of the
        week, month, day of the month without zero padding, and year, you could
        use:

    >>> toyplot.locator.Timestamp(format="{0:dddd}, {0:MMMM} {0:D}, {0:YYYY}")
    """
    def __init__(self, count=None, interval=None, timezone="utc", format=None):
        if interval is not None:
            if isinstance(interval, str):
                interval = (1, interval)
            interval = (int(interval[0]), interval[1].lower())

            amount, units = interval

            if units in ["millenium", "millenia"]:
                interval = dict(duration=datetime.timedelta(days=365 * 1000 * amount), generator=_year_generator(1000 * amount), format="{0:YYYY}")
            elif units in ["century", "centuries"]:
                interval = dict(duration=datetime.timedelta(days=365 * 100 * amount), generator=_year_generator(100 * amount), format="{0:YYYY}")
            elif units in ["decade", "decades"]:
                interval = dict(duration=datetime.timedelta(days=365 * 10 * amount), generator=_year_generator(10 * amount), format="{0:YYYY}")
            elif units in ["year", "years"]:
                interval = dict(duration=datetime.timedelta(days=365 * amount), generator=_year_generator(amount), format="{0:YYYY}")
            elif units in ["quarter", "quarters"]:
                interval = dict(duration=datetime.timedelta(days=90 * amount), generator=_month_generator(3 * amount), format="{0:MMMM} {0:YYYY}")
            elif units in ["month", "months"]:
                interval = dict(duration=datetime.timedelta(days=30 * amount), generator=_month_generator(amount), format="{0:MMMM} {0:YYYY}")
            elif units in ["week", "weeks"]:
                interval = dict(duration=datetime.timedelta(days=7 * amount), generator=_day_generator(7 * amount), format="{0:ddd}, {0:MMM} {0:D}, {0.year}")
            elif units in ["day", "days"]:
                interval = dict(duration=datetime.timedelta(days=amount), generator=_day_generator(amount), format="{0:ddd}, {0:MMM} {0:D}")
            elif units in ["hour", "hours"]:
                interval = dict(duration=datetime.timedelta(hours=amount), generator=_hour_generator(amount), format="{0:M}/{0:D} {0:HH}:{0:mm}")
            elif units in ["minute", "minutes"]:
                interval = dict(duration=datetime.timedelta(minutes=amount), generator=_minute_generator(amount), format="{0:M}/{0:D} {0:HH}:{0:mm}")
            elif units in ["second", "seconds"]:
                interval = dict(duration=datetime.timedelta(seconds=amount), generator=_second_generator(amount), format="{0:HH}:{0:mm}:{0:ss}")

        self._count = count
        self._interval = interval
        self._timezone = timezone
        self._format = format

    def ticks(self, domain_min, domain_max):
        interval = self._interval

        # If the caller didn't specify an interval, find one that yields the number of locations closest to the requested count
        if interval is None:
            if self._count is None:
                self._count = 7

            closest_difference = None

            for match in _intervals:
                count = (domain_max - domain_min) / match["duration"].total_seconds()
                difference = numpy.abs(self._count - count)

                if (closest_difference is None) or (difference < closest_difference):
                    interval = match
                    closest_difference = difference

        # Generate ticks
        generator = interval["generator"]
        label_format = interval["format"] if self._format is None else self._format

        locations = [location for location in generator(arrow.get(domain_min), arrow.get(domain_max), self._timezone)]
        labels = [label_format.format(arrow.get(location).to(self._timezone)) for location in locations]
        titles = numpy.repeat(None, len(labels))
        return locations, labels, titles
