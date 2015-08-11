from __future__ import division

from behave import *

import json
import nose.tools
import numpy
import toyplot.color
import toyplot.testing

@given(u'a broadcast color {value}')
def step_impl(context, value):
    context.color = eval(value)


@given(u'a broadcast shape {value}')
def step_impl(context, value):
    context.shape = eval(value)


@then(u'toyplot.color.broadcast should return an all-red color array with shape (2)')
def step_impl(context):
    array = toyplot.color.broadcast(context.color, context.shape)
    numpy.testing.assert_array_equal(array, toyplot.color.array([(1,0,0,1), (1,0,0,1)]))


@then(u'toyplot.color.broadcast should return an all-red color array with shape (2,3)')
def step_impl(context):
    array = toyplot.color.broadcast(context.color, context.shape)
    numpy.testing.assert_array_equal(array, toyplot.color.array([[(1,0,0,1), (1,0,0,1), (1,0,0,1)], [(1,0,0,1), (1,0,0,1), (1,0,0,1)]]))


@then(u'toyplot.color.broadcast should return a red-blue color array with shape (2)')
def step_impl(context):
    array = toyplot.color.broadcast(context.color, context.shape)
    numpy.testing.assert_array_equal(array, toyplot.color.array([(1,0,0,1), (0,0,1,1)]))


@then(u'toyplot.color.broadcast should return a red-blue color array with shape (3,2)')
def step_impl(context):
    array = toyplot.color.broadcast(context.color, context.shape)
    numpy.testing.assert_array_equal(array, toyplot.color.array([[(1,0,0,1), (0,0,1,1)], [(1,0,0,1), (0,0,1,1)], [(1,0,0,1), (0,0,1,1)]]))


@then(u'toyplot.color.broadcast should return a red-green-blue-yellow color array with shape (2,2)')
def step_impl(context):
    array = toyplot.color.broadcast(context.color, context.shape)
    numpy.testing.assert_array_equal(array, toyplot.color.array([[(1,0,0,1), (0,1,0,1)], [(0,0,1,1), (1,1,0,1)]]))


@then(u'toyplot.color.broadcast should return a blues color array with shape (3)')
def step_impl(context):
    array = toyplot.color.broadcast(context.color, context.shape)
    numpy.testing.assert_array_equal(array, toyplot.color.array([
        (0.03137254901960784, 0.25098039215686274, 0.5058823529411764, 1.0),
        (0.4823529411764706, 0.8, 0.7686274509803922, 1.0),
        (0.9686274509803922, 0.9882352941176471, 0.9411764705882353, 1.0)]))


@then(u'toyplot.color.broadcast should return a blues color array with shape (2,3) and identical columns')
def step_impl(context):
    array = toyplot.color.broadcast(context.color, context.shape)
    numpy.testing.assert_array_equal(array, toyplot.color.array([
        [(0.03137254901960784, 0.25098039215686274, 0.5058823529411764, 1.0),
        (0.4823529411764706, 0.8, 0.7686274509803922, 1.0),
        (0.9686274509803922, 0.9882352941176471, 0.9411764705882353, 1.0)],
        [(0.03137254901960784, 0.25098039215686274, 0.5058823529411764, 1.0),
        (0.4823529411764706, 0.8, 0.7686274509803922, 1.0),
        (0.9686274509803922, 0.9882352941176471, 0.9411764705882353, 1.0)]]))


@then(u'toyplot.color.broadcast should return a blues color array with shape (2,3)')
def step_impl(context):
    array = toyplot.color.broadcast(context.color, context.shape)
    numpy.testing.assert_array_equal(array, toyplot.color.array([
        [(0.03137254901960784, 0.25098039215686274, 0.5058823529411764, 1.0),
        (0.11372549019607844, 0.49254901960784314, 0.7168627450980393, 1.0),
        (0.3411764705882353, 0.7215686274509804, 0.8156862745098039, 1.0)],
        [(0.6235294117647059, 0.8533333333333334, 0.7215686274509804, 1.0),
        (0.8313725490196079, 0.9341176470588235, 0.8070588235294117, 1.0),
        (0.9686274509803922, 0.9882352941176471, 0.9411764705882353, 1.0)]]))


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


