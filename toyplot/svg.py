# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

from multipledispatch import dispatch
import collections
import itertools
import json
import numbers
import numpy
import toyplot.axes
import toyplot.canvas
import toyplot.color
import toyplot.compatibility
import toyplot.mark
import uuid
import xml.etree.ElementTree as xml

def apply_changes(svg, changes):
  for change_type, instructions in changes.items():
    if change_type == "set-mark-style":
      for mark_id, style in instructions:
        mark = svg.find(".//*[@id='%s']" % mark_id)
        style = toyplot.style.combine(dict([declaration.split(":") for declaration in mark.get("style").split(";") if declaration != ""]), style)
        mark.set("style", _css_style(style))
    elif change_type == "set-datum-style":
      for mark_id, series, datum, style in instructions:
        mark_xml = svg.find(".//*[@id='%s']" % mark_id)
        series_xml = mark_xml.findall("*[@class='toyplot-Series']")[series]
        datum_xml = series_xml.findall("*[@class='toyplot-Datum']")[datum]
        style = toyplot.style.combine(dict([declaration.split(":") for declaration in datum_xml.get("style").split(";") if declaration != ""]), style)
        datum_xml.set("style", _css_style(style))
    elif change_type == "set-datum-text":
      for mark_id, series, datum, text in instructions:
        mark_xml = svg.find(".//*[@id='%s']" % mark_id)
        series_xml = mark_xml.findall("*[@class='toyplot-Series']")[series]
        datum_xml = series_xml.findall("*[@class='toyplot-Datum']")[datum]
        datum_xml.text = text

def render(canvas, fobj=None, animation=False):
  """Render the SVG representation of a canvas.

  Parameters
  ----------
  canvas: :class:`toyplot.canvas.Canvas`
    The canvas to be rendered.

  fobj: file-like object or string, optional
    The file to write.  Use a string filepath to write data directly to disk.
    If `None` (the default), the SVG tree will be returned to the caller
    instead.

  animation: boolean, optional
    If `True`, return a representation of the changes to be made to the SVG
    tree for animation.

  Returns
  -------
  svg: xml.etree.ElementTree.Element or `None`
    SVG representation of `canvas`, as a DOM tree, or `None` if the caller
    specifies the `fobj` parameter.

  changes: JSON-compatible data structure, or `None`
    JSON-compatible representation of the animated changes to `canvas`.

  Notes
  -----
  The SVG representation of a canvas should be considered the "canonical"
  representation - the other toyplot backends operate by converting the output
  from toyplot.svg.render() to the desired end target.
  """

  canvas.autorender(False)

  context = _RenderContext()
  svg = xml.Element("svg", xmlns="http://www.w3.org/2000/svg", attrib={"xmlns:toyplot":"http://www.sandia.gov/toyplot"}, width="%rpx" % canvas._width, height="%rpx" % canvas._height, style=_css_style(canvas._style), id=context.get_id(canvas))
  for child in canvas._children:
    _render(canvas, child, context.push(svg))

  if isinstance(fobj, toyplot.compatibility.string_type):
    with open(fobj, "wb") as file:
      file.write(xml.tostring(svg, method="xml"))
  elif fobj is not None:
    fobj.write(xml.tostring(svg, method="xml"))
  else:
    if animation:
      svg_animation = collections.defaultdict(lambda: collections.defaultdict(list))
      for time, time_changes in canvas._animation.items()[:-1]:
        svg_animation[time] # Ensure we have an entry for every time, even if there aren't any changes.
        for type, type_changes in time_changes.items():
          for change in type_changes:
            svg_animation[time][type].append([context.get_id(change[0])] + list(change[1:]))
      return svg, svg_animation
    else:
      return svg





















def _css_style(*styles):
  style = toyplot.style.combine(*styles)
  return ";".join(["%s:%s" % (key, value) for key, value in sorted(style.items())])

def _css_attrib(*styles):
  style = toyplot.style.combine(*styles)
  attrib = {}
  if len(style):
    attrib["style"] =  ";".join(["%s:%s" % (key, value) for key, value in sorted(style.items())])
  return attrib

class _RenderContext(object):
  def __init__(self, root=None, id_cache={}):
    self._root = root
    self._id_cache = id_cache

  def push(self, root):
    return _RenderContext(root, self._id_cache)

  @property
  def root(self):
    return self._root

  def get_id(self, obj):
    python_id = id(obj)
    if python_id not in self._id_cache:
      self._id_cache[python_id] = "t" + uuid.uuid4().hex
    return self._id_cache[python_id]

def _flat_contiguous(a):
  i = 0
  result = []
  for (k, g) in itertools.groupby(a.ravel()):
      n = len(list(g))
      if k:
          result.append(slice(i, i + n))
      i += n
  return result

def _render_data_table(root_xml, table, title):
  names = []
  data = []
  for name, column in table.items():
    if column.dtype == toyplot.color.dtype:
      for suffix, channel in zip([":red", ":green", ":blue", ":alpha"], ["r", "g", "b", "a"]):
        names.append(name + suffix)
        data.append(column[channel].tolist())
    else:
      names.append(name)
      data.append(column.tolist())

  xml_data_table = xml.SubElement(root_xml, "toyplot:data-table", title=title)
  xml_data_table.text = json.dumps({"names":names, "data":data}, sort_keys=True)
  return xml_data_table

