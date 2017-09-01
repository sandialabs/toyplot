# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import nose
import numpy
import toyplot.data


@given(u'a sample toyplot.data.Table')
def step_impl(context):
    numpy.random.seed(1324)
    context.data = toyplot.data.Table()
    context.data["foo"] = numpy.arange(0, 144, 15)
    context.data["bar"] = numpy.random.normal(scale=100, size=10)
    context.data["baz"] = numpy.random.choice(["red", "green", "blue"], 10)
    context.data["blah"] = numpy.repeat("", 10)


@given(u'an instance of toyplot.coordinates.Table')
def step_impl(context):
    context.table_axes = context.canvas.table(context.data)


@then(u'the table can be rendered with defaults')
def step_impl(context):
    pass


@then(u'the table can be rendered with header styles')
def step_impl(context):
    context.table_axes.top.column[1].lstyle = {"fill": "red"}


@then(u'the table can be rendered with column styles')
def step_impl(context):
    context.table_axes.cells.column[1].lstyle = {"fill": "red"}


@then(u'the table can be rendered with row styles')
def step_impl(context):
    context.table_axes.cells.row[1].lstyle = {"fill": "green"}


@then(u'the table can be rendered with cell styles')
def step_impl(context):
    context.table_axes.cells.cell[1, 1].lstyle = {"fill": "blue"}


@then(u'the table can be rendered and row styles override column styles')
def step_impl(context):
    context.table_axes.cells.column[1].lstyle = {"fill": "red"}
    context.table_axes.cells.row[1].lstyle = {"fill": "green"}


@then(u'the table can be rendered and cell styles override row styles')
def step_impl(context):
    context.table_axes.cells.row[1].lstyle = {"fill": "green"}
    context.table_axes.cells.cell[1, 1].lstyle = {"fill": "blue"}


@then(u'the table can be rendered and cell styles override column styles')
def step_impl(context):
    context.table_axes.cells.column[1].lstyle = {"fill": "red"}
    context.table_axes.cells.cell[1, 1].lstyle = {"fill": "blue"}


@then(u'the table can be rendered with extra horizontal lines')
def step_impl(context):
    context.table_axes.cells.grid.hlines[0, ...] = "single"


@then(u'the table can be rendered with extra vertical lines')
def step_impl(context):
    context.table_axes.cells.grid.vlines[..., 1] = "single"


@then(u'the table can be rendered with a full grid')
def step_impl(context):
    context.table_axes.cells.grid.hlines[...] = "single"
    context.table_axes.cells.grid.vlines[...] = "single"


@then(u'the table can be rendered with grid styles')
def step_impl(context):
    context.table_axes.cells.grid.style = {"stroke": "lightgray"}
    context.table_axes.cells.grid.hlines[...] = "single"
    context.table_axes.cells.grid.vlines[...] = "single"


@then(u'the table can be rendered with doubled lines')
def step_impl(context):
    context.table_axes.cells.grid.hlines[1, ...] = "double"
    context.table_axes.cells.grid.vlines[..., 1] = "double"


@then(u'the table can be rendered with custom doubled line separation')
def step_impl(context):
    context.table_axes.cells.grid.hlines[1, ...] = "double"
    context.table_axes.cells.grid.vlines[..., 1] = "double"
    context.table_axes.cells.grid.separation = 4


@then(u'the table can be rendered with column offsets')
def step_impl(context):
    context.table_axes.cells.column[0].lstyle = {"-toyplot-anchor-shift": -50}
    context.table_axes.cells.column[2].lstyle = {"-toyplot-anchor-shift": 50}


@then(u'the table can be rendered with custom header content')
def step_impl(context):
    context.table_axes.top.cell[0, 1].data = "My Column"


@then(u'the table can be rendered with custom cell content')
def step_impl(context):
    context.table_axes.cells.cell[1, 1].data = "My Cell"


@then(u'the table can be rendered with embedded plots')
def step_impl(context):
    numpy.random.seed(1234)
    context.table_axes.body.cell[0, 3].cartesian().plot(numpy.sin(numpy.linspace(0, 10)))
    context.table_axes.body.cell[1, 3].cartesian().bars(
        numpy.random.uniform(0.1, 1, size=10))
    context.table_axes.body.cell[2, 3].cartesian().bars(numpy.random.choice(
        [-1, 1], size=30), color=numpy.random.choice(["red", "blue"], size=30))
    context.table_axes.body.cell[3:5, 3].cartesian().fill(
        3 + numpy.cos(numpy.linspace(0, 5)) + numpy.sin(numpy.linspace(0, 20)))


@then(u'the table can be rendered with custom column widths')
def step_impl(context):
    context.table_axes.cells.column[0].width = 50
    context.table_axes.cells.column[2].width = 250


@then(u'the table can be rendered with left justification')
def step_impl(context):
    context.table_axes.cells.column[0].align = "left"


@then(u'the table can be rendered with center justification')
def step_impl(context):
    context.table_axes.cells.column[2].align = "center"


@then(u'the table can be rendered with right justification')
def step_impl(context):
    context.table_axes.cells.column[2].align = "right"


