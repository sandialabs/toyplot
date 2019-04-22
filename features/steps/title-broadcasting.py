# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.


from behave import *

import numpy

@given(u'a set of per-series title values')
def step_impl(context):
    context.series_titles = numpy.array(["S%s" % series for series in numpy.arange(context.series.shape[1])])

@given(u'a set of per-datum title values')
def step_impl(context):
    context.datum_titles = numpy.array([["S%sD%s" % (series, datum) for series in numpy.arange(context.series.shape[1])] for datum in numpy.arange(context.series.shape[0])])

@then(u'bars can be rendered with one explicit title')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", title="bar")

@then(u'bars can be rendered with per-series titles')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", title=context.series_titles)

@then(u'bars can be rendered with per-datum titles')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", title=context.datum_titles)

@then(u'bars can be rendered with a single series and per-datum titles')
def step_impl(context):
    context.x = numpy.linspace(0, 1)
    context.series = context.x ** 2
    context.series_titles = numpy.array(["S%s" % series for series in numpy.arange(context.series.shape[0])])
    context.axes.bars(context.series, title=context.series_titles)

@then(u'fills can be rendered with one explicit title')
def step_impl(context):
    context.axes.fill(context.series, title="fill")

@then(u'fills can be rendered with per-series titles')
def step_impl(context):
    context.axes.fill(context.series, title=context.series_titles[:-1])

@then(u'hlines can be rendered with one explicit title')
def step_impl(context):
    context.axes.hlines(context.series[:,0], title="hline")

@then(u'hlines can be rendered with per-datum titles')
def step_impl(context):
    context.axes.hlines(context.series[:,0], title=context.datum_titles[:,0])

@then(u'plots can be rendered with one explicit title')
def step_impl(context):
    context.axes.plot(context.series, title="plot")

@then(u'plots can be rendered with per-series titles')
def step_impl(context):
    context.axes.plot(context.series, title=context.series_titles)

@then(u'plots can be rendered with per datum titles')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mtitle=context.datum_titles)

@then(u'plots can be rendered with per-series and per datum titles')
def step_impl(context):
    context.axes.plot(context.series, title=context.series_titles, marker="o", mtitle=context.datum_titles)

@then(u'rects can be rendered with one explicit title')
def step_impl(context):
    context.axes.rectangle(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], title="rect")

@then(u'rects can be rendered with per-datum titles')
def step_impl(context):
    context.axes.rectangle(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], title=context.datum_titles[:-1,0])

@then(u'scatterplots can be rendered with one explicit title')
def step_impl(context):
    context.axes.scatterplot(context.series, title="scatterplot")

@then(u'scatterplots can be rendered with per-series titles')
def step_impl(context):
    context.axes.scatterplot(context.series, title=context.series_titles)

@then(u'scatterplots can be rendered with per-datum titles')
def step_impl(context):
    context.axes.scatterplot(context.series, title=context.datum_titles)

@then(u'text can be rendered with one explicit title')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, title="text")

@then(u'text can be rendered with per-datum titles')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, title=context.datum_titles[:,0])

@then(u'vlines can be rendered with one explicit title')
def step_impl(context):
    context.axes.vlines(context.series[:,0], title="vline")

@then(u'vlines can be rendered with per-datum titles')
def step_impl(context):
    context.axes.vlines(context.series[:,0], title=context.datum_titles[:,0])