def _render_marker(root, cx, cy, size, marker, marker_style=None, label_style=None, extra_class=None):
  if marker is None:
    return
  if isinstance(marker, toyplot.compatibility.string_type):
    marker = {"shape":marker}
  shape = marker.get("shape", None)
  shape_angle = marker.get("angle", 0)
  shape_style = marker.get("mstyle", None)
  shape_label = marker.get("label", None)
  shape_label_style = marker.get("lstyle", None)

  if shape in _render_marker.variations:
    variation = _render_marker.variations[shape]
    shape = variation[0]
    shape_angle += variation[1]

  attrib = _css_attrib(marker_style, shape_style)
  if extra_class is not None:
    attrib["class"] = extra_class
  marker_xml = xml.SubElement(root, "g", attrib=attrib)
  if shape == "|":
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle, cx, cy), x1=repr(cx), x2=repr(cx), y1=repr(cy - (size / 2)), y2=repr(cy + (size / 2)))
  elif shape == "+":
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle, cx, cy), x1=repr(cx), x2=repr(cx), y1=repr(cy - (size / 2)), y2=repr(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle, cx, cy), x1=repr(cx - (size / 2)), x2=repr(cx + (size / 2)), y1=repr(cy), y2=repr(cy))
  elif shape == "*":
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle, cx, cy), x1=repr(cx), x2=repr(cx), y1=repr(cy - (size / 2)), y2=repr(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle - 60, cx, cy), x1=repr(cx), x2=repr(cx), y1=repr(cy - (size / 2)), y2=repr(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle + 60, cx, cy), x1=repr(cx), x2=repr(cx), y1=repr(cy - (size / 2)), y2=repr(cy + (size / 2)))
  elif shape == "^":
    xml.SubElement(marker_xml, "polygon", transform="rotate(%r, %r, %r)" % (shape_angle, cx, cy), points=" ".join(["%r,%r" % (xp, yp) for xp, yp in [(cx - (size / 2), cy + (size / 2)), (cx, cy - (size / 2)), (cx + (size / 2), cy + (size / 2))]]))
  elif shape == "s":
    xml.SubElement(marker_xml, "rect", transform="rotate(%r, %r, %r)" % (shape_angle, cx, cy), x=repr(cx-(size / 2)), y=repr(cy-(size / 2)), width=repr(size), height=repr(size))
  elif shape == "o":
    xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 2))
  elif shape == "oo":
    xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 2))
    xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 4))
  elif shape == "o|":
    xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 2))
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle, cx, cy), x1=repr(cx), x2=repr(cx), y1=repr(cy - (size / 2)), y2=repr(cy + (size / 2)))
  elif shape == "o+":
    xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 2))
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle, cx, cy), x1=repr(cx), x2=repr(cx), y1=repr(cy - (size / 2)), y2=repr(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle, cx, cy), x1=repr(cx - (size / 2)), x2=repr(cx + (size / 2)), y1=repr(cy), y2=repr(cy))
  elif shape == "o*":
    xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 2))
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle, cx, cy), x1=repr(cx), x2=repr(cx), y1=repr(cy - (size / 2)), y2=repr(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle - 60, cx, cy), x1=repr(cx), x2=repr(cx), y1=repr(cy - (size / 2)), y2=repr(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%r, %r, %r)" % (shape_angle + 60, cx, cy), x1=repr(cx), x2=repr(cx), y1=repr(cy - (size / 2)), y2=repr(cy + (size / 2)))
  elif shape == "path":
    shape_path = marker.get("path")
    xml.SubElement(marker_xml, "path", transform="translate(%r, %r) scale(%r) translate(%r, %r)" % (cx, cy, size, -cx, -cy), d="M " + repr(cx) + " " + repr(cy) + shape_path)

  if shape_label is not None:
    xml.SubElement(marker_xml, "text", x=repr(cx), y=repr(cy), attrib=_css_attrib({"stroke":"none", "fill":toyplot.color.near_black, "text-anchor":"middle", "alignment-baseline":"middle", "font-size":"%rpx" % (size * 0.75)}, label_style, shape_label_style)).text = shape_label
_render_marker.variations = {"-": ("|", 90), "x": ("+", 45), "v": ("^", 180), "<": ("^", -90), ">": ("^", 90), "d": ("s", 45), "o-": ("o|", 90), "ox": ("o+", 45)}

