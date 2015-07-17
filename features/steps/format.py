from behave import *

import nose.tools
import numpy.testing
import toyplot.format


@given(u'an instance of toyplot.format.DefaultFormatter')
def step_impl(context):
    context.formatter = toyplot.format.DefaultFormatter()


@then(u'formatting strings with the toyplot.format.DefaultFormatter should produce valid output')
def step_impl(context):
    prefix, separator, suffix = context.formatter.format("1")
    nose.tools.assert_equal(prefix, "1")
    nose.tools.assert_equal(separator, "")
    nose.tools.assert_equal(suffix, "")


@then(u'formatting integers with the toyplot.format.DefaultFormatter should produce valid output')
def step_impl(context):
    prefix, separator, suffix = context.formatter.format(1)
    nose.tools.assert_equal(prefix, "1")
    nose.tools.assert_equal(separator, "")
    nose.tools.assert_equal(suffix, "")


@given(u'an instance of toyplot.format.FloatFormatter')
def step_impl(context):
    context.formatter = toyplot.format.FloatFormatter()


@then(u'formatting floats with the toyplot.format.FloatFormatter should produce valid output')
def step_impl(context):
    column = numpy.arange(4) + 0.1
    prefix, separator, suffix = context.formatter.format(4.1)
    nose.tools.assert_equal(prefix, "4")
    nose.tools.assert_equal(separator, ".")
    nose.tools.assert_equal(suffix, "1")


@then(u'formatting integers with the toyplot.format.FloatFormatter should produce valid output')
def step_impl(context):
    prefix, separator, suffix = context.formatter.format(1)
    nose.tools.assert_equal(prefix, "1")
    nose.tools.assert_equal(separator, "")
    nose.tools.assert_equal(suffix, "")
