from behave import *

import numpy
import toyplot.generate
import toyplot.layout
import toyplot.testing

@given(u'a prufer tree.')
def step_impl(context):
    numpy.random.seed(1234)
    context.graph = toyplot.generate.prufer_tree(numpy.random.choice(4, 12))

@given(u'a ba graph.')
def step_impl(context):
    context.graph = toyplot.generate.barabasi_albert_graph(n=20)

@given(u'a default layout.')
def step_impl(context):
    context.layout = None

@given(u'a random layout.')
def step_impl(context):
    context.layout = toyplot.layout.Random()

@given(u'a eades layout.')
def step_impl(context):
    context.layout = toyplot.layout.Eades()

@given(u'a fruchterman-reingold layout.')
def step_impl(context):
    context.layout = toyplot.layout.FruchtermanReingold()

@given(u'a buchheim layout.')
def step_impl(context):
    context.layout = toyplot.layout.Buchheim()

@given(u'a graphviz layout.')
def step_impl(context):
    context.layout = toyplot.layout.GraphViz()

@then(u'the rendered graph should match the {reference} reference.')
def step_impl(context, reference):
    canvas, axes, mark = toyplot.graph(context.graph, layout=context.layout)
    toyplot.testing.assert_canvas_equal(canvas, reference)

