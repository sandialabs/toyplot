# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import numpy
import toyplot.color

def plot_luma(a, b=None): #pragma: no cover
    if b is not None:
        colormaps = [(a, b)]
    else:
        colormaps = a

    grid_n = 4.0
    grid_m = numpy.ceil(len(colormaps) / grid_n)
    canvas = toyplot.Canvas(grid_n * 150, grid_m * 150)
    for index, (name, colormap) in enumerate(colormaps):
        if isinstance(colormap, toyplot.color.Palette):
            colormap = toyplot.color.LinearMap(colormap)
        x = numpy.linspace(0, 1, 200)
        y = [toyplot.color.to_lab(color)[0] for color in colormap.colors(x, 0, 1)]

        axes = canvas.cartesian(
            grid=(grid_m, grid_n, index),
            ymin=0,
            ymax=100,
            gutter=30,
            xshow=True,
            yshow=True,
            label=name,
            )
        axes.scatterplot(x, y, size=10, color=(x, colormap))
    return canvas
