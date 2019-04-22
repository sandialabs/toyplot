# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functions used by the Toyplot implementation to validate inputs.  These are not intended for end-users.
"""


import numbers
import numpy

def instance(value, types):
    """Raise an exception if a value isn't one of the given type(s)."""
    if not isinstance(value, types):
        raise ValueError("Expected %s, received %s." % (types, type(value))) # pragma: no cover
    return value


def value_in(value, choices):
    """Raise an exception if a value doesn't match one of the given choices."""
    if value not in choices:
        raise ValueError("Expected one of %s, received %r." % (", ".join([repr(choice) for choice in choices]), value)) # pragma: no cover
    return value


def table_keys(table, keys, length=None, min_length=None, modulus=None):
    """Raise an exception if any of the given keys fails to match the column keys in the given table."""
    keys = string_vector(keys, length=length, min_length=min_length, modulus=modulus)
    allowed = list(table.keys())
    for key in keys:
        if key not in allowed:
            raise ValueError("Table key must match one of %s, received %s." % (", ".join(allowed), key)) # pragma: no cover
    return keys


def scalar(value):
    """Raise an exception if a value isn't a number."""
    if not isinstance(value, numbers.Number):
        raise ValueError("Expected a number, received %s." % value) # pragma: no cover
    return value


def scalar_array(value):
    """Raise an exception if a value isn't convertable to an array of numbers."""
    array = numpy.ma.array(value).astype("float64")
    array.mask = numpy.ma.mask_or(array.mask, ~numpy.isfinite(array))
    return array


def vector(value, length=None, min_length=None, modulus=None):
    """Raise an exception if a value isn't convertable to a 1D array."""
    array = numpy.ma.array(value)
    if array.shape == ():
        array = numpy.ma.repeat(array, 1)
    if array.ndim != 1:
        raise ValueError("Expected a vector.") # pragma: no cover
    if length is not None:
        if len(array) != length:
            raise ValueError("Expected %s values, received %s" % (length, len(array))) # pragma: no cover
    if min_length is not None:
        if len(array) < min_length:
            raise ValueError("Expected %s or more values, received %s" % (min_length, len(array))) # pragma: no cover
    if modulus is not None:
        if len(array) % modulus != 0:
            raise ValueError("Expected a multiple of %s values, received %s" % (modulus, len(array))) # pragma: no cover
    return array


def integer_vector(value, length=None, min_length=None, modulus=None):
    """Raise an exception if a value isn't convertable to a 1D array of integers."""
    return vector(value, length=length, min_length=min_length, modulus=modulus).astype("int64")


def scalar_vector(value, length=None, min_length=None, modulus=None):
    """Raise an exception if a value isn't convertable to a 1D array of numbers."""
    return vector(value, length=length, min_length=min_length, modulus=modulus).astype("float64")


def string_vector(value, length=None, min_length=None, modulus=None):
    """Raise an exception if a value isn't convertable to a 1D array of numbers."""
    return vector(value, length=length, min_length=min_length, modulus=modulus).astype("unicode")


def scalar_matrix(value, rows=None, columns=None):
    """Raise an exception if a value isn't convertable to a 2D array of numbers."""
    array = scalar_array(value)
    if array.ndim != 2:
        raise ValueError("Expected a matrix.") # pragma: no cover
    if rows is not None:
        if array.shape[0] != rows:
            raise ValueError("Expected %s rows, received %s." % (rows, array.shape[0])) # pragma: no cover
    if columns is not None:
        if array.shape[1] != columns:
            raise ValueError("Expected %s columns, received %s." % (columns, array.shape[1])) # pragma: no cover
    return array


def optional_string(value):
    """Raise an exception if a value isn't a string, or None."""
    if not isinstance(value, (str, type(None))):
        raise ValueError("Expected a string value or None, received %s." % value) # pragma: no cover
    return value


def filename(value):
    """Raise an exception if a value isn't a valid string filename, or None."""
    return optional_string(value)


def hyperlink(value):
    """Raise an exception if a value isn't a valid string hyperlink, or None."""
    return optional_string(value)
