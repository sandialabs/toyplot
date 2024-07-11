# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import test
import numpy

def sample_data():
    data = []
    data.append(numpy.column_stack((numpy.linspace(0, 1), numpy.linspace(0, 1) ** 2)))
    data.append(numpy.linspace(0, 1) ** 3)
    return data


@given(u'the data is rendered as boundary bars')
def step_impl(context):
    context.marks = [context.axes.bars(data, baseline=None) for data in sample_data()]


@given(u'the data is rendered as boundary fills')
def step_impl(context):
    context.marks = [context.axes.fill(data, baseline=None) for data in sample_data()]


@given(u'the data is rendered as magnitude bars')
def step_impl(context):
    context.marks = [context.axes.bars(data, baseline="symmetric") for data in sample_data()]


@given(u'the data is rendered as magnitude fills')
def step_impl(context):
    context.marks = [context.axes.fill(data, baseline="symmetric") for data in sample_data()]


@given(u'the data is rendered as plots')
def step_impl(context):
    context.marks = [context.axes.plot(data) for data in sample_data()]


@given(u'the data is rendered as scatterplots')
def step_impl(context):
    context.marks = [context.axes.scatterplot(data) for data in sample_data()]


@given(u'the marks are used to create a legend')
def step_impl(context):
    entries = [("Mark %s" % index, mark) for index, mark in enumerate(context.marks)]
    table = context.canvas.legend(entries, corner=("top-left", 50, 100, 25 * len(entries)))
    table.cells.grid.hlines[...] = "single"
    table.cells.grid.vlines[...] = "single"


