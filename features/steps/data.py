# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import test
import numpy.testing
import toyplot.data

@given(u'an array, contiguous regions of the array can be consolidated')
def step_impl(context):
    array = [1, 1, 2, 2, 2, 3, 4, 2, 2]
    begin, end, values = toyplot.data.contiguous(array)
    numpy.testing.assert_array_equal(begin, [0, 2, 5, 6, 7])
    numpy.testing.assert_array_equal(end, [2, 5, 6, 7, 9])
    numpy.testing.assert_array_equal(values, [1, 2, 3, 4, 2])

