from behave import *

import toyplot.testing

@then(u'text can be aligned with default alignment')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-anchor-default")

@then(u'text can be aligned with left alignment')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "text-anchor":"start"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-anchor-start")

@then(u'text can be aligned with center alignment')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "text-anchor":"middle"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-anchor-middle")

@then(u'text can be aligned with right alignment')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "text-anchor":"end"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-anchor-end")

@then(u'text can be aligned with positive anchor shift')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "text-anchor":"middle", "-toyplot-anchor-shift":"10px"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-anchor-shift-positive")

@then(u'text can be aligned with negative anchor shift')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "text-anchor":"middle", "-toyplot-anchor-shift":"-10px"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-anchor-shift-negative")

@then(u'text can be aligned with hanging alignment')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "alignment-baseline":"hanging"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-alignment-baseline-hanging")

@then(u'text can be aligned with central alignment')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "alignment-baseline":"central"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-alignment-baseline-central")

@then(u'text can be aligned with middle alignment')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "alignment-baseline":"middle"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-alignment-baseline-middle")

@then(u'text can be aligned with alphabetic alignment')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "alignment-baseline":"alpha"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-alignment-baseline-alpha")

@then(u'text can be aligned with positive baseline shift')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "baseline-shift":"100%"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-baseline-shift-positive")

@then(u'text can be aligned with negative baseline shift')
def step_impl(context):
  context.axes.text(0, 0, "Text!", style={"font-size":"24px", "baseline-shift":"-100%"})
  context.axes.scatterplot(0, 0, color="black", size=7);
  toyplot.testing.assert_canvas_equal(context.canvas, "text-baseline-shift-negative")


