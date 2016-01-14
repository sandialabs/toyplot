from behave import *

import nose.tools
import toyplot.html


@given(u'text with default alignment')
def step_impl(context):
    context.axes.text(0, 0, "Text!", style={"font-size": "24px"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with left alignment')
def step_impl(context):
    context.axes.text(
        0, 0, "Text!", style={"font-size": "24px", "text-anchor": "start"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with center alignment')
def step_impl(context):
    context.axes.text(
        0, 0, "Text!", style={"font-size": "24px", "text-anchor": "middle"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with right alignment')
def step_impl(context):
    context.axes.text(
        0, 0, "Text!", style={"font-size": "24px", "text-anchor": "end"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with positive anchor shift')
def step_impl(context):
    context.axes.text(
        0,
        0,
        "Text!",
        style={
            "font-size": "24px",
            "text-anchor": "middle",
            "-toyplot-anchor-shift": "10px"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with negative anchor shift')
def step_impl(context):
    context.axes.text(
        0,
        0,
        "Text!",
        style={
            "font-size": "24px",
            "text-anchor": "middle",
            "-toyplot-anchor-shift": "-10px"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with hanging alignment')
def step_impl(context):
    context.axes.text(
        0,
        0,
        "Text!",
        style={
            "font-size": "24px",
            "alignment-baseline": "hanging"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with central alignment')
def step_impl(context):
    context.axes.text(
        0,
        0,
        "Text!",
        style={
            "font-size": "24px",
            "alignment-baseline": "central"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with middle alignment')
def step_impl(context):
    context.axes.text(
        0,
        0,
        "Text!",
        style={
            "font-size": "24px",
            "alignment-baseline": "middle"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with alphabetic alignment')
def step_impl(context):
    context.axes.text(
        0,
        0,
        "Text!",
        style={
            "font-size": "24px",
            "alignment-baseline": "alphabetic"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with positive baseline shift')
def step_impl(context):
    context.axes.text(
        0, 0, "Text!", style={"font-size": "24px", "baseline-shift": "100%"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with negative baseline shift')
def step_impl(context):
    context.axes.text(
        0, 0, "Text!", style={"font-size": "24px", "baseline-shift": "-100%"})
    context.axes.scatterplot(0, 0, color="black")

@when(u'text is aligned with an unknown text-anchor value, an exception is raised.')
def step_impl(context):
    with nose.tools.assert_raises(ValueError):
        context.axes.text(
            0, 0, "Text!", style={"text-anchor": "foo"})
        toyplot.html.render(context.canvas)

@when(u'text is aligned with an unknown alignment-baseline value, an exception is raised.')
def step_impl(context):
    with nose.tools.assert_raises(ValueError):
        context.axes.text(
            0, 0, "Text!", style={"alignment-baseline": "foo"})
        toyplot.html.render(context.canvas)


@given(u'rich text {markup}')
def step_impl(context, markup):
    context.axes.text(0, 0, markup, color=toyplot.color.near_black, style={"font-size": "32px"})

