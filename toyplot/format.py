# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numpy

class ColumnFormatter(object):
  """Base class for column formatters - objects that compute text representations of column data."""
  def format(self, column):
    """Return a text representation of the given column.

    Parameters
    ----------
    column: numpy.ndarray

    Returns
    -------
    prefix : sequence of strings
      Formatted data to be displayed before the separator.
    separator : sequence of strings
      Optional separator between formatted data, or empty strings.
    suffix : numpy.ndarray of strings, or None
      Optional formatted data to be displayed after the separator, or empty strings.
    """
    raise NotImplementedError()

class DefaultFormatter(ColumnFormatter):
  def format(self, column):
    return (numpy.char.mod("%s", column), [""] * len(column), [""] * len(column))

class FloatFormatter(ColumnFormatter):
  def __init__(self, format="%.6g"):
    self._format = format

  def format(self, column):
    formatted = [(self._format % value).split(".") + ["."] for value in column]
    prefix, suffix, separator = zip(*formatted)
    return (prefix, separator, suffix)
