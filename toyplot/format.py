# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Strategy objects for formatting text."""

from __future__ import division

import custom_inherit
import numpy
import six


@six.add_metaclass(custom_inherit.DocInheritMeta(style="numpy_napoleon"))
class Formatter(object):
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


class DefaultFormatter(Formatter):
    """Formats data using its default string representation."""
    def format(self, value):
        return "%s" % value, "", ""


class FloatFormatter(Formatter):
    """Formats floating-point values with aligned decimal points.

    Parameters
    ----------
    format: format string, optional
        Uses standard Python Format String Syntax.
    nanshow: bool, optional
        Set to `False` to hide NaN values.
    """
    def __init__(self, format="{:.6g}", nanshow=True):
        self._format = format
        self._nanshow = nanshow

    def format(self, value):
        if isinstance(value, six.string_types):
            return value, "", ""

        if numpy.isnan(value) and not self._nanshow:
            return "", "", ""

        formatted = self._format.format(value).split(".")
        if len(formatted) == 1:
            return formatted[0], "", ""
        return formatted[0], ".", formatted[1]


class UnitFormatter(Formatter):
    """Formats values with corresponding units
    
    Parameters
    ----------
    format: format string, optional
        Uses standard Python Format String Syntax.
    nanshow: bool, optional
        Set to `False` to hide NaN values.
    """

    def __init__(self, format="{:.6g}", nanshow=True, units='pt'):
        self._format = format
        self._nanshow = nanshow
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

        if isinstance(value, six.string_types):
            return value, "", ""

        if numpy.isnan(value) and not self._nanshow:
            return "", "", ""

        formatted = self._format.format(value).split(".")
        if len(formatted) == 1:
            return formatted[0] +" " +UnitFormatter._units[self._units], "", ""
        return formatted[0], ".", formatted[1] +" " +UnitFormatter._units[self._units]


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



class CurrencyFormatter(Formatter):
    """Formats currency value with corresponding codes
        places:  required number of places after the decimal point
        curr:    optional currency symbol before the sign (may be blank)
        sep:     optional grouping separator (comma, period, space, or blank)
        dp:      decimal point indicator (comma or period)
                 only specify as blank when places is zero
   """
    def __init__(self, format="{:,.2f}", nanshow=True, curr='cad',
        sep=',', dp='.',):
        self._format = format
        self._nanshow = nanshow
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
        if isinstance(value, six.string_types):
            return value, "", ""

        if numpy.isnan(value) and not self._nanshow:
            return "", "", ""

        formatted = self._format.format(value).split(".")
        return CurrencyFormatter._codes[self._curr] + formatted[0], self._dp, formatted[1]


CurrencyFormatter._codes = {
        "aud": "$", 
        "cad": "$",
        "eur": u"\u20AC",
        "gbp": u"\u00a3",
        "hkd": "HK$",
        "usd": "$",
}
