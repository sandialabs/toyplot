# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Functions for broadcasting values into 1D or 2D arrays.

The functions in this module are used by Toyplot to handle the conversion from
`constant`, `per-series`, and `per-datum` values into their canonical 1D and 2D
array representations.
"""


import numpy


def scalar(value, shape):
    """Return a 1D or 2D array of floats with the given shape.

    Parameters
    ----------
    shape: (tuple)
        Shape of the desired output array.  A 1-tuple will produce a 1D output
        vector containing :math:`N` per-series values.  A 2-tuple will produce an :math:`M \\times N`
        output matrix of per-datum values grouped into :math:`N` series.

    Returns
    -------
    array: :class:`numpy.ndarray`
    """
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


def pyobject(value, shape):
    """Return a 1D or 2D array of objects with the given shape.

    Parameters
    ----------
    shape: (tuple)
        Shape of the desired output array.  A 1-tuple will produce a 1D output
        vector containing :math:`N` per-series values.  A 2-tuple will produce an :math:`M \\times N`
        output matrix of per-datum values grouped into :math:`N` series.

    Returns
    -------
    array: :class:`numpy.ndarray`
    """
    array = numpy.array(value)
    # As a special-case, allow a vector with shape M to be matched-up with an
    # M x 1 matrix.
    if array.ndim == 1 and isinstance(shape, tuple) and len(
            shape) == 2 and array.shape[0] == shape[0] and shape[1] == 1:
        return numpy.reshape(array, shape)
    result = numpy.empty(shape, dtype="object")
    result.flat = [u for u, _ in numpy.broadcast(array, result)]
    return result
