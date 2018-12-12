# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import collections

import nose.tools
import numpy.testing
import toyplot


@given(u'axes-bars-boundaries-masked-nan')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(size=(50, 50))
    b = numpy.ma.column_stack((numpy.min(observations, axis=1), numpy.median(
        observations, axis=1), numpy.max(observations, axis=1)))
    b[10:20, 0] = numpy.nan
    b[30:40, 1] = numpy.ma.masked
    b[20:30, 2] = numpy.nan

    context.axes.bars(b, baseline=None)


@given(u'axes-bars-histogram')
def step_impl(context):
    numpy.random.seed(1234)
    context.axes.bars(numpy.histogram(numpy.random.normal(size=10000), 100))


@given(u'axes-bars-magnitudes-masked-nan')
def step_impl(context):
    x = numpy.linspace(0, 2 * numpy.pi, 51)
    y = numpy.ma.column_stack((
        1 + 0.5 * numpy.sin(x),
        1 + 0.5 * numpy.cos(x),
        1 + 0.2 * numpy.sin(2 * x),
    ))
    y[8:18, 0] = numpy.nan
    y[33:43, 1] = numpy.ma.masked

    context.axes.bars(x, y)


@given(u'axes-bars-n-boundaries-along-y')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.axes.bars(series, along="y", baseline=None)


@given(u'axes-bars-n-boundaries-centers')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.axes.bars(x, series, baseline=None)


@given(u'axes-bars-n-boundaries-edges')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.axes.bars(x1, x2, series, baseline=None)


@given(u'axes-bars-n-boundaries-titles')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.min(
            observations, axis=1), numpy.percentile(
            observations, 25, axis=1), numpy.percentile(
                observations, 50, axis=1), numpy.percentile(
                    observations, 75, axis=1), numpy.max(
                        observations, axis=1)))

    context.axes.bars(
        series,
        title=[
            "1st quartile",
            "2nd quartile",
            "3rd quartile",
            "4th quartile"],
        baseline=None)


@given(u'axes-bars-n-boundaries')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.axes.bars(series, baseline=None)


@given(u'axes-bars-n-magnitudes-along-y')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.axes.bars(series, along="y")


@given(u'axes-bars-n-magnitudes-centers')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.axes.bars(x, series)


@given(u'axes-bars-n-magnitudes-edges')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.axes.bars(x1, x2, series)


@given(u'axes-bars-n-magnitudes-symmetric')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.axes.bars(series, baseline="symmetric")


@given(u'axes-bars-n-magnitudes-titles')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.axes.bars(series, baseline="stacked", title=["mean", "standard deviation"])


@given(u'axes-bars-n-magnitudes-wiggle')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.axes.bars(series, baseline="wiggle")


@given(u'axes-bars-n-magnitudes')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))

    context.axes.bars(series)


@given(u'axes-bars-one-boundary-centers')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y1 = numpy.mean(observations, axis=1)

    context.axes.bars(x, y1, baseline=None)


@given(u'axes-bars-one-boundary-edges')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    y1 = numpy.mean(observations, axis=1)

    context.axes.bars(x1, x2, y1, baseline=None)


@given(u'axes-bars-one-boundary')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y1 = numpy.mean(observations, axis=1)

    context.axes.bars(y1, baseline=None)


@given(u'axes-bars-one-magnitude-centers')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    context.axes.bars(x, y)


@given(u'axes-bars-one-magnitude-edges')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.cumsum(numpy.random.random(len(observations) + 1))
    x1 = x[:-1]
    x2 = x[1:]
    y = numpy.mean(observations, axis=1)

    context.axes.bars(x1, x2, y)


@given(u'axes-bars-one-magnitude')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    context.axes.bars(y)


@given(u'bars-one-magnitude')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    context.axes.bars(y)


