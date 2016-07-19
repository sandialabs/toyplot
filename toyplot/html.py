# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division, absolute_import

from multipledispatch import dispatch
import base64
import collections
import copy
import io
import itertools
import json
import numbers
import numpy
import string
import toyplot.coordinates
import toyplot.canvas
import toyplot.color
import toyplot.compatibility
import toyplot.mark
import uuid
import xml.etree.ElementTree as xml

try:
    import HTMLParser
except: # pragma: no cover
    import html.parser as HTMLParser

class _NumpyJSONEncoder(json.JSONEncoder):

    def default(self, obj): # pragma: no cover
        if isinstance(obj, numpy.generic):
            return numpy.asscalar(obj)
        return json.JSONEncoder.default(self, obj)


class _RenderContext(object):
    def __init__(self, root):
        self._animation = collections.defaultdict(lambda: collections.defaultdict(list))
        self._coordinate_systems = set()
        self._data = list()
        self._id_cache = dict()
        self._parent = None
        self._rendered = set()
        self._root = root
        self._visible_axes = set()

    def add_coordinate_system(self, coordinate_system):
        self._coordinate_systems.add(coordinate_system)

    def add_data(self, item, content, title, filename):
        if isinstance(item, toyplot.mark.Mark) and item.annotation:
            return

        self._data.append({
            "id": self.get_id(item),
            "title": title,
            "content": content,
            "filename": filename,
            })

    def add_visible_axis(self, axis):
        self._visible_axes.add(axis)

    def already_rendered(self, renderable):
        if renderable in self._rendered:
            return True
        self._rendered.add(renderable)
        return False

    def get_id(self, obj):
        python_id = id(obj)
        if python_id not in self._id_cache:
            self._id_cache[python_id] = "t" + uuid.uuid4().hex
        return self._id_cache[python_id]

    def copy(self, parent):
        result = copy.copy(self)
        result._parent = parent
        return result

    @property
    def animation(self):
        return self._animation

    @property
    def coordinate_systems(self):
        return self._coordinate_systems

    @property
    def parent(self):
        return self._parent

    @property
    def root(self):
        return self._root

    @property
    def visible_axes(self):
        return self._visible_axes

def apply_changes(html, changes):
    for change_type, instructions in changes.items():
        if change_type == "set-mark-style":
            for mark_id, style in instructions:
                mark = html.find(".//*[@id='%s']" % mark_id)
                style = toyplot.style.combine(dict([declaration.split(
                    ":") for declaration in mark.get("style").split(";") if declaration != ""]), style)
                mark.set("style", _css_style(style))
        elif change_type == "set-datum-style":
            for mark_id, series, datum, style in instructions:
                mark_xml = html.find(".//*[@id='%s']" % mark_id)
                series_xml = mark_xml.findall(
                    "*[@class='toyplot-Series']")[series]
                datum_xml = series_xml.findall(
                    "*[@class='toyplot-Datum']")[datum]
                style = toyplot.style.combine(dict([declaration.split(
                    ":") for declaration in datum_xml.get("style").split(";") if declaration != ""]), style)
                datum_xml.set("style", _css_style(style))
        elif change_type == "set-datum-text":
            for mark_id, series, datum, text in instructions:
                mark_xml = html.find(".//*[@id='%s']" % mark_id)
                series_xml = mark_xml.findall(
                    "*[@class='toyplot-Series']")[series]
                datum_xml = series_xml.findall(
                    "*[@class='toyplot-Datum']")[datum]
                datum_xml.text = text


def render(canvas, fobj=None, animation=False):
    """Render the HTML representation of a canvas.

    Generates HTML markup with an embedded SVG representation of the canvas, plus
    JavaScript code for interactivity.  If the canvas contains animation, the
    markup will include an HTML user interface to control playback.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      The canvas to be rendered.

    fobj: file-like object or string, optional
      The file to write.  Use a string filepath to write data directly to disk.
      If `None` (the default), the HTML tree will be returned to the caller
      instead.

    animation: boolean, optional
      If `True`, return a representation of the changes to be made to the HTML
      tree for animation.

    Returns
    -------
    html: xml.etree.ElementTree.Element or `None`
      HTML representation of `canvas`, as a DOM tree, or `None` if the caller
      specifies the `fobj` parameter.

    changes: JSON-compatible data structure, or `None`
      JSON-compatible representation of the animated changes to `canvas`.

    Notes
    -----
    The output HTML is the "canonical" representation of a Toyplot canvas - the
    other toyplot backends operate by converting the output from
    toyplot.html.render() to the desired end target.

    Note that the output HTML is a fragment wrapped in a <div>, suitable for
    embedding in a larger document.  It is the caller's responsibility to
    supply the <html>, <body> etc. if the result is intended as a standalone
    HTML document.
    """
    canvas = toyplot.require.instance(canvas, toyplot.canvas.Canvas)
    canvas.autorender(False)

    # Create the top-level HTML element.
    root_xml = xml.Element(
        "div",
        align="center",
        attrib={"class": "toyplot"},
        id="t" + uuid.uuid4().hex,
        )

    # Render the canvas.
    context = _RenderContext(root=root_xml)
    _render(canvas, context.copy(parent=root_xml))

    # Return / write the results.
    if isinstance(fobj, toyplot.compatibility.string_type):
        with open(fobj, "wb") as file:
            file.write(xml.tostring(root_xml, method="html"))
    elif fobj is not None:
        fobj.write(xml.tostring(root_xml, method="html"))
    else:
        if animation:
            return root_xml, context.animation
        return root_xml


def _color_fixup(styles):
    """It turns-out that many applications and libraries (Inkscape, Adobe Illustrator, Qt)
    don't handle CSS rgba() colors correctly.  So convert them to CSS rgb colors and use
    fill-opacity / stroke-opacity instead."""

    if "fill" in styles:
        color = toyplot.color.css(styles["fill"])
        if color is not None:
            opacity = float(styles.get("fill-opacity", 1.0))
            styles["fill"] = "rgb(%.3g%%,%.3g%%,%.3g%%)" % (
                color["r"] * 100, color["g"] * 100, color["b"] * 100)
            styles["fill-opacity"] = str(color["a"] * opacity)
    if "stroke" in styles:
        color = toyplot.color.css(styles["stroke"])
        if color is not None:
            opacity = float(styles.get("stroke-opacity", 1.0))
            styles["stroke"] = "rgb(%.3g%%,%.3g%%,%.3g%%)" % (
                color["r"] * 100, color["g"] * 100, color["b"] * 100)
            styles["stroke-opacity"] = str(color["a"] * opacity)

    return styles

def _css_style(*styles):
    style = _color_fixup(toyplot.style.combine(*styles))
    return ";".join(["%s:%s" % (key, value)
                     for key, value in sorted(style.items())])


def _css_attrib(*styles):
    style = _color_fixup(toyplot.style.combine(*styles))
    attrib = {}
    if len(style):
        attrib["style"] = ";".join(
            ["%s:%s" % (key, value) for key, value in sorted(style.items())])
    return attrib


def _flat_contiguous(a):
    i = 0
    result = []
    for (k, g) in itertools.groupby(a.ravel()):
        n = len(list(g))
        if k:
            result.append(slice(i, i + n))
        i += n
    return result


class _HTMLParser(HTMLParser.HTMLParser):
    def __init__(self, element, font_size):
        HTMLParser.HTMLParser.__init__(self)
        self._element = element
        self._font_size = font_size
        self._root_node = xml.Element("root")
        self._current_node = self._root_node
        self._parent_map = {self._root_node: self._root_node}

    def push_node(self, tag, **kwargs):
        node = xml.SubElement(self._current_node, tag, **kwargs)
        self._parent_map[node] = self._current_node
        self._current_node = node

    def pop_node(self):
        while self._current_node.tag == "br":
            self._current_node = self._parent_map[self._current_node]
        while True:
            self._current_node = self._parent_map[self._current_node]
            if self._current_node.tag != "br":
                break

    def walk_tree(self, node, attributes, style, stack_state, global_state):
        if node.tag == "text":
            attributes = copy.copy(attributes)
            style = copy.copy(style)
            style["dominant-baseline"] = "inherit"
            x = global_state.pop("x", None)
            if x is not None:
                attributes["x"] = x
            new_y = global_state["line-y"] + stack_state["dy"]
            if new_y != global_state["current-y"]:
                attributes["dy"] = new_y - global_state["current-y"]
                global_state["current-y"] = new_y
            tspan = xml.SubElement(self._element, "tspan")
            for key, value in attributes.items():
                tspan.set(key, str(value))
            tspan.set("style", _css_style(style))
            tspan.text = node.text
        else:
            attributes = copy.copy(attributes)
            style = copy.copy(style)
            stack_state = copy.copy(stack_state)
            if node.tag in ["b", "strong"]:
                style["font-weight"] = "bold"
            elif node.tag == "br":
                font_size = stack_state["font-size"]
                global_state["x"] = 0
                global_state["line-y"] += font_size * 1.2
            elif node.tag == "code":
                style["font-family"] = "monospace"
            elif node.tag in ["em", "i"]:
                style["font-style"] = "italic"
            elif node.tag == "small":
                font_size = stack_state["font-size"]
                stack_state["font-size"] = font_size * 0.8
                style["font-size"] = "%spx" % (font_size * 0.8)
            elif node.tag == "sub":
                font_size = stack_state["font-size"]
                stack_state["font-size"] = font_size * 0.7
                style["font-size"] = "%spx" % (font_size * 0.7)
                stack_state["dy"] += font_size * 0.2
            elif node.tag == "sup":
                font_size = stack_state["font-size"]
                stack_state["font-size"] = font_size * 0.7
                style["font-size"] = "%spx" % (font_size * 0.7)
                stack_state["dy"] -= font_size * 0.3
            for child in node:
                self.walk_tree(child, attributes, style, stack_state, global_state)

    def handle_starttag(self, tag, attrs):
        if tag == "br":
            self.push_node("br")
        elif tag in ["b", "code", "em", "i", "small", "strong", "sub", "sup"]:
            self.push_node(tag)
        else:
            toyplot.log.warning("Ignoring unknown <%s> tag." % tag) # pragma: no cover

    def handle_endtag(self, tag):
        if tag in ["br"]:
            toyplot.log.warning("%s must not have an end tag." % tag) # pragma: no cover
        elif tag in ["b", "code", "em", "i", "small", "strong", "sub", "sup"]:
            self.pop_node()
        else:
            toyplot.log.warning("Ignoring unknown </%s> tag." % tag) # pragma: no cover

    def handle_data(self, text):
        xml.SubElement(self._current_node, "text").text = text

    def close(self):
        HTMLParser.HTMLParser.close(self)
        self.walk_tree(self._root_node, attributes={}, style={}, stack_state={"dy":0,"font-size":self._font_size}, global_state={"line-y":0, "current-y":0})


