from behave import *

import numpy
import toyplot.testing


@given(u'a default canvas')
def step_impl(context):
    context.canvas = toyplot.Canvas()


@given(u'a set of cartesian axes')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    context.axes = context.canvas.axes()


@given(u'a sample plot')
def step_impl(context):
    context.axes.plot(numpy.sin(numpy.linspace(0, 10)))


@then(u'the visualization should match the {reference} reference image')
def step_impl(context, reference):
    toyplot.testing.assert_canvas_equal(context.canvas, reference)

