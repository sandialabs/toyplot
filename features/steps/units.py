from behave import *
import nose.tools

import toyplot.units

@when(u'converting 72 without default units to points the result should be raise ValueError')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    toyplot.units.convert(72, "pt")

@when(u'converting 72 with default units pt to in the result should be return 1.0')
def step_impl(context):
  nose.tools.assert_equal(toyplot.units.convert(72, "in", default="pt"), 1.0)

@when(u'converting 72pt to in the result should be return 1.0')
def step_impl(context):
  nose.tools.assert_equal(toyplot.units.convert("72pt", "in"), 1.0)

@when(u'converting (72, pt) to in the result should be return 1.0')
def step_impl(context):
  nose.tools.assert_equal(toyplot.units.convert((72, "pt"), "in"), 1.0)

@when(u'converting 96px to in the result should be return 1.0')
def step_impl(context):
  nose.tools.assert_equal(toyplot.units.convert("96px", "in"), 1.0)

@when(u'converting 96px to pt the result should be return 72.0')
def step_impl(context):
  nose.tools.assert_equal(toyplot.units.convert("96px", "pt"), 72.0)

@when(u'converting .5in to pt the result should be return 36.0')
def step_impl(context):
  nose.tools.assert_equal(toyplot.units.convert(".5in", "pt"), 36.0)

@when(u'converting 1in to cm the result should be return 2.54')
def step_impl(context):
  nose.tools.assert_almost_equal(toyplot.units.convert("1in", "cm"), 2.54)

@when(u'converting 1 furlong to in the result should be raise ValueError')
def step_impl(context):
  with nose.tools.assert_raises(ValueError):
    toyplot.units.convert("1 furlong", "in")


