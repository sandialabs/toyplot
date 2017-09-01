# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import toyplot

import testing


@when(
    u'creating a plot with unicode text in a cartesian axes x label, the plot will match unicode-cartesian-x-label')
def step_impl(context):
    axes = context.canvas.cartesian(xlabel=u"L\u0302")
    testing.assert_canvas_equal(context.canvas, "unicode-cartesian-x-label")


@when(
    u'creating a plot with unicode text in a cartesian axes y label, the plot will match unicode-cartesian-y-label')
def step_impl(context):
    axes = context.canvas.cartesian(ylabel=u"L\u0302")
    testing.assert_canvas_equal(context.canvas, "unicode-cartesian-y-label")


@when(
    u'creating a plot with unicode text in a cartesian axes label, the plot will match unicode-cartesian-label')
def step_impl(context):
    axes = context.canvas.cartesian(label=u"L\u0302")
    testing.assert_canvas_equal(context.canvas, "unicode-cartesian-label")


@when(
    u'creating a plot with unicode text in a cartesian axes tick labels, the plot will match unicode-cartesian-tick-labels')
def step_impl(context):
    axes = context.canvas.cartesian()
    axes.x.ticks.locator = toyplot.locator.Explicit([0], [u"L\u0302"])
    testing.assert_canvas_equal(context.canvas, "unicode-cartesian-tick-labels")


@when(
    u'creating a plot with unicode text in a cartesian axes text mark, the plot will match unicode-cartesian-text')
def step_impl(context):
    axes = context.canvas.cartesian()
    axes.text(0, 0, u"L\u0302")
    testing.assert_canvas_equal(context.canvas, "unicode-cartesian-text")


@when(
    u'creating a plot with unicode text in canvas text, the plot will match unicode-canvas-text')
def step_impl(context):
    context.canvas.text(100, 100, u"L\u0302")
    testing.assert_canvas_equal(context.canvas, "unicode-canvas-text")
