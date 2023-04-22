# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Provides data objects (marks) that are displayed on a :class:`canvas <toyplot.canvas.Canvas>`."""


import itertools
import logging

import custom_inherit
import numpy

import toyplot.color
import toyplot.marker
import toyplot.require


log = logging.getLogger(__name__)


##########################################################################
# Basic Toyplot marks

class Mark(object, metaclass=custom_inherit.DocInheritMeta(style="numpy_napoleon")):
    """Abstract interface for Toyplot marks.

    Marks are data objects that are added to a coordinate system for display on
    a :class:`canvas <toyplot.canvas.Canvas>`.  Marks carry no explicit visual
    representation of their own - it is up to the coordinate system and
    :ref:`rendering backend<backends>` to determine how to render the data.

    For example, a :class:`scatterplot <toyplot.mark.Point>` mark is
    rendered using points by a :class:`cartesian
    <toyplot.coordinates.Cartesian>` coordinate system, but could be rendered
    using lines by a hypothetical parallel coordinate system.
    """
    def __init__(self, annotation=False):
        self._annotation = False
        self.annotation = annotation

    @property
    def annotation(self):
        return self._annotation

    @annotation.setter
    def annotation(self, value):
        self._annotation = True if value else False

    def _finalize(self):
        return self

    def domain(self, axis): # pylint: disable=no-self-use
        """Return minimum and maximum domain values for the mark along the given axis.

        Parameters
        ----------
        axis: string, required
            Name of an axis along which to return domain values.

        Returns
        -------
        minimum: minimum domain value along the given axis, or `None`.
        maximum: maximum domain value along the given axis, or `None`.
        """
        return (None, None)

    def extents(self, axes): # pylint: disable=no-self-use
        """Return range extents for the mark using the given axes.

        Parameters
        ----------
        axes: sequence of strings, required
            Specifies the order in which domain coordinates must be returned.

        Returns
        -------
        coordinates: tuple containing arrays of coordinates, in the order specified by the `axes` parameter.
        extents: (left, right, top, bottom) tuple of arrays containing the extents of each datum in range-space, relative to the domain coordinates.
        """
        empty = numpy.array([])
        return tuple([empty] * len(axes)), tuple([empty] * 4)

    @property
    def markers(self): # pylint: disable=no-self-use
        """Return an ordered set of markers used by this mark, if any.

        Returns
        -------
        markers: list of :class:`toyplot.marker.Marker` objects.
        """
        return []

    def __format__(self, format_spec):
        return "".join([format(marker) for marker in self.markers])


class AxisLines(Mark):
    """Render multiple lines parallel to an axis.

    Do not create AxisLines instances directly.  Use factory methods such as
    :meth:`toyplot.coordinates.Cartesian.hlines` and :meth:`toyplot.coordinates.Cartesian.vlines` instead.
    """
    def __init__(
            self,
            coordinate_axes,
            table,
            coordinates,
            stroke,
            opacity,
            title,
            style,
            annotation,
        ):
        Mark.__init__(self, annotation)

        # 1 axis identifier
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=1)

        self._table = toyplot.require.instance(table, toyplot.data.Table)
        # 1 coordinate column
        self._coordinates = toyplot.require.table_keys(table, coordinates, length=1)
        # 1 stroke color column
        self._stroke = toyplot.require.table_keys(table, stroke, length=1)
        # 1 opacity column
        self._opacity = toyplot.require.table_keys(table, opacity, length=1)
        # 1 title column
        self._title = toyplot.require.table_keys(table, title, length=1)
        # Line style
        self._style = toyplot.style.require(style, allowed=toyplot.style.allowed.line)

    def domain(self, axis):
        if axis == self._coordinate_axes:
            return toyplot.data.minimax([self._table[self._coordinates[0]]])
        return (None, None)


