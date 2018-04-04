# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import nose.tools
import numpy.testing
import toyplot.format


@given(u'an instance of toyplot.format.DefaultFormatter')
def step_impl(context):
    context.formatter = toyplot.format.DefaultFormatter()


@then(
    u'formatting strings with the toyplot.format.DefaultFormatter should produce valid output')
def step_impl(context):
    prefix, separator, suffix = context.formatter.format("1")
    nose.tools.assert_equal(prefix, "1")
    nose.tools.assert_equal(separator, "")
    nose.tools.assert_equal(suffix, "")


@then(
    u'formatting integers with the toyplot.format.DefaultFormatter should produce valid output')
def step_impl(context):
    prefix, separator, suffix = context.formatter.format(1)
    nose.tools.assert_equal(prefix, "1")
    nose.tools.assert_equal(separator, "")
    nose.tools.assert_equal(suffix, "")


@given(u'an instance of toyplot.format.FloatFormatter')
def step_impl(context):
    context.formatter = toyplot.format.FloatFormatter()


@then(
    u'formatting floats with the toyplot.format.FloatFormatter should produce valid output')
def step_impl(context):
    column = numpy.arange(4) + 0.1
    prefix, separator, suffix = context.formatter.format(4.1)
    nose.tools.assert_equal(prefix, "4")
    nose.tools.assert_equal(separator, ".")
    nose.tools.assert_equal(suffix, "1")


@then(
    u'formatting integers with the toyplot.format.FloatFormatter should produce valid output')
def step_impl(context):
    prefix, separator, suffix = context.formatter.format(1)
    nose.tools.assert_equal(prefix, "1")
    nose.tools.assert_equal(separator, "")
    nose.tools.assert_equal(suffix, "")

    
@given(u'an instance of toyplot.format.UnitFormatter')
def step_impl(context):
    context.formatter = toyplot.format.UnitFormatter()


@then(
    u'formatting inch units with the toyplot.format.UnitFormatter should produce valid output')
def step_impl(context):
    val = context.formatter.format(12.2, "inches")
    prefix, separator, suffix, units = val
    nose.tools.assert_equal(prefix, "12")
    nose.tools.assert_equal(separator, ".")
    nose.tools.assert_equal(suffix, "2")
    nose.tools.assert_equal(units, "in")


@then(
    u'formatting point units with the toyplot.format.UnitFormatter should produce valid output')
def step_impl(context):
    val = context.formatter.format(5.1, "points")
    prefix, separator, suffix, units = val
    nose.tools.assert_equal(prefix, "5")
    nose.tools.assert_equal(separator, ".")
    nose.tools.assert_equal(suffix, "1")
    nose.tools.assert_equal(units, "pt")


@given(u'an instance of toyplot.format.CurrencyFormatter')
def step_impl(context):
    context.formatter = toyplot.format.CurrencyFormatter(curr="cad")


@then(
    u'formatting Canadian currency with the toyplot.format.CurrencyFormatter should produce valid output')
def step_impl(context):
    codes, prefix, dp, suffix = context.formatter.format(100.00)
    nose.tools.assert_equal(codes, "$")
    nose.tools.assert_equal(prefix, "100")
    nose.tools.assert_equal(dp, ".")
    nose.tools.assert_equal(suffix, "00")


@then(
    u'formatting European currency with the toyplot.format.CurrencyFormatter should produce valid output')
def step_impl(context):
    context.formatter = toyplot.format.CurrencyFormatter(curr="eur")
    val = context.formatter.format(9000.56)
    codes, prefix, dp, suffix = val
    nose.tools.assert_equal(codes, "€")
    nose.tools.assert_equal(prefix, "9,000")
    nose.tools.assert_equal(dp, ".")
    nose.tools.assert_equal(suffix, "56")

@then(
    u'formatting British currency with the toyplot.format.CurrencyFormatter should produce valid output')
def step_impl(context):
    context.formatter = toyplot.format.CurrencyFormatter(curr="gbp")
    val = context.formatter.format(23423410.5)
    codes, prefix, dp, suffix = val
    nose.tools.assert_equal(codes, "£")
    nose.tools.assert_equal(prefix, "23,423,410")
    nose.tools.assert_equal(dp, ".")
    nose.tools.assert_equal(suffix, "50")
