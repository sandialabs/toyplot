# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import collections

import test
import numpy.testing
import toyplot


@given(u'axes-rect-singular-along-y')
def step_impl(context):
    context.axes.x.domain.min = 0
    context.axes.x.domain.max = 1
    context.axes.y.domain.min = 0
    context.axes.y.domain.max = 1
    context.axes.rectangle(0.1, 0.2, 0.3, 0.6, along="y")


@given(u'axes-rect-singular')
def step_impl(context):
    context.axes.x.domain.min = 0
    context.axes.x.domain.max = 1
    context.axes.y.domain.min = 0
    context.axes.y.domain.max = 1
    context.axes.rectangle(0.1, 0.2, 0.3, 0.6)


@given(u'axes-rect')
def step_impl(context):
    x1 = numpy.arange(1, 10)
    x2 = x1 + 0.5
    y1 = x1 - 0.5
    y2 = x1 ** 1.5
    color = x1
    title = x1
    colormap = toyplot.color.CategoricalMap(toyplot.color.brewer.palette("BlueRed"))

    context.axes.rectangle(x1, x2, y1, y2, color=(color, colormap), title=title)


