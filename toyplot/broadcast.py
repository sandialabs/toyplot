# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import numpy


def scalar(value, shape):
    array = numpy.array(value).astype("float64")
    # As a special-case, allow a vector with shape M to be matched-up with an
    # M x 1 matrix.
    if array.ndim == 1 and isinstance(shape, tuple) and len(
            shape) == 2 and array.shape[0] == shape[0] and shape[1] == 1:
        return numpy.reshape(array, shape)
    return numpy.broadcast_arrays(array, numpy.empty(shape))[0]


#def string(value, shape):
#    array = numpy.array(value).astype("unicode")
#    # As a special-case, allow a vector with shape M to be matched-up with an
#    # M x 1 matrix.
#    if array.ndim == 1 and isinstance(shape, tuple) and len(
#            shape) == 2 and array.shape[0] == shape[0] and shape[1] == 1:
#        return numpy.reshape(array, shape)
#    return numpy.broadcast_arrays(array, numpy.empty(shape))[0]


def object(value, shape):
    array = numpy.array(value)
    # As a special-case, allow a vector with shape M to be matched-up with an
    # M x 1 matrix.
    if array.ndim == 1 and isinstance(shape, tuple) and len(
            shape) == 2 and array.shape[0] == shape[0] and shape[1] == 1:
        return numpy.reshape(array, shape)
    result = numpy.empty(shape, dtype="object")
    result.flat = [u for u, v in numpy.broadcast(array, result)]
    return result
