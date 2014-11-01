from behave import *
import nose.tools

import toyplot.units

@when(u'toyplot.units.points receives 72')
def step_impl(context):
  context.value = 72

@then(u'toyplot.units.points should return 72')
def step_impl(context):
  nose.tools.assert_equal(toyplot.units.points(context.value), 72)

@when(u'toyplot.units.points receives .5 inch')
def step_impl(context):
  context.value = (0.5, "inch")

@then(u'toyplot.units.points should return 36')
def step_impl(context):
  nose.tools.assert_equal(toyplot.units.points(context.value), 36)

@when(u'toyplot.units.points receives string')
def step_impl(context):
  context.value = "72"

@then(u'toyplot.units.points should raise ValueError')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    toyplot.units.points(context.value)

@when(u'toyplot.units.points receives 1 furlong')
def step_impl(context):
  context.value = (1, "furlong")

