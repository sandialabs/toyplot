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
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-defaults")

@then(u'the cartesian axes can be rendered with hidden axes')
def step_impl(context):
  context.axes.show=False
  nose.tools.assert_equal(context.axes.show, False)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-show")

@then(u'the cartesian axes can be rendered with axes label')
def step_impl(context):
  context.axes.label.text="Howdy!"
  nose.tools.assert_equal(context.axes.label.text, "Howdy!")
  context.axes.label.style={"fill":"red"}
  nose.tools.assert_equal(context.axes.label.style["fill"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-label")

@then(u'the cartesian axes can be rendered with hidden x axis')
def step_impl(context):
  context.axes.x.show=False
  nose.tools.assert_equal(context.axes.x.show, False)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-show")

@then(u'the cartesian axes can be rendered with log-10 x scale')
def step_impl(context):
  context.axes.x.scale="log"
  nose.tools.assert_equal(context.axes.x.scale, ("log", 10))
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-scale")

@then(u'the cartesian axes can be rendered with hidden x spine')
def step_impl(context):
  context.axes.x.spine.show=False
  nose.tools.assert_equal(context.axes.x.spine.show, False)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-spine-show")

@then(u'the cartesian axes can be rendered with x spine at an explicit position')
def step_impl(context):
  context.axes.x.spine.position=0
  nose.tools.assert_equal(context.axes.x.spine.position, 0)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-spine-position")

@then(u'the cartesian axes can be rendered with x spine at the high end of y')
def step_impl(context):
  context.axes.x.spine.position="high"
  nose.tools.assert_equal(context.axes.x.spine.position, "high")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-spine-position-high")

@then(u'the cartesian axes can be rendered with styled x spine')
def step_impl(context):
  context.axes.x.spine.style={"stroke":"red"}
  nose.tools.assert_equal(context.axes.x.spine.style["stroke"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-spine-style")

@then(u'the cartesian axes can be rendered with visible x ticks')
def step_impl(context):
  context.axes.x.ticks.show=True
  nose.tools.assert_equal(context.axes.x.ticks.show, True)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-show")


@then(u'the cartesian axes can be rendered with sized x ticks')
def step_impl(context):
  context.axes.x.ticks.show=True
  context.axes.x.ticks.length=20
  nose.tools.assert_equal(context.axes.x.ticks.length, 20)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-length")

@then(u'the cartesian axes can be rendered with styled x ticks')
def step_impl(context):
  context.axes.x.ticks.show=True
  context.axes.x.ticks.style={"stroke":"red"}
  nose.tools.assert_equal(context.axes.x.ticks.style["stroke"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-style")

@then(u'the cartesian axes can be rendered with x ticks controlled by a locator')
def step_impl(context):
  context.axes.x.ticks.show=True
  locator=toyplot.locator.Basic(count=11)
  context.axes.x.ticks.locator=locator
  nose.tools.assert_is(context.axes.x.ticks.locator, locator)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-locator")

@then(u'the cartesian axes can be rendered with x axis per-tick styles identified by index')
def step_impl(context):
  context.axes.x.ticks.show=True
  context.axes.x.ticks.tick(index=0).style={"stroke":"red"}
  nose.tools.assert_equal(context.axes.x.ticks.tick(index=0).style["stroke"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-tick-index-style")

@then(u'the cartesian axes can be rendered with x axis per-tick styles identified by value')
def step_impl(context):
  context.axes.x.ticks.show=True
  context.axes.x.ticks.tick(value=0).style={"stroke":"red"}
  nose.tools.assert_equal(context.axes.x.ticks.tick(value=0).style["stroke"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-tick-value-style")

@then(u'the cartesian axes can be rendered with hidden x tick labels')
def step_impl(context):
  context.axes.x.ticks.labels.show=False
  nose.tools.assert_equal(context.axes.x.ticks.labels.show, False)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-labels-show")

@then(u'the cartesian axes can be rendered with angled x tick labels')
def step_impl(context):
  context.axes.x.ticks.labels.angle=-45
  nose.tools.assert_equal(context.axes.x.ticks.labels.angle, -45)
  context.axes.x.ticks.labels.style={"text-anchor":"end"}
  nose.tools.assert_equal(context.axes.x.ticks.labels.style["text-anchor"], "end")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-labels-angle")

@then(u'the cartesian axes can be rendered with styled x tick labels')
def step_impl(context):
  context.axes.x.ticks.labels.style={"fill":"red"}
  nose.tools.assert_equal(context.axes.x.ticks.labels.style["fill"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-labels-style")

@then(u'the cartesian axes can be rendered with x axis per-tick-label styles identified by index')
def step_impl(context):
  context.axes.x.ticks.labels.label(index=0).style={"fill":"red"}
  nose.tools.assert_equal(context.axes.x.ticks.labels.label(index=0).style["fill"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-labels-label-index-style")

@then(u'the cartesian axes can be rendered with x axis per-tick-label styles identified by value')
def step_impl(context):
  context.axes.x.ticks.labels.label(value=0).style={"fill":"red"}
  nose.tools.assert_equal(context.axes.x.ticks.labels.label(value=0).style["fill"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-ticks-labels-label-value-style")

@then(u'the cartesian axes can be rendered with x axis label')
def step_impl(context):
  context.axes.x.label.text="Howdy!"
  nose.tools.assert_equal(context.axes.x.label.text, "Howdy!")
  context.axes.x.label.style={"fill":"red"}
  nose.tools.assert_equal(context.axes.x.label.style["fill"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-label")

@then(u'the cartesian axes can be rendered with explicit x axis domain')
def step_impl(context):
  context.axes.x.domain.min=0
  nose.tools.assert_equal(context.axes.x.domain.min, 0)
  context.axes.x.domain.max=1
  nose.tools.assert_equal(context.axes.x.domain.max, 1)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-x-domain")












@then(u'the cartesian axes can be rendered with hidden y axis')
def step_impl(context):
  context.axes.y.show=False
  nose.tools.assert_equal(context.axes.y.show, False)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-show")

@then(u'the cartesian axes can be rendered with log-10 y scale')
def step_impl(context):
  context.axes.y.scale="log"
  nose.tools.assert_equal(context.axes.y.scale, ("log", 10))
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-scale")

@then(u'the cartesian axes can be rendered with hidden y spine')
def step_impl(context):
  context.axes.y.spine.show=False
  nose.tools.assert_equal(context.axes.y.spine.show, False)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-spine-show")

@then(u'the cartesian axes can be rendered with y spine at an explicit position')
def step_impl(context):
  context.axes.y.spine.position=10
  nose.tools.assert_equal(context.axes.y.spine.position, 10)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-spine-position")

@then(u'the cartesian axes can be rendered with y spine at the high end of x')
def step_impl(context):
  context.axes.y.spine.position="high"
  nose.tools.assert_equal(context.axes.y.spine.position, "high")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-spine-position-high")

@then(u'the cartesian axes can be rendered with styled y spine')
def step_impl(context):
  context.axes.y.spine.style={"stroke":"red"}
  nose.tools.assert_equal(context.axes.y.spine.style["stroke"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-spine-style")

@then(u'the cartesian axes can be rendered with visible y ticks')
def step_impl(context):
  context.axes.y.ticks.show=True
  nose.tools.assert_equal(context.axes.y.ticks.show, True)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-show")


@then(u'the cartesian axes can be rendered with sized y ticks')
def step_impl(context):
  context.axes.y.ticks.show=True
  context.axes.y.ticks.length=20
  nose.tools.assert_equal(context.axes.y.ticks.length, 20)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-length")

@then(u'the cartesian axes can be rendered with styled y ticks')
def step_impl(context):
  context.axes.y.ticks.show=True
  context.axes.y.ticks.style={"stroke":"red"}
  nose.tools.assert_equal(context.axes.y.ticks.style["stroke"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-style")

@then(u'the cartesian axes can be rendered with y ticks controlled by a locator')
def step_impl(context):
  context.axes.y.ticks.show=True
  locator=toyplot.locator.Basic(count=5)
  context.axes.y.ticks.locator=locator
  nose.tools.assert_is(context.axes.y.ticks.locator, locator)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-locator")

@then(u'the cartesian axes can be rendered with y axis per-tick styles identified by index')
def step_impl(context):
  context.axes.y.ticks.show=True
  context.axes.y.ticks.tick(index=0).style={"stroke":"red"}
  nose.tools.assert_equal(context.axes.y.ticks.tick(index=0).style["stroke"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-tick-index-style")

@then(u'the cartesian axes can be rendered with y axis per-tick styles identified by value')
def step_impl(context):
  context.axes.y.ticks.show=True
  context.axes.y.ticks.tick(value=0).style={"stroke":"red"}
  nose.tools.assert_equal(context.axes.y.ticks.tick(value=0).style["stroke"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-tick-value-style")

@then(u'the cartesian axes can be rendered with hidden y tick labels')
def step_impl(context):
  context.axes.y.ticks.labels.show=False
  nose.tools.assert_equal(context.axes.y.ticks.labels.show, False)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-labels-show")

@then(u'the cartesian axes can be rendered with angled y tick labels')
def step_impl(context):
  context.axes.y.ticks.labels.angle=-45
  nose.tools.assert_equal(context.axes.y.ticks.labels.angle, -45)
  context.axes.y.ticks.labels.style={"text-anchor":"end"}
  nose.tools.assert_equal(context.axes.y.ticks.labels.style["text-anchor"], "end")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-labels-angle")

@then(u'the cartesian axes can be rendered with styled y tick labels')
def step_impl(context):
  context.axes.y.ticks.labels.style={"fill":"red"}
  nose.tools.assert_equal(context.axes.y.ticks.labels.style["fill"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-labels-style")

@then(u'the cartesian axes can be rendered with y axis per-tick-label styles identified by index')
def step_impl(context):
  context.axes.y.ticks.labels.label(index=0).style={"fill":"red"}
  nose.tools.assert_equal(context.axes.y.ticks.labels.label(index=0).style["fill"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-labels-label-index-style")

@then(u'the cartesian axes can be rendered with y axis per-tick-label styles identified by value')
def step_impl(context):
  context.axes.y.ticks.labels.label(value=0).style={"fill":"red"}
  nose.tools.assert_equal(context.axes.y.ticks.labels.label(value=0).style["fill"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-ticks-labels-label-value-style")

@then(u'the cartesian axes can be rendered with y axis label')
def step_impl(context):
  context.axes.y.label.text="Howdy!"
  nose.tools.assert_equal(context.axes.y.label.text, "Howdy!")
  context.axes.y.label.style={"fill":"red"}
  nose.tools.assert_equal(context.axes.y.label.style["fill"], "red")
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-label")

@then(u'the cartesian axes can be rendered with explicit y axis domain')
def step_impl(context):
  context.axes.y.domain.min=0
  nose.tools.assert_equal(context.axes.y.domain.min, 0)
  context.axes.y.domain.max=1
  nose.tools.assert_equal(context.axes.y.domain.max, 1)
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-cartesian-y-domain")













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
  context.axes.column(1).header.style = {"fill":"red"}
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-header-style")

@then(u'the table can be rendered with column styles')
def step_impl(context):
  context.axes.column(1).style = {"fill":"red"}
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-column-style")

@then(u'the table can be rendered with row styles')
def step_impl(context):
  context.axes.row(1).style = {"fill":"green"}
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-row-style")

@then(u'the table can be rendered with cell styles')
def step_impl(context):
  context.axes.cell(1, 1).style = {"fill":"blue"}
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-cell-style")

@then(u'the table can be rendered and row styles override column styles')
def step_impl(context):
  context.axes.column(1).style = {"fill":"red"}
  context.axes.row(1).style = {"fill":"green"}
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-column-row-style")

@then(u'the table can be rendered and cell styles override row styles')
def step_impl(context):
  context.axes.row(1).style = {"fill":"green"}
  context.axes.cell(1, 1).style = {"fill":"blue"}
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-row-cell-style")

@then(u'the table can be rendered and cell styles override column styles')
def step_impl(context):
  context.axes.column(1).style = {"fill":"red"}
  context.axes.cell(1, 1).style = {"fill":"blue"}
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-column-cell-style")

@then(u'the table can be rendered with extra horizontal lines')
def step_impl(context):
  context.axes.grid.hlines[0,...] = "single"
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-hlines")

@then(u'the table can be rendered with extra vertical lines')
def step_impl(context):
  context.axes.grid.vlines[...,1] = "single"
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-vlines")

@then(u'the table can be rendered with a full grid')
def step_impl(context):
  context.axes.grid.hlines[...] = "single"
  context.axes.grid.vlines[...] = "single"
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-full-grid")

@then(u'the table can be rendered with grid styles')
def step_impl(context):
  context.axes.grid.style = {"stroke":"lightgray"}
  context.axes.grid.hlines[...] = "single"
  context.axes.grid.vlines[...] = "single"
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-grid-styles")

@then(u'the table can be rendered with doubled lines')
def step_impl(context):
  context.axes.grid.hlines[1,...] = "double"
  context.axes.grid.vlines[...,1] = "double"
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-doubled-lines")

@then(u'the table can be rendered with custom doubled line separation')
def step_impl(context):
  context.axes.grid.hlines[1,...] = "double"
  context.axes.grid.vlines[...,1] = "double"
  context.axes.grid.separation = 4
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-doubled-line-separation")

@then(u'the table can be rendered with column offsets')
def step_impl(context):
  context.axes.column("foo").offset = -50
  context.axes.column("baz").offset = 50
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-column-offsets")

@then(u'the table can be rendered with custom header content')
def step_impl(context):
  context.axes.column(1).header.content = "My Column"
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-header-content")

@then(u'the table can be rendered with custom cell content')
def step_impl(context):
  context.axes.cell(1, 1).content = "My Cell"
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-cell-content")
 
@then(u'the table can be rendered with embedded plots')
def step_impl(context):
  numpy.random.seed(1234)
  context.axes.cell(0, 3).axes().plot(numpy.sin(numpy.linspace(0, 10)))
  context.axes.cell(1, 3).axes().bars(numpy.random.uniform(0.1, 1, size=10))
  context.axes.cell(2, 3).axes().bars(numpy.random.choice([-1, 1], size=30), fill=numpy.random.choice(["red", "blue"], size=30))
  context.axes.cell(3, 3, rowspan=2).axes().fill(3 + numpy.cos(numpy.linspace(0, 5)) + numpy.sin(numpy.linspace(0, 20)))
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-embedded-plots")
 
@then(u'the table can be rendered with custom column widths')
def step_impl(context):
  context.axes.column("foo").width = 50
  context.axes.column("baz").width = 250
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-custom-column-widths")
 
@then(u'the table can be rendered with left justification')
def step_impl(context):
  context.axes.column("foo").justify = "left"
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-left-justification")
 
@then(u'the table can be rendered with center justification')
def step_impl(context):
  context.axes.column("baz").justify = "center"
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-center-justification")
 
@then(u'the table can be rendered with right justification')
def step_impl(context):
  context.axes.column("baz").justify = "right"
  toyplot.testing.assert_canvas_equal(context.canvas, "axes-table-right-justification")
 