@dispatch(toyplot.canvas.Canvas, toyplot.axes.Cartesian, _RenderContext)
def _render(canvas, axes, context):
  axes._finalize_domain()

  axes_data = {"x":[], "y":[]}
  if axes.x._scale == "linear":
    axes_data["x"].append({"scale":"linear", "range":{"min":axes._xmin_range + axes._padding, "max":axes._xmax_range - axes._padding}, "domain":{"min":axes._xmin_computed, "max":axes._xmax_computed}})
  else:
    scale, base = axes.x._scale
    if scale == "log":
      if axes._xmax_computed < 0 or axes._xmin_computed > 0:
        axes_data["x"].append({"scale":"log", "base":base, "range":{"min":axes._xmin_range + axes._padding, "max":axes._xmax_range - axes._padding}, "domain":{"min":axes._xmin_computed, "max":axes._xmax_computed}})
      else:
        axes_data["x"].append({"scale":"log", "base":base, "range":{"min":axes._xmin_range + axes._padding, "max":axes._project_x(-1.0)}, "domain":{"min":axes._xmin_computed, "max":-1.0}})
        axes_data["x"].append({"scale":"linear", "range":{"min":axes._project_x(-1.0), "max":axes._project_x(1.0)}, "domain":{"min":-1.0, "max":1.0}})
        axes_data["x"].append({"scale":"log", "base":base, "range":{"min":axes._project_x(1.0), "max":axes._xmax_range - axes._padding}, "domain":{"min":1.0, "max":axes._xmax_computed}})

  if axes.y._scale == "linear":
    axes_data["y"].append({"scale":"linear", "range":{"min":axes._ymin_range + axes._padding, "max":axes._ymax_range - axes._padding}, "domain":{"min":axes._ymin_computed, "max":axes._ymax_computed}})
  else:
    scale, base = axes.y._scale
    if scale == "log":
      if axes._ymax_computed < 0 or axes._ymin_computed > 0:
        axes_data["y"].append({"scale":"log", "base":base, "range":{"min":axes._ymin_range + axes._padding, "max":axes._ymax_range - axes._padding}, "domain":{"min":axes._ymin_computed, "max":axes._ymax_computed}})
      else:
        axes_data["y"].append({"scale":"log", "base":base, "range":{"min":axes._project_y(-1.0), "max":axes._ymax_range - axes._padding}, "domain":{"min":axes._ymin_computed, "max":-1.0}})
        axes_data["y"].append({"scale":"linear", "range":{"min":axes._project_y(1.0), "max":axes._project_y(-1.0)}, "domain":{"min":-1.0, "max":1.0}})
        axes_data["y"].append({"scale":"log", "base":base, "range":{"min":axes._ymin_range + axes._padding, "max":axes._project_y(1.0)}, "domain":{"min":1.0, "max":axes._ymax_computed}})

  class custom_encoder(json.JSONEncoder):
    def default(self, obj):
      if isinstance(obj, numpy.generic):
        return numpy.asscalar(obj)
      print(type(obj))
      return json.JSONEncoder.default(self, obj)

  axes_xml = xml.SubElement(context.root, "g", id=context.get_id(axes), attrib={"class":"toyplot-axes-Cartesian"})
  xml.SubElement(axes_xml, "toyplot:axes").text = json.dumps(axes_data, cls=custom_encoder, sort_keys=True)

  clip_xml = xml.SubElement(axes_xml, "clipPath", id="t" + uuid.uuid4().hex)
  xml.SubElement(clip_xml, "rect", x=repr(axes._xmin_range), y=repr(axes._ymin_range), width=repr(axes._xmax_range - axes._xmin_range), height=repr(axes._ymax_range - axes._ymin_range))

  children_xml = xml.SubElement(axes_xml, "g", attrib={"class":"toyplot-coordinate-events", "clip-path":"url(#%s)" % clip_xml.get("id")}, style=_css_style({"cursor":"crosshair"}))
  xml.SubElement(children_xml, "rect", x=repr(axes._xmin_range), y=repr(axes._ymin_range), width=repr(axes._xmax_range - axes._xmin_range), height=repr(axes._ymax_range - axes._ymin_range), style=_css_style({"visibility":"hidden", "pointer-events":"all"}))
  for child in axes._children:
    _render(axes, child, context.push(children_xml))

  if axes.coordinates._show:
    coordinates_xml = xml.SubElement(axes_xml, "g", style=_css_style({"visibility":"hidden"}), attrib={"class":"toyplot-coordinates"})
    xml.SubElement(coordinates_xml, "rect", x=repr(axes.coordinates._xmin_range), y=repr(axes.coordinates._ymin_range), width=repr(axes.coordinates._xmax_range - axes.coordinates._xmin_range), height=repr(axes.coordinates._ymax_range - axes.coordinates._ymin_range), style=_css_style(axes.coordinates._style))
    xml.SubElement(coordinates_xml, "text", x=repr((axes.coordinates._xmin_range + axes.coordinates._xmax_range) * 0.5), y=repr((axes.coordinates._ymin_range + axes.coordinates._ymax_range) * 0.5), style=_css_style(axes.coordinates.label._style))

  if axes._show:
    if axes.x.spine._position == "low":
      spine_y = axes._ymax_range
    elif axes.x.spine._position == "high":
      spine_y = axes._ymin_range
    else:
      spine_y = axes._project_y(axes.x.spine._position)

    if axes.y.spine._position == "low":
      spine_x = axes._xmin_range
    elif axes.y.spine._position == "high":
      spine_x = axes._xmax_range
    else:
      spine_x = axes._project_x(axes.y.spine._position)

    if axes.x._show:
      if axes.x.spine._show:
        x1 = axes._xmin_range
        x2 = axes._xmax_range
        if axes._xmin_implicit is not None:
          x1 = max(x1, axes._project_x(axes._xmin_implicit))
          x2 = min(x2, axes._project_x(axes._xmax_implicit))
        xml.SubElement(axes_xml, "line", x1=repr(x1), y1=repr(spine_y), x2=repr(x2), y2=repr(spine_y), style=_css_style(axes.x.spine._style))

      if axes.x.ticks._show:
        ticks_group = xml.SubElement(axes_xml, "g")
        for location, tick_style in zip(axes._xtick_locations, axes.x.ticks.tick.styles(axes._xtick_locations)):
          x = axes._project_x(location)
          y1 = axes._ymax_range
          y2 = axes._ymax_range - axes.x.ticks._length
          xml.SubElement(ticks_group, "line", x1=repr(x), y1=repr(y1), x2=repr(x), y2=repr(y2), style=_css_style(axes.x.ticks._style, tick_style))

      if axes.x.ticks.labels._show:
        ticks_group = xml.SubElement(axes_xml, "g")
        for location, label, title, label_style in zip(axes._xtick_locations, axes._xtick_labels, axes._xtick_titles, axes.x.ticks.labels.label.styles(axes._xtick_locations)):
          x = axes._project_x(location)
          y = axes._ymax_range
          label_xml = xml.SubElement(ticks_group, "text", x=repr(x), y=repr(y), style=_css_style({"text-anchor":"middle", "alignment-baseline":"middle", "baseline-shift":"-80%"}, axes.x.ticks.labels._style, label_style))
          label_xml.text = label
          if axes.x.ticks.labels._angle:
            label_xml.set("transform", "rotate(%r, %r, %r)" % (axes.x.ticks.labels._angle, x, y))
          if title is not None:
            xml.SubElement(label_xml, "title").text = str(title)

      if axes.x.label._text is not None:
        x = (axes._xmin_range + axes._xmax_range) * 0.5
        y = axes._ymax_range
        xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(axes.x.label._style)).text = axes.x.label._text

    if axes.y._show:
      if axes.y.spine._show:
        y1 = axes._ymin_range
        y2 = axes._ymax_range
        if axes._ymin_implicit is not None:
          y1 = max(y1, axes._project_y(axes._ymax_implicit))
          y2 = min(y2, axes._project_y(axes._ymin_implicit))
        xml.SubElement(axes_xml, "line", x1=repr(spine_x), y1=repr(y1), x2=repr(spine_x), y2=repr(y2), style=_css_style(axes.y.spine._style))

      if axes.y.ticks._show:
        ticks_group = xml.SubElement(axes_xml, "g")
        for location, tick_style in zip(axes._ytick_locations, axes.y.ticks.tick.styles(axes._ytick_locations)):
          y = axes._project_y(location)
          x1 = axes._xmin_range
          x2 = axes._xmin_range + axes.y.ticks._length
          xml.SubElement(ticks_group, "line", x1=repr(x1), y1=repr(y), x2=repr(x2), y2=repr(y), style=_css_style(axes.y.ticks._style, tick_style))

      if axes.y.ticks.labels._show:
        ticks_group = xml.SubElement(axes_xml, "g")
        for location, label, title, label_style in zip(axes._ytick_locations, axes._ytick_labels, axes._ytick_titles, axes.y.ticks.labels.label.styles(axes._ytick_locations)):
          x = axes._xmin_range
          y = axes._project_y(location)
          label_xml = xml.SubElement(ticks_group, "text", x=repr(x), y=repr(y), style=_css_style({"text-anchor":"middle", "alignment-baseline":"middle", "baseline-shift":"80%"}, axes.y.ticks.labels._style, label_style))
          label_xml.text = label
          if axes.y.ticks.labels._angle:
            label_xml.set("transform", "rotate(%r, %r, %r)" % (axes.y.ticks.labels._angle, x, y))
          if title is not None:
            xml.SubElement(label_xml, "title").text = str(title)

      if axes.y.label._text is not None:
        x = axes._xmin_range
        y = (axes._ymin_range + axes._ymax_range) * 0.5
        xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), transform="rotate(-90, %r, %r)" % (x, y), style=_css_style(axes.y.label._style)).text = axes.y.label._text

    if axes.label._text is not None:
      x = (axes._xmin_range + axes._xmax_range) * 0.5
      y = axes._ymin_range
      xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(axes.label._style)).text = axes.label._text