def _draw_text(
        root,
        text,
        x=0,
        y=0,
        style=None,
        angle=None,
        title=None,
        attributes={},
        ):

    if not text:
        return

    style = copy.copy(style)

    font_size = toyplot.units.convert(style["font-size"], target="px", default="px")
    style["dominant-baseline"] = style.pop("alignment-baseline", "middle")

    baseline_shift = -toyplot.units.convert(style.pop("baseline-shift", 0), target="px", default="px", reference=font_size)
    anchor_shift = toyplot.units.convert(style.pop("-toyplot-anchor-shift", 0), target="px", default="px", reference=font_size)

    transform = "translate(%r,%r)" % (x, y)
    if angle:
        transform += "rotate(%r)" % (-angle)
    if baseline_shift or anchor_shift:
        transform += "translate(%r,%r)" % (anchor_shift, baseline_shift)

    text_xml = xml.SubElement(
        root,
        "text",
        transform=transform,
        style=_css_style(style),
        attrib=attributes,
        )
    if title is not None:
        xml.SubElement(text_xml, "title").text = str(title)

    parser = _HTMLParser(text_xml, font_size)
    parser.feed(text)
    parser.close()


def _draw_marker(
        root,
        cx,
        cy,
        size,
        marker,
        marker_style=None,
        label_style=None,
        extra_class=None,
        title=None):
    if marker is None:
        return
    if isinstance(marker, toyplot.compatibility.string_type):
        marker = {"shape": marker}
    shape = marker.get("shape", None)
    shape_angle = marker.get("angle", 0)
    shape_style = marker.get("mstyle", None)
    shape_label = marker.get("label", None)
    shape_label_style = marker.get("lstyle", None)

    if shape in _draw_marker.variations:
        variation = _draw_marker.variations[shape]
        shape = variation[0]
        shape_angle += variation[1]

    attrib = _css_attrib(marker_style, shape_style)
    if extra_class is not None:
        attrib["class"] = extra_class
    marker_xml = xml.SubElement(root, "g", attrib=attrib)
    if title is not None:
        xml.SubElement(marker_xml, "title").text = str(title)
    if shape == "|":
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle,
                                                         cx,
                                                         cy),
                       x1=repr(cx),
                       x2=repr(cx),
                       y1=repr(cy - (size / 2)),
                       y2=repr(cy + (size / 2)))
    elif shape == "+":
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle,
                                                         cx,
                                                         cy),
                       x1=repr(cx),
                       x2=repr(cx),
                       y1=repr(cy - (size / 2)),
                       y2=repr(cy + (size / 2)))
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle,
                                                         cx,
                                                         cy),
                       x1=repr(cx - (size / 2)),
                       x2=repr(cx + (size / 2)),
                       y1=repr(cy),
                       y2=repr(cy))
    elif shape == "*":
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle,
                                                         cx,
                                                         cy),
                       x1=repr(cx),
                       x2=repr(cx),
                       y1=repr(cy - (size / 2)),
                       y2=repr(cy + (size / 2)))
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle + 60,
                                                         cx,
                                                         cy),
                       x1=repr(cx),
                       x2=repr(cx),
                       y1=repr(cy - (size / 2)),
                       y2=repr(cy + (size / 2)))
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle - 60,
                                                         cx,
                                                         cy),
                       x1=repr(cx),
                       x2=repr(cx),
                       y1=repr(cy - (size / 2)),
                       y2=repr(cy + (size / 2)))
    elif shape == "^":
        xml.SubElement(marker_xml,
                       "polygon",
                       transform="rotate(%r, %r, %r)" % (-shape_angle,
                                                         cx,
                                                         cy),
                       points=" ".join(["%r,%r" % (xp,
                                                   yp) for xp,
                                        yp in [(cx - (size / 2),
                                                cy + (size / 2)),
                                               (cx,
                                                cy - (size / 2)),
                                               (cx + (size / 2),
                                                cy + (size / 2))]]))
    elif shape == "s":
        xml.SubElement(marker_xml,
                       "rect",
                       transform="rotate(%r, %r, %r)" % (-shape_angle,
                                                         cx,
                                                         cy),
                       x=repr(cx - (size / 2)),
                       y=repr(cy - (size / 2)),
                       width=repr(size),
                       height=repr(size))
    elif shape == "o":
        xml.SubElement(
            marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 2))
    elif shape == "oo":
        xml.SubElement(
            marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 2))
        xml.SubElement(
            marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 4))
    elif shape == "o|":
        xml.SubElement(
            marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 2))
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle,
                                                         cx,
                                                         cy),
                       x1=repr(cx),
                       x2=repr(cx),
                       y1=repr(cy - (size / 2)),
                       y2=repr(cy + (size / 2)))
    elif shape == "o+":
        xml.SubElement(
            marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 2))
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle,
                                                         cx,
                                                         cy),
                       x1=repr(cx),
                       x2=repr(cx),
                       y1=repr(cy - (size / 2)),
                       y2=repr(cy + (size / 2)))
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle,
                                                         cx,
                                                         cy),
                       x1=repr(cx - (size / 2)),
                       x2=repr(cx + (size / 2)),
                       y1=repr(cy),
                       y2=repr(cy))
    elif shape == "o*":
        xml.SubElement(
            marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(size / 2))
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle,
                                                         cx,
                                                         cy),
                       x1=repr(cx),
                       x2=repr(cx),
                       y1=repr(cy - (size / 2)),
                       y2=repr(cy + (size / 2)))
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle + 60,
                                                         cx,
                                                         cy),
                       x1=repr(cx),
                       x2=repr(cx),
                       y1=repr(cy - (size / 2)),
                       y2=repr(cy + (size / 2)))
        xml.SubElement(marker_xml,
                       "line",
                       transform="rotate(%r, %r, %r)" % (-shape_angle - 60,
                                                         cx,
                                                         cy),
                       x1=repr(cx),
                       x2=repr(cx),
                       y1=repr(cy - (size / 2)),
                       y2=repr(cy + (size / 2)))

    if shape_label: # Not technically necessary, but we should avoid computing the style for every marker if we don't have to.
        _draw_text(
            root=marker_xml,
            text=shape_label,
            x=cx,
            y=cy,
            style = toyplot.style.combine(
                {
                    "stroke": "none",
                    "fill": toyplot.color.near_black,
                    "text-anchor": "middle",
                    "alignment-baseline": "middle",
                    "font-size": "%rpx" % (size * 0.75),
                },
                label_style,
                shape_label_style),
            )
    return marker_xml

_draw_marker.variations = {"-": ("|", 90), "/": ("|", -45), "\\": ("|", 45), "x": ("+", 45), "v": ("^", 180), "<": (
    "^", -90), ">": ("^", 90), "d": ("s", 45), "o-": ("o|", 90), "ox": ("o+", 45)}


def _axis_transform(x1, y1, x2, y2, offset, return_length=False):
    p = numpy.row_stack(((x1, y1), (x2, y2)))
    basis = p[1] - p[0]
    length = numpy.linalg.norm(basis)
    theta = numpy.rad2deg(numpy.arctan2(basis[1], basis[0]))
    transform=str()
    if p[0][0] or p[0][1]:
        transform += "translate(%s,%s)" % (p[0][0], p[0][1])
    if theta:
        transform += "rotate(%s)" % theta
    if offset:
        transform += "translate(0,%s)" % offset
    if return_length:
        return transform, length
    return transform


@dispatch(toyplot.canvas.Canvas, _RenderContext)
def _render(canvas, context):
    svg_xml = xml.SubElement(
        context.parent,
        "svg",
        xmlns="http://www.w3.org/2000/svg",
        attrib={
            "class": "toyplot-canvas-Canvas",
            "xmlns:toyplot": "http://www.sandia.gov/toyplot",
            "xmlns:xlink": "http://www.w3.org/1999/xlink",
            },
        width="%rpx" % canvas.width,
        height="%rpx" % canvas.height,
        viewBox="0 0 %r %r" % (canvas.width, canvas.height),
        preserveAspectRatio="xMidYMid meet",
        style=_css_style(canvas._style),
        id=context.get_id(canvas))

    for child in canvas._children:
        _render(canvas, child._finalize(), context.copy(parent=svg_xml))

    interactive_xml = xml.SubElement(
        context.parent,
        "div",
        attrib={"class": "toyplot-interactive"},
        )

    _render_data_table_export(context.copy(parent=interactive_xml))
    _render_data_cursors(context.copy(parent=interactive_xml))
    _render_interactive_mouse_coordinates(context.copy(parent=interactive_xml))
    _render(canvas._animation, context.copy(parent=interactive_xml))


