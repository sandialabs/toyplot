# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *
import io
import nose.tools
import numpy.testing
import toyplot.testing
import xml.etree.ElementTree as xml

@given(u'a canvas with a border')
def step_impl(context):
    context.canvas = toyplot.Canvas(style={"border":"1px solid %s" % toyplot.color.near_black})

@then(u'axes can be added to the canvas using the default layout.')
def step_impl(context):
    context.canvas.cartesian(label="Default Layout")

@then(u'axes can be added to the canvas using explicit bounds.')
def step_impl(context):
    context.canvas.cartesian(bounds=(100, 200, 100, 200), label="100, 200, 100, 200")
    context.canvas.cartesian(bounds=(-200, -100, -200, -100), label="-200, -100, -200, -100")
    context.canvas.cartesian(bounds=("50%", "85%", "1cm", (2, "cm")), label="50%, 85%, 1cm, (2, cm)")
    context.canvas.cartesian(bounds=("1cm", "50%", "50%", "-1cm"), label="1cm, 50%, 50%, -1cm")

@then(u'axes can be added to the canvas using grid layout.')
def step_impl(context):
    context.canvas.cartesian(grid=(3, 3, 0), label="3x3")
    context.canvas.cartesian(grid=(3, 3, 0, 1, 1, 2), label="3x3 colspan=2")
    context.canvas.cartesian(grid=(3, 3, 1, 0), gutter=30, label="3x3 gutter=30")
    context.canvas.cartesian(grid=(3, 3, 1, 1), gutter=30, label="3x3 gutter=30")
    context.canvas.cartesian(
        grid=(
            3,
            3,
            1,
            2,
            2,
            1),
        gutter=30,
        label="3x3 gutter=30 rowspan=2")

@then(u'axes can be added to the canvas using corner layout.')
def step_impl(context):
    context.canvas.cartesian(label="top", corner=("top", 30, 100, 30))
    context.canvas.cartesian(label="top-right", corner=("top-right", 30, 100, 30))
    context.canvas.cartesian(label="right", corner=("right", 30, 100, 30))
    context.canvas.cartesian(label="bottom-right", corner=("bottom-right", 30, 100, 30))
    context.canvas.cartesian(label="bottom", corner=("bottom", 30, 100, 30))
    context.canvas.cartesian(label="bottom-left", corner=("bottom-left", 30, 100, 30))
    context.canvas.cartesian(label="left", corner=("left", 30, 100, 30))
    context.canvas.cartesian(label="top-left", corner=("top-left", 30, 100, 30))

@then(u'axes can be added to the canvas using rect layout.')
def step_impl(context):
    context.canvas.cartesian(rect=(100, 100, 100, 100), label="100, 200, 100, 100")
    context.canvas.cartesian(rect=(-200, -200, 100, 100), label="-200, -200, 100, 100")
    context.canvas.cartesian(rect=("25%", 250, "50%", "10%"), label="25%, 250, 50%, 10%")
    context.canvas.cartesian(rect=("10%", 400, "5cm", "1cm"), label="10%, 400, 5cm, 1cm")

@then(u'the canvas can be rendered in Jupyter as HTML')
def step_impl(context):
    html = context.canvas._repr_html_()
    nose.tools.assert_is_instance(html, toyplot.compatibility.string_type)

@then(u'the canvas can be rendered in Jupyter as a PNG image')
def step_impl(context):
    png = context.canvas._repr_png_()
    image = toyplot.testing.read_png(io.BytesIO(png))
    nose.tools.assert_equal(image.shape, (600, 600, 4))
    nose.tools.assert_equal(image.dtype, "uint8")

@then(u'numberlines can be added to the canvas using relative coordinates')
def step_impl(context):
    context.canvas.numberline(-400, -400, -100, -100)

