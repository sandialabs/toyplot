# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Classes and functions for working with raw data."""


import collections
import itertools
import numbers
import os
import sys
import xml.etree.ElementTree as xml

import numpy

import toyplot.color

_data_dir = os.path.abspath(os.path.dirname(__file__))

def minimax(items):
    """Compute the minimum and maximum of an arbitrary collection of scalar- or array-like items.

    The `items` parameter must be an iterable containing any combination of
    `None`, scalars, numpy arrays, or numpy masked arrays.  None, NaN, masked
    values, and empty arrays are all handled correctly.  Returns `(None, None)`
    if the inputs don't contain any usable values.

    Returns
    -------
    min: minimum value of the input arrays, or None.
    max: maximum value of the input arrays, or None.
    """
    group_min = None
    group_max = None

    for item in items:
        item_min = None
        item_max = None
        if isinstance(item, toyplot.data.Table):
            raise ValueError("toyplot.data.Table is not allowed.") # pragma: no cover
        elif isinstance(item, numpy.ma.MaskedArray):
            pass
        elif isinstance(item, numpy.ndarray):
            item = numpy.ma.array(item)
        elif item is None:
            item = numpy.ma.array([])
        else:
            item = numpy.ma.array([item])

        # Ignore null values
        selection = numpy.ma.getmaskarray(item)
        # Ignore NaN values
        if issubclass(item.dtype.type, numpy.number):
            selection = numpy.logical_or(selection, numpy.isnan(item).data)
        selection = numpy.logical_not(selection)
        if numpy.count_nonzero(selection):
            item_min = item[selection].min()
            item_max = item[selection].max()

        if group_min is None:
            group_min = item_min
        else:
            if item_min is not None:
                group_min = min(group_min, item_min)

        if group_max is None:
            group_max = item_max
        else:
            if item_max is not None:
                group_max = max(group_max, item_max)

    return group_min, group_max


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

    Parameters
    ----------
    data: (data series, optional)
        You may initialize a toyplot.data.Table with any of the following:

        * None (the default) - creates an empty table (a table without any columns).
        * :class:`toyplot.data.Table` - creates a copy of the given table.
        * :class:`collections.OrderedDict` - creates a column for each key-value pair in the input, in the same order.  Each value must be implicitly convertable to a numpy masked array, and every value must contain the same number of items.
        * object returned when loading a `.npz` file with :func:`numpy.load` - creates a column for each key-value pair in the given file, in the same order.  Each array in the input file must contain the same number of items.
        * :class:`dict` / :class:`collections.abc.Mapping` - creates a column for each key-value pair in the input, sorted by key in lexicographical order.  Each value must be implicitly convertable to a numpy masked array, and every value must contain the same number of items.
        * :class:`list` / :class:`collections.abc.Sequence` - creates a column for each key-value tuple in the input sequence, in the same order.  Each value must be implicitly convertable to a numpy masked array, and every value must contain the same number of items.
        * :class:`numpy.ndarray` - creates a column for each column in a numpy matrix (2D array).  The order of the columns is maintained, and each column is assigned a unique name.
        * :class:`pandas.DataFrame` - creates a column for each column in a `Pandas <http://pandas.pydata.org>`_ data frame.  The order of the columns is maintained.

    index: bool or string, optional
        Controls whether to convert a `Pandas <http://pandas.pydata.org>`_ data
        frame index to columns in the resulting table.  Use index=False (the
        default) to leave the data frame index out of the table.  Use
        index=True to include the index in the table, using default column
        names (hierarchical indices will be stored in the table using multiple
        columns).  Use index="format string" to include the index and control
        how the index column names are generated.  The given format string can
        use positional `{}` / `{0}` or keyword `{index}` arguments to
        incorporate a zero-based index id into the column names.
    """

    def __init__(self, data=None, index=False):
        self._columns = collections.OrderedDict()
        self._metadata = collections.defaultdict(dict)

        if data is not None:
            keys = None
            values = None

            # Input data for which an explicit column ordering is known.
            if isinstance(data, (
                    collections.OrderedDict,
                    toyplot.data.Table,
                    numpy.lib.npyio.NpzFile,
                )):
                keys = [key for key in data.keys()]
                values = [data[key] for key in keys]
            # Input data for which an explicit column ordering is not known.
            elif isinstance(data, (dict, collections.abc.Mapping)):
                keys = [key for key in sorted(data.keys())]
                values = [data[key] for key in keys]
            # Input data based on sequences.
            elif isinstance(data, (list, collections.abc.Sequence)):
                keys = [key for key, value in data]
                values = [value for key, value in data]
            # Input data based on numpy arrays.
            elif isinstance(data, numpy.ndarray):
                if data.ndim != 2:
                    raise ValueError(
                        "Only two-dimensional arrays are allowed.")
                keys = [str(i) for i in numpy.arange(data.shape[1])]
                values = [data[:, i] for i in numpy.arange(data.shape[1])]
            # Input data based on Pandas data structures.
            elif "pandas" in sys.modules:
                import pandas
                if isinstance(data, pandas.DataFrame):
                    keys = [str(data.iloc[:, i].name) for i in range(data.shape[1])]
                    values = [data.iloc[:, i] for i in range(data.shape[1])]

                    if index:
                        key_format = "index{}" if index == True else index
                        keys = [key_format.format(i, index=i) for i in range(data.index.nlevels)] + keys
                        values = [data.index.get_level_values(i) for i in range(data.index.nlevels)] + values

            if keys is None or values is None:
                raise ValueError("Can't create a toyplot.data.Table from an instance of %s" % type(data))

            # Get the set of unique keys, so we can see if there are any duplicates.
            keys = numpy.array(keys, dtype="object")
            key_counter = collections.Counter(keys)
            key_dictionary = numpy.array(list(key_counter.keys()))
            key_counts = numpy.array(list(key_counter.values()))

            if numpy.any(key_counts > 1):
                toyplot.log.warning("Altering duplicate column names to make them unique.")

            # "Reserve" all of the keys that aren't duplicated.
            reserved_keys = set([key for key, count in zip(key_dictionary, key_counts) if count == 1])
            # Now, iterate through the keys that do contain duplicates, altering them to make them unique,
            # while ensuring that the unique versions don't conflict with reserved keys.
            for key, count in zip(key_dictionary, key_counts):
                if count == 1:
                    continue

                suffix = 1
                for i in numpy.flatnonzero(keys == key):
                    if key not in reserved_keys:
                        reserved_keys.add(key)
                        continue
                    while "%s-%s" % (key, suffix) in reserved_keys:
                        suffix += 1
                    keys[i] = "%s-%s" % (key, suffix)
                    reserved_keys.add(keys[i])

            # Store the data.
            for key, value in zip(keys, values):
                self[key] = value


    def __getitem__(self, index):
        column = None
        column_slice = None

        # Cases that return a column (array):

        # table["a"]
        if isinstance(index, str):
            column = index
            column_slice = slice(None, None, None)
        # table["a", 10], table["a", 10:20], table["a", [10, 12, 18]], etc.
        elif isinstance(index, tuple) and isinstance(index[0], str):
            column = index[0]
            column_slice = index[1]

        if column is not None and column_slice is not None:
            return self._columns[column][column_slice]

        row_slice = None
        columns = None

        # table[10]
        if isinstance(index, numbers.Integral):
            row_slice = slice(index, index + 1)
            columns = self._columns.keys()
        # table[10:20]
        elif isinstance(index, slice):
            row_slice = index
            columns = self._columns.keys()
        elif isinstance(index, tuple):
            # table[10, ]
            if isinstance(index[0], numbers.Integral):
                row_slice = slice(index[0], index[0] + 1)
            # table[10:20, ], table[[10, 12, 18], ], etc.
            else:
                row_slice = index[0]

            # table[, "a"]
            if isinstance(index[1], str):
                columns = [index[1]]
            # table[, ["a", "b", "c"]], etc.
            else:
                columns = index[1]
        else:
            index = numpy.array(index)
            if issubclass(index.dtype.type, numpy.character):
                columns = index
                row_slice = slice(None, None, None)
            else:
                row_slice = index
                columns = self._columns.keys()

        if row_slice is not None and columns is not None:
            return Table([(column, self._columns[column][row_slice]) for column in columns])


    def __setitem__(self, index, value):
        if isinstance(index, str):
            value = numpy.ma.array(value)
            if value.ndim != 1:
                raise ValueError("Can't assign %s-dimensional array to the '%s' column." % (value.ndim, index))
            for column in self._columns.values():
                if column.shape != value.shape:
                    raise ValueError("Expected %s values, received %s." % (column.shape[0], value.shape[0]))
            column = str(index)
            self._columns[column] = value
            return

        if isinstance(index, tuple):
            if isinstance(index[0], str) and isinstance(index[1], (int, slice)):
                column, column_slice = index
                self._columns[column][column_slice] = value
                return

        raise ValueError("Unsupported key for assignment: %s" % (index,))

    def __delitem__(self, key):
        return self._columns.__delitem__(key)

    def __len__(self):
        return list(self._columns.values())[0].shape[0] if len(self._columns) else 0

    def __iter__(self):
        for row in numpy.arange(self.__len__()):
            yield tuple([column[row] for column in self._columns.values()])

    def _repr_html_(self):
        root_xml = xml.Element(
            "table",
            style="border-collapse:collapse; border:none; color: %s" %
            toyplot.color.black)
        root_xml.set("class", "toyplot-data-Table")
        header_xml = xml.SubElement(
            root_xml,
            "tr",
            style="border:none;border-bottom:1px solid %s" %
            toyplot.color.black)
        for name in self._columns.keys():
            xml.SubElement(
                header_xml,
                "th",
                style="text-align:left;border:none;padding-right:1em;").text = str(name)

        iterators = [iter(column) for column in self._columns.values()]
        for _ in numpy.arange(len(self)):
            for index, iterator in enumerate(iterators):
                value = next(iterator)

                if isinstance(value, numbers.Number):
                    value = "{:.12g}".format(value)
                else:
                    value = str(value)

                if index == 0:
                    row_xml = xml.SubElement(
                        root_xml, "tr", style="border:none")
                xml.SubElement(
                    row_xml,
                    "td",
                    style="border:none;padding-right:1em;").text = value

        return xml.tostring(root_xml, encoding="unicode", method="html")

    @property
    def shape(self):
        """The table shape (number of rows and columns).

        Returns
        -------
        shape: tuple
            (number of rows, number of columns) tuple.
        """
        return (
            list(self._columns.values())[0].shape[0] if len(self._columns) else 0,
            len(self._columns),
        )

    def items(self):
        """Return column names and columns, in column order.

        Returns
        -------
        items: list
            Sequence of (name, column) tuples.
        """
        return self._columns.items()

    def keys(self):
        """Return the table column names, in column order.

        Returns
        -------
        keys: sequence of :class:`str` column names.
        """
        return self._columns.keys()

    def values(self):
        """Return the table columns, in column order.

        Returns
        -------
        values: sequence of :class:`numpy.ndarray` columns.
        """
        return self._columns.values()

    def metadata(self, column):
        """Return metadata for one of the table's columns.

        Parameters
        ----------
        column: string.
          The name of an existing column.

        Returns
        -------
        metadata: :class:`dict` containing key-value pairs.
        """
        if column not in self._columns:
            raise ValueError("Unknown column name '%s'" % column)
        return self._metadata[column]

    def matrix(self):
        """Convert the table to a matrix (2D numpy array).

        The data type of the returned array is chosen based on the types of the
        columns within the table.  Tables containing a homogeneous set of column
        types will return an array of the the same type.  If the table contains one
        or more string columns, the results will be an array of strings.

        Returns
        -------
        matrix: :class:`numpy.ma.MaskedArray`
            The returned array will have two dimensions.
        """
        return numpy.ma.column_stack(list(self._columns.values()))


def read_csv(fobj, convert=False):
    """Load a CSV (delimited text) file.

    Parameters
    ----------
    fobj: file-like object or string, required
        The file to read.  Use a string filepath, an open file, or a file-like object.
    convert: boolean, optional
        By default, the columns in a table will contain strings.  If True,
        convert column types to integers and floats where possible.

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
    if isinstance(fobj, str):
        fobj = open(fobj, "r")
    rows = [row for row in csv.reader(fobj)]
    columns = zip(*rows)

    result = Table([(column[0], column[1:]) for column in columns])

    if convert:
        for name in result.keys():
            try:
                result[name] = result[name].astype("int")
            except:
                try:
                    result[name] = result[name].astype("float")
                except:
                    pass

    return result