def _render_data_table_export(context):
    if not context._data:
        return

    context.parent.append(xml.XML(
        """<ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"/>
            <li class="toyplot-mark-popup-save-csv" style="border-radius:3px;padding:5px;list-style:none;margin:0" onmouseover="this.style.color='steelblue';this.style.background='white'" onmouseout="this.style.color='white';this.style.background='steelblue'">
                Save as .csv
            </li>
        </ul>"""))

    data_tables = list()
    for data in context._data:
        content = data["content"]

        names = []
        columns = []

        if isinstance(content, toyplot.data.Table):
            for name, column in content.items():
                if "toyplot:exportable" in content.metadata(name) and content.metadata(name)["toyplot:exportable"]:
                    if column.dtype == toyplot.color.dtype:
                        raise ValueError("Color column table export isn't supported.") # pragma: no cover
                    else:
                        names.append(name)
                        columns.append(column.tolist())
        else: # Assume numpy matrix
            for column in content.T:
                names.append(column[0])
                columns.append(column[1:].tolist())

        if names and columns:
            data_tables.append({
                "id": data["id"],
                "filename": data["filename"] if data["filename"] else "toyplot",
                "title": data["title"],
                "names": names,
                "columns": columns,
                })

    xml.SubElement(context.parent, "script").text = string.Template("""
        (function()
        {
          var data_tables = $data_tables;

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#$root_id .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        """).substitute(
            root_id=context.root.get("id"),
            data_tables=json.dumps(data_tables),
            )


def _render_data_cursors(context):
    if not context.coordinate_systems:
        return

def _render_interactive_mouse_coordinates(context):
    if not context.visible_axes:
        return

    visible_axes = dict()
    for axis in context.visible_axes:
        key = context.get_id(axis)
        visible_axes[key] = list()
        for segment in axis.projection._segments:
            visible_axes[key].append(
            {
                "scale": segment.scale,
                "domain":
                {
                    "min": segment.domain.min,
                    "max": segment.domain.max,
                    "bounds":
                    {
                        "min": segment.domain.bounds.min,
                        "max": segment.domain.bounds.max,
                    },
                },
                "range":
                {
                    "min": segment.range.min,
                    "max": segment.range.max,
                    "bounds":
                    {
                        "min": segment.range.bounds.min,
                        "max": segment.range.bounds.max,
                    },
                },
            })

    xml.SubElement(context.parent, "script").text = string.Template("""
        (function()
        {
            function _sign(x)
            {
                return x < 0 ? -1 : x > 0 ? 1 : 0;
            }

            function _mix(a, b, amount)
            {
                return ((1.0 - amount) * a) + (amount * b);
            }

            function _log(x, base)
            {
                return Math.log(Math.abs(x)) / Math.log(base);
            }

            function _in_range(a, x, b)
            {
                var left = Math.min(a, b);
                var right = Math.max(a, b);
                return left <= x && x <= right;
            }

            function inside(range, projection)
            {
                for(var i = 0; i != projection.length; ++i)
                {
                    var segment = projection[i];
                    if(_in_range(segment.range.min, range, segment.range.max))
                        return true;
                }
                return false;
            }

            function to_domain(range, projection)
            {
                for(var i = 0; i != projection.length; ++i)
                {
                    var segment = projection[i];
                    if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                    {
                        if(segment.scale == "linear")
                        {
                            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                            return _mix(segment.domain.min, segment.domain.max, amount)
                        }
                        else if(segment.scale[0] == "log")
                        {
                            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                            var base = segment.scale[1];
                            return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                        }
                    }
                }
            }

            function display_coordinates(e)
            {
                var current = svg.createSVGPoint();
                current.x = e.clientX;
                current.y = e.clientY;

                for(var axis_id in axes)
                {
                    var axis = document.querySelector("#" + axis_id);
                    var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                    if(coordinates)
                    {
                        var projection = axes[axis_id];
                        var local = current.matrixTransform(axis.getScreenCTM().inverse());
                        if(inside(local.x, projection))
                        {
                            var domain = to_domain(local.x, projection);
                            coordinates.style.visibility = "visible";
                            coordinates.setAttribute("transform", "translate(" + local.x + ")");
                            var text = coordinates.querySelector("text");
                            text.textContent = domain.toFixed(2);
                        }
                        else
                        {
                            coordinates.style.visibility= "hidden";
                        }
                    }
                }
            }

            var root_id = "$root_id";
            var axes = $visible_axes;

            var svg = document.querySelector("#" + root_id + " svg");
            svg.addEventListener("click", display_coordinates);
        })();
        """).substitute(
        root_id=context.root.get("id"),
        visible_axes=json.dumps(visible_axes, cls=_NumpyJSONEncoder, sort_keys=True),
        )


@dispatch(toyplot.canvas.Canvas._AnimationFrames, _RenderContext)
def _render(frames, context):
    # Collect animation data.
    for time, time_changes in list(frames.items())[:-1]:
        # Ensure we have an entry for every time, even if there aren't any
        # changes.
        context.animation[time]
        for type, type_changes in time_changes.items():
            for change in type_changes:
                context.animation[time][type].append(
                    [context.get_id(change[0])] + list(change[1:]))

    if len(context.animation) < 2:
        return

    times = numpy.array(sorted(context.animation.keys()))
    durations = times[1:] - times[:-1]
    changes = [change for time, change in sorted(context.animation.items())]

    context.parent.append(xml.XML(
        """<div class="toyplot-vcr-controls">
            <input class="toyplot-current-frame" title="Frame" type="range" min="0" max="{frames}" step="1" value="0"/>
            <button class="toyplot-rewind" title="Rewind" style="width:40px;height:24px">
                <svg width="20" height="20">
                    <polygon points="10,5 0,10 10,15" stroke="none" fill="{near_black}"/>
                    <polygon points="20,5 10,10 20,15" stroke="none" fill="{near_black}"/>
                </svg>
            </button>
            <button class="toyplot-reverse-play" title="Reverse Play" style="width:40px;height:24px">
                <svg width="20" height="20">
                    <polygon points="15,5 5,10 15,15" stroke="none" fill="{near_black}"/>
                </svg>
            </button>
            <button class="toyplot-frame-rewind" title="Frame Rewind" style="width:40px;height:24px">
                <svg width="20" height="20">
                    <polygon points="15,5 5,10 15,15" stroke="none" fill="{near_black}"/>
                    <rect x="17" y="5" width="2" height="10" stroke="none" fill="{near_black}"/>
                </svg>
            </button>
            <button class="toyplot-stop" title="Stop" style="width:40px;height:24px">
                <svg width="20" height="20">
                    <rect x="5" y="5" width="10" height="10" stroke="none" fill="{near_black}"/>
                </svg>
            </button>
            <button class="toyplot-frame-advance" title="Frame Advance" style="width:40px;height:24px">
                <svg width="20" height="20">
                    <polygon points="5,5 15,10 5,15" stroke="none" fill="{near_black}"/>
                    <rect x="1" y="5" width="2" height="10" stroke="none" fill="{near_black}"/>
                </svg>
            </button>
            <button class="toyplot-forward-play" title="Play" style="width:40px;height:24px">
                <svg width="20" height="20">
                    <polygon points="5,5 15,10 5,15" stroke="none" fill="{near_black}"/>
                </svg>
            </button>
            <button class="toyplot-fast-forward" title="Fast Forward" style="width:40px;height:24px">
                <svg width="20" height="20">
                    <polygon points="0,5 10,10 0,15" stroke="none" fill="{near_black}"/>
                    <polygon points="10,5 20,10 10,15" stroke="none" fill="{near_black}"/>
                </svg>
            </button>
        </div>""".format(
            frames = len(times) - 2,
            near_black=toyplot.color.near_black,
            )))

    xml.SubElement(context.parent, "script").text = string.Template("""
        (function()
        {
          var root_id = "$root_id";
          var frame_durations = $frame_durations;
          var state_changes = $state_changes;

          var current_frame = null;
          var timeout = null;

          function set_timeout(value)
          {
            if(timeout !== null)
              window.clearTimeout(timeout);
            timeout = value;
          }

          function set_current_frame(frame)
          {
            current_frame = frame;
            document.querySelector("#" + root_id + " .toyplot-current-frame").value = frame;
          }

          function play_reverse()
          {
            set_current_frame((current_frame - 1 + frame_durations.length) % frame_durations.length);
            render_changes(0, current_frame+1)
            set_timeout(window.setTimeout(play_reverse, frame_durations[(current_frame - 1 + frame_durations.length) % frame_durations.length] * 1000));
          }

          function play_forward()
          {
            set_current_frame((current_frame + 1) % frame_durations.length);
            render_changes(current_frame, current_frame+1);
            set_timeout(window.setTimeout(play_forward, frame_durations[current_frame] * 1000));
          }

          var item_cache = {};
          function get_item(id)
          {
            if(!(id in item_cache))
              item_cache[id] = document.getElementById(id);
            return item_cache[id];
          }

          function render_changes(begin, end)
          {
            for(var frame = begin; frame != end; ++frame)
            {
                var changes = state_changes[frame];
                for(var type in changes)
                {
                  var type_changes = changes[type]
                  if(type == "set-mark-style")
                  {
                    for(var i = 0; i != type_changes.length; ++i)
                    {
                      var mark_style = type_changes[i];
                      var mark = get_item(mark_style[0]);
                      for(var key in mark_style[1])
                        mark.style.setProperty(key, mark_style[1][key]);
                    }
                  }
                  else if(type == "set-datum-style")
                  {
                    for(var i = 0; i != type_changes.length; ++i)
                    {
                      var datum_style = type_changes[i];
                      var datum = get_item(datum_style[0]).querySelectorAll(".toyplot-Series")[datum_style[1]].querySelectorAll(".toyplot-Datum")[datum_style[2]];
                      for(var key in datum_style[3])
                        datum.style.setProperty(key, datum_style[3][key]);
                    }
                  }
                }
            }
          }

          function on_set_frame()
          {
            set_timeout(null);
            set_current_frame(document.querySelector("#" + root_id + " .toyplot-current-frame").valueAsNumber);
            render_changes(0, current_frame+1);
          }

          function on_frame_rewind()
          {
            set_timeout(null);
            set_current_frame((current_frame - 1 + frame_durations.length) % frame_durations.length);
            render_changes(0, current_frame+1);
          }

          function on_rewind()
          {
            set_current_frame(0);
            render_changes(0, current_frame+1);
          }

          function on_play_reverse()
          {
            set_timeout(window.setTimeout(play_reverse, frame_durations[(current_frame - 1 + frame_durations.length) % frame_durations.length] * 1000));
          }

          function on_stop()
          {
            set_timeout(null);
          }

          function on_play_forward()
          {
            set_timeout(window.setTimeout(play_forward, frame_durations[current_frame] * 1000));
          }

          function on_fast_forward()
          {
            set_timeout(null);
            set_current_frame(frame_durations.length - 1);
            render_changes(0, current_frame + 1)
          }

          function on_frame_advance()
          {
            set_timeout(null);
            set_current_frame((current_frame + 1) % frame_durations.length);
            render_changes(current_frame, current_frame+1);
          }

          set_current_frame(0);
          render_changes(0, current_frame+1);

          document.querySelector("#" + root_id + " .toyplot-current-frame").oninput = on_set_frame;
          document.querySelector("#" + root_id + " .toyplot-rewind").onclick = on_rewind;
          document.querySelector("#" + root_id + " .toyplot-reverse-play").onclick = on_play_reverse;
          document.querySelector("#" + root_id + " .toyplot-frame-rewind").onclick = on_frame_rewind;
          document.querySelector("#" + root_id + " .toyplot-stop").onclick = on_stop;
          document.querySelector("#" + root_id + " .toyplot-frame-advance").onclick = on_frame_advance;
          document.querySelector("#" + root_id + " .toyplot-forward-play").onclick = on_play_forward;
          document.querySelector("#" + root_id + " .toyplot-fast-forward").onclick = on_fast_forward;
        })();
        """).substitute(
            root_id=context.root.get("id"),
            frame_durations=json.dumps(durations.tolist()),
            state_changes=json.dumps(changes, cls=_NumpyJSONEncoder),
            )


