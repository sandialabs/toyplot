# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Provides layout algorithms.
"""

from __future__ import division

import io
import numbers
import numpy
import subprocess
import toyplot.compatibility
import toyplot.units

def region(
        xmin,
        xmax,
        ymin,
        ymax,
        bounds=None,
        rect=None,
        corner=None,
        grid=None,
        gutter=40):
    """Specify a rectangular target region relative to a parent region.

    Parameters
    ----------
    xmin: number, required
      Minimum X boundary of the parent region, specified in CSS pixel units.
    xmax: number, required
      Maximum X boundary of the parent region, specified in CSS pixel units.
    ymin: number, required
      Minimum Y boundary of the parent region, specified in CSS pixel units.
    ymax: number, required
      Maximum Y boundary of the parent region, specified in CSS pixel units.
    gutter: number, string, or (number, string) tuple, optional
      Padding around the target region, specified in real-world units.  Defaults
      to CSS pixel units.  See :ref:`units` for details.

    Returns
    -------
    xmin, xmax, ymin, ymax: number
      The boundaries of the target region, specified in CSS pixel units.
    """

    gutter = toyplot.units.convert(gutter, "px", default="px")

    def convert(min, max, value):
        value = toyplot.units.convert(
            value, "px", default="px", reference=max - min)
        if value < 0:
            return float(max + value)
        return float(min + value)

    # Specify explicit bounds for the region
    if bounds is not None:
        if isinstance(bounds, tuple) and len(bounds) == 4:
            return (
                convert(
                    xmin, xmax, bounds[0]), convert(
                    xmin, xmax, bounds[1]), convert(
                    ymin, ymax, bounds[2]), convert(
                    ymin, ymax, bounds[3]))
        raise TypeError(
            "bounds parameter must be an (xmin, xmax, ymin, ymax) tuple.")
    # Specify an explicit rectangle for the region
    if rect is not None:
        if isinstance(rect, tuple) and len(rect) == 4:
            x = convert(xmin, xmax, rect[0])
            y = convert(ymin, ymax, rect[1])
            width = toyplot.units.convert(
                rect[2], "px", default="px", reference=xmax - xmin)
            height = toyplot.units.convert(
                rect[3], "px", default="px", reference=ymax - ymin)
            return (x, x + width, y, y + height)
        raise ValueError("Unrecognized rect type")
    # Offset a rectangle from a corner
    if corner is not None:
        if isinstance(corner, tuple) and len(corner) == 4:
            position = corner[0]
            inset = toyplot.units.convert(corner[1], "px", default="px")
            width = toyplot.units.convert(
                corner[2], "px", default="px", reference=xmax - xmin)
            height = toyplot.units.convert(
                corner[3], "px", default="px", reference=ymax - ymin)
        else:
            raise ValueError("Unrecognized corner type")
        if position == "top":
            return ((xmin + xmax - width) / 2,
                    (xmin + xmax + width) / 2,
                    ymin + inset,
                    ymin + inset + height)
        elif position == "top-right":
            return (
                xmax -
                width -
                inset,
                xmax -
                inset,
                ymin +
                inset,
                ymin +
                inset +
                height)
        elif position == "right":
            return (
                xmax - width - inset,
                xmax - inset,
                (ymin + ymax - height) / 2,
                (ymin + ymax + height) / 2)
        elif position == "bottom-right":
            return (
                xmax -
                width -
                inset,
                xmax -
                inset,
                ymax -
                inset -
                height,
                ymax -
                inset)
        elif position == "bottom":
            return ((xmin + xmax - width) / 2,
                    (xmin + xmax + width) / 2,
                    ymax - inset - height,
                    ymax - inset)
        elif position == "bottom-left":
            return (
                xmin +
                inset,
                xmin +
                inset +
                width,
                ymax -
                inset -
                height,
                ymax -
                inset)
        elif position == "left":
            return (
                xmin + inset,
                xmin + inset + width,
                (ymin + ymax - height) / 2,
                (ymin + ymax + height) / 2)
        elif position == "top-left":
            return (
                xmin +
                inset,
                xmin +
                inset +
                width,
                ymin +
                inset,
                ymin +
                inset +
                height)
        else:
            raise ValueError("Unrecognized corner")
    # Choose a cell from an MxN grid, with optional column/row spanning.
    if grid is not None:
        # Cell n (in left-to-right, top-to-bottom order) of an M x N grid
        if len(grid) == 3:
            M, N, n = grid
            i = n // N
            j = n % N
            rowspan, colspan = (1, 1)
        elif len(grid) == 4:  # Cell i,j of an M x N grid
            M, N, i, j = grid
            rowspan, colspan = (1, 1)
        # Cells [i, i+rowspan), [j, j+colspan) of an M x N grid
        elif len(grid) == 6:
            M, N, i, rowspan, j, colspan = grid

        cell_width = (xmax - xmin) / N
        cell_height = (ymax - ymin) / M

        return (
            (j * cell_width) + gutter,
            ((j + colspan) * cell_width) - gutter,
            (i * cell_height) + gutter,
            ((i + rowspan) * cell_height) - gutter,
        )
    # If nothing else fits, consume the entire region
    return (xmin + gutter, xmax - gutter, ymin + gutter, ymax - gutter)

class Graph(object):
    """Base class for graph layout algorithms - objects that compute the positions and orientations of graph vertices and edges."""

    def graph(self, vcount, edges, vcoordinates):
        """Return a set of coordinates for the given graph.

        Parameters
        ----------
        """

        raise NotImplementedError()

class Null(Graph):
    """Do-nothing graph layout."""
    def graph(self, vcount, edges, vcoordinates):
        pass

class Random(Graph):
    """Compute a random graph layout."""
    def __init__(self, seed):
        self._generator = numpy.random.RandomState(seed=seed)

    def graph(self, vcount, edges, vcoordinates):
        vcoordinates[...] = self._generator.uniform(size=vcoordinates.shape)

class GraphViz(Graph):
    """Compute a graph layout using GraphViz."""
    def graph(self, vcount, edges, vcoordinates):
        dotfile = io.BytesIO()
        dotfile.write("digraph {\n")
        for source, target in edges:
            dotfile.write("%s -> %s\n" % (source, target))
        dotfile.write("}\n")

        command = [
            "fdp",
            "-Tplain",
            ]
        graphviz = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout, stderr = graphviz.communicate(dotfile.getvalue())
        vertices = []
        edges = []
        for line in io.BytesIO(stdout):
            if line.startswith("node"):
                vertices.append(line.split())
            elif line.startswith("edge"):
                edges.append(line.split())
        for index, vertex in enumerate(vertices):
            vcoordinates[index, 0] = float(vertex[2])
            vcoordinates[index, 1] = float(vertex[3])
        #for edge in edges:
        #    print edge
