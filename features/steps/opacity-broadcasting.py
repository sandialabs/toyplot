from __future__ import division

from behave import *

import numpy
import toyplot.testing

@given(u'a set of per-series opacity values')
def step_impl(context):
    context.series_opacities = numpy.linspace(1, 0.1, context.series.shape[1])

@given(u'a set of per-datum opacity values')
def step_impl(context):
    numpy.random.seed(1234)
    context.datum_opacities = numpy.column_stack((
        numpy.random.uniform(1, 0.75, size=context.series.shape[0]),
        numpy.random.uniform(0.75, 0.5, size=context.series.shape[0]),
        numpy.random.uniform(0.5, 0.25, size=context.series.shape[0]),
        numpy.random.uniform(0.25, 0.1, size=context.series.shape[0]),
        ))

@then(u'hlines can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.hlines(context.series[:,0], opacity=0.1)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-hlines-one-opacity")

@then(u'hlines can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.hlines(context.series[:,0], opacity=numpy.linspace(0, 1, context.series.shape[0]))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-hlines-per-datum-opacities")

@then(u'vlines can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.vlines(context.series[:,0], opacity=0.1)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-vlines-one-opacity")

@then(u'vlines can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.vlines(context.series[:,0], opacity=numpy.linspace(0, 1, context.series.shape[0]))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "opacity-broadcast-vlines-per-datum-opacities")


