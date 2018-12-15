# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

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


@given(u'text with angled anchor shift')
def step_impl(context):
    context.axes.text(
        0,
        0,
        "+++",
        angle=30,
        style={
            "font-size": "32px",
            "-toyplot-anchor-shift": "10px"})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with vertical alignment top')
def step_impl(context):
    text = """First line<br/>Second line<br/>Third line"""
    context.axes.text(
        0,
        0,
        text,
        style={
            "font-size": "24px",
            "-toyplot-vertical-align": "top",
		})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with vertical alignment first baseline')
def step_impl(context):
    text = """First line<br/>Second line<br/>Third line"""
    context.axes.text(
        0,
        0,
        text,
        style={
            "font-size": "24px",
            "-toyplot-vertical-align": "first-baseline",
		})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with vertical alignment middle')
def step_impl(context):
    text = """First line<br/>Second line<br/>Third line"""
    context.axes.text(
        0,
        0,
        text,
        style={
            "font-size": "24px",
            "-toyplot-vertical-align": "middle",
		})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with vertical alignment last baseline')
def step_impl(context):
    text = """First line<br/>Second line<br/>Third line"""
    context.axes.text(
        0,
        0,
        text,
        style={
            "font-size": "24px",
            "-toyplot-vertical-align": "last-baseline",
		})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with vertical alignment bottom')
def step_impl(context):
    text = """First line<br/>Second line<br/>Third line"""
    context.axes.text(
        0,
        0,
        text,
        style={
            "font-size": "24px",
            "-toyplot-vertical-align": "bottom",
		})
    context.axes.scatterplot(0, 0, color="black")


@given(u'text with alignment baselines')
def step_impl(context):
    text = """<span style="alignment-baseline:alphabetic">Alphabetic</span>
<span style="alignment-baseline:middle">Middle</span>
<span style="alignment-baseline:central">Central</span>
<span style="alignment-baseline:hanging">Hanging</span>"""

    context.axes.text(
        0,
        0,
        text,
        style={
            "font-size": "24px",
		})
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


@given(u'text with angled baseline shift')
def step_impl(context):
    context.axes.text(
        0, 0, "+++", angle=30, style={"font-size": "32px", "baseline-shift": "10px"})
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
    context.axes.text(0, 0, markup, color=toyplot.color.black, style={"font-size": "32px"})


@given(u'text using font-family {family}')
def step_impl(context, family):
    context.axes.text(0, 0, "Font-family: %s" % family, style={"font-family": family, "font-size": "32px"})


@when(u'text is drawn with an unknown font family, an exception is raised.')
def step_impl(context):
    with nose.tools.assert_raises(ValueError):
        context.axes.text(0, 0, "Font-family: nonexistent", style={"font-family": "nonexistent", "font-size": "32px"})
        context.canvas._repr_html_()


