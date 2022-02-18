# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functionality for managing colors, palettes, and color maps."""


import collections
import colorsys
import re
import xml.etree.ElementTree as xml

import custom_inherit
import numpy

import toyplot.projection


black = "#292724"
"""Default color used throughout Toyplot figures."""

dtype = {"names": ["r", "g", "b", "a"], "formats": ["float64", "float64", "float64", "float64"]}
"""Data type for storing RGBA color information in :class:`numpy.ndarray` instances.
"""


def _html_color_swatches(colors, css_class, margin=0):
    root_xml = xml.Element(
        "div",
        style="overflow:hidden; height:auto",
        attrib={"class": css_class})
    for color in colors:
        xml.SubElement(
            root_xml,
            "div",
            style="float:left;width:20px;height:20px;margin-right:%spx;background-color:%s" % (margin, to_css(color)))
    return xml.tostring(root_xml, encoding="unicode", method="html")


def _jupyter_color_swatches(colors):
    if isinstance(colors, numpy.ndarray) and colors.shape == () and colors.dtype == dtype:
        return _html_color_swatches([colors], "toyplot-color-Swatch")
    elif isinstance(colors, numpy.ndarray) and colors.ndim == 1 and colors.dtype == dtype:
        return _html_color_swatches(colors, "toyplot-color-Swatches", margin=5)
    return None # pragma: no cover


try: # pragma: no cover
    import IPython # pylint: disable=wrong-import-position,wrong-import-order
    ip = IPython.get_ipython()
    html_formatter = ip.display_formatter.formatters['text/html']
    html_formatter.for_type_by_name('numpy', 'ndarray', _jupyter_color_swatches)
except:
    pass


def lab(l, a, b):
    """Construct a Toyplot color from CIE Lab values."""
    y = (l + 16.0) / 116.0
    x = a / 500.0 + y
    z = y - b / 200.0

    x3 = x * x * x
    z3 = z * z * z
    return xyz(
        lab.white[0] * (x3 if x3 > lab.epsilon else (x - 16.0 / 116.0) / 7.787),
        lab.white[1] * (numpy.power(((l + 16.0) / 116.0), 3) if l > (lab.kappa * lab.epsilon) else l / lab.kappa),
        lab.white[2] * (z3 if z3 > lab.epsilon else (z - 16.0 / 116.0) / 7.787),
        )
lab.epsilon = 216.0 / 24389.0
lab.kappa = 24389.0 / 27.0
lab.white = numpy.array([95.047, 100.0, 108.883])


def rgb(r, g, b):
    """Construct a Toyplot color from RGB values.

    Returns
    -------
    color: :class:`numpy.ndarray` scalar containing RGBA values with dtype = :data:`toyplot.color.dtype`.
    """
    return numpy.array((r, g, b, 1.0), dtype=dtype)


def rgba(r, g, b, a):
    """Construct a Toyplot color from RGBA values.

    Returns
    -------
    color: :class:`numpy.ndarray` scalar containing RGBA values with dtype = :data:`toyplot.color.dtype`.
    """
    return numpy.array((r, g, b, a), dtype=dtype)


def xyz(x, y, z):
    """Construct a Toyplot color from CIE XYZ values, using observer = 2 deg and illuminant = D65."""
    x = x / 100.0
    y = y / 100.0
    z = z / 100.0

    r = x * 3.2406 + y * -1.5372 + z * -0.4986
    g = x * -0.9689 + y * 1.8758 + z * 0.0415
    b = x * 0.0557 + y * -0.2040 + z * 1.0570

    r = 1.055 * numpy.power(r, 1 / 2.4) - 0.055 if r > 0.0031308 else 12.92 * r
    g = 1.055 * numpy.power(g, 1 / 2.4) - 0.055 if g > 0.0031308 else 12.92 * g
    b = 1.055 * numpy.power(b, 1 / 2.4) - 0.055 if b > 0.0031308 else 12.92 * b

    return rgb(*numpy.clip((r, g, b), 0, 1))


def to_lab(color):
    """Convert a Toyplot color to a CIE Lab color."""

    color = to_xyz(color)

    def pivot(n):
        return numpy.power(n, 1.0 / 3.0) if n > pivot.epsilon else (pivot.kappa * n + 16) / 116
    pivot.epsilon = 216.0 / 24389.0
    pivot.kappa = 24389.0 / 27.0

    x = pivot(color[0] / to_lab.white[0])
    y = pivot(color[1] / to_lab.white[1])
    z = pivot(color[2] / to_lab.white[2])

    return numpy.array([max(0, 116 * y - 16), 500 * (x - y), 200 * (y - z)])
to_lab.white = numpy.array([95.047, 100.0, 108.883])


def to_xyz(color):
    """Convert a Toyplot color to a CIE XYZ color using observer = 2 deg and illuminant = D65."""
    def pivot(n):
        return (numpy.power((n + 0.055) / 1.055, 2.4) if n > 0.04045 else n / 12.92) * 100.0

    r = pivot(color["r"])
    g = pivot(color["g"])
    b = pivot(color["b"])

    return numpy.array([
        r * 0.4124 + g * 0.3576 + b * 0.1805,
        r * 0.2126 + g * 0.7152 + b * 0.0722,
        r * 0.0193 + g * 0.1192 + b * 0.9505,
        ])


def _require_color(color):
    if isinstance(color, str):
        return css(color)
    elif isinstance(color, (numpy.void, numpy.ndarray)) and color.dtype == dtype:
        return color
    elif isinstance(color, (tuple, list, numpy.ndarray)) and len(color) == 3:
        return rgb(color[0], color[1], color[2])
    elif isinstance(color, (tuple, list, numpy.ndarray)) and len(color) == 4:
        return rgba(color[0], color[1], color[2], color[3])
    else:
        raise ValueError("Expected a CSS color string or a Toyplot.color.value.") # pragma: no cover


def broadcast(colors, shape, default=None):
    """Return a 1D or 2D array of colors with the given shape.

    Parameters
    ----------
    shape : tuple
        Shape of the desired output array. A 1-tuple will produce a 1D output
        array containing :math:`N` per-series colors.  A 2-tuple will produce
        an :math:`M \\times N` output matrix of per-datum colors grouped into
        :math:`N` series.

    Returns
    -------
    colors: One- or two-dimensional :class:`numpy.ndarray` containing RGBA values with dtype = :data:`toyplot.color.dtype`.
    """
    if colors is None and default is None:
        raise ValueError("Must supply colors or default.") # pragma: no cover
    if not isinstance(shape, tuple):
        shape = (shape,)
    if not isinstance(shape, tuple):
        raise ValueError("Shape parameter must be a tuple with length 1 or 2.") # pragma: no cover
    if not 0 < len(shape) < 3:
        raise ValueError("Shape parameter must be a tuple with length 1 or 2.") # pragma: no cover

    per_datum = len(shape) == 2

    # Supply default color(s).
    if colors is None:
        colors = default

    # Next, extract the user's choice of custom palette / colormap.
    colormap = None
    if isinstance(colors, Map):
        colormap = colors
        colors = numpy.arange(shape[0]) # By default, generate [0, M) per-datum values
        if per_datum and shape[1] > 1:
            colors = numpy.arange(shape[1]) # More than one series, so generate [0, N) per-series values
    elif isinstance(colors, tuple) and len(colors) == 2 and isinstance(colors[1], Map):
        colors, colormap = colors

    # Next, convert the supplied colors into a toyplot color array.
    if isinstance(colors, collections.abc.Sequence):
        colors = numpy.array(colors)

    if isinstance(colors, numpy.ndarray):
        if colors.dtype == dtype: # Already an array of colors
            pass
        elif issubclass(colors.dtype.type, numpy.number): # Array of numeric values, so map values to colors
            if colormap is None:
                colormap = brewer.map("BlueRed", domain_min=colors.min(), domain_max=colors.max())
            colors = colormap.colors(colors)
        elif issubclass(colors.dtype.type, numpy.character): # Convert CSS strings to colors.
            colors = numpy.array([_require_color(color) for color in colors.flat], dtype=dtype).reshape(colors.shape)
    else: # A single value, so convert to a color
        colors = _require_color(colors)

    # Sanity-check to ensure that per-datum colors aren't broadcasted as a per-series shape
    if colors.ndim > len(shape):
        raise ValueError("Per-datum colors aren't allowed here - expecting per-series colors.") # pragma: no cover

    # As a special-case, allow a vector with shape M to be matched-up with an
    # M x 1 matrix.
    if colors.ndim == 1 and per_datum and colors.shape[0] == shape[0] and shape[1] == 1:
        return numpy.reshape(colors, shape)

    return numpy.array(numpy.broadcast_arrays(colors, numpy.empty(shape))[0])


class Palette(object):
    """Storage for an ordered collection of colors.

    Parameters
    ----------
    colors: sequence of color values, optional
      Specifies the list of color values to store in the palette.  Each color may
      be a CSS color string, a Toyplot color, a sequence of three RGB values, or
      a sequence of four RGBA values.  If `colors` is unspecified, the palette
      will be initialized with a default collection of colors.

    reverse: boolean, optional
      If `True`, the values in `colors` will be stored in reverse order.

    Notes
    -----
    You can iterate over the colors in a Palette using normal Python iteration.

    Palettes are displayed as a collection of color swatches when viewed in a
    Jupyter notebook.
    """
    def __init__(self, colors=None, reverse=False):
        if colors is None:
            colors = numpy.array(brewer._data["Set2"][8]) / 255.0

        self._colors = numpy.array([_require_color(color) for color in colors], dtype=dtype)

        if reverse:
            self._colors = self._colors[::-1]

    def __len__(self):
        return len(self._colors)

    def __getitem__(self, index):
        return numpy.array(self._colors[int(index)], dtype=dtype)

    def __iter__(self):
        for color in self._colors:
            yield numpy.array(color, dtype=dtype)

    def _repr_html_(self):
        return _html_color_swatches(self._colors, "toyplot-color-Palette")

    def __add__(self, other):
        if not isinstance(other, Palette):
            raise NotImplementedError("Only toyplot.color.Palette instances can be added together.") # pragma: no cover
        return Palette(numpy.concatenate((self._colors, other._colors)))

    def __iadd__(self, other):
        if not isinstance(other, Palette):
            raise NotImplementedError("Only toyplot.color.Palette instances can be added together.") # pragma: no cover
        self._colors = numpy.concatenate((self._colors, other._colors))
        return self

    def color(self, index):
        """Return one color from the palette.

        Parameters
        ----------
        index: integer
          Specifies the index of the color to retrieve.

        Returns
        -------
        color: :class:`numpy.ndarray` scalar containing RGBA values with dtype = :data:`toyplot.color.dtype`.
        """
        return self.__getitem__(index)

    def css(self, index):
        """Return the CSS representation of one color from the palette.

        Parameters
        ----------
        index: integer
          Specifies the index of the color to retrieve.

        Returns
        -------
        css: :class:`str` containing a CSS color.
        """
        return to_css(self._colors[int(index)])


def _mix(a, b, amount):
    return (a * (1 - amount)) + (b * (amount))


def spread(color, count=5, lightness=0.9, reverse=False):
    """Create a palette by progressively altering an initial color."""
    color = _require_color(color)
    h, l, s = colorsys.rgb_to_hls(color["r"], color["g"], color["b"])
    results = []
    for i in range(count):
        r, g, b = colorsys.hls_to_rgb(h, _mix(l, lightness, i / (count-1)), s)
        results.append(rgba(r, g, b, color["a"]))
    return Palette(numpy.array(results), reverse=reverse)


class Map(object, metaclass=custom_inherit.DocInheritMeta(style="numpy_napoleon")):
    """Abstract interface for objects that map scalar values to colors."""
    class DomainHelper(object):
        """Interface to get / set the domain for a :class:`toyplot.color.Map`."""
        def __init__(self, domain_min, domain_max):
            self._min = domain_min
            self._max = domain_max

        @property
        def min(self):
            """Minimum domain value."""
            return self._min

        @min.setter
        def min(self, value):
            self._min = value

        @property
        def max(self):
            """Maximum domain value."""
            return self._max

        @max.setter
        def max(self, value):
            self._max = value

    def __init__(self, domain_min, domain_max):
        self._domain = Map.DomainHelper(domain_min, domain_max)

    def _finalize(self):
        return self

    @property
    def domain(self):
        """Accessor for the map's domain.

        Returns
        -------
        domain: :class:`toyplot.color.Map.DomainHelper`
            Provides access to the minimum and maximum domain values for the map.
        """
        return self._domain


class CategoricalMap(Map):
    """Maps 1D categorical values (nonnegative integers) to colors.

    Parameters
    ----------
    palette: an instance of :class:`toyplot.color.Palette`
      Defines the set of colors used by the map.

    Notes
    -----
    Categorical maps are displayed as a collection of color swatches when viewed
    in a Jupyter notebook.
    """
    def __init__(self, palette=None):
        if palette is None:
            palette = Palette()
        self._palette = palette
        super(CategoricalMap, self).__init__(domain_min=0, domain_max=len(palette))

    def colors(self, values, domain_min=None, domain_max=None):
        """Convert a sequence of categorical (nonnegative integer) values to colors.

        Each value is mapped to a color in the underlying palette.  Note that the
        palette repeats infinitely, so any nonnegative integer value will return
        a color from the palette.

        Parameters
        ----------
        values: array-like collection of nonnegative integers

        Returns
        -------
        colors: :class:`numpy.ndarray` containing RGBA values with dtype = :data:`toyplot.color.dtype` and the same shape as `values`.
        """
        values = numpy.array(values, dtype="int64")
        flat = numpy.ravel(values) % len(self._palette._colors)
        result = self._palette._colors[flat]
        return result.reshape(values.shape)

    def color(self, index, domain_min=None, domain_max=None):
        """Return one color from the map.

        Parameters
        ----------
        index: nonnegative integer
          Specifies the index of the color to retrieve.  Note that the palette
          repeats infinitely, so any nonnegative integer value will return a color
          from the palette.

        Returns
        -------
        color: :class:`numpy.ndarray` scalar containing RGBA values with dtype = :data:`toyplot.color.dtype`.
        """
        return self.colors(index, domain_min, domain_max)

    def css(self, index, domain_min=None, domain_max=None):
        """Return the CSS representation of one color from the map.

        Parameters
        ----------
        index: nonnegative integer
          Specifies the index of the color to retrieve.  Note that the palette
          repeats infinitely, so any nonnegative integer value will return a color
          from the palette.

        Returns
        -------
        css: :class:`str` containing a CSS color.
        """
        return to_css(self.colors(index, domain_min, domain_max))

    def _repr_html_(self):
        return _html_color_swatches(self._palette._colors, "toyplot-color-CategoricalMap")