@dispatch(toyplot.canvas.Canvas, toyplot.axes.Table, _RenderContext)
def _render(canvas, axes, context):
  axes_xml = xml.SubElement(context.root, "g", id=context.get_id(axes), attrib={"class":"toyplot-axes-Table"})

  x_boundaries, y_boundaries = axes._boundaries()

  # Render column headers.
  for column_index, (key, column) in enumerate(zip(axes._keys, axes._columns)):
    x = (x_boundaries[column_index] + x_boundaries[column_index + 1]) / 2
    y = (y_boundaries[0] + y_boundaries[1]) / 2
    xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(toyplot.style.combine(axes._hstyle, column.header.style, {"text-anchor":"middle"}))).text = key if column.header.content is None else column.header.content

  # Render column contents.
  for column_index, column in enumerate(axes._columns):
    column_style = toyplot.style.combine(axes._style, column.style)

    column_left = x_boundaries[column_index]
    column_right = x_boundaries[column_index + 1]
    column_center = (column_left + column_right) / 2

    padding = 5
    formatted_left = column_left + padding
    formatted_right = column_right - padding

    prefix, separator, suffix = column.formatted

    for row_index, row in enumerate(axes._rows):
      row_style = toyplot.style.combine(column_style, row.style)
      cell_style = toyplot.style.combine(row_style, axes._cells[row_index, column_index].style)
      cell_content = axes._cells[row_index, column_index]._content

      cell_prefix = prefix[row_index]
      cell_separator = separator[row_index]
      cell_suffix = suffix[row_index]

      y = (y_boundaries[row_index + 1] + y_boundaries[row_index + 2]) / 2

      if column.justify == "left":
        x = formatted_left + column.offset
        xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(toyplot.style.combine(cell_style, {"text-anchor":"begin"}))).text = cell_content if cell_content is not None else cell_prefix + cell_separator + cell_suffix
      elif column.justify == "center":
        x = column_center
        xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(toyplot.style.combine(cell_style, {"text-anchor":"middle"}))).text = cell_content if cell_content is not None else cell_prefix + cell_separator + cell_suffix
      elif column.justify == "right":
        x = formatted_right + column.offset
        xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(toyplot.style.combine(cell_style, {"text-anchor":"end"}))).text = cell_content if cell_content is not None else cell_prefix + cell_separator + cell_suffix
      elif column.justify is "separator":
        x = column_center + column.offset

        if cell_content:
          xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(toyplot.style.combine(cell_style, {"text-anchor":"middle"}))).text = cell_content
        elif cell_prefix and cell_separator and cell_suffix:
          xml.SubElement(axes_xml, "text", x=repr(x - 2), y=repr(y), style=_css_style(toyplot.style.combine(cell_style, {"text-anchor":"end"}))).text = cell_prefix
          xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(toyplot.style.combine(cell_style, {"text-anchor":"middle"}))).text = cell_separator
          xml.SubElement(axes_xml, "text", x=repr(x + 2), y=repr(y), style=_css_style(toyplot.style.combine(cell_style, {"text-anchor":"begin"}))).text = cell_suffix
        elif cell_prefix and cell_suffix:
          xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(toyplot.style.combine(cell_style, {"text-anchor":"end"}))).text = cell_prefix
          xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(toyplot.style.combine(cell_style, {"text-anchor":"begin"}))).text = cell_suffix
        elif cell_prefix:
          xml.SubElement(axes_xml, "text", x=repr(x), y=repr(y), style=_css_style(toyplot.style.combine(cell_style, {"text-anchor":"middle"}))).text = cell_prefix

  # Render children.
  for child in axes._children:
    _render(axes._parent, child, context.push(axes_xml))

  # Render grid lines.
  separation = axes.grid.separation / 2

  def contiguous(a):
    i = 0
    result = []
    for (k, g) in itertools.groupby(a.ravel()):
      n = len(list(g))
      if k:
        result.append((i, i + n, k))
      i += n
    return result

  for row_index, row in enumerate(axes._grid._hlines):
    y = y_boundaries[row_index]
    for start, end, line_type in contiguous(row):
      if line_type == "single":
        xml.SubElement(axes_xml, "line", x1=repr(x_boundaries[start]), y1=repr(y), x2=repr(x_boundaries[end]), y2=repr(y), style=_css_style(axes._grid._style))
      elif line_type == "double":
        xml.SubElement(axes_xml, "line", x1=repr(x_boundaries[start]), y1=repr(y - separation), x2=repr(x_boundaries[end]), y2=repr(y - separation), style=_css_style(axes._grid._style))
        xml.SubElement(axes_xml, "line", x1=repr(x_boundaries[start]), y1=repr(y + separation), x2=repr(x_boundaries[end]), y2=repr(y + separation), style=_css_style(axes._grid._style))

  for column_index, column in enumerate(axes._grid._vlines.T):
    x = x_boundaries[column_index]
    for start, end, line_type in contiguous(column):
      if line_type == "single":
        xml.SubElement(axes_xml, "line", x1=repr(x), y1=repr(y_boundaries[start]), x2=repr(x), y2=repr(y_boundaries[end]), style=_css_style(axes._grid._style))
      elif line_type == "double":
        xml.SubElement(axes_xml, "line", x1=repr(x - separation), y1=repr(y_boundaries[start]), x2=repr(x - separation), y2=repr(y_boundaries[end]), style=_css_style(axes._grid._style))
        xml.SubElement(axes_xml, "line", x1=repr(x + separation), y1=repr(y_boundaries[start]), x2=repr(x + separation), y2=repr(y_boundaries[end]), style=_css_style(axes._grid._style))

