# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.


from behave import *

import numpy

@given(u'a set of per-series opacity values')
def step_impl(context):
    context.series_opacities = numpy.linspace(1, 0.1, context.series.shape[1])

@given(u'a set of per-datum opacity values')
def step_impl(context):
    numpy.random.seed(1234)
    context.datum_opacities = numpy.random.uniform(0, 1, size=context.series.shape)

@then(u'bars can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", opacity=0.2)

@then(u'bars can be rendered with per-series opacities')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", opacity=numpy.linspace(0.2, 0.8, 4))

@then(u'bars can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", opacity=context.datum_opacities)

@then(u'bars can be rendered with a single series and per-datum opacities')
def step_impl(context):
    context.x = numpy.linspace(0, 1)
    context.series = context.x ** 2
    context.datum_opacities = numpy.linspace(1, 0.1, context.series.shape[0])
    context.axes.bars(context.series, opacity=context.datum_opacities)

@then(u'fills can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.fill(context.series, opacity=0.2)

@then(u'fills can be rendered with per-series opacities')
def step_impl(context):
    context.axes.fill(context.series, opacity=numpy.linspace(0.2, 0.8, 3))

@then(u'hlines can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.hlines(context.series[:,0], opacity=0.1)

@then(u'hlines can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.hlines(context.series[:,0], opacity=context.datum_opacities[:,0])

@then(u'plots can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.plot(context.series, opacity=0.2)

@then(u'plots can be rendered with per-series opacities')
def step_impl(context):
    context.axes.plot(context.series, opacity=context.series_opacities)

@then(u'rects can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.rectangle(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], opacity=0.2)

@then(u'rects can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.rectangle(context.series[:-1,0], context.series[1:,0], context.series[:-1,1], context.series[1:,1], opacity=context.datum_opacities[:-1,0])

@then(u'scatterplots can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.scatterplot(context.series, opacity=0.2)

@then(u'scatterplots can be rendered with per-series opacities')
def step_impl(context):
    context.axes.scatterplot(context.series, opacity=context.series_opacities)

@then(u'scatterplots can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.scatterplot(context.series, opacity=context.datum_opacities)

@then(u'text can be rendered with one explicit opacity')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, opacity=0.2)

@then(u'text can be rendered with per-datum opacities')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, annotation=False, opacity=context.datum_opacities[:,0])

@then(u'vlines can be rendered with one explicit opacity')
def step_impl(context):
    context.axes.vlines(context.series[:,0], opacity=0.1)

@then(u'vlines can be rendered with per-datum opacities')
def step_impl(context):
    context.axes.vlines(context.series[:,0], opacity=context.datum_opacities[:,0])


