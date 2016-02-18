# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

from behave import *

import numpy
import toyplot.color


@given(u'a set of diverging series')
def step_impl(context):
    context.x = numpy.linspace(0, 1)
    context.series = numpy.column_stack((context.x**2, context.x**2/2, context.x**2/3, context.x**2/4))

@given(u'a set of per-series values')
def step_impl(context):
    context.series_values = numpy.array([0, 1, 2, 3])

@given(u'a set of per-series colors')
def step_impl(context):
    context.series_colors = ["red", "green", "blue", "yellow"]

@given(u'a set of per-datum values')
def step_impl(context):
    context.datum_values = numpy.arange(context.series.size).reshape(context.series.T.shape).T

@given(u'a set of per-datum colors')
def step_impl(context):
    context.datum_colors = numpy.tile(toyplot.color.css("black"), context.series.shape)
    context.datum_colors[15:20, 0] = toyplot.color.css("red")
    context.datum_colors[25:30, 1] = toyplot.color.css("green")
    context.datum_colors[35:40, 2] = toyplot.color.css("blue")
    context.datum_colors[45:50, 3] = toyplot.color.css("yellow")

@then(u'bars can be rendered with default colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric")

@then(u'bars can be rendered with one explicit color')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color="red")

@then(u'bars can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.series_colors)

@then(u'bars can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.datum_colors)

@then(u'bars can be rendered with colormap colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=toyplot.color.LinearMap(toyplot.color.brewer.palette("Set1")))

@then(u'bars can be rendered with per-series value colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.series_values)

@then(u'bars can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=(context.series_values, toyplot.color.LinearMap()))

@then(u'bars can be rendered with per-datum value colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.datum_values)

@then(u'bars can be rendered with per-datum value + colormap colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=(context.datum_values, toyplot.color.LinearMap()))


@then(u'fills can be rendered with default colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric")

@then(u'fills can be rendered with one explicit color')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color="red")

@then(u'fills can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=context.series_colors)

@then(u'fills can be rendered with colormap colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=toyplot.color.LinearMap(toyplot.color.brewer.palette("Set1")))

@then(u'fills can be rendered with per-series value colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=context.series_values)

@then(u'fills can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=(context.series_values, toyplot.color.LinearMap()))



@then(u'hlines can be rendered with default colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0])

@then(u'hlines can be rendered with one explicit color')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color="red")

@then(u'hlines can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color=context.datum_colors[:,0])

@then(u'hlines can be rendered with colormap colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color=toyplot.color.LinearMap(toyplot.color.brewer.palette("Set1")))

@then(u'hlines can be rendered with per-datum value colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.hlines(context.series[:,0], color=datum_values)

@then(u'hlines can be rendered with per-datum value + colormap colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.hlines(context.series[:,0], color=(datum_values, toyplot.color.LinearMap()))

@then(u'plots can be rendered with default colors')
def step_impl(context):
    context.axes.plot(context.series)

@then(u'plots can be rendered with one explicit color')
def step_impl(context):
    context.axes.plot(context.series, color="red")

@then(u'plots can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.plot(context.series, color=context.series_colors)

@then(u'plots can be rendered with colormap colors')
def step_impl(context):
    context.axes.plot(context.series, color=toyplot.color.LinearMap(toyplot.color.brewer.palette("Set1")))

@then(u'plots can be rendered with per-series value colors')
def step_impl(context):
    context.axes.plot(context.series, color=context.series_values)

@then(u'plots can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.plot(context.series, color=(context.series_values, toyplot.color.LinearMap()))

@then(u'plots can be rendered with default marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o")

@then(u'plots can be rendered with one explicit marker color')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill="red")

@then(u'plots can be rendered with per-series explicit marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=context.series_colors)

@then(u'plots can be rendered with colormap marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=toyplot.color.LinearMap(toyplot.color.brewer.palette("Set1")))

@then(u'plots can be rendered with per-series value marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=context.series_values)

@then(u'plots can be rendered with per-series value + colormap marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=(context.series_values, toyplot.color.LinearMap()))

@then(u'plots can be rendered with per-datum value marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=context.datum_values)

@then(u'plots can be rendered with per-datum value + colormap marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=(context.datum_values, toyplot.color.LinearMap()))


@then(u'rects can be rendered with default colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1])

@then(u'rects can be rendered with one explicit color')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color="red")

@then(u'rects can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color=context.datum_colors[:-1,0])

@then(u'rects can be rendered with colormap colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color=toyplot.color.LinearMap(toyplot.color.brewer.palette("Set1")))

@then(u'rects can be rendered with per-datum value colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color=context.datum_values[:-1,0])

@then(u'rects can be rendered with per-datum value + colormap colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color=(context.datum_values[:-1,0], toyplot.color.LinearMap()))



@then(u'scatterplots can be rendered with default colors')
def step_impl(context):
    context.axes.scatterplot(context.series)

@then(u'scatterplots can be rendered with one explicit color')
def step_impl(context):
    context.axes.scatterplot(context.series, color="red")

@then(u'scatterplots can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.series_colors)

@then(u'scatterplots can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.datum_colors)

@then(u'scatterplots can be rendered with colormap colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=toyplot.color.LinearMap(toyplot.color.brewer.palette("Set1")))

@then(u'scatterplots can be rendered with per-series value colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.series_values)

@then(u'scatterplots can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=(context.series_values, toyplot.color.LinearMap()))

@then(u'scatterplots can be rendered with per-datum value colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.datum_values)

@then(u'scatterplots can be rendered with per-datum value + colormap colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=(context.datum_values, toyplot.color.LinearMap()))


@then(u'text can be rendered with default colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False)

@then(u'text can be rendered with one explicit color')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color="red")

@then(u'text can be rendered with per-datum explicit colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color=context.datum_colors[:,0])

@then(u'text can be rendered with colormap colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color=toyplot.color.LinearMap(toyplot.color.brewer.palette("Set1")))

@then(u'text can be rendered with per-datum value colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color=datum_values)

@then(u'text can be rendered with per-datum value + colormap colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color=(datum_values, toyplot.color.LinearMap()))


@then(u'vlines can be rendered with default colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0])

@then(u'vlines can be rendered with one explicit color')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color="red")

@then(u'vlines can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color=context.datum_colors[:,0])

@then(u'vlines can be rendered with colormap colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color=toyplot.color.LinearMap(toyplot.color.brewer.palette("Set1")))

@then(u'vlines can be rendered with per-datum value colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.vlines(context.series[:,0], color=datum_values)

@then(u'vlines can be rendered with per-datum value + colormap colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.vlines(context.series[:,0], color=(datum_values, toyplot.color.LinearMap()))

@then(u'bars can be rendered with an array of CSS colors')
def step_impl(context):
    color = numpy.array(["red", "#3f2", "rgb(10%, 20%, 90%)", "rgba(0%, 0%, 0%, 0.5)"])
    context.axes.bars(context.series, baseline="symmetric", color=color)