class DivergingMap(Map):
    """Maps 1D values to colors using a perceptually-uniform diverging color map.

    Based on "Diverging Color Maps for Scientific Visualization", Kenneth
    Moreland, http://www.sandia.gov/~kmorel/documents/ColorMaps

    Values within the domain specified at construction time are mapped to the
    colors in the underlying palette.  Values outside the domain are clamped to
    the minimum / maximum domain values.  If unspecified, the domain will be
    computed on-the-fly every time :meth:`toyplot.color.DivergingMap.colors` is
    called.

    Parameters
    ----------
    low: Toyplot color, optional
      Defines the color used to represent low values.

    high: Toyplot color, optional
      Defines the color used to represent high values.

    domain_min: scalar, optional

    domain_max: scalar, optional

    Notes
    -----
    Diverging maps generate a color preview when viewed in a Jupyter notebook.
    """
    def __init__(self, low=None, high=None, domain_min=None, domain_max=None):
        super(DivergingMap, self).__init__(domain_min=domain_min, domain_max=domain_max)

        def _lab_to_msh(L, a, b):
            M = numpy.sqrt(L * L + a * a + b * b)
            s = numpy.arccos(L / M) if (M > 0.001) else 0.0
            h = numpy.arctan2(b, a) if (s > 0.001) else 0.0
            return M, s, h

        def middle(original):
            m, s, h = 88, 0, original[2]
            if m > original[0]:
                spin = original[
                    1] * numpy.sqrt((m * m) - (original[0] * original[0])) / (original[0] * numpy.sin(original[1]))
            else:
                spin = 0
            h = h + spin if h > 0 else h - spin
            return m, s, h

        if low is None:
            low = rgb(0.230, 0.299, 0.754)
        if high is None:
            high = rgb(0.706, 0.016, 0.150)

        self._low = _lab_to_msh(*to_lab(low)) # pylint: disable=no-value-for-parameter
        self._high = _lab_to_msh(*to_lab(high)) # pylint: disable=no-value-for-parameter
        self._mid_low = middle(self._low)
        self._mid_high = middle(self._high)

    def colors(self, values, domain_min=None, domain_max=None):
        """Convert an array-like collection of values to colors.

        Parameters
        ----------
        values: array-like collection of scalar values

        Returns
        -------
        colors: :class:`numpy.ndarray` containing RGBA values with dtype = :data:`toyplot.color.dtype` and the same shape as `values`.
        """

        def _msh_to_lab(M, s, h):
            L = M * numpy.cos(s)
            a = M * numpy.sin(s) * numpy.cos(h)
            b = M * numpy.sin(s) * numpy.sin(h)
            return L, a, b

        values = numpy.array(values)
        domain_min = domain_min if domain_min is not None else self.domain.min if self.domain.min is not None else values.min()
        domain_max = domain_max if domain_max is not None else self.domain.max if self.domain.max is not None else values.max()

        flat = numpy.clip(numpy.ravel(values), domain_min, domain_max)
        flat = (flat - domain_min) / (domain_max - domain_min) if (domain_max - \
                domain_min) > 0 else numpy.zeros(flat.shape)
        result = numpy.zeros(flat.shape, dtype=dtype)
        for index, amount in enumerate(flat):
            if amount < 0.5:
                a = self._low
                b = self._mid_low
                amount = amount * 2.0
            else:
                a = self._mid_high
                b = self._high
                amount = (amount - 0.5) * 2.0
            result[index] = lab(
                *
                _msh_to_lab(
                    _mix(
                        a[0],
                        b[0],
                        amount),
                    _mix(
                        a[1],
                        b[1],
                        amount),
                    _mix(
                        a[2],
                        b[2],
                        amount)))
        return result.reshape(values.shape)

    def color(self, value, domain_min=None, domain_max=None):
        """Convert one value to a color.

        Parameters
        ----------
        value: scalar value

        Returns
        -------
        color: :class:`numpy.ndarray` scalar containing RGBA values with dtype = :data:`toyplot.color.dtype`.
        """
        return self.colors(value, domain_min, domain_max)

    def css(self, value, domain_min=None, domain_max=None):
        """Convert one value to a CSS representation of its color.

        Parameters
        ----------
        value: scalar value

        Returns
        -------
        css: :class:`str` containing a CSS color.
        """
        return to_css(self.colors(value, domain_min, domain_max))

    def _repr_html_(self):
        domain_min = self.domain.min if self.domain.min is not None else 0
        domain_max = self.domain.max if self.domain.max is not None else 1
        stops = numpy.linspace(domain_min, domain_max, 64, endpoint=True)
        colors = self.colors(stops)

        gradient_stops = ",".join([to_css(color) + " %.1f%%" % (position * 100.0) for color, position in zip(colors, stops)])

        root_xml = xml.Element(
            "div",
            style="overflow:hidden; height:auto",
            attrib={"class": "toyplot-color-DivergingMap"},
            )

        xml.SubElement(
            root_xml,
            "div",
            style="float:left;width:200px;height:20px;background:linear-gradient(to right,%s)" % (gradient_stops),
            )
        return xml.tostring(root_xml, encoding="unicode", method="html")


class LinearMap(Map):
    """Maps 1D values to colors.

    Values within the domain specified at construction time are mapped to the
    colors in the underlying palette.  Values outside the domain are clamped to
    the minimum / maximum domain values.  If unspecified, the domain will be
    computed on-the-fly each time :meth:`toyplot.color.LinearMap.colors` is
    called.

    Parameters
    ----------
    palette: :class:`toyplot.color.Palette`
        Specify the set of colors used by the map.
    stops: sequence of scalars, one per palette color, optional
        Specify a "stop" in the range [0, 1] for each palette color.  By
        default the stops are evenly spaced.
    center: scalar, optional
        If specified, map [domain_min, center] to the first half of the color
        palette, and [center, domain_max] to the second half of the palette.
        This is useful for diverging palettes when there is a domain-specific
        critical value that should fall in the middle of the color range, such
        as zero or a mean or median.
    domain_min: scalar, optional
    domain_max: scalar, optional

    Notes
    -----
    Linear maps are displayed as a color preview of their domain when viewed in
    a Jupyter notebook.
    """

    def __init__(self, palette=None, stops=None, center=None, domain_min=None, domain_max=None):
        super(LinearMap, self).__init__(domain_min=domain_min, domain_max=domain_max)

        if palette is None:
            palette = brewer.palette("BlueRed")
        if stops is None:
            stops = numpy.linspace(0, 1, len(palette), endpoint=True)
        stops = numpy.array(stops)

        if stops.shape != palette._colors.shape:
            raise ValueError("Number of stops must match palette length.") # pragma: no cover

        self._palette = palette
        self._stops = stops
        self._center = center


    def colors(self, values, domain_min=None, domain_max=None):
        """Convert an array-like collection of values to colors.

        Parameters
        ----------
        values: array-like collection of scalar values

        Returns
        -------
        colors: :class:`numpy.ndarray` containing RGBA values with dtype = :data:`toyplot.color.dtype` and the same shape as `values`.
        """
        values = numpy.array(values)
        domain_min = domain_min if domain_min is not None else self.domain.min if self.domain.min is not None else values.min()
        domain_max = domain_max if domain_max is not None else self.domain.max if self.domain.max is not None else values.max()

        # If the domain is empty, default to the first color in the palette
        if domain_min == domain_max:
            return numpy.full_like(values, self._palette[0], dtype=dtype)

        if self._center is not None:
            segments = [
                toyplot.projection.Piecewise.Segment("linear", -numpy.inf, domain_min, self._center, self._center, -numpy.inf, 0, 0.5, 0.5),
                toyplot.projection.Piecewise.Segment("linear", self._center, self._center, domain_max, numpy.inf, 0.5, 0.5, 1.0, numpy.inf),
            ]
            projection = toyplot.projection.Piecewise(segments)
        else:
            projection = toyplot.projection.linear(domain_min, domain_max, 0.0, 1.0)

        flat = projection(numpy.ravel(values))
        result = numpy.empty(flat.shape, dtype=dtype)
        result["r"] = numpy.interp(flat, self._stops, self._palette._colors["r"])
        result["g"] = numpy.interp(flat, self._stops, self._palette._colors["g"])
        result["b"] = numpy.interp(flat, self._stops, self._palette._colors["b"])
        result["a"] = numpy.interp(flat, self._stops, self._palette._colors["a"])
        return result.reshape(values.shape)

    def color(self, value, domain_min=None, domain_max=None):
        """Convert one value to a color.

        Parameters
        ----------
        value: scalar value

        Returns
        -------
        color: :class:`numpy.ndarray` scalar containing RGBA values with dtype = :data:`toyplot.color.dtype`.
        """
        return self.colors(value, domain_min, domain_max)

    def css(self, value, domain_min=None, domain_max=None):
        """Convert one value to a CSS representation of its color.

        Parameters
        ----------
        value: scalar value

        Returns
        -------
        css: :class:`str` containing a CSS color.
        """
        return to_css(self.colors(value, domain_min, domain_max))

    def _repr_html_(self):
        domain_min = self.domain.min if self.domain.min is not None else 0
        domain_max = self.domain.max if self.domain.max is not None else 1
        stops = numpy.linspace(domain_min, domain_max, 64, endpoint=True)
        colors = self.colors(stops)

        gradient_stops = ",".join([to_css(color) + " %.1f%%" % (position * 100.0) for color, position in zip(colors, stops)])

        root_xml = xml.Element(
            "div",
            style="overflow:hidden; height:auto",
            attrib={"class": "toyplot-color-LinearMap"},
            )

        xml.SubElement(
            root_xml,
            "div",
            style="float:left;width:200px;height:20px;background:linear-gradient(to right,%s)" % (gradient_stops),
            )
        return xml.tostring(root_xml, encoding="unicode", method="html")