@dispatch(toyplot.canvas.Canvas, toyplot.coordinates.Axis, _RenderContext)
def _render(canvas, axis, context):
    if context.already_rendered(axis):
        return

    if axis.show:
        context.add_visible_axis(axis)

        transform, length = _axis_transform(axis._x1, axis._y1, axis._x2, axis._y2, offset=axis._offset, return_length=True)

        axis_xml = xml.SubElement(
            context.parent,
            "g",
            id=context.get_id(axis),
            transform=transform,
            attrib={"class": "toyplot-coordinates-Axis"},
            )

        if axis.spine.show:
            x1 = 0
            x2 = length
            if axis.domain.show and axis._data_min is not None and axis._data_max is not None:
                x1 = max(
                    x1, axis.projection(axis._data_min))
                x2 = min(
                    x2, axis.projection(axis._data_max))
            xml.SubElement(
                axis_xml,
                "line",
                x1=repr(x1),
                y1=repr(0),
                x2=repr(x2),
                y2=repr(0),
                style=_css_style(
                    axis.spine._style))

            if axis.ticks.show:
                y1 = axis._ticks_near if axis._tick_location == "below" else -axis._ticks_near
                y2 = -axis._ticks_far if axis._tick_location == "below" else axis._ticks_far

                ticks_group = xml.SubElement(axis_xml, "g")
                for location, tick_style in zip(
                        axis._tick_locations,
                        axis.ticks.tick.styles(axis._tick_locations),
                    ):
                    x = axis.projection(location)
                    xml.SubElement(
                        ticks_group,
                        "line",
                        x1=repr(x),
                        y1=repr(y1),
                        x2=repr(x),
                        y2=repr(y2),
                        style=_css_style(
                            axis.ticks._style,
                            tick_style))

        if axis.ticks.labels.show:
            location = axis._tick_labels_location

            if axis.ticks.labels.angle:
                alignment_baseline = "central"

                if location == "above":
                    text_anchor = "start" if axis.ticks.labels.angle > 0 else "end"
                elif location == "below":
                    text_anchor = "end" if axis.ticks.labels.angle > 0 else "start"
            else:
                alignment_baseline = "alphabetic" if location == "above" else "hanging"
                text_anchor = "middle"

            y = axis._tick_labels_offset if location == "below" else -axis._tick_labels_offset

            ticks_group = xml.SubElement(axis_xml, "g")
            for location, label, title, label_style in zip(
                    axis._tick_locations,
                    axis._tick_labels,
                    axis._tick_titles,
                    axis.ticks.labels.label.styles(axis._tick_locations),
                ):
                x = axis.projection(location)

                style=toyplot.style.combine(
                    {
                        "alignment-baseline": alignment_baseline,
                        "text-anchor": text_anchor,
                    },
                    axis.ticks.labels.style,
                    label_style,
                )

                _draw_text(
                    root=ticks_group,
                    text=label,
                    x=x,
                    y=y,
                    style=style,
                    angle=axis.ticks.labels.angle,
                    title=title,
                    )

        location = axis._label_location
        alignment_baseline = "alphabetic" if location == "above" else "hanging"
        text_anchor = "middle"
        y = axis._label_offset if location == "below" else -axis._label_offset

        _draw_text(
            root=axis_xml,
            text=axis.label.text,
            x=length * 0.5,
            y=y,
            style=toyplot.style.combine(
                {
                    "alignment-baseline": alignment_baseline,
                    "text-anchor": text_anchor,
                },
                axis.label.style,
            ),
            )

        if axis.interactive.coordinates.show:
            coordinates_xml = xml.SubElement(
                axis_xml, "g",
                attrib={"class": "toyplot-coordinates-Axis-coordinates"},
                style=_css_style({"visibility": "hidden"}),
                transform="",
                )

            if axis.interactive.coordinates.tick.show:
                y1 = axis._tick_labels_offset if axis._interactive_coordinates_location == "below" else -axis._tick_labels_offset
                y1 *= 0.5
                y2 = -axis._tick_labels_offset if axis._interactive_coordinates_location == "below" else axis._tick_labels_offset
                y2 *= 0.75
                marker_xml = xml.SubElement(
                    coordinates_xml, "line",
                    x1="0",
                    x2="0",
                    y1=repr(y1),
                    y2=repr(y2),
                    style=_css_style(axis.interactive.coordinates.tick.style),
                    )

            if axis.interactive.coordinates.label.show:
                y = axis._tick_labels_offset if axis._interactive_coordinates_location == "below" else -axis._tick_labels_offset
                alignment_baseline = "hanging" if axis._interactive_coordinates_location == "below" else "alphabetic"
                text_xml = xml.SubElement(
                    coordinates_xml, "text",
                    x="0",
                    y=repr(y),
                    style=_css_style(toyplot.style.combine(
                        {"alignment-baseline": alignment_baseline},
                        axis.interactive.coordinates.label.style,
                        )),
                    )


@dispatch(toyplot.canvas.Canvas, toyplot.coordinates.Numberline, _RenderContext)
def _render(canvas, numberline, context):
    context.add_coordinate_system(numberline)

    numberline_xml = xml.SubElement(context.parent, "g", id=context.get_id(
        numberline), attrib={"class": "toyplot-coordinates-Numberline"})

    clip_xml = xml.SubElement(
        numberline_xml,
        "clipPath",
        id="t" + uuid.uuid4().hex,
        )

    transform, length = _axis_transform(numberline._x1, numberline._y1, numberline._x2, numberline._y2, offset=0, return_length=True)

    height = numberline.axis._offset
    if numberline._child_offset:
        height += numpy.amax(list(numberline._child_offset.values()))

    xml.SubElement(
        clip_xml,
        "rect",
        x=repr(0),
        y=repr(-height),
        width=repr(length),
        height=repr(height + numberline.axis._offset),
        )

    children_xml = xml.SubElement(
        numberline_xml,
        "g",
        attrib={"clip-path": "url(#%s)" % clip_xml.get("id")},
        transform=transform,
        )

    for child in numberline._children:
        _render(numberline, child._finalize(), context.copy(parent=children_xml))

    _render(canvas, numberline.axis, context.copy(parent=numberline_xml))


@dispatch(toyplot.coordinates.Numberline, toyplot.color.CategoricalMap, _RenderContext)
def _render(numberline, colormap, context):
    offset = numberline._child_offset[colormap]
    width = numberline._child_width[colormap]
    style = numberline._child_style[colormap]

    mark_xml = xml.SubElement(
        context.parent,
        "g", id=context.get_id(colormap),
        attrib={"class": "toyplot-color-CategoricalMap"},
        )
    if offset:
        mark_xml.set("transform", "translate(0,%s)" % -offset)

    samples = numpy.linspace(colormap.domain.min, colormap.domain.max, len(colormap._palette), endpoint=True)
    projected = numberline.axis.projection(samples)
    colormap_range_min, colormap_range_max = numberline.axis.projection([colormap.domain.min, colormap.domain.max])

    for index, (x1, x2), in enumerate(zip(projected[:-1], projected[1:])):
        color = colormap._palette[index]
        xml.SubElement(
            mark_xml,
            "rect",
            x=repr(x1),
            y=repr(-width * 0.5),
            width=repr(x2 - x1),
            height=repr(width),
            style=_css_style({"stroke": "none", "fill": toyplot.color.to_css(color)}),
            )

    style = toyplot.style.combine(
        {"stroke": "none", "stroke-width":1.0, "fill": "none"},
        style,
        )

    xml.SubElement(
        mark_xml,
        "rect",
        x=repr(colormap_range_min),
        y=repr(-width * 0.5),
        width=repr(colormap_range_max - colormap_range_min),
        height=repr(width),
        style=_css_style(style),
        )

