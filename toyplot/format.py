# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numpy


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


class DefaultFormatter(Formatter):

    def format(self, value):
        return "%s" % value, "", ""


class FloatFormatter(Formatter):

    def __init__(self, format="{:.6g}"):
        self._format = format

    def format(self, value):
        try:
            formatted = self._format.format(value).split(".")
            if len(formatted) == 1:
                return formatted[0], "", ""
            return formatted[0], ".", formatted[1]
        except:
            return str(value), "", ""