@dispatch(toyplot.axes.Cartesian, toyplot.mark.BarBoundaries, _RenderContext)
def _render(axes, mark, context):
  left = mark._table[mark._left[0]]
  right = mark._table[mark._right[0]]
  boundaries = numpy.ma.column_stack([mark._table[key] for key in mark._boundaries])

  if mark._left_right_axis == "x":
    axis1 = "x"
    axis2 = "y"
    distance1 = "width"
    distance2 = "height"
    left = axes._project_x(left)
    right = axes._project_x(right)
    boundaries = axes._project_y(boundaries)
  elif mark._left_right_axis == "y":
    axis1 = "y"
    axis2 = "x"
    distance1 = "height"
    distance2 = "width"
    left = axes._project_y(left)
    right = axes._project_y(right)
    boundaries = axes._project_x(boundaries)

  mark_xml = xml.SubElement(context.root, "g", style=_css_style(mark._style), id=context.get_id(mark), attrib={"class":"toyplot-mark-BarBoundaries"})
  _render_data_table(mark_xml, mark._table, title="Bar Data")

  for boundary1, boundary2, fill, opacity, title in zip(boundaries.T[:-1], boundaries.T[1:], [mark._table[key] for key in mark._fill], [mark._table[key] for key in mark._opacity], [mark._table[key] for key in mark._title]):
    not_null = numpy.invert(numpy.logical_or(numpy.ma.getmaskarray(boundary1), numpy.ma.getmaskarray(boundary2)))

    series_xml = xml.SubElement(mark_xml, "g", attrib={"class":"toyplot-Series"})
    for dleft, dright, dboundary1, dboundary2, dfill, dopacity, dtitle in zip(left[not_null], right[not_null], boundary1[not_null], boundary2[not_null], fill[not_null], opacity[not_null], title[not_null]):
      dstyle = toyplot.style.combine({"fill":toyplot.color.to_css(dfill), "opacity":dopacity}, mark._style)
      datum_xml = xml.SubElement(series_xml, "rect", attrib={"class":"toyplot-Datum", axis1:repr(min(dleft, dright)), axis2:repr(min(dboundary1, dboundary2)), distance1:repr(numpy.abs(dleft - dright)), distance2:repr(numpy.abs(dboundary1 - dboundary2))}, style=_css_style(dstyle))
      if dtitle is not None:
        xml.SubElement(datum_xml, "title").text = str(dtitle)

@dispatch(toyplot.axes.Cartesian, toyplot.mark.BarMagnitudes, _RenderContext)
def _render(axes, mark, context):
  left = mark._table[mark._left[0]]
  right = mark._table[mark._right[0]]
  boundaries = numpy.ma.cumsum(numpy.ma.column_stack([mark._table[mark._baseline[0]]] + [mark._table[key] for key in mark._magnitudes]), axis=1)
  not_null = numpy.invert(numpy.ma.any(numpy.ma.getmaskarray(boundaries), axis=1))

  if mark._left_right_axis == "x":
    axis1 = "x"
    axis2 = "y"
    distance1 = "width"
    distance2 = "height"
    left = axes._project_x(left)
    right = axes._project_x(right)
    boundaries = axes._project_y(boundaries)
  elif mark._left_right_axis == "y":
    axis1 = "y"
    axis2 = "x"
    distance1 = "height"
    distance2 = "width"
    left = axes._project_y(left)
    right = axes._project_y(right)
    boundaries = axes._project_x(boundaries)

  mark_xml = xml.SubElement(context.root, "g", style=_css_style(mark._style), id=context.get_id(mark), attrib={"class":"toyplot-mark-BarMagnitudes"})
  _render_data_table(mark_xml, mark._table, title="Bar Data")

  for boundary1, boundary2, fill, opacity, title in zip(boundaries.T[:-1], boundaries.T[1:], [mark._table[key] for key in mark._fill], [mark._table[key] for key in mark._opacity], [mark._table[key] for key in mark._title]):
    series_xml = xml.SubElement(mark_xml, "g", attrib={"class":"toyplot-Series"})
    for dleft, dright, dboundary1, dboundary2, dfill, dopacity, dtitle in zip(left[not_null], right[not_null], boundary1[not_null], boundary2[not_null], fill[not_null], opacity[not_null], title[not_null]):
      dstyle = toyplot.style.combine({"fill":toyplot.color.to_css(dfill), "opacity":dopacity}, mark._style)
      datum_xml = xml.SubElement(series_xml, "rect", attrib={"class":"toyplot-Datum", axis1:repr(min(dleft, dright)), axis2:repr(min(dboundary1, dboundary2)), distance1:repr(numpy.abs(dleft - dright)), distance2:repr(numpy.abs(dboundary1 - dboundary2))}, style=_css_style(dstyle))
      if dtitle is not None:
        xml.SubElement(datum_xml, "title").text = str(dtitle)

