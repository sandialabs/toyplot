from behave import *
import nose.tools

import toyplot.projection

@given(u'A linear projection with 0, 1 and 0, 100')
def step_impl(context):
  context.projection = toyplot.projection.Linear(0, 1, 0, 100)

@then(u'0 should project to 0')
def step_impl(context):
  nose.tools.assert_equal(context.projection(0), 0)
  nose.tools.assert_equal(context.projection.inverse(0), 0)

@then(u'0.5 should project to 50')
def step_impl(context):
  nose.tools.assert_equal(context.projection(0.5), 50)
  nose.tools.assert_equal(context.projection.inverse(50), 0.5)

@then(u'1 should project to 100')
def step_impl(context):
  nose.tools.assert_equal(context.projection(1.0), 100)
  nose.tools.assert_equal(context.projection.inverse(100), 1.0)

@given(u'A log10 projection with 1, 100 and 0, 100')
def step_impl(context):
  context.projection = toyplot.projection.Log(1, 100, 0, 100, 10)

@then(u'1 should project to 0')
def step_impl(context):
  nose.tools.assert_equal(context.projection(1), 0)

@then(u'10 should project to 50')
def step_impl(context):
  nose.tools.assert_equal(context.projection(10), 50)

@then(u'100 should project to 100')
def step_impl(context):
  nose.tools.assert_equal(context.projection(100), 100)

@given(u'A symlog10 projection with -100, 100 and 0, 100')
def step_impl(context):
  context.projection = toyplot.projection.SymmetricLog(-100, 100, 0, 100, 10)

@then(u'-100 should project to 0')
def step_impl(context):
  nose.tools.assert_equal(context.projection(-100), 0)

@then(u'0 should project to 50')
def step_impl(context):
  nose.tools.assert_equal(context.projection(0), 50)


