# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Strategy objects for formatting text."""


import numbers
import warnings

import custom_inherit
import numpy

import toyplot


class Formatter(object, metaclass=custom_inherit.DocInheritMeta(style="numpy_napoleon")):
    """Abstract interface for formatters - objects that compute text representations from data."""

    def format(self, value):
        """Return a text representation of the given value.

        Parameters
        ----------
        value: value to be formatted

        Returns
        -------
        prefix : string
          Formatted data to be displayed before the separator.
        separator : string
          Separator between formatted data, or empty string.
        suffix : string
          Formatted data to be displayed after the separator, or empty string.
        """
        raise NotImplementedError() # pragma: no cover


class NullFormatter(Formatter):
    """Do-nothing formatter that returns empty strings."""
    def format(self, value):
        return "", "", ""


class BasicFormatter(Formatter):
    """Convert data to its default string representation."""
    def __init__(self, nanshow=True):
        self._nanshow = nanshow

    def format(self, value):
        try:
            if not self._nanshow and numpy.isnan(value):
                return "", "", ""
        except:
            pass

        return "%s" % value, "", ""


class FloatFormatter(BasicFormatter):
    """Formats floating-point values with aligned decimal points.

    Parameters
    ----------
    format: format string, optional
        Uses standard Python Format String Syntax.
    nanshow: bool, optional
        Set to `False` to hide NaN values.
    """
    def __init__(self, format="{:.6g}", nanshow=True):
        super(FloatFormatter, self).__init__(nanshow=nanshow)
        self._format = format

    def format(self, value):
        if isinstance(value, numbers.Number) and not numpy.isnan(value):
            formatted = self._format.format(value).split(".")
            if len(formatted) == 1:
                return formatted[0], "", ""
            return formatted[0], ".", formatted[1]

        return super(FloatFormatter, self).format(value)


class UnitFormatter(BasicFormatter):
    """Formats values with corresponding units

    Parameters
    ----------
    format: format string, optional
        Uses standard Python Format String Syntax.
    nanshow: bool, optional
        Set to `False` to hide NaN values.
    """

    def __init__(self, format="{:.6g}", nanshow=True, units='pt'):
        super(UnitFormatter, self).__init__(nanshow=nanshow)
        self._format = format
        self._units = units

        if units not in UnitFormatter._units:
            raise Exception("Incorrect type of units provided") #pragma: no cover

    def format(self, value):
        """Return a text representation of the given value.

        Parameters
        ----------
        value: value to be formatted
        units: units to be formatted

        Returns
        -------
        prefix : string
          Formatted data to be displayed before the separator.
        separator : string
          Separator between formatted data, or empty string.
        suffix : string
          Formatted data to be displayed after the separator, or empty string.
        units : string
          Formatted units to be displayed after the suffix, or empty string.
        """

        if isinstance(value, numbers.Number) and not numpy.isnan(value):
            formatted = self._format.format(value).split(".")
            if len(formatted) == 1:
                return formatted[0] +" " +UnitFormatter._units[self._units], "", ""
            return formatted[0], ".", formatted[1] +" " +UnitFormatter._units[self._units]

        return super(UnitFormatter, self).format(value)

UnitFormatter._units = {
    "centimeter": "cm",
    "centimeters": "cm",
    "cm": "cm",
    "decimeter": "dm",
    "decimeters": "dm",
    "dm": "dm",
    "in": "in",
    "inch": "in",
    "inches": "in",
    "m": "m",
    "meter": "m",
    "meters": "m",
    "millimeter": "mm",
    "millimeters": "mm",
    "mm": "mm",
    "pc": "pc",
    "pica": "pc",
    "picas": "pc",
    "pixel": "px",
    "pixels": "px",
    "point": "pt",
    "points": "pt",
    "pt": "pt",
    "px": "px",
}



class CurrencyFormatter(BasicFormatter):
    """Formats currency value with corresponding codes

    Parameters
    ----------
    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period) only specify as blank when places is zero
    """
    def __init__(self, format="{:,.2f}", nanshow=True, curr='cad', sep=',', dp='.',):
        super(CurrencyFormatter, self).__init__(nanshow=nanshow)
        self._format = format
        self._curr = curr
        self._sep = sep
        self._dp = dp

        if self._curr not in CurrencyFormatter._codes:
            raise Exception("Incorrect currency provided") #pragma: no cover

    def format(self, value):
        """Return a text representation of the given currency value.

        Parameters
        ----------
        value: value to be formatted

        Returns
        -------
        codes : string
          Formatted currency code to be displayed before the prefix, or empty string.
        prefix : string
          Formatted data to be displayed before the separator.
        dp : string
          Separator between formatted data, or empty string.
        suffix : string
          Formatted data to be displayed after the separator, or empty string.
        """

        if isinstance(value, numbers.Number) and not numpy.isnan(value):
            formatted = self._format.format(value).split(".")
            return CurrencyFormatter._codes[self._curr] + formatted[0], self._dp, formatted[1]

        return super(CurrencyFormatter, self).format(value)

CurrencyFormatter._codes = {
        "aud": "$",
        "cad": "$",
        "eur": u"\u20AC",
        "gbp": u"\u00a3",
        "hkd": "HK$",
        "usd": "$",
}
