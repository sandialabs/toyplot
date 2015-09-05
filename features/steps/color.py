from __future__ import division

from behave import *

import json
import nose.tools
import numpy
import toyplot.color
import toyplot.testing


@when(u'toyplot.color.css receives {value}')
def step_impl(context, value):
    context.value = value


@then(u'toyplot.color.css should return {value}')
def step_impl(context, value):
    toyplot.testing.assert_color_equal(
        toyplot.color.css(context.value), eval(value))


@when(u'toyplot.color.to_css receives {value}')
def step_impl(context, value):
    context.value = eval(value)


@then(u'toyplot.color.to_css should return {value}')
def step_impl(context, value):
    nose.tools.assert_equal(toyplot.color.to_css(context.value), value)


@given(u'a collection of Color Brewer palettes')
def step_impl(context):
    context.palettes = {
        name: toyplot.color.brewer(name) for name in toyplot.color.brewer.names()}


@then(u'each palette can be rendered as ipython html')
def step_impl(context):
    for name, palette in context.palettes.items():
        toyplot.testing.assert_html_equal(
            palette._repr_html_(), "color-brewer-%s" % name)


@when(u'the user creates a Color Brewer palette')
def step_impl(context):
    context.palette = toyplot.color.brewer("BlueYellowRed")


@then(u'the Color Brewer palette should have the maximum number of colors')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-brewer")


@when(u'the user creates a sized Color Brewer palette')
def step_impl(context):
    context.palette = toyplot.color.brewer("BlueYellowRed", 5)


@then(u'the Color Brewer palette should have the requested number of colors')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-brewer-count")


@when(u'the user creates a reversed Color Brewer palette')
def step_impl(context):
    context.palette = toyplot.color.brewer("BlueYellowRed", 5, reverse=True)


@then(u'the Color Brewer palette should have its colors reversed')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-brewer-reverse")


@given(u'a collection of diverging color maps')
def step_impl(context):
    context.color_maps = [(name, toyplot.color.diverging(name))
                          for name in toyplot.color.diverging.names()]


@then(u'each diverging color map can be rendered as ipython html')
def step_impl(context):
    for name, color_map in context.color_maps:
        toyplot.testing.assert_html_equal(
            color_map._repr_html_(), "color-diverging-map-%s" % name)


@when(u'the user creates a default diverging color map')
def step_impl(context):
    context.color_map = toyplot.color.DivergingMap()