class BrewerFactory(object):
    """Creates Toyplot color palettes and maps based on the Color Brewer 2.0 palettes."""
    def names(self, category=None):
        """Return a list of available palette names."""
        names = [name for name in sorted(self._data.keys())]
        if category is not None:
            names = [name for name in names if self.category(name) == category]
        return names

    def category(self, name):
        """Return the category for the given palette."""
        return self._type_map[self._data[name]["type"]]

    def counts(self, name):
        """Return a list of available palette sizes."""
        return sorted([count for count in self._data[name].keys() if count not in["type", "reverse"]])

    def palette(self, name, count=None, reverse=False):
        """Construct a :py:class:`toyplot.color.Palette` instance from a ColorBrewer 2.0 palette.

        Note that some of the sequential palettes have been renamed / reversed
        so that low-luma colors are always mapped to low values and high-luma
        colors are always mapped to high values.

        Parameters
        ----------
        name: :class:`str`
          The name of the ColorBrewer 2.0 palette.

        count: integer, optional
          The number of values in the palette.  If unspecified, the named palette
          with the largest number of values is returned.

        reverse: boolean, optional
          If `True`, the values in `palette` will be stored in reverse order.

        Returns
        -------
        palette: :py:class:`toyplot.color.Palette`
        """
        if count is None:
            count = max(self.counts(name))
        data = numpy.array(self._data[name][count]) / 255.0
        if self._data[name].get("reverse", False):
            data = data[::-1]
        return Palette(data, reverse=reverse)

    def palettes(self, category=None):
        """Return a (name, palette) tuple for every Color Brewer 2.0 palette.

        Parameters
        ----------
        category: :class:`str`, optional
            If specified, only return palettes from the given category.

        Returns
        -------
        palettes: sequence of (:class:`str`, :class:`toyplot.color.Palette`) tuples.
        """
        return [(name, self.palette(name)) for name in self.names(category)]

    def map(self, name, count=None, reverse=False, center=None, domain_min=None, domain_max=None):
        """Return a color map that uses the given Color Brewer 2.0 palette.

        Returns
        -------
        colormap: :class:`toyplot.color.LinearMap` or :class:`toyplot.color.CategoricalMap`, depending on the palette category.
        """
        if self.category(name) == "qualitative":
            return CategoricalMap(
                palette=self.palette(name=name, count=count, reverse=reverse),
                )

        return LinearMap(
            palette=self.palette(name=name, count=count, reverse=reverse),
            center=center,
            domain_min=domain_min,
            domain_max=domain_max,
            )

    def maps(self, category=None):
        """Return a (name, colormap) tuple for every Color Brewer 2.0 palette.

        The type of the returned colormaps will be chosen based on the category of each palette.

        Parameters
        ----------
        category: :class:`str`, optional
            If specified, only return palettes from the given category.

        Returns
        -------
        palettes: sequence of (:class:`str`, :class:`toyplot.color.Map`) tuples.
        """
        return [(name, self.map(name)) for name in self.names(category)]

    _type_map = {"div": "diverging", "qual": "qualitative", "seq": "sequential"}

    _data = {
        "Spectral": {
            3: [
                (252, 141, 89),
                (255, 255, 191),
                (153, 213, 148)],
            4: [
                (215, 25, 28),
                (253, 174, 97),
                (171, 221, 164),
                (43, 131, 186)],
            5: [
                (215, 25, 28),
                (253, 174, 97),
                (255, 255, 191),
                (171, 221, 164),
                (43, 131, 186)],
            6: [
                (213, 62, 79),
                (252, 141, 89),
                (254, 224, 139),
                (230, 245, 152),
                (153, 213, 148),
                (50, 136, 189)],
            7: [
                (213, 62, 79),
                (252, 141, 89),
                (254, 224, 139),
                (255, 255, 191),
                (230, 245, 152),
                (153, 213, 148),
                (50, 136, 189)],
            8: [
                (213, 62, 79),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 139),
                (230, 245, 152),
                (171, 221, 164),
                (102, 194, 165),
                (50, 136, 189)],
            9: [
                (213, 62, 79),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 139),
                (255, 255, 191),
                (230, 245, 152),
                (171, 221, 164),
                (102, 194, 165),
                (50, 136, 189)],
            10: [
                (158, 1, 66),
                (213, 62, 79),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 139),
                (230, 245, 152),
                (171, 221, 164),
                (102, 194, 165),
                (50, 136, 189),
                (94, 79, 162)],
            11: [
                (158, 1, 66),
                (213, 62, 79),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 139),
                (255, 255, 191),
                (230, 245, 152),
                (171, 221, 164),
                (102, 194, 165),
                (50, 136, 189),
                (94, 79, 162)], "type": "div", "reverse": True},
        "GreenYellowRed": {
            3: [
                (252, 141, 89),
                (255, 255, 191),
                (145, 207, 96)],
            4: [
                (215, 25, 28),
                (253, 174, 97),
                (166, 217, 106),
                (26, 150, 65)],
            5: [
                (215, 25, 28),
                (253, 174, 97),
                (255, 255, 191),
                (166, 217, 106),
                (26, 150, 65)],
            6: [
                (215, 48, 39),
                (252, 141, 89),
                (254, 224, 139),
                (217, 239, 139),
                (145, 207, 96),
                (26, 152, 80)],
            7: [
                (215, 48, 39),
                (252, 141, 89),
                (254, 224, 139),
                (255, 255, 191),
                (217, 239, 139),
                (145, 207, 96),
                (26, 152, 80)],
            8: [
                (215, 48, 39),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 139),
                (217, 239, 139),
                (166, 217, 106),
                (102, 189, 99),
                (26, 152, 80)],
            9: [
                (215, 48, 39),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 139),
                (255, 255, 191),
                (217, 239, 139),
                (166, 217, 106),
                (102, 189, 99),
                (26, 152, 80)],
            10: [
                (165, 0, 38),
                (215, 48, 39),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 139),
                (217, 239, 139),
                (166, 217, 106),
                (102, 189, 99),
                (26, 152, 80),
                (0, 104, 55)],
            11: [
                (165, 0, 38),
                (215, 48, 39),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 139),
                (255, 255, 191),
                (217, 239, 139),
                (166, 217, 106),
                (102, 189, 99),
                (26, 152, 80),
                (0, 104, 55)], "type": "div", "reverse": True},
        "BlueRed": {
            3: [
                (239, 138, 98),
                (247, 247, 247),
                (103, 169, 207)],
            4: [
                (202, 0, 32),
                (244, 165, 130),
                (146, 197, 222),
                (5, 113, 176)],
            5: [
                (202, 0, 32),
                (244, 165, 130),
                (247, 247, 247),
                (146, 197, 222),
                (5, 113, 176)],
            6: [
                (178, 24, 43),
                (239, 138, 98),
                (253, 219, 199),
                (209, 229, 240),
                (103, 169, 207),
                (33, 102, 172)],
            7: [
                (178, 24, 43),
                (239, 138, 98),
                (253, 219, 199),
                (247, 247, 247),
                (209, 229, 240),
                (103, 169, 207),
                (33, 102, 172)],
            8: [
                (178, 24, 43),
                (214, 96, 77),
                (244, 165, 130),
                (253, 219, 199),
                (209, 229, 240),
                (146, 197, 222),
                (67, 147, 195),
                (33, 102, 172)],
            9: [
                (178, 24, 43),
                (214, 96, 77),
                (244, 165, 130),
                (253, 219, 199),
                (247, 247, 247),
                (209, 229, 240),
                (146, 197, 222),
                (67, 147, 195),
                (33, 102, 172)],
            10: [
                (103, 0, 31),
                (178, 24, 43),
                (214, 96, 77),
                (244, 165, 130),
                (253, 219, 199),
                (209, 229, 240),
                (146, 197, 222),
                (67, 147, 195),
                (33, 102, 172),
                (5, 48, 97)],
            11: [
                (103, 0, 31),
                (178, 24, 43),
                (214, 96, 77),
                (244, 165, 130),
                (253, 219, 199),
                (247, 247, 247),
                (209, 229, 240),
                (146, 197, 222),
                (67, 147, 195),
                (33, 102, 172),
                (5, 48, 97)], "type": "div", "reverse": True},
        "PinkGreen": {
            3: [
                (233, 163, 201),
                (247, 247, 247),
                (161, 215, 106)],
            4: [
                (208, 28, 139),
                (241, 182, 218),
                (184, 225, 134),
                (77, 172, 38)],
            5: [
                (208, 28, 139),
                (241, 182, 218),
                (247, 247, 247),
                (184, 225, 134),
                (77, 172, 38)],
            6: [
                (197, 27, 125),
                (233, 163, 201),
                (253, 224, 239),
                (230, 245, 208),
                (161, 215, 106),
                (77, 146, 33)],
            7: [
                (197, 27, 125),
                (233, 163, 201),
                (253, 224, 239),
                (247, 247, 247),
                (230, 245, 208),
                (161, 215, 106),
                (77, 146, 33)],
            8: [
                (197, 27, 125),
                (222, 119, 174),
                (241, 182, 218),
                (253, 224, 239),
                (230, 245, 208),
                (184, 225, 134),
                (127, 188, 65),
                (77, 146, 33)],
            9: [
                (197, 27, 125),
                (222, 119, 174),
                (241, 182, 218),
                (253, 224, 239),
                (247, 247, 247),
                (230, 245, 208),
                (184, 225, 134),
                (127, 188, 65),
                (77, 146, 33)],
            10: [
                (142, 1, 82),
                (197, 27, 125),
                (222, 119, 174),
                (241, 182, 218),
                (253, 224, 239),
                (230, 245, 208),
                (184, 225, 134),
                (127, 188, 65),
                (77, 146, 33),
                (39, 100, 25)],
            11: [
                (142, 1, 82),
                (197, 27, 125),
                (222, 119, 174),
                (241, 182, 218),
                (253, 224, 239),
                (247, 247, 247),
                (230, 245, 208),
                (184, 225, 134),
                (127, 188, 65),
                (77, 146, 33),
                (39, 100, 25)], "type": "div"},
        "PurpleGreen": {
            3: [
                (175, 141, 195),
                (247, 247, 247),
                (127, 191, 123)],
            4: [
                (123, 50, 148),
                (194, 165, 207),
                (166, 219, 160),
                (0, 136, 55)],
            5: [
                (123, 50, 148),
                (194, 165, 207),
                (247, 247, 247),
                (166, 219, 160),
                (0, 136, 55)],
            6: [
                (118, 42, 131),
                (175, 141, 195),
                (231, 212, 232),
                (217, 240, 211),
                (127, 191, 123),
                (27, 120, 55)],
            7: [
                (118, 42, 131),
                (175, 141, 195),
                (231, 212, 232),
                (247, 247, 247),
                (217, 240, 211),
                (127, 191, 123),
                (27, 120, 55)],
            8: [
                (118, 42, 131),
                (153, 112, 171),
                (194, 165, 207),
                (231, 212, 232),
                (217, 240, 211),
                (166, 219, 160),
                (90, 174, 97),
                (27, 120, 55)],
            9: [
                (118, 42, 131),
                (153, 112, 171),
                (194, 165, 207),
                (231, 212, 232),
                (247, 247, 247),
                (217, 240, 211),
                (166, 219, 160),
                (90, 174, 97),
                (27, 120, 55)],
            10: [
                (64, 0, 75),
                (118, 42, 131),
                (153, 112, 171),
                (194, 165, 207),
                (231, 212, 232),
                (217, 240, 211),
                (166, 219, 160),
                (90, 174, 97),
                (27, 120, 55),
                (0, 68, 27)],
            11: [
                (64, 0, 75),
                (118, 42, 131),
                (153, 112, 171),
                (194, 165, 207),
                (231, 212, 232),
                (247, 247, 247),
                (217, 240, 211),
                (166, 219, 160),
                (90, 174, 97),
                (27, 120, 55),
                (0, 68, 27)], "type": "div"},
        "BlueYellowRed": {
            3: [
                (252, 141, 89),
                (255, 255, 191),
                (145, 191, 219)],
            4: [
                (215, 25, 28),
                (253, 174, 97),
                (171, 217, 233),
                (44, 123, 182)],
            5: [
                (215, 25, 28),
                (253, 174, 97),
                (255, 255, 191),
                (171, 217, 233),
                (44, 123, 182)],
            6: [
                (215, 48, 39),
                (252, 141, 89),
                (254, 224, 144),
                (224, 243, 248),
                (145, 191, 219),
                (69, 117, 180)],
            7: [
                (215, 48, 39),
                (252, 141, 89),
                (254, 224, 144),
                (255, 255, 191),
                (224, 243, 248),
                (145, 191, 219),
                (69, 117, 180)],
            8: [
                (215, 48, 39),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 144),
                (224, 243, 248),
                (171, 217, 233),
                (116, 173, 209),
                (69, 117, 180)],
            9: [
                (215, 48, 39),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 144),
                (255, 255, 191),
                (224, 243, 248),
                (171, 217, 233),
                (116, 173, 209),
                (69, 117, 180)],
            10: [
                (165, 0, 38),
                (215, 48, 39),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 144),
                (224, 243, 248),
                (171, 217, 233),
                (116, 173, 209),
                (69, 117, 180),
                (49, 54, 149)],
            11: [
                (165, 0, 38),
                (215, 48, 39),
                (244, 109, 67),
                (253, 174, 97),
                (254, 224, 144),
                (255, 255, 191),
                (224, 243, 248),
                (171, 217, 233),
                (116, 173, 209),
                (69, 117, 180),
                (49, 54, 149)], "type": "div", "reverse": True},
        "BlueGreenBrown": {
            3: [
                (216, 179, 101),
                (245, 245, 245),
                (90, 180, 172)],
            4: [
                (166, 97, 26),
                (223, 194, 125),
                (128, 205, 193),
                (1, 133, 113)],
            5: [
                (166, 97, 26),
                (223, 194, 125),
                (245, 245, 245),
                (128, 205, 193),
                (1, 133, 113)],
            6: [
                (140, 81, 10),
                (216, 179, 101),
                (246, 232, 195),
                (199, 234, 229),
                (90, 180, 172),
                (1, 102, 94)],
            7: [
                (140, 81, 10),
                (216, 179, 101),
                (246, 232, 195),
                (245, 245, 245),
                (199, 234, 229),
                (90, 180, 172),
                (1, 102, 94)],
            8: [
                (140, 81, 10),
                (191, 129, 45),
                (223, 194, 125),
                (246, 232, 195),
                (199, 234, 229),
                (128, 205, 193),
                (53, 151, 143),
                (1, 102, 94)],
            9: [
                (140, 81, 10),
                (191, 129, 45),
                (223, 194, 125),
                (246, 232, 195),
                (245, 245, 245),
                (199, 234, 229),
                (128, 205, 193),
                (53, 151, 143),
                (1, 102, 94)],
            10: [
                (84, 48, 5),
                (140, 81, 10),
                (191, 129, 45),
                (223, 194, 125),
                (246, 232, 195),
                (199, 234, 229),
                (128, 205, 193),
                (53, 151, 143),
                (1, 102, 94),
                (0, 60, 48)],
            11: [
                (84, 48, 5),
                (140, 81, 10),
                (191, 129, 45),
                (223, 194, 125),
                (246, 232, 195),
                (245, 245, 245),
                (199, 234, 229),
                (128, 205, 193),
                (53, 151, 143),
                (1, 102, 94),
                (0, 60, 48)], "type": "div", "reverse": True},
        "GrayRed": {
            3: [
                (239, 138, 98),
                (255, 255, 255),
                (153, 153, 153)],
            4: [
                (202, 0, 32),
                (244, 165, 130),
                (186, 186, 186),
                (64, 64, 64)],
            5: [
                (202, 0, 32),
                (244, 165, 130),
                (255, 255, 255),
                (186, 186, 186),
                (64, 64, 64)],
            6: [
                (178, 24, 43),
                (239, 138, 98),
                (253, 219, 199),
                (224, 224, 224),
                (153, 153, 153),
                (77, 77, 77)],
            7: [
                (178, 24, 43),
                (239, 138, 98),
                (253, 219, 199),
                (255, 255, 255),
                (224, 224, 224),
                (153, 153, 153),
                (77, 77, 77)],
            8: [
                (178, 24, 43),
                (214, 96, 77),
                (244, 165, 130),
                (253, 219, 199),
                (224, 224, 224),
                (186, 186, 186),
                (135, 135, 135),
                (77, 77, 77)],
            9: [
                (178, 24, 43),
                (214, 96, 77),
                (244, 165, 130),
                (253, 219, 199),
                (255, 255, 255),
                (224, 224, 224),
                (186, 186, 186),
                (135, 135, 135),
                (77, 77, 77)],
            10: [
                (103, 0, 31),
                (178, 24, 43),
                (214, 96, 77),
                (244, 165, 130),
                (253, 219, 199),
                (224, 224, 224),
                (186, 186, 186),
                (135, 135, 135),
                (77, 77, 77),
                (26, 26, 26)],
            11: [
                (103, 0, 31),
                (178, 24, 43),
                (214, 96, 77),
                (244, 165, 130),
                (253, 219, 199),
                (255, 255, 255),
                (224, 224, 224),
                (186, 186, 186),
                (135, 135, 135),
                (77, 77, 77),
                (26, 26, 26)], "type": "div", "reverse": True},
        "PurpleOrange": {
            3: [
                (241, 163, 64),
                (247, 247, 247),
                (153, 142, 195)],
            4: [
                (230, 97, 1),
                (253, 184, 99),
                (178, 171, 210),
                (94, 60, 153)],
            5: [
                (230, 97, 1),
                (253, 184, 99),
                (247, 247, 247),
                (178, 171, 210),
                (94, 60, 153)],
            6: [
                (179, 88, 6),
                (241, 163, 64),
                (254, 224, 182),
                (216, 218, 235),
                (153, 142, 195),
                (84, 39, 136)],
            7: [
                (179, 88, 6),
                (241, 163, 64),
                (254, 224, 182),
                (247, 247, 247),
                (216, 218, 235),
                (153, 142, 195),
                (84, 39, 136)],
            8: [
                (179, 88, 6),
                (224, 130, 20),
                (253, 184, 99),
                (254, 224, 182),
                (216, 218, 235),
                (178, 171, 210),
                (128, 115, 172),
                (84, 39, 136)],
            9: [
                (179, 88, 6),
                (224, 130, 20),
                (253, 184, 99),
                (254, 224, 182),
                (247, 247, 247),
                (216, 218, 235),
                (178, 171, 210),
                (128, 115, 172),
                (84, 39, 136)],
            10: [
                (127, 59, 8),
                (179, 88, 6),
                (224, 130, 20),
                (253, 184, 99),
                (254, 224, 182),
                (216, 218, 235),
                (178, 171, 210),
                (128, 115, 172),
                (84, 39, 136),
                (45, 0, 75)],
            11: [
                (127, 59, 8),
                (179, 88, 6),
                (224, 130, 20),
                (253, 184, 99),
                (254, 224, 182),
                (247, 247, 247),
                (216, 218, 235),
                (178, 171, 210),
                (128, 115, 172),
                (84, 39, 136),
                (45, 0, 75)], "type": "div", "reverse": True},
        "Set2": {
            3: [
                (102, 194, 165),
                (252, 141, 98),
                (141, 160, 203)],
            4: [
                (102, 194, 165),
                (252, 141, 98),
                (141, 160, 203),
                (231, 138, 195)],
            5: [
                (102, 194, 165),
                (252, 141, 98),
                (141, 160, 203),
                (231, 138, 195),
                (166, 216, 84)],
            6: [
                (102, 194, 165),
                (252, 141, 98),
                (141, 160, 203),
                (231, 138, 195),
                (166, 216, 84),
                (255, 217, 47)],
            7: [
                (102, 194, 165),
                (252, 141, 98),
                (141, 160, 203),
                (231, 138, 195),
                (166, 216, 84),
                (255, 217, 47),
                (229, 196, 148)],
            8: [
                (102, 194, 165),
                (252, 141, 98),
                (141, 160, 203),
                (231, 138, 195),
                (166, 216, 84),
                (255, 217, 47),
                (229, 196, 148),
                (179, 179, 179)], "type": "qual"},
        "Accent": {
            3: [
                (127, 201, 127),
                (190, 174, 212),
                (253, 192, 134)],
            4: [
                (127, 201, 127),
                (190, 174, 212),
                (253, 192, 134),
                (255, 255, 153)],
            5: [
                (127, 201, 127),
                (190, 174, 212),
                (253, 192, 134),
                (255, 255, 153),
                (56, 108, 176)],
            6: [
                (127, 201, 127),
                (190, 174, 212),
                (253, 192, 134),
                (255, 255, 153),
                (56, 108, 176),
                (240, 2, 127)],
            7: [
                (127, 201, 127),
                (190, 174, 212),
                (253, 192, 134),
                (255, 255, 153),
                (56, 108, 176),
                (240, 2, 127),
                (191, 91, 23)],
            8: [
                (127, 201, 127),
                (190, 174, 212),
                (253, 192, 134),
                (255, 255, 153),
                (56, 108, 176),
                (240, 2, 127),
                (191, 91, 23),
                (102, 102, 102)], "type": "qual"},
        "Set1": {
            3: [
                (228, 26, 28),
                (55, 126, 184),
                (77, 175, 74)],
            4: [
                (228, 26, 28),
                (55, 126, 184),
                (77, 175, 74),
                (152, 78, 163)],
            5: [
                (228, 26, 28),
                (55, 126, 184),
                (77, 175, 74),
                (152, 78, 163),
                (255, 127, 0)],
            6: [
                (228, 26, 28),
                (55, 126, 184),
                (77, 175, 74),
                (152, 78, 163),
                (255, 127, 0),
                (255, 255, 51)],
            7: [
                (228, 26, 28),
                (55, 126, 184),
                (77, 175, 74),
                (152, 78, 163),
                (255, 127, 0),
                (255, 255, 51),
                (166, 86, 40)],
            8: [
                (228, 26, 28),
                (55, 126, 184),
                (77, 175, 74),
                (152, 78, 163),
                (255, 127, 0),
                (255, 255, 51),
                (166, 86, 40),
                (247, 129, 191)],
            9: [
                (228, 26, 28),
                (55, 126, 184),
                (77, 175, 74),
                (152, 78, 163),
                (255, 127, 0),
                (255, 255, 51),
                (166, 86, 40),
                (247, 129, 191),
                (153, 153, 153)], "type": "qual"},
        "Set3": {
            3: [
                (141, 211, 199),
                (255, 255, 179),
                (190, 186, 218)],
            4: [
                (141, 211, 199),
                (255, 255, 179),
                (190, 186, 218),
                (251, 128, 114)],
            5: [
                (141, 211, 199),
                (255, 255, 179),
                (190, 186, 218),
                (251, 128, 114),
                (128, 177, 211)],
            6: [
                (141, 211, 199),
                (255, 255, 179),
                (190, 186, 218),
                (251, 128, 114),
                (128, 177, 211),
                (253, 180, 98)],
            7: [
                (141, 211, 199),
                (255, 255, 179),
                (190, 186, 218),
                (251, 128, 114),
                (128, 177, 211),
                (253, 180, 98),
                (179, 222, 105)],
            8: [
                (141, 211, 199),
                (255, 255, 179),
                (190, 186, 218),
                (251, 128, 114),
                (128, 177, 211),
                (253, 180, 98),
                (179, 222, 105),
                (252, 205, 229)],
            9: [
                (141, 211, 199),
                (255, 255, 179),
                (190, 186, 218),
                (251, 128, 114),
                (128, 177, 211),
                (253, 180, 98),
                (179, 222, 105),
                (252, 205, 229),
                (217, 217, 217)],
            10: [
                (141, 211, 199),
                (255, 255, 179),
                (190, 186, 218),
                (251, 128, 114),
                (128, 177, 211),
                (253, 180, 98),
                (179, 222, 105),
                (252, 205, 229),
                (217, 217, 217),
                (188, 128, 189)],
            11: [
                (141, 211, 199),
                (255, 255, 179),
                (190, 186, 218),
                (251, 128, 114),
                (128, 177, 211),
                (253, 180, 98),
                (179, 222, 105),
                (252, 205, 229),
                (217, 217, 217),
                (188, 128, 189),
                (204, 235, 197)],
            12: [
                (141, 211, 199),
                (255, 255, 179),
                (190, 186, 218),
                (251, 128, 114),
                (128, 177, 211),
                (253, 180, 98),
                (179, 222, 105),
                (252, 205, 229),
                (217, 217, 217),
                (188, 128, 189),
                (204, 235, 197),
                (255, 237, 111)], "type": "qual"},
        "Dark2": {
            3: [
                (27, 158, 119),
                (217, 95, 2),
                (117, 112, 179)],
            4: [
                (27, 158, 119),
                (217, 95, 2),
                (117, 112, 179),
                (231, 41, 138)],
            5: [
                (27, 158, 119),
                (217, 95, 2),
                (117, 112, 179),
                (231, 41, 138),
                (102, 166, 30)],
            6: [
                (27, 158, 119),
                (217, 95, 2),
                (117, 112, 179),
                (231, 41, 138),
                (102, 166, 30),
                (230, 171, 2)],
            7: [
                (27, 158, 119),
                (217, 95, 2),
                (117, 112, 179),
                (231, 41, 138),
                (102, 166, 30),
                (230, 171, 2),
                (166, 118, 29)],
            8: [
                (27, 158, 119),
                (217, 95, 2),
                (117, 112, 179),
                (231, 41, 138),
                (102, 166, 30),
                (230, 171, 2),
                (166, 118, 29),
                (102, 102, 102)], "type": "qual"},
        "Paired": {
            3: [
                (166, 206, 227),
                (31, 120, 180),
                (178, 223, 138)],
            4: [
                (166, 206, 227),
                (31, 120, 180),
                (178, 223, 138),
                (51, 160, 44)],
            5: [
                (166, 206, 227),
                (31, 120, 180),
                (178, 223, 138),
                (51, 160, 44),
                (251, 154, 153)],
            6: [
                (166, 206, 227),
                (31, 120, 180),
                (178, 223, 138),
                (51, 160, 44),
                (251, 154, 153),
                (227, 26, 28)],
            7: [
                (166, 206, 227),
                (31, 120, 180),
                (178, 223, 138),
                (51, 160, 44),
                (251, 154, 153),
                (227, 26, 28),
                (253, 191, 111)],
            8: [
                (166, 206, 227),
                (31, 120, 180),
                (178, 223, 138),
                (51, 160, 44),
                (251, 154, 153),
                (227, 26, 28),
                (253, 191, 111),
                (255, 127, 0)],
            9: [
                (166, 206, 227),
                (31, 120, 180),
                (178, 223, 138),
                (51, 160, 44),
                (251, 154, 153),
                (227, 26, 28),
                (253, 191, 111),
                (255, 127, 0),
                (202, 178, 214)],
            10: [
                (166, 206, 227),
                (31, 120, 180),
                (178, 223, 138),
                (51, 160, 44),
                (251, 154, 153),
                (227, 26, 28),
                (253, 191, 111),
                (255, 127, 0),
                (202, 178, 214),
                (106, 61, 154)],
            11: [
                (166, 206, 227),
                (31, 120, 180),
                (178, 223, 138),
                (51, 160, 44),
                (251, 154, 153),
                (227, 26, 28),
                (253, 191, 111),
                (255, 127, 0),
                (202, 178, 214),
                (106, 61, 154),
                (255, 255, 153)],
            12: [
                (166, 206, 227),
                (31, 120, 180),
                (178, 223, 138),
                (51, 160, 44),
                (251, 154, 153),
                (227, 26, 28),
                (253, 191, 111),
                (255, 127, 0),
                (202, 178, 214),
                (106, 61, 154),
                (255, 255, 153),
                (177, 89, 40)], "type": "qual"},
        "Pastel2": {
            3: [
                (179, 226, 205),
                (253, 205, 172),
                (203, 213, 232)],
            4: [
                (179, 226, 205),
                (253, 205, 172),
                (203, 213, 232),
                (244, 202, 228)],
            5: [
                (179, 226, 205),
                (253, 205, 172),
                (203, 213, 232),
                (244, 202, 228),
                (230, 245, 201)],
            6: [
                (179, 226, 205),
                (253, 205, 172),
                (203, 213, 232),
                (244, 202, 228),
                (230, 245, 201),
                (255, 242, 174)],
            7: [
                (179, 226, 205),
                (253, 205, 172),
                (203, 213, 232),
                (244, 202, 228),
                (230, 245, 201),
                (255, 242, 174),
                (241, 226, 204)],
            8: [
                (179, 226, 205),
                (253, 205, 172),
                (203, 213, 232),
                (244, 202, 228),
                (230, 245, 201),
                (255, 242, 174),
                (241, 226, 204),
                (204, 204, 204)], "type": "qual"},
        "Pastel1": {
            3: [
                (251, 180, 174),
                (179, 205, 227),
                (204, 235, 197)],
            4: [
                (251, 180, 174),
                (179, 205, 227),
                (204, 235, 197),
                (222, 203, 228)],
            5: [
                (251, 180, 174),
                (179, 205, 227),
                (204, 235, 197),
                (222, 203, 228),
                (254, 217, 166)],
            6: [
                (251, 180, 174),
                (179, 205, 227),
                (204, 235, 197),
                (222, 203, 228),
                (254, 217, 166),
                (255, 255, 204)],
            7: [
                (251, 180, 174),
                (179, 205, 227),
                (204, 235, 197),
                (222, 203, 228),
                (254, 217, 166),
                (255, 255, 204),
                (229, 216, 189)],
            8: [
                (251, 180, 174),
                (179, 205, 227),
                (204, 235, 197),
                (222, 203, 228),
                (254, 217, 166),
                (255, 255, 204),
                (229, 216, 189),
                (253, 218, 236)],
            9: [
                (251, 180, 174),
                (179, 205, 227),
                (204, 235, 197),
                (222, 203, 228),
                (254, 217, 166),
                (255, 255, 204),
                (229, 216, 189),
                (253, 218, 236),
                (242, 242, 242)], "type": "qual"},
        "RedOrange": {
            3: [
                (254, 232, 200),
                (253, 187, 132),
                (227, 74, 51)],
            4: [
                (254, 240, 217),
                (253, 204, 138),
                (252, 141, 89),
                (215, 48, 31)],
            5: [
                (254, 240, 217),
                (253, 204, 138),
                (252, 141, 89),
                (227, 74, 51),
                (179, 0, 0)],
            6: [
                (254, 240, 217),
                (253, 212, 158),
                (253, 187, 132),
                (252, 141, 89),
                (227, 74, 51),
                (179, 0, 0)],
            7: [
                (254, 240, 217),
                (253, 212, 158),
                (253, 187, 132),
                (252, 141, 89),
                (239, 101, 72),
                (215, 48, 31),
                (153, 0, 0)],
            8: [
                (255, 247, 236),
                (254, 232, 200),
                (253, 212, 158),
                (253, 187, 132),
                (252, 141, 89),
                (239, 101, 72),
                (215, 48, 31),
                (153, 0, 0)],
            9: [
                (255, 247, 236),
                (254, 232, 200),
                (253, 212, 158),
                (253, 187, 132),
                (252, 141, 89),
                (239, 101, 72),
                (215, 48, 31),
                (179, 0, 0),
                (127, 0, 0)], "type": "seq", "reverse": True},
        "BluePurple": {
            3: [
                (236, 231, 242),
                (166, 189, 219),
                (43, 140, 190)],
            4: [
                (241, 238, 246),
                (189, 201, 225),
                (116, 169, 207),
                (5, 112, 176)],
            5: [
                (241, 238, 246),
                (189, 201, 225),
                (116, 169, 207),
                (43, 140, 190),
                (4, 90, 141)],
            6: [
                (241, 238, 246),
                (208, 209, 230),
                (166, 189, 219),
                (116, 169, 207),
                (43, 140, 190),
                (4, 90, 141)],
            7: [
                (241, 238, 246),
                (208, 209, 230),
                (166, 189, 219),
                (116, 169, 207),
                (54, 144, 192),
                (5, 112, 176),
                (3, 78, 123)],
            8: [
                (255, 247, 251),
                (236, 231, 242),
                (208, 209, 230),
                (166, 189, 219),
                (116, 169, 207),
                (54, 144, 192),
                (5, 112, 176),
                (3, 78, 123)],
            9: [
                (255, 247, 251),
                (236, 231, 242),
                (208, 209, 230),
                (166, 189, 219),
                (116, 169, 207),
                (54, 144, 192),
                (5, 112, 176),
                (4, 90, 141),
                (2, 56, 88)], "type": "seq", "reverse": True},
        "PurpleBlue": {
            3: [
                (224, 236, 244),
                (158, 188, 218),
                (136, 86, 167)],
            4: [
                (237, 248, 251),
                (179, 205, 227),
                (140, 150, 198),
                (136, 65, 157)],
            5: [
                (237, 248, 251),
                (179, 205, 227),
                (140, 150, 198),
                (136, 86, 167),
                (129, 15, 124)],
            6: [
                (237, 248, 251),
                (191, 211, 230),
                (158, 188, 218),
                (140, 150, 198),
                (136, 86, 167),
                (129, 15, 124)],
            7: [
                (237, 248, 251),
                (191, 211, 230),
                (158, 188, 218),
                (140, 150, 198),
                (140, 107, 177),
                (136, 65, 157),
                (110, 1, 107)],
            8: [
                (247, 252, 253),
                (224, 236, 244),
                (191, 211, 230),
                (158, 188, 218),
                (140, 150, 198),
                (140, 107, 177),
                (136, 65, 157),
                (110, 1, 107)],
            9: [
                (247, 252, 253),
                (224, 236, 244),
                (191, 211, 230),
                (158, 188, 218),
                (140, 150, 198),
                (140, 107, 177),
                (136, 65, 157),
                (129, 15, 124),
                (77, 0, 75)], "type": "seq", "reverse": True},
        "Oranges": {
            3: [
                (254, 230, 206),
                (253, 174, 107),
                (230, 85, 13)],
            4: [
                (254, 237, 222),
                (253, 190, 133),
                (253, 141, 60),
                (217, 71, 1)],
            5: [
                (254, 237, 222),
                (253, 190, 133),
                (253, 141, 60),
                (230, 85, 13),
                (166, 54, 3)],
            6: [
                (254, 237, 222),
                (253, 208, 162),
                (253, 174, 107),
                (253, 141, 60),
                (230, 85, 13),
                (166, 54, 3)],
            7: [
                (254, 237, 222),
                (253, 208, 162),
                (253, 174, 107),
                (253, 141, 60),
                (241, 105, 19),
                (217, 72, 1),
                (140, 45, 4)],
            8: [
                (255, 245, 235),
                (254, 230, 206),
                (253, 208, 162),
                (253, 174, 107),
                (253, 141, 60),
                (241, 105, 19),
                (217, 72, 1),
                (140, 45, 4)],
            9: [
                (255, 245, 235),
                (254, 230, 206),
                (253, 208, 162),
                (253, 174, 107),
                (253, 141, 60),
                (241, 105, 19),
                (217, 72, 1),
                (166, 54, 3),
                (127, 39, 4)], "type": "seq", "reverse": True},
        "GreenBlue": {
            3: [
                (229, 245, 249),
                (153, 216, 201),
                (44, 162, 95)],
            4: [
                (237, 248, 251),
                (178, 226, 226),
                (102, 194, 164),
                (35, 139, 69)],
            5: [
                (237, 248, 251),
                (178, 226, 226),
                (102, 194, 164),
                (44, 162, 95),
                (0, 109, 44)],
            6: [
                (237, 248, 251),
                (204, 236, 230),
                (153, 216, 201),
                (102, 194, 164),
                (44, 162, 95),
                (0, 109, 44)],
            7: [
                (237, 248, 251),
                (204, 236, 230),
                (153, 216, 201),
                (102, 194, 164),
                (65, 174, 118),
                (35, 139, 69),
                (0, 88, 36)],
            8: [
                (247, 252, 253),
                (229, 245, 249),
                (204, 236, 230),
                (153, 216, 201),
                (102, 194, 164),
                (65, 174, 118),
                (35, 139, 69),
                (0, 88, 36)],
            9: [
                (247, 252, 253),
                (229, 245, 249),
                (204, 236, 230),
                (153, 216, 201),
                (102, 194, 164),
                (65, 174, 118),
                (35, 139, 69),
                (0, 109, 44),
                (0, 68, 27)], "type": "seq", "reverse": True},
        "BrownOrangeYellow": {
            3: [
                (255, 247, 188),
                (254, 196, 79),
                (217, 95, 14)],
            4: [
                (255, 255, 212),
                (254, 217, 142),
                (254, 153, 41),
                (204, 76, 2)],
            5: [
                (255, 255, 212),
                (254, 217, 142),
                (254, 153, 41),
                (217, 95, 14),
                (153, 52, 4)],
            6: [
                (255, 255, 212),
                (254, 227, 145),
                (254, 196, 79),
                (254, 153, 41),
                (217, 95, 14),
                (153, 52, 4)],
            7: [
                (255, 255, 212),
                (254, 227, 145),
                (254, 196, 79),
                (254, 153, 41),
                (236, 112, 20),
                (204, 76, 2),
                (140, 45, 4)],
            8: [
                (255, 255, 229),
                (255, 247, 188),
                (254, 227, 145),
                (254, 196, 79),
                (254, 153, 41),
                (236, 112, 20),
                (204, 76, 2),
                (140, 45, 4)],
            9: [
                (255, 255, 229),
                (255, 247, 188),
                (254, 227, 145),
                (254, 196, 79),
                (254, 153, 41),
                (236, 112, 20),
                (204, 76, 2),
                (153, 52, 4),
                (102, 37, 6)], "type": "seq", "reverse": True},
        "GreenYellow": {
            3: [
                (247, 252, 185),
                (173, 221, 142),
                (49, 163, 84)],
            4: [
                (255, 255, 204),
                (194, 230, 153),
                (120, 198, 121),
                (35, 132, 67)],
            5: [
                (255, 255, 204),
                (194, 230, 153),
                (120, 198, 121),
                (49, 163, 84),
                (0, 104, 55)],
            6: [
                (255, 255, 204),
                (217, 240, 163),
                (173, 221, 142),
                (120, 198, 121),
                (49, 163, 84),
                (0, 104, 55)],
            7: [
                (255, 255, 204),
                (217, 240, 163),
                (173, 221, 142),
                (120, 198, 121),
                (65, 171, 93),
                (35, 132, 67),
                (0, 90, 50)],
            8: [
                (255, 255, 229),
                (247, 252, 185),
                (217, 240, 163),
                (173, 221, 142),
                (120, 198, 121),
                (65, 171, 93),
                (35, 132, 67),
                (0, 90, 50)],
            9: [
                (255, 255, 229),
                (247, 252, 185),
                (217, 240, 163),
                (173, 221, 142),
                (120, 198, 121),
                (65, 171, 93),
                (35, 132, 67),
                (0, 104, 55),
                (0, 69, 41)], "type": "seq", "reverse": True},
        "Reds": {
            3: [
                (254, 224, 210),
                (252, 146, 114),
                (222, 45, 38)],
            4: [
                (254, 229, 217),
                (252, 174, 145),
                (251, 106, 74),
                (203, 24, 29)],
            5: [
                (254, 229, 217),
                (252, 174, 145),
                (251, 106, 74),
                (222, 45, 38),
                (165, 15, 21)],
            6: [
                (254, 229, 217),
                (252, 187, 161),
                (252, 146, 114),
                (251, 106, 74),
                (222, 45, 38),
                (165, 15, 21)],
            7: [
                (254, 229, 217),
                (252, 187, 161),
                (252, 146, 114),
                (251, 106, 74),
                (239, 59, 44),
                (203, 24, 29),
                (153, 0, 13)],
            8: [
                (255, 245, 240),
                (254, 224, 210),
                (252, 187, 161),
                (252, 146, 114),
                (251, 106, 74),
                (239, 59, 44),
                (203, 24, 29),
                (153, 0, 13)],
            9: [
                (255, 245, 240),
                (254, 224, 210),
                (252, 187, 161),
                (252, 146, 114),
                (251, 106, 74),
                (239, 59, 44),
                (203, 24, 29),
                (165, 15, 21),
                (103, 0, 13)], "type": "seq", "reverse": True},
        "PurpleRed": {
            3: [
                (253, 224, 221),
                (250, 159, 181),
                (197, 27, 138)],
            4: [
                (254, 235, 226),
                (251, 180, 185),
                (247, 104, 161),
                (174, 1, 126)],
            5: [
                (254, 235, 226),
                (251, 180, 185),
                (247, 104, 161),
                (197, 27, 138),
                (122, 1, 119)],
            6: [
                (254, 235, 226),
                (252, 197, 192),
                (250, 159, 181),
                (247, 104, 161),
                (197, 27, 138),
                (122, 1, 119)],
            7: [
                (254, 235, 226),
                (252, 197, 192),
                (250, 159, 181),
                (247, 104, 161),
                (221, 52, 151),
                (174, 1, 126),
                (122, 1, 119)],
            8: [
                (255, 247, 243),
                (253, 224, 221),
                (252, 197, 192),
                (250, 159, 181),
                (247, 104, 161),
                (221, 52, 151),
                (174, 1, 126),
                (122, 1, 119)],
            9: [
                (255, 247, 243),
                (253, 224, 221),
                (252, 197, 192),
                (250, 159, 181),
                (247, 104, 161),
                (221, 52, 151),
                (174, 1, 126),
                (122, 1, 119),
                (73, 0, 106)], "type": "seq", "reverse": True},
        "Greens": {
            3: [
                (229, 245, 224),
                (161, 217, 155),
                (49, 163, 84)],
            4: [
                (237, 248, 233),
                (186, 228, 179),
                (116, 196, 118),
                (35, 139, 69)],
            5: [
                (237, 248, 233),
                (186, 228, 179),
                (116, 196, 118),
                (49, 163, 84),
                (0, 109, 44)],
            6: [
                (237, 248, 233),
                (199, 233, 192),
                (161, 217, 155),
                (116, 196, 118),
                (49, 163, 84),
                (0, 109, 44)],
            7: [
                (237, 248, 233),
                (199, 233, 192),
                (161, 217, 155),
                (116, 196, 118),
                (65, 171, 93),
                (35, 139, 69),
                (0, 90, 50)],
            8: [
                (247, 252, 245),
                (229, 245, 224),
                (199, 233, 192),
                (161, 217, 155),
                (116, 196, 118),
                (65, 171, 93),
                (35, 139, 69),
                (0, 90, 50)],
            9: [
                (247, 252, 245),
                (229, 245, 224),
                (199, 233, 192),
                (161, 217, 155),
                (116, 196, 118),
                (65, 171, 93),
                (35, 139, 69),
                (0, 109, 44),
                (0, 68, 27)], "type": "seq", "reverse": True},
        "BlueGreenYellow": {
            3: [
                (237, 248, 177),
                (127, 205, 187),
                (44, 127, 184)],
            4: [
                (255, 255, 204),
                (161, 218, 180),
                (65, 182, 196),
                (34, 94, 168)],
            5: [
                (255, 255, 204),
                (161, 218, 180),
                (65, 182, 196),
                (44, 127, 184),
                (37, 52, 148)],
            6: [
                (255, 255, 204),
                (199, 233, 180),
                (127, 205, 187),
                (65, 182, 196),
                (44, 127, 184),
                (37, 52, 148)],
            7: [
                (255, 255, 204),
                (199, 233, 180),
                (127, 205, 187),
                (65, 182, 196),
                (29, 145, 192),
                (34, 94, 168),
                (12, 44, 132)],
            8: [
                (255, 255, 217),
                (237, 248, 177),
                (199, 233, 180),
                (127, 205, 187),
                (65, 182, 196),
                (29, 145, 192),
                (34, 94, 168),
                (12, 44, 132)],
            9: [
                (255, 255, 217),
                (237, 248, 177),
                (199, 233, 180),
                (127, 205, 187),
                (65, 182, 196),
                (29, 145, 192),
                (34, 94, 168),
                (37, 52, 148),
                (8, 29, 88)], "type": "seq", "reverse": True},
        "Purples": {
            3: [
                (239, 237, 245),
                (188, 189, 220),
                (117, 107, 177)],
            4: [
                (242, 240, 247),
                (203, 201, 226),
                (158, 154, 200),
                (106, 81, 163)],
            5: [
                (242, 240, 247),
                (203, 201, 226),
                (158, 154, 200),
                (117, 107, 177),
                (84, 39, 143)],
            6: [
                (242, 240, 247),
                (218, 218, 235),
                (188, 189, 220),
                (158, 154, 200),
                (117, 107, 177),
                (84, 39, 143)],
            7: [
                (242, 240, 247),
                (218, 218, 235),
                (188, 189, 220),
                (158, 154, 200),
                (128, 125, 186),
                (106, 81, 163),
                (74, 20, 134)],
            8: [
                (252, 251, 253),
                (239, 237, 245),
                (218, 218, 235),
                (188, 189, 220),
                (158, 154, 200),
                (128, 125, 186),
                (106, 81, 163),
                (74, 20, 134)],
            9: [
                (252, 251, 253),
                (239, 237, 245),
                (218, 218, 235),
                (188, 189, 220),
                (158, 154, 200),
                (128, 125, 186),
                (106, 81, 163),
                (84, 39, 143),
                (63, 0, 125)], "type": "seq", "reverse": True},
        "BlueGreen": {
            3: [
                (224, 243, 219),
                (168, 221, 181),
                (67, 162, 202)],
            4: [
                (240, 249, 232),
                (186, 228, 188),
                (123, 204, 196),
                (43, 140, 190)],
            5: [
                (240, 249, 232),
                (186, 228, 188),
                (123, 204, 196),
                (67, 162, 202),
                (8, 104, 172)],
            6: [
                (240, 249, 232),
                (204, 235, 197),
                (168, 221, 181),
                (123, 204, 196),
                (67, 162, 202),
                (8, 104, 172)],
            7: [
                (240, 249, 232),
                (204, 235, 197),
                (168, 221, 181),
                (123, 204, 196),
                (78, 179, 211),
                (43, 140, 190),
                (8, 88, 158)],
            8: [
                (247, 252, 240),
                (224, 243, 219),
                (204, 235, 197),
                (168, 221, 181),
                (123, 204, 196),
                (78, 179, 211),
                (43, 140, 190),
                (8, 88, 158)],
            9: [
                (247, 252, 240),
                (224, 243, 219),
                (204, 235, 197),
                (168, 221, 181),
                (123, 204, 196),
                (78, 179, 211),
                (43, 140, 190),
                (8, 104, 172),
                (8, 64, 129)], "type": "seq", "reverse": True},
        "Greys": {
            3: [
                (240, 240, 240),
                (189, 189, 189),
                (99, 99, 99)],
            4: [
                (247, 247, 247),
                (204, 204, 204),
                (150, 150, 150),
                (82, 82, 82)],
            5: [
                (247, 247, 247),
                (204, 204, 204),
                (150, 150, 150),
                (99, 99, 99),
                (37, 37, 37)],
            6: [
                (247, 247, 247),
                (217, 217, 217),
                (189, 189, 189),
                (150, 150, 150),
                (99, 99, 99),
                (37, 37, 37)],
            7: [
                (247, 247, 247),
                (217, 217, 217),
                (189, 189, 189),
                (150, 150, 150),
                (115, 115, 115),
                (82, 82, 82),
                (37, 37, 37)],
            8: [
                (255, 255, 255),
                (240, 240, 240),
                (217, 217, 217),
                (189, 189, 189),
                (150, 150, 150),
                (115, 115, 115),
                (82, 82, 82),
                (37, 37, 37)],
            9: [
                (255, 255, 255),
                (240, 240, 240),
                (217, 217, 217),
                (189, 189, 189),
                (150, 150, 150),
                (115, 115, 115),
                (82, 82, 82),
                (37, 37, 37),
                (0, 0, 0)], "type": "seq", "reverse": True},
        "RedOrangeYellow": {
            3: [
                (255, 237, 160),
                (254, 178, 76),
                (240, 59, 32)],
            4: [
                (255, 255, 178),
                (254, 204, 92),
                (253, 141, 60),
                (227, 26, 28)],
            5: [
                (255, 255, 178),
                (254, 204, 92),
                (253, 141, 60),
                (240, 59, 32),
                (189, 0, 38)],
            6: [
                (255, 255, 178),
                (254, 217, 118),
                (254, 178, 76),
                (253, 141, 60),
                (240, 59, 32),
                (189, 0, 38)],
            7: [
                (255, 255, 178),
                (254, 217, 118),
                (254, 178, 76),
                (253, 141, 60),
                (252, 78, 42),
                (227, 26, 28),
                (177, 0, 38)],
            8: [
                (255, 255, 204),
                (255, 237, 160),
                (254, 217, 118),
                (254, 178, 76),
                (253, 141, 60),
                (252, 78, 42),
                (227, 26, 28),
                (177, 0, 38)], "type": "seq", "reverse": True},
        "RedPurple": {
            3: [
                (231, 225, 239),
                (201, 148, 199),
                (221, 28, 119)],
            4: [
                (241, 238, 246),
                (215, 181, 216),
                (223, 101, 176),
                (206, 18, 86)],
            5: [
                (241, 238, 246),
                (215, 181, 216),
                (223, 101, 176),
                (221, 28, 119),
                (152, 0, 67)],
            6: [
                (241, 238, 246),
                (212, 185, 218),
                (201, 148, 199),
                (223, 101, 176),
                (221, 28, 119),
                (152, 0, 67)],
            7: [
                (241, 238, 246),
                (212, 185, 218),
                (201, 148, 199),
                (223, 101, 176),
                (231, 41, 138),
                (206, 18, 86),
                (145, 0, 63)],
            8: [
                (247, 244, 249),
                (231, 225, 239),
                (212, 185, 218),
                (201, 148, 199),
                (223, 101, 176),
                (231, 41, 138),
                (206, 18, 86),
                (145, 0, 63)],
            9: [
                (247, 244, 249),
                (231, 225, 239),
                (212, 185, 218),
                (201, 148, 199),
                (223, 101, 176),
                (231, 41, 138),
                (206, 18, 86),
                (152, 0, 67),
                (103, 0, 31)], "type": "seq", "reverse": True},
        "Blues": {
            3: [
                (222, 235, 247),
                (158, 202, 225),
                (49, 130, 189)],
            4: [
                (239, 243, 255),
                (189, 215, 231),
                (107, 174, 214),
                (33, 113, 181)],
            5: [
                (239, 243, 255),
                (189, 215, 231),
                (107, 174, 214),
                (49, 130, 189),
                (8, 81, 156)],
            6: [
                (239, 243, 255),
                (198, 219, 239),
                (158, 202, 225),
                (107, 174, 214),
                (49, 130, 189),
                (8, 81, 156)],
            7: [
                (239, 243, 255),
                (198, 219, 239),
                (158, 202, 225),
                (107, 174, 214),
                (66, 146, 198),
                (33, 113, 181),
                (8, 69, 148)],
            8: [
                (247, 251, 255),
                (222, 235, 247),
                (198, 219, 239),
                (158, 202, 225),
                (107, 174, 214),
                (66, 146, 198),
                (33, 113, 181),
                (8, 69, 148)],
            9: [
                (247, 251, 255),
                (222, 235, 247),
                (198, 219, 239),
                (158, 202, 225),
                (107, 174, 214),
                (66, 146, 198),
                (33, 113, 181),
                (8, 81, 156),
                (8, 48, 107)], "type": "seq", "reverse": True},
        "GreenBluePurple": {
            3: [
                (236, 226, 240),
                (166, 189, 219),
                (28, 144, 153)],
            4: [
                (246, 239, 247),
                (189, 201, 225),
                (103, 169, 207),
                (2, 129, 138)],
            5: [
                (246, 239, 247),
                (189, 201, 225),
                (103, 169, 207),
                (28, 144, 153),
                (1, 108, 89)],
            6: [
                (246, 239, 247),
                (208, 209, 230),
                (166, 189, 219),
                (103, 169, 207),
                (28, 144, 153),
                (1, 108, 89)],
            7: [
                (246, 239, 247),
                (208, 209, 230),
                (166, 189, 219),
                (103, 169, 207),
                (54, 144, 192),
                (2, 129, 138),
                (1, 100, 80)],
            8: [
                (255, 247, 251),
                (236, 226, 240),
                (208, 209, 230),
                (166, 189, 219),
                (103, 169, 207),
                (54, 144, 192),
                (2, 129, 138),
                (1, 100, 80)],
            9: [
                (255, 247, 251),
                (236, 226, 240),
                (208, 209, 230),
                (166, 189, 219),
                (103, 169, 207),
                (54, 144, 192),
                (2, 129, 138),
                (1, 108, 89),
                (1, 70, 54)], "type": "seq", "reverse": True},
        }


