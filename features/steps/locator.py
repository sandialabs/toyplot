from behave import *

import arrow
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
    toyplot.testing.assert_canvas_equal(canvas, "tick-locator-default")


@then(u'the data can be rendered with ticks evenly spread across the domain')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(
        xticklocator=toyplot.locator.Basic(count=10, format="{:.3g}"))
    axes.y.ticks.locator = toyplot.locator.Basic(count=3, format="{:.1f}")
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(canvas, "tick-locator-basic")


@then(u'the data can be rendered with explicit locations')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(
        xticklocator=toyplot.locator.Explicit(
            locations=[
                0,
                2,
                numpy.pi,
                4,
                6]))
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(
        canvas, "tick-locator-explicit-locations")


@then(u'the data can be rendered with explicit locations and explicit labels')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(xticklocator=toyplot.locator.Explicit(
        locations=[0, numpy.pi, 2 * numpy.pi], labels=["0", "pi", "2pi"]))
    axes.y.ticks.locator = toyplot.locator.Explicit([-1, 1], ["-1", "1"])
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(
        canvas, "tick-locator-explicit-locations-labels")


@then(u'the data can be rendered with explicit labels')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(
        xticklocator=toyplot.locator.Explicit(labels=["red", "green", "blue"]))
    axes.y.ticks.locator = toyplot.locator.Explicit([-1, 1], ["-1", "1"])
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(canvas, "tick-locator-explicit-labels")


@then(u'the data can be rendered with ticks identified by heckbert')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(xticklocator=toyplot.locator.Heckbert(count=10))
    axes.y.ticks.locator = toyplot.locator.Heckbert(count=3)
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(canvas, "tick-locator-heckbert")


@then(u'the data can be rendered with ticks identified by optimization')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(xticklocator=toyplot.locator.Extended(count=12))
    axes.y.ticks.locator = toyplot.locator.Extended(count=5)
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(canvas, "tick-locator-extended")

@then(u'the data can be rendered without ticks')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.axes(xticklocator=toyplot.locator.Null())
    axes.y.ticks.locator = toyplot.locator.Null()
    axes.plot(context.x, context.y)
    toyplot.testing.assert_canvas_equal(canvas, "tick-locator-null")

@given(u'five years of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2021, 1, 1).timestamp

@given(u'one year of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2017, 1, 1).timestamp

@given(u'six months of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 7, 1).timestamp

@given(u'one month of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 2, 1).timestamp

@given(u'one week of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 8).timestamp

@given(u'one day of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 2).timestamp

@given(u'six hours of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 1, 6).timestamp

@given(u'two hours of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 1, 2).timestamp

@given(u'one hour of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 1, 1).timestamp

@given(u'thirty minutes of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 1, 0, 30).timestamp

@given(u'five minutes of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 1, 0, 5).timestamp

@given(u'two minutes of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 1, 0, 2).timestamp

@given(u'one minute of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 1, 0, 1, 0).timestamp

@given(u'thirty seconds of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 1, 0, 0, 30).timestamp

@given(u'five seconds of timestamp data')
def step_impl(context):
    context.timestamp_begin = arrow.get(2016, 1, 1).timestamp
    context.timestamp_end = arrow.get(2016, 1, 1, 0, 0, 5).timestamp

@given(u'a visualization using the timestamp locator')
def step_impl(context):
    numpy.random.seed(1234)
    timestamps = numpy.random.uniform(context.timestamp_begin, context.timestamp_end, size=100)

    context.canvas = toyplot.Canvas(width=800, height=200)
    axes = context.canvas.axes(xmin=context.timestamp_begin, xmax=context.timestamp_end, yshow=False)
    axes.x.ticks.locator = toyplot.locator.Timestamp(count=7)
    axes.x.ticks.show = True
    axes.scatterplot(timestamps, numpy.zeros_like(timestamps), marker="|", size=200)

@then(u'the generated figure will match {reference}')
def step_impl(context, reference):
    toyplot.testing.assert_canvas_equal(context.canvas, reference)


