# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numbers
import numpy
import toyplot.compatibility

def style(style):
  """Verify that the given object is usable as a style."""
  if not isinstance(style, (dict, type(None))):
    raise ValueError("Expected a dictionary of CSS styles or None, received %s." % style)
  return style

def instance(value, types):
  """Verify the type of a value."""
  if not isinstance(value, types):
    raise ValueError("Expected %s, received %s." % (types, type(value)))
  return value

def value_in(value, choices):
  if value not in choices:
    raise ValueError("Expected one of %s, received %s." % (",".join([str(choice) for choice in choices]), value))
  return value

def table_keys(table, keys, length=None, min_length=None):
  keys = string_vector(keys, length=length, min_length=min_length)
  allowed = list(table.keys())
  for key in keys:
    if key not in allowed:
      raise ValueError("Table key must match one of %s, received %s." % (", ".join(allowed), key))
  return keys

def scalar(value):
  if not isinstance(value, numbers.Number):
    raise ValueError("Expected a number, received %s." % value)
  return value

def scalar_array(value):
  array = numpy.ma.array(value).astype("float64")
  array.mask = numpy.ma.mask_or(array.mask, ~numpy.isfinite(array))
  return array

def scalar_vector(value, length=None):
  array = scalar_array(value)
  if array.shape == ():
    array = numpy.ma.repeat(array, 1)
  if array.ndim != 1:
    raise ValueError("Expected a vector.")
  if length is not None:
    if len(array) != length:
      raise ValueError("Expected %s values, received %s." % (length, len(array)))
  return array

def scalar_matrix(value, rows=None, columns=None):
  array = scalar_array(value)
  if array.ndim != 2:
    raise ValueError("Expected a matrix.")
  if rows is not None:
    if array.shape[0] != rows:
      raise ValueError("Expected %s rows, received %s." % (rows, array.shape[0]))
  if columns is not None:
    if array.shape[1] != columns:
      raise ValueError("Expected %s columns, received %s." % (columns, array.shape[1]))
  return array

def string(value):
  if not isinstance(value, toyplot.compatibility.string_type):
    raise ValueError("Expected a string, received %s." % value)
  return value

def string_vector(value, length=None, min_length=None):
  if isinstance(value, (toyplot.compatibility.string_type)):
    value = [value]
  array = numpy.ma.array(value).astype("str")
  if array.ndim != 1:
    raise ValueError("Expected a vector.")
  if length is not None:
    if len(array) != length:
      raise ValueError("Expected %s values, received %s" % (length, len(array)))
  if min_length is not None:
    if len(array) < min_length:
      raise ValueError("Expected %s or more values, received %s" % (min_length, len(array)))
  return array

def optional_string(value):
  if not isinstance(value, (toyplot.compatibility.string_type, type(None))):
    raise ValueError("Expected a string value or None, received %s." % value)
  return value

def marker_array(value, length=None):
  if isinstance(value, (toyplot.compatibility.string_type, tuple)):
    array = [value] * (1 if length is None else length)
  else:
    array = value
  if length is not None:
    if len(array) != length:
      raise ValueError("Expected %s values, received %s." % (length, len(array)))
  return array

