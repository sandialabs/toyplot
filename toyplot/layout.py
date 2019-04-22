# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Provides layout algorithms.
"""


import time

import custom_inherit
import numpy

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
        margin=None):
    """Specify a rectangular target region relative to a parent region.

    Parameters
    ----------
    xmin: :class:`number<numbers.Number>`, required
      Minimum X boundary of the parent region, specified in CSS pixel units.
    xmax: :class:`number<numbers.Number>`, required
      Maximum X boundary of the parent region, specified in CSS pixel units.
    ymin: :class:`number<numbers.Number>`, required
      Minimum Y boundary of the parent region, specified in CSS pixel units.
    ymax: :class:`number<numbers.Number>`, required
      Maximum Y boundary of the parent region, specified in CSS pixel units.
    margin: :class:`number<numbers.Number>`, string, (:class:`number<numbers.Number>`, string) tuple, or tuple containing between one and four :class:`numbers<numbers.Number>`, strings, or (:class:`number<numbers.Number>`, string) tuples, optional
      Padding around the target region, specified in real-world units.  Defaults
      to CSS pixel units.  See :ref:`units` for details.  Follows the same behavior as the CSS margin property.

    Returns
    -------
    xmin, xmax, ymin, ymax: :class:`number<numbers.Number>`
      The boundaries of the target region, specified in CSS pixel units.
    """

    if margin is None:
        margin = 0

    if isinstance(margin, tuple):
        if len(margin) == 4:
            margin_top = toyplot.units.convert(margin[0], "px", default="px")
            margin_right = toyplot.units.convert(margin[1], "px", default="px")
            margin_bottom = toyplot.units.convert(margin[2], "px", default="px")
            margin_left = toyplot.units.convert(margin[3], "px", default="px")
        elif len(margin) == 3:
            margin_top = toyplot.units.convert(margin[0], "px", default="px")
            margin_left = margin_right = toyplot.units.convert(margin[1], "px", default="px")
            margin_bottom = toyplot.units.convert(margin[2], "px", default="px")
        elif len(margin) == 2:
            margin_top = margin_bottom = toyplot.units.convert(margin[0], "px", default="px")
            margin_left = margin_right = toyplot.units.convert(margin[1], "px", default="px")
        elif len(margin) == 1:
            margin_top = margin_bottom = margin_left = margin_right = toyplot.units.convert(margin[0], "px", default="px")
    else:
        margin_top = margin_bottom = margin_left = margin_right = toyplot.units.convert(margin, "px", default="px")

    def convert(vmin, vmax, value):
        value = toyplot.units.convert(
            value, "px", default="px", reference=vmax - vmin)
        if value < 0:
            return float(vmax + value)
        return float(vmin + value)

    # Specify explicit bounds for the region
    if bounds is not None:
        if isinstance(bounds, tuple) and len(bounds) == 4:
            return (
                convert(xmin, xmax, bounds[0]),
                convert(xmin, xmax, bounds[1]),
                convert(ymin, ymax, bounds[2]),
                convert(ymin, ymax, bounds[3]),
            )
        raise TypeError("bounds parameter must be an (xmin, xmax, ymin, ymax) tuple.") # pragma: no cover
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
        raise ValueError("Unrecognized rect type") # pragma: no cover
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
            raise ValueError("corner parameter must be a (corner, inset, width, height) tuple.") # pragma: no cover
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
            raise ValueError("Unrecognized corner") # pragma: no cover

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
            (j * cell_width) + margin_left,
            ((j + colspan) * cell_width) - margin_right,
            (i * cell_height) + margin_top,
            ((i + rowspan) * cell_height) - margin_bottom,
        )
    # If nothing else fits, consume the entire region
    return (xmin + margin_left, xmax - margin_right, ymin + margin_top, ymax - margin_bottom)


class Graph(object):
    """Stores graph layout information.

    Typically used when sharing a layout among more than one graph.
    """
    def __init__(self, vids, vcoordinates, edges, eshapes, ecoordinates):
        self._vids = vids
        self._vcoordinates = vcoordinates
        self._edges = edges
        self._eshapes = eshapes
        self._ecoordinates = ecoordinates

    @property
    def vcount(self):
        """Return the number of vertices :math:`V` in the graph."""
        return len(self._vids)

    @property
    def vids(self):
        """Return :math:`V` graph vertex identifiers."""
        return self._vids

    @property
    def vcoordinates(self):
        """Return graph vertex coordinates as a :math:`V \\times 2` matrix."""
        return self._vcoordinates

    @property
    def ecount(self):
        """Return the number of edges :math:`E` in the graph."""
        return len(self._edges)

    @property
    def eshapes(self):
        """Return a vector of :math:`E` string edge shapes."""
        return self._eshapes

    @property
    def ecoordinates(self):
        """Return a matrix of edge coordinates.  The number of coordinates is determined by the contents of the `eshapes` vector."""
        return self._ecoordinates

    @property
    def edges(self):
        """Return the graph edges as a :math:`E \\times 2` matrix of source, target indices."""
        return self._edges

def graph(a, b=None, c=None, olayout=None, layout=None, vcoordinates=None):
    """Compute a graph layout."""

    stack = [c, b, a]

    # Identify the graph's edges.
    if isinstance(stack[-1], numpy.ndarray) and stack[-1].ndim == 2 and stack[-1].shape[1] == 2:
        edges = stack.pop()
        ecount = edges.shape[0]
    else:
        sources = toyplot.require.vector(stack.pop())
        ecount = len(sources)
        targets = toyplot.require.vector(stack.pop(), ecount)
        edges = numpy.column_stack((sources, targets))

    # Identify the vertex ids induced by the edges.
    vids, edges = numpy.unique(edges, return_inverse=True)
    edges = edges.reshape((ecount, 2), order="C")

    # If the caller supplied extra vertex ids, merge them in.
    if stack and stack[-1] is not None:
        extra_vids = toyplot.require.vector(stack.pop())
        disconnected_vids = numpy.setdiff1d(extra_vids, vids)
        vids = numpy.append(vids, disconnected_vids)

    # Setup storage to receive vertex coordinates
    vcount = len(vids)
    ivcoordinates = numpy.ma.masked_all((vcount, 2))

    # If the caller supplied the layout for an external graph, merge those coordinates in.
    if olayout is not None:
        olayout = toyplot.require.instance(olayout, (toyplot.mark.Graph, toyplot.layout.Graph))
        oindices = numpy.in1d(olayout.vids, vids, assume_unique=True)
        iindices = numpy.in1d(vids, olayout.vids, assume_unique=True)
        ivcoordinates[iindices] = olayout.vcoordinates[oindices]

    # If the caller supplied extra vertex coordinates, merge them in.
    if vcoordinates is not None:
        external_vcoordinates = toyplot.require.scalar_matrix(vcoordinates, rows=vcount, columns=2)
        mask = numpy.ma.getmaskarray(external_vcoordinates)
        ivcoordinates = numpy.ma.where(mask, ivcoordinates, external_vcoordinates)

    # Apply the layout algorithm to whatever's left.
    start = time.time()
    if layout is None:
        # If there are unspecified coordinates, use a force-directed layout.
        if numpy.ma.is_masked(ivcoordinates):
            layout = toyplot.layout.FruchtermanReingold()
        else:
            # Otherwise, we can ignore the vertices and just create edges.
            layout = toyplot.layout.IgnoreVertices()
    vcoordinates, eshapes, ecoordinates = layout.graph(ivcoordinates, edges)
    toyplot.log.info("Graph layout time: %s ms", (time.time() - start) * 1000)

    if numpy.ma.is_masked(vcoordinates):
        raise RuntimeError("Graph layout cannot return masked vertex coordinates.") # pragma: no cover

    return Graph(vids, vcoordinates, edges, eshapes, ecoordinates)

def _add_at(target, target_indices, source):
    """Add source values to the target and handle duplicate indices correctly.

    With numpy, the expression `target[indices] += source` does not work intuitively
    if there are duplicate indices.  This function handles this case as you would
    expect, by accumulating multiple values for a single target.
    """
    if getattr(numpy.add, "at", None) is not None:
        numpy.add.at(target, target_indices, source)
    else: # Shim for numpy < 1.8
        for source_index, target_index in enumerate(target_indices): # pragma: no cover
            target[target_index] += source[source_index]


#def _floyd_warshall_shortest_path(vcount, edges):
#    """Compute the (directed) shortest paths between every pair of vertices in a graph, using the Floyd-Warshall algorithm.
#
#    Floyd-Warshall is a good choice for computing paths between all pairs of
#    vertices in dense graphs.
#
#    Note that this algorithm is directed, i.e. a path from i -> j doesn't imply
#    a path from j -> i.  The results will contain numpy.inf for vertices that
#    have no path.
#
#    Returns
#    -------
#    shortest_paths: :math:`V \\times V matrix`
#        A matrix where element :math:`E_ij` contains the shortest path distance
#        between vertex :math:`i` and vertex :math:`j`.
#    """
#    distance = numpy.empty((vcount, vcount))
#    distance[...] = numpy.inf
#    distance[numpy.diag_indices_from(distance)] = 0
#    distance[edges.T[0], edges.T[1]] = 1
#    for k in numpy.arange(vcount):
#        for i in numpy.arange(vcount):
#            for j in numpy.arange(vcount):
#                if distance[i, j] > distance[i, k] + distance[k, j]:
#                    distance[i, j] = distance[i, k] + distance[k, j]
#
#    return distance