brewer = BrewerFactory()
"""Instance of :class:`toyplot.color.BrewerFactory`

Use this to create Toyplot color palettes and maps based on the Color Brewer 2.0 palettes.
"""

class LinearFactory(object):
    """Creates high-quality linear color maps by name."""
    def names(self):
        """Return a list of available map names."""
        return [name for name in self._data.keys()]

    def map(self, name, domain_min=None, domain_max=None):
        """Construct a named :py:class:`toyplot.color.LinearMap` instance.

        Parameters
        ----------
        name: :class:`str`
          The name of the map.  Use :py:meth:`toyplot.color.LinearFactory.names` to retrieve a list of available names.

        Returns
        -------
        map: :class:`toyplot.color.LinearMap`
        """
        palette = Palette([rgb(red, green, blue) for _, red, green, blue in self._data[name]])
        return LinearMap(palette=palette, domain_min=domain_min, domain_max=domain_max)

    def maps(self):
        """Return a (name, colormap) tuple for every map in the collection.

        Returns
        -------
        palettes: sequence of (:class:`str`, :class:`toyplot.color.DivergingMap`) tuples.
        """
        return [(name, self.map(name)) for name in self.names()]

    _data = collections.OrderedDict([
        ("Blackbody", [
            (0.0, 0.0, 0.0, 0.0),
            (0.015873015873, 0.0497734776566, 0.0152477941455, 0.00852887312598),
            (0.031746031746, 0.084855813636, 0.0304955882911, 0.017057746252),
            (0.047619047619, 0.110596777851, 0.045468486547, 0.0255866193779),
            (0.0634920634921, 0.131828466896, 0.0581726828908, 0.0341240566996),
            (0.0793650793651, 0.15396956097, 0.0666492584387, 0.0428429968035),
            (0.0952380952381, 0.177679162416, 0.0725166219647, 0.050823629234),
            (0.111111111111, 0.201904856852, 0.0780963813824, 0.0578148506676),
            (0.126984126984, 0.22659740784, 0.0833966086871, 0.0640284471441),
            (0.142857142857, 0.251720295995, 0.0884210421079, 0.0696046995283),
            (0.15873015873, 0.277244781506, 0.0931718709304, 0.0746415380267),
            (0.174603174603, 0.303147494519, 0.0976499344002, 0.0792101025496),
            (0.190476190476, 0.329403084274, 0.101856249237, 0.0834333445488),
            (0.206349206349, 0.355973461763, 0.105794993876, 0.0876339441208),
            (0.222222222222, 0.382848034388, 0.109463756409, 0.0918462462183),
            (0.238095238095, 0.410019181885, 0.112858537428, 0.0960705967607),
            (0.253968253968, 0.437479394285, 0.115974391474, 0.100307286568),
            (0.269841269841, 0.465221354411, 0.118805374491, 0.104556559102),
            (0.285714285714, 0.493237985431, 0.12134447042, 0.108818616983),
            (0.301587301587, 0.521522475956, 0.123583494231, 0.113093627519),
            (0.31746031746, 0.550068290666, 0.125512967442, 0.117381727397),
            (0.333333333333, 0.57886917165, 0.12712196061, 0.121683026697),
            (0.349206349206, 0.607919133853, 0.128397895268, 0.125997612321),
            (0.365079365079, 0.637212456877, 0.129326295006, 0.130325550956),
            (0.380952380952, 0.666743674634, 0.129890471593, 0.134666891619),
            (0.396825396825, 0.691292894468, 0.141293283089, 0.136258919233),
            (0.412698412698, 0.706485699582, 0.170344592267, 0.132534602103),
            (0.428571428571, 0.721654217074, 0.19689465803, 0.128274044848),
            (0.444444444444, 0.736799548299, 0.221800939447, 0.12340916854),
            (0.460317460317, 0.751922741791, 0.245555262747, 0.117853905198),
            (0.47619047619, 0.767024796621, 0.268467312199, 0.111496560918),
            (0.492063492063, 0.782106665487, 0.290745094317, 0.104187424625),
            (0.507936507937, 0.797169257565, 0.312535115222, 0.0957174093272),
            (0.52380952381, 0.812213441141, 0.333944389252, 0.0857782387212),
            (0.539682539683, 0.827240046048, 0.355053366625, 0.073879942571),
            (0.555555555556, 0.842249865912, 0.375923953617, 0.0591516202944),
            (0.571428571429, 0.857243660245, 0.396604712155, 0.039717323074),
            (0.587301587302, 0.870379942456, 0.418565674041, 0.0197163850683),
            (0.603174603175, 0.874344023609, 0.446974056864, 0.0181687081555),
            (0.619047619048, 0.878025845405, 0.47466075806, 0.0167976393343),
            (0.634920634921, 0.881420328496, 0.501760962635, 0.015617018173),
            (0.650793650794, 0.884522146084, 0.528379005009, 0.0146406842395),
            (0.666666666667, 0.887325704879, 0.554597071914, 0.013882477102),
            (0.68253968254, 0.889825124527, 0.58048102161, 0.0133562363286),
            (0.698412698413, 0.892014215292, 0.606084400817, 0.0130758014873),
            (0.714285714286, 0.893886453749, 0.631451293491, 0.0130550121463),
            (0.730158730159, 0.895434956251, 0.656618388603, 0.0133077078736),
            (0.746031746032, 0.89665244983, 0.681616511604, 0.0138477282374),
            (0.761904761905, 0.897531240228, 0.706471778936, 0.0146889128057),
            (0.777777777778, 0.898063176628, 0.731206482064, 0.0158451011466),
            (0.793650793651, 0.898239612652, 0.755839773918, 0.0173301328282),
            (0.809523809524, 0.89805136309, 0.780388208579, 0.0191578474186),
            (0.825396825397, 0.897488655734, 0.804866170399, 0.0213420844859),
            (0.84126984127, 0.896541077606, 0.829286218697, 0.0238966835982),
            (0.857142857143, 0.913697911059, 0.845646813981, 0.222765707352),
            (0.873015873016, 0.929653817018, 0.862126431003, 0.33192044996),
            (0.888888888889, 0.944238596146, 0.878764667333, 0.425002143402),
            (0.904761904762, 0.957362272625, 0.895566343629, 0.511514604922),
            (0.920634920635, 0.968933860547, 0.912535569382, 0.594836247911),
            (0.936507936508, 0.978859451813, 0.929675808036, 0.676549211736),
            (0.952380952381, 0.987040267732, 0.946989936457, 0.757507161315),
            (0.968253968254, 0.993370582651, 0.964480299321, 0.838212075166),
            (0.984126984127, 0.997735414612, 0.982148758928, 0.918976236288),
            (1.0, 1.0, 1.0, 1.0),
            ]),
        ("ExtendedBlackbody", [
            (0.0, 0.0, 0.0, 0.0),
            (0.015873015873, 0.0410204653528, 0.0125357909278, 0.0689109347353),
            (0.031746031746, 0.0728292511021, 0.0251074193759, 0.111084701438),
            (0.047619047619, 0.0914725053853, 0.0382924505445, 0.150828141972),
            (0.0634920634921, 0.103435457753, 0.0498523739394, 0.192399506279),
            (0.0793650793651, 0.11697787554, 0.0553384939223, 0.235590084984),
            (0.0952380952381, 0.13106897058, 0.0574858157959, 0.28012851826),
            (0.111111111111, 0.14451899335, 0.0588070736298, 0.325831740794),
            (0.126984126984, 0.157365748413, 0.0592310259517, 0.372622130916),
            (0.142857142857, 0.169638222229, 0.0586571629275, 0.420432193125),
            (0.15873015873, 0.181358128671, 0.0569469344531, 0.469202864472),
            (0.174603174603, 0.192541718123, 0.053903275425, 0.518882124122),
            (0.190476190476, 0.203200974518, 0.049231841621, 0.569423844856),
            (0.206349206349, 0.213344430591, 0.0424592716177, 0.620786858997),
            (0.222222222222, 0.22885083664, 0.0323118386732, 0.667716252697),
            (0.238095238095, 0.263917734376, 0.0170229151511, 0.696700251951),
            (0.253968253968, 0.297886776896, 0.0, 0.725911289487),
            (0.269841269841, 0.331147696924, 0.0, 0.755344187716),
            (0.285714285714, 0.363946896841, 0.0, 0.784994035048),
            (0.301587301587, 0.396448879507, 0.0, 0.814856165251),
            (0.31746031746, 0.428767984311, 0.0, 0.844926138887),
            (0.333333333333, 0.460986165649, 0.0, 0.875199726605),
            (0.349206349206, 0.509059764325, 0.0, 0.874878090633),
            (0.365079365079, 0.586657040025, 0.0, 0.788483458434),
            (0.380952380952, 0.647525018598, 0.0, 0.703448899692),
            (0.396825396825, 0.697310408138, 0.0, 0.61974037226),
            (0.412698412698, 0.739133997894, 0.0, 0.53725751376),
            (0.428571428571, 0.774966161238, 0.0, 0.455769190891),
            (0.444444444444, 0.806168536879, 0.0, 0.374768042226),
            (0.460317460317, 0.833747021783, 0.0227410599117, 0.293092362571),
            (0.47619047619, 0.854040299862, 0.09354692431, 0.239815658098),
            (0.492063492063, 0.86584929908, 0.151233844244, 0.239392814342),
            (0.507936507937, 0.877555741581, 0.194962727652, 0.23874888687),
            (0.52380952381, 0.889160050233, 0.232289833256, 0.237874380272),
            (0.539682539683, 0.900662633109, 0.265865002202, 0.236758898038),
            (0.555555555556, 0.912063883111, 0.296966217671, 0.235391010074),
            (0.571428571429, 0.923364177686, 0.326317530516, 0.233758094872),
            (0.587301587302, 0.934563878629, 0.354372124996, 0.231846149973),
            (0.603174603175, 0.945663331952, 0.381433685093, 0.229639562377),
            (0.619047619048, 0.956662867807, 0.407716114152, 0.227120827894),
            (0.634920634921, 0.96756280046, 0.433375921467, 0.224270204635),
            (0.650793650794, 0.978363428298, 0.458531111592, 0.22106528053),
            (0.666666666667, 0.975483038855, 0.493783717836, 0.21455014879),
            (0.68253968254, 0.97122066712, 0.528209235633, 0.20714036059),
            (0.698412698413, 0.966451052441, 0.56138151885, 0.198927581099),
            (0.714285714286, 0.961153380556, 0.593535622168, 0.189790175914),
            (0.730158730159, 0.955305133435, 0.624849458821, 0.17956891477),
            (0.746031746032, 0.948881871951, 0.655461076484, 0.168048219356),
            (0.761904761905, 0.941856982438, 0.685479806242, 0.154923356801),
            (0.777777777778, 0.934201379395, 0.714993736449, 0.139738100068),
            (0.793650793651, 0.925883154566, 0.744074884731, 0.121752089424),
            (0.809523809524, 0.916867159951, 0.772782874939, 0.0996076368025),
            (0.825396825397, 0.907114508751, 0.801167612557, 0.0702264586709),
            (0.84126984127, 0.896581973444, 0.829271271014, 0.0241364485172),
            (0.857142857143, 0.913697911059, 0.845646813981, 0.222765707352),
            (0.873015873016, 0.929653817018, 0.862126431003, 0.33192044996),
            (0.888888888889, 0.944238596146, 0.878764667333, 0.425002143402),
            (0.904761904762, 0.957362272625, 0.895566343629, 0.511514604922),
            (0.920634920635, 0.968933860547, 0.912535569382, 0.594836247911),
            (0.936507936508, 0.978859451813, 0.929675808036, 0.676549211736),
            (0.952380952381, 0.987040267732, 0.946989936457, 0.757507161315),
            (0.968253968254, 0.993370582651, 0.964480299321, 0.838212075166),
            (0.984126984127, 0.997735414612, 0.982148758928, 0.918976236288),
            (1.0, 1.0, 1.0, 1.0),
            ]),
        ("Kindlmann", [
            (0.0, 0.0, 0.0, 0.0),
            (0.015873015873, 0.0671185329588, 0.00322224968401, 0.0636827982308),
            (0.031746031746, 0.107829620358, 0.00527193539053, 0.110584717909),
            (0.047619047619, 0.132822207081, 0.00761865377028, 0.158685364855),
            (0.0634920634921, 0.150658364632, 0.00977706834929, 0.204368743721),
            (0.0793650793651, 0.164513703673, 0.0117840704797, 0.246150470866),
            (0.0952380952381, 0.17635738249, 0.0136716834002, 0.287096916371),
            (0.111111111111, 0.186956701473, 0.0157459008722, 0.330140235882),
            (0.126984126984, 0.196609134947, 0.0179376087423, 0.374519096987),
            (0.142857142857, 0.2058836328, 0.0200081348995, 0.419451331093),
            (0.15873015873, 0.215553664962, 0.0221102465109, 0.463608665805),
            (0.174603174603, 0.226519452924, 0.0241216136235, 0.506117428928),
            (0.190476190476, 0.239514530077, 0.0260436809284, 0.546294801685),
            (0.206349206349, 0.250904916966, 0.0280614987688, 0.588999620164),
            (0.222222222222, 0.249817749702, 0.0308415106025, 0.646402205149),
            (0.238095238095, 0.214242447671, 0.0350037426956, 0.732877018055),
            (0.253968253968, 0.0580253778952, 0.0728643854324, 0.831022738042),
            (0.269841269841, 0.0367499971596, 0.164763702978, 0.770392363186),
            (0.285714285714, 0.0335272327849, 0.22111999029, 0.703052629353),
            (0.301587301587, 0.0307269848338, 0.262580080746, 0.640328823938),
            (0.31746031746, 0.0281909469934, 0.295692282825, 0.584878656573),
            (0.333333333333, 0.0256345140463, 0.323638967672, 0.537652138675),
            (0.349206349206, 0.0239684879129, 0.348256161303, 0.498334574679),
            (0.365079365079, 0.0224741887644, 0.370718323302, 0.466267149604),
            (0.380952380952, 0.0213578271529, 0.391778498521, 0.440286960104),
            (0.396825396825, 0.0203201805033, 0.411937775621, 0.419241969322),
            (0.412698412698, 0.0208128086974, 0.431596539161, 0.400454861389),
            (0.428571428571, 0.021854471454, 0.451151641812, 0.380313980138),
            (0.444444444444, 0.0230712391057, 0.470629535023, 0.358711501755),
            (0.460317460317, 0.0233722345904, 0.490071489565, 0.335491504837),
            (0.47619047619, 0.0249491579525, 0.509419733567, 0.310616410835),
            (0.492063492063, 0.0254113583837, 0.528747638664, 0.283789671987),
            (0.507936507937, 0.0265511754015, 0.548001432252, 0.255097177506),
            (0.52380952381, 0.0275272678001, 0.56719680403, 0.224620515107),
            (0.539682539683, 0.0288835693814, 0.586306830784, 0.193022962508),
            (0.555555555556, 0.0289206421838, 0.605358177366, 0.161427264774),
            (0.571428571429, 0.0298263835637, 0.624285254063, 0.133059337268),
            (0.587301587302, 0.0308293566636, 0.643105492554, 0.112622799332),
            (0.603174603175, 0.0316208723034, 0.661869577571, 0.102453272786),
            (0.619047619048, 0.0331152985419, 0.68067601948, 0.0949485127762),
            (0.634920634921, 0.0345435219144, 0.699700412917, 0.0699256651954),
            (0.650793650794, 0.0857184757511, 0.717719140782, 0.0342188050111),
            (0.666666666667, 0.175139323574, 0.733108825242, 0.0350250894642),
            (0.68253968254, 0.251518174426, 0.747272852278, 0.0360866952214),
            (0.698412698413, 0.32393651684, 0.760140598481, 0.0363956325921),
            (0.714285714286, 0.395075620074, 0.771599170072, 0.0373892404385),
            (0.730158730159, 0.465330965142, 0.781654750673, 0.0372943827485),
            (0.746031746032, 0.535176000781, 0.790252205312, 0.0377717872748),
            (0.761904761905, 0.604490052123, 0.797425818444, 0.037983205084),
            (0.777777777778, 0.673240541923, 0.803195625374, 0.0389751481252),
            (0.793650793651, 0.741211512026, 0.807646935033, 0.0389840587975),
            (0.809523809524, 0.809722616014, 0.810405609028, 0.0389139062698),
            (0.825396825397, 0.884677097587, 0.809315141207, 0.0422072429217),
            (0.84126984127, 0.961041572569, 0.804311591633, 0.182431699323),
            (0.857142857143, 0.976621102575, 0.813785197546, 0.509571446188),
            (0.873015873016, 0.982984770875, 0.829568990311, 0.644079693295),
            (0.888888888889, 0.987002084869, 0.848098160851, 0.728496452077),
            (0.904761904762, 0.9899438027, 0.868188821379, 0.789375598354),
            (0.920634920635, 0.992130297633, 0.889285349012, 0.837111330813),
            (0.936507936508, 0.993977903803, 0.91097796791, 0.876642196307),
            (0.952380952381, 0.995740780243, 0.932999641601, 0.91092373222),
            (0.968253968254, 0.997106329898, 0.955300428452, 0.942209465159),
            (0.984126984127, 0.998512698466, 0.977660727116, 0.971567030755),
            (1.0, 1.0, 1.0, 1.0),
            ]),
        ("ExtendedKindlmann", [
            (0.0, 0.0, 0.0, 0.0),
            (0.015873015873, 0.0665872190856, 0.00317348530238, 0.0660895850313),
            (0.031746031746, 0.105381244894, 0.00562454296989, 0.117187973649),
            (0.047619047619, 0.126123053183, 0.00837798019045, 0.174964238809),
            (0.0634920634921, 0.137680744083, 0.0110625831087, 0.231566300512),
            (0.0793650793651, 0.145039082102, 0.013451479997, 0.282277543576),
            (0.0952380952381, 0.152044276014, 0.0156859399984, 0.327623693074),
            (0.111111111111, 0.161138270143, 0.0176484986723, 0.369879578682),
            (0.126984126984, 0.172685805995, 0.0195648094698, 0.409048640995),
            (0.142857142857, 0.165244050347, 0.0224832200874, 0.47021606479),
            (0.15873015873, 0.0279918458412, 0.0373112977636, 0.583889898993),
            (0.174603174603, 0.0238593181565, 0.127541825162, 0.499528856699),
            (0.190476190476, 0.0202386790283, 0.173243934499, 0.422468500932),
            (0.206349206349, 0.0172147086694, 0.204326250648, 0.360918661076),
            (0.222222222222, 0.0151405787086, 0.228521481166, 0.315024556602),
            (0.238095238095, 0.0137064006539, 0.249278518333, 0.281945765499),
            (0.253968253968, 0.0130509562483, 0.268304082234, 0.257774660955),
            (0.269841269841, 0.0139459196116, 0.286752940039, 0.234259017963),
            (0.285714285714, 0.0147354562034, 0.305005386829, 0.208719146502),
            (0.301587301587, 0.0155954467859, 0.323085920627, 0.180811206659),
            (0.31746031746, 0.0164494399433, 0.341015039205, 0.150220485094),
            (0.333333333333, 0.0172595614171, 0.358784804599, 0.117294366612),
            (0.349206349206, 0.0182093863706, 0.376357630368, 0.0845231419061),
            (0.365079365079, 0.0190863651751, 0.3937190206, 0.059250497456),
            (0.380952380952, 0.0200967930623, 0.410922707788, 0.049733608345),
            (0.396825396825, 0.020763380415, 0.428313466899, 0.0314984637501),
            (0.412698412698, 0.0813196226022, 0.443521025455, 0.0212422538125),
            (0.428571428571, 0.154492186368, 0.456128474882, 0.0218404104551),
            (0.444444444444, 0.22436299475, 0.466598243329, 0.0224293240327),
            (0.460317460317, 0.293165415215, 0.474818917034, 0.0228389362808),
            (0.47619047619, 0.361087617102, 0.480786997283, 0.0230247509697),
            (0.492063492063, 0.427869336004, 0.484593045332, 0.0230890727087),
            (0.507936507937, 0.494710180878, 0.485909764738, 0.0239295955349),
            (0.52380952381, 0.571030341606, 0.481000290069, 0.027614468239),
            (0.539682539683, 0.659238616311, 0.466351530046, 0.0317364210825),
            (0.555555555556, 0.759019086035, 0.437421423072, 0.036400614635),
            (0.571428571429, 0.866948968961, 0.388363362964, 0.0413685026023),
            (0.587301587302, 0.956773664209, 0.334498978088, 0.0929916734685),
            (0.603174603175, 0.962500599909, 0.364829931363, 0.213272013492),
            (0.619047619048, 0.96531706949, 0.39732820503, 0.272635650325),
            (0.634920634921, 0.968204554641, 0.427383873897, 0.332558246158),
            (0.650793650794, 0.972456233298, 0.452132993621, 0.42362405976),
            (0.666666666667, 0.974924322329, 0.475311962572, 0.523734287229),
            (0.68253968254, 0.975989878868, 0.497598275123, 0.620461989691),
            (0.698412698413, 0.977020548467, 0.518704726869, 0.710319751135),
            (0.714285714286, 0.978023338129, 0.539236804307, 0.792434027154),
            (0.730158730159, 0.978917589225, 0.559781782268, 0.866134059622),
            (0.746031746032, 0.979938765414, 0.580626873885, 0.930969250325),
            (0.761904761905, 0.973007886008, 0.607681188528, 0.981198138945),
            (0.777777777778, 0.933324131326, 0.657798954369, 0.983583414204),
            (0.793650793651, 0.908309474089, 0.697018458541, 0.985524181948),
            (0.809523809524, 0.894668785948, 0.729537811457, 0.987056417428),
            (0.825396825397, 0.889934261241, 0.757640205324, 0.988334733592),
            (0.84126984127, 0.892048970738, 0.782727772582, 0.989640628941),
            (0.857142857143, 0.898924549826, 0.805934065795, 0.990584977084),
            (0.873015873016, 0.908996109804, 0.827911240696, 0.991685867082),
            (0.888888888889, 0.916820311909, 0.850623202421, 0.992856600763),
            (0.904761904762, 0.920183803811, 0.874775808751, 0.99393928426),
            (0.920634920635, 0.921584746406, 0.899420945982, 0.9951557335),
            (0.936507936508, 0.923619461565, 0.923730853729, 0.996269632514),
            (0.952380952381, 0.928399919483, 0.947174005275, 0.996489083038),
            (0.968253968254, 0.937779381782, 0.969167619817, 0.996973557569),
            (0.984126984127, 0.95568711212, 0.988614720577, 0.997872974429),
            (1.0, 1.0, 1.0, 1.0),
            ]),
    ])


