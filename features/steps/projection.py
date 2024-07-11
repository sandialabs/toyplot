# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import test
import numpy.testing

import toyplot.projection


@given(u'A linear projection with 0, 1 and 0, 100')
def step_impl(context):
    context.projection = toyplot.projection.linear(0, 1, 0, 100)


@then(u'0 should project to 0')
def step_impl(context):
    test.assert_equal(context.projection(0), 0)
    test.assert_equal(context.projection.inverse(0), 0)


@then(u'0.5 should project to 50')
def step_impl(context):
    test.assert_equal(context.projection(0.5), 50)
    test.assert_equal(context.projection.inverse(50), 0.5)


@then(u'1 should project to 100')
def step_impl(context):
    test.assert_equal(context.projection(1.0), 100)
    test.assert_equal(context.projection.inverse(100), 1.0)


@given(u'A log10 projection with 1, 100 and 0, 100')
def step_impl(context):
    context.projection = toyplot.projection.log(10, 1, 100, 0, 100)


@then(u'1 should project to 0')
def step_impl(context):
    test.assert_equal(context.projection(1), 0)
    test.assert_equal(context.projection.inverse(0), 1)


@then(u'10 should project to 50')
def step_impl(context):
    test.assert_equal(context.projection(10), 50)
    test.assert_equal(context.projection.inverse(50), 10)


@then(u'100 should project to 100')
def step_impl(context):
    test.assert_equal(context.projection(100), 100)
    test.assert_equal(context.projection.inverse(100), 100)


@given(u'A log10 projection with -100, 100 and 0, 100')
def step_impl(context):
    context.projection = toyplot.projection.log(10, -100, 100, 0, 100)


@then(u'-100 should project to 0')
def step_impl(context):
    test.assert_equal(context.projection(-100), 0)
    test.assert_equal(context.projection.inverse(0), -100)


@then(u'0 should project to 50')
def step_impl(context):
    test.assert_equal(context.projection(0), 50)
    test.assert_equal(context.projection.inverse(50), 0)
