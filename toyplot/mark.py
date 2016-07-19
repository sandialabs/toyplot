# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import itertools
import numpy
import toyplot.color
import toyplot.require


##########################################################################
# Basic Toyplot marks

class Mark(object):

    """Base class for all Toyplot marks.
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

    def domain(self, axis):
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

    def extents(self, axes):
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
        self._style = toyplot.require.style(style, allowed=toyplot.require.style.line)

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
        # Bar style
        self._style = toyplot.require.style(style, allowed=toyplot.require.style.fill)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        if axis == self._coordinate_axes[0]:
            return toyplot.data.minimax([self._table[self._left[0]], self._table[self._right[0]]])
        if axis == self._coordinate_axes[1]:
            return toyplot.data.minimax([self._table[key] for key in self._boundaries])


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
        # Bar style
        self._style = toyplot.require.style(style, allowed=toyplot.require.style.fill)
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
        self._style = toyplot.require.style(style, allowed=toyplot.require.style.fill)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        if axis == self._coordinate_axes[0]:
            return toyplot.data.minimax([self._table[self._position[0]]])
        if axis == self._coordinate_axes[1]:
            return toyplot.data.minimax([self._table[key] for key in self._boundaries])

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
        self._style = toyplot.require.style(style, allowed=toyplot.require.style.fill)
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


class Graph(Mark): # pragma: no cover

    """Plot a graph (collection of vertices and edges).

    Do not create Graph instances directly.  Use factory methods such as
    :meth:`toyplot.coordinates.Cartesian.graph` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            vtable,
            vid,
            vlabel,
            vcoordinates,
            vmarker,
            vsize,
            vcolor,
            vopacity,
            vtitle,
            vstyle,
            vlstyle,
            vlshow,
            etable,
            esource,
            etarget,
            eshape,
            ecoordinates,
            ecolor,
            ewidth,
            eopacity,
            estyle,
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
        self._vstyle = toyplot.require.style(vstyle, allowed=toyplot.require.style.marker)
        # Vertex marker label style
        self._vlstyle = toyplot.require.style(vlstyle, allowed=toyplot.require.style.text)
        # Draw vertex labels
        self._vlshow = vlshow

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
        self._estyle = toyplot.require.style(estyle, allowed=toyplot.require.style.line)

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
            raise ValueError("Image must be a 1D, 2D or 3D array.")
        if data.shape[2] < 1 or data.shape[2] > 4:
            raise ValueError("Image must contain 1, 2, 3, or 4 channels.")
        if issubclass(data.dtype.type, (numpy.object_, numpy.complexfloating, numpy.flexible)) and data.dtype != toyplot.color.dtype:
            raise ValueError("Unsupported image dtype: %s" % data.dtype)

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
        self._style = toyplot.require.style(style, allowed=toyplot.require.style.line)
        # Marker style
        self._mstyle = toyplot.require.style(mstyle, allowed=toyplot.require.style.marker)
        # Marker label style
        self._mlstyle = toyplot.require.style(mlstyle, allowed=toyplot.require.style.text)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        if axis == self._coordinate_axes[0]:
            return toyplot.data.minimax([self._table[self._coordinates[0]]])
        if axis == self._coordinate_axes[1]:
            return toyplot.data.minimax([self._table[key] for key in self._series])