@then(u'the default diverging color map can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.color_map._repr_html_(), "color-diverging-map")


@when(u'the user creates a custom diverging color map')
def step_impl(context):
    context.color_map = toyplot.color.DivergingMap(
        toyplot.color.rgb(0.7, 0, 0), toyplot.color.rgb(0, 0.6, 0))


@then(u'the custom diverging color map can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.color_map._repr_html_(), "color-diverging-map-custom")


@when(u'the user creates a default diverging color map with domain')
def step_impl(context):
    context.color_map = toyplot.color.DivergingMap(domain_min=0, domain_max=1)


@then(u'individual values can be mapped to colors by the diverging color map')
def step_impl(context):
    toyplot.testing.assert_color_equal(
        context.color_map.color(-1), [0.33479085, 0.28308437, 0.75649522, 1.])
    toyplot.testing.assert_color_equal(
        context.color_map.color(0), [0.33479085, 0.28308437, 0.75649522, 1.])
    toyplot.testing.assert_color_equal(
        context.color_map.color(0.5), [0.86541961, 0.86538428, 0.86533315, 1.])
    toyplot.testing.assert_color_equal(
        context.color_map.color(1), [0.69462562, 0.00296461, 0.15458183, 1.])
    toyplot.testing.assert_color_equal(
        context.color_map.color(2), [0.69462562, 0.00296461, 0.15458183, 1.])


@then(
    u'individual values can be mapped to css colors by the diverging color map')
def step_impl(context):
    nose.tools.assert_equal(
        context.color_map.css(-1), "rgba(33.5%,28.3%,75.6%,1)")
    nose.tools.assert_equal(
        context.color_map.css(0), "rgba(33.5%,28.3%,75.6%,1)")
    nose.tools.assert_equal(
        context.color_map.css(0.5), "rgba(86.5%,86.5%,86.5%,1)")
    nose.tools.assert_equal(
        context.color_map.css(1), "rgba(69.5%,0.296%,15.5%,1)")
    nose.tools.assert_equal(
        context.color_map.css(2), "rgba(69.5%,0.296%,15.5%,1)")


@given(u'a linear color map')
def step_impl(context):
    context.color_map = toyplot.color.LinearMap(
        toyplot.color.Palette(["red", "blue"]), domain_min=0, domain_max=1)


@then(u'the linear color map can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.color_map._repr_html_(), "color-linear-map")


@then(u'the linear color map can map scalar values to toyplot colors')
def step_impl(context):
    toyplot.testing.assert_color_equal(
        context.color_map.color(-1), (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(
        context.color_map.color(0), (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(
        context.color_map.color(0.5), (0.5, 0, 0.5, 1))
    toyplot.testing.assert_color_equal(
        context.color_map.color(1), (0, 0, 1, 1))
    toyplot.testing.assert_color_equal(
        context.color_map.color(2), (0, 0, 1, 1))


@then(u'the linear color map can map scalar values to css colors')
def step_impl(context):
    nose.tools.assert_equal(context.color_map.css(-1), "rgba(100%,0%,0%,1)")
    nose.tools.assert_equal(context.color_map.css(0), "rgba(100%,0%,0%,1)")
    nose.tools.assert_equal(context.color_map.css(0.5), "rgba(50%,0%,50%,1)")
    nose.tools.assert_equal(context.color_map.css(1), "rgba(0%,0%,100%,1)")
    nose.tools.assert_equal(context.color_map.css(2), "rgba(0%,0%,100%,1)")


@given(u'a starting color')
def step_impl(context):
    context.color = toyplot.color.Palette().color(0)


@then(u'the color can be used to generate a palette of lighter shades')
def step_impl(context):
    palette = toyplot.color.lighten(context.color)
    toyplot.testing.assert_html_equal(palette._repr_html_(), "color-lighten")


@given(u'two color palettes')
def step_impl(context):
    context.palettes = [
        toyplot.color.brewer("Reds"), toyplot.color.brewer("Blues")]


@then(u'the color palettes can be concatenated into a single palette')
def step_impl(context):
    palette = context.palettes[0] + context.palettes[1]
    toyplot.testing.assert_html_equal(
        palette._repr_html_(), "color-palette-add")


@given(u'a color palette')
def step_impl(context):
    context.palette = toyplot.color.brewer("Reds")


@then(u'another palette can be appended')
def step_impl(context):
    context.palette += toyplot.color.brewer("Blues")
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-palette-iadd")


@given(u'a default color palette')
def step_impl(context):
    context.palette = toyplot.color.Palette()


@then(u'the palette should contain 8 colors')
def step_impl(context):
    nose.tools.assert_equal(len(context.palette), 8)


@then(u'the default palette can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-palette")


@given(u'a reversed default color palette')
def step_impl(context):
    context.palette = toyplot.color.Palette(reverse=True)


@then(u'the reversed palette can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-palette-reverse")

@given(u'a collection of CSS color names, a color palette can be created')
def step_impl(context):
    palette = toyplot.color.Palette(["red", "green", "blue", (1, 1, 0)])
    toyplot.testing.assert_html_equal(palette._repr_html_(), "color-palette-css-names")

@given(u'a color palette, colors can be retrieved using item notation')
def step_impl(context):
    palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    toyplot.testing.assert_color_equal(palette[0], (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(palette[1], (0, 1, 0, 1))
    toyplot.testing.assert_color_equal(palette[-1], (0, 0, 1, 1))
    with nose.tools.assert_raises(IndexError):
        palette[3]
    with nose.tools.assert_raises(TypeError):
        palette[0:3]

@given(u'a color palette, callers can iterate over the colors')
def step_impl(context):
    palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    color = iter(palette)
    toyplot.testing.assert_color_equal(next(color), (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(next(color), (0, 1, 0, 1))
    toyplot.testing.assert_color_equal(next(color), (0, 0, 1, 1))
    with nose.tools.assert_raises(StopIteration):
        next(color)

@given(u'a color palette, callers can retrieve colors by index')
def step_impl(context):
    palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    toyplot.testing.assert_color_equal(palette.color(0), (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(palette.color(-1), (0, 0, 1, 1))

@given(u'a color palette, colors can retrieve css colors by index')
def step_impl(context):
    palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    nose.tools.assert_equal(palette.css(0), "rgba(100%,0%,0%,1)")
    nose.tools.assert_equal(palette.css(-1), "rgba(0%,0%,100%,1)")

@given(u'a categorical color map, the map can be rendered as ipython html')
def step_impl(context):
    colormap = toyplot.color.CategoricalMap(
        toyplot.color.brewer("BlueGreenBrown", 3))
    toyplot.testing.assert_html_equal(colormap._repr_html_(), "color-categorical-map")

@given(u'a categorical color map, multiple colors can be returned by index')
def step_impl(context):
    colormap = toyplot.color.CategoricalMap(
        toyplot.color.Palette(["red", "lime", "blue", (1, 1, 1)]))
    toyplot.testing.assert_colors_equal(colormap.colors(
        [0, 1, 3, 4]), [(1, 0, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1), (1, 0, 0, 1)])

@given(u'a categorical color map, individual colors can be returned by index')
def step_impl(context):
    colormap = toyplot.color.CategoricalMap(
        toyplot.color.Palette(["red", "lime", "blue", (1, 1, 1)]))
    toyplot.testing.assert_color_equal(colormap.color(0), (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(colormap.color(-1), (1, 1, 1, 1))

@given(u'a categorical color map, individual css colors can be returned by index')
def step_impl(context):
    colormap = toyplot.color.CategoricalMap(
        toyplot.color.Palette(["red", "lime", "blue", (1, 1, 1)]))
    nose.tools.assert_equal(colormap.css(0), "rgba(100%,0%,0%,1)")
    nose.tools.assert_equal(colormap.css(-1), "rgba(100%,100%,100%,1)")

@given(u'a set of diverging series')
def step_impl(context):
    context.x = numpy.linspace(0, 1)
    context.series = numpy.column_stack((context.x**2, context.x**2/2, context.x**2/3, context.x**2/4))

@given(u'a set of per-series values')
def step_impl(context):
    context.series_values = numpy.array([1, 4, 3, 2])

@given(u'a set of per-series colors')
def step_impl(context):
    context.series_colors = ["red", "green", "blue", "yellow"]

@given(u'a set of per-datum values')
def step_impl(context):
    numpy.random.seed(1234)
    context.datum_values = numpy.column_stack((
        numpy.random.normal(loc=0, size=context.series.shape[0]),
        numpy.random.normal(loc=3, size=context.series.shape[0]),
        numpy.random.normal(loc=6, size=context.series.shape[0]),
        numpy.random.normal(loc=9, size=context.series.shape[0]),
        ))

@given(u'a set of per-datum colors')
def step_impl(context):
    context.datum_colors = numpy.tile(toyplot.color.css("black"), context.series.shape)
    context.datum_colors[15:20, 0] = toyplot.color.css("red")
    context.datum_colors[25:30, 1] = toyplot.color.css("green")
    context.datum_colors[35:40, 2] = toyplot.color.css("blue")
    context.datum_colors[45:50, 3] = toyplot.color.css("yellow")

@then(u'bars can be rendered with default colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-default")

@then(u'bars can be rendered with one explicit color')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-one-color")

@then(u'bars can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.series_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-series-colors")

@then(u'bars can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.datum_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-datum-colors")

@then(u'bars can be rendered with palette colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-palette")

@then(u'bars can be rendered with colormap colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-colormap")

@then(u'bars can be rendered with per-series value colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.series_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-series-values")

@then(u'bars can be rendered with per-series value + palette colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=(context.series_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-series-values-palette")

@then(u'bars can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=(context.series_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-series-values-colormap")

@then(u'bars can be rendered with per-datum value colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=context.datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-datum-values")

@then(u'bars can be rendered with per-datum value + palette colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=(context.datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-datum-values-palette")

@then(u'bars can be rendered with per-datum value + colormap colors')
def step_impl(context):
    context.axes.bars(context.series, baseline="symmetric", color=(context.datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-bars-per-datum-values-colormap")


@then(u'fills can be rendered with default colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-default")

@then(u'fills can be rendered with one explicit color')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-one-color")

@then(u'fills can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=context.series_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-per-series-colors")

@then(u'fills can be rendered with palette colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-palette")

@then(u'fills can be rendered with colormap colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-colormap")

@then(u'fills can be rendered with per-series value colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=context.series_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-per-series-values")

@then(u'fills can be rendered with per-series value + palette colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=(context.series_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-per-series-values-palette")

@then(u'fills can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.fill(context.series, baseline="symmetric", color=(context.series_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-fills-per-series-values-colormap")



@then(u'hlines can be rendered with default colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-default")

@then(u'hlines can be rendered with one explicit color')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-one-color")

@then(u'hlines can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color=context.datum_colors[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-per-datum-colors")

@then(u'hlines can be rendered with palette colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-palette")

@then(u'hlines can be rendered with colormap colors')
def step_impl(context):
    context.axes.hlines(context.series[:,0], color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-colormap")

@then(u'hlines can be rendered with per-datum value colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.hlines(context.series[:,0], color=datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-per-datum-values")

@then(u'hlines can be rendered with per-datum value + palette colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.hlines(context.series[:,0], color=(datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-per-datum-values-palette")

@then(u'hlines can be rendered with per-datum value + colormap colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.hlines(context.series[:,0], color=(datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-hlines-per-datum-values-colormap")

@then(u'plots can be rendered with default colors')
def step_impl(context):
    context.axes.plot(context.series)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-default")

@then(u'plots can be rendered with one explicit color')
def step_impl(context):
    context.axes.plot(context.series, color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-one-color")

@then(u'plots can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.plot(context.series, color=context.series_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-colors")

@then(u'plots can be rendered with palette colors')
def step_impl(context):
    context.axes.plot(context.series, color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-palette")

@then(u'plots can be rendered with colormap colors')
def step_impl(context):
    context.axes.plot(context.series, color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-colormap")

@then(u'plots can be rendered with per-series value colors')
def step_impl(context):
    context.axes.plot(context.series, color=context.series_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values")

@then(u'plots can be rendered with per-series value + palette colors')
def step_impl(context):
    context.axes.plot(context.series, color=(context.series_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values-palette")

@then(u'plots can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.plot(context.series, color=(context.series_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values-colormap")

@then(u'plots can be rendered with default marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-marker-default")

@then(u'plots can be rendered with one explicit marker color')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-one-marker-color")

@then(u'plots can be rendered with per-series explicit marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=context.series_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-marker-colors")

@then(u'plots can be rendered with palette marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-palette-marker")

@then(u'plots can be rendered with colormap marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-colormap-marker")

@then(u'plots can be rendered with per-series value marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=context.series_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values-marker")

@then(u'plots can be rendered with per-series value + palette marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=(context.series_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values-palette-marker")

@then(u'plots can be rendered with per-series value + colormap marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=(context.series_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-series-values-colormap-marker")

@then(u'plots can be rendered with per-datum value marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=context.datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-datum-values-marker")

@then(u'plots can be rendered with per-datum value + palette marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=(context.datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-datum-values-palette-marker")

@then(u'plots can be rendered with per-datum value + colormap marker colors')
def step_impl(context):
    context.axes.plot(context.series, marker="o", mfill=(context.datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-plots-per-datum-values-colormap-marker")



@then(u'scatterplots can be rendered with default colors')
def step_impl(context):
    context.axes.scatterplot(context.series)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-default")

@then(u'scatterplots can be rendered with one explicit color')
def step_impl(context):
    context.axes.scatterplot(context.series, color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-one-color")

@then(u'scatterplots can be rendered with per-series explicit colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.series_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-series-colors")

@then(u'scatterplots can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.datum_colors)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-datum-colors")

@then(u'scatterplots can be rendered with palette colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-palette")

@then(u'scatterplots can be rendered with colormap colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-colormap")

@then(u'scatterplots can be rendered with per-series value colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.series_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-series-values")

@then(u'scatterplots can be rendered with per-series value + palette colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=(context.series_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-series-values-palette")

@then(u'scatterplots can be rendered with per-series value + colormap colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=(context.series_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-series-values-colormap")

@then(u'scatterplots can be rendered with per-datum value colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=context.datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-datum-values")

@then(u'scatterplots can be rendered with per-datum value + palette colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=(context.datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-datum-values-palette")

@then(u'scatterplots can be rendered with per-datum value + colormap colors')
def step_impl(context):
    context.axes.scatterplot(context.series, color=(context.datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-scatterplots-per-datum-values-colormap")


@then(u'text can be rendered with default colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-default")

@then(u'text can be rendered with one explicit color')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-one-color")

@then(u'text can be rendered with per-datum explicit colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, color=context.datum_colors[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-per-datum-colors")

@then(u'text can be rendered with palette colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-palette")

@then(u'text can be rendered with colormap colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    context.axes.text(context.x, context.series[:,0], text, color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-colormap")

@then(u'text can be rendered with per-datum value colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.text(context.x, context.series[:,0], text, color=datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-per-datum-values")

@then(u'text can be rendered with per-datum value + palette colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.text(context.x, context.series[:,0], text, color=(datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-per-datum-values-palette")

@then(u'text can be rendered with per-datum value + colormap colors')
def step_impl(context):
    text = ["#"] * len(context.series)
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.text(context.x, context.series[:,0], text, color=(datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-text-per-datum-values-colormap")


@then(u'vlines can be rendered with default colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-default")

@then(u'vlines can be rendered with one explicit color')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color="red")
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-one-color")

@then(u'vlines can be rendered with per-datum explicit colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color=context.datum_colors[:,0])
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-per-datum-colors")

@then(u'vlines can be rendered with palette colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color=toyplot.color.brewer("Set1"))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-palette")

@then(u'vlines can be rendered with colormap colors')
def step_impl(context):
    context.axes.vlines(context.series[:,0], color=toyplot.color.LinearMap(toyplot.color.brewer("Set1")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-colormap")

@then(u'vlines can be rendered with per-datum value colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.vlines(context.series[:,0], color=datum_values)
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-per-datum-values")

@then(u'vlines can be rendered with per-datum value + palette colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.vlines(context.series[:,0], color=(datum_values, toyplot.color.brewer("Reds")))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-per-datum-values-palette")

@then(u'vlines can be rendered with per-datum value + colormap colors')
def step_impl(context):
    datum_values = numpy.arange(len(context.series[:,0]))
    context.axes.vlines(context.series[:,0], color=(datum_values, toyplot.color.LinearMap()))
    toyplot.testing.assert_canvas_equal(
        context.canvas, "color-broadcast-vlines-per-datum-values-colormap")


