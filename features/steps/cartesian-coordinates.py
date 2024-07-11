# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import numpy
import toyplot.data

import test
import testing


@then(u'the cartesian axes can be rendered with defaults')
def step_impl(context):
    pass


@then(u'the cartesian axes can be rendered with hidden axes')
def step_impl(context):
    context.axes.show = False
    test.assert_equal(context.axes.show, False)


@then(u'the cartesian axes can be rendered with axes label')
def step_impl(context):
    context.axes.label.text = "Howdy!"
    test.assert_equal(context.axes.label.text, "Howdy!")
    context.axes.label.style = {"fill": "red"}
    test.assert_equal(context.axes.label.style["fill"], "red")


@then(u'the cartesian axes can be rendered with hidden x axis')
def step_impl(context):
    context.axes.x.show = False
    test.assert_equal(context.axes.x.show, False)


@then(u'the cartesian axes can be rendered with log-10 x scale')
def step_impl(context):
    context.axes.x.scale = "log"
    test.assert_equal(context.axes.x.scale, ("log", 10))


@then(u'the cartesian axes can be rendered with hidden x spine')
def step_impl(context):
    context.axes.x.spine.show = False
    test.assert_equal(context.axes.x.spine.show, False)


@then(
    u'the cartesian axes can be rendered with x spine at an explicit position')
def step_impl(context):
    context.axes.x.spine.position = 0
    test.assert_equal(context.axes.x.spine.position, 0)


@then(u'the cartesian axes can be rendered with x spine at the high end of y')
def step_impl(context):
    context.axes.x.spine.position = "high"
    test.assert_equal(context.axes.x.spine.position, "high")


@then(u'the cartesian axes can be rendered with styled x spine')
def step_impl(context):
    context.axes.x.spine.style = {"stroke": "red"}
    test.assert_equal(context.axes.x.spine.style["stroke"], "red")


@then(u'the cartesian axes can be rendered with visible x ticks')
def step_impl(context):
    context.axes.x.ticks.show = True
    test.assert_equal(context.axes.x.ticks.show, True)


@then(u'the cartesian axes can be rendered with sized x ticks')
def step_impl(context):
    context.axes.x.ticks.show = True
    context.axes.x.ticks.far = 10
    context.axes.x.ticks.near = 3
    test.assert_equal(context.axes.x.ticks.far, 10)
    test.assert_equal(context.axes.x.ticks.near, 3)


@then(u'the cartesian axes can be rendered with styled x ticks')
def step_impl(context):
    context.axes.x.ticks.show = True
    context.axes.x.ticks.style = {"stroke": "red"}
    test.assert_equal(context.axes.x.ticks.style["stroke"], "red")


@then(
    u'the cartesian axes can be rendered with x ticks controlled by a locator')
def step_impl(context):
    context.axes.x.ticks.show = True
    locator = toyplot.locator.Uniform(count=11)
    context.axes.x.ticks.locator = locator
    test.assert_is(context.axes.x.ticks.locator, locator)


@then(
    u'the cartesian axes can be rendered with x axis per-tick styles identified by index')
def step_impl(context):
    context.axes.x.ticks.show = True
    context.axes.x.ticks.tick(index=0).style = {"stroke": "red"}
    test.assert_equal(
        context.axes.x.ticks.tick(index=0).style["stroke"], "red")


@then(
    u'the cartesian axes can be rendered with x axis per-tick styles identified by value')
def step_impl(context):
    context.axes.x.ticks.show = True
    context.axes.x.ticks.tick(value=0).style = {"stroke": "red"}
    test.assert_equal(
        context.axes.x.ticks.tick(value=0).style["stroke"], "red")


@then(u'the cartesian axes can be rendered with hidden x tick labels')
def step_impl(context):
    context.axes.x.ticks.labels.show = False
    test.assert_equal(context.axes.x.ticks.labels.show, False)


@then(u'the cartesian axes can be rendered with angled x tick labels')
def step_impl(context):
    context.axes.x.ticks.labels.angle = 45
    test.assert_equal(context.axes.x.ticks.labels.angle, 45)
    context.axes.x.ticks.show = True


@then(u'the cartesian axes can be rendered with offset x tick labels')
def step_impl(context):
    context.axes.x.ticks.labels.offset = "0.125in"
    test.assert_equal(context.axes.x.ticks.labels.offset, 12)


@then(u'the cartesian axes can be rendered with styled x tick labels')
def step_impl(context):
    context.axes.x.ticks.labels.style = {"fill": "red"}
    test.assert_equal(context.axes.x.ticks.labels.style["fill"], "red")


