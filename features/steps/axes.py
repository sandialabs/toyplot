from behave import *

import nose
import numpy
import toyplot.data
import toyplot.testing


@given(u'a set of cartesian axes')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    context.axes = context.canvas.axes()


@given(u'a default plot')
def step_impl(context):
    context.axes.plot(numpy.sin(numpy.linspace(0, 10)))


@then(u'the cartesian axes can be rendered with defaults')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-defaults")


@then(u'the cartesian axes can be rendered with hidden axes')
def step_impl(context):
    context.axes.show = False
    nose.tools.assert_equal(context.axes.show, False)
    toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-show")


@then(u'the cartesian axes can be rendered with axes label')
def step_impl(context):
    context.axes.label.text = "Howdy!"
    nose.tools.assert_equal(context.axes.label.text, "Howdy!")
    context.axes.label.style = {"fill": "red"}
    nose.tools.assert_equal(context.axes.label.style["fill"], "red")
    toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-label")


@then(u'the cartesian axes can be rendered with hidden x axis')
def step_impl(context):
    context.axes.x.show = False
    nose.tools.assert_equal(context.axes.x.show, False)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-show")


@then(u'the cartesian axes can be rendered with log-10 x scale')
def step_impl(context):
    context.axes.x.scale = "log"
    nose.tools.assert_equal(context.axes.x.scale, ("log", 10))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-scale")


@then(u'the cartesian axes can be rendered with hidden x spine')
def step_impl(context):
    context.axes.x.spine.show = False
    nose.tools.assert_equal(context.axes.x.spine.show, False)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-spine-show")


@then(
    u'the cartesian axes can be rendered with x spine at an explicit position')
def step_impl(context):
    context.axes.x.spine.position = 0
    nose.tools.assert_equal(context.axes.x.spine.position, 0)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-spine-position")


@then(u'the cartesian axes can be rendered with x spine at the high end of y')
def step_impl(context):
    context.axes.x.spine.position = "high"
    nose.tools.assert_equal(context.axes.x.spine.position, "high")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-spine-position-high")


