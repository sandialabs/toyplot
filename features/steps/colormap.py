# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import testing

import numpy
import toyplot.color

@given(u'a linear color map without a domain')
def step_impl(context):
    context.colormap = toyplot.color.brewer.map("BlueYellowRed")


@given(u'colormap values {}')
def step_impl(context, values):
	context.values = eval(values)


@when(u'mapping colors without a domain')
def step_impl(context):
    context.colors = context.colormap.colors(context.values)


@then(u'the color swatches should match the {} reference html')
def step_impl(context, reference):
    testing.assert_html_equal(toyplot.color._jupyter_color_swatches(context.colors), reference)

