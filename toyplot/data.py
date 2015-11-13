# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import itertools
import numbers
import numpy
import toyplot.color
import toyplot.compatibility
import xml.etree.ElementTree as xml


def contiguous(a):
    """Split an array into a collection of contiguous ranges.
    """
    i = 0
    begin = []
    end = []
    values = []
    for (value, group) in itertools.groupby(numpy.array(a).ravel()):
        begin.append(i)
        end.append(i + len(list(group)))
        values.append(value)
        i = end[-1]
    return numpy.array(begin), numpy.array(end), numpy.array(values)


class Table(object):

    """Encapsulates an ordered, heterogeneous collection of labelled data series.
    """

    def __init__(self, data=None):
        self._columns = collections.OrderedDict()
        self._metadata = collections.defaultdict(dict)

        if data is not None:
            # Input data for which an explicit column ordering is known.
            if isinstance(data, (
                    collections.OrderedDict,
                    toyplot.data.Table,
                    numpy.lib.npyio.NpzFile,
                )):
                for key in data.keys():
                    self[key] = data[key]
                return
            # Input data for which an explicit column ordering is not known.
            if isinstance(data, (dict, collections.Mapping)):
                for key in sorted(data.keys()):
                    self[key] = data[key]
                return
            # Input data based on sequences.
            if isinstance(data, (list, collections.Sequence)):
                for key, values in data:
                    self[key] = values
                return
            # Input data based on numpy arrays.
            if isinstance(data, numpy.ndarray):
                if data.ndim == 2:
                    for column_index in numpy.arange(data.shape[1]):
                        self["C%s" % column_index] = data[:, column_index]
                else:
                    raise ValueError(
                        "Only two-dimensional arrays are allowed.")
                return
            # Input data based on Pandas data structures.
            try:
                import pandas
                if isinstance(data, pandas.DataFrame):
                    for key in data.keys():
                        self[key] = data[key]
                    return
            except:
                pass

            raise ValueError("Unsupported data type: %s" % type(data))

    def __getitem__(self, index):
        # Return a single column by name
        if isinstance(index, toyplot.compatibility.string_type):
            return self._columns[index]
        # Return a single row by index
        if isinstance(index, numbers.Integral):
            index = slice(index, index + 1)
        return Table(collections.OrderedDict(
            [(key, self._columns[key][index]) for key in self._columns.keys()]))

    def __setitem__(self, key, value):
        if not isinstance(key, toyplot.compatibility.string_type):
            raise ValueError("Column name '%s' must be a string." % key)
        key = toyplot.compatibility.unicode_type(key)
        value = numpy.ma.array(value)
        if value.ndim != 1:
            raise ValueError("Only 1D arrays are allowed.")
        for column in self._columns.values():
            if column.shape != value.shape:
                raise ValueError(
                    "Expected %s values, received %s." %
                    (column.shape[0], value.shape[0]))
        self._columns[key] = value

    def __delitem__(self, key):
        return self._columns.__delitem__(key)

    def __len__(self):
        return list(self._columns.values())[0].shape[0] if len(self._columns) else 0

    def _repr_html_(self):
        root_xml = xml.Element(
            "table",
            style="border-collapse:collapse; border:none; color: %s" %
            toyplot.color.near_black)
        root_xml.set("class", "toyplot-data-Table")
        header_xml = xml.SubElement(
            root_xml,
            "tr",
            style="border:none;border-bottom:1px solid %s" %
            toyplot.color.near_black)
        for name in self._columns.keys():
            xml.SubElement(
                header_xml,
                "th",
                style="text-align:left;border:none;padding-right:1em;").text = toyplot.compatibility.unicode_type(name)

        iterators = [iter(column) for column in self._columns.values()]
        for row_index in numpy.arange(len(self)):
            for index, iterator in enumerate(iterators):
                value = next(iterator)
                if index == 0:
                    row_xml = xml.SubElement(
                        root_xml, "tr", style="border:none")
                xml.SubElement(
                    row_xml,
                    "td",
                    style="border:none;padding-right:1em;").text = toyplot.compatibility.unicode_type(value)

        return toyplot.compatibility.unicode_type(xml.tostring(root_xml, encoding="utf-8", method="html"), encoding="utf-8")

    @property
    def shape(self):
        """Return the shape (number of rows and columns) of the table.

        Returns
        -------
        shape: (number of rows, number of columns) tuple.
        """
        return (
            list(self._columns.values())[0].shape[0] if len(self._columns) else 0,
            len(self._columns),
        )

    def items(self):
        """Return the table names and columns, in column order.

        Returns
        -------
        items: sequence of (name, column) tuples.
        """
        return self._columns.items()

    def keys(self):
        """Return the table column names, in column order.

        Returns
        -------
        keys: sequence of string column names.
        """
        return self._columns.keys()

    def values(self):
        """Return the table columns, in column order.

        Returns
        -------
        values: sequence of numpy.ndarray columns.
        """
        return self._columns.values()

    def columns(self, keys):
        """Return a subset of the table's columns.

        Parameters
        ----------
        keys: sequence of string column names.

        Returns
        -------
        table: :class:`toyplot.data.Table` containing the requested columns.
        """
        return Table(
            collections.OrderedDict([(key, self._columns[key]) for key in keys]))

    def metadata(self, column):
        """Return metadata for one of the table's columns.

        Parameters
        ----------
        column: string.
          The name of an existing column.

        Returns
        -------
        metadata: dict containing key-value pairs.
        """
        if column not in self._columns:
            raise ValueError("Unknown column name '%s'" % column)
        return self._metadata[column]

    def rows(self, index):
        """Return a subset of the table's rows.

        Parameters
        ----------
        index: integer row index, or a slice.

        Returns
        -------
        table: :class:`toyplot.data.Table` containing the requested rows.
        """
        if isinstance(index, numbers.Integral):
            index = slice(index, index + 1)
        return Table(collections.OrderedDict(
            [(key, self._columns[key][index]) for key in self._columns.keys()]))

    def matrix(self):
        """Convert the table to a matrix (2D numpy array).

        The data type of the returned array is chosen based on the types of the
        columns within the table.  Tables containing a homogeneous set of column
        types will return an array of the the same type.  If the table contains one
        or more string columns, the results will be an array of strings.

        Returns
        -------
        matrix: :class:`numpy.ma.array` with two dimensions.
        """
        return numpy.ma.column_stack(list(self._columns.values()))


def read_csv(fobj):
    """Load a CSV (delimited text) file.

    Parameters
    ----------
    fobj: file-like object or string, required
      The file to read.  Use a string filepath, an open file, or a file-like object.

    Returns
    -------
    table: :class:`toyplot.data.Table`

    Notes
    -----
    read_csv() is a simple tool for use in demos and tutorials.  For more full-featured
    delimited text parsing, you should consider the :mod:`csv` module included in the
    Python standard library, or functionality provided by `numpy` or `Pandas`.
    """
    import csv
    if isinstance(fobj, toyplot.compatibility.string_type):
        fobj = open(fobj, "r")
    rows = [row for row in csv.reader(fobj)]
    columns = zip(*rows)
    return Table(collections.OrderedDict(
        [(column[0], column[1:]) for column in columns]))