class BarBoundaries(Mark):
    """Render multiple stacked bars defined by bar boundaries.

    Do not create BarBoundaries instances directly.  Use factory methods such as
    :func:`toyplot.bars` or :meth:`toyplot.coordinates.Cartesian.bars` instead.
    """
    def __init__(
            self,
            coordinate_axes,
            table,
            left,
            right,
            boundaries,
            fill,
            opacity,
            title,
            hyperlink,
            style,
            filename,
        ):
        Mark.__init__(self)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # 1 coordinate column
        self._left = toyplot.require.table_keys(table, left, length=1)
        # 1 coordinate column
        self._right = toyplot.require.table_keys(table, right, length=1)
        # N bar boundary columns
        self._boundaries = toyplot.require.table_keys(table, boundaries, min_length=2)
        # N-1 fill color columns
        self._fill = toyplot.require.table_keys(table, fill, length=len(boundaries) - 1)
        # N-1 opacity columns
        self._opacity = toyplot.require.table_keys(table, opacity, length=len(boundaries) - 1)
        # N-1 title columns
        self._title = toyplot.require.table_keys(table, title, length=len(boundaries) - 1)
        # N-1 hyperlink columns
        self._hyperlink = toyplot.require.table_keys(table, hyperlink, length=len(boundaries) - 1)
        # Bar style
        self._style = toyplot.style.require(style, allowed=toyplot.style.allowed.fill)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        if axis == self._coordinate_axes[0]:
            return toyplot.data.minimax([self._table[self._left[0]], self._table[self._right[0]]])
        if axis == self._coordinate_axes[1]:
            return toyplot.data.minimax([self._table[key] for key in self._boundaries])

    @property
    def markers(self):
        result = []

        for fill, opacity in zip(
                [self._table[key] for key in self._fill],
                [self._table[key] for key in self._opacity],
            ):
            result.append(toyplot.marker.create(shape="s", mstyle=toyplot.style.combine(
                {
                    "fill": toyplot.color.to_css(fill[0]),
                    "fill-opacity": opacity[0],
                },
                self._style,
                ),
            ))

        return result


class BarMagnitudes(Mark):
    """Render multiple stacked bars defined by bar magnitudes.

    Do not create BarMagnitudes instances directly.  Use factory methods such as
    :func:`toyplot.bars` or :meth:`toyplot.coordinates.Cartesian.bars` instead.
    """
    def __init__(
            self,
            coordinate_axes,
            table,
            left,
            right,
            baseline,
            magnitudes,
            fill,
            opacity,
            title,
            hyperlink,
            style,
            filename,
        ):
        Mark.__init__(self)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)
        # 1 coordinate column
        self._left = toyplot.require.table_keys(table, left, length=1)
        # 1 coordinate column
        self._right = toyplot.require.table_keys(table, right, length=1)
        # 1 baseline column
        self._baseline = toyplot.require.table_keys(table, baseline, length=1)
        # N bar magnitude columns
        self._magnitudes = toyplot.require.table_keys(table, magnitudes, min_length=1)
        # N fill color columns
        self._fill = toyplot.require.table_keys(table, fill, length=len(magnitudes))
        # N opacity columns
        self._opacity = toyplot.require.table_keys(table, opacity, length=len(magnitudes))
        # N title columns
        self._title = toyplot.require.table_keys(table, title, length=len(magnitudes))
        # N hyperlink columns
        self._hyperlink = toyplot.require.table_keys(table, hyperlink, length=len(magnitudes))
        # Bar style
        self._style = toyplot.style.require(style, allowed=toyplot.style.allowed.fill)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        if axis == self._coordinate_axes[0]:
            return toyplot.data.minimax([self._table[self._left[0]], self._table[self._right[0]]])
        if axis == self._coordinate_axes[1]:
            boundaries = numpy.column_stack([self._table[key] for key in self._magnitudes])
            boundaries = numpy.column_stack((self._table[self._baseline[0]], boundaries))
            boundaries = numpy.cumsum(boundaries, axis=1)
            return toyplot.data.minimax([boundaries])

    @property
    def markers(self):
        result = []

        for fill, opacity in zip(
                [self._table[key] for key in self._fill],
                [self._table[key] for key in self._opacity],
            ):
            result.append(toyplot.marker.create(shape="s", mstyle=toyplot.style.combine(
                {
                    "fill": toyplot.color.to_css(fill[0]),
                    "fill-opacity": opacity[0],
                },
                self._style,
                ),
            ))

        return result


