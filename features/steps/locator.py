from behave import *

import numpy
import toyplot.locator
import toyplot.testing


@given(u'sample sin wave data')
def step_impl(context):
    context.x = numpy.linspace(0, 2 * numpy.pi, 100)
    context.y = numpy.sin(context.x)


@then(u'the data can be rendered with default ticks')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes()
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(canvas, "locator-defaults")


@then(u'the data can be rendered with ticks evenly spread across the domain')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(
        xticklocator=toyplot.locator.Basic(count=10, format="{:.3g}"))
    axes.y.ticks.locator = toyplot.locator.Basic(count=3, format="{:.1f}")
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(canvas, "basic-tick-locator")


@then(u'the data can be rendered with explicit locations')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(
        xticklocator=toyplot.locator.Explicit(locations=[0, 2, numpy.pi, 4, 6]))
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(
        canvas, "explicit-tick-locator-locations")


@then(u'the data can be rendered with explicit locations and explicit labels')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(xticklocator=toyplot.locator.Explicit(
        locations=[0, numpy.pi, 2 * numpy.pi], labels=["0", "pi", "2pi"]))
    axes.y.ticks.locator = toyplot.locator.Explicit([-1, 1], ["-1", "1"])
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(
        canvas, "explicit-tick-locator-locations-labels")


@then(u'the data can be rendered with explicit labels')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(
        xticklocator=toyplot.locator.Explicit(labels=["red", "green", "blue"]))
    axes.y.ticks.locator = toyplot.locator.Explicit([-1, 1], ["-1", "1"])
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(canvas, "explicit-tick-locator-labels")


@then(u'the data can be rendered with ticks identified by heckbert')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(xticklocator=toyplot.locator.Heckbert(count=10))
    axes.y.ticks.locator = toyplot.locator.Heckbert(count=3)
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(canvas, "heckbert-tick-locator")


@then(u'the data can be rendered with ticks identified by optimization')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(xticklocator=toyplot.locator.Extended(count=12))
    axes.y.ticks.locator = toyplot.locator.Extended(count=5)
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(canvas, "extended-tick-locator")
