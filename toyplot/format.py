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
    left : numpy.ndarray of strings
      Formatted data to be displayed to the left of the separator.
    separator : numpy.ndarray of strings, or None
      Optional separator between formatted data.
    right : numpy.ndarray of strings, or None
      Optional formatted data to be displayed to the right of the separator.
    """
    raise NotImplementedError()

class DefaultFormatter(ColumnFormatter):
  def format(self, column):
    return (numpy.char.mod("%s", column), None, None)

class FloatFormatter(ColumnFormatter):
  def __init__(self, format="%.3g"):
    self._format = format

  def format(self, column):
    return (numpy.char.mod(self._format, column), None, None)