@dispatch(toyplot.coordinates.Numberline, toyplot.color.Map, _RenderContext)
def _render(numberline, colormap, context):
    offset = numberline._child_offset[colormap]
    width = numberline._child_width[colormap]
    style = numberline._child_style[colormap]

    colormap_range_min, colormap_range_max = numberline.axis.projection([colormap.domain.min, colormap.domain.max])

    mark_xml = xml.SubElement(
        context.parent,
        "g", id=context.get_id(colormap),
        attrib={"class": "toyplot-color-Map"},
        )
    if offset:
        mark_xml.set("transform", "translate(0, %s)" % -offset)

    defs_xml = xml.SubElement(
        mark_xml,
        "defs",
        )

    gradient_xml = xml.SubElement(
        defs_xml,
        "linearGradient",
        id="t" + uuid.uuid4().hex,
        x1=repr(colormap_range_min),
        x2=repr(colormap_range_max),
        y1=repr(0),
        y2=repr(0),
        gradientUnits="userSpaceOnUse",
        )

    samples = numpy.linspace(colormap.domain.min, colormap.domain.max, 64, endpoint=True)
    for sample in samples:
        color = colormap.colors(sample)
        psample = numberline.axis.projection(sample)
        offset = (psample - colormap_range_min) / (colormap_range_max - colormap_range_min)
        xml.SubElement(
            gradient_xml,
            "stop",
            offset="%s" % offset,
            attrib={
                "stop-color": "rgb(%.3g%%,%.3g%%,%.3g%%)" % (color["r"] * 100, color["g"] * 100, color["b"] * 100),
                "stop-opacity": str(color["a"]),
                },
            )

    style = toyplot.style.combine(
        {"stroke": "none", "stroke-width":1.0, "fill": "url(#%s)" % gradient_xml.get("id")},
        style,
        )

    xml.SubElement(
        mark_xml,
        "rect",
        x=repr(colormap_range_min),
        y=repr(-width * 0.5),
        width=repr(colormap_range_max - colormap_range_min),
        height=repr(width),
        style=_css_style(style),
        )


@dispatch(toyplot.coordinates.Numberline, toyplot.mark.Scatterplot, _RenderContext)
def _render(numberline, mark, context):
    offset = numberline._child_offset[mark]

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(mark._style),
        id=context.get_id(mark),
        attrib={"class": "toyplot-mark-Scatterplot"},
        )
    if offset:
        mark_xml.set("transform", "translate(0,%s)" % -offset)

    context.add_data(mark, mark._table, title="Scatterplot Data", filename=mark._filename)

    dimension1 = numpy.ma.column_stack([mark._table[key] for key in mark._coordinates])
    X = numberline.axis.projection(dimension1)
    for x, marker, msize, mfill, mstroke, mopacity, mtitle in zip(
            X.T,
            [mark._table[key] for key in mark._marker],
            [mark._table[key] for key in mark._msize],
            [mark._table[key] for key in mark._mfill],
            [mark._table[key] for key in mark._mstroke],
            [mark._table[key] for key in mark._mopacity],
            [mark._table[key] for key in mark._mtitle],
        ):
        not_null = numpy.invert(numpy.ma.getmaskarray(x))

        series_xml = xml.SubElement(
            mark_xml, "g", attrib={"class": "toyplot-Series"})
        for dx, dmarker, dsize, dfill, dstroke, dopacity, dtitle in zip(
                x[not_null],
                marker[not_null],
                msize[not_null],
                mfill[not_null],
                mstroke[not_null],
                mopacity[not_null],
                mtitle[not_null],
            ):
            dstyle = toyplot.style.combine(
                {
                    "fill": toyplot.color.to_css(dfill),
                    "stroke": toyplot.color.to_css(dstroke),
                    "opacity": dopacity,
                },
                mark._mstyle)
            datum_xml = _draw_marker(
                series_xml,
                dx,
                0,
                dsize,
                dmarker,
                dstyle,
                mark._mlstyle,
                extra_class="toyplot-Datum",
                title=dtitle,
                )


@dispatch(toyplot.canvas.Canvas, toyplot.coordinates.Cartesian, _RenderContext)
def _render(canvas, axes, context):
    context.add_coordinate_system(axes)

    cartesian_xml = xml.SubElement(context.parent, "g", id=context.get_id(
        axes), attrib={"class": "toyplot-coordinates-Cartesian"})

    clip_xml = xml.SubElement(cartesian_xml, "clipPath", id="t" + uuid.uuid4().hex)
    xml.SubElement(
        clip_xml,
        "rect",
        x=repr(axes._xmin_range - axes.padding),
        y=repr(axes._ymin_range - axes.padding),
        width=repr(axes._xmax_range - axes._xmin_range + axes.padding * 2),
        height=repr(axes._ymax_range - axes._ymin_range + axes.padding * 2),
        )

    children_xml = xml.SubElement(
        cartesian_xml,
        "g",
        attrib={"clip-path" : "url(#%s)" % clip_xml.get("id")},
        )

    for child in axes._children:
        _render(axes, child._finalize(), context.copy(parent=children_xml))

    if axes._show:
        _render(canvas, axes.x, context.copy(parent=cartesian_xml))
        _render(canvas, axes.y, context.copy(parent=cartesian_xml))
        _draw_text(
            root=cartesian_xml,
            text=axes.label._text,
            x=(axes._xmin_range + axes._xmax_range) * 0.5,
            y=axes._ymin_range,
            style=axes.label._style,
            )


@dispatch(toyplot.canvas.Canvas, toyplot.coordinates.Table, _RenderContext)
def _render(canvas, axes, context):
    axes_xml = xml.SubElement(context.parent, "g", id=context.get_id(
        axes), attrib={"class": "toyplot-coordinates-Table"})

    context.add_data(axes, axes._cell_data, title="Table Data", filename=axes._filename)

    # Render title
    _draw_text(
        root=axes_xml,
        text=axes._label._text,
        x=(axes._xmin_range + axes._xmax_range) * 0.5,
        y=axes._ymin_range,
        style=axes._label._style,
        )

    # For each unique group of cells.
    for cell_group in numpy.unique(axes._cell_group):
        cell_selection = (axes._cell_group == cell_group)

        # Skip hidden groups.
        cell_show = axes._cell_show[cell_selection][0]
        if not cell_show:
            continue

        # Identify the closed range of rows and columns that contain the cell.
        cell_rows, cell_columns = numpy.nonzero(cell_selection)
        row_min = cell_rows.min()
        row_max = cell_rows.max()
        column_min = cell_columns.min()
        column_max = cell_columns.max()

        # Render the cell background.
        cell_style = axes._cell_style[cell_selection][0]
        if cell_style is not None:
            # Compute the cell boundaries.
            cell_top = axes._cell_top[row_min]
            cell_bottom = axes._cell_bottom[row_max]
            cell_left = axes._cell_left[column_min]
            cell_right = axes._cell_right[column_max]

            cell_xml = xml.SubElement(
                axes_xml,
                "rect",
                x=repr(cell_left),
                y=repr(cell_top),
                width=repr(cell_right - cell_left),
                height=repr(cell_bottom - cell_top),
                style=_css_style({"fill":"none", "stroke":"none"}, cell_style),
                )

            cell_title = axes._cell_title[cell_selection][0]
            if cell_title is not None:
                xml.SubElement(cell_xml, "title").text = str(cell_title)

        # Render the cell data.
        cell_data = axes._cell_data[cell_selection][0]
        if cell_data is not None:
            # Compute the cell boundaries.
            padding = 5
            cell_top = axes._cell_top[row_min]
            cell_bottom = axes._cell_bottom[row_max]
            cell_left = axes._cell_left[column_min] + padding
            cell_right = axes._cell_right[column_max] - padding

            # Compute the text placement within the cell boundaries.
            cell_align = axes._cell_align[cell_selection][0]
            if cell_align is None:
                cell_align = "left"
            cell_angle = axes._cell_angle[cell_selection][0]
            y = (cell_top + cell_bottom) / 2

            # Format the cell data.
            cell_format = axes._cell_format[cell_selection][0]
            prefix, separator, suffix = cell_format.format(cell_data)

            # Get the cell style.
            cell_lstyle = axes._cell_lstyle[cell_selection][0]

            # Render the cell data.
            if cell_align == "left":
                x = cell_left
                _draw_text(
                    root=axes_xml,
                    x=x,
                    y=y,
                    style=toyplot.style.combine(cell_lstyle, {"text-anchor": "begin"}),
                    text=prefix + separator + suffix,
                    )
            elif cell_align == "center":
                x = (cell_left + cell_right) / 2
                _draw_text(
                    root=axes_xml,
                    x=x,
                    y=y,
                    angle=cell_angle,
                    style=toyplot.style.combine(cell_lstyle, {"text-anchor": "middle"}),
                    text=prefix + separator + suffix,
                    )
            elif cell_align == "right":
                x = cell_right
                _draw_text(
                    root=axes_xml,
                    x=x,
                    y=y,
                    style=toyplot.style.combine(cell_lstyle, {"text-anchor": "end"}),
                    text=prefix + separator + suffix,
                    )
            elif cell_align is "separator":
                x = (cell_left + cell_right) / 2
                _draw_text(
                    root=axes_xml,
                    x=x - 2,
                    y=y,
                    style=toyplot.style.combine(cell_lstyle, {"text-anchor": "end"}),
                    text=prefix,
                    )
                _draw_text(
                    root=axes_xml,
                    x=x,
                    y=y,
                    style=toyplot.style.combine(cell_lstyle, {"text-anchor": "middle"}),
                    text=separator,
                    )
                _draw_text(
                    root=axes_xml,
                    x=x + 2,
                    y=y,
                    style=toyplot.style.combine(cell_lstyle, {"text-anchor": "begin"}),
                    text=suffix,
                    )

    # Render children.
    for child in axes._axes:
        _render(axes._parent, child._finalize(), context.copy(parent=axes_xml))

    # Render grid lines.
    row_boundaries = axes._row_boundaries
    column_boundaries = axes._column_boundaries

    separation = axes._separation / 2

    def contiguous(a):
        i = 0
        result = []
        for (k, g) in itertools.groupby(a.ravel()):
            n = len(list(g))
            if k:
                result.append((i, i + n, k))
            i += n
        return result

    hlines = numpy.copy(axes._hlines)
    hlines[numpy.logical_not(axes._hlines_show)] = False
    for row_index, row in enumerate(hlines):
        y = row_boundaries[row_index]
        for start, end, line_type in contiguous(row):
            if line_type == "single":
                xml.SubElement(
                    axes_xml,
                    "line",
                    x1=repr(column_boundaries[start]),
                    y1=repr(y),
                    x2=repr(column_boundaries[end]),
                    y2=repr(y),
                    style=_css_style(axes._gstyle),
                    )
            elif line_type == "double":
                xml.SubElement(
                    axes_xml,
                    "line",
                    x1=repr(
                        column_boundaries[start]),
                    y1=repr(
                        y - separation),
                    x2=repr(
                        column_boundaries[end]),
                    y2=repr(
                        y - separation),
                    style=_css_style(
                        axes._gstyle))
                xml.SubElement(
                    axes_xml,
                    "line",
                    x1=repr(
                        column_boundaries[start]),
                    y1=repr(
                        y + separation),
                    x2=repr(
                        column_boundaries[end]),
                    y2=repr(
                        y + separation),
                    style=_css_style(
                        axes._gstyle))

    vlines = numpy.copy(axes._vlines)
    vlines[numpy.logical_not(axes._vlines_show)] = False
    for column_index, column in enumerate(vlines.T):
        x = column_boundaries[column_index]
        for start, end, line_type in contiguous(column):
            if line_type == "single":
                xml.SubElement(
                    axes_xml,
                    "line",
                    x1=repr(x),
                    y1=repr(row_boundaries[start]),
                    x2=repr(x),
                    y2=repr(row_boundaries[end]),
                    style=_css_style(axes._gstyle),
                    )
            elif line_type == "double":
                xml.SubElement(
                    axes_xml,
                    "line",
                    x1=repr(x - separation),
                    y1=repr(row_boundaries[start]),
                    x2=repr(x - separation),
                    y2=repr(row_boundaries[end]),
                    style=_css_style(axes._gstyle),
                    )
                xml.SubElement(
                    axes_xml,
                    "line",
                    x1=repr(x + separation),
                    y1=repr(row_boundaries[start]),
                    x2=repr(x + separation),
                    y2=repr(row_boundaries[end]),
                    style=_css_style(axes._gstyle),
                    )


