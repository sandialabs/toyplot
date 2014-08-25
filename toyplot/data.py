# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import collections
import numbers
import numpy
import xml.etree.ElementTree as xml

class Table(object):
  """Encapsulates an ordered, heterogeneous collection of labelled data series.

  You may retrieve columns by integer index as with a normal list, or by column
  label, both using [] syntax.  Note that a .data file could contain duplicate
  column labels, in which case label lookup will throw an exception and index
  lookup must be used.
  """
  def __init__(self, data=None):
    if data is None:
      data = collections.OrderedDict()

    if not isinstance(data, collections.OrderedDict):
      raise ValueError("Unsupported data type: %s" % type(data))

    self._columns = data

  def __getitem__(self, key):
    # Return a single column
    if isinstance(key, basestring):
      return self._columns[key]
    # Return a single row
    if isinstance(key, numbers.Integral):
      index = numpy.array([key])
    # Return a collection of rows using slicing
    elif isinstance(key, slice):
      index = key
    # Return an explicit collection of rows
    else:
      index = numpy.array(key)
    return Table(collections.OrderedDict([(key, self._columns[key][index]) for key in self._columns.keys()]))

  def __setitem__(self, key, value):
    if isinstance(value, numpy.ndarray):
      if value.ndim != 1:
        raise ValueError("Only 1D arrays are allowed.")
      for column in self._columns.values():
        if column.shape != value.shape:
          raise ValueError("Expected %s values, received %s." % (column.shape[0], value.shape[0]))
    self._columns[key] = value

  def __delitem__(self, key):
    return self._columns.__delitem__(key)

  def _repr_html_(self):
    root_xml = xml.Element("table", style="border-collapse:collapse; border:none")
    header_xml = xml.SubElement(root_xml, "tr", style="border:none;border-bottom:1px solid black")
    for name in self._columns.keys():
      xml.SubElement(header_xml, "th", style="text-align:center;border:none").text = str(name)

    try:
      iterators = [iter(column) for column in self._columns.values()]
      while True:
        for index, iterator in enumerate(iterators):
          value = iterator.next()
          if index == 0:
            row_xml = xml.SubElement(root_xml, "tr", style="border:none")
          xml.SubElement(row_xml, "td", style="border:none").text = str(value)
    except StopIteration:
      pass

    return xml.tostring(root_xml, method="html")

  def keys(self):
    return self._columns.keys()

  def columns(self, keys):
    return Table(collections.OrderedDict([(key, self._columns[key]) for key in keys]))

  def rows(self, keys):
    if isinstance(keys, numbers.Integral):
      index = numpy.array([keys])
    elif isinstance(keys, slice):
      index = keys
    else:
      index = numpy.array(keys)
    return Table(collections.OrderedDict([(key, self._columns[key][index]) for key in self._columns.keys()]))

#  def __getslice__(self,i,j):
#    return columns(list.__getslice__(self, i, j))
#
#  def __add__(self,other):
#    return columns(list.__add__(self,other))
#
#  def __mul__(self,other):
#    return columns(list.__mul__(self,other))
#
#  def index(self, key):
#    """Return the zero-based index of a column, identified by zero-based index or label.
#
#    Raises an exception if the label can't be found, or there is more than one
#    column with the given label.
#    """
#    if isinstance(key, numbers.Integral):
#      return key
#    else:
#      candidates = [(index, column) for index, column in enumerate(self) if column.label == key]
#      if len(candidates) == 0:
#        raise LookupError("No column with label %s." % key)
#      elif len(candidates) == 1:
#        return candidates[0][0]
#      else:
#        raise LookupError("More than one column with label %s." % key)
#
#  def insert(self, key, column):
#    list.insert(self, self.index(key), column)

#class Table:
#  def __init__(self, data):
#    self._data = data
#
#  def _repr_html_(self):
#    root_xml = xml.Element("table", style="border-collapse:collapse; border:none")
#
#    if isinstance(self._data, numpy.ndarray):
#      if self._data.ndim == 1:
#        header_xml = xml.SubElement(root_xml, "tr", style="border:none;border-bottom:1px solid black")
#        for name, type in self._data.dtype.descr:
#          xml.SubElement(header_xml, "th", style="text-align:center;border:none").text = str(name)
#
#        for row in self._data:
#          row_xml = xml.SubElement(root_xml, "tr", style="border:none")
#          for value in row:
#            xml.SubElement(row_xml, "td", style="border:none").text = self._format.format(value)
#      elif self._data.ndim == 2:
#        for row in self._data:
#          row_xml = xml.SubElement(root_xml, "tr", style="border:none")
#          for value in row:
#            xml.SubElement(row_xml, "td", style="border:none").text = self._format.format(value)
#
#    elif isinstance(self._data, scipy.sparse.coo_matrix):
#      rows = numpy.unique(self._data.row)
#      columns = numpy.unique(self._data.col)
#      csr = self._data.tocsr()
#
#      header_xml = xml.SubElement(root_xml, "tr", style="border:none;border-bottom:1px solid black")
#      xml.SubElement(header_xml, "th", style="border:none")
#      for column in columns:
#        xml.SubElement(header_xml, "th", style="text-align:center;border:none").text = str(column)
#
#      for row in rows:
#        row_slice = csr[row]
#        row_xml = xml.SubElement(root_xml, "tr", style="border:none")
#        xml.SubElement(row_xml, "th", style="border:none").text = str(row)
#        for column in columns:
#          cell_xml = xml.SubElement(row_xml, "td", style="border:none")
#          if numpy.any(row_slice.indices == column):
#            cell_xml.text = self._format.format(row_slice[0, column])
#
#    return xml.tostring(root_xml, method="html")
