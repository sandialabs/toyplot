# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import numbers
import numpy
import toyplot.color
import toyplot.compatibility
import xml.etree.ElementTree as xml

class Table(object):
  """Encapsulates an ordered, heterogeneous collection of labelled data series.
  """
  def __init__(self, data=None):
    self._columns = collections.OrderedDict()

    if data is not None:
      if isinstance(data, collections.OrderedDict):
        for key, value in data.items():
          self[key] = value
      elif isinstance(data, toyplot.data.Table):
        for key, value in data.items():
          self[key] = value
      elif isinstance(data, dict):
        for key in sorted(data.keys()):
          self[key] = data[key]
      else:
        raise ValueError("Unsupported data type: %s" % type(data))

  def __getitem__(self, index):
    # Return a single column by name
    if isinstance(index, toyplot.compatibility.string_type):
      return self._columns[index]
    # Return a single row by index
    if isinstance(index, numbers.Integral):
      index = slice(index, index + 1)
    return Table(collections.OrderedDict([(key, self._columns[key][index]) for key in self._columns.keys()]))

  def __setitem__(self, key, value):
    if not isinstance(key, toyplot.compatibility.string_type):
      raise ValueError("Column name must be a string.")
    value = numpy.ma.array(value)
    if value.ndim != 1:
      raise ValueError("Only 1D arrays are allowed.")
    for column in self._columns.values():
      if column.shape != value.shape:
        raise ValueError("Expected %s values, received %s." % (column.shape[0], value.shape[0]))
    self._columns[key] = value

  def __delitem__(self, key):
    return self._columns.__delitem__(key)

  def __len__(self):
    return self._columns.values()[0].shape[0] if len(self._columns) else 0

  def _repr_html_(self):
    root_xml = xml.Element("table", style="border-collapse:collapse; border:none; color: %s" % toyplot.color.near_black)
    header_xml = xml.SubElement(root_xml, "tr", style="border:none;border-bottom:1px solid %s" % toyplot.color.near_black)
    for name in self._columns.keys():
      xml.SubElement(header_xml, "th", style="text-align:left;border:none").text = str(name)

    iterators = [iter(column) for column in self._columns.values()]
    for row_index in numpy.arange(len(self)):
      for index, iterator in enumerate(iterators):
        value = iterator.next()
        if index == 0:
          row_xml = xml.SubElement(root_xml, "tr", style="border:none")
        xml.SubElement(row_xml, "td", style="border:none").text = str(value)

    return xml.tostring(root_xml, method="html")

  @property
  def shape(self):
    return (self._columns.values()[0].shape[0] if len(self._columns) else 0, len(self._columns))

  def items(self):
    return self._columns.items()

  def keys(self):
    return self._columns.keys()

  def values(self):
    return self._columns.values()

  def columns(self, keys):
    return Table(collections.OrderedDict([(key, self._columns[key]) for key in keys]))

  def rows(self, index):
    if isinstance(index, numbers.Integral):
      index = slice(index, index + 1)
    return Table(collections.OrderedDict([(key, self._columns[key][index]) for key in self._columns.keys()]))