class Ellipse(Mark):
    """Plot ellipses.

    Do not create Ellipse instances directly.  Use factory methods such as
    :meth:`toyplot.coordinates.Cartesian.ellipse` instead.
    """
    def __init__(
            self,
            coordinate_axes,
            table,
            x,
            y,
            rx,
            ry,
            angle,
            fill,
            opacity,
            title,
            style,
            filename,
        ):
        Mark.__init__(self)

        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        self._x = toyplot.require.table_keys(table, x, length=1)
        self._y = toyplot.require.table_keys(table, y, length=1)
        # 1 x-radius column
        self._rx = toyplot.require.table_keys(table, rx, length=1)
        # 1 y-radius column
        self._ry = toyplot.require.table_keys(table, ry, length=1)
        # 1 angle column
        self._angle = toyplot.require.table_keys(table, angle, length=1)
        # 1 fill color column
        self._fill = toyplot.require.table_keys(table, fill, length=1)
        # 1 opacity column
        self._opacity = toyplot.require.table_keys(table, opacity, length=1)
        # 1 title column
        self._title = toyplot.require.table_keys(table, title, length=1)
        # Ellipse style
        self._style = toyplot.style.require(style, allowed=toyplot.style.allowed.fill)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        x = self._table[self._x[0]]
        y = self._table[self._y[0]]
        rx = self._table[self._rx[0]]
        ry = self._table[self._ry[0]]
        theta = numpy.radians(self._table[self._angle[0]])

        u = numpy.column_stack((rx * numpy.cos(theta), rx * numpy.sin(theta)))
        v = numpy.column_stack((ry * numpy.cos(theta + numpy.pi / 2), ry * numpy.sin(theta + numpy.pi / 2)))

        dx = numpy.sqrt(u[:,0] * u[:,0] + v[:,0] * v[:,0])
        dy = numpy.sqrt(u[:,1] * u[:,1] + v[:,1] * v[:,1])

        if axis == self._coordinate_axes[0]:
            return toyplot.data.minimax((x - dx, x + dx))
        if axis == self._coordinate_axes[1]:
            return toyplot.data.minimax((y - dy, y + dy))


class FillBoundaries(Mark):
    """Render multiple stacked fill regions defined by boundaries.

    Do not create FillBoundaries instances directly.  Use factory methods such
    as :func:`toyplot.fill` or :meth:`toyplot.coordinates.Cartesian.fill` instead.
    """
    def __init__(
            self,
            coordinate_axes,
            table,
            position,
            boundaries,
            fill,
            opacity,
            title,
            style,
            annotation,
            filename,
        ):
        Mark.__init__(self, annotation)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)
        # 1 coordinate column
        self._position = toyplot.require.table_keys(table, position, length=1)
        # N fill boundary columns
        self._boundaries = toyplot.require.table_keys(table, boundaries, min_length=2)
        # N-1 fill colors
        self._fill = toyplot.require.vector(fill, length=len(boundaries) - 1)
        # N-1 opacities
        self._opacity = toyplot.require.scalar_vector(opacity, length=len(boundaries) - 1)
        # N-1 titles
        #self._title = toyplot.require.object_vector(title, length=len(boundaries) - 1)
        self._title = title
        # Fill style
        self._style = toyplot.style.require(style, allowed=toyplot.style.allowed.fill)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        if axis == self._coordinate_axes[0]:
            return toyplot.data.minimax([self._table[self._position[0]]])
        if axis == self._coordinate_axes[1]:
            return toyplot.data.minimax([self._table[key] for key in self._boundaries])

    @property
    def markers(self):
        result = []

        for fill, opacity in zip(
                self._fill,
                self._opacity,
            ):

            result.append(toyplot.marker.create(shape="s", mstyle=toyplot.style.combine(
                    {
                        "fill": toyplot.color.to_css(fill),
                        "fill-opacity": opacity,
                    },
                    self._style,
                ),
            ))

        return result