@dispatch((toyplot.mark.BarBoundaries, toyplot.mark.BarMagnitudes))
def _legend_markers(mark):
    markers = []

    for fill, opacity in zip(
            [mark._table[key] for key in mark._fill],
            [mark._table[key] for key in mark._opacity],
        ):
        markers.append(
        {
            "shape": "s",
            "mstyle": toyplot.style.combine(
                {
                    "fill": toyplot.color.to_css(fill[0]),
                    "fill-opacity": opacity[0],
                },
                mark._style,
            ),
        })

    return markers


@dispatch(toyplot.coordinates.Cartesian, type(None), _RenderContext)
def _render(axes, mark, context):
    pass


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.BarBoundaries, _RenderContext)
def _render(axes, mark, context):
    left = mark._table[mark._left[0]]
    right = mark._table[mark._right[0]]
    boundaries = numpy.ma.column_stack(
        [mark._table[key] for key in mark._boundaries])

    if mark._coordinate_axes.tolist() == ["x", "y"]:
        axis1 = "x"
        axis2 = "y"
        distance1 = "width"
        distance2 = "height"
        left = axes._project_x(left)
        right = axes._project_x(right)
        boundaries = axes._project_y(boundaries)
    elif mark._coordinate_axes.tolist() == ["y", "x"]:
        axis1 = "y"
        axis2 = "x"
        distance1 = "height"
        distance2 = "width"
        left = axes._project_y(left)
        right = axes._project_y(right)
        boundaries = axes._project_x(boundaries)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-BarBoundaries"})
    context.add_data(mark, mark._table, title="Bar Data", filename=mark._filename)

    for boundary1, boundary2, fill, opacity, title in zip(
            boundaries.T[:-1],
            boundaries.T[1:],
            [mark._table[key] for key in mark._fill],
            [mark._table[key] for key in mark._opacity],
            [mark._table[key] for key in mark._title],
        ):
        not_null = numpy.invert(
            numpy.logical_or(
                numpy.ma.getmaskarray(boundary1),
                numpy.ma.getmaskarray(boundary2)))

        series_xml = xml.SubElement(
            mark_xml, "g", attrib={"class": "toyplot-Series"})
        for dleft, dright, dboundary1, dboundary2, dfill, dopacity, dtitle in zip(
                left[not_null],
                right[not_null],
                boundary1[not_null],
                boundary2[not_null],
                fill[not_null],
                opacity[not_null],
                title[not_null],
            ):
            dstyle = toyplot.style.combine({
                "fill": toyplot.color.to_css(dfill),
                "opacity": dopacity,
                }, mark._style)
            datum_xml = xml.SubElement(
                series_xml,
                "rect",
                attrib={
                    "class": "toyplot-Datum",
                    axis1: repr(min(dleft, dright)),
                    axis2: repr(min(dboundary1, dboundary2)),
                    distance1: repr(numpy.abs(dleft - dright)),
                    distance2: repr(numpy.abs(dboundary1 - dboundary2)),
                    },
                style=_css_style(dstyle),
                )
            if dtitle is not None:
                xml.SubElement(datum_xml, "title").text = str(dtitle)


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.BarMagnitudes, _RenderContext)
def _render(axes, mark, context):
    left = mark._table[mark._left[0]]
    right = mark._table[mark._right[0]]
    boundaries = numpy.ma.cumsum(numpy.ma.column_stack(
        [mark._table[mark._baseline[0]]] + [mark._table[key] for key in mark._magnitudes]), axis=1)
    not_null = numpy.invert(
        numpy.ma.any(numpy.ma.getmaskarray(boundaries), axis=1))

    if mark._coordinate_axes.tolist() == ["x", "y"]:
        axis1 = "x"
        axis2 = "y"
        distance1 = "width"
        distance2 = "height"
        left = axes._project_x(left)
        right = axes._project_x(right)
        boundaries = axes._project_y(boundaries)
    elif mark._coordinate_axes.tolist() == ["y", "x"]:
        axis1 = "y"
        axis2 = "x"
        distance1 = "height"
        distance2 = "width"
        left = axes._project_y(left)
        right = axes._project_y(right)
        boundaries = axes._project_x(boundaries)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-BarMagnitudes"})
    context.add_data(mark, mark._table, title="Bar Data", filename=mark._filename)

    for boundary1, boundary2, fill, opacity, title in zip(
            boundaries.T[:-1],
            boundaries.T[1:],
            [mark._table[key] for key in mark._fill],
            [mark._table[key] for key in mark._opacity],
            [mark._table[key] for key in mark._title],
        ):
        series_xml = xml.SubElement(
            mark_xml, "g", attrib={"class": "toyplot-Series"})
        for dleft, dright, dboundary1, dboundary2, dfill, dopacity, dtitle in zip(
                left[not_null],
                right[not_null],
                boundary1[not_null],
                boundary2[not_null],
                fill[not_null],
                opacity[not_null],
                title[not_null],
            ):
            dstyle = toyplot.style.combine(
                {"fill": toyplot.color.to_css(dfill), "opacity": dopacity}, mark._style)
            datum_xml = xml.SubElement(
                series_xml,
                "rect",
                attrib={
                    "class": "toyplot-Datum",
                    axis1: repr(min(dleft, dright)),
                    axis2: repr(min(dboundary1, dboundary2)),
                    distance1: repr(numpy.abs(dleft - dright)),
                    distance2: repr(numpy.abs(dboundary1 - dboundary2)),
                    },
                style=_css_style(dstyle),
                )
            if dtitle is not None:
                xml.SubElement(datum_xml, "title").text = str(dtitle)


@dispatch((toyplot.mark.FillBoundaries, toyplot.mark.FillMagnitudes))
def _legend_markers(mark):
    markers = []

    for fill, opacity in zip(
            mark._fill,
            mark._opacity,
        ):

        markers.append(
        {
            "shape": "s",
            "mstyle": toyplot.style.combine(
                {
                    "fill": toyplot.color.to_css(fill),
                    "fill-opacity": opacity,
                },
                mark._style,
            ),
        })

    return markers



