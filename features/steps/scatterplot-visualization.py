# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import collections

import nose.tools
import numpy.testing
import toyplot


@given(u'axes-scatterplot-markers')
def step_impl(context):
    marker_style = {"stroke": toyplot.color.black, "fill": "cornsilk"}
    label_style = {"stroke": "none", "fill": toyplot.color.black}
    markers = [
        None,
        "",
        "|",
        "-",
        "/",
        "\\",
        "+",
        "x",
        toyplot.marker.create(shape="x", angle=-22.5),
        "*",
        "^",
        toyplot.marker.create(shape=">", mstyle={"stroke": "red"}),
        toyplot.marker.create(shape="v", mstyle={"stroke": "red", "fill": "yellow"}),
        "<",
        "s",
        "d",
        "o",
        "oo",
        "o|",
        "o-",
        "o+",
        "ox",
        "o*",
        toyplot.marker.create(shape="", label="A"),
        toyplot.marker.create(shape="o", label="1"),
        toyplot.marker.create(shape="s", mstyle={"stroke": "blue", "fill": "white"}, label="B", lstyle={"fill": "blue"}),
        toyplot.marker.create(shape="d", label="2", lstyle={"fill": "green"}),
    ]

    context.axes.scatterplot(
        numpy.arange(
            len(markers)),
        color="steelblue",
        marker=markers,
        size=10,
        mstyle=marker_style,
        mlstyle=label_style)


@given(u'axes-scatterplot-n-variables-along-y')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.axes.scatterplot(series, along="y")


@given(u'axes-scatterplot-n-variables-x')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.axes.scatterplot(x, series)


@given(u'axes-scatterplot-n-variables')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    series = numpy.column_stack((numpy.min(observations, axis=1), numpy.mean(
        observations, axis=1), numpy.max(observations, axis=1)))

    context.axes.scatterplot(series)


@given(u'axes-scatterplot-one-variable-fill')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)
    color = numpy.arange(len(observations))

    context.axes.scatterplot(y, color=color)


@given(u'axes-scatterplot-one-variable-x')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    x = numpy.linspace(0, 1, len(observations))
    y = numpy.mean(observations, axis=1)

    context.axes.scatterplot(x, y)


@given(u'axes-scatterplot-one-variable')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    context.axes.scatterplot(y)


@given(u'axes-scatterplot-singular')
def step_impl(context):
    x = numpy.linspace(0, 2 * numpy.pi)
    y = numpy.sin(x)

    context.axes.plot(x, y)
    context.axes.scatterplot(x[0], y[0], color="red")


@given(u'scatterplot-one-variable')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(25, 100))
    y = numpy.mean(observations, axis=1)

    context.axes.scatterplot(y)