class FillMagnitudes(Mark):
    """Render multiple stacked fill regions defined by magnitudes.

    Do not create FillMagnitudes instances directly.  Use factory methods such
    as :func:`toyplot.fill` or :meth:`toyplot.coordinates.Cartesian.fill` instead.
    """
    def __init__(
            self,
            coordinate_axes,
            table,
            position,
            baseline,
            magnitudes,
            fill,
            opacity,
            title,
            style,
            annotation,
            filename,
        ):
        Mark.__init__(self, annotation)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # 1 coordinate column
        self._position = toyplot.require.table_keys(table, position, length=1)
        # 1 baseline column
        self._baseline = toyplot.require.table_keys(table, baseline, length=1)
        # N fill magnitude columns
        self._magnitudes = toyplot.require.table_keys(table, magnitudes)
        # N fill colors
        self._fill = toyplot.require.vector(fill, length=len(magnitudes))
        # N opacities
        self._opacity = toyplot.require.scalar_vector(opacity, length=len(magnitudes))
        # N titles
        #self._title = toyplot.require.object_vector(title, length=len(magnitudes))
        self._title = title
        # Fill style
        self._style = toyplot.style.require(style, allowed=toyplot.style.allowed.fill)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        if axis == self._coordinate_axes[0]:
            return toyplot.data.minimax([self._table[self._position[0]]])
        if axis == self._coordinate_axes[1]:
            boundaries = numpy.column_stack([self._table[key] for key in self._magnitudes])
            boundaries = numpy.column_stack((self._table[self._baseline[0]], boundaries))
            boundaries = numpy.cumsum(boundaries, axis=1)
            return toyplot.data.minimax([boundaries])

    @property
    def markers(self):
        result = []

        for fill, opacity in zip(
                self._fill,
                self._opacity,
            ):

            result.append(toyplot.marker.create(shape="s", mstyle=toyplot.style.combine(
                    {
                        "fill": toyplot.color.to_css(fill),
                        "fill-opacity": opacity,
                    },
                    self._style,
                ),
            ))

        return result


class Graph(Mark): # pragma: no cover
    """Plot a graph (collection of vertices and edges).

    Do not create Graph instances directly.  Use factory methods such as
    :meth:`toyplot.coordinates.Cartesian.graph` instead.
    """
    def __init__(
            self,
            coordinate_axes,
            ecolor,
            ecoordinates,
            efilename,
            eopacity,
            eshape,
            esource,
            estyle,
            etable,
            etarget,
            ewidth,
            hmarker,
            mmarker,
            mposition,
            tmarker,
            vcolor,
            vcoordinates,
            vfilename,
            vid,
            vlabel,
            vlshow,
            vlstyle,
            vmarker,
            vopacity,
            vsize,
            vstyle,
            vtable,
            vtitle,
        ):
        Mark.__init__(self)

        # D axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, min_length=1)

        self._vtable = toyplot.require.instance(vtable, toyplot.data.Table)
        # 1 vertex id column
        self._vid = toyplot.require.table_keys(vtable, vid, length=1)
        # 1 vertex label column
        self._vlabel = toyplot.require.table_keys(vtable, vlabel, length=1)
        # D coordinate columns
        self._vcoordinates = toyplot.require.table_keys(vtable, vcoordinates, length=len(self._coordinate_axes))
        # 1 vertex marker column
        self._vmarker = toyplot.require.table_keys(vtable, vmarker, length=1)
        # 1 vertex marker size column
        self._vsize = toyplot.require.table_keys(vtable, vsize, length=1)
        # 1 vertex marker color column
        self._vcolor = toyplot.require.table_keys(vtable, vcolor, length=1)
        # 1 marker opacity column
        self._vopacity = toyplot.require.table_keys(vtable, vopacity, length=1)
        # 1 vertex titles column
        self._vtitle = toyplot.require.table_keys(vtable, vtitle, length=1)
        # Vertex marker style
        self._vstyle = toyplot.style.require(vstyle, allowed=toyplot.style.allowed.marker)
        # Vertex marker label style
        self._vlstyle = toyplot.style.require(vlstyle, allowed=toyplot.style.allowed.text)
        # Draw vertex labels
        self._vlshow = vlshow
        # Export filename
        self._vfilename = toyplot.require.filename(vfilename)

        self._etable = toyplot.require.instance(etable, toyplot.data.Table)
        # 1 edge source column
        self._esource = toyplot.require.table_keys(etable, esource, length=1)
        # 1 edge target column
        self._etarget = toyplot.require.table_keys(etable, etarget, length=1)
        # 1 edge shape column
        self._eshape = toyplot.require.table_keys(etable, eshape, length=1)

        ecoordinate_count = 0
        for shape in self._etable[self._eshape[0]]:
            for segment in shape:
                if segment == "M":
                    ecoordinate_count += 1
                elif segment == "L":
                    ecoordinate_count += 1
                elif segment == "Q":
                    ecoordinate_count += 2
                elif segment == "C":
                    ecoordinate_count += 3
                else:
                    raise ValueError("Unknown edge shape segment: %s" % segment)

        # C x D edge coordinate columns
        self._ecoordinates = toyplot.require.scalar_matrix(ecoordinates, rows=ecoordinate_count, columns=len(self._coordinate_axes))

        # 1 edge color column
        self._ecolor = toyplot.require.table_keys(etable, ecolor, length=1)
        # 1 edge width column
        self._ewidth = toyplot.require.table_keys(etable, ewidth, length=1)
        # 1 edge opacity column
        self._eopacity = toyplot.require.table_keys(etable, eopacity, length=1)
        # Edge style
        self._estyle = toyplot.style.require(estyle, allowed=toyplot.style.allowed.line)
        # Export filename
        self._efilename = toyplot.require.filename(efilename)
        # 1 head marker column
        self._hmarker = toyplot.require.table_keys(etable, hmarker, length=1)
        # 1 middle marker column
        self._mmarker = toyplot.require.table_keys(etable, mmarker, length=1)
        # 1 middle marker position column
        self._mposition = toyplot.require.table_keys(etable, mposition, length=1)
        # 1 tail marker column
        self._tmarker = toyplot.require.table_keys(etable, tmarker, length=1)

    def domain(self, axis):
        index = numpy.flatnonzero(self._coordinate_axes == axis)[0]
        return toyplot.data.minimax([self._vtable[self._vcoordinates[index]], self._ecoordinates[:, index]])


    @property
    def vcount(self):
        """Return the number of vertices in the graph."""
        return len(self._vtable)

    @property
    def vids(self):
        """Returns the graph vertex identifiers."""
        return self._vtable[self._vid[0]]

    @property
    def vcoordinates(self):
        """Return the graph vertex coordinates."""
        return numpy.column_stack([self._vtable[column] for column in self._vcoordinates])

    @property
    def ecount(self):
        """Return the number of edges in the graph."""
        return len(self._etable)

    @property
    def esources(self):
        return self._etable[self._esource[0]]

    @property
    def etargets(self):
        return self._etable[self._etarget[0]]

    @property
    def eshapes(self):
        return self._etable[self._eshape[0]]

    @property
    def ecoordinates(self):
        return self._ecoordinates

    @property
    def edges(self):
        """Return the graph edges as a :math:`E \\times 2` matrix of source, target indices."""
        return numpy.column_stack((self._etable[self._esource[0]], self._etable[self._etarget[0]]))


