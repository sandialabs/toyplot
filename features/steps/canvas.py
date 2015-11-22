from behave import *
import nose.tools
import numpy.testing
import toyplot.testing

@when(u'adding axes to a canvas, they can be positioned using the default layout.')
def step_impl(context):
    canvas = toyplot.Canvas(style={"border":"1px solid %s" % toyplot.color.near_black})
    canvas.axes(label="Default Layout")
    toyplot.testing.assert_canvas_equal(canvas, "canvas-layout-default")

@when(u'adding axes to a canvas, they can be positioned using explicit bounds.')
def step_impl(context):
    canvas = toyplot.Canvas(style={"border":"1px solid %s" % toyplot.color.near_black})
    canvas.axes(bounds=(100, 200, 100, 200), label="100, 200, 100, 200")
    canvas.axes(bounds=(-200, -100, -200, -100), label="-200, -100, -200, -100")
    canvas.axes(bounds=("50%", "85%", "1cm", (2, "cm")), label="50%, 85%, 1cm, (2, cm)")
    canvas.axes(bounds=("1cm", "50%", "50%", "-1cm"), label="1cm, 50%, 50%, -1cm")
    toyplot.testing.assert_canvas_equal(canvas, "canvas-layout-bounds")

@when(u'adding axes to a canvas, they can be positioned using grid layout.')
def step_impl(context):
    canvas = toyplot.Canvas(style={"border":"1px solid %s" % toyplot.color.near_black})
    canvas.axes(grid=(3, 3, 0), label="3x3")
    canvas.axes(grid=(3, 3, 0, 1, 1, 2), label="3x3 colspan=2")
    canvas.axes(grid=(3, 3, 1, 0), gutter=30, label="3x3 gutter=30")
    canvas.axes(grid=(3, 3, 1, 1), gutter=30, label="3x3 gutter=30")
    canvas.axes(
        grid=(
            3,
            3,
            1,
            2,
            2,
            1),
        gutter=30,
        label="3x3 gutter=30 rowspan=2")
    toyplot.testing.assert_canvas_equal(canvas, "canvas-layout-grid")

@when(u'adding axes to a canvas, they can be positioned using corner layout.')
def step_impl(context):
    style = {"stroke": toyplot.color.near_black}
    canvas = toyplot.Canvas(style={"border": "1px solid %s" % toyplot.color.near_black})
    canvas.legend([("top", "^")], style=style, corner=("top", 10, 100, 30))
    canvas.legend([("top-right", "^")], style=style, corner=("top-right", 10, 100, 30))
    canvas.legend([("right", "^")], style=style, corner=("right", 10, 100, 30))
    canvas.legend([("bottom-right", "^")], style=style, corner=("bottom-right", 10, 150, 30))
    canvas.legend([("bottom-right", "^")], style=style, corner=("bottom-right", "2cm", (4,"cm"), "10%"))
    canvas.legend([("bottom", "^")], style=style, corner=("bottom", 10, 100, 30))
    canvas.legend([("bottom-left", "^")], style=style, corner=("bottom-left", 10, 100, 30))
    canvas.legend([("left", "^")], style=style, corner=("left", 10, 100, 30))
    canvas.legend([("top-left", "^")], style=style, corner=("top-left", 10, 100, 30))
    canvas.legend([("top-left", "^")], style=style, corner=("top-left", 50, 100, 30))
    canvas.legend([("top-left", "^")], style=style, corner=("top-left", 100, "20%", "10%"))
    toyplot.testing.assert_canvas_equal(canvas, "canvas-layout-corner")

@when(u'adding axes to a canvas, they can be positioned using rect layout.')
def step_impl(context):
    canvas = toyplot.Canvas(style={"border":"1px solid %s" % toyplot.color.near_black})
    canvas.axes(rect=(100, 100, 100, 100), label="100, 200, 100, 100")
    canvas.axes(rect=(-200, -200, 100, 100), label="-200, -200, 100, 100")
    canvas.axes(rect=("25%", 250, "50%", "10%"), label="25%, 250, 50%, 10%")
    canvas.axes(rect=("10%", 400, "5cm", "1cm"), label="10%, 400, 5cm, 1cm")
    toyplot.testing.assert_canvas_equal(canvas, "canvas-layout-rect")