@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.FillBoundaries, _RenderContext)
def _render(axes, mark, context):
    boundaries = numpy.ma.column_stack(
        [mark._table[key] for key in mark._boundaries])

    if mark._coordinate_axes.tolist() == ["x", "y"]:
        position = axes._project_x(mark._table[mark._position[0]])
        boundaries = axes._project_y(boundaries)
    elif mark._coordinate_axes.tolist() == ["y", "x"]:
        position = axes._project_y(mark._table[mark._position[0]])
        boundaries = axes._project_x(boundaries)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-FillBoundaries"})
    context.add_data(mark, mark._table, title="Fill Data", filename=mark._filename)

    for boundary1, boundary2, fill, opacity, title in zip(
            boundaries.T[:-1], boundaries.T[1:], mark._fill, mark._opacity, mark._title):
        not_null = numpy.invert(
            numpy.logical_or(
                numpy.ma.getmaskarray(boundary1),
                numpy.ma.getmaskarray(boundary2)))
        segments = _flat_contiguous(not_null)

        series_style = toyplot.style.combine(
            {"fill": toyplot.color.to_css(fill), "opacity": opacity}, mark._style)

        for segment in segments:
            if mark._coordinate_axes[0] == "x":
                coordinates = zip(
                    numpy.concatenate((position[segment], position[segment][::-1])),
                    numpy.concatenate((boundary1[segment], boundary2[segment][::-1])))
            elif mark._coordinate_axes[0] == "y":
                coordinates = zip(
                    numpy.concatenate((boundary1[segment], boundary2[segment][::-1])),
                    numpy.concatenate((position[segment], position[segment][::-1])))
            series_xml = xml.SubElement(mark_xml, "polygon", points=" ".join(
                ["%r,%r" % (xi, yi) for xi, yi in coordinates]), style=_css_style(series_style))
            if title is not None:
                xml.SubElement(series_xml, "title").text = str(title)


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.FillMagnitudes, _RenderContext)
def _render(axes, mark, context):
    magnitudes = numpy.ma.column_stack(
        [mark._table[mark._baseline[0]]] + [mark._table[key] for key in mark._magnitudes])
    boundaries = numpy.ma.cumsum(magnitudes, axis=1)
    not_null = numpy.invert(
        numpy.ma.any(numpy.ma.getmaskarray(boundaries), axis=1))
    segments = _flat_contiguous(not_null)

    if mark._coordinate_axes.tolist() == ["x", "y"]:
        position = axes._project_x(mark._table[mark._position[0]])
        boundaries = axes._project_y(boundaries)
    elif mark._coordinate_axes.tolist() == ["y", "x"]:
        position = axes._project_y(mark._table[mark._position[0]])
        boundaries = axes._project_x(boundaries)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-FillMagnitudes"})
    context.add_data(mark, mark._table, title="Fill Data", filename=mark._filename)

    for boundary1, boundary2, fill, opacity, title in zip(
            boundaries.T[:-1], boundaries.T[1:], mark._fill, mark._opacity, mark._title):
        series_style = toyplot.style.combine(
            {"fill": toyplot.color.to_css(fill), "opacity": opacity}, mark._style)
        for segment in segments:
            if mark._coordinate_axes[0] == "x":
                coordinates = zip(
                    numpy.concatenate((position[segment], position[segment][::-1])),
                    numpy.concatenate((boundary1[segment], boundary2[segment][::-1])))
            elif mark._coordinate_axes[0] == "y":
                coordinates = zip(
                    numpy.concatenate((boundary1[segment], boundary2[segment][::-1])),
                    numpy.concatenate((position[segment], position[segment][::-1])))
            series_xml = xml.SubElement(mark_xml, "polygon", points=" ".join(
                ["%r,%r" % (xi, yi) for xi, yi in coordinates]), style=_css_style(series_style))
            if title is not None:
                xml.SubElement(series_xml, "title").text = str(title)


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.AxisLines, _RenderContext)
def _render(axes, mark, context):
    if mark._coordinate_axes[0] == "x":
        p1 = "x1"
        p2 = "x2"
        b1 = "y1"
        b2 = "y2"
        position = axes._project_x(mark._table[mark._coordinates[0]])
        boundary1 = axes._ymin_range
        boundary2 = axes._ymax_range
    elif mark._coordinate_axes[0] == "y":
        p1 = "y1"
        p2 = "y2"
        b1 = "x1"
        b2 = "x2"
        position = axes._project_y(mark._table[mark._coordinates[0]])
        boundary1 = axes._xmin_range
        boundary2 = axes._xmax_range
    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-AxisLines"})
    series_xml = xml.SubElement(
        mark_xml, "g", attrib={"class": "toyplot-Series"})
    for dposition, dstroke, dopacity, dtitle in zip(
            position,
            mark._table[mark._stroke[0]],
            mark._table[mark._opacity[0]],
            mark._table[mark._title[0]],
        ):
        dstyle = toyplot.style.combine(
            {"stroke": toyplot.color.to_css(dstroke), "opacity": dopacity}, mark._style)
        datum_xml = xml.SubElement(
            series_xml,
            "line",
            attrib={
                "class": "toyplot-Datum",
                p1: repr(dposition),
                p2: repr(dposition),
                b1: repr(boundary1),
                b2: repr(boundary2),
            },
            style=_css_style(dstyle),
        )
        if dtitle is not None:
            xml.SubElement(datum_xml, "title").text = str(dtitle)


@dispatch(toyplot.mark.Mark)
def _legend_markers(mark):
    return []


@dispatch((toyplot.canvas.Canvas, toyplot.coordinates.Cartesian), toyplot.mark.Legend, _RenderContext)
def _render(canvas, legend, context):
    if not legend._entries:
        return

    entries = []

    for entry in legend._entries:
        label, spec = entry

        if isinstance(spec, toyplot.mark.Mark):
            markers = _legend_markers(spec)
        elif isinstance(spec, list):
            markers = spec
        else:
            markers = [spec]

        entries.append((label, markers))

    x = legend._xmin
    y = legend._ymin
    width = legend._xmax - legend._xmin
    height = legend._ymax - legend._ymin
    marker_height = (height - (legend._gutter * (len(entries) + 1))) / len(entries)
    marker_width = marker_height

    label_offset = (numpy.amax([len(markers) for label, markers in entries]) * (legend._gutter + marker_width)) + legend._gutter

    xml.SubElement(
        context.parent,
        "rect",
        x=repr(x),
        y=repr(y),
        width=repr(width),
        height=repr(height),
        style=_css_style(legend._style),
        id=context.get_id(legend),
        attrib={"class": "toyplot-mark-Legend"},
        )

    for i, (label, markers) in enumerate(entries):
        marker_y = y + ((i + 1) * legend._gutter) + (i * marker_height)

        for j, marker in enumerate(markers):
            marker_x = x + label_offset - (len(markers) * (marker_width + legend._gutter)) + (j * (marker_width + legend._gutter))

            _draw_marker(
                context.parent,
                marker_x + (marker_width / 2),
                marker_y + (marker_height / 2),
                min(marker_width, marker_height),
                marker,
                {},#computed_style,
                {},
                )

        _draw_text(
            root=context.parent,
            text=label,
            x=x + label_offset,
            y=y + ((i + 1) * legend._gutter) +  (i * marker_height) + (marker_height / 2),
            style=legend._lstyle,
            )


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.Graph, _RenderContext)
def _render(axes, mark, context): # pragma: no cover
    # Project edge coordinates
    for i in range(2):
        if mark._coordinate_axes[i] == "x":
            x = axes._project_x(mark._ecoordinates.T[i])
        elif mark._coordinate_axes[i] == "y":
            y = axes._project_y(mark._ecoordinates.T[i])

    mark_xml = xml.SubElement(context.parent, "g", id=context.get_id(mark), attrib={"class": "toyplot-mark-Graph"})
    #context.add_data(mark, mark._vtable, title="Graph Vertex Data", filename=mark._vertex_filename)
    #context.add_data(mark, mark._etable, title="Graph Edge Data", filename=mark._edge_filename)

    coordinate_index = 0
    edge_xml = xml.SubElement(mark_xml, "g", attrib={"class": "toyplot-Edges"})
    for esource, etarget, eshape, ecolor, ewidth, eopacity in zip(
            mark._etable[mark._esource[0]],
            mark._etable[mark._etarget[0]],
            mark._etable[mark._eshape[0]],
            mark._etable[mark._ecolor[0]],
            mark._etable[mark._ewidth[0]],
            mark._etable[mark._eopacity[0]],
        ):
        estyle = toyplot.style.combine(
            {
                "fill": "none",
                "stroke": toyplot.color.to_css(ecolor),
                "stroke-width": ewidth,
                "stroke-opacity": eopacity,
            },
            mark._estyle)

        path = []
        for segment in eshape:
            if segment == "M":
                count = 1
            elif segment == "L":
                count = 1
            elif segment == "Q":
                count = 2
            elif segment == "C":
                count = 3
            path.append(segment)
            for i in range(count):
                path.append(str(x[coordinate_index]))
                path.append(str(y[coordinate_index]))
                coordinate_index += 1

        xml.SubElement(
            edge_xml,
            "path",
            d=" ".join(path),
            style=_css_style(estyle),
            )

    # Project vertex coordinates
    for i in range(2):
        if mark._coordinate_axes[i] == "x":
            x = axes._project_x(mark._vtable[mark._vcoordinates[i]])
        elif mark._coordinate_axes[i] == "y":
            y = axes._project_y(mark._vtable[mark._vcoordinates[i]])

    vertex_xml = xml.SubElement(mark_xml, "g", attrib={"class": "toyplot-Vertices"})
    for vx, vy, vmarker, vsize, vcolor, vopacity, vtitle in zip(
            x,
            y,
            mark._vtable[mark._vmarker[0]],
            mark._vtable[mark._vsize[0]],
            mark._vtable[mark._vcolor[0]],
            mark._vtable[mark._vopacity[0]],
            mark._vtable[mark._vtitle[0]],
        ):
        vstyle = toyplot.style.combine(
            {
                "fill": toyplot.color.to_css(vcolor),
                "stroke": toyplot.color.to_css(vcolor),
                "opacity": vopacity,
            },
            mark._vstyle)
        _draw_marker(
            vertex_xml,
            vx,
            vy,
            vsize,
            vmarker,
            vstyle,
            mark._vlstyle,
            extra_class="toyplot-Datum",
            title=vtitle,
            )

    # Render vertex labels
    if mark._vlshow:
        vlabel_xml = xml.SubElement(mark_xml, "g", attrib={"class": "toyplot-Labels"})
        for dx, dy, dtext in zip(x, y, mark._vtable[mark._vlabel[0]]):
            _draw_text(
                root=vlabel_xml,
                text=toyplot.compatibility.unicode_type(dtext),
                x=dx,
                y=dy,
                style=mark._vlstyle,
                attributes={"class": "toyplot-Datum"},
                )