class Rect(Mark):

    """Plot axis-aligned rectangles.

    Do not create Rect instances directly.  Use factory methods such as
    :meth:`toyplot.coordinates.Cartesian.rects` instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            left,
            right,
            top,
            bottom,
            fill,
            opacity,
            title,
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
        # 1 coordinate column
        self._top = toyplot.require.table_keys(table, top, length=1)
        # 1 coordinate column
        self._bottom = toyplot.require.table_keys(table, bottom, length=1)
        # 1 fill color column
        self._fill = toyplot.require.table_keys(table, fill, length=1)
        # 1 opacity column
        self._opacity = toyplot.require.table_keys(table, opacity, length=1)
        # 1 title column
        self._title = toyplot.require.table_keys(table, title, length=1)
        # Rectangle style
        self._style = toyplot.require.style(style, allowed=toyplot.require.style.fill)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        if axis == self._coordinate_axes[0]:
            return toyplot.data.minimax([self._table[self._left[0]], self._table[self._right[0]]])
        if axis == self._coordinate_axes[1]:
            return toyplot.data.minimax([self._table[self._top[0]], self._table[self._bottom[0]]])


class Scatterplot(Mark):

    """Plot multivariate data series using markers.

    Do not create Scatterplot instances directly.  Use factory methods such as
    :func:`toyplot.scatterplot` and :meth:`toyplot.coordinates.Cartesian.scatterplot`
    instead.
    """

    def __init__(
            self,
            coordinate_axes,
            table,
            coordinates,
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

        # D axis identifiers
        self._coordinate_axes = toyplot.require.string_vector(coordinate_axes, min_length=1)
        D = len(self._coordinate_axes)

        self._table = toyplot.require.instance(table, toyplot.data.Table)

        # D * N coordinate columns
        self._coordinates = toyplot.require.table_keys(table, coordinates, modulus=D)
        N = len(self._coordinates) / D

        # N marker columns
        self._marker = toyplot.require.table_keys(table, marker, length=N)
        # N marker size columns
        self._msize = toyplot.require.table_keys(table, msize, length=N)
        # N marker fill color columns
        self._mfill = toyplot.require.table_keys(table, mfill, length=N)
        # N marker stroke color columns
        self._mstroke = toyplot.require.table_keys(table, mstroke, length=N)
        # N marker opacity columns
        self._mopacity = toyplot.require.table_keys(table, mopacity, length=N)
        # N marker title columns
        self._mtitle = toyplot.require.table_keys(table, mtitle, length=N)
        # Global style
        self._style = toyplot.require.style(style, allowed=set())
        # Marker style
        self._mstyle = toyplot.require.style(mstyle, allowed=toyplot.require.style.marker)
        # Marker label style
        self._mlstyle = toyplot.require.style(mlstyle, allowed=toyplot.require.style.text)
        # Export filename
        self._filename = toyplot.require.filename(filename)

    def domain(self, axis):
        columns = [coordinate_column for coordinate_axis, coordinate_column in zip(itertools.cycle(self._coordinate_axes), self._coordinates) if coordinate_axis == axis]
        return toyplot.data.minimax([self._table[column] for column in columns])


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
                "alignment-baseline": "middle",
                "font-size": "12px",
                "font-weight": "normal",
                "stroke": "none",
                "text-anchor": "middle",
            },
            toyplot.require.style(style, allowed=toyplot.require.style.text),
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


##########################################################################
# More specialized marks

class Legend(Mark):

    """Render a figure legend (a collection of markers and labels).

    Do not create Legend instances directly.  Use factory methods such as
    :meth:`toyplot.canvas.Canvas.legend` or :meth:`toyplot.coordinates.Cartesian.legend` instead.
    """

    def __init__(self, xmin, xmax, ymin, ymax, entries, style, lstyle):
        Mark.__init__(self)
        self._xmin = xmin
        self._xmax = xmax
        self._ymin = ymin
        self._ymax = ymax
        self._gutter = 10
        self._entries = entries
        # Styles the box surrounding the legend
        self._style = toyplot.style.combine(
            {
                "fill": "none",
                "stroke": "none",
            },
            toyplot.require.style(style, allowed=toyplot.require.style.fill),
            )
        # Styles the legend labels
        self._lstyle = toyplot.style.combine(
            {
                "alignment-baseline": "middle",
                "font-size":"12px",
                "stroke":"none",
            },
            toyplot.require.style(lstyle, allowed=toyplot.require.style.text),
            )


