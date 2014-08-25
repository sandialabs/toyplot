# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

import collections
import itertools
import json
import numbers
import numpy
import toyplot.color.css
import uuid
import xml.etree.ElementTree as xml

def apply_changes(svg, changes):
  for change_type, instructions in changes.items():
    if change_type == "set-mark-style":
      for mark_id, style in instructions:
        mark = svg.find(".//*[@id='%s']" % mark_id)
        computed_style = dict([declaration.split(":") for declaration in mark.get("style").split(";") if declaration != ""])
        computed_style.update(style)
        mark.set("style", _css_style(computed_style))
    elif change_type == "set-datum-style":
      for mark_id, series, datum, style in instructions:
        mark_xml = svg.find(".//*[@id='%s']" % mark_id)
        series_xml = mark_xml.findall("*[@class='toyplot-Series']")[series]
        datum_xml = series_xml.findall("*[@class='toyplot-Datum']")[datum]
        computed_style = dict([declaration.split(":") for declaration in datum_xml.get("style").split(";") if declaration != ""])
        computed_style.update(style)
        datum_xml.set("style", _css_style(computed_style))
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
  canvas : :class:`toyplot.Canvas`
    The canvas to be rendered.

  fobj : file-like object or string, optional
    The file to write.  Use a string filepath to write data directly to disk.
    If `None` (the default), the SVG tree will be returned to the caller
    instead.

  animation : boolean, optional
    If `True`, return a representation of the changes to be made to the SVG
    tree for animation.

  Returns
  -------
  svg : xml.etree.ElementTree.Element or `None`
    SVG representation of `canvas`, as a DOM tree, or `None` if the caller
    specifies the `fobj` parameter.

  changes : JSON-compatible data structure, or `None`
    JSON-compatible representation of the animated changes to `canvas`.

  Notes
  -----
  The SVG representation of a canvas should be considered the "canonical"
  representation - the other toyplot backends operate by converting the output
  from toyplot.svg.render() to the desired end target.
  """

  canvas.autorender(False)

  id_cache = _id_cache()

  svg = xml.Element("svg", xmlns="http://www.w3.org/2000/svg", attrib={"xmlns:toyplot":"http://www.sandia.gov/toyplot"}, width="%spx" % canvas._width, height="%spx" % canvas._height, style=_css_style(canvas._style), id=id_cache(canvas))
  for child in canvas._children:
    _render_item(svg, child, canvas, id_cache)

  if isinstance(fobj, basestring):
    with open(fobj, "w") as file:
      file.write(xml.tostring(svg, method="xml"))
  elif fobj is not None:
    fobj.write(xml.tostring(svg, method="xml"))
  else:
    if animation:
      svg_animation = collections.defaultdict(lambda : collections.defaultdict(list))
      for time, time_changes in canvas._animation.iteritems():
        svg_animation[time] # Ensure we have an entry for every time, even if there aren't any changes.
        for type, type_changes in time_changes.iteritems():
          for change in type_changes:
            svg_animation[time][type].append([id_cache(change[0])] + list(change[1:]))
      return svg, svg_animation
    else:
      return svg





















def _css_style(*styles):
  computed_style = {}
  for style in styles:
    if style is not None:
      computed_style.update(style)
  return "".join(["%s:%s;" % (key, value) for key, value in computed_style.items()])

def _css_attrib(*styles):
  computed_style = {}
  for style in styles:
    if style is not None:
      computed_style.update(style)
  attrib = {}
  if len(computed_style):
    attrib["style"] =  "".join(["%s:%s;" % (key, value) for key, value in computed_style.items()])
  return attrib

class _id_cache(object):
  def __init__(self):
    self._cache = {}
  def __call__(self, object):
    python_id = id(object)
    if python_id not in self._cache:
      self._cache[python_id] = "t" + uuid.uuid4().hex
    return self._cache[python_id]

def _flat_contiguous(a):
  i = 0
  result = []
  for (k, g) in itertools.groupby(a.ravel()):
      n = len(list(g))
      if k:
          result.append(slice(i, i + n))
      i += n
  return result

def _render_marker(root, cx, cy, size, marker, marker_style=None, label_style=None, extra_class=None):
  if marker is None:
    return
  if isinstance(marker, basestring):
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
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle, cx, cy), x1=str(cx), x2=str(cx), y1=str(cy - (size / 2)), y2=str(cy + (size / 2)))
  elif shape == "+":
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle, cx, cy), x1=str(cx), x2=str(cx), y1=str(cy - (size / 2)), y2=str(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle, cx, cy), x1=str(cx - (size / 2)), x2=str(cx + (size / 2)), y1=str(cy), y2=str(cy))
  elif shape == "*":
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle, cx, cy), x1=str(cx), x2=str(cx), y1=str(cy - (size / 2)), y2=str(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle - 60, cx, cy), x1=str(cx), x2=str(cx), y1=str(cy - (size / 2)), y2=str(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle + 60, cx, cy), x1=str(cx), x2=str(cx), y1=str(cy - (size / 2)), y2=str(cy + (size / 2)))
  elif shape == "^":
    xml.SubElement(marker_xml, "polygon", transform="rotate(%s, %s, %s)" % (shape_angle, cx, cy), points=" ".join(["%s,%s" % (xp, yp) for xp, yp in [(cx - (size / 2), cy + (size / 2)), (cx, cy - (size / 2)), (cx + (size / 2), cy + (size / 2))]]))
  elif shape == "s":
    xml.SubElement(marker_xml, "rect", transform="rotate(%s, %s, %s)" % (shape_angle, cx, cy), x=str(cx-(size / 2)), y=str(cy-(size / 2)), width=str(size), height=str(size))
  elif shape == "o":
    xml.SubElement(marker_xml, "circle", cx=str(cx), cy=str(cy), r=str(size / 2))
  elif shape == "oo":
    xml.SubElement(marker_xml, "circle", cx=str(cx), cy=str(cy), r=str(size / 2))
    xml.SubElement(marker_xml, "circle", cx=str(cx), cy=str(cy), r=str(size / 4))
  elif shape == "o|":
    xml.SubElement(marker_xml, "circle", cx=str(cx), cy=str(cy), r=str(size / 2))
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle, cx, cy), x1=str(cx), x2=str(cx), y1=str(cy - (size / 2)), y2=str(cy + (size / 2)))
  elif shape == "o+":
    xml.SubElement(marker_xml, "circle", cx=str(cx), cy=str(cy), r=str(size / 2))
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle, cx, cy), x1=str(cx), x2=str(cx), y1=str(cy - (size / 2)), y2=str(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle, cx, cy), x1=str(cx - (size / 2)), x2=str(cx + (size / 2)), y1=str(cy), y2=str(cy))
  elif shape == "o*":
    xml.SubElement(marker_xml, "circle", cx=str(cx), cy=str(cy), r=str(size / 2))
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle, cx, cy), x1=str(cx), x2=str(cx), y1=str(cy - (size / 2)), y2=str(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle - 60, cx, cy), x1=str(cx), x2=str(cx), y1=str(cy - (size / 2)), y2=str(cy + (size / 2)))
    xml.SubElement(marker_xml, "line", transform="rotate(%s, %s, %s)" % (shape_angle + 60, cx, cy), x1=str(cx), x2=str(cx), y1=str(cy - (size / 2)), y2=str(cy + (size / 2)))
  elif shape == "path":
    shape_path = marker.get("path")
    xml.SubElement(marker_xml, "path", transform="translate(%s, %s) scale(%s) translate(%s, %s)" % (cx, cy, size, -cx, -cy), d="M " + str(cx) + " " + str(cy) + shape_path)

  if shape_label is not None:
    xml.SubElement(marker_xml, "text", x=str(cx), y=str(cy), attrib=_css_attrib({"stroke":"none", "fill":"black", "text-anchor":"middle", "alignment-baseline":"middle", "font-size":"%spx" % (size * 0.75)}, label_style, shape_label_style)).text = shape_label
_render_marker.variations = {"-" : ("|", 90), "x" : ("+", 45), "v" : ("^", 180), "<" : ("^", -90), ">" : ("^", 90), "d" : ("s", 45), "o-" : ("o|", 90), "ox" : ("o+", 45)}

def _render_Axes2D(root, item, parent, id_cache):
  item._finalize_domain()

  axes_data = {"x":[], "y":[]}
  if item.x._scale == "linear":
    axes_data["x"].append({"scale":"linear", "range":{"min":item._xmin_range + item._padding, "max":item._xmax_range - item._padding}, "domain":{"min":item._xmin_computed, "max":item._xmax_computed}})
  else:
    scale, base = item.x._scale
    if scale == "log":
      if item._xmax_computed < 0 or item._xmin_computed > 0:
        axes_data["x"].append({"scale":"log", "base":base, "range":{"min":item._xmin_range + item._padding, "max":item._xmax_range - item._padding}, "domain":{"min":item._xmin_computed, "max":item._xmax_computed}})
      else:
        axes_data["x"].append({"scale":"log", "base":base, "range":{"min":item._xmin_range + item._padding, "max":item._project_x(-1.0)}, "domain":{"min":item._xmin_computed, "max":-1.0}})
        axes_data["x"].append({"scale":"linear", "range":{"min":item._project_x(-1.0), "max":item._project_x(1.0)}, "domain":{"min":-1.0, "max":1.0}})
        axes_data["x"].append({"scale":"log", "base":base, "range":{"min":item._project_x(1.0), "max":item._xmax_range - item._padding}, "domain":{"min":1.0, "max":item._xmax_computed}})

  if item.y._scale == "linear":
    axes_data["y"].append({"scale":"linear", "range":{"min":item._ymin_range + item._padding, "max":item._ymax_range - item._padding}, "domain":{"min":item._ymin_computed, "max":item._ymax_computed}})
  else:
    scale, base = item.y._scale
    if scale == "log":
      if item._ymax_computed < 0 or item._ymin_computed > 0:
        axes_data["y"].append({"scale":"log", "base":base, "range":{"min":item._ymin_range + item._padding, "max":item._ymax_range - item._padding}, "domain":{"min":item._ymin_computed, "max":item._ymax_computed}})
      else:
        axes_data["y"].append({"scale":"log", "base":base, "range":{"min":item._project_y(-1.0), "max":item._ymax_range - item._padding}, "domain":{"min":item._ymin_computed, "max":-1.0}})
        axes_data["y"].append({"scale":"linear", "range":{"min":item._project_y(1.0), "max":item._project_y(-1.0)}, "domain":{"min":-1.0, "max":1.0}})
        axes_data["y"].append({"scale":"log", "base":base, "range":{"min":item._ymin_range + item._padding, "max":item._project_y(1.0)}, "domain":{"min":1.0, "max":item._ymax_computed}})

  item_xml = xml.SubElement(root, "g", id=id_cache(item), attrib={"class":"toyplot-Axes2D"})
  xml.SubElement(item_xml, "toyplot:axes").text = json.dumps(axes_data)

  clip_xml = xml.SubElement(item_xml, "clipPath", id="t" + uuid.uuid4().hex)
  xml.SubElement(clip_xml, "rect", x=str(item._xmin_range), y=str(item._ymin_range), width=str(item._xmax_range - item._xmin_range), height=str(item._ymax_range - item._ymin_range))

  children_xml = xml.SubElement(item_xml, "g", attrib={"class":"toyplot-coordinate-events", "clip-path":"url(#%s)" % clip_xml.get("id")}, style=_css_style({"cursor":"crosshair"}))
  xml.SubElement(children_xml, "rect", x=str(item._xmin_range), y=str(item._ymin_range), width=str(item._xmax_range - item._xmin_range), height=str(item._ymax_range - item._ymin_range), style=_css_style({"visibility":"hidden", "pointer-events":"all"}))
  for child in item._children:
    _render_item(children_xml, child, item, id_cache)

  if item.coordinates._show:
    coordinates_xml = xml.SubElement(item_xml, "g", style=_css_style({"visibility":"hidden"}), attrib={"class":"toyplot-coordinates"})
    xml.SubElement(coordinates_xml, "rect", x=str(item.coordinates._xmin_range), y=str(item.coordinates._ymin_range), width=str(item.coordinates._xmax_range - item.coordinates._xmin_range), height=str(item.coordinates._ymax_range - item.coordinates._ymin_range), style=_css_style(item.coordinates._style))
    xml.SubElement(coordinates_xml, "text", x=str((item.coordinates._xmin_range + item.coordinates._xmax_range) * 0.5), y=str((item.coordinates._ymin_range + item.coordinates._ymax_range) * 0.5), style=_css_style(item.coordinates.label._style))

  if item._show:
    if item.x.spine._position == "low":
      spine_y = item._ymax_range
    elif item.x.spine._position == "high":
      spine_y = item._ymin_range
    else:
      spine_y = item._project_y(item.x.spine._position)

    if item.y.spine._position == "low":
      spine_x = item._xmin_range
    elif item.y.spine._position == "high":
      spine_x = item._xmax_range
    else:
      spine_x = item._project_x(item.y.spine._position)

    if item.x._show:
      if item.x.spine._show:
        x1 = item._xmin_range
        x2 = item._xmax_range
        if item._xmin_implicit is not None:
          x1 = max(x1, item._project_x(item._xmin_implicit))
          x2 = min(x2, item._project_x(item._xmax_implicit))
        xml.SubElement(item_xml, "line", x1=str(x1), y1=str(spine_y), x2=str(x2), y2=str(spine_y), style=_css_style(item.x.spine._style))

      if item.x.ticks._show:
        ticks_group = xml.SubElement(item_xml, "g")
        for location, tick_style in zip(item._xtick_locations, item.x.ticks.tick.styles(item._xtick_locations)):
          x = item._project_x(location)
          y1 = item._ymax_range
          y2 = item._ymax_range - item.x.ticks._length
          xml.SubElement(ticks_group, "line", x1=str(x), y1=str(y1), x2=str(x), y2=str(y2), style=_css_style(item.x.ticks._style, tick_style))

      if item.x.ticks.labels._show:
        ticks_group = xml.SubElement(item_xml, "g")
        for location, label, title, label_style in zip(item._xtick_locations, item._xtick_labels, item._xtick_titles, item.x.ticks.labels.label.styles(item._xtick_locations)):
          x = item._project_x(location)
          y = item._ymax_range
          label_xml = xml.SubElement(ticks_group, "text", x=str(x), y=str(y), style=_css_style({"text-anchor":"middle", "alignment-baseline":"middle", "baseline-shift":"-80%"}, item.x.ticks.labels._style, label_style))
          label_xml.text = label
          if item.x.ticks.labels._angle:
            label_xml.set("transform", "rotate(%s, %s, %s)" % (item.x.ticks.labels._angle, x, y))
          if title is not None:
            xml.SubElement(label_xml, "title").text = str(title)

      if item.x.label._text is not None:
        x = (item._xmin_range + item._xmax_range) * 0.5
        y = item._ymax_range
        xml.SubElement(item_xml, "text", x=str(x), y=str(y), style=_css_style(item.x.label._style)).text = item.x.label._text

    if item.y._show:
      if item.y.spine._show:
        y1 = item._ymin_range
        y2 = item._ymax_range
        if item._ymin_implicit is not None:
          y1 = max(y1, item._project_y(item._ymax_implicit))
          y2 = min(y2, item._project_y(item._ymin_implicit))
        xml.SubElement(item_xml, "line", x1=str(spine_x), y1=str(y1), x2=str(spine_x), y2=str(y2), style=_css_style(item.y.spine._style))

      if item.y.ticks._show:
        ticks_group = xml.SubElement(item_xml, "g")
        for location, tick_style in zip(item._ytick_locations, item.y.ticks.tick.styles(item._ytick_locations)):
          y = item._project_y(location)
          x1 = item._xmin_range
          x2 = item._xmin_range + item.y.ticks._length
          xml.SubElement(ticks_group, "line", x1=str(x1), y1=str(y), x2=str(x2), y2=str(y), style=_css_style(item.y.ticks._style, tick_style))

      if item.y.ticks.labels._show:
        ticks_group = xml.SubElement(item_xml, "g")
        for location, label, title, label_style in zip(item._ytick_locations, item._ytick_labels, item._ytick_titles, item.y.ticks.labels.label.styles(item._ytick_locations)):
          x = item._xmin_range
          y = item._project_y(location)
          label_xml = xml.SubElement(ticks_group, "text", x=str(x), y=str(y), style=_css_style({"text-anchor":"middle", "alignment-baseline":"middle", "baseline-shift":"80%"}, item.y.ticks.labels._style, label_style))
          label_xml.text = label
          if item.y.ticks.labels._angle:
            label_xml.set("transform", "rotate(%s, %s, %s)" % (item.y.ticks.labels._angle, x, y))
          if title is not None:
            xml.SubElement(label_xml, "title").text = str(title)

      if item.y.label._text is not None:
        x = item._xmin_range
        y = (item._ymin_range + item._ymax_range) * 0.5
        xml.SubElement(item_xml, "text", x=str(x), y=str(y), transform="rotate(-90, %s, %s)" % (x, y), style=_css_style(item.y.label._style)).text = item.y.label._text

    if item.label._text is not None:
      x = (item._xmin_range + item._xmax_range) * 0.5
      y = item._ymin_range
      xml.SubElement(item_xml, "text", x=str(x), y=str(y), style=_css_style(item.label._style)).text = item.label._text

def _render_BarBoundariesMark(root, item, parent, id_cache):
  bar1 = item._position.T[0]
  bar2 = item._position.T[1]

  if isinstance(parent, toyplot.Axes2D):
    if item._along == "x":
      axis1 = "x"
      axis2 = "y"
      distance1 = "width"
      distance2 = "height"
      bar1 = parent._project_x(bar1)
      bar2 = parent._project_x(bar2)
      boundaries = parent._project_y(item._series)
    elif item._along == "y":
      axis1 = "y"
      axis2 = "x"
      distance1 = "height"
      distance2 = "width"
      bar1 = parent._project_y(bar1)
      bar2 = parent._project_y(bar2)
      boundaries = parent._project_x(item._series)

  item_xml = xml.SubElement(root, "g", style=_css_style(item._style), id=id_cache(item), attrib={"class":"toyplot-BarBoundariesMark"})

  xml.SubElement(item_xml, "toyplot:data-table", title="Bar Data").text = json.dumps({"names":["position"] + ["series%s" % s for s in range(item._series.shape[1])], "data":[item._position.tolist()] + [s.tolist() for s in item._series.T]})

  for boundary1, boundary2, fill, opacity, title in zip(boundaries.T[:-1], boundaries.T[1:], item._fill.T, item._opacity.T, item._title.T):
    not_null = numpy.invert(numpy.logical_or(numpy.ma.getmaskarray(boundary1), numpy.ma.getmaskarray(boundary2)))

    series_xml = xml.SubElement(item_xml, "g", attrib={"class":"toyplot-Series"})
    for dbar1, dbar2, dboundary1, dboundary2, dfill, dopacity, dtitle in zip(bar1[not_null], bar2[not_null], boundary1[not_null], boundary2[not_null], fill[not_null], opacity[not_null], title[not_null]):
      dstyle = {"fill":toyplot.color.css.convert(dfill), "opacity":dopacity}
      dstyle.update(item._style)
      datum_xml = xml.SubElement(series_xml, "rect", attrib={"class":"toyplot-Datum", axis1:str(min(dbar1, dbar2)), axis2:str(min(dboundary1, dboundary2)), distance1:str(numpy.abs(dbar1 - dbar2)), distance2:str(numpy.abs(dboundary1 - dboundary2))}, style=_css_style(dstyle))
      if dtitle is not None:
        xml.SubElement(datum_xml, "title").text = str(dtitle)

def _render_BarMagnitudesMark(root, item, parent, id_cache):
  bar1 = item._position.T[0]
  bar2 = item._position.T[1]
  boundaries = numpy.ma.cumsum(numpy.ma.column_stack((item._baseline, item._series)), axis=1)
  not_null = numpy.invert(numpy.ma.any(numpy.ma.getmaskarray(boundaries), axis=1))

  if isinstance(parent, toyplot.Axes2D):
    if item._along == "x":
      axis1 = "x"
      axis2 = "y"
      distance1 = "width"
      distance2 = "height"
      bar1 = parent._project_x(bar1)
      bar2 = parent._project_x(bar2)
      boundaries = parent._project_y(boundaries)
    elif item._along == "y":
      axis1 = "y"
      axis2 = "x"
      distance1 = "height"
      distance2 = "width"
      bar1 = parent._project_y(bar1)
      bar2 = parent._project_y(bar2)
      boundaries = parent._project_x(boundaries)

  item_xml = xml.SubElement(root, "g", style=_css_style(item._style), id=id_cache(item), attrib={"class":"toyplot-BarMagnitudesMark"})

  xml.SubElement(item_xml, "toyplot:data-table", title="Bar Data").text = json.dumps({"names":["position0", "position1"] + ["series%s" % s for s in range(item._series.shape[1])], "data":[p.tolist() for p in item._position.T] + [s.tolist() for s in item._series.T]})

  for boundary1, boundary2, fill, opacity, title in zip(boundaries.T[:-1], boundaries.T[1:], item._fill.T, item._opacity.T, item._title.T):
    series_xml = xml.SubElement(item_xml, "g", attrib={"class":"toyplot-Series"})
    for dbar1, dbar2, dboundary1, dboundary2, dfill, dopacity, dtitle in zip(bar1[not_null], bar2[not_null], boundary1[not_null], boundary2[not_null], fill[not_null], opacity[not_null], title[not_null]):
      dstyle = {"fill":toyplot.color.css.convert(dfill), "opacity":dopacity}
      dstyle.update(item._style)
      datum_xml = xml.SubElement(series_xml, "rect", attrib={"class":"toyplot-Datum", axis1:str(min(dbar1, dbar2)), axis2:str(min(dboundary1, dboundary2)), distance1:str(numpy.abs(dbar1 - dbar2)), distance2:str(numpy.abs(dboundary1 - dboundary2))}, style=_css_style(dstyle))
      if dtitle is not None:
        xml.SubElement(datum_xml, "title").text = str(dtitle)

def _render_FillBoundariesMark(root, item, parent, id_cache):
  if isinstance(parent, toyplot.Axes2D):
    if item._along == "x":
      position = parent._project_x(item._position)
      boundaries = parent._project_y(item._series)
    elif item._along == "y":
      position = parent._project_y(item._position)
      boundaries = parent._project_x(item._series)

  item_xml = xml.SubElement(root, "g", style=_css_style(item._style), id=id_cache(item), attrib={"class":"toyplot-FillBoundariesMark"})

  xml.SubElement(item_xml, "toyplot:data-table", title="Fill Data").text = json.dumps({"names":["position"] + ["series%s" % s for s in range(item._series.shape[1])], "data":[item._position.tolist()] + [s.tolist() for s in item._series.T]})

  for boundary1, boundary2, fill, opacity, title in zip(boundaries.T[:-1], boundaries.T[1:], item._fill, item._opacity, item._title):
    not_null = numpy.invert(numpy.logical_or(numpy.ma.getmaskarray(boundary1), numpy.ma.getmaskarray(boundary2)))
    segments = _flat_contiguous(not_null)

    series_style = {"fill":toyplot.color.css.convert(fill), "opacity":opacity}
    series_style.update(item._style)

    for segment in segments:
      if item._along == "x":
        coordinates = zip(numpy.concatenate((position[segment], position[segment][::-1])), numpy.concatenate((boundary1[segment], boundary2[segment][::-1])))
      elif item._along == "y":
        coordinates = zip(numpy.concatenate((boundary1[segment], boundary2[segment][::-1])), numpy.concatenate((position[segment], position[segment][::-1])))
      series_xml = xml.SubElement(item_xml, "polygon", points=" ".join(["%s,%s" % (xi, yi) for xi, yi in coordinates]), style=_css_style(series_style))
      if title is not None:
        xml.SubElement(series_xml, "title").text = str(title)

def _render_FillMagnitudesMark(root, item, parent, id_cache):
  magnitudes = numpy.ma.column_stack((item._baseline, item._series))
  boundaries = numpy.ma.cumsum(magnitudes, axis=1)
  not_null = numpy.invert(numpy.ma.any(numpy.ma.getmaskarray(boundaries), axis=1))
  segments = _flat_contiguous(not_null)

  if isinstance(parent, toyplot.Axes2D):
    if item._along == "x":
      position = parent._project_x(item._position)
      boundaries = parent._project_y(boundaries)
    elif item._along == "y":
      position = parent._project_y(item._position)
      boundaries = parent._project_x(boundaries)

  item_xml = xml.SubElement(root, "g", style=_css_style(item._style), id=id_cache(item), attrib={"class":"toyplot-FillMagnitudesMark"})

  xml.SubElement(item_xml, "toyplot:data-table", title="Fill Data").text = json.dumps({"names":["position"] + ["series%s" % s for s in range(item._series.shape[1])], "data":[item._position.tolist()] + [s.tolist() for s in item._series.T]})

  for boundary1, boundary2, fill, opacity, title in zip(boundaries.T[:-1], boundaries.T[1:], item._fill, item._opacity, item._title):
    series_style = {"fill":toyplot.color.css.convert(fill), "opacity":opacity}
    series_style.update(item._style)
    for segment in segments:
      if item._along == "x":
        coordinates = zip(numpy.concatenate((position[segment], position[segment][::-1])), numpy.concatenate((boundary1[segment], boundary2[segment][::-1])))
      elif item._along == "y":
        coordinates = zip(numpy.concatenate((boundary1[segment], boundary2[segment][::-1])), numpy.concatenate((position[segment], position[segment][::-1])))
      series_xml = xml.SubElement(item_xml, "polygon", points=" ".join(["%s,%s" % (xi, yi) for xi, yi in coordinates]), style=_css_style(series_style))
      if title is not None:
        xml.SubElement(series_xml, "title").text = str(title)

def _render_AxisLinesMark(root, item, parent, id_cache):
  if isinstance(parent, toyplot.Axes2D):
    if item._along == "x":
      p1="x1"
      p2="x2"
      b1="y1"
      b2="y2"
      position = parent._project_x(item._position)
      boundary1 = parent._ymin_range
      boundary2 = parent._ymax_range
    elif item._along == "y":
      p1="y1"
      p2="y2"
      b1="x1"
      b2="x2"
      position = parent._project_y(item._position)
      boundary1 = parent._xmin_range
      boundary2 = parent._xmax_range
  item_xml = xml.SubElement(root, "g", style=_css_style(item._style), id=id_cache(item), attrib={"class":"toyplot-AxisLinesMark"})
  series_xml = xml.SubElement(item_xml, "g", attrib={"class":"toyplot-Series"})
  for dposition, dstroke, dopacity, dtitle in zip(position, item._stroke, item._opacity, item._title):
    dstyle = {"stroke":toyplot.color.css.convert(dstroke), "opacity":dopacity}
    dstyle.update(item._style)
    datum_xml = xml.SubElement(series_xml, "line", attrib={"class":"toyplot-Datum",p1:str(dposition), p2:str(dposition), b1:str(boundary1), b2:str(boundary2)}, style=_css_style(dstyle))
    if dtitle is not None:
      xml.SubElement(datum_xml, "title").text = str(dtitle)

def _render_LegendMark(root, item, parent, id_cache):
  x = item._xmin
  y = item._ymin
  width = item._xmax - item._xmin
  height = item._ymax - item._ymin
  xml.SubElement(root, "rect", x=str(x), y=str(y), width=str(width), height=str(height), style=_css_style(item._style), id=id_cache(item), attrib={"class":"toyplot-LegendMark"})

  mark_count = len(item._marks)
  if mark_count:
    mark_gutter = item._gutter
    mark_height = (height - (item._gutter * (mark_count+1))) / mark_count

    for i, mark in enumerate(item._marks):
      mark_x = x + mark_gutter
      mark_y = y + ((i + 1) * mark_gutter) + (i * mark_height)
      mark_width = mark_height

      mark_style = {}
      if isinstance(mark, tuple) and len(mark) == 2:
        mark_label, mark_type = mark
      elif isinstance(mark, tuple) and len(mark) == 3:
        mark_label, mark_type, mark_style = mark

      if mark_type == "line":
        xml.SubElement(root, "line", x1=str(mark_x), y1=str(mark_y + mark_height), x2=str(mark_x + mark_width), y2=str(mark_y), style=_css_style(mark_style))
      elif mark_type == "rect":
        xml.SubElement(root, "rect", x=str(mark_x), y=str(mark_y), width=str(mark_width), height=str(mark_height), style=_css_style({"stroke":"none"}, mark_style))
      elif isinstance(mark_type, toyplot.PlotMark):
        dstyle = {"stroke":toyplot.color.css.convert(mark_type._stroke[0])}
        dstyle.update(mark_type._style)
        xml.SubElement(root, "line", x1=str(mark_x), y1=str(mark_y + mark_height), x2=str(mark_x + mark_width), y2=str(mark_y), style=_css_style(dstyle, mark_style))
      elif isinstance(mark_type, (toyplot.BarBoundariesMark, toyplot.BarMagnitudesMark, toyplot.FillBoundariesMark, toyplot.FillMagnitudesMark)):
        dstyle = {"fill":toyplot.color.css.convert(mark_type._fill[0]), "opacity":mark_type._opacity[0]}
        dstyle.update(mark_type._style)
        xml.SubElement(root, "rect", x=str(mark_x), y=str(mark_y), width=str(mark_width), height=str(mark_height), style=_css_style(dstyle, mark_style))
      else:
        computed_style = {"stroke":"black", "fill":"none"}
        computed_style.update(mark_style)
        _render_marker(root, mark_x + (mark_width / 2), mark_y + (mark_height / 2), min(mark_width, mark_height), mark_type, computed_style, {})

      label_x = x + mark_width + (2 * mark_gutter)
      label_y = y + ((i + 1) * mark_gutter) + (i * mark_height) + (mark_height / 2)
      xml.SubElement(root, "text", x=str(label_x), y=str(label_y), style=_css_style({"alignment-baseline":"middle", "stroke":"none"}, item._label_style)).text = mark_label

def _render_PlotMark(root, item, parent, id_cache):
  if isinstance(parent, toyplot.Axes2D):
    if item._along == "x":
      position = parent._project_x(item._position)
      series = parent._project_y(item._series)
    elif item._along == "y":
      position = parent._project_y(item._position)
      series = parent._project_x(item._series)

  item_xml = xml.SubElement(root, "g", style=_css_style(item._style), id=id_cache(item), attrib={"class":"toyplot-PlotMark"})

  xml.SubElement(item_xml, "toyplot:data-table", title="Plot Data").text = json.dumps({"names":["position"] + ["series%s" % s for s in range(item._series.shape[1])], "data":[item._position.tolist()] + [s.tolist() for s in item._series.T]})

  for series, stroke, stroke_width, stroke_opacity, title, marker, size, fill, opacity  in zip(series.T, item._stroke.T, item._stroke_width.T, item._stroke_opacity.T, item._title.T, item._marker.T, item._size.T, item._fill.T, item._opacity.T):
    not_null = numpy.invert(numpy.logical_or(numpy.ma.getmaskarray(position), numpy.ma.getmaskarray(series)))
    segments = _flat_contiguous(not_null)

    size = numpy.sqrt(size)
    stroke_style = {"stroke":toyplot.color.css.convert(stroke), "stroke-width":stroke_width, "stroke-opacity":stroke_opacity}
    stroke_style.update(item._style)
    if item._along == "x":
      x = position
      y = series
    elif item._along == "y":
      x = series
      y = position
    series_xml = xml.SubElement(item_xml, "g", attrib={"class":"toyplot-Series"})
    if item._show_stroke:
      d = []
      for segment in segments:
        start, stop, step = segment.indices(len(not_null))
        for i in range(start, start+1):
          d.append("M %s %s" % (x[i], y[i]))
        for i in range(start+1, stop):
          d.append("L %s %s" % (x[i], y[i]))
      xml.SubElement(series_xml, "path", d=" ".join(d), style=_css_style(stroke_style))
    for dx, dy, dmarker, dsize, dfill, dopacity in zip(x[not_null], y[not_null], marker[not_null], size[not_null], fill[not_null], opacity[not_null]):
      dstyle = {"fill":toyplot.color.css.convert(dfill),"opacity":dopacity}
      dstyle.update(item._mstyle)
      _render_marker(series_xml, dx, dy, dsize, dmarker, dstyle, item._mlstyle, extra_class="toyplot-Datum")

    if title is not None:
      xml.SubElement(series_xml, "title").text = str(title)

def _render_RectMark(root, item, parent, id_cache):
  if isinstance(parent, toyplot.Axes2D):
    if item._along == "x":
      x1 = parent._project_x(item._series.T[0])
      x2 = parent._project_x(item._series.T[1])
      y1 = parent._project_y(item._series.T[2])
      y2 = parent._project_y(item._series.T[3])
    elif item._along == "y":
      x1 = parent._project_x(item._series.T[2])
      x2 = parent._project_x(item._series.T[3])
      y1 = parent._project_y(item._series.T[0])
      y2 = parent._project_y(item._series.T[1])
  item_xml = xml.SubElement(root, "g", style=_css_style(item._style), id=id_cache(item), attrib={"class":"toyplot-RectMark"})
  xml.SubElement(item_xml, "toyplot:data-table", title="Rect Data").text = json.dumps({"names":["series%s" % s for s in range(item._series.shape[1])], "data":[s.tolist() for s in item._series.T]})
  series_xml = xml.SubElement(item_xml, "g", attrib={"class":"toyplot-Series"})
  for dx1, dx2, dy1, dy2, dfill, dopacity, dtitle in zip(x1, x2, y1, y2, item._fill, item._opacity, item._title):
    dstyle = {"fill":toyplot.color.css.convert(dfill), "opacity":dopacity}
    dstyle.update(item._style)
    datum_xml = xml.SubElement(series_xml, "rect", attrib={"class":"toyplot-Datum"}, x=str(min(dx1, dx2)), y=str(min(dy1, dy2)), width=str(numpy.abs(dx1 - dx2)), height=str(numpy.abs(dy1 - dy2)), style=_css_style(dstyle))
    if dtitle is not None:
      xml.SubElement(datum_xml, "title").text = str(dtitle)

def _render_Table(root, item, parent, id_cache):
  item_xml = xml.SubElement(root, "g", id=id_cache(item), attrib={"class":"toyplot-Table"})

def _render_TextMark(root, item, parent, id_cache):
  if isinstance(parent, toyplot.Axes2D):
    if item._along == "x":
      x = parent._project_x(item._series.T[0])
      y = parent._project_y(item._series.T[1])
    elif item._along == "y":
      x = parent._project_x(item._series.T[1])
      y = parent._project_y(item._series.T[0])
  else:
    x = item._series.T[0]
    y = item._series.T[1]

  item_xml = xml.SubElement(root, "g", style=_css_style(item._style), id=id_cache(item), attrib={"class":"toyplot-TextMark"})
  xml.SubElement(item_xml, "toyplot:data-table", title="Text Data").text = json.dumps({"names":["text"] + ["series%s" % s for s in range(item._series.shape[1])], "data":[item._text.tolist()] + [s.tolist() for s in item._series.T]})
  series_xml = xml.SubElement(item_xml, "g", attrib={"class":"toyplot-Series"})
  for dx, dy, dtext, dangle, dfill, dopacity, dtitle in zip(x, y, item._text, item._angle, item._fill, item._opacity, item._title):
    dstyle = {"fill":toyplot.color.css.convert(dfill), "opacity":dopacity}
    dstyle.update(item._style)
    datum_xml = xml.SubElement(series_xml, "text", attrib={"class":"toyplot-Datum"}, x=str(dx), y=str(dy), transform="rotate(%s, %s, %s)" % (dangle, dx, dy), style=_css_style(dstyle))
    if dtext is not None:
      datum_xml.text = str(dtext)
    if dtitle is not None:
      xml.SubElement(datum_xml, "title").text = str(dtitle)

def _render_VColorBarMark(root, item, parent, id_cache):
  item._finalize_domain()

  xmin = item._xmin_range
  xmax = item._xmax_range

  ymin = item._project_y(item._vmax_computed)
  ymax = item._project_y(item._vmin_computed)
  samples = numpy.linspace(item._vmax_computed, item._vmin_computed, 256, endpoint=True)
  swatch_size = (ymax - ymin) / (len(samples) - 1)
  swatches = numpy.linspace(ymin - (swatch_size / 2), ymax + (swatch_size / 2), len(samples) + 1, endpoint=True)

  item_xml = xml.SubElement(root, "g", style=_css_style(item._style), id=id_cache(item), attrib={"class":"toyplot-VColorBarMark"})
  for sample, y1, y2 in zip(samples, swatches[:-1], swatches[1:]):
    color = item._project_color(sample)
    xml.SubElement(item_xml, "rect", x=str(xmin), y=str(y1), width=str(xmax - xmin), height=str((y2-y1) + (swatch_size / 2)), style=_css_style({"stroke":"none", "fill":toyplot.color.css.convert(color)}))

  if item.ticks._show:
    ticks_group = xml.SubElement(item_xml, "g")
    for location, tick_style in zip(item._tick_locations, item.ticks.tick.styles(item._tick_locations)):
      y = item._project_y(location)
      x1 = item._xmax_range
      x2 = item._xmax_range + item.ticks._length
      xml.SubElement(ticks_group, "line", x1=str(x1), y1=str(y), x2=str(x2), y2=str(y), style=_css_style(item.ticks._style, tick_style))

  if item.ticks.labels._show:
    ticks_group = xml.SubElement(item_xml, "g")
    for location, label, title, label_style in zip(item._tick_locations, item._tick_labels, item._tick_titles, item.ticks.labels.label.styles(item._tick_locations)):
      x = item._xmax_range + (item.ticks._length if item.ticks._show else 0)
      y = item._project_y(location)
      label_xml = xml.SubElement(ticks_group, "text", x=str(x), y=str(y), transform="rotate(-90, %s, %s)" % (x, y), style=_css_style({"text-anchor":"middle", "alignment-baseline":"middle", "baseline-shift":"-80%"}, item.ticks.labels._style, label_style))
      label_xml.text = label
      if title is not None:
        xml.SubElement(label_xml, "title").text = str(title)

  if item.label._text is not None:
    x = item._xmax_range + (item.ticks._length if item.ticks._show else 0)
    y = (item._ymin_range + item._ymax_range) * 0.5
    xml.SubElement(item_xml, "text", x=str(x), y=str(y), transform="rotate(-90, %s, %s)" % (x, y), style=_css_style(item.label._style)).text = item.label._text

def _render_item(root, item, parent, id_cache):
  item_type = type(item)
  if item_type in _render_item.methods:
    _render_item.methods[item_type](root, item, parent, id_cache)
  else:
    raise Exception("Cannot render unknown type: %s" % (item_type,)) # pragma: no cover
_render_item.methods = {
  toyplot.Axes2D : _render_Axes2D,
  toyplot.AxisLinesMark : _render_AxisLinesMark,
  toyplot.BarBoundariesMark : _render_BarBoundariesMark,
  toyplot.BarMagnitudesMark : _render_BarMagnitudesMark,
  toyplot.FillBoundariesMark : _render_FillBoundariesMark,
  toyplot.FillMagnitudesMark : _render_FillMagnitudesMark,
  toyplot.LegendMark : _render_LegendMark,
  toyplot.PlotMark : _render_PlotMark,
  toyplot.RectMark : _render_RectMark,
  toyplot.Table : _render_Table,
  toyplot.TextMark : _render_TextMark,
  toyplot.VColorBarMark : _render_VColorBarMark,
}

