from behave import *
import toyplot.testing

@then(u'the visualization should match the {reference} reference image')
def step_impl(context, reference):
    toyplot.testing.assert_canvas_equal(context.canvas, reference)

