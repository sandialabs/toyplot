from __future__ import division

from behave import *

import numpy
import toyplot.color
import toyplot.testing

@given(u'a set of diverging series')
def step_impl(context):
    context.x = numpy.linspace(0, 1)
    context.series = numpy.column_stack((context.x**2, context.x**2/2, context.x**2/3, context.x**2/4))

@given(u'a set of per-series values')
def step_impl(context):
    context.series_values = numpy.array([1, 4, 3, 2])

@given(u'a set of per-series colors')
def step_impl(context):
    context.series_colors = ["red", "green", "blue", "yellow"]

@given(u'a set of per-datum values')
def step_impl(context):
    numpy.random.seed(1234)
    context.datum_values = numpy.column_stack((
        numpy.random.normal(loc=0, size=context.series.shape[0]),
        numpy.random.normal(loc=3, size=context.series.shape[0]),
        numpy.random.normal(loc=6, size=context.series.shape[0]),
        numpy.random.normal(loc=9, size=context.series.shape[0]),
        ))

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
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-default")

@then(u'bars can be rendered with one explicit color')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-one-color")

@then(u'bars can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.series_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-series-colors")

@then(u'bars can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.datum_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-datum-colors")

@then(u'bars can be rendered with palette colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-palette")

@then(u'bars can be rendered with colormap colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-colormap")

@then(u'bars can be rendered with per-series value colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.series_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-series-values")

@then(u'bars can be rendered with per-series value + palette colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=(context.series_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-series-values-palette")

@then(u'bars can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=(context.series_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-series-values-colormap")

@then(u'bars can be rendered with per-datum value colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-datum-values")

@then(u'bars can be rendered with per-datum value + palette colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=(context.datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-datum-values-palette")

@then(u'bars can be rendered with per-datum value + colormap colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=(context.datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-datum-values-colormap")


@then(u'fills can be rendered with default colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-default")

@then(u'fills can be rendered with one explicit color')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-one-color")

@then(u'fills can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=context.series_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-per-series-colors")

@then(u'fills can be rendered with palette colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-palette")

@then(u'fills can be rendered with colormap colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-colormap")

@then(u'fills can be rendered with per-series value colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=context.series_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-per-series-values")

@then(u'fills can be rendered with per-series value + palette colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=(context.series_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-per-series-values-palette")

@then(u'fills can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=(context.series_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-per-series-values-colormap")



@then(u'hlines can be rendered with default colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-default")

@then(u'hlines can be rendered with one explicit color')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-one-color")

@then(u'hlines can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color=context.datum_colors[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-per-datum-colors")

@then(u'hlines can be rendered with palette colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-palette")

@then(u'hlines can be rendered with colormap colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-colormap")

@then(u'hlines can be rendered with per-datum value colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.hlines(context.series[:,0], color=datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-per-datum-values")

@then(u'hlines can be rendered with per-datum value + palette colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.hlines(context.series[:,0], color=(datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-per-datum-values-palette")

@then(u'hlines can be rendered with per-datum value + colormap colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.hlines(context.series[:,0], color=(datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-per-datum-values-colormap")

@then(u'plots can be rendered with default colors')
def step_impl(context):
    context.axes.plot(context.series)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-default")

@then(u'plots can be rendered with one explicit color')
def step_impl(context):
    context.axes.plot(context.series, color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-one-color")

@then(u'plots can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.plot(context.series, color=context.series_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-colors")

@then(u'plots can be rendered with palette colors')
def step_impl(context):
    context.axes.plot(context.series, color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-palette")

@then(u'plots can be rendered with colormap colors')
def step_impl(context):
    context.axes.plot(context.series, color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-colormap")

@then(u'plots can be rendered with per-series value colors')
def step_impl(context):
    context.axes.plot(context.series, color=context.series_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values")

@then(u'plots can be rendered with per-series value + palette colors')
def step_impl(context):
    context.axes.plot(context.series, color=(context.series_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values-palette")

@then(u'plots can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.plot(context.series, color=(context.series_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values-colormap")

@then(u'plots can be rendered with default marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-marker-default")

@then(u'plots can be rendered with one explicit marker color')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-one-marker-color")

@then(u'plots can be rendered with per-series explicit marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=context.series_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-marker-colors")

@then(u'plots can be rendered with palette marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-palette-marker")

@then(u'plots can be rendered with colormap marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-colormap-marker")

@then(u'plots can be rendered with per-series value marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=context.series_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values-marker")

@then(u'plots can be rendered with per-series value + palette marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=(context.series_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values-palette-marker")

@then(u'plots can be rendered with per-series value + colormap marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=(context.series_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values-colormap-marker")

@then(u'plots can be rendered with per-datum value marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=context.datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-datum-values-marker")

@then(u'plots can be rendered with per-datum value + palette marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=(context.datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-datum-values-palette-marker")

@then(u'plots can be rendered with per-datum value + colormap marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=(context.datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-datum-values-colormap-marker")


@then(u'rects can be rendered with default colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-rects-default")

@then(u'rects can be rendered with one explicit color')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-rects-one-color")

@then(u'rects can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color=context.datum_colors[:-1,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-rects-per-datum-colors")

@then(u'rects can be rendered with palette colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-rects-palette")

@then(u'rects can be rendered with colormap colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-rects-colormap")

@then(u'rects can be rendered with per-datum value colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color=context.datum_values[:-1,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-rects-per-datum-values")

@then(u'rects can be rendered with per-datum value + palette colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color=(context.datum_values[:-1,0], toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-rects-per-datum-values-palette")

@then(u'rects can be rendered with per-datum value + colormap colors')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], color=(context.datum_values[:-1,0], toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-rects-per-datum-values-colormap")



@then(u'scatterplots can be rendered with default colors')
def step_impl(context):
    context.axes.scatterplot(context.series)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-default")

@then(u'scatterplots can be rendered with one explicit color')
def step_impl(context):
    context.axes.scatterplot(context.series, color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-one-color")

@then(u'scatterplots can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.series_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-series-colors")

@then(u'scatterplots can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.datum_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-datum-colors")

@then(u'scatterplots can be rendered with palette colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-palette")

@then(u'scatterplots can be rendered with colormap colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-colormap")

@then(u'scatterplots can be rendered with per-series value colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.series_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-series-values")

@then(u'scatterplots can be rendered with per-series value + palette colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=(context.series_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-series-values-palette")

@then(u'scatterplots can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=(context.series_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-series-values-colormap")

@then(u'scatterplots can be rendered with per-datum value colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-datum-values")

@then(u'scatterplots can be rendered with per-datum value + palette colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=(context.datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-datum-values-palette")

@then(u'scatterplots can be rendered with per-datum value + colormap colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=(context.datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-datum-values-colormap")


@then(u'text can be rendered with default colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-default")

@then(u'text can be rendered with one explicit color')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-one-color")

@then(u'text can be rendered with per-datum explicit colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color=context.datum_colors[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-per-datum-colors")

@then(u'text can be rendered with palette colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-palette")

@then(u'text can be rendered with colormap colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-colormap")

@then(u'text can be rendered with per-datum value colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color=datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-per-datum-values")

@then(u'text can be rendered with per-datum value + palette colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color=(datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-per-datum-values-palette")

@then(u'text can be rendered with per-datum value + colormap colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.text(context.x, context.series[:,0], text, annotation=False, color=(datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-per-datum-values-colormap")


@then(u'vlines can be rendered with default colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-default")

@then(u'vlines can be rendered with one explicit color')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-one-color")

@then(u'vlines can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color=context.datum_colors[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-per-datum-colors")

@then(u'vlines can be rendered with palette colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-palette")

@then(u'vlines can be rendered with colormap colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-colormap")

@then(u'vlines can be rendered with per-datum value colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.vlines(context.series[:,0], color=datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-per-datum-values")

@then(u'vlines can be rendered with per-datum value + palette colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.vlines(context.series[:,0], color=(datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-per-datum-values-palette")

@then(u'vlines can be rendered with per-datum value + colormap colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.vlines(context.series[:,0], color=(datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-per-datum-values-colormap")


