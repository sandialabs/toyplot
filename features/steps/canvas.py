from behave import *
import PIL.Image
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
    context.canvas.axes(label="Default Layout")

@then(u'axes can be added to the canvas using explicit bounds.')
def step_impl(context):
    context.canvas.axes(bounds=(100, 200, 100, 200), label="100, 200, 100, 200")
    context.canvas.axes(bounds=(-200, -100, -200, -100), label="-200, -100, -200, -100")
    context.canvas.axes(bounds=("50%", "85%", "1cm", (2, "cm")), label="50%, 85%, 1cm, (2, cm)")
    context.canvas.axes(bounds=("1cm", "50%", "50%", "-1cm"), label="1cm, 50%, 50%, -1cm")

@then(u'axes can be added to the canvas using grid layout.')
def step_impl(context):
    context.canvas.axes(grid=(3, 3, 0), label="3x3")
    context.canvas.axes(grid=(3, 3, 0, 1, 1, 2), label="3x3 colspan=2")
    context.canvas.axes(grid=(3, 3, 1, 0), gutter=30, label="3x3 gutter=30")
    context.canvas.axes(grid=(3, 3, 1, 1), gutter=30, label="3x3 gutter=30")
    context.canvas.axes(
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
    style = {"stroke": toyplot.color.near_black}
    context.canvas.legend([("top", "^")], style=style, corner=("top", 10, 100, 30))
    context.canvas.legend([("top-right", "^")], style=style, corner=("top-right", 10, 100, 30))
    context.canvas.legend([("right", "^")], style=style, corner=("right", 10, 100, 30))
    context.canvas.legend([("bottom-right", "^")], style=style, corner=("bottom-right", 10, 150, 30))
    context.canvas.legend([("bottom-right", "^")], style=style, corner=("bottom-right", "2cm", (4,"cm"), "10%"))
    context.canvas.legend([("bottom", "^")], style=style, corner=("bottom", 10, 100, 30))
    context.canvas.legend([("bottom-left", "^")], style=style, corner=("bottom-left", 10, 100, 30))
    context.canvas.legend([("left", "^")], style=style, corner=("left", 10, 100, 30))
    context.canvas.legend([("top-left", "^")], style=style, corner=("top-left", 10, 100, 30))
    context.canvas.legend([("top-left", "^")], style=style, corner=("top-left", 50, 100, 30))
    context.canvas.legend([("top-left", "^")], style=style, corner=("top-left", 100, "20%", "10%"))

@then(u'axes can be added to the canvas using rect layout.')
def step_impl(context):
    context.canvas.axes(rect=(100, 100, 100, 100), label="100, 200, 100, 100")
    context.canvas.axes(rect=(-200, -200, 100, 100), label="-200, -200, 100, 100")
    context.canvas.axes(rect=("25%", 250, "50%", "10%"), label="25%, 250, 50%, 10%")
    context.canvas.axes(rect=("10%", 400, "5cm", "1cm"), label="10%, 400, 5cm, 1cm")

@then(u'the canvas can be rendered in Jupyter as HTML')
def step_impl(context):
    html = context.canvas._repr_html_()
    nose.tools.assert_is_instance(html, toyplot.compatibility.string_type)

@then(u'the canvas can be rendered in Jupyter as a PNG image')
def step_impl(context):
    png = context.canvas._repr_png_()
    image = PIL.Image.open(io.BytesIO(png))
    nose.tools.assert_equal(image.format, "PNG")

