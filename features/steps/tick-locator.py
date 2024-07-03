# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import numpy
import sys
import toyplot.locator
from toyplot.require import as_float

import testing

try:
    import arrow
except:
    pass

def arrow_available(context):
    if "arrow" in sys.modules:
        return True

    context.scenario.skip(reason="The arrow library is not available.")
    return False


@given(u'sample sin wave data')
def step_impl(context):
    context.x = numpy.linspace(0, 2 * numpy.pi, 100)
    context.y = numpy.sin(context.x)


@then(u'the data can be rendered with default ticks')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.cartesian()
    axes.plot(context.x, context.y)
    testing.assert_canvas_equal(canvas, "tick-locator-default")


@then(u'the data can be rendered with ticks evenly spread across the domain')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.cartesian(
        xticklocator=toyplot.locator.Uniform(count=10, format="{:.3g}"))
    axes.y.ticks.locator = toyplot.locator.Uniform(count=3, format="{:.1f}")
    axes.plot(context.x, context.y)
    testing.assert_canvas_equal(canvas, "tick-locator-basic")


@then(u'the data can be rendered with explicit locations')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.cartesian(
        xticklocator=toyplot.locator.Explicit(
            locations=[
                0,
                2,
                numpy.pi,
                4,
                6]))
    axes.plot(context.x, context.y)
    testing.assert_canvas_equal(
        canvas, "tick-locator-explicit-locations")


@then(u'the data can be rendered with explicit locations and explicit labels')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.cartesian(xticklocator=toyplot.locator.Explicit(
        locations=[0, numpy.pi, 2 * numpy.pi], labels=["0", "pi", "2pi"]))
    axes.y.ticks.locator = toyplot.locator.Explicit([-1, 1], ["-1", "1"])
    axes.plot(context.x, context.y)
    testing.assert_canvas_equal(
        canvas, "tick-locator-explicit-locations-labels")


@then(u'the data can be rendered with explicit labels')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.cartesian(
        xticklocator=toyplot.locator.Explicit(labels=["red", "green", "blue"]))
    axes.y.ticks.locator = toyplot.locator.Explicit([-1, 1], ["-1", "1"])
    axes.plot(context.x, context.y)
    testing.assert_canvas_equal(canvas, "tick-locator-explicit-labels")


@then(u'the data can be rendered with ticks identified by heckbert')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.cartesian(xticklocator=toyplot.locator.Heckbert(count=10))
    axes.y.ticks.locator = toyplot.locator.Heckbert(count=3)
    axes.plot(context.x, context.y)
    testing.assert_canvas_equal(canvas, "tick-locator-heckbert")


@then(u'the data can be rendered with ticks identified by optimization')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.cartesian(xticklocator=toyplot.locator.Extended(count=12))
    axes.y.ticks.locator = toyplot.locator.Extended(count=5)
    axes.plot(context.x, context.y)
    testing.assert_canvas_equal(canvas, "tick-locator-extended")

@then(u'the data can be rendered without ticks')
def step_impl(context):
    canvas = toyplot.Canvas()
    axes = canvas.cartesian(xticklocator=toyplot.locator.Null())
    axes.y.ticks.locator = toyplot.locator.Null()
    axes.plot(context.x, context.y)
    testing.assert_canvas_equal(canvas, "tick-locator-null")

@given(u'seven thousand years of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(9016, 1, 1).timestamp()

@given(u'one thousand years of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(3016, 1, 1).timestamp()

@given(u'one hundred years of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2116, 1, 1).timestamp()

@given(u'five years of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2021, 1, 1).timestamp()

@given(u'one year of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2017, 1, 1).timestamp()

@given(u'six months of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 7, 1).timestamp()

@given(u'one month of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 2, 1).timestamp()

@given(u'one week of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 8).timestamp()

@given(u'one day of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 2).timestamp()

@given(u'six hours of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 1, 6).timestamp()

@given(u'two hours of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 1, 2).timestamp()

@given(u'one hour of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 1, 1).timestamp()

@given(u'thirty minutes of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 1, 0, 30).timestamp()

@given(u'five minutes of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 1, 0, 5).timestamp()

@given(u'two minutes of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 1, 0, 2).timestamp()

@given(u'one minute of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 1, 0, 1, 0).timestamp()

@given(u'thirty seconds of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 1, 0, 0, 30).timestamp()

@given(u'five seconds of timestamp data')
def step_impl(context):
    if arrow_available(context):
        context.timestamp_begin = arrow.get(2016, 1, 1).timestamp()
        context.timestamp_end = arrow.get(2016, 1, 1, 0, 0, 5).timestamp()

@given(u'a default interval')
def step_impl(context):
    context.timestamp_interval = None

@given(u'a {count} {units} interval')
def step_impl(context, count, units):
    context.timestamp_interval = (as_float(count), units)

@given(u'an interval of days')
def step_impl(context):
    context.timestamp_interval = "days"

@given(u'a visualization using the timestamp locator')
def step_impl(context):
    numpy.random.seed(1234)
    timestamps = numpy.random.uniform(context.timestamp_begin, context.timestamp_end, size=10)

    context.canvas = toyplot.Canvas(width=800, height=200)
    numberline = context.canvas.numberline(min=context.timestamp_begin, max=context.timestamp_end)
    numberline.axis.ticks.locator = toyplot.locator.Timestamp(interval=context.timestamp_interval)
    numberline.axis.ticks.show = True
    numberline.scatterplot(timestamps, marker="|", size=15)

@given(u'a visualization using daily tick locators with a timezone')
def step_impl(context):
    start = arrow.Arrow(2018, 7, 2, tzinfo="US/Eastern")
    end = arrow.Arrow(2018, 7, 7, tzinfo="US/Eastern")
    timestamps = [datetime[0].timestamp() for datetime in arrow.Arrow.span_range("day", start, end)]

    context.canvas = toyplot.Canvas(width=800, height=200)
    numberline = context.canvas.numberline()
    numberline.axis.ticks.locator = toyplot.locator.Timestamp(timezone="US/Eastern")
    numberline.axis.ticks.show = True
    numberline.scatterplot(timestamps, marker="|", size=15)