def _adjacency_list(vcount, edges):
    """Return an adjacency list representation of a graph."""
    targets = [[] for i in numpy.arange(vcount)]
    for source, target in edges:
        targets[source].append(target)
    return targets


def _require_tree(children):
    """Return the root vertex and maximum depth of a tree.

    Parameters
    ----------
    children: list of lists
        Adjacency list representation of a graph.

    Returns
    -------
    root: integer
        Index of the root vertex.
    depth: integer
        Maximum depth of the tree.
    """
    roots = numpy.setdiff1d(numpy.arange(len(children)), numpy.concatenate(children))
    if len(roots) != 1:
        raise ValueError("Not a tree.") # pragma: no cover
    root = roots[0]

    depth = []
    visited = numpy.zeros(len(children), dtype=bool)
    def mark_visited(vertex, vdepth=0):
        if visited[vertex]:
            raise ValueError("Not a tree.") # pragma: no cover
        depth.append(vdepth)
        visited[vertex] = True
        for child in children[vertex]:
            mark_visited(child, vdepth + 1)
    mark_visited(root)

    return root, max(depth)

class EdgeLayout(object, metaclass=custom_inherit.DocInheritMeta(style="numpy_napoleon")):
    """Abstract interface for algorithms that compute graph edge coordinates."""
    def edges(self, vcoordinates, edges):
        """Return edge coordinates for a graph.

        Parameters
        ----------
        vcoordinates : :math:`V \\times 2` matrix
            Contains the coordinates for every graph vertex, in vertex order.
        edges : :math:`E \\times 2` matrix
            Contains the integer vertex indices for every graph edge in edge
            order.  The first and second matrix columns contain the source and
            target vertices respectively.

        Returns
        -------
        eshapes : array of :math:`E` strings
            Contains a shape string for each edge, in edge order.  The shape
            string contains drawing codes that define an arbitrary-complexity
            path for the edge, using a set of current coordinates and a turtle
            drawing model.  The following codes are currently allowed:

            * `M` - change the current coordinates without drawing (requires one set of coordinates).
            * `L` - draw a straight line segment from the current coordinates (requires one set of coordinates).
            * `Q` - draw a quadratic Bezier curve from the current coordinates (requires two sets of coordinates).
            * `C` - draw a cubic Bezier curve from the current coordinates (requires three sets of coordinates).
        ecoordinates : matrix containing two columns
            Contains coordinates for each of the edge shape strings, in drawing-code order.
        """
        raise NotImplementedError() # pragma: no cover


