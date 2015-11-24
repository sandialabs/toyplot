from behave import *

import numpy
import toyplot.testing

@given(u'a explicit linear color map')
def step_impl(context):
    context.colormap = toyplot.color.LinearMap(toyplot.color.brewer("BlueRed"), domain_min=0, domain_max=1)

@then(u'a vertical color scale can be added to the canvas')
def step_impl(context):
    context.canvas.color_scale(context.colormap, x1=100, x2=100, y1="-10%", y2="10%")
    toyplot.testing.assert_canvas_equal(context.canvas, "color-scale-canvas-vertical")

@then(u'a diagonal color scale can be added to the canvas')
def step_impl(context):
    context.canvas.color_scale(context.colormap, x1=100, x2=-100, y1=-100, y2=100)
    toyplot.testing.assert_canvas_equal(context.canvas, "color-scale-canvas-diagonal")

@given(u'a set of default axes')
def step_impl(context):
    context.axes = context.canvas.axes()

@then(u'a color scale can be added to the axes')
def step_impl(context):
    context.axes.color_scale(context.colormap)
    toyplot.testing.assert_canvas_equal(context.canvas, "color-scale-axes-default")

@then(u'a color scale with default colormap can be added to a matrix visualization')
def step_impl(context):
    numpy.random.seed(1234)
    values = numpy.random.normal(size=(10, 10))
    context.canvas.matrix(values, scale=True)
    toyplot.testing.assert_canvas_equal(context.canvas, "color-scale-matrix-default")

@then(u'a color scale with explicit colormap can be added to a matrix visualization')
def step_impl(context):
    numpy.random.seed(1234)
    values = numpy.random.normal(size=(10, 10))
    colormap = toyplot.color.LinearMap(toyplot.color.brewer("BlueGreenBrown"), domain_min=-2, domain_max=2)
    context.canvas.matrix((values, colormap), scale=True)
    toyplot.testing.assert_canvas_equal(context.canvas, "color-scale-matrix-explicit")