@dispatch(toyplot.mark.Plot)
def _legend_markers(mark):
    markers = []

    for stroke, stroke_width, stroke_opacity in zip(mark._stroke.T, mark._stroke_width.T, mark._stroke_opacity.T):
        markers.append(
        {
            "shape": "/",
            "mstyle": toyplot.style.combine(
                {
                    "stroke": toyplot.color.to_css(stroke),
                    "stroke-width": stroke_width,
                    "stroke-opacity": stroke_opacity,
                },
                mark._style,
            ),
        })

    return markers


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.Plot, _RenderContext)
def _render(axes, mark, context):
    position = mark._table[mark._coordinates[0]]
    series = numpy.ma.column_stack([mark._table[key] for key in mark._series])

    if mark._coordinate_axes[0] == "x":
        position = axes._project_x(position)
        series = axes._project_y(series)
    elif mark._coordinate_axes[0] == "y":
        position = axes._project_y(position)
        series = axes._project_x(series)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(toyplot.style.combine({"fill":"none"}, mark._style)),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-Plot"})
    context.add_data(mark, mark._table, title="Plot Data", filename=mark._filename)

    for series, stroke, stroke_width, stroke_opacity, stroke_title, marker, msize, mfill, mstroke, mopacity, mtitle in zip(
            series.T,
            mark._stroke.T,
            mark._stroke_width.T,
            mark._stroke_opacity.T,
            mark._stroke_title.T,
            [mark._table[key] for key in mark._marker],
            [mark._table[key] for key in mark._msize],
            [mark._table[key] for key in mark._mfill],
            [mark._table[key] for key in mark._mstroke],
            [mark._table[key] for key in mark._mopacity],
            [mark._table[key] for key in mark._mtitle],
        ):
        not_null = numpy.invert(numpy.logical_or(
            numpy.ma.getmaskarray(position), numpy.ma.getmaskarray(series)))
        segments = _flat_contiguous(not_null)

        stroke_style = toyplot.style.combine(
            {
                "stroke": toyplot.color.to_css(stroke),
                "stroke-width": stroke_width,
                "stroke-opacity": stroke_opacity},
            mark._style)
        if mark._coordinate_axes[0] == "x":
            x = position
            y = series
        elif mark._coordinate_axes[0] == "y":
            x = series
            y = position
        series_xml = xml.SubElement(
            mark_xml, "g", attrib={"class": "toyplot-Series"})
        if stroke_title is not None:
            xml.SubElement(series_xml, "title").text = str(stroke_title)

        d = []
        for segment in segments:
            start, stop, step = segment.indices(len(not_null))
            for i in range(start, start + 1):
                d.append("M %r %r" % (x[i], y[i]))
            for i in range(start + 1, stop):
                d.append("L %r %r" % (x[i], y[i]))
        xml.SubElement(
            series_xml,
            "path",
            d=" ".join(d),
            style=_css_style(stroke_style))
        for dx, dy, dmarker, dsize, dfill, dstroke, dopacity, dtitle in zip(
                x[not_null],
                y[not_null],
                marker[not_null],
                msize[not_null],
                mfill[not_null],
                mstroke[not_null],
                mopacity[not_null],
                mtitle[not_null],
            ):
            dstyle = toyplot.style.combine(
                {
                    "fill": toyplot.color.to_css(dfill),
                    "stroke": toyplot.color.to_css(dstroke),
                    "opacity": dopacity},
                mark._mstyle)
            datum_xml = _draw_marker(
                series_xml,
                dx,
                dy,
                dsize,
                dmarker,
                dstyle,
                mark._mlstyle,
                extra_class="toyplot-Datum",
                title=dtitle,
                )


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.Rect, _RenderContext)
def _render(axes, mark, context):
    if mark._coordinate_axes.tolist() == ["x", "y"]:
        x1 = axes._project_x(mark._table[mark._left[0]])
        x2 = axes._project_x(mark._table[mark._right[0]])
        y1 = axes._project_y(mark._table[mark._top[0]])
        y2 = axes._project_y(mark._table[mark._bottom[0]])
    elif mark._coordinate_axes.tolist() == ["y", "x"]:
        x1 = axes._project_x(mark._table[mark._top[0]])
        x2 = axes._project_x(mark._table[mark._bottom[0]])
        y1 = axes._project_y(mark._table[mark._left[0]])
        y2 = axes._project_y(mark._table[mark._right[0]])
    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-Rect"})
    context.add_data(mark, mark._table, title="Rect Data", filename=mark._filename)

    series_xml = xml.SubElement(
        mark_xml, "g", attrib={"class": "toyplot-Series"})
    for dx1, dx2, dy1, dy2, dfill, dopacity, dtitle in zip(
            x1,
            x2,
            y1,
            y2,
            mark._table[mark._fill[0]],
            mark._table[mark._opacity[0]],
            mark._table[mark._title[0]],
        ):
        dstyle = toyplot.style.combine(
            {"fill": toyplot.color.to_css(dfill), "opacity": dopacity}, mark._style)
        datum_xml = xml.SubElement(
            series_xml,
            "rect",
            attrib={"class": "toyplot-Datum"},
            x=repr(min(dx1, dx2)),
            y=repr(min(dy1, dy2)),
            width=repr(numpy.abs(dx1 - dx2)),
            height=repr(numpy.abs(dy1 - dy2)),
            style=_css_style(dstyle),
            )
        if dtitle is not None:
            xml.SubElement(datum_xml, "title").text = str(dtitle)


@dispatch(toyplot.mark.Scatterplot)
def _legend_markers(mark):
    markers = []

    for marker, mfill, mstroke, mopacity in zip(
            [mark._table[key] for key in mark._marker],
            [mark._table[key] for key in mark._mfill],
            [mark._table[key] for key in mark._mstroke],
            [mark._table[key] for key in mark._mopacity],
        ):

        for dmarker, dfill, dstroke, dopacity in zip(
                marker,
                mfill,
                mstroke,
                mopacity,
            ):
            if isinstance(dmarker, toyplot.compatibility.string_type):
                dmarker = {"shape": dmarker}
            dmarker["mstyle"] = toyplot.style.combine(
                dmarker.get("mstyle", None),
                {
                    "fill": toyplot.color.to_css(dfill),
                    "stroke": toyplot.color.to_css(dstroke),
                    "opacity": dopacity,
                },
                mark._mstyle,
                )
            dmarker["lstyle"] = toyplot.style.combine(
                dmarker.get("lstyle", None),
                mark._mlstyle,
                )
            markers.append(dmarker)
            break

    return markers


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.Scatterplot, _RenderContext)
def _render(axes, mark, context):
    dimension1 = numpy.ma.column_stack([mark._table[key] for key in mark._coordinates[0::2]])
    dimension2 = numpy.ma.column_stack([mark._table[key] for key in mark._coordinates[1::2]])

    if mark._coordinate_axes[0] == "x":
        X = axes._project_x(dimension1)
        Y = axes._project_y(dimension2)
    elif mark._coordinate_axes[0] == "y":
        X = axes._project_x(dimension2)
        Y = axes._project_y(dimension1)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(mark._style),
        id=context.get_id(mark),
        attrib={"class": "toyplot-mark-Scatterplot"},
        )
    context.add_data(mark, mark._table, title="Scatterplot Data", filename=mark._filename)

    for x, y, marker, msize, mfill, mstroke, mopacity, mtitle in zip(
            X.T,
            Y.T,
            [mark._table[key] for key in mark._marker],
            [mark._table[key] for key in mark._msize],
            [mark._table[key] for key in mark._mfill],
            [mark._table[key] for key in mark._mstroke],
            [mark._table[key] for key in mark._mopacity],
            [mark._table[key] for key in mark._mtitle],
        ):
        not_null = numpy.invert(numpy.logical_or(
            numpy.ma.getmaskarray(x), numpy.ma.getmaskarray(y)))

        series_xml = xml.SubElement(
            mark_xml, "g", attrib={"class": "toyplot-Series"})
        for dx, dy, dmarker, dsize, dfill, dstroke, dopacity, dtitle in zip(
                x[not_null],
                y[not_null],
                marker[not_null],
                msize[not_null],
                mfill[not_null],
                mstroke[not_null],
                mopacity[not_null],
                mtitle[not_null],
            ):
            dstyle = toyplot.style.combine(
                {
                    "fill": toyplot.color.to_css(dfill),
                    "stroke": toyplot.color.to_css(dstroke),
                    "opacity": dopacity,
                },
                mark._mstyle)
            datum_xml = _draw_marker(
                series_xml,
                dx,
                dy,
                dsize,
                dmarker,
                dstyle,
                mark._mlstyle,
                extra_class="toyplot-Datum",
                title=dtitle,
                )


@dispatch((toyplot.canvas.Canvas, toyplot.coordinates.Cartesian), toyplot.mark.Text, _RenderContext)
def _render(parent, mark, context):
    x = mark._table[mark._coordinates[numpy.where(mark._coordinate_axes == "x")[0][0]]]
    y = mark._table[mark._coordinates[numpy.where(mark._coordinate_axes == "y")[0][0]]]

    if isinstance(parent, toyplot.coordinates.Cartesian):
        x = parent._project_x(x)
        y = parent._project_y(y)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-Text"})
    context.add_data(mark, mark._table, title="Text Data", filename=mark._filename)
    series_xml = xml.SubElement(
        mark_xml, "g", attrib={"class": "toyplot-Series"})
    for dx, dy, dtext, dangle, dfill, dopacity, dtitle in zip(
            x,
            y,
            mark._table[mark._text[0]],
            mark._table[mark._angle[0]],
            mark._table[mark._fill[0]],
            mark._table[mark._opacity[0]],
            mark._table[mark._title[0]],
        ):

        _draw_text(
            root=series_xml,
            text=toyplot.compatibility.unicode_type(dtext),
            x=dx,
            y=dy,
            angle=dangle,
            attributes={"class": "toyplot-Datum"},
            style=toyplot.style.combine({"fill": toyplot.color.to_css(dfill), "opacity": dopacity}, mark._style),
            title=dtitle,
            )


@dispatch((toyplot.canvas.Canvas), toyplot.mark.Image, _RenderContext)
def _render(parent, mark, context):
    import png
    buffer = io.BytesIO()

    data = mark._data

    toyplot.log.debug("Image data: %s %s", data.shape, data.dtype)

    if data.dtype == toyplot.color.dtype:
        data = numpy.dstack((data["r"], data["g"], data["b"], data["a"]))
    if issubclass(data.dtype.type, numpy.bool_):
        bitdepth=1
    elif issubclass(data.dtype.type, numpy.floating):
        data = (data * 255.0).astype("uint8")
        bitdepth=8
    else:
        bitdepth=8

    width = data.shape[1]
    height = data.shape[0]
    greyscale = data.shape[2] < 3
    alpha = data.shape[2] == 2 or data.shape[2] == 4

    writer = png.Writer(width=width, height=height, greyscale=greyscale, alpha=alpha, bitdepth=bitdepth)
    writer.write(buffer, numpy.reshape(data, (-1, data.shape[1] * data.shape[2])))
    encoded = base64.standard_b64encode(buffer.getvalue()).decode("ascii")

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        id=context.get_id(mark),
        attrib={"class": "toyplot-mark-Image"},
        )

    xml.SubElement(
        mark_xml,
        "image",
        x=repr(mark._xmin_range),
        y=repr(mark._ymin_range),
        width=repr(mark._xmax_range - mark._xmin_range),
        height=repr(mark._ymax_range - mark._ymin_range),
        attrib={"xlink:href": "data:image/png;base64," + encoded},
        )

