# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import nose.tools
import numpy.testing
import toyplot.format


@given(u'an instance of toyplot.format.BasicFormatter')
def step_impl(context):
    context.formatter = toyplot.format.BasicFormatter()


@given(u'an instance of toyplot.format.BasicFormatter with nanshow off')
def step_impl(context):
    context.formatter = toyplot.format.BasicFormatter(nanshow=False)


@given(u'an instance of toyplot.format.FloatFormatter')
def step_impl(context):
    context.formatter = toyplot.format.FloatFormatter()


@given(u'an instance of toyplot.format.UnitFormatter using {units}')
def step_impl(context, units):
    context.formatter = toyplot.format.UnitFormatter(units=eval(units))


@given(u'an instance of toyplot.format.CurrencyFormatter using {currency}')
def step_impl(context, currency):
    context.formatter = toyplot.format.CurrencyFormatter(curr=eval(currency))


@then(u'formatting {value} should produce {output}')
def step_impl(context, value, output):
	value = eval(value)
	output = eval(output)
	prefix, separator, suffix = context.formatter.format(value)
	nose.tools.assert_equal(prefix, output[0])
	nose.tools.assert_equal(separator, output[1])
	nose.tools.assert_equal(suffix, output[2])