@then(
    u'the cartesian axes can be rendered with x axis per-tick-label styles identified by index')
def step_impl(context):
    context.axes.x.ticks.labels.label(index=0).style = {"fill": "red"}
    test.assert_equal(
        context.axes.x.ticks.labels.label(index=0).style["fill"], "red")


@then(
    u'the cartesian axes can be rendered with x axis per-tick-label styles identified by value')
def step_impl(context):
    context.axes.x.ticks.labels.label(value=0).style = {"fill": "red"}
    test.assert_equal(
        context.axes.x.ticks.labels.label(value=0).style["fill"], "red")


@then(u'the cartesian axes can be rendered with x axis label')
def step_impl(context):
    context.axes.x.label.text = "Howdy!"
    test.assert_equal(context.axes.x.label.text, "Howdy!")
    context.axes.x.label.style = {"fill": "red"}
    test.assert_equal(context.axes.x.label.style["fill"], "red")


@then(u'the cartesian axes can be rendered with explicit x axis domain')
def step_impl(context):
    context.axes.x.domain.min = 0
    test.assert_equal(context.axes.x.domain.min, 0)
    context.axes.x.domain.max = 1
    test.assert_equal(context.axes.x.domain.max, 1)


@then(u'the cartesian axes can be rendered with hidden y axis')
def step_impl(context):
    context.axes.y.show = False
    test.assert_equal(context.axes.y.show, False)


@then(u'the cartesian axes can be rendered with log-10 y scale')
def step_impl(context):
    context.axes.y.scale = "log"
    test.assert_equal(context.axes.y.scale, ("log", 10))


@then(u'the cartesian axes can be rendered with hidden y spine')
def step_impl(context):
    context.axes.y.spine.show = False
    test.assert_equal(context.axes.y.spine.show, False)


@then(
    u'the cartesian axes can be rendered with y spine at an explicit position')
def step_impl(context):
    context.axes.y.spine.position = 10
    test.assert_equal(context.axes.y.spine.position, 10)


@then(u'the cartesian axes can be rendered with y spine at the high end of x')
def step_impl(context):
    context.axes.y.spine.position = "high"
    test.assert_equal(context.axes.y.spine.position, "high")


@then(u'the cartesian axes can be rendered with styled y spine')
def step_impl(context):
    context.axes.y.spine.style = {"stroke": "red"}
    test.assert_equal(context.axes.y.spine.style["stroke"], "red")


@then(u'the cartesian axes can be rendered with visible y ticks')
def step_impl(context):
    context.axes.y.ticks.show = True
    test.assert_equal(context.axes.y.ticks.show, True)


@then(u'the cartesian axes can be rendered with sized y ticks')
def step_impl(context):
    context.axes.y.ticks.show = True
    context.axes.y.ticks.near = 3
    context.axes.y.ticks.far = 10
    test.assert_equal(context.axes.y.ticks.near, 3)
    test.assert_equal(context.axes.y.ticks.far, 10)


@then(u'the cartesian axes can be rendered with styled y ticks')
def step_impl(context):
    context.axes.y.ticks.show = True
    context.axes.y.ticks.style = {"stroke": "red"}
    test.assert_equal(context.axes.y.ticks.style["stroke"], "red")


@then(
    u'the cartesian axes can be rendered with y ticks controlled by a locator')
def step_impl(context):
    context.axes.y.ticks.show = True
    locator = toyplot.locator.Uniform(count=5)
    context.axes.y.ticks.locator = locator
    test.assert_is(context.axes.y.ticks.locator, locator)


@then(
    u'the cartesian axes can be rendered with y axis per-tick styles identified by index')
def step_impl(context):
    context.axes.y.ticks.show = True
    context.axes.y.ticks.tick(index=0).style = {"stroke": "red"}
    test.assert_equal(
        context.axes.y.ticks.tick(index=0).style["stroke"], "red")


@then(
    u'the cartesian axes can be rendered with y axis per-tick styles identified by value')
def step_impl(context):
    context.axes.y.ticks.show = True
    context.axes.y.ticks.tick(value=0).style = {"stroke": "red"}
    test.assert_equal(
        context.axes.y.ticks.tick(value=0).style["stroke"], "red")


@then(u'the cartesian axes can be rendered with hidden y tick labels')
def step_impl(context):
    context.axes.y.ticks.labels.show = False
    test.assert_equal(context.axes.y.ticks.labels.show, False)


@then(u'the cartesian axes can be rendered with angled y tick labels')
def step_impl(context):
    context.axes.y.ticks.labels.angle = -45
    test.assert_equal(context.axes.y.ticks.labels.angle, -45)
    context.axes.y.ticks.show = True


