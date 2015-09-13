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


class GraphEdges(object):
    """Based class for graph edge layout algorithms - objects that compute coordinates for graph edges only."""
    def edges(self, vcount, edges, vcoordinates):
        raise NotImplementedError()


class StraightEdges(GraphEdges):
    """Creates straight edges between graph vertices."""
    def edges(self, vcount, edges, vcoordinates):
        eshape = numpy.tile("ML", len(edges))
        ecoordinates = numpy.empty((len(edges) * 2, 2))
        ecoordinates[0::2] = vcoordinates[edges.T[0]]
        ecoordinates[1::2] = vcoordinates[edges.T[1]]
        return eshape, ecoordinates


class CurvedEdges(GraphEdges):
    """Creates curved edges between graph vertices."""
    def __init__(self, curvature=0.15):
        self._curvature = curvature

    def edges(self, vcount, edges, vcoordinates):
        eshape = numpy.tile("MQ", len(edges))
        ecoordinates = numpy.empty((len(edges) * 3, 2))

        sources = vcoordinates[edges.T[0]]
        targets = vcoordinates[edges.T[1]]
        offsets = numpy.dot(targets - sources, [[0, 1], [-1, 0]]) * self._curvature
        midpoints = ((sources + targets) * 0.5) + offsets

        ecoordinates[0::3] = sources
        ecoordinates[1::3] = midpoints
        ecoordinates[2::3] = targets

        return eshape, ecoordinates


class Graph(object):
    """Base class for graph layout algorithms - objects that compute coordinates for graph vertices and edges."""
    def graph(self, vcount, edges):
        raise NotImplementedError()


class Random(Graph):
    """Compute a random graph layout."""
    def __init__(self, edges=None, seed=1234):
        if edges is None:
            edges = StraightEdges()

        self._edges = edges
        self._generator = numpy.random.RandomState(seed=seed)

    def graph(self, vcount, edges):
        vcoordinates = numpy.ma.array(self._generator.uniform(size=(vcount, 2)))
        eshape, ecoordinates = self._edges.edges(vcount, edges, vcoordinates)
        return vcoordinates, eshape, ecoordinates

def _add_at(target, target_indices, source):
    """Add source values to the target and handle duplicate indices correctly.

    With numpy, the expression `target[indices] += source` does not work intuitively
    if there are duplicate indices.  This function handles this case as you would
    expect, by accumulating multiple values for a single target.
    """
    if getattr(numpy.add, "at", None) is not None:
        numpy.add.at(target, target_indices, source)
    else: # Shim for numpy < 1.8
        for source_index, target_index in enumerate(target_indices):
            target[target_index] += source[source_index]


class Eades(Graph):
    """Compute a force directed graph layout using the 1984 algorithm by Eades."""
    def __init__(self, edges=None, c1=2, c2=1, c3=1, c4=0.1, M=100, seed=1234):
        if edges is None:
            edges = StraightEdges()

        self._edges = edges
        self._c1 = c1
        self._c2 = c2
        self._c3 = c3
        self._c4 = c4
        self._M = M
        self._generator = numpy.random.RandomState(seed=seed)

    def graph(self, vcount, edges):
        # Initialize coordinates
        vcoordinates = numpy.ma.array(self._generator.uniform(size=(vcount, 2)))

        # Repeatedly apply attract / repel forces to the vertices
        vertices = numpy.column_stack(numpy.triu_indices(n=vcount, k=1))
        for iteration in numpy.arange(self._M):
            offsets = numpy.zeros((vcount, 2))

            # Repel
            a = vcoordinates[vertices.T[0]]
            b = vcoordinates[vertices.T[1]]
            delta = a - b
            distance = numpy.linalg.norm(delta, axis=1)[:,None]
            delta /= distance
            force = self._c3 / numpy.square(distance)
            delta *= force
            _add_at(offsets, vertices.T[0], delta)
            _add_at(offsets, vertices.T[1], -delta)

            # Attract
            a = vcoordinates[edges.T[0]]
            b = vcoordinates[edges.T[1]]
            delta = b - a
            distance = numpy.linalg.norm(delta, axis=1)[:,None]
            delta /= distance
            force = self._c1 * numpy.log(distance / self._c2)
            delta *= force
            _add_at(offsets, edges.T[0], delta)
            _add_at(offsets, edges.T[1], -delta)

            # Sum offsets
            vcoordinates += self._c4 * offsets

        eshape, ecoordinates = self._edges.edges(vcount, edges, vcoordinates)
        return vcoordinates, eshape, ecoordinates