@dispatch(toyplot.axes.Cartesian, toyplot.mark.FillBoundaries, _RenderContext)
def _render(axes, mark, context):
  boundaries = numpy.ma.column_stack([mark._table[key] for key in mark._boundaries])

  if mark._position_axis == "x":
    position = axes._project_x(mark._table[mark._position[0]])
  else:
    position = axes._project_y(mark._table[mark._position[0]])

  if mark._boundary_axis == "x":
    boundaries = axes._project_x(boundaries)
  else:
    boundaries = axes._project_y(boundaries)

  mark_xml = xml.SubElement(context.root, "g", style=_css_style(mark._style), id=context.get_id(mark), attrib={"class":"toyplot-mark-FillBoundaries"})
  _render_data_table(mark_xml, mark._table, title="Fill Data")

  for boundary1, boundary2, fill, opacity, title in zip(boundaries.T[:-1], boundaries.T[1:], mark._fill, mark._opacity, mark._title):
    not_null = numpy.invert(numpy.logical_or(numpy.ma.getmaskarray(boundary1), numpy.ma.getmaskarray(boundary2)))
    segments = _flat_contiguous(not_null)

    series_style = toyplot.style.combine({"fill":toyplot.color.to_css(fill), "opacity":opacity}, mark._style)

    for segment in segments:
      if mark._position_axis == "x":
        coordinates = zip(numpy.concatenate((position[segment], position[segment][::-1])), numpy.concatenate((boundary1[segment], boundary2[segment][::-1])))
      elif mark._position_axis == "y":
        coordinates = zip(numpy.concatenate((boundary1[segment], boundary2[segment][::-1])), numpy.concatenate((position[segment], position[segment][::-1])))
      series_xml = xml.SubElement(mark_xml, "polygon", points=" ".join(["%r,%r" % (xi, yi) for xi, yi in coordinates]), style=_css_style(series_style))
      if title is not None:
        xml.SubElement(series_xml, "title").text = str(title)

@dispatch(toyplot.axes.Cartesian, toyplot.mark.FillMagnitudes, _RenderContext)
def _render(axes, mark, context):
  magnitudes = numpy.ma.column_stack([mark._table[mark._baseline[0]]] + [mark._table[key] for key in mark._magnitudes])
  boundaries = numpy.ma.cumsum(magnitudes, axis=1)
  not_null = numpy.invert(numpy.ma.any(numpy.ma.getmaskarray(boundaries), axis=1))
  segments = _flat_contiguous(not_null)

  if mark._position_axis == "x":
    position = axes._project_x(mark._table[mark._position[0]])
  else:
    position = axes._project_y(mark._table[mark._position[0]])

  if mark._magnitude_axis == "x":
    boundaries = axes._project_x(boundaries)
  else:
    boundaries = axes._project_y(boundaries)

  mark_xml = xml.SubElement(context.root, "g", style=_css_style(mark._style), id=context.get_id(mark), attrib={"class":"toyplot-mark-FillMagnitudes"})
  _render_data_table(mark_xml, mark._table, title="Fill Data")

  for boundary1, boundary2, fill, opacity, title in zip(boundaries.T[:-1], boundaries.T[1:], mark._fill, mark._opacity, mark._title):
    series_style = toyplot.style.combine({"fill":toyplot.color.to_css(fill), "opacity":opacity}, mark._style)
    for segment in segments:
      if mark._position_axis == "x":
        coordinates = zip(numpy.concatenate((position[segment], position[segment][::-1])), numpy.concatenate((boundary1[segment], boundary2[segment][::-1])))
      elif mark._position_axis == "y":
        coordinates = zip(numpy.concatenate((boundary1[segment], boundary2[segment][::-1])), numpy.concatenate((position[segment], position[segment][::-1])))
      series_xml = xml.SubElement(mark_xml, "polygon", points=" ".join(["%r,%r" % (xi, yi) for xi, yi in coordinates]), style=_css_style(series_style))
      if title is not None:
        xml.SubElement(series_xml, "title").text = str(title)

@dispatch(toyplot.axes.Cartesian, toyplot.mark.AxisLines, _RenderContext)
def _render(axes, mark, context):
  if mark._axes[0] == "x":
    p1="x1"
    p2="x2"
    b1="y1"
    b2="y2"
    position = axes._project_x(mark._table[mark._coordinates[0]])
    boundary1 = axes._ymin_range
    boundary2 = axes._ymax_range
  elif mark._axes[0] == "y":
    p1="y1"
    p2="y2"
    b1="x1"
    b2="x2"
    position = axes._project_y(mark._table[mark._coordinates[0]])
    boundary1 = axes._xmin_range
    boundary2 = axes._xmax_range
  mark_xml = xml.SubElement(context.root, "g", style=_css_style(mark._style), id=context.get_id(mark), attrib={"class":"toyplot-mark-AxisLines"})
  series_xml = xml.SubElement(mark_xml, "g", attrib={"class":"toyplot-Series"})
  for dposition, dstroke, dopacity, dtitle in zip(position, mark._table[mark._stroke[0]], mark._table[mark._opacity[0]], mark._table[mark._title[0]]):
    dstyle = toyplot.style.combine({"stroke":toyplot.color.to_css(dstroke), "opacity":dopacity}, mark._style)
    datum_xml = xml.SubElement(series_xml, "line", attrib={"class":"toyplot-Datum",p1:repr(dposition), p2:repr(dposition), b1:repr(boundary1), b2:repr(boundary2)}, style=_css_style(dstyle))
    if dtitle is not None:
      xml.SubElement(datum_xml, "title").text = str(dtitle)