class StraightEdges(EdgeLayout):
    """Creates straight edges between graph vertices."""
    def edges(self, vcoordinates, edges):
        loops = edges.T[0] == edges.T[1]
        if numpy.any(loops):
            toyplot.log.warning("Graph contains %s loop edges that will not be visible.", numpy.count_nonzero(loops))

        eshapes = numpy.tile("ML", len(edges))
        ecoordinates = numpy.empty((len(edges) * 2, 2))
        ecoordinates[0::2] = vcoordinates[edges.T[0]]
        ecoordinates[1::2] = vcoordinates[edges.T[1]]
        return eshapes, ecoordinates


class CurvedEdges(EdgeLayout):
    """Creates curved edges between graph vertices.

    Parameters
    ----------
    curvature : number
        Controls the curvature of each edge's arc, as a percentage of the
        distance between the edge's vertices.  Use negative values to curve
        edges in the opposite direction.
    """
    def __init__(self, curvature=0.15):
        self._curvature = curvature

    def edges(self, vcoordinates, edges):
        loops = edges.T[0] == edges.T[1]
        if numpy.any(loops):
            toyplot.log.warning("Graph contains %s loop edges that will not be visible.", numpy.count_nonzero(loops))

        eshapes = numpy.tile("MQ", len(edges))
        ecoordinates = numpy.empty((len(edges) * 3, 2))

        sources = vcoordinates[edges.T[0]]
        targets = vcoordinates[edges.T[1]]
        offsets = numpy.dot(targets - sources, [[0, 1], [-1, 0]]) * self._curvature
        midpoints = ((sources + targets) * 0.5) + offsets

        ecoordinates[0::3] = sources
        ecoordinates[1::3] = midpoints
        ecoordinates[2::3] = targets

        return eshapes, ecoordinates


