# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import numpy
import toyplot.locator

def _set_square_domain(context, size):
    context.axes.x.domain.min = -size
    context.axes.x.domain.max = size
    context.axes.y.domain.min = -size
    context.axes.y.domain.max = size


@given(u'a basic ellipse')
def step_impl(context):
    _set_square_domain(context, 20)
    context.axes.ellipse(0, 0, 20, 10)


@given(u'a rotated ellipse')
def step_impl(context):
    _set_square_domain(context, 20)
    context.axes.ellipse(0, 0, 20, 10, 30)


@given(u'an ellipse with log y axis')
def step_impl(context):
    _set_square_domain(context, 20)
    context.axes.y.scale = "log"
    context.axes.ellipse(0, 0, 20, 10, 30)


@given(u'an ellipse with a title')
def step_impl(context):
    _set_square_domain(context, 20)
    context.axes.ellipse(0, 0, 20, 10, 30, title="An ellipse.")


@given(u'an ellipse with a custom style')
def step_impl(context):
    _set_square_domain(context, 20)
    context.axes.ellipse(0, 0, 20, 10, 30, style={"stroke": "crimson", "fill": "none"})


@given(u'an ellipse with a custom color')
def step_impl(context):
    _set_square_domain(context, 20)
    context.axes.ellipse(0, 0, 20, 10, 30, color="crimson")


@given(u'an ellipse with a custom opacity')
def step_impl(context):
    _set_square_domain(context, 20)
    context.axes.ellipse(0, 0, 20, 10, 30, opacity=0.5)


@given(u'multiple ellipses')
def step_impl(context):
    _set_square_domain(context, 20)
    context.axes.ellipse([-10, 10], [0, 0], [5, 5], [2.5, 2.5], [30, -30], color=["crimson", "royalblue"])

