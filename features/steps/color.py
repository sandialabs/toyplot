from __future__ import division

from behave import *

import json
import nose.tools
import numpy
import toyplot.color
import toyplot.testing

@when(u'toyplot.color.css receives {value}')
def step_impl(context, value):
  context.value = value

@then(u'toyplot.color.css should return {value}')
def step_impl(context, value):
  toyplot.testing.assert_color_equal(toyplot.color.css(context.value), eval(value))

@when(u'toyplot.color.to_css receives {value}')
def step_impl(context, value):
  context.value = eval(value)

@then(u'toyplot.color.to_css should return {value}')
def step_impl(context, value):
  nose.tools.assert_equal(toyplot.color.to_css(context.value), value)

@given(u'a collection of Color Brewer palettes')
def step_impl(context):
  context.palettes = {name : toyplot.color.brewer(name) for name in toyplot.color.brewer.names()}

@then(u'each palette can be rendered as ipython html')
def step_impl(context):
  for name, palette in context.palettes.items():
    toyplot.testing.assert_html_equal(palette._repr_html_(), "color-brewer-%s" % name)

@when(u'the user creates a Color Brewer palette')
def step_impl(context):
  context.palette = toyplot.color.brewer("BlueYellowRed")

@then(u'the Color Brewer palette should have the maximum number of colors')
def step_impl(context):
  toyplot.testing.assert_html_equal(context.palette._repr_html_(), "color-brewer")

@when(u'the user creates a sized Color Brewer palette')
def step_impl(context):
  context.palette = toyplot.color.brewer("BlueYellowRed", 5)

@then(u'the Color Brewer palette should have the requested number of colors')
def step_impl(context):
  toyplot.testing.assert_html_equal(context.palette._repr_html_(), "color-brewer-count")

@when(u'the user creates a reversed Color Brewer palette')
def step_impl(context):
  context.palette = toyplot.color.brewer("BlueYellowRed", 5, reverse=True)

@then(u'the Color Brewer palette should have its colors reversed')
def step_impl(context):
  toyplot.testing.assert_html_equal(context.palette._repr_html_(), "color-brewer-reverse")

@when(u'broadcasting one color to a 2d array')
def step_impl(context):
  context.value = toyplot.color.broadcast("red", (4, 4))

@then(u'toyplot.color.broadcast should broadcast the value to the 2d array')
def step_impl(context):
  nose.tools.assert_equal(context.value.shape, (4, 4))
  for value in numpy.nditer(context.value):
    toyplot.testing.assert_color_equal(value, (1, 0, 0, 1))

@when(u'broadcasting a list of colors to a 1d array')
def step_impl(context):
  context.value = toyplot.color.broadcast(["red", "rgb(0, 255, 0)", (0, 0, 1, 1)], 3)

@then(u'toyplot.color.broadcast should broadcast the list to the 1d array')
def step_impl(context):
  numpy.testing.assert_array_equal(context.value, toyplot.color.array([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)]))

@when(u'broadcasting a list of colors to a 2d array')
def step_impl(context):
  context.value = toyplot.color.broadcast(["red", "blue"], (3, 2))

@then(u'toyplot.color.broadcast should broadcast the list to the 2d array')
def step_impl(context):
  numpy.testing.assert_array_equal(context.value, toyplot.color.array([[(1, 0, 0, 1), (0, 0, 1, 1)],[(1, 0, 0, 1), (0, 0, 1, 1)],[(1, 0, 0, 1), (0, 0, 1, 1)]])) 

@when(u'broadcasting a 1d array of css colors to a 1d array')
def step_impl(context):
  context.value = toyplot.color.broadcast(numpy.array(["red", "blue"]), 2)

@then(u'toyplot.color.broadcast should broadcast the 1d array of colors to the 1d array')
def step_impl(context):
  numpy.testing.assert_array_equal(context.value, toyplot.color.array([(1, 0, 0, 1), (0, 0, 1, 1)])) 

@when(u'broadcasting a 1d array of css colors to a 2d array')
def step_impl(context):
  context.value = toyplot.color.broadcast(numpy.array(["red", "blue"]), (2, 2))

@then(u'toyplot.color.broadcast should broadcast the 1d array of colors to the 2d array')
def step_impl(context):
  numpy.testing.assert_array_equal(context.value, toyplot.color.array([[(1, 0, 0, 1), (0, 0, 1, 1)],[(1, 0, 0, 1), (0, 0, 1, 1)]])) 


