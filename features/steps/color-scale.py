# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import numpy
import toyplot.color

@given(u'a linear colormap')
def step_impl(context):
    context.colormap = toyplot.color.brewer.map("BlueRed", domain_min=0, domain_max=1)

@given(u'a categorical colormap')
def step_impl(context):
    context.colormap = toyplot.color.CategoricalMap()

@then(u'a vertical color scale can be added to the canvas')
def step_impl(context):
    context.canvas.color_scale(context.colormap, x1=100, x2=100, y1="-10%", y2="10%")

@then(u'a diagonal color scale can be added to the canvas')
def step_impl(context):
    context.canvas.color_scale(context.colormap, x1=100, x2=-100, y1=-100, y2=100)

@given(u'a set of default axes')
def step_impl(context):
    context.axes = context.canvas.axes()

@then(u'a color scale can be added to the axes')
def step_impl(context):
    context.axes.color_scale(context.colormap)

@then(u'a color scale with default colormap can be added to a matrix visualization')
def step_impl(context):
    numpy.random.seed(1234)
    values = numpy.random.normal(size=(10, 10))
    context.canvas.matrix(values, colorshow=True)

@then(u'a color scale with linear colormap can be added to a matrix visualization')
def step_impl(context):
    numpy.random.seed(1234)
    values = numpy.random.normal(size=(10, 10))
    colormap = toyplot.color.brewer.map("BlueGreenBrown", domain_min=-2, domain_max=2)
    context.canvas.matrix((values, colormap), colorshow=True)

