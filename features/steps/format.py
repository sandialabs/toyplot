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
    context.formatter = toyplot.format.UnitFormatter(nanshow=False, units="inches")


@then(
    u'formatting inch units with the toyplot.format.UnitFormatter should produce valid output')
def step_impl(context):
    val = context.formatter.format(12.2)
    prefix, separator, suffix = val
    nose.tools.assert_equal(prefix, "12")
    nose.tools.assert_equal(separator, ".")
    nose.tools.assert_equal(suffix, "2 in")


@then(
    u'formatting point units with the toyplot.format.UnitFormatter should produce valid output')
def step_impl(context):
    val = context.formatter.format(5.1)
    prefix, separator, suffix = val
    nose.tools.assert_equal(prefix, "5")
    nose.tools.assert_equal(separator, ".")
    nose.tools.assert_equal(suffix, "1 in")

    val = context.formatter.format(5)
    prefix, separator, suffix = val
    nose.tools.assert_equal(prefix, "5 in")
    nose.tools.assert_equal(separator, "")
    nose.tools.assert_equal(suffix, "")

@then(
    u'formatting units with the toyplot.format.UnitFormatter should handle invalid input correctly')
def step_impl(context):
    val = context.formatter.format("5")
    prefix, separator, suffix = val
    nose.tools.assert_equal(prefix, "5")
    nose.tools.assert_equal(separator, "")
    nose.tools.assert_equal(suffix, "")

    val = context.formatter.format("test", "")
    prefix, separator, suffix = val
    nose.tools.assert_equal(prefix, "test")
    nose.tools.assert_equal(separator, "")
    nose.tools.assert_equal(suffix, "")

    prefix, dp, suffix = context.formatter.format(numpy.nan)
    nose.tools.assert_equal(prefix, "")
    nose.tools.assert_equal(dp, "")
    nose.tools.assert_equal(suffix, "")


@given(u'an instance of toyplot.format.CurrencyFormatter')
def step_impl(context):
    context.formatter = toyplot.format.CurrencyFormatter(curr="cad", nanshow=False)


@then(
    u'formatting Canadian currency with the toyplot.format.CurrencyFormatter should produce valid output')
def step_impl(context):
    prefix, dp, suffix = context.formatter.format(100.00)
    nose.tools.assert_equal(prefix, "$100")
    nose.tools.assert_equal(dp, ".")
    nose.tools.assert_equal(suffix, "00")

    prefix, dp, suffix = context.formatter.format(50)
    nose.tools.assert_equal(prefix, "$50")
    nose.tools.assert_equal(dp, ".")
    nose.tools.assert_equal(suffix, "00")


@then(
    u'formatting European currency with the toyplot.format.CurrencyFormatter should produce valid output')
def step_impl(context):
    context.formatter = toyplot.format.CurrencyFormatter(curr="eur", nanshow=False)
    val = context.formatter.format(9000.56)
    prefix, dp, suffix = val
    nose.tools.assert_equal(prefix, u"\u20AC" +"9,000")
    nose.tools.assert_equal(dp, ".")
    nose.tools.assert_equal(suffix, "56")

@then(
    u'formatting British currency with the toyplot.format.CurrencyFormatter should produce valid output')
def step_impl(context):
    context.formatter = toyplot.format.CurrencyFormatter(curr="gbp", nanshow=False)
    val = context.formatter.format(23423410.5)
    prefix, dp, suffix = val
    nose.tools.assert_equal(prefix, u"\u00a3" +"23,423,410")
    nose.tools.assert_equal(dp, ".")
    nose.tools.assert_equal(suffix, "50")

@then(
    u'formatting currency with the toyplot.format.CurrencyFormatter should handle errors correctly')
def step_impl(context):
    prefix, dp, suffix = context.formatter.format("test")
    nose.tools.assert_equal(prefix, "")
    nose.tools.assert_equal(dp, "")
    nose.tools.assert_equal(suffix, "")

    prefix, dp, suffix = context.formatter.format(numpy.nan)
    nose.tools.assert_equal(prefix, "")
    nose.tools.assert_equal(dp, "")
    nose.tools.assert_equal(suffix, "")