class GraphLayout(object, metaclass=custom_inherit.DocInheritMeta(style="numpy_napoleon")):
    """Abstract interface for algorithms that compute coordinates for graph vertices and edges."""
    def graph(self, vcoordinates, edges):
        """Compute vertex and edge coordinates for a graph.

        Parameters
        ----------
        vcoordinates : :math:`V \\times 2` masked array
            Coordinates for every graph vertex, in vertex order.  Where
            practical, only masked coordinates will have values assigned by the
            underlying algorithm.
        edges : :math:`E \\times 2` matrix
            Contains the integer vertex indices for every graph edge in edge
            order.  The first and second matrix columns contain the source and
            target vertices respectively.

        Returns
        -------
        vcoordinates : :math:`V \\times 2` matrix
            Contains coordinates for every graph vertex, in vertex order.
        eshapes : array of :math:`E` strings
            Contains a shape string for each edge, in edge order.  The shape
            string contains drawing codes that define an arbitrary-complexity
            path for the edge, using a set of current coordinates and a turtle
            drawing model.  The following codes are currently allowed:

            * `M` - change the current coordinates without drawing (requires one set of coordinates).
            * `L` - draw a straight line segment (requires one set of coordinates).
            * `Q` - draw a quadratic Bezier curve (requires two sets of coordinates).
            * `C` - draw a cubic Bezier curve (requires three sets of coordinates).
        ecoordinates : matrix containing two columns
            Contains coordinates for each of the edge shape strings, in drawing-code order.
        """
        raise NotImplementedError() # pragma: no cover


class IgnoreVertices(GraphLayout):
    """Do-nothing graph layout for use when all vertices are already specified.

    Parameters
    ----------
    edges: :class:`toyplot.layout.EdgeLayout` instance, optional
        The default will generate straight edges.
    """
    def __init__(self, edges=None):
        if edges is None:
            edges = StraightEdges()

        self._edges = edges

    def graph(self, vcoordinates, edges):
        eshapes, ecoordinates = self._edges.edges(vcoordinates, edges)
        return vcoordinates, eshapes, ecoordinates


class Random(GraphLayout):
    """Compute a random graph layout.

    Parameters
    ----------
    edges: :class:`toyplot.layout.EdgeLayout` instance, optional
        The default will generate straight edges.
    seed: integer, optional
        Random seed used to generate vertex coordinates.
    """
    def __init__(self, edges=None, seed=1234):
        if edges is None:
            edges = StraightEdges()

        self._edges = edges
        self._seed = seed

    def graph(self, vcoordinates, edges):
        generator = numpy.random.RandomState(seed=self._seed)
        mask = numpy.ma.getmaskarray(vcoordinates)
        vcoordinates = numpy.ma.where(mask, generator.uniform(-1, 1, size=vcoordinates.shape), vcoordinates)
        eshapes, ecoordinates = self._edges.edges(vcoordinates, edges)
        return vcoordinates, eshapes, ecoordinates