def cars():
    """Return sample automobile model data.

    Returns
    -------
    table: :class:`toyplot.data.Table`
        Table containing descriptions of multiple makes and models of automobile.
    """
    return read_csv(cars.path, convert=True)
cars.path = os.path.join(_data_dir, "cars.csv")


def communities():
    """Return sample community detection data.

    Returns
    -------
    edges: :class:`numpy.ndarray`
        An :math:`E \\times 2` matrix containing source and target vertex ids for :math:`E` edges.
    truth: :class:`numpy.ndarray`
        A :math:`V \\times 2` matrix containing a vertex id and ground-truth community id for :math:`V` vertices.
    assigned: :class:`numpy.ndarray`
        A :math:`V \\times 2` matrix containing a vertex id and alternate community id for :math:`V` vertices.
    """
    edges = numpy.array([row.split() for row in open(os.path.join(_data_dir, "community-edges.csv"), "rb")], dtype="int")
    truth = numpy.array([row.split() for row in open(os.path.join(_data_dir, "community-truth.csv"), "rb")], dtype="int")
    assigned = numpy.array([row.split() for row in open(os.path.join(_data_dir, "community-assigned.csv"), "rb")], dtype="int")

    return edges, truth, assigned


def commute():
    """Return sample OBD-II commuting data.

    Returns
    -------
    table: :class:`toyplot.data.Table`
        Table containing a stream of OBD-II data collected from an automobile during a morning commute.
    """
    return read_csv(commute.path)
commute.path = os.path.join(_data_dir, "commute.csv")


def deliveries():
    """Return sample delivery data.

    Returns
    -------
    table: :class:`toyplot.data.Table`
        Table containing a stream of OBD-II data collected from an automobile during a morning commute.
    """
    return read_csv(deliveries.path)
deliveries.path = os.path.join(_data_dir, "deliveries.csv")


def temperatures():
    """Return sample temperature data.

    Returns
    -------
    table: :class:`toyplot.data.Table`
        Table containing temperature data collected by NOAA.
    """
    return read_csv(temperatures.path)
temperatures.path = os.path.join(_data_dir, "temperatures.csv")