linear = LinearFactory()
"""Instance of :class:`toyplot.color.LinearFactory`

Use this to create Toyplot linear color maps by name.
"""


class DivergingFactory(object):
    """Creates high-quality diverging color maps by name."""
    def names(self):
        """Return a list of available map names."""
        return [name for name in sorted(self._data.keys())]

    def map(self, name, domain_min=None, domain_max=None):
        """Construct a named :py:class:`toyplot.color.DivergingMap` instance.

        Parameters
        ----------
        name: :class:`str`
          The name of the map.  Use :py:meth:`toyplot.color.DivergingFactory.names` to retrieve a list of available names.

        Returns
        -------
        map: :class:`toyplot.color.DivergingMap`
        """
        low, high = self._data[name]
        return DivergingMap(low, high, domain_min, domain_max)

    def maps(self):
        """Return a (name, colormap) tuple for every map in the collection.

        Returns
        -------
        palettes: sequence of (:class:`str`, :class:`toyplot.color.DivergingMap`) tuples.
        """
        return [(name, self.map(name)) for name in self.names()]

    _data = {
        "BlueBrown": (rgb(0.217, 0.525, 0.910), rgb(0.677, 0.492, 0.093)),
        "BlueRed": (rgb(0.230, 0.299, 0.754), rgb(0.706, 0.016, 0.150)),
        "GreenRed": (rgb(0.085, 0.532, 0.201), rgb(0.758, 0.214, 0.233)),
        "PurpleGreen": (rgb(0.436, 0.308, 0.631), rgb(0.085, 0.532, 0.201)),
        "PurpleOrange": (rgb(0.436, 0.308, 0.631), rgb(0.759, 0.334, 0.046)),
    }

