# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numpy
import toyplot.compatibility


class Formatter(object):
    """Base class for formatters - objects that compute text representations from data."""

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
        if isinstance(value, toyplot.compatibility.string_type):
            return value, "", ""

        if numpy.isnan(value) and not self._nanshow:
            return "", "", ""

        formatted = self._format.format(value).split(".")
        if len(formatted) == 1:
            return formatted[0], "", ""
        return formatted[0], ".", formatted[1]