@dispatch((toyplot.canvas.Canvas, toyplot.axes.Cartesian), toyplot.mark.Legend, _RenderContext)
def _render(canvas, legend, context):
  x = legend._xmin
  y = legend._ymin
  width = legend._xmax - legend._xmin
  height = legend._ymax - legend._ymin
  xml.SubElement(context.root, "rect", x=repr(x), y=repr(y), width=repr(width), height=repr(height), style=_css_style(legend._style), id=context.get_id(legend), attrib={"class":"toyplot-mark-Legend"})

  mark_count = len(legend._marks)
  if mark_count:
    mark_gutter = legend._gutter
    mark_height = (height - (legend._gutter * (mark_count+1))) / mark_count

    for i, mark in enumerate(legend._marks):
      mark_x = x + mark_gutter
      mark_y = y + ((i + 1) * mark_gutter) + (i * mark_height)
      mark_width = mark_height

      mark_style = {}
      if isinstance(mark, tuple) and len(mark) == 2:
        mark_label, mark_type = mark
      elif isinstance(mark, tuple) and len(mark) == 3:
        mark_label, mark_type, mark_style = mark

      if mark_type == "line":
        xml.SubElement(context.root, "line", x1=repr(mark_x), y1=repr(mark_y + mark_height), x2=repr(mark_x + mark_width), y2=repr(mark_y), style=_css_style(mark_style))
      elif mark_type == "rect":
        xml.SubElement(context.root, "rect", x=repr(mark_x), y=repr(mark_y), width=repr(mark_width), height=repr(mark_height), style=_css_style({"stroke":"none"}, mark_style))
      elif isinstance(mark_type, toyplot.mark.Plot):
        dstyle = toyplot.style.combine({"stroke":toyplot.color.to_css(mark_type._stroke[0])}, mark_type._style)
        xml.SubElement(context.root, "line", x1=repr(mark_x), y1=repr(mark_y + mark_height), x2=repr(mark_x + mark_width), y2=repr(mark_y), style=_css_style(dstyle, mark_style))
      elif isinstance(mark_type, (toyplot.mark.BarBoundaries, toyplot.mark.BarMagnitudes, toyplot.mark.FillBoundaries, toyplot.mark.FillMagnitudes)):
        dstyle = toyplot.style.combine({"fill":toyplot.color.to_css(mark_type._fill[0]), "opacity":mark_type._opacity[0]}, mark_type._style)
        xml.SubElement(context.root, "rect", x=repr(mark_x), y=repr(mark_y), width=repr(mark_width), height=repr(mark_height), style=_css_style(dstyle, mark_style))
      else:
        computed_style = toyplot.style.combine({"stroke":toyplot.color.near_black, "fill":"none"}, mark_style)
        _render_marker(context.root, mark_x + (mark_width / 2), mark_y + (mark_height / 2), min(mark_width, mark_height), mark_type, computed_style, {})

      label_x = x + mark_width + (2 * mark_gutter)
      label_y = y + ((i + 1) * mark_gutter) + (i * mark_height) + (mark_height / 2)
      xml.SubElement(context.root, "text", x=repr(label_x), y=repr(label_y), style=_css_style({"alignment-baseline":"middle", "stroke":"none"}, legend._lstyle)).text = mark_label

@dispatch(toyplot.axes.Cartesian, toyplot.mark.Plot, _RenderContext)
def _render(axes, mark, context):
  position = mark._table[mark._coordinates[0]]
  series = numpy.ma.column_stack([mark._table[key] for key in mark._series])

  if mark._coordinate_axes[0] == "x":
    position = axes._project_x(position)
    series = axes._project_y(series)
  elif mark._coordinate_axes[0] == "y":
    position = axes._project_y(position)
    series = axes._project_x(series)

  mark_xml = xml.SubElement(context.root, "g", style=_css_style(mark._style), id=context.get_id(mark), attrib={"class":"toyplot-mark-Plot"})
  _render_data_table(mark_xml, mark._table, title="Plot Data")

  for series, stroke, stroke_width, stroke_opacity, title, marker, size, fill, opacity  in zip(series.T, mark._stroke.T, mark._stroke_width.T, mark._stroke_opacity.T, mark._title.T, [mark._table[key] for key in mark._marker], [mark._table[key] for key in mark._size], [mark._table[key] for key in mark._fill], [mark._table[key] for key in mark._opacity]):
    not_null = numpy.invert(numpy.logical_or(numpy.ma.getmaskarray(position), numpy.ma.getmaskarray(series)))
    segments = _flat_contiguous(not_null)

    size = numpy.sqrt(size)
    stroke_style = toyplot.style.combine({"stroke":toyplot.color.to_css(stroke), "stroke-width":stroke_width, "stroke-opacity":stroke_opacity}, mark._style)
    if mark._coordinate_axes[0] == "x":
      x = position
      y = series
    elif mark._coordinate_axes[0] == "y":
      x = series
      y = position
    series_xml = xml.SubElement(mark_xml, "g", attrib={"class":"toyplot-Series"})
    if mark._show_stroke:
      d = []
      for segment in segments:
        start, stop, step = segment.indices(len(not_null))
        for i in range(start, start+1):
          d.append("M %r %r" % (x[i], y[i]))
        for i in range(start+1, stop):
          d.append("L %r %r" % (x[i], y[i]))
      xml.SubElement(series_xml, "path", d=" ".join(d), style=_css_style(stroke_style))
    for dx, dy, dmarker, dsize, dfill, dopacity in zip(x[not_null], y[not_null], marker[not_null], size[not_null], fill[not_null], opacity[not_null]):
      dstyle = toyplot.style.combine({"fill":toyplot.color.to_css(dfill),"opacity":dopacity}, mark._mstyle)
      _render_marker(series_xml, dx, dy, dsize, dmarker, dstyle, mark._mlstyle, extra_class="toyplot-Datum")

    if title is not None:
      xml.SubElement(series_xml, "title").text = str(title)