class Image(Mark):
    """Plot a bitmap image.

    Do not create Image instances directly.  Use factory methods such as
    :func:`toyplot.image` and :func:`toyplot.canvas.Canvas.image` instead.
    """
    def __init__(
            self,
            xmin_range,
            xmax_range,
            ymin_range,
            ymax_range,
            data,
        ):
        Mark.__init__(self)

        self._xmin_range = xmin_range
        self._xmax_range = xmax_range
        self._ymin_range = ymin_range
        self._ymax_range = ymax_range

        data = numpy.atleast_3d(data)

        if data.ndim != 3:
            raise ValueError("Image must be a 1D, 2D or 3D array.") # pragma: no cover
        if data.shape[2] < 1 or data.shape[2] > 4:
            raise ValueError("Image must contain 1, 2, 3, or 4 channels.") # pragma: no cover
        if issubclass(data.dtype.type, (numpy.object_, numpy.complexfloating, numpy.flexible)) and data.dtype != toyplot.color.dtype:
            raise ValueError("Unsupported image dtype: %s" % data.dtype) # pragma: no cover

        self._data = data


class Plot(Mark):
    """Plot multiple bivariate data series using lines and/or markers.

    Do not create Plot instances directly.  Use factory methods such as
    :func:`toyplot.plot`, :func:`toyplot.scatterplot`,
    :meth:`toyplot.coordinates.Cartesian.plot` and
    :meth:`toyplot.coordinates.Cartesian.scatterplot` instead.
    """
    def __init__(
            self,
            coordinate_axes,
            table,
            coordinates,
            series,
            stroke,
            stroke_width,
            stroke_opacity,
            stroke_title,
            marker,
            msize,
            mfill,
            mstroke,
            mopacity,
            mtitle,
            style,
            mstyle,
            mlstyle,
            filename,
        ):
        Mark.__init__(self)

        # 2 axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, length=2)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # 1 coordinate column
        self._coordinates = toyplot.require.table_keys(table, coordinates, length=1)
        # N coordinate columns
        self._series = toyplot.require.table_keys(table, series, min_length=1)
        # N stroke colors
        self._stroke = toyplot.require.vector(stroke, length=len(series))
        # N stroke widths
        self._stroke_width = toyplot.require.scalar_vector(stroke_width, length=len(series))
        # N stroke opacities
        self._stroke_opacity = toyplot.require.scalar_vector(stroke_opacity, length=len(series))
        # N stroke titles
        self._stroke_title = stroke_title
        # N marker columns
        self._marker = toyplot.require.table_keys(table, marker, length=len(series))
        # N marker size columns
        self._msize = toyplot.require.table_keys(table, msize, length=len(series))
        # N marker fill color columns
        self._mfill = toyplot.require.table_keys(table, mfill, length=len(series))
        # N marker stroke color columns
        self._mstroke = toyplot.require.table_keys(table, mstroke, length=len(series))
        # N marker opacity columns
        self._mopacity = toyplot.require.table_keys(table, mopacity, length=len(series))
        # N marker title columns
        self._mtitle = toyplot.require.table_keys(table, mtitle, length=len(series))
        # Line style
        self._style = toyplot.style.require(style, allowed=toyplot.style.allowed.line)
        # Marker style
        self._mstyle = toyplot.style.require(mstyle, allowed=toyplot.style.allowed.marker)
        # Marker label style
        self._mlstyle = toyplot.style.require(mlstyle, allowed=toyplot.style.allowed.text)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        if axis == self._coordinate_axes[0]:
            return toyplot.data.minimax([self._table[self._coordinates[0]]])
        if axis == self._coordinate_axes[1]:
            return toyplot.data.minimax([self._table[key] for key in self._series])

    @property
    def markers(self):
        result = []

        for stroke, stroke_width, stroke_opacity in zip(self._stroke.T, self._stroke_width.T, self._stroke_opacity.T):
            result.append(toyplot.marker.create(shape="/", mstyle=toyplot.style.combine(
                    {
                        "fill": toyplot.color.to_css(stroke),
                        "stroke": toyplot.color.to_css(stroke),
                        "stroke-width": stroke_width,
                        "stroke-opacity": stroke_opacity,
                    },
                    self._style,
                ),
            ))

        return result


