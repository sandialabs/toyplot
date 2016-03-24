# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import nose
import numpy
import toyplot.data
import toyplot.testing


@given(u'values from -1000 to -1')
def step_impl(context):
    context.x = numpy.linspace(-1000, -1, 100)


@given(u'values from -1000 to -0.01')
def step_impl(context):
    context.x = numpy.linspace(-1000, -0.01, 100)


@given(u'values from -1000 to 0')
def step_impl(context):
    context.x = numpy.linspace(-1000, 0, 100)


@given(u'values from -1000 to 0.5')
def step_impl(context):
    context.x = numpy.linspace(-1000, 0.5, 100)


@given(u'values from -0.5 to 1000')
def step_impl(context):
    context.x = numpy.linspace(-0.5, 1000, 100)


@given(u'values from 0 to 1000')
def step_impl(context):
    context.x = numpy.linspace(0, 1000, 100)


@given(u'values from 0.01 to 1000')
def step_impl(context):
    context.x = numpy.linspace(0.01, 1000, 100)


@given(u'values from 1 to 1000')
def step_impl(context):
    context.x = numpy.linspace(1, 1000, 100)


@given(u'values from -1000 to 1000')
def step_impl(context):
    context.x = numpy.linspace(-1000, 1000, 100)


@given(u'log 10 axes on x and y')
def step_impl(context):
    context.axes = context.canvas.axes(xscale="log10", yscale="log10")


@given(u'log 2 axes on x and y')
def step_impl(context):
    context.axes = context.canvas.axes(xscale="log2", yscale="log2")


@given(u'log 10 axes on x and y with custom format')
def step_impl(context):
    context.axes = context.canvas.axes(xscale="log10", yscale="log10")
    context.axes.x.ticks.locator = toyplot.locator.Log(base=10, format="{base}^{exponent}")
    context.axes.y.ticks.locator = toyplot.locator.Log(base=10, format="{base}^{exponent}")


@when(u'plotting x, x with markers')
def step_impl(context):
    context.axes.plot(context.x, context.x, marker="o")


@given(u'squared values from 0 to 10')
def step_impl(context):
    context.values = numpy.linspace(0, 10) ** 2


@given(u'squared values from -10 to 0')
def step_impl(context):
    context.values = -(numpy.linspace(10, 0) ** 2)


@given(u'log 10 axes on y with domain min 10')
def step_impl(context):
    context.axes = context.canvas.axes(yscale="log10")
    context.axes.y.domain.min = 10


@given(u'log 10 axes on y with domain max -10')
def step_impl(context):
    context.axes = context.canvas.axes(yscale="log10")
    context.axes.y.domain.max = -10


@when(u'plotting the values with bars')
def step_impl(context):
    context.axes.bars(context.values)