class Eades(GraphLayout):
    """Compute a force directed graph layout using the 1984 algorithm of Eades.

    Parameters
    ----------
    edges: :class:`toyplot.layout.EdgeLayout` instance, optional
        The default will generate straight edges.
    c1, c2, c3, c4: numbers, optional
        Constants defined in Eades' original paper.
    M: integer, optional
        Number of iterations to run the spring simulation.
    seed: integer, optional
        Random seed used to initialize vertex coordinates.
    """
    def __init__(self, edges=None, c1=2, c2=1, c3=1, c4=0.1, M=100, seed=1234):
        if edges is None:
            edges = StraightEdges()

        self._edges = edges
        self._c1 = c1
        self._c2 = c2
        self._c3 = c3
        self._c4 = c4
        self._M = M
        self._seed = seed

    def graph(self, vcoordinates, edges):
        generator = numpy.random.RandomState(seed=self._seed)
        # Initialize coordinates
        mask = numpy.ma.getmaskarray(vcoordinates)
        vcoordinates = numpy.ma.where(mask, generator.uniform(-1, 1, size=vcoordinates.shape), vcoordinates)

        # Repeatedly apply attract / repel forces to the vertices
        vertices = numpy.column_stack(numpy.triu_indices(n=len(vcoordinates), k=1))
        for iteration in numpy.arange(self._M):
            offsets = numpy.zeros_like(vcoordinates)

            # Repel
            a = vcoordinates[vertices.T[0]]
            b = vcoordinates[vertices.T[1]]
            delta = a - b
            distance = numpy.linalg.norm(delta, axis=1)[:, None]
            delta /= distance
            force = self._c3 / numpy.square(distance)
            delta *= force
            _add_at(offsets, vertices.T[0], delta)
            _add_at(offsets, vertices.T[1], -delta)

            # Attract
            a = vcoordinates[edges.T[0]]
            b = vcoordinates[edges.T[1]]
            delta = b - a
            distance = numpy.linalg.norm(delta, axis=1)[:, None]
            delta /= distance
            force = self._c1 * numpy.log(distance / self._c2)
            delta *= force
            _add_at(offsets, edges.T[0], delta)
            _add_at(offsets, edges.T[1], -delta)

            # Sum offsets
            vcoordinates = numpy.ma.where(mask, vcoordinates + self._c4 * offsets, vcoordinates)

        eshapes, ecoordinates = self._edges.edges(vcoordinates, edges)
        return vcoordinates, eshapes, ecoordinates


class FruchtermanReingold(GraphLayout):
    """Compute a force directed graph layout using the 1991 algorithm of Fruchterman and Reingold.

    Parameters
    ----------
    edges: :class:`toyplot.layout.EdgeLayout` instance, optional
        The default will generate straight edges.
    area, temperature: numbers, optional
        Constants defined in the original paper.
    M: integer, optional
        Number of iterations to run the spring simulation.
    seed: integer, optional
        Random seed used to initialize vertex coordinates.
    """
    def __init__(self, edges=None, area=1, temperature=0.1, M=50, seed=1234):
        if edges is None:
            edges = StraightEdges()

        self._edges = edges
        self._area = area
        self._temperature = temperature
        self._M = M
        self._seed = seed

    def graph(self, vcoordinates, edges):
        generator = numpy.random.RandomState(seed=self._seed)
        # Setup parameters
        k = numpy.sqrt(self._area / len(vcoordinates))

        # Initialize coordinates
        mask = numpy.ma.getmaskarray(vcoordinates)
        vcoordinates = numpy.ma.where(mask, generator.uniform(-1, 1, size=vcoordinates.shape), vcoordinates)

        # Repeatedly apply attract / repel forces to the vertices
        vertices = numpy.column_stack(numpy.triu_indices(n=len(vcoordinates), k=1))
        for temperature in numpy.linspace(self._temperature, 0, self._M, endpoint=False):
            offsets = numpy.zeros_like(vcoordinates)

            # Repel
            a = vcoordinates[vertices.T[0]]
            b = vcoordinates[vertices.T[1]]
            delta = a - b
            distance = numpy.linalg.norm(delta, axis=1)[:, None]
            delta /= distance
            force = numpy.square(k) / distance
            delta *= force
            _add_at(offsets, vertices.T[0], +delta)
            _add_at(offsets, vertices.T[1], -delta)

            # Attract
            a = vcoordinates[edges.T[0]]
            b = vcoordinates[edges.T[1]]
            delta = b - a
            distance = numpy.linalg.norm(delta, axis=1)[:, None]
            delta /= distance
            force = numpy.square(distance) / k
            delta *= force
            _add_at(offsets, edges.T[0], +delta)
            _add_at(offsets, edges.T[1], -delta)

            # Limit offsets to the temperature
            distance = numpy.linalg.norm(offsets, axis=1)
            offsets /= distance[:, None]
            offsets *= numpy.minimum(temperature, distance)[:, None]

            # Sum offsets
            vcoordinates = numpy.ma.where(mask, vcoordinates + offsets, vcoordinates)

        eshapes, ecoordinates = self._edges.edges(vcoordinates, edges)
        return vcoordinates, eshapes, ecoordinates