@then(u'the cartesian axes can be rendered with styled x spine')
def step_impl(context):
    context.axes.x.spine.style = {"stroke": "red"}
    nose.tools.assert_equal(context.axes.x.spine.style["stroke"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-spine-style")


@then(u'the cartesian axes can be rendered with visible x ticks')
def step_impl(context):
    context.axes.x.ticks.show = True
    nose.tools.assert_equal(context.axes.x.ticks.show, True)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-show")


@then(u'the cartesian axes can be rendered with sized x ticks')
def step_impl(context):
    context.axes.x.ticks.show = True
    context.axes.x.ticks.length = 20
    nose.tools.assert_equal(context.axes.x.ticks.length, 20)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-length")


@then(u'the cartesian axes can be rendered with styled x ticks')
def step_impl(context):
    context.axes.x.ticks.show = True
    context.axes.x.ticks.style = {"stroke": "red"}
    nose.tools.assert_equal(context.axes.x.ticks.style["stroke"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-style")


@then(
    u'the cartesian axes can be rendered with x ticks controlled by a locator')
def step_impl(context):
    context.axes.x.ticks.show = True
    locator = toyplot.locator.Basic(count=11)
    context.axes.x.ticks.locator = locator
    nose.tools.assert_is(context.axes.x.ticks.locator, locator)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-locator")


@then(
    u'the cartesian axes can be rendered with x axis per-tick styles identified by index')
def step_impl(context):
    context.axes.x.ticks.show = True
    context.axes.x.ticks.tick(index=0).style = {"stroke": "red"}
    nose.tools.assert_equal(
        context.axes.x.ticks.tick(index=0).style["stroke"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-tick-index-style")


@then(
    u'the cartesian axes can be rendered with x axis per-tick styles identified by value')
def step_impl(context):
    context.axes.x.ticks.show = True
    context.axes.x.ticks.tick(value=0).style = {"stroke": "red"}
    nose.tools.assert_equal(
        context.axes.x.ticks.tick(value=0).style["stroke"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-tick-value-style")


@then(u'the cartesian axes can be rendered with hidden x tick labels')
def step_impl(context):
    context.axes.x.ticks.labels.show = False
    nose.tools.assert_equal(context.axes.x.ticks.labels.show, False)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-labels-show")


@then(u'the cartesian axes can be rendered with angled x tick labels')
def step_impl(context):
    context.axes.x.ticks.labels.angle = -45
    nose.tools.assert_equal(context.axes.x.ticks.labels.angle, -45)
    context.axes.x.ticks.show = True
    context.axes.x.ticks.labels.offset = 10
    context.axes.x.ticks.labels.style = {
        "text-anchor": "middle", "baseline-shift": 0}
    nose.tools.assert_equal(
        context.axes.x.ticks.labels.style["text-anchor"], "middle")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-labels-angle")


@then(u'the cartesian axes can be rendered with styled x tick labels')
def step_impl(context):
    context.axes.x.ticks.labels.style = {"fill": "red"}
    nose.tools.assert_equal(context.axes.x.ticks.labels.style["fill"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-labels-style")


@then(
    u'the cartesian axes can be rendered with x axis per-tick-label styles identified by index')
def step_impl(context):
    context.axes.x.ticks.labels.label(index=0).style = {"fill": "red"}
    nose.tools.assert_equal(
        context.axes.x.ticks.labels.label(index=0).style["fill"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-labels-label-index-style")


@then(
    u'the cartesian axes can be rendered with x axis per-tick-label styles identified by value')
def step_impl(context):
    context.axes.x.ticks.labels.label(value=0).style = {"fill": "red"}
    nose.tools.assert_equal(
        context.axes.x.ticks.labels.label(value=0).style["fill"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-ticks-labels-label-value-style")


@then(u'the cartesian axes can be rendered with x axis label')
def step_impl(context):
    context.axes.x.label.text = "Howdy!"
    nose.tools.assert_equal(context.axes.x.label.text, "Howdy!")
    context.axes.x.label.style = {"fill": "red"}
    nose.tools.assert_equal(context.axes.x.label.style["fill"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-label")


@then(u'the cartesian axes can be rendered with explicit x axis domain')
def step_impl(context):
    context.axes.x.domain.min = 0
    nose.tools.assert_equal(context.axes.x.domain.min, 0)
    context.axes.x.domain.max = 1
    nose.tools.assert_equal(context.axes.x.domain.max, 1)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-x-domain")


@then(u'the cartesian axes can be rendered with hidden y axis')
def step_impl(context):
    context.axes.y.show = False
    nose.tools.assert_equal(context.axes.y.show, False)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-show")


@then(u'the cartesian axes can be rendered with log-10 y scale')
def step_impl(context):
    context.axes.y.scale = "log"
    nose.tools.assert_equal(context.axes.y.scale, ("log", 10))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-scale")


@then(u'the cartesian axes can be rendered with hidden y spine')
def step_impl(context):
    context.axes.y.spine.show = False
    nose.tools.assert_equal(context.axes.y.spine.show, False)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-spine-show")


@then(
    u'the cartesian axes can be rendered with y spine at an explicit position')
def step_impl(context):
    context.axes.y.spine.position = 10
    nose.tools.assert_equal(context.axes.y.spine.position, 10)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-spine-position")


@then(u'the cartesian axes can be rendered with y spine at the high end of x')
def step_impl(context):
    context.axes.y.spine.position = "high"
    nose.tools.assert_equal(context.axes.y.spine.position, "high")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-spine-position-high")


@then(u'the cartesian axes can be rendered with styled y spine')
def step_impl(context):
    context.axes.y.spine.style = {"stroke": "red"}
    nose.tools.assert_equal(context.axes.y.spine.style["stroke"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-spine-style")


@then(u'the cartesian axes can be rendered with visible y ticks')
def step_impl(context):
    context.axes.y.ticks.show = True
    nose.tools.assert_equal(context.axes.y.ticks.show, True)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-show")


@then(u'the cartesian axes can be rendered with sized y ticks')
def step_impl(context):
    context.axes.y.ticks.show = True
    context.axes.y.ticks.length = 20
    nose.tools.assert_equal(context.axes.y.ticks.length, 20)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-length")


@then(u'the cartesian axes can be rendered with styled y ticks')
def step_impl(context):
    context.axes.y.ticks.show = True
    context.axes.y.ticks.style = {"stroke": "red"}
    nose.tools.assert_equal(context.axes.y.ticks.style["stroke"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-style")


@then(
    u'the cartesian axes can be rendered with y ticks controlled by a locator')
def step_impl(context):
    context.axes.y.ticks.show = True
    locator = toyplot.locator.Basic(count=5)
    context.axes.y.ticks.locator = locator
    nose.tools.assert_is(context.axes.y.ticks.locator, locator)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-locator")


@then(
    u'the cartesian axes can be rendered with y axis per-tick styles identified by index')
def step_impl(context):
    context.axes.y.ticks.show = True
    context.axes.y.ticks.tick(index=0).style = {"stroke": "red"}
    nose.tools.assert_equal(
        context.axes.y.ticks.tick(index=0).style["stroke"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-tick-index-style")


@then(
    u'the cartesian axes can be rendered with y axis per-tick styles identified by value')
def step_impl(context):
    context.axes.y.ticks.show = True
    context.axes.y.ticks.tick(value=0).style = {"stroke": "red"}
    nose.tools.assert_equal(
        context.axes.y.ticks.tick(value=0).style["stroke"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-tick-value-style")


@then(u'the cartesian axes can be rendered with hidden y tick labels')
def step_impl(context):
    context.axes.y.ticks.labels.show = False
    nose.tools.assert_equal(context.axes.y.ticks.labels.show, False)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-labels-show")


@then(u'the cartesian axes can be rendered with angled y tick labels')
def step_impl(context):
    context.axes.y.ticks.labels.angle = -45
    nose.tools.assert_equal(context.axes.y.ticks.labels.angle, -45)
    context.axes.y.ticks.show = True
    context.axes.y.ticks.labels.offset = 10
    context.axes.y.ticks.labels.style = {
        "text-anchor": "middle", "baseline-shift": 0}
    nose.tools.assert_equal(
        context.axes.y.ticks.labels.style["text-anchor"], "middle")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-labels-angle")


@then(u'the cartesian axes can be rendered with styled y tick labels')
def step_impl(context):
    context.axes.y.ticks.labels.style = {"fill": "red"}
    nose.tools.assert_equal(context.axes.y.ticks.labels.style["fill"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-labels-style")


@then(
    u'the cartesian axes can be rendered with y axis per-tick-label styles identified by index')
def step_impl(context):
    context.axes.y.ticks.labels.label(index=0).style = {"fill": "red"}
    nose.tools.assert_equal(
        context.axes.y.ticks.labels.label(index=0).style["fill"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-labels-label-index-style")


@then(
    u'the cartesian axes can be rendered with y axis per-tick-label styles identified by value')
def step_impl(context):
    context.axes.y.ticks.labels.label(value=0).style = {"fill": "red"}
    nose.tools.assert_equal(
        context.axes.y.ticks.labels.label(value=0).style["fill"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-ticks-labels-label-value-style")


@then(u'the cartesian axes can be rendered with y axis label')
def step_impl(context):
    context.axes.y.label.text = "Howdy!"
    nose.tools.assert_equal(context.axes.y.label.text, "Howdy!")
    context.axes.y.label.style = {"fill": "red"}
    nose.tools.assert_equal(context.axes.y.label.style["fill"], "red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-label")


@then(u'the cartesian axes can be rendered with explicit y axis domain')
def step_impl(context):
    context.axes.y.domain.min = 0
    nose.tools.assert_equal(context.axes.y.domain.min, 0)
    context.axes.y.domain.max = 1
    nose.tools.assert_equal(context.axes.y.domain.max, 1)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-cartesian-y-domain")


@given(u'a sample toyplot.data.Table')
def step_impl(context):
    numpy.random.seed(1324)
    context.data = toyplot.data.Table()
    context.data["foo"] = numpy.arange(0, 144, 15)
    context.data["bar"] = numpy.random.normal(scale=100, size=10)
    context.data["baz"] = numpy.random.choice(["red", "green", "blue"], 10)
    context.data["blah"] = numpy.repeat("", 10)


@given(u'an instance of toyplot.axes.Table')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    context.axes = context.canvas.table(context.data)


@then(u'the table can be rendered with defaults')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-defaults")


@then(u'the table can be rendered with header styles')
def step_impl(context):
    context.axes.header.column(1).style = {"fill": "red"}
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-header-style")


@then(u'the table can be rendered with column styles')
def step_impl(context):
    context.axes.column(1).style = {"fill": "red"}
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-column-style")


@then(u'the table can be rendered with row styles')
def step_impl(context):
    context.axes.row(1).style = {"fill": "green"}
    toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-row-style")


@then(u'the table can be rendered with cell styles')
def step_impl(context):
    context.axes.cell(1, 1).style = {"fill": "blue"}
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-cell-style")


@then(u'the table can be rendered and row styles override column styles')
def step_impl(context):
    context.axes.column(1).style = {"fill": "red"}
    context.axes.row(1).style = {"fill": "green"}
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-column-row-style")


@then(u'the table can be rendered and cell styles override row styles')
def step_impl(context):
    context.axes.row(1).style = {"fill": "green"}
    context.axes.cell(1, 1).style = {"fill": "blue"}
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-row-cell-style")


@then(u'the table can be rendered and cell styles override column styles')
def step_impl(context):
    context.axes.column(1).style = {"fill": "red"}
    context.axes.cell(1, 1).style = {"fill": "blue"}
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-column-cell-style")


@then(u'the table can be rendered with extra horizontal lines')
def step_impl(context):
    context.axes.grid.hlines[0, ...] = "single"
    toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-hlines")


@then(u'the table can be rendered with extra vertical lines')
def step_impl(context):
    context.axes.grid.vlines[..., 1] = "single"
    toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-vlines")


@then(u'the table can be rendered with a full grid')
def step_impl(context):
    context.axes.grid.hlines[...] = "single"
    context.axes.grid.vlines[...] = "single"
    toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-full-grid")


@then(u'the table can be rendered with grid styles')
def step_impl(context):
    context.axes.grid.style = {"stroke": "lightgray"}
    context.axes.grid.hlines[...] = "single"
    context.axes.grid.vlines[...] = "single"
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-grid-styles")


@then(u'the table can be rendered with doubled lines')
def step_impl(context):
    context.axes.grid.hlines[1, ...] = "double"
    context.axes.grid.vlines[..., 1] = "double"
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-doubled-lines")


@then(u'the table can be rendered with custom doubled line separation')
def step_impl(context):
    context.axes.grid.hlines[1, ...] = "double"
    context.axes.grid.vlines[..., 1] = "double"
    context.axes.grid.separation = 4
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-doubled-line-separation")


@then(u'the table can be rendered with column offsets')
def step_impl(context):
    context.axes.column(0).column_offset = -50
    context.axes.column(2).column_offset = 50
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-column-offsets")


@then(u'the table can be rendered with custom header content')
def step_impl(context):
    context.axes.header.cell(0, 1).data = "My Column"
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-header-content")


@then(u'the table can be rendered with custom cell content')
def step_impl(context):
    context.axes.cell(1, 1).data = "My Cell"
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-cell-content")


@then(u'the table can be rendered with embedded plots')
def step_impl(context):
    numpy.random.seed(1234)
    context.axes.body.cell(0, 3).axes().plot(numpy.sin(numpy.linspace(0, 10)))
    context.axes.body.cell(1, 3).axes().bars(
        numpy.random.uniform(0.1, 1, size=10))
    context.axes.body.cell(2, 3).axes().bars(numpy.random.choice(
        [-1, 1], size=30), fill=numpy.random.choice(["red", "blue"], size=30))
    context.axes.body.cell(3, 3, rowspan=2).axes().fill(
        3 + numpy.cos(numpy.linspace(0, 5)) + numpy.sin(numpy.linspace(0, 20)))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-embedded-plots")


@then(u'the table can be rendered with custom column widths')
def step_impl(context):
    context.axes.column(0).width = 50
    context.axes.column(2).width = 250
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-custom-column-widths")


@then(u'the table can be rendered with left justification')
def step_impl(context):
    context.axes.column(0).align = "left"
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-left-justification")


@then(u'the table can be rendered with center justification')
def step_impl(context):
    context.axes.column(2).align = "center"
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-center-justification")


@then(u'the table can be rendered with right justification')
def step_impl(context):
    context.axes.column(2).align = "right"
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-right-justification")


@then(u'the table can be rendered with a label')
def step_impl(context):
    context.axes.label.text = "Quarterly Report"
    toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-label")


@then(u'the table can be rendered with multiple embedded axes in merged cells')
def step_impl(context):
    numpy.random.seed(1234)
    context.axes.body.column(2).merge().axes().bars(numpy.random.random(20), along="y")
    context.axes.body.column(3).merge().axes().bars(numpy.random.random(20), along="y")
    toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-multiple-axes")


@then(u'an instance of toyplot.axes.Table can be rendered without a header')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    context.axes = context.canvas.table(context.data, hrows=0)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-table-without-header")

@then(u'the table can be rendered using the convenience API')
def step_impl(context):
    canvas, table = toyplot.table(context.data)
    toyplot.testing.assert_canvas_equal(canvas, "axes-table-convenience-api")


@given(u'values from -1000 to -1')
def step_impl(context):
    context.x = numpy.linspace(-1000, -1, 100)


@given(u'log 10 axes on x and y')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    context.axes = context.canvas.axes(xscale="log10", yscale="log10")


@given(u'plotting x, x with markers')
def step_impl(context):
    context.axes.plot(context.x, context.x, marker="o")


@then(u'the result should be a log-log plot from -1000 to -1')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-scale-negative-1000-negative-1")


@given(u'values from -1000 to -0.01')
def step_impl(context):
    context.x = numpy.linspace(-1000, -0.01, 100)


@then(u'the result should be a log-log plot from -1000 to -0.01')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-scale-negative-1000-negative-0.01")


@given(u'values from -1000 to 0')
def step_impl(context):
    context.x = numpy.linspace(-1000, 0, 100)


@then(u'the result should be a log-log plot from -1000 to 0')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-scale-negative-1000-zero")


@given(u'values from 0 to 1000')
def step_impl(context):
    context.x = numpy.linspace(0, 1000, 100)


@then(u'the result should be a log-log plot from 0 to 1000')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-scale-zero-1000")


@given(u'values from 0.01 to 1000')
def step_impl(context):
    context.x = numpy.linspace(0.01, 1000, 100)


@then(u'the result should be a log-log plot from 0.01 to 1000')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-scale-0.01-1000")


@given(u'values from 1 to 1000')
def step_impl(context):
    context.x = numpy.linspace(1, 1000, 100)


@then(u'the result should be a log-log plot from 1 to 1000')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-scale-1-1000")


@given(u'values from -1000 to 0.5')
def step_impl(context):
    context.x = numpy.linspace(-1000, 0.5, 100)


@then(u'the result should be a log-log plot from -1000 to 0.5')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-scale-negative-1000-0.5")


@given(u'values from -0.5 to 1000')
def step_impl(context):
    context.x = numpy.linspace(-0.5, 1000, 100)


@then(u'the result should be a log-log plot from -0.5 to 1000')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-scale-negative-0.5-1000")


@given(u'values from -1000 to 1000')
def step_impl(context):
    context.x = numpy.linspace(-1000, 1000, 100)


@then(u'the result should be a log-log plot from -1000 to 1000')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-scale-negative-1000-1000")


@given(u'log 2 axes on x and y')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    context.axes = context.canvas.axes(xscale="log2", yscale="log2")


@then(u'the result should be a base 2 log-log plot from -1000 to -1')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-2-scale-negative-1000-negative-1")


@then(u'the result should be a base 2 log-log plot from 1 to 1000')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-2-scale-1-1000")


@then(u'the result should be a base 2 log-log plot from -1000 to 1000')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-2-scale-negative-1000-1000")


@given(u'log 10 axes on x and y with custom format')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    context.axes = context.canvas.axes(xscale="log10", yscale="log10")
    context.axes.x.ticks.locator = toyplot.locator.Log(base=10, format="{base}^{exponent}")
    context.axes.y.ticks.locator = toyplot.locator.Log(base=10, format="{base}^{exponent}")


@then(u'the result should be a log-log plot from -1000 to 1000 with custom labels')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-log-10-scale-negative-1000-1000-custom-format")


@given(u'position and boundary data')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(50, 100))
    context.position = numpy.linspace(0, 1)
    context.boundaries = numpy.column_stack(
        (numpy.min(
            observations, axis=1), numpy.mean(
            observations, axis=1), numpy.max(
                observations, axis=1)))


@when(u'creating a fill plot with one boundary')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(context.boundaries.T[1])


@then(
    u'the result should be a fill plot between the boundary and the origin with implicit x')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-one-boundary")


@when(u'creating a fill plot with one boundary and position')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.boundaries.T[1])


@then(u'the result should be a fill plot between the boundary and the origin')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-one-boundary-position")


@when(u'creating a fill plot with two boundaries and position')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.boundaries.T[1], context.boundaries.T[2])


@then(u'the result should be a fill plot between the two boundaries')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-two-boundaries-position")


@when(u'creating a fill plot with multiple boundaries')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(context.boundaries)


@then(
    u'the result should be multiple fill series between the boundaries with implicit x')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-boundaries")


@when(u'creating a fill plot with multiple boundaries and position')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.boundaries)


@then(u'the result should be multiple fill series between the boundaries')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-boundaries-position")


@when(u'creating a fill plot with multiple boundaries and position along y')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.boundaries, along="y")


@then(
    u'the result should be multiple fill series between the boundaries along y')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-boundaries-position-along-y")


@when(u'creating a fill plot with multiple boundaries and per-series titles')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.boundaries, title=["1st half", "2nd half"])


@then(
    u'the result should be multiple fill series between the boundaries with titles')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-boundaries-titles")


@given(u'position and magnitude data')
def step_impl(context):
    numpy.random.seed(1234)
    observations = numpy.random.normal(loc=1, size=(50, 100))
    context.position = numpy.linspace(0, 1)
    context.magnitudes = numpy.column_stack(
        (numpy.mean(observations, axis=1), numpy.std(observations, axis=1)))


@when(u'creating a fill plot with one magnitude')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.magnitudes.T[0], baseline="stacked")


@then(
    u'the result should be one fill series stacked above the origin with implicit x')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-one-magnitude")


@when(u'creating a fill plot with one magnitude and position')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.magnitudes.T[0], baseline="stacked")


@then(u'the result should be one fill series stacked above the origin')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-one-magnitude-position")


@when(u'creating a fill plot with multiple magnitudes')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.magnitudes, baseline="stacked")


@then(
    u'the result should be multiple fill series stacked above the origin with implicit x')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes")


@when(u'creating a fill plot with multiple magnitudes and position')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.magnitudes, baseline="stacked")


@then(u'the result should be multiple fill series stacked above the origin')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes-position")


@when(u'creating a fill plot with multiple magnitudes and position along y')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.magnitudes, baseline="stacked", along="y")


@then(
    u'the result should be multiple fill series stacked above the origin along y')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes-position-along-y")


@when(u'creating a fill plot with multiple magnitudes and per-series titles')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.position, context.magnitudes, baseline="stacked", title=[
            "1st half", "2nd half"])


@then(
    u'the result should be multiple fill series stacked above the origin with titles')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes-position-titles")


@when(u'creating a fill plot with multiple magnitudes and symmetric baseline')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.magnitudes, baseline="symmetric")


@then(
    u'the result should be multiple fill series stacked with symmetric baseline')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes-symmetric-baseline")


@when(u'creating a fill plot with multiple magnitudes and wiggle baseline')
def step_impl(context):
    context.canvas, axes, mark = toyplot.fill(
        context.magnitudes, baseline="wiggle")


@then(
    u'the result should be multiple fill series stacked with wiggle baseline')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-fill-n-magnitudes-wiggle-baseline")


@when(u'adding default line marks to axes')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    axes = context.canvas.axes()
    axes.hlines(numpy.linspace(0, 0.6), style={"stroke":"steelblue", "opacity":0.4})
    axes.vlines(numpy.linspace(0, 1), style={"stroke":"steelblue", "opacity":0.4})
    axes.plot(numpy.linspace(0.25, 0.75), numpy.linspace(0.25, 0.75) ** 2);

@then(u'the line marks should be treated as annotations.')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-lines-annotation")


@when(u'adding data line marks to axes')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    axes = context.canvas.axes()
    axes.hlines(numpy.linspace(0, 0.6), style={"stroke":"steelblue", "opacity":0.4}, annotation=False)
    axes.vlines(numpy.linspace(0, 1), style={"stroke":"steelblue", "opacity":0.4}, annotation=False)
    axes.plot(numpy.linspace(0.25, 0.75), numpy.linspace(0.25, 0.75) ** 2);


@then(u'the line marks should be treated as data.')
def step_impl(context):
    toyplot.testing.assert_canvas_equal(
        context.canvas, "axes-lines-data")

@given(u'a matrix')
def step_impl(context):
    numpy.random.seed(1234)
    context.matrix = numpy.random.normal(size=(10, 10))

@then(u'a default matrix visualization can be created with the convenience API')
def step_impl(context):
    canvas, table = toyplot.matrix(context.matrix)
    toyplot.testing.assert_canvas_equal(
        canvas, "matrix-default")

@then(u'a default matrix visualization can be created with the standard API')
def step_impl(context):
    canvas = toyplot.Canvas()
    table = canvas.matrix(context.matrix)
    toyplot.testing.assert_canvas_equal(
        canvas, "matrix-default")


