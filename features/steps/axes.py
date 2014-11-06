from behave import *

import numpy
import toyplot.data
import toyplot.testing

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
 
