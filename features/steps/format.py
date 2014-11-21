from behave import *

import nose.tools
import numpy.testing
import toyplot.format

@given(u'an instance of toyplot.format.DefaultFormatter')
def step_impl(context):
  context.formatter = toyplot.format.DefaultFormatter()

@then(u'formatting strings with the toyplot.format.DefaultFormatter should produce valid output')
def step_impl(context):
  column = numpy.arange(4).astype("string")
  prefixes, separators, suffixes = context.formatter.format(column)
  numpy.testing.assert_array_equal(prefixes, ["0", "1", "2", "3"])
  numpy.testing.assert_array_equal(separators, [""] * 4)
  numpy.testing.assert_array_equal(suffixes, [""] * 4)

@then(u'formatting integers with the toyplot.format.DefaultFormatter should produce valid output')
def step_impl(context):
  column = numpy.arange(4)
  prefixes, separators, suffixes = context.formatter.format(column)
  numpy.testing.assert_array_equal(prefixes, ["0", "1", "2", "3"])
  numpy.testing.assert_array_equal(separators, [""] * 4)
  numpy.testing.assert_array_equal(suffixes, [""] * 4)

@given(u'an instance of toyplot.format.FloatFormatter')
def step_impl(context):
  context.formatter = toyplot.format.FloatFormatter()

@then(u'formatting floats with the toyplot.format.FloatFormatter should produce valid output')
def step_impl(context):
  column = numpy.arange(4) + 0.1
  prefixes, separators, suffixes = context.formatter.format(column)
  numpy.testing.assert_array_equal(prefixes, ["0", "1", "2", "3"])
  numpy.testing.assert_array_equal(separators, ["."] * 4)
  numpy.testing.assert_array_equal(suffixes, ["1"] * 4)

@then(u'formatting mixed floats and integers with the toyplot.format.FloatFormatter should produce valid output')
def step_impl(context):
  column = numpy.array([0.1, 1.1, 2, 3.1])
  prefixes, separators, suffixes = context.formatter.format(column)
  numpy.testing.assert_array_equal(prefixes, ["0", "1", "2", "3"])
  numpy.testing.assert_array_equal(separators, [".", ".", "", "."])
  numpy.testing.assert_array_equal(suffixes, ["1", "1", "", "1"])

@then(u'formatting integers with the toyplot.format.FloatFormatter should produce valid output')
def step_impl(context):
  column = numpy.arange(4)
  prefixes, separators, suffixes = context.formatter.format(column)
  numpy.testing.assert_array_equal(prefixes, ["0", "1", "2", "3"])
  numpy.testing.assert_array_equal(separators, [""] * 4)
  numpy.testing.assert_array_equal(suffixes, [""] * 4)