class Buchheim(GraphLayout):
    """Compute a tree layout using the 2002 algorithm of Buchheim, Junger, and Leipert.

    Note: this layout currently ignores preexisting vertex coordinates.
    """
    def __init__(self, edges=None, basis=None):
        if edges is None:
            edges = StraightEdges()

        if basis is None:
            basis = [[1, 0], [0, -1]]

        self._edges = edges
        self._basis = numpy.array(basis)

    def graph(self, vcoordinates, edges):
        # Convert the graph to an adjacency list
        children = _adjacency_list(len(vcoordinates), edges)
        # Ensure we actually have a tree
        root, depth = _require_tree(children)

        # Get rid of the mask, it complicates things.
        vcoordinates = numpy.array(vcoordinates)

        # Convert our flat adjacency list into a hierarchy, to make the implementation easier.
        class Vertex(object):
            def __init__(self, vertex, parent=None, number=0, depth=0):
                self.vertex = vertex
                self.parent = parent
                self.number = number
                self.depth = depth
                self.children = [Vertex(child, self, number, depth+1) for number, child in enumerate(children[vertex])]
                self.mod = 0
                self.thread = None
                self.ancestor = self
                self.prelim = 0
                self.change = 0
                self.shift = 0

        # We follow Appendix A of the original paper as closely as possible here.
        distance = 1
        def FirstWalk(v):
            if not v.children: # v is a leaf
                v.prelim = 0
                if v.number: # v has a left sibling
                    v.prelim = v.parent.children[v.number-1].prelim + distance
            else: # v is not a leaf
                defaultAncestor = v.children[0] # leftmost child of v
                for w in v.children:
                    FirstWalk(w)
                    defaultAncestor = Apportion(w, defaultAncestor)
                ExecuteShifts(v)
                midpoint = 0.5 * (v.children[0].prelim + v.children[-1].prelim)
                if v.number: # v has a left sibling
                    v.prelim = v.parent.children[v.number-1].prelim + distance
                    v.mod = v.prelim - midpoint
                else:
                    v.prelim = midpoint

        def Apportion(v, defaultAncestor):
            if v.number: # v has a left sibling
                vip = vop = v
                vim = v.parent.children[v.number-1]
                vom = vip.parent.children[0]
                sip = vip.mod
                sop = vop.mod
                sim = vim.mod
                som = vom.mod
                while NextRight(vim) and NextLeft(vip):
                    vim = NextRight(vim)
                    vip = NextLeft(vip)
                    vom = NextLeft(vom)
                    vop = NextRight(vop)
                    vop.ancestor = v
                    shift = (vim.prelim + sim) - (vip.prelim + sip) + distance
                    if shift > 0:
                        MoveSubtree(Ancestor(vim, v, defaultAncestor), v, shift)
                        sip += shift
                        sop += shift
                    sim += vim.mod
                    sip += vip.mod
                    som += vom.mod
                    sop += vop.mod
                if NextRight(vim) and not NextRight(vop):
                    vop.thread = NextRight(vim)
                    vop.mod += sim - sop
                if NextLeft(vip) and not NextLeft(vom):
                    vom.thread = NextLeft(vip)
                    vom.mod += sip - som
                    defaultAncestor = v
            return defaultAncestor

        def NextLeft(v):
            if v.children:
                return v.children[0]
            else:
                return v.thread

        def NextRight(v):
            if v.children:
                return v.children[-1]
            else:
                return v.thread

        def MoveSubtree(wm, wp, shift):
            subtrees = wp.number - wm.number
            wp.change -= shift / subtrees
            wp.shift += shift
            wm.change += shift / subtrees
            wp.prelim += shift
            wp.mod += shift

        def ExecuteShifts(v):
            shift = 0
            change = 0
            for w in v.children:
                w.prelim += shift
                w.mod += shift
                change += w.change
                shift += w.shift + change

        def Ancestor(vim, v, defaultAncestor):
            if vim.ancestor in v.parent.children:
                return vim.ancestor
            else:
                return defaultAncestor

        def SecondWalk(v, m):
            vcoordinates[v.vertex][0] = v.prelim + m
            vcoordinates[v.vertex][1] = v.depth
            for w in v.children:
                SecondWalk(w, m + v.mod)

        r = Vertex(root)
        FirstWalk(r)
        SecondWalk(r, -r.prelim)

        vcoordinates = numpy.dot(vcoordinates, self._basis)

        eshapes, ecoordinates = self._edges.edges(vcoordinates, edges)
        return vcoordinates, eshapes, ecoordinates