@then(u'the table can be rendered with a label')
def step_impl(context):
    context.table_axes.label.text = "Quarterly Report"


@then(u'the table can be rendered with multiple embedded axes in merged cells')
def step_impl(context):
    numpy.random.seed(1234)
    context.table_axes.body.column[2].merge().cartesian().bars(numpy.random.random(20), along="y")
    context.table_axes.body.column[3].merge().cartesian().bars(numpy.random.random(20), along="y")


@then(u'the table can be rendered with real world units')
def step_impl(context):
    context.table_axes.cells.grid.hlines[...] = "single"
    context.table_axes.cells.grid.vlines[...] = "single"
    context.table_axes.cells.column[0].width = (1, "cm")
    context.table_axes.cells.row[0].height = "1cm"

@then(u'an instance of toyplot.coordinates.Table can be rendered without a header')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    context.table_axes = context.canvas.table(context.data, trows=0)

@then(u'the table can be rendered using the convenience API')
def step_impl(context):
    context.canvas, context.table_axes = toyplot.table(context.data)


@given(u'a sample toyplot.data.Table containing null values')
def step_impl(context):
    numpy.random.seed(1234)
    context.data = toyplot.data.Table(numpy.random.random((4, 4)))
    for key, column in context.data.items():
        context.data[key] = numpy.ma.masked_where(column < 0.5, column)

@given(u'an instance of toyplot.coordinates.Table with 4 rows and 3 columns')
def step_impl(context):
    context.table_axes = context.canvas.table(rows=4, columns=3)
    context.table_axes.cells.grid.hlines[...] = "single"
    context.table_axes.cells.grid.vlines[...] = "single"

@given(u'an instance of toyplot.coordinates.Table with every region enabled')
def step_impl(context):
    context.table_axes = context.canvas.table(trows=3, rows=3, brows=3, lcolumns=3, columns=3, rcolumns=3)
    context.table_axes.cells.cells.data = numpy.arange(81).reshape(9, 9)

@given(u'every grid line is enabled')
def step_impl(context):
    context.table_axes.cells.grid.hlines[...] = "single"
    context.table_axes.cells.grid.vlines[...] = "single"

@given(u'the first row is deleted')
def step_impl(context):
    context.table_axes.cells.row[0].delete()

@given(u'every region is colored')
def step_impl(context):
    context.table_axes.top.left.cells.style = {"fill":"red", "opacity":0.2}
    context.table_axes.top.cells.style = {"fill":"orange", "opacity":0.2}
    context.table_axes.top.right.cells.style = {"fill":"yellow", "opacity":0.2}
    context.table_axes.right.cells.style = {"fill":"greenyellow", "opacity":0.2}
    context.table_axes.bottom.right.cells.style = {"fill":"green", "opacity":0.2}
    context.table_axes.bottom.cells.style = {"fill":"aqua", "opacity":0.2}
    context.table_axes.bottom.left.cells.style = {"fill":"blue", "opacity":0.2}
    context.table_axes.left.cells.style = {"fill":"purple", "opacity":0.2}


@given(u'a middle row is deleted')
def step_impl(context):
    context.table_axes.cells.row[4].delete()

@given(u'the last row is deleted')
def step_impl(context):
    context.table_axes.cells.row[-1].delete()

@given(u'the first column is deleted')
def step_impl(context):
    context.table_axes.cells.column[0].delete()

@given(u'a middle column is deleted')
def step_impl(context):
    context.table_axes.cells.column[4].delete()

@given(u'the last column is deleted')
def step_impl(context):
    context.table_axes.cells.column[-1].delete()

@given(u'a {region} {celltype} is inserted {position} {selection}')
def step_impl(context, region, celltype, position, selection):
    if region == "top":
        region = context.table_axes.top
    elif region == "body":
        region = context.table_axes.body
    elif region == "bottom":
        region = context.table_axes.bottom
    elif region == "left":
        region = context.table_axes.left
    elif region == "right":
        region = context.table_axes.right
    else:
        raise ValueError("Unknown region: %s" % region)

    if celltype == "row":
        accessor = region.row
    elif celltype == "column":
        accessor = region.column
    else:
        raise ValueError("Unknown cell type: %s" % celltype)

    if position == "before":
        accessor.insert(before=int(selection))
    elif position == "after":
        accessor.insert(after=int(selection))
    else:
        raise ValueError("Unknown position: %s" % position)

@given(u'{region} {selection} is merged')
def step_impl(context, region, selection):
    if region == "top":
        region = context.table_axes.top
    elif region == "top-left":
        region = context.table_axes.top.left
    elif region == "body":
        region = context.table_axes.body
    elif region == "bottom":
        region = context.table_axes.bottom
    elif region == "left":
        region = context.table_axes.left
    elif region == "right":
        region = context.table_axes.right
    elif region == "cells":
        region = context.table_axes.cells
    else:
        raise ValueError("Unknown region: %s" % region)

    row_begin, row_end, column_begin, column_end = eval(selection)

    region.cell[row_begin:row_end,column_begin:column_end].merge()

