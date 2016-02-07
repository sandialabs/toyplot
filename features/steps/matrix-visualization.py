# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import numpy
import toyplot.locator

@given(u'a matrix')
def step_impl(context):
    numpy.random.seed(1234)
    context.matrix = numpy.random.normal(size=(10, 10))

@given(u'a matrix visualization created with the convenience API')
def step_impl(context):
    context.canvas, table = toyplot.matrix(context.matrix)

@given(u'a matrix visualization created with the standard API')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    table = context.canvas.matrix(context.matrix)

@given(u'a matrix visualization created with a custom palette')
def step_impl(context):
    palette = toyplot.color.brewer.palette("BlueGreenBrown")
    context.canvas = toyplot.Canvas()
    table = context.canvas.matrix((context.matrix, palette))

@given(u'a matrix visualization created with a custom colormap')
def step_impl(context):
    palette = toyplot.color.brewer.palette("BlueGreenBrown")
    colormap = toyplot.color.LinearMap(palette, domain_min=-1, domain_max=1)
    context.canvas = toyplot.Canvas()
    table = context.canvas.matrix((context.matrix, colormap))

@given(u'a matrix visualization created with custom labels')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    table = context.canvas.matrix(context.matrix, tlabel="Top", blabel="Bottom", llabel="Left", rlabel="Right", rshow=True, bshow=True)

@given(u'a matrix visualization created with right and bottom index locators')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    table = context.canvas.matrix(context.matrix, rlocator=toyplot.locator.Integer(), blocator=toyplot.locator.Integer())