diverging = DivergingFactory()
"""Instance of :class:`toyplot.color.DivergingFactory`

Use this to create Toyplot diverging color maps by name.
"""


def to_css(color):
    """Convert a Toyplot color to a CSS string.

    Parameters
    ----------
    color: :class:`numpy.ndarray`
        Array of RGBA values with dtype = :data:`toyplot.color.dtype`, which is converted to a CSS rgba() color.

    Returns
    -------
    css: :class:`str` containing a CSS color value.
      """
    return "rgba(%.1f%%,%.1f%%,%.1f%%,%.3f)" % (color["r"] * 100, color["g"] * 100, color["b"] * 100, color["a"])


def css(value):
    """Construct a Toyplot color from a CSS string.

    Parameters
    ----------
    value: :class:`str`

    Returns
    -------
    color: :class:`numpy.ndarray` scalar containing RGBA values with dtype = :data:`toyplot.color.dtype`.
    """
    if value.lower() in css.names:
        color = css.names[value.lower()]
        return rgba(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, 1.0)

    if value.lower() == "transparent":
        return rgba(0, 0, 0, 0)

    match = css.hex3(value)
    if match:
        r, g, b = [int(group * 2, 16) / 255.0 for group in match.groups()]
        return rgba(r, g, b, 1)

    match = css.hex6(value)
    if match:
        r, g, b = [int(group, 16) / 255.0 for group in match.groups()]
        return rgba(r, g, b, 1)

    match = css.rgb(value)
    if match:
        r, g, b = [int(group) / 255.0 for group in match.groups()]
        return rgba(r, g, b, 1)

    match = css.rgb_percent(value)
    if match:
        r, g, b = [float(group) / 100.0 for group in match.groups()]
        return rgba(r, g, b, 1)

    match = css.rgba(value)
    if match:
        r, g, b, a = [
            int(group) / 255.0 for group in match.groups()[:3]] + [float(match.groups()[3])]
        return rgba(r, g, b, a)

    match = css.rgba_percent(value)
    if match:
        r, g, b, a = [
            float(group) / 100.0 for group in match.groups()[:3]] + [float(match.groups()[3])]
        return rgba(r, g, b, a)

    match = css.hsl(value)
    if match:
        h, s, l = [float(group) for group in match.groups()]
        r, g, b = colorsys.hls_to_rgb((h / 360.0) % 1, l / 100.0, s / 100.0)
        return rgba(r, g, b, 1)

    match = css.hsla(value)
    if match:
        h, s, l, a = [float(group) for group in match.groups()]
        r, g, b = colorsys.hls_to_rgb((h / 360.0) % 1, l / 100.0, s / 100.0)
        return rgba(r, g, b, a)