class Point(Mark):
    """Represent one or more data series as points in an arbitrary-dimension space.

    Do not create Point instances directly.  Use factory methods such as
    :func:`toyplot.scatterplot` and :meth:`toyplot.coordinates.Cartesian.scatterplot`
    instead.
    """
    def __init__(
            self,
            coordinate_axes,
            coordinates,
            filename,
            marker,
            mfill,
            mhyperlink,
            mlstyle,
            mopacity,
            msize,
            mstroke,
            mstyle,
            mtitle,
            table,
        ):
        Mark.__init__(self)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # We require at last one coordinate dimension (number of dimensions = D)
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, min_length=1)
        D = len(self._coordinate_axes)

        # We require D coordinate columns for each series (number of series = N)
        self._coordinates = toyplot.require.table_keys(table, coordinates, modulus=D)
        N = len(self._coordinates) / D

        # We require 1 export filename
        self._filename = toyplot.require.filename(filename)
        # We require 1 marker style
        self._mstyle = toyplot.style.require(mstyle, allowed=toyplot.style.allowed.marker)
        # We require 1 marker label style
        self._mlstyle = toyplot.style.require(mlstyle, allowed=toyplot.style.allowed.text)

        # We require N marker columns
        self._marker = toyplot.require.table_keys(table, marker, length=N)
        # We require N marker fill color columns
        self._mfill = toyplot.require.table_keys(table, mfill, length=N)
        # We require N marker hyperlink columns
        self._mhyperlink = toyplot.require.table_keys(table, mhyperlink, length=N)
        # We require N marker opacity columns
        self._mopacity = toyplot.require.table_keys(table, mopacity, length=N)
        # We require N marker size columns
        self._msize = toyplot.require.table_keys(table, msize, length=N)
        # We require N marker stroke color columns
        self._mstroke = toyplot.require.table_keys(table, mstroke, length=N)
        # We require N marker title columns
        self._mtitle = toyplot.require.table_keys(table, mtitle, length=N)

    def domain(self, axis):
        columns = [coordinate_column for coordinate_axis, coordinate_column in zip(itertools.cycle(self._coordinate_axes), self._coordinates) if coordinate_axis == axis]
        return toyplot.data.minimax([self._table[column] for column in columns])

    @property
    def markers(self):
        result = []

        for marker, mfill, mstroke, mopacity in zip(
                [self._table[key] for key in self._marker],
                [self._table[key] for key in self._mfill],
                [self._table[key] for key in self._mstroke],
                [self._table[key] for key in self._mopacity],
            ):

            for dmarker, dfill, dstroke, dopacity in zip(marker, mfill, mstroke, mopacity):
                mstyle = toyplot.style.combine(
                {
                    "fill": toyplot.color.to_css(dfill),
                    "stroke": toyplot.color.to_css(dstroke),
                    "opacity": dopacity,
                },
                self._mstyle
                )

                dmarker = toyplot.marker.create(mstyle=mstyle, lstyle=self._mlstyle) + toyplot.marker.convert(dmarker)

                result.append(dmarker)
                break

        return result