@dispatch(toyplot.axes.Cartesian, toyplot.mark.Rect, _RenderContext)
def _render(axes, mark, context):
  if mark._left_right_axis == "x":
    x1 = axes._project_x(mark._table[mark._left[0]])
    x2 = axes._project_x(mark._table[mark._right[0]])
    y1 = axes._project_y(mark._table[mark._top[0]])
    y2 = axes._project_y(mark._table[mark._bottom[0]])
  elif mark._left_right_axis == "y":
    x1 = axes._project_x(mark._table[mark._top[0]])
    x2 = axes._project_x(mark._table[mark._bottom[0]])
    y1 = axes._project_y(mark._table[mark._left[0]])
    y2 = axes._project_y(mark._table[mark._right[0]])
  mark_xml = xml.SubElement(context.root, "g", style=_css_style(mark._style), id=context.get_id(mark), attrib={"class":"toyplot-mark-Rect"})
  _render_data_table(mark_xml, mark._table, title="Rect Data")

  series_xml = xml.SubElement(mark_xml, "g", attrib={"class":"toyplot-Series"})
  for dx1, dx2, dy1, dy2, dfill, dopacity, dtitle in zip(x1, x2, y1, y2, mark._table[mark._fill[0]], mark._table[mark._opacity[0]], mark._table[mark._title[0]]):
    dstyle = toyplot.style.combine({"fill":toyplot.color.to_css(dfill), "opacity":dopacity}, mark._style)
    datum_xml = xml.SubElement(series_xml, "rect", attrib={"class":"toyplot-Datum"}, x=repr(min(dx1, dx2)), y=repr(min(dy1, dy2)), width=repr(numpy.abs(dx1 - dx2)), height=repr(numpy.abs(dy1 - dy2)), style=_css_style(dstyle))
    if dtitle is not None:
      xml.SubElement(datum_xml, "title").text = str(dtitle)

@dispatch((toyplot.canvas.Canvas, toyplot.axes.Cartesian), toyplot.mark.Text, _RenderContext)
def _render(parent, mark, context):
  x = mark._table[mark._coordinates[numpy.where(mark._axes == "x")[0][0]]]
  y = mark._table[mark._coordinates[numpy.where(mark._axes == "y")[0][0]]]

  if isinstance(parent, toyplot.axes.Cartesian):
    x = parent._project_x(x)
    y = parent._project_y(y)

  mark_xml = xml.SubElement(context.root, "g", style=_css_style(mark._style), id=context.get_id(mark), attrib={"class":"toyplot-mark-Text"})
  _render_data_table(mark_xml, mark._table, title="Text Data")
  series_xml = xml.SubElement(mark_xml, "g", attrib={"class":"toyplot-Series"})
  for dx, dy, dtext, dangle, dfill, dopacity, dtitle in zip(x, y, mark._table[mark._text[0]], mark._table[mark._angle[0]], mark._table[mark._fill[0]], mark._table[mark._opacity[0]], mark._table[mark._title[0]]):
    dstyle = toyplot.style.combine({"fill":toyplot.color.to_css(dfill), "opacity":dopacity}, mark._style)
    datum_xml = xml.SubElement(series_xml, "text", attrib={"class":"toyplot-Datum"}, x=repr(dx), y=repr(dy), transform="rotate(%r, %r, %r)" % (dangle, dx, dy), style=_css_style(dstyle))
    if dtext is not None:
      datum_xml.text = str(dtext)
    if dtitle is not None:
      xml.SubElement(datum_xml, "title").text = str(dtitle)

@dispatch(toyplot.canvas.Canvas, toyplot.mark.VColorBar, _RenderContext)
def _render(canvas, mark, context):
  mark._finalize_domain()

  xmin = mark._xmin_range
  xmax = mark._xmax_range

  ymin = mark._project_y(mark._vmax_computed)
  ymax = mark._project_y(mark._vmin_computed)
  samples = numpy.linspace(mark._vmax_computed, mark._vmin_computed, 256, endpoint=True)
  swatch_size = (ymax - ymin) / (len(samples) - 1)
  swatches = numpy.linspace(ymin - (swatch_size / 2), ymax + (swatch_size / 2), len(samples) + 1, endpoint=True)

  mark_xml = xml.SubElement(context.root, "g", style=_css_style(mark._style), id=context.get_id(mark), attrib={"class":"toyplot-mark-VColorBar"})
  for sample, y1, y2 in zip(samples, swatches[:-1], swatches[1:]):
    color = mark._project_color(sample)
    xml.SubElement(mark_xml, "rect", x=repr(xmin), y=repr(y1), width=repr(xmax - xmin), height=repr((y2-y1) + (swatch_size / 2)), style=_css_style({"stroke":"none", "fill":toyplot.color.to_css(color)}))

  if mark.ticks._show:
    ticks_group = xml.SubElement(mark_xml, "g")
    for location, tick_style in zip(mark._tick_locations, mark.ticks.tick.styles(mark._tick_locations)):
      y = mark._project_y(location)
      x1 = mark._xmax_range
      x2 = mark._xmax_range + mark.ticks._length
      xml.SubElement(ticks_group, "line", x1=repr(x1), y1=repr(y), x2=repr(x2), y2=repr(y), style=_css_style(mark.ticks._style, tick_style))

  if mark.ticks.labels._show:
    ticks_group = xml.SubElement(mark_xml, "g")
    for location, label, title, label_style in zip(mark._tick_locations, mark._tick_labels, mark._tick_titles, mark.ticks.labels.label.styles(mark._tick_locations)):
      x = mark._xmax_range + (mark.ticks._length if mark.ticks._show else 0)
      y = mark._project_y(location)
      label_xml = xml.SubElement(ticks_group, "text", x=repr(x), y=repr(y), transform="rotate(-90, %r, %r)" % (x, y), style=_css_style({"text-anchor":"middle", "alignment-baseline":"middle", "baseline-shift":"-80%"}, mark.ticks.labels._style, label_style))
      label_xml.text = label
      if title is not None:
        xml.SubElement(label_xml, "title").text = str(title)

  if mark.label._text is not None:
    x = mark._xmax_range + (mark.ticks._length if mark.ticks._show else 0)
    y = (mark._ymin_range + mark._ymax_range) * 0.5
    xml.SubElement(mark_xml, "text", x=repr(x), y=repr(y), transform="rotate(-90, %r, %r)" % (x, y), style=_css_style(mark.label._style)).text = mark.label._text