css.hex3 = re.compile(r"^#([\da-f])([\da-f])([\da-f])$", re.I).match
css.hex6 = re.compile(r"^#([\da-f]{2})([\da-f]{2})([\da-f]{2})$", re.I).match
css.rgb = re.compile(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\)").match
css.rgb_percent = re.compile(r"rgb\(\s*(.*)%\s*,\s*(.*)%\s*,\s*(.*)%\)").match
css.rgba = re.compile(r"rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(.*)\)").match
css.rgba_percent = re.compile(r"rgba\(\s*(.*)%\s*,\s*(.*)%\s*,\s*(.*)%,\s*(.*)\)").match
css.hsl = re.compile(r"hsl\(\s*(.*)\s*,\s*(.*)%\s*,\s*(.*)%\)").match
css.hsla = re.compile(r"hsla\(\s*(.*)\s*,\s*(.*)%\s*,\s*(.*)%,\s*(.*)\)").match
css.names = {
    "aliceblue": (240, 248, 255),
    "antiquewhite": (250, 235, 215),
    "aqua": (0, 255, 255),
    "aquamarine": (127, 255, 212),
    "azure": (240, 255, 255),
    "beige": (245, 245, 220),
    "bisque": (255, 228, 196),
    "black": (0, 0, 0),
    "blanchedalmond": (255, 235, 205),
    "blue": (0, 0, 255),
    "blueviolet": (138, 43, 226),
    "brown": (165, 42, 42),
    "burlywood": (222, 184, 135),
    "cadetblue": (95, 158, 160),
    "chartreuse": (127, 255, 0),
    "chocolate": (210, 105, 30),
    "coral": (255, 127, 80),
    "cornflowerblue": (100, 149, 237),
    "cornsilk": (255, 248, 220),
    "crimson": (220, 20, 60),
    "cyan": (0, 255, 255),
    "darkblue": (0, 0, 139),
    "darkcyan": (0, 139, 139),
    "darkgoldenrod": (184, 134, 11),
    "darkgray": (169, 169, 169),
    "darkgreen": (0, 100, 0),
    "darkgrey": (169, 169, 169),
    "darkkhaki": (189, 183, 107),
    "darkmagenta": (139, 0, 139),
    "darkolivegreen": (85, 107, 47),
    "darkorange": (255, 140, 0),
    "darkorchid": (153, 50, 204),
    "darkred": (139, 0, 0),
    "darksalmon": (233, 150, 122),
    "darkseagreen": (143, 188, 143),
    "darkslateblue": (72, 61, 139),
    "darkslategray": (47, 79, 79),
    "darkslategrey": (47, 79, 79),
    "darkturquoise": (0, 206, 209),
    "darkviolet": (148, 0, 211),
    "deeppink": (255, 20, 147),
    "deepskyblue": (0, 191, 255),
    "dimgray": (105, 105, 105),
    "dimgrey": (105, 105, 105),
    "dodgerblue": (30, 144, 255),
    "firebrick": (178, 34, 34),
    "floralwhite": (255, 250, 240),
    "forestgreen": (34, 139, 34),
    "fuchsia": (255, 0, 255),
    "gainsboro": (220, 220, 220),
    "ghostwhite": (248, 248, 255),
    "gold": (255, 215, 0),
    "goldenrod": (218, 165, 32),
    "gray": (128, 128, 128),
    "green": (0, 128, 0),
    "greenyellow": (173, 255, 47),
    "grey": (128, 128, 128),
    "honeydew": (240, 255, 240),
    "hotpink": (255, 105, 180),
    "indianred": (205, 92, 92),
    "indigo": (75, 0, 130),
    "ivory": (255, 255, 240),
    "khaki": (240, 230, 140),
    "lavender": (230, 230, 250),
    "lavenderblush": (255, 240, 245),
    "lawngreen": (124, 252, 0),
    "lemonchiffon": (255, 250, 205),
    "lightblue": (173, 216, 230),
    "lightcoral": (240, 128, 128),
    "lightcyan": (224, 255, 255),
    "lightgoldenrodyellow": (250, 250, 210),
    "lightgray": (211, 211, 211),
    "lightgreen": (144, 238, 144),
    "lightgrey": (211, 211, 211),
    "lightpink": (255, 182, 193),
    "lightsalmon": (255, 160, 122),
    "lightseagreen": (32, 178, 170),
    "lightskyblue": (135, 206, 250),
    "lightslategray": (119, 136, 153),
    "lightslategrey": (119, 136, 153),
    "lightsteelblue": (176, 196, 222),
    "lightyellow": (255, 255, 224),
    "lime": (0, 255, 0),
    "limegreen": (50, 205, 50),
    "linen": (250, 240, 230),
    "magenta": (255, 0, 255),
    "maroon": (128, 0, 0),
    "mediumaquamarine": (102, 205, 170),
    "mediumblue": (0, 0, 205),
    "mediumorchid": (186, 85, 211),
    "mediumpurple": (147, 112, 219),
    "mediumseagreen": (60, 179, 113),
    "mediumslateblue": (123, 104, 238),
    "mediumspringgreen": (0, 250, 154),
    "mediumturquoise": (72, 209, 204),
    "mediumvioletred": (199, 21, 133),
    "midnightblue": (25, 25, 112),
    "mintcream": (245, 255, 250),
    "mistyrose": (255, 228, 225),
    "moccasin": (255, 228, 181),
    "navajowhite": (255, 222, 173),
    "navy": (0, 0, 128),
    "oldlace": (253, 245, 230),
    "olive": (128, 128, 0),
    "olivedrab": (107, 142, 35),
    "orange": (255, 165, 0),
    "orangered": (255, 69, 0),
    "orchid": (218, 112, 214),
    "palegoldenrod": (238, 232, 170),
    "palegreen": (152, 251, 152),
    "paleturquoise": (175, 238, 238),
    "palevioletred": (219, 112, 147),
    "papayawhip": (255, 239, 213),
    "peachpuff": (255, 218, 185),
    "peru": (205, 133, 63),
    "pink": (255, 192, 203),
    "plum": (221, 160, 221),
    "powderblue": (176, 224, 230),
    "purple": (128, 0, 128),
    "red": (255, 0, 0),
    "rosybrown": (188, 143, 143),
    "royalblue": (65, 105, 225),
    "saddlebrown": (139, 69, 19),
    "salmon": (250, 128, 114),
    "sandybrown": (244, 164, 96),
    "seagreen": (46, 139, 87),
    "seashell": (255, 245, 238),
    "sienna": (160, 82, 45),
    "silver": (192, 192, 192),
    "skyblue": (135, 206, 235),
    "slateblue": (106, 90, 205),
    "slategray": (112, 128, 144),
    "slategrey": (112, 128, 144),
    "snow": (255, 250, 250),
    "springgreen": (0, 255, 127),
    "steelblue": (70, 130, 180),
    "tan": (210, 180, 140),
    "teal": (0, 128, 128),
    "thistle": (216, 191, 216),
    "tomato": (255, 99, 71),
    "turquoise": (64, 224, 208),
    "violet": (238, 130, 238),
    "wheat": (245, 222, 179),
    "white": (255, 255, 255),
    "whitesmoke": (245, 245, 245),
    "yellow": (255, 255, 0),
    "yellowgreen": (154, 205, 50),
}