class Range(Mark):
    """Represents axis-aligned ranges (min/max pairs) in arbitrary-dimensional space.

    Do not create Range instances directly.  Use factory methods such as
    :meth:`toyplot.coordinates.Cartesian.rects` instead.
    """
    def __init__(
            self,
            coordinate_axes,
            coordinates,
            filename,
            fill,
            opacity,
            style,
            table,
            title,
        ):
        Mark.__init__(self)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # We require at least one coordinate dimension (number of dimensions = D)
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, min_length=1)
        D = len(self._coordinate_axes)

        # We require 2 * D coordinate columns for each series (number of series = N)
        self._coordinates = toyplot.require.table_keys(table, coordinates, modulus=2 * D)
        N = len(self._coordinates) / (2 * D)

        # We require 1 export filename
        self._filename = toyplot.require.filename(filename)
        # We require 1 fill style
        self._style = toyplot.style.require(style, allowed=toyplot.style.allowed.fill)

        # We require N fill color columns
        self._fill = toyplot.require.table_keys(table, fill, length=N)
        # We require N opacity columns
        self._opacity = toyplot.require.table_keys(table, opacity, length=N)
        # We require N title columns
        self._title = toyplot.require.table_keys(table, title, length=N)

    def domain(self, axis):
        index = numpy.flatnonzero(self._coordinate_axes == axis)[0]
        return toyplot.data.minimax((self._table[self._coordinates[index * 2 + 0]], self._table[self._coordinates[index * 2 + 1]]))


class Text(Mark):
    """Render text.

    Do not create Text instances directly.  Use factory methods such as
    :meth:`toyplot.canvas.Canvas.text` or :meth:`toyplot.coordinates.Cartesian.text` instead.
    """
    def __init__(
            self,
            coordinate_axes,
            table,
            coordinates,
            text,
            angle,
            fill,
            opacity,
            title,
            style,
            annotation,
            filename,
        ):
        Mark.__init__(self, annotation)

        # D axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, min_length=1)

        self._table = toyplot.require.instance(table, toyplot.data.Table)
        # D coordinate columns
        self._coordinates = toyplot.require.table_keys(table, coordinates, length=len(self._coordinate_axes))
        # 1 text column
        self._text = toyplot.require.table_keys(table, text, length=1)
        # 1 angle column
        self._angle = toyplot.require.table_keys(table, angle, length=1)
        # 1 fill color column
        self._fill = toyplot.require.table_keys(table, fill, length=1)
        # 1 opacity column
        self._opacity = toyplot.require.table_keys(table, opacity, length=1)
        # 1 title column
        self._title = toyplot.require.table_keys(table, title, length=1)
        # Text style
        self._style = toyplot.style.combine(
            {
                "-toyplot-vertical-align": "middle",
                "font-family": "helvetica",
                "font-size": "12px",
                "font-weight": "normal",
                "stroke": "none",
                "text-anchor": "middle",
            },
            toyplot.style.require(style, allowed=toyplot.style.allowed.text),
            )
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        for index, coordinate_axis in enumerate(self._coordinate_axes):
            if coordinate_axis == axis:
                return toyplot.data.minimax(self._table[self._coordinates[index]])

    def extents(self, axes):
        axis_map = {key: index for index, key in enumerate(self._coordinate_axes)}
        coordinates = tuple([self._table[self._coordinates[axis_map[axis]]] for axis in axes])
        extents = toyplot.text.extents(self._table[self._text[0]], self._table[self._angle[0]], self._style)
        return coordinates, extents
