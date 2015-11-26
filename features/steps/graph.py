from behave import *

import numpy
import toyplot.generate
import toyplot.layout
import toyplot.testing

@given(u'a prufer tree')
def step_impl(context):
    numpy.random.seed(1234)
    context.graph = toyplot.generate.prufer_tree(numpy.random.choice(4, 12))

@given(u'a ba graph')
def step_impl(context):
    context.graph = toyplot.generate.barabasi_albert_graph(n=20)

@given(u'a default graph layout')
def step_impl(context):
    context.layout = None

@given(u'a random graph layout')
def step_impl(context):
    context.layout = toyplot.layout.Random()

@given(u'a eades graph layout')
def step_impl(context):
    context.layout = toyplot.layout.Eades()

@given(u'a fruchterman-reingold graph layout')
def step_impl(context):
    context.layout = toyplot.layout.FruchtermanReingold()

@given(u'a buchheim graph layout')
def step_impl(context):
    context.layout = toyplot.layout.Buchheim()

@given(u'a graphviz graph layout')
def step_impl(context):
    context.layout = toyplot.layout.GraphViz()

@given(u'a fruchterman-reingold-curved-edge graph layout')
def step_impl(context):
    context.layout = toyplot.layout.FruchtermanReingold(edges=toyplot.layout.CurvedEdges())

@when(u'the graph and layout are combined')
def step_impl(context):
    context.canvas, axes, mark = toyplot.graph(context.graph, layout=context.layout)

@when(u'a graph visualization is constructed from explicit source and target edge arrays')
def step_impl(context):
    numpy.random.seed(1234)
    sources = numpy.random.choice(8, 10)
    targets = numpy.random.choice(8, 10)
    context.canvas, axes, mark = toyplot.graph(sources, targets)

@given(u'explicit source and target arrays')
def step_impl(context):
    numpy.random.seed(1234)
    context.sources = numpy.random.choice(8, 10)
    context.targets = numpy.random.choice(8, 10)

@when(u'the source and target arrays and layout are combined')
def step_impl(context):
    context.canvas, axes, mark = toyplot.graph(context.sources, context.targets, layout=context.layout)

@given(u'explicit source and target arrays with loops')
def step_impl(context):
    numpy.random.seed(1234)
    context.sources = numpy.concatenate((numpy.random.choice(8, 10), [1, 3]))
    context.targets = numpy.concatenate((numpy.random.choice(8, 10), [1, 3]))