@then(u'the cartesian axes can be rendered with offset y tick labels')
def step_impl(context):
    context.axes.y.ticks.labels.offset = "16px"
    test.assert_equal(context.axes.y.ticks.labels.offset, 16)


@then(u'the cartesian axes can be rendered with styled y tick labels')
def step_impl(context):
    context.axes.y.ticks.labels.style = {"fill": "red"}
    test.assert_equal(context.axes.y.ticks.labels.style["fill"], "red")


@then(
    u'the cartesian axes can be rendered with y axis per-tick-label styles identified by index')
def step_impl(context):
    context.axes.y.ticks.labels.label(index=0).style = {"fill": "red"}
    test.assert_equal(
        context.axes.y.ticks.labels.label(index=0).style["fill"], "red")


@then(
    u'the cartesian axes can be rendered with y axis per-tick-label styles identified by value')
def step_impl(context):
    context.axes.y.ticks.labels.label(value=0).style = {"fill": "red"}
    test.assert_equal(
        context.axes.y.ticks.labels.label(value=0).style["fill"], "red")


@then(u'the cartesian axes can be rendered with y axis label')
def step_impl(context):
    context.axes.y.label.text = "Howdy!"
    test.assert_equal(context.axes.y.label.text, "Howdy!")
    context.axes.y.label.style = {"fill": "red"}
    test.assert_equal(context.axes.y.label.style["fill"], "red")


@then(u'the cartesian axes can be rendered with explicit y axis domain')
def step_impl(context):
    context.axes.y.domain.min = 0
    test.assert_equal(context.axes.y.domain.min, 0)
    context.axes.y.domain.max = 1
    test.assert_equal(context.axes.y.domain.max, 1)


@given(u'a shared axis')
def step_impl(context):
    context.shared_axes = context.axes.share("x")


@given(u'a sample plot with two nonoverlapping series and shared x axis')
def step_impl(context):
    context.axes.scatterplot(numpy.arange(50, 100), numpy.arange(50, 100), color="crimson")
    context.shared_axes = context.axes.share("x")
    context.shared_axes.scatterplot(numpy.arange(10, 60), numpy.arange(50, 100), color="royalblue")


@when(u'adding default line marks to axes')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.hlines(numpy.linspace(0, 0.6), style={"stroke":"steelblue", "opacity":0.4})
    axes.vlines(numpy.linspace(0, 1), style={"stroke":"steelblue", "opacity":0.4})
    axes.plot(numpy.linspace(0.25, 0.75), numpy.linspace(0.25, 0.75) ** 2);

@then(u'the line marks should be treated as annotations.')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-lines-annotation")


@when(u'adding data line marks to axes')
def step_impl(context):
    context.canvas = toyplot.Canvas()
    axes = context.canvas.cartesian()
    axes.hlines(numpy.linspace(0, 0.6), style={"stroke":"steelblue", "opacity":0.4}, annotation=False)
    axes.vlines(numpy.linspace(0, 1), style={"stroke":"steelblue", "opacity":0.4}, annotation=False)
    axes.plot(numpy.linspace(0.25, 0.75), numpy.linspace(0.25, 0.75) ** 2);


@then(u'the line marks should be treated as data.')
def step_impl(context):
    testing.assert_canvas_equal(
        context.canvas, "axes-lines-data")


@given(u'axes-palette')
def step_impl(context):
    for i in range(10):
        context.axes.plot(numpy.arange(2), numpy.repeat(i, 2))


@given(u'axes-palettes')
def step_impl(context):
    context.axes.fill(numpy.sin(numpy.linspace(0, 2 * numpy.pi, 100)), style={"fill-opacity": 0.5})
    context.axes.plot(numpy.sin(numpy.linspace(0, 2 * numpy.pi, 100)), marker="o")
    context.axes.fill(numpy.cos(numpy.linspace(0, 2 * numpy.pi, 100)), style={"fill-opacity": 0.5})
    context.axes.plot(numpy.cos(numpy.linspace(0, 2 * numpy.pi, 100)), marker="o")
    context.axes.fill((numpy.linspace(0, 1, 100)), style={"fill-opacity": 0.5})
    context.axes.plot((numpy.linspace(0, 1, 100)), marker="o")


@given(u'axes-tick-titles')
def step_impl(context):
    context.axes.x.ticks.locator = toyplot.locator.Explicit(locations=[-0.5, 0, 0.5], titles=["Foo", "Bar", "Baz"])
    context.axes.y.ticks.locator = toyplot.locator.Explicit(locations=[-0.5, 0, 0.5], titles=["Red", "Green", "Blue"])


