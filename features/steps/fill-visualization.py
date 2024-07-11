# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import numpy
import toyplot.data

import testing


@given(u'position and boundary data')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(50, 100))
    context.position = numpy.linspace(0, 1)
    context.boundaries = numpy.column_stack(
        (numpy.min(
            observations, axis=1), numpy.mean(
            observations, axis=1), numpy.max(
                observations, axis=1)))


@when(u'creating a fill plot with one boundary')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(context.boundaries.T[1])


@then(
    u'the result should be a fill plot between the boundary and the origin with implicit x')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-one-boundary")


@when(u'creating a fill plot with one boundary and position')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.boundaries.T[1])


@then(u'the result should be a fill plot between the boundary and the origin')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-one-boundary-position")


@when(u'creating a fill plot with two boundaries and position')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.boundaries.T[1], context.boundaries.T[2])


@then(u'the result should be a fill plot between the two boundaries')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-two-boundaries-position")


@when(u'creating a fill plot with multiple boundaries')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(context.boundaries)


@then(
    u'the result should be multiple fill series between the boundaries with implicit x')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-boundaries")


@when(u'creating a fill plot with multiple boundaries and position')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.boundaries)


@then(u'the result should be multiple fill series between the boundaries')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-boundaries-position")


@when(u'creating a fill plot with multiple boundaries and position along y')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.boundaries, along="y")


@then(
    u'the result should be multiple fill series between the boundaries along y')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-boundaries-position-along-y")


@when(u'creating a fill plot with multiple boundaries and per-series titles')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.boundaries, title=["1st half", "2nd half"])


@then(
    u'the result should be multiple fill series between the boundaries with titles')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-boundaries-titles")


@given(u'position and magnitude data')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(50, 100))
    context.position = numpy.linspace(0, 1)
    context.magnitudes = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))


@when(u'creating a fill plot with one magnitude')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.magnitudes.T[0], baseline="stacked")


@then(
    u'the result should be one fill series stacked above the origin with implicit x')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-one-magnitude")


@when(u'creating a fill plot with one magnitude and position')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.magnitudes.T[0], baseline="stacked")


@then(u'the result should be one fill series stacked above the origin')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-one-magnitude-position")


@when(u'creating a fill plot with multiple magnitudes')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.magnitudes, baseline="stacked")


@then(
    u'the result should be multiple fill series stacked above the origin with implicit x')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes")


@when(u'creating a fill plot with multiple magnitudes and position')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.magnitudes, baseline="stacked")


@then(u'the result should be multiple fill series stacked above the origin')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes-position")


@when(u'creating a fill plot with multiple magnitudes and position along y')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.magnitudes, baseline="stacked", along="y")


@then(
    u'the result should be multiple fill series stacked above the origin along y')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes-position-along-y")


@when(u'creating a fill plot with multiple magnitudes and per-series titles')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.magnitudes, baseline="stacked", title=[
            "1st half", "2nd half"])


@then(
    u'the result should be multiple fill series stacked above the origin with titles')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes-position-titles")


@when(u'creating a fill plot with multiple magnitudes and symmetric baseline')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.magnitudes, baseline="symmetric")


@then(
    u'the result should be multiple fill series stacked with symmetric baseline')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes-symmetric-baseline")


@when(u'creating a fill plot with multiple magnitudes and wiggle baseline')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.magnitudes, baseline="wiggle")


@then(
    u'the result should be multiple fill series stacked with wiggle baseline')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes-wiggle-baseline")


@given(u'axes-fill-boundaries-masked-nan')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(size=(50, 50))
    b = numpy.ma.column_stack((numpy.min(observations, axis=1), numpy.median(
        observations, axis=1), numpy.max(observations, axis=1)))
    b[10:20, 0] = numpy.nan
    b[30:40, 1] = numpy.ma.masked
    b[20:30, 2] = numpy.nan

    context.axes.fill(b)


@given(u'axes-fill-magnitudes-masked-nan')
def step_impl(context):
    x = numpy.linspace(0, 2 * numpy.pi, 51)
    y = numpy.ma.column_stack((
        1 + 0.5 * numpy.sin(x),
        1 + 0.5 * numpy.cos(x),
        1 + 0.2 * numpy.sin(2 * x),
    ))
    y[8:18, 0] = numpy.nan
    y[33:43, 1] = numpy.ma.masked

    context.axes.fill(x, y, baseline="stacked")


