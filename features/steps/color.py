from __future__ import division

from behave import *

import json
import nose.tools
import toyplot.color
import toyplot.testing

@when(u'toyplot.color.css receives {value}')
def step_impl(context, value):
  context.value = value

@then(u'toyplot.color.css should return {value}')
def step_impl(context, value):
  toyplot.testing.assert_color_equal(toyplot.color.css(context.value), eval(value))

@when(u'toyplot.color.to_css receives {value}')
def step_impl(context, value):
  context.value = eval(value)

@then(u'toyplot.color.to_css should return {value}')
def step_impl(context, value):
  nose.tools.assert_equal(toyplot.color.to_css(context.value), value)