class FruchtermanReingold(Graph):
    """Compute a force directed graph layout using the 1991 algorithm of Fruchterman and Reingold."""
    def __init__(self, edges=None, area=1, temperature=0.1, M=50, seed=1234):
        if edges is None:
            edges = StraightEdges()

        self._edges = edges
        self._area = area
        self._temperature = temperature
        self._M = M
        self._generator = numpy.random.RandomState(seed=seed)

    def graph(self, vcount, edges):
        # Setup parameters
        k = numpy.sqrt(self._area / vcount)

        # Initialize coordinates
        vcoordinates = numpy.ma.array(self._generator.uniform(size=(vcount, 2)))

        # Repeatedly apply attract / repel forces to the vertices
        vertices = numpy.column_stack(numpy.triu_indices(n=vcount, k=1))
        for temperature in numpy.linspace(self._temperature, 0, self._M, endpoint=False):
            offsets = numpy.zeros((vcount, 2))

            # Repel
            a = vcoordinates[vertices.T[0]]
            b = vcoordinates[vertices.T[1]]
            delta = a - b
            distance = numpy.linalg.norm(delta, axis=1)[:,None]
            delta /= distance
            force = numpy.square(k) / distance
            delta *= force
            _add_at(offsets, vertices.T[0], +delta)
            _add_at(offsets, vertices.T[1], -delta)

            # Attract
            a = vcoordinates[edges.T[0]]
            b = vcoordinates[edges.T[1]]
            delta = b - a
            distance = numpy.linalg.norm(delta, axis=1)[:,None]
            delta /= distance
            force = numpy.square(distance) / k
            delta *= force
            _add_at(offsets, edges.T[0], +delta)
            _add_at(offsets, edges.T[1], -delta)

            # Limit offsets to the temperature
            distance = numpy.linalg.norm(offsets, axis=1)
            offsets /= distance[:,None]
            offsets *= numpy.minimum(temperature, distance)[:,None]

            # Sum offsets
            vcoordinates += offsets

        eshape, ecoordinates = self._edges.edges(vcount, edges, vcoordinates)
        return vcoordinates, eshape, ecoordinates

class GraphViz(Graph):
    """Compute a graph layout using GraphViz."""
    def graph(self, vcount, edges):
        dotfile = io.BytesIO()
        dotfile.write("digraph {\n")
        dotfile.write("node [fixedsize = shape; width=0; height=0;]\n")
        for vertex in numpy.arange(vcount):
            dotfile.write("""%s\n""" % vertex)
        for source, target in edges:
            dotfile.write("%s -> %s\n" % (source, target))
        dotfile.write("}\n")

        command = [
            "dot",
            "-Tplain",
            ]
        graphviz = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout, stderr = graphviz.communicate(dotfile.getvalue())

        if stderr:
            toyplot.log.error(stderr)

        vertices = []
        edges = []
        for line in io.BytesIO(stdout):
            if line.startswith("node"):
                vertices.append(line.split())
            elif line.startswith("edge"):
                edges.append(line.split())

        vcoordinates = numpy.ma.empty((vcount, 2))
        for vertex in vertices:
            index = int(vertex[1])
            vcoordinates[index, 0] = float(vertex[2])
            vcoordinates[index, 1] = float(vertex[3])

        eshape = []
        ecoordinates = []
        for edge in edges:
            count = int(edge[3])
            shape = "M"
            for i in range((count - 1) // 3):
                shape += "C"
            eshape.append(shape)
            for i in range(4, 4 + count * 2, 2):
                ecoordinates.append([float(edge[i]), float(edge[i+1])])

        eshape = numpy.array(eshape)
        ecoordinates = numpy.array(ecoordinates)

        return vcoordinates, eshape, ecoordinates
