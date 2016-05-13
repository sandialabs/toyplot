# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import nose.tools
import numpy

@given(u'single and multi series data')
def step_impl(context):
    context.data = []
    context.data.append(numpy.column_stack((numpy.linspace(0, 1), numpy.linspace(0, 1) ** 2)))
    context.data.append(numpy.linspace(0, 1) ** 3)

@given(u'the data is rendered as bars')
def step_impl(context):
    context.marks = [context.axes.bars(data) for data in context.data]

@given(u'the data is rendered as fills')
def step_impl(context):
    context.marks = [context.axes.fill(data, baseline="symmetric") for data in context.data]

@given(u'the data is rendered as plots')
def step_impl(context):
    context.marks = [context.axes.plot(data) for data in context.data]

@given(u'the data is rendered as scatterplots')
def step_impl(context):
    context.marks = [context.axes.scatterplot(data) for data in context.data]

@given(u'the marks are added to a legend')
def step_impl(context):
    context.entries = [("Mark %s" % index, mark) for index, mark in enumerate(context.marks)]

@given(u'the legend is added to the canvas')
def step_impl(context):
    context.canvas.legend(context.entries, corner=("top-left", 50, 50, 25 * len(context.entries)))


