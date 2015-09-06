from __future__ import division

from behave import *

import numpy
import toyplot.testing

@given(u'a set of per-series title values')
def step_impl(context):
    context.series_titles = numpy.array(["S%s" % series for series in numpy.arange(context.series.shape[1])])

@given(u'a set of per-datum title values')
def step_impl(context):
    context.datum_titles = numpy.array([["S%sD%s" % (series, datum) for series in numpy.arange(context.series.shape[1])] for datum in numpy.arange(context.series.shape[0])])

@then(u'bars can be rendered with one explicit title')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", title="bar")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-bars-one-title")

@then(u'bars can be rendered with per-series titles')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", title=context.series_titles)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-bars-per-series-titles")

@then(u'bars can be rendered with per-datum titles')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", title=context.datum_titles)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-bars-per-datum-titles")

@then(u'fills can be rendered with one explicit title')
def step_impl(context):
    context.axes.fill(context.series, title="fill")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-fills-one-title")

@then(u'fills can be rendered with per-series titles')
def step_impl(context):
    context.axes.fill(context.series, title=context.series_titles[:-1])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-fills-per-series-titles")

@then(u'hlines can be rendered with one explicit title')
def step_impl(context):
    context.axes.hlines(context.series[:,0], title="hline")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-hlines-one-title")

@then(u'hlines can be rendered with per-datum titles')
def step_impl(context):
    context.axes.hlines(context.series[:,0], title=context.datum_titles[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-hlines-per-datum-titles")

@then(u'plots can be rendered with one explicit title')
def step_impl(context):
    context.axes.plot(context.series, title="plot")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-plots-one-title")

@then(u'plots can be rendered with per-series titles')
def step_impl(context):
    context.axes.plot(context.series, title=context.series_titles)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-plots-per-series-titles")

@then(u'rects can be rendered with one explicit title')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], title="rect")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-rects-one-title")

@then(u'rects can be rendered with per-datum titles')
def step_impl(context):
    context.axes.rects(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], title=context.datum_titles[:-1,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-rects-per-datum-titles")

@then(u'scatterplots can be rendered with one explicit title')
def step_impl(context):
    context.axes.scatterplot(context.series, title="scatterplot")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-scatterplots-one-title")

@then(u'scatterplots can be rendered with per-series titles')
def step_impl(context):
    context.axes.scatterplot(context.series, title=context.series_titles)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-scatterplots-per-series-titles")

@then(u'scatterplots can be rendered with per-datum titles')
def step_impl(context):
    context.axes.scatterplot(context.series, title=context.datum_titles)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-scatterplots-per-datum-titles")

@then(u'text can be rendered with one explicit title')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, title="text")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-text-one-title")

@then(u'text can be rendered with per-datum titles')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, title=context.datum_titles[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-text-per-datum-titles")

@then(u'vlines can be rendered with one explicit title')
def step_impl(context):
    context.axes.vlines(context.series[:,0], title="vline")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-vlines-one-title")

@then(u'vlines can be rendered with per-datum titles')
def step_impl(context):
    context.axes.vlines(context.series[:,0], title=context.datum_titles[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "title-broadcast-vlines-per-datum-titles")


