# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

# pylint: disable=function-redefined

from __future__ import division, absolute_import

import base64
import collections
import copy
import functools
import io
import itertools
import json
import string
import uuid
import xml.etree.ElementTree as xml

from multipledispatch import dispatch
import numpy

import toyplot.coordinates
import toyplot.canvas
import toyplot.color
import toyplot.compatibility
import toyplot.mark
import toyplot.marker


_namespace = dict()

#: Decorator for registering custom rendering code.
#:
#: This is only of use when creating your own custom Toyplot marks.  It is
#: not intended for end-users.
#:
#: Example
#: -------
#: To register your own rendering function::
#:
#:     @toyplot.html.dispatch(toyplot.coordinates.Cartesian, MyCustomMark, toyplot.html.RenderContext)
#:     def _render(axes, mark, context):
#:         # Rendering implementation here
dispatch = functools.partial(dispatch, namespace=_namespace)


class _NumpyJSONEncoder(json.JSONEncoder):
    # pylint: disable=method-hidden
    def default(self, obj): # pragma: no cover
        if isinstance(obj, numpy.generic):
            return numpy.asscalar(obj)
        return json.JSONEncoder.default(self, obj)


class RenderContext(object):
    """Stores context data during rendering.

    This is only of use when creating custom Toyplot marks.  It is not intended
    for end-users.
    """
    def __init__(self, root):
        self._animation = collections.defaultdict(lambda: collections.defaultdict(list))
        self._id_cache = dict()
        self._parent = None
        self._rendered = set()
        self._root = root
        self._javascript_modules = dict()
        self._javascript_calls = list()


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

    def define(self, name, dependencies=None, factory=None, value=None):
        """Define a Javascript module that can be embedded in the output markup.

        The module will only be embedded in the output if it is listed as a
        dependency of another module, or code specified using :meth:`require`.

        You must specify either `factory` or `value`.

        Parameters
        ----------
        name: string, required
            Module name.  Any string is valid, but alphanumerics separated with
            slashes are recommended. Multiple calls to `define` with the same
            name argument will be silently ignored.
        dependencies: sequence of strings, required
            Names of modules that are dependencies by this module (if any).
        factory: string, optional
            Javascript factory for this module, which must be a function that
            takes the modules listed in `dependencies`, in-order, as arguments,
            and returns the initialized module.
        value: Python object, optional
            Arbitrary value for this module, which must be a JSON-convertible
            value (string, number, boolean, None, list, or dict).
        """
        if name in self._javascript_modules:
            return

        if dependencies is None:
            dependencies = []

        if factory is None and value is None:
            raise ValueError("You must specify either factory or value.")
        if factory is not None and value is not None:
            raise ValueError("You must specify either factory or value.")
        if value is not None and dependencies:
            raise ValueError("Dependencies can only be specified when defining a factory, not a value.")

        self._javascript_modules[name] = (dependencies, factory, value)

    def require(self, dependencies=None, arguments=None, code=None):
        """Embed Javascript code and its dependencies into the output markup.

        The given code will be unconditionally embedded in the output markup,
        along with any modules listed as dependencies (plus their dependencies,
        and-so-on).

        Parameters
        ----------
        dependencies: sequence of strings, optional
            Names of modules that are required by this code.
        arguments: sequence of Python objects, optional
            Additional arguments to be passed to the Javascript code.
            Arguments must be compatible with :func:`json.dumps`.
        code: string, required
            Javascript function to be embedded, which must accept the modules
            listed in `requirements` in-order, followed by the values listed in
            `arguments` in-order, as arguments.
        """
        if dependencies is None:
            dependencies = []
        if arguments is None:
            arguments = []
        if code is None:
            raise ValueError("You must specify a Javascript function using the code argument.")
        self._javascript_calls.append((dependencies, arguments, code))

    @property
    def animation(self):
        return self._animation

    @property
    def parent(self):
        """Current DOM node.  Typical rendering code will append HTML content to this node."""
        return self._parent

    @property
    def root(self):
        """Top-level DOM node."""
        return self._root


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


def render(canvas, fobj=None, animation=False, style=None):
    """Convert a canvas to its HTML DOM representation.

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

    style: dict, optional
      Dictionary of CSS styles that will be applied to the top-level output <div>.

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
        attrib={"class": "toyplot"},
        id="t" + uuid.uuid4().hex,
        )
    if style is not None:
        root_xml.set("style", toyplot.style.to_css(style))

    # Setup a render context
    context = RenderContext(root=root_xml)

    # Register a Javascript module to keep track of the root id
    context.define("toyplot/root/id", value=root_xml.get("id"))
    # Register a Javascript module to keep track of the root
    context.define("toyplot/root", ["toyplot/root/id"], factory="""function(root_id)
    {
        return document.querySelector("#" + root_id);
    }""")

    # Render the canvas.
    _render(canvas, context.copy(parent=root_xml)) # pylint: disable=no-value-for-parameter

    # Return / write the results.
    if isinstance(fobj, toyplot.compatibility.string_type):
        with open(fobj, "wb") as stream:
            stream.write(xml.tostring(root_xml, method="html"))
    elif fobj is not None:
        fobj.write(xml.tostring(root_xml, method="html"))
    else:
        if animation:
            return root_xml, context.animation
        return root_xml


def tostring(canvas, style=None):
    """Convert a canvas to its HTML string representation.

    Generates HTML markup with an embedded SVG representation of the canvas, plus
    JavaScript code for interactivity.  If the canvas contains animation, the
    markup will include an HTML user interface to control playback.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      The canvas to be rendered.

    style: dict, optional
      Dictionary of CSS styles that will be applied to the top-level output <div>.

    Returns
    -------
    html: string
      HTML representation of `canvas` as a string.

    Notes
    -----
    The output HTML is a fragment wrapped in a <div>, suitable for embedding in
    a larger document.  It is the caller's responsibility to supply the <html>,
    <body> etc. if the result is intended as a standalone HTML document.
    """
    return toyplot.compatibility.unicode_type(xml.tostring(render(canvas=canvas, style=style), encoding="utf-8", method="html"), encoding="utf-8")


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


def _walk_tree(node):
    yield ("start", node.tag, node.attrib)
    if node.text:
        yield ("text", node.text)
    for child in node:
        for item in _walk_tree(child):
            yield item
    yield ("end", node.tag)
    if node.tail:
        yield ("text", node.tail)

def _draw_text(
        root,
        text,
        x=0,
        y=0,
        style=None,
        angle=None,
        title=None,
        attributes=None,
    ):

    if not text:
        return

    style = toyplot.style.combine({"font-family": "helvetica"}, style)

    if attributes is None:
        attributes = {}

    fonts = toyplot.font.ReportlabLibrary()
    layout = text if isinstance(text, toyplot.text.Layout) else toyplot.text.layout(text, style, fonts)

    transform = "translate(%r,%r)" % (x, y)
    if angle:
        transform += "rotate(%r)" % (-angle)

    group = xml.SubElement(
        root,
        "g",
        transform=transform,
        attrib=attributes,
        )

    if title is not None:
        xml.SubElement(group, "title").text = str(title)

    if layout.style.get("-toyplot-text-layout-visibility", None) == "visible":
        xml.SubElement(
            group,
            "rect",
            x=str(layout.left),
            y=str(layout.top),
            width=str(layout.width),
            height=str(layout.height),
            stroke="red",
            fill="none",
            opacity="0.5",
            )
        xml.SubElement(
            group,
            "circle",
            x="0",
            y="0",
            r="3",
            stroke="none",
            fill="red",
            opacity="0.5",
            )

    hyperlink = []
    for line in layout.children:
        if line.style.get("-toyplot-text-layout-line-visibility", None) == "visible":
            xml.SubElement(
                group,
                "rect",
                x=str(line.left),
                y=str(line.top),
                width=str(line.width),
                height=str(line.height),
                stroke="green",
                fill="none",
                opacity="0.5",
                )
            xml.SubElement(
                group,
                "line",
                x1=str(line.left),
                y1=str(line.baseline),
                x2=str(line.right),
                y2=str(line.baseline),
                stroke="green",
                fill="none",
                opacity="0.5",
                )
        for box in line.children:
            if isinstance(box, toyplot.text.TextBox):
                xml.SubElement(
                    group,
                    "text",
                    x=str(box.left),
                    y=str(box.baseline),
                    style=toyplot.style.to_css(box.style),
                    ).text = box.text
                if box.style.get("-toyplot-text-layout-box-visibility", None) == "visible":
                    xml.SubElement(
                        group,
                        "rect",
                        x=str(box.left),
                        y=str(box.top),
                        width=str(box.width),
                        height=str(box.height),
                        stroke="blue",
                        fill="none",
                        opacity="0.5",
                        )
                    xml.SubElement(
                        group,
                        "line",
                        x1=str(box.left),
                        y1=str(box.baseline),
                        x2=str(box.right),
                        y2=str(box.baseline),
                        stroke="blue",
                        fill="none",
                        opacity="0.5",
                        )

            elif isinstance(box, toyplot.text.MarkerBox):
                _draw_marker(
                    group,
                    cx=(box.left + box.right) * 0.5,
                    cy=(box.top + box.bottom) * 0.5,
                    default=toyplot.marker.create(size=box.height),
                    marker=box.marker,
                    )
                if box.style.get("-toyplot-text-layout-box-visibility", None) == "visible":
                    xml.SubElement(
                        group,
                        "rect",
                        x=str(box.left),
                        y=str(box.top),
                        width=str(box.width),
                        height=str(box.height),
                        stroke="blue",
                        fill="none",
                        opacity="0.5",
                        )
                    xml.SubElement(
                        group,
                        "line",
                        x1=str(box.left),
                        y1=str(box.baseline),
                        x2=str(box.right),
                        y2=str(box.baseline),
                        stroke="blue",
                        fill="none",
                        opacity="0.5",
                        )

            elif isinstance(box, toyplot.text.PushHyperlink):
                hyperlink.append(group)
                group = xml.SubElement(group, "a")
                group.set("xlink:href", box.href)
            elif isinstance(box, toyplot.text.PopHyperlink):
                group = hyperlink.pop()


def _draw_marker(
        root,
        cx,
        cy,
        default,
        marker,
        extra_class=None,
        title=None,
        ):

    if not marker:
        return

    marker = default + toyplot.marker.convert(marker)

    if marker.shape in _draw_marker.variations:
        variation = _draw_marker.variations[marker.shape]
        marker = marker + toyplot.marker.create(shape=variation[0], angle=marker.angle + variation[1])

    attrib = _css_attrib(marker.mstyle)
    if extra_class is not None:
        attrib["class"] = extra_class
    marker_xml = xml.SubElement(root, "g", attrib=attrib)
    if title is not None:
        xml.SubElement(marker_xml, "title").text = str(title)
    if marker.shape == "|":
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle, cx, cy),
            x1=repr(cx),
            x2=repr(cx),
            y1=repr(cy - (marker.size / 2)),
            y2=repr(cy + (marker.size / 2)))
    elif marker.shape == "+":
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle, cx, cy),
            x1=repr(cx),
            x2=repr(cx),
            y1=repr(cy - (marker.size / 2)),
            y2=repr(cy + (marker.size / 2)))
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle, cx, cy),
            x1=repr(cx - (marker.size / 2)),
            x2=repr(cx + (marker.size / 2)),
            y1=repr(cy),
            y2=repr(cy))
    elif marker.shape == "*":
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle, cx, cy),
            x1=repr(cx),
            x2=repr(cx),
            y1=repr(cy - (marker.size / 2)),
            y2=repr(cy + (marker.size / 2)))
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle + 60, cx, cy),
            x1=repr(cx),
            x2=repr(cx),
            y1=repr(cy - (marker.size / 2)),
            y2=repr(cy + (marker.size / 2)))
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle - 60, cx, cy),
            x1=repr(cx),
            x2=repr(cx),
            y1=repr(cy - (marker.size / 2)),
            y2=repr(cy + (marker.size / 2)))
    elif marker.shape == "^":
        xml.SubElement(marker_xml,
            "polygon",
            transform="rotate(%r, %r, %r)" % (-marker.angle, cx, cy),
            points=" ".join(["%r,%r" % (xp, yp) for xp, yp in [
               (cx - (marker.size / 2), cy + (marker.size / 2)),
               (cx, cy - (marker.size / 2)),
               (cx + (marker.size / 2), cy + (marker.size / 2)),
   ]]))
    elif marker.shape == "s":
        xml.SubElement(
            marker_xml,
            "rect",
            transform="rotate(%r, %r, %r)" % (-marker.angle, cx, cy),
            x=repr(cx - (marker.size / 2)),
            y=repr(cy - (marker.size / 2)),
            width=repr(marker.size),
            height=repr(marker.size))
    elif marker.shape == "o":
        xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(marker.size / 2))
    elif marker.shape == "oo":
        xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(marker.size / 2))
        xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(marker.size / 4))
    elif marker.shape == "o|":
        xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(marker.size / 2))
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle, cx, cy),
            x1=repr(cx),
            x2=repr(cx),
            y1=repr(cy - (marker.size / 2)),
            y2=repr(cy + (marker.size / 2)))
    elif marker.shape == "o+":
        xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(marker.size / 2))
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle, cx, cy),
            x1=repr(cx),
            x2=repr(cx),
            y1=repr(cy - (marker.size / 2)),
            y2=repr(cy + (marker.size / 2)))
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle,
            cx,
            cy),
            x1=repr(cx - (marker.size / 2)),
            x2=repr(cx + (marker.size / 2)),
            y1=repr(cy),
            y2=repr(cy))
    elif marker.shape == "o*":
        xml.SubElement(marker_xml, "circle", cx=repr(cx), cy=repr(cy), r=repr(marker.size / 2))
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle, cx, cy),
            x1=repr(cx),
            x2=repr(cx),
            y1=repr(cy - (marker.size / 2)),
            y2=repr(cy + (marker.size / 2)))
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle + 60, cx, cy),
            x1=repr(cx),
            x2=repr(cx),
            y1=repr(cy - (marker.size / 2)),
            y2=repr(cy + (marker.size / 2)))
        xml.SubElement(
            marker_xml,
            "line",
            transform="rotate(%r, %r, %r)" % (-marker.angle - 60, cx, cy),
            x1=repr(cx),
            x2=repr(cx),
            y1=repr(cy - (marker.size / 2)),
            y2=repr(cy + (marker.size / 2)))

    if marker.label: # Never compute a text layout unless we have to.
        _draw_text(
            root=marker_xml,
            text=marker.label,
            x=cx,
            y=cy,
            style=toyplot.style.combine(
                {
                    "-toyplot-vertical-align": "middle",
                    "fill": toyplot.color.near_black,
                    "font-size": "%rpx" % (marker.size * 0.75),
                    "stroke": "none",
                    "text-anchor": "middle",
                },
                marker.lstyle),
            )
    return marker_xml

_draw_marker.variations = {
    "-": ("|", 90),
    "/": ("|", -45),
    "\\": ("|", 45),
    "x": ("+", 45),
    ">": ("^", -90),
    "v": ("^", 180),
    "<": ("^", 90),
    "d": ("s", 45),
    "o-": ("o|", 90),
    "ox": ("o+", 45),
    }


def _axis_transform(x1, y1, x2, y2, offset, return_length=False):
    p = numpy.row_stack(((x1, y1), (x2, y2)))
    basis = p[1] - p[0]
    length = numpy.linalg.norm(basis)
    theta = numpy.rad2deg(numpy.arctan2(basis[1], basis[0]))
    transform = str()
    if p[0][0] or p[0][1]:
        transform += "translate(%s,%s)" % (p[0][0], p[0][1])
    if theta:
        transform += "rotate(%s)" % theta
    if offset:
        transform += "translate(0,%s)" % offset
    if return_length:
        return transform, length
    return transform


@dispatch(toyplot.canvas.Canvas, RenderContext)
def _render(canvas, context):
    # Create the root SVG element.
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

    # Render everything on the canvas.
    for child in canvas._children:
        _render(canvas, child._finalize(), context.copy(parent=svg_xml))

    # Create a container for any Javascript code.
    javascript_xml = xml.SubElement(
        context.parent,
        "div",
        attrib={"class": "toyplot-behavior"},
        )

    # Register a Javascript module to keep track of the canvas id.
    context.define("toyplot/canvas/id", value=context.get_id(canvas))
    # Register a Javascript module to keep track of the canvas.
    context.define("toyplot/canvas", ["toyplot/canvas/id"], factory="""function(canvas_id)
    {
        return document.querySelector("#" + canvas_id);
    }""")

    # Register a Javascript module for storing table data.
    context.define("toyplot/tables", factory="""function()
    {
        var tables = [];

        var module = {};

        module.store = function(owner, key, names, columns)
        {
            tables.push({owner: owner, key: key, names: names, columns: columns});
        }

        module.get_csv = function(owner, key)
        {
            var csv = "";
            for(var i = 0; i != tables.length; ++i)
            {
                var table = tables[i];
                if(table.owner != owner)
                    continue;
                if(table.key != key)
                    continue;

                csv += table.names.join(",") + "\\n";
                for(var i = 0; i != table.columns[0].length; ++i)
                {
                  for(var j = 0; j != table.columns.length; ++j)
                  {
                    if(j)
                      csv += ",";
                    csv += table.columns[j][i];
                  }
                  csv += "\\n";
                }
                return csv;
            }
        }

        return module;
    }""")

    # Register a Javascript module for saving data from the browser.
    context.define("toyplot/io", factory="""function()
    {
        var module = {};
        module.save_file = function(mime_type, charset, data, filename)
        {
            var uri = "data:" + mime_type + ";charset=" + charset + "," + data;
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = filename;

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
        };
        return module;
    }""")

    # Register a Javascript module to provide a popup context menu.
    context.define("toyplot/menus/context", ["toyplot/root", "toyplot/canvas"], factory="""function(root, canvas)
    {
        var wrapper = document.createElement("div");
        wrapper.innerHTML = "<ul class='toyplot-context-menu' style='background:#eee; border:1px solid #b8b8b8; border-radius:5px; box-shadow: 0px 0px 8px rgba(0%,0%,0%,0.25); margin:0; padding:3px 0; position:fixed; visibility:hidden;'></ul>"
        var menu = wrapper.firstChild;

        root.appendChild(menu);

        var items = [];

        var ignore_mouseup = null;
        function open_menu(e)
        {
            var show_menu = false;
            for(var index=0; index != items.length; ++index)
            {
                var item = items[index];
                if(item.show(e))
                {
                    item.item.style.display = "block";
                    show_menu = true;
                }
                else
                {
                    item.item.style.display = "none";
                }
            }

            if(show_menu)
            {
                ignore_mouseup = true;
                menu.style.left = (e.clientX + 1) + "px";
                menu.style.top = (e.clientY - 5) + "px";
                menu.style.visibility = "visible";
                e.stopPropagation();
                e.preventDefault();
            }
        }

        function close_menu()
        {
            menu.style.visibility = "hidden";
        }

        function contextmenu(e)
        {
            open_menu(e);
        }

        function mousemove(e)
        {
            ignore_mouseup = false;
        }

        function mouseup(e)
        {
            if(ignore_mouseup)
            {
                ignore_mouseup = false;
                return;
            }
            close_menu();
        }

        function keydown(e)
        {
            if(e.key == "Escape" || e.key == "Esc" || e.keyCode == 27)
            {
                close_menu();
            }
        }

        canvas.addEventListener("contextmenu", contextmenu);
        canvas.addEventListener("mousemove", mousemove);
        document.addEventListener("mouseup", mouseup);
        document.addEventListener("keydown", keydown);

        var module = {};
        module.add_item = function(label, show, activate)
        {
            var wrapper = document.createElement("div");
            wrapper.innerHTML = "<li class='toyplot-context-menu-item' style='background:#eee; color:#333; padding:2px 20px; list-style:none; margin:0; text-align:left;'>" + label + "</li>"
            var item = wrapper.firstChild;

            items.push({item: item, show: show});

            function mouseover()
            {
                this.style.background = "steelblue";
                this.style.color = "white";
            }

            function mouseout()
            {
                this.style.background = "#eee";
                this.style.color = "#333";
            }

            function choose_item(e)
            {
                close_menu();
                activate();

                e.stopPropagation();
                e.preventDefault();
            }

            item.addEventListener("mouseover", mouseover);
            item.addEventListener("mouseout", mouseout);
            item.addEventListener("mouseup", choose_item);
            item.addEventListener("contextmenu", choose_item);

            menu.appendChild(item);
        };
        return module;
    }""")

    # Embed Javascript code and dependencies in the container.
    _render_javascript(context.copy(parent=javascript_xml))
    _render(canvas._animation, context.copy(parent=javascript_xml)) # pylint: disable=no-value-for-parameter


def _render_javascript(context):
    # Convert module dependencies into an adjacency list.
    adjacency_list = collections.defaultdict(list)
    for name, (requirements, factory, value) in context._javascript_modules.items():
        for requirement in requirements:
            adjacency_list[name].append(requirement)

    # Identify required modules and sort them into topological order.
    modules = []
    visited = {}
    def search(name, visited, modules):
        visited[name] = True
        for neighbor in adjacency_list[name]:
            if not visited.get(neighbor, False):
                search(neighbor, visited, modules)
        modules.append((name, context._javascript_modules[name]))
    for requirements, arguments, code in context._javascript_calls:
        for requirement in requirements:
            if not visited.get(requirement, False):
                search(requirement, visited, modules)

    # Generate the code.
    script = """(function()
{
var modules={};
"""

    # Initialize required modules.
    for name, (requirements, factory, value) in modules:
        script += """modules["%s"] = """ % name

        if factory is not None:
            script += "("
            script += factory
            script += ")("
            argument_list = ["""modules["%s"]""" % requirement for requirement in requirements]
            script += ",".join(argument_list)
            script += ");\n"
        if value is not None:
            script += json.dumps(value, cls=_NumpyJSONEncoder, sort_keys=True)
            script += ";\n"

    # Make all calls.
    for requirements, arguments, code in context._javascript_calls:
        script += """("""
        script += code
        script += """)("""
        argument_list = ["""modules["%s"]""" % requirement for requirement in requirements]
        argument_list += [json.dumps(argument, cls=_NumpyJSONEncoder, sort_keys=True) for argument in arguments]
        script += ",".join(argument_list)
        script += """);\n"""

    script += """})();"""

    # Create the DOM elements.
    xml.SubElement(context.parent, "script").text = script


def _render_table(owner, key, label, table, filename, context):
    if isinstance(owner, toyplot.mark.Mark) and owner.annotation:
        return
    if isinstance(owner, toyplot.coordinates.Table) and owner.annotation:
        return

    names = []
    columns = []

    if isinstance(table, toyplot.data.Table):
        for name, column in table.items():
            if "toyplot:exportable" in table.metadata(name) and table.metadata(name)["toyplot:exportable"]:
                if column.dtype == toyplot.color.dtype:
                    raise ValueError("Color column table export isn't supported.") # pragma: no cover
                else:
                    names.append(name)
                    columns.append(column.tolist())
    else: # Assume numpy matrix
        for column in table.T:
            names.append(column[0])
            columns.append(column[1:].tolist())

    if not (names and columns):
        return

    owner_id = context.get_id(owner)
    if filename is None:
        filename = "toyplot"

    context.require(
        dependencies=["toyplot/tables", "toyplot/menus/context", "toyplot/io"],
        arguments=[owner_id, key, label, names, columns, filename],
        code="""function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
        {
            tables.store(owner_id, key, names, columns);

            var owner = document.querySelector("#" + owner_id);
            function show_item(e)
            {
                return owner.contains(e.target);
            }

            function choose_item()
            {
                io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
            }

            context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
        }""",
    )


@dispatch(toyplot.canvas.Canvas._AnimationFrames, RenderContext)
def _render(frames, context):
    # Collect animation data.
    for time, time_changes in list(frames.items())[:-1]:
        # Ensure we have an entry for every time, even if there aren't any
        # changes.
        context.animation[time]
        for frame_type, type_changes in time_changes.items():
            for change in type_changes:
                context.animation[time][frame_type].append(
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
            frames=len(times) - 2,
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


@dispatch(toyplot.canvas.Canvas, toyplot.coordinates.Axis, RenderContext)
def _render(canvas, axis, context):
    if context.already_rendered(axis):
        return

    if not axis.show:
        return

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
            vertical_align = "middle"

            if location == "above":
                text_anchor = "start" if axis.ticks.labels.angle > 0 else "end"
            elif location == "below":
                text_anchor = "end" if axis.ticks.labels.angle > 0 else "start"
        else:
            vertical_align = "last-baseline" if location == "above" else "top"
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

            style = toyplot.style.combine(
                {
                    "-toyplot-vertical-align": vertical_align,
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
    vertical_align = "last-baseline" if location == "above" else "top"
    text_anchor = "middle"
    y = axis._label_offset if location == "below" else -axis._label_offset

    _draw_text(
        root=axis_xml,
        text=axis.label.text,
        x=length * 0.5,
        y=y,
        style=toyplot.style.combine(
            {
                "-toyplot-vertical-align": vertical_align,
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
            xml.SubElement(
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
            xml.SubElement(
                coordinates_xml, "text",
                x="0",
                y=repr(y),
                style=_css_style(toyplot.style.combine(
                    {"alignment-baseline": alignment_baseline},
                    axis.interactive.coordinates.label.style,
                    )),
                )

    context.define("toyplot.coordinates.Axis", ["toyplot/canvas"], """
        function(canvas)
        {
            function sign(x)
            {
                return x < 0 ? -1 : x > 0 ? 1 : 0;
            }

            function mix(a, b, amount)
            {
                return ((1.0 - amount) * a) + (amount * b);
            }

            function log(x, base)
            {
                return Math.log(Math.abs(x)) / Math.log(base);
            }

            function in_range(a, x, b)
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
                    if(in_range(segment.range.min, range, segment.range.max))
                        return true;
                }
                return false;
            }

            function to_domain(range, projection)
            {
                for(var i = 0; i != projection.length; ++i)
                {
                    var segment = projection[i];
                    if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                    {
                        if(segment.scale == "linear")
                        {
                            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                            return mix(segment.domain.min, segment.domain.max, amount)
                        }
                        else if(segment.scale[0] == "log")
                        {
                            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                            var base = segment.scale[1];
                            return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                        }
                    }
                }
            }

            var axes = {};

            function display_coordinates(e)
            {
                var current = canvas.createSVGPoint();
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

            canvas.addEventListener("click", display_coordinates);

            var module = {};
            module.show_coordinates = function(axis_id, projection)
            {
                axes[axis_id] = projection;
            }

            return module;
        }""",
        )

    projection = []
    for segment in axis.projection._segments:
        projection.append({
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

    context.require(
        dependencies=["toyplot.coordinates.Axis"],
        arguments=[context.get_id(axis), projection],
        code="""function(axis, axis_id, projection)
        {
            axis.show_coordinates(axis_id, projection);
        }""",
    )


@dispatch(toyplot.canvas.Canvas, toyplot.coordinates.Numberline, RenderContext)
def _render(canvas, numberline, context):
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


@dispatch(toyplot.coordinates.Numberline, toyplot.color.CategoricalMap, RenderContext)
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

@dispatch(toyplot.coordinates.Numberline, toyplot.color.Map, RenderContext)
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


@dispatch(toyplot.coordinates.Numberline, toyplot.mark.Scatterplot, RenderContext)
def _render(numberline, mark, context):
    offset = numberline._child_offset[mark]

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        id=context.get_id(mark),
        attrib={"class": "toyplot-mark-Scatterplot"},
        )
    if offset:
        mark_xml.set("transform", "translate(0,%s)" % -offset)

    _render_table(owner=mark, key="data", label="scatterplot data", table=mark._table, filename=mark._filename, context=context)

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
            _draw_marker(
                series_xml,
                cx=dx,
                cy=0,
                default=toyplot.marker.create(size=dsize, mstyle=dstyle, lstyle=mark._mlstyle),
                marker=dmarker,
                extra_class="toyplot-Datum",
                title=dtitle,
                )


@dispatch(toyplot.canvas.Canvas, toyplot.coordinates.Cartesian, RenderContext)
def _render(canvas, axes, context):
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
            y=axes._ymin_range - axes.label._offset,
            style=axes.label._style,
            )


@dispatch(toyplot.canvas.Canvas, toyplot.coordinates.Table, RenderContext)
def _render(canvas, axes, context):
    axes_xml = xml.SubElement(context.parent, "g", id=context.get_id(
        axes), attrib={"class": "toyplot-coordinates-Table"})

    _render_table(owner=axes, key="data", label="table data", table=axes._cell_data, filename=axes._filename, context=context)

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

        # Optionally render the cell background.
        cell_style = axes._cell_style[cell_selection][0]
        cell_link = axes._cell_link[cell_selection][0]
        cell_title = axes._cell_title[cell_selection][0]
        if cell_style is not None or cell_link is not None or cell_title is not None:
            # Compute the cell boundaries.
            cell_top = axes._cell_top[row_min]
            cell_bottom = axes._cell_bottom[row_max]
            cell_left = axes._cell_left[column_min]
            cell_right = axes._cell_right[column_max]

            cell_parent_xml = axes_xml
            if cell_link is not None:
                cell_parent_xml = xml.SubElement(
                    cell_parent_xml,
                    "a",
                    attrib={"xlink:href": cell_link},
                    )

            cell_xml = xml.SubElement(
                cell_parent_xml,
                "rect",
                x=repr(cell_left),
                y=repr(cell_top),
                width=repr(cell_right - cell_left),
                height=repr(cell_bottom - cell_top),
                style=_css_style({"fill":"transparent", "stroke":"none"}, cell_style),
                )

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
                    style=toyplot.style.combine(cell_lstyle, {"text-anchor": "start"}),
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
                    style=toyplot.style.combine(cell_lstyle, {"text-anchor": "start"}),
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


@dispatch(toyplot.coordinates.Cartesian, type(None), RenderContext)
def _render(axes, mark, context):
    pass


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.BarBoundaries, RenderContext)
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
        left = axes.project("x", left)
        right = axes.project("x", right)
        boundaries = axes.project("y", boundaries)
    elif mark._coordinate_axes.tolist() == ["y", "x"]:
        axis1 = "y"
        axis2 = "x"
        distance1 = "height"
        distance2 = "width"
        left = axes.project("y", left)
        right = axes.project("y", right)
        boundaries = axes.project("x", boundaries)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-BarBoundaries"})

    _render_table(owner=mark, key="data", label="bar data", table=mark._table, filename=mark._filename, context=context)

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


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.BarMagnitudes, RenderContext)
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
        left = axes.project("x", left)
        right = axes.project("x", right)
        boundaries = axes.project("y", boundaries)
    elif mark._coordinate_axes.tolist() == ["y", "x"]:
        axis1 = "y"
        axis2 = "x"
        distance1 = "height"
        distance2 = "width"
        left = axes.project("y", left)
        right = axes.project("y", right)
        boundaries = axes.project("x", boundaries)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-BarMagnitudes"})

    _render_table(owner=mark, key="data", label="bar data", table=mark._table, filename=mark._filename, context=context)

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


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.FillBoundaries, RenderContext)
def _render(axes, mark, context):
    boundaries = numpy.ma.column_stack(
        [mark._table[key] for key in mark._boundaries])

    if mark._coordinate_axes.tolist() == ["x", "y"]:
        position = axes.project("x", mark._table[mark._position[0]])
        boundaries = axes.project("y", boundaries)
    elif mark._coordinate_axes.tolist() == ["y", "x"]:
        position = axes.project("y", mark._table[mark._position[0]])
        boundaries = axes.project("x", boundaries)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-FillBoundaries"})

    _render_table(owner=mark, key="data", label="fill data", table=mark._table, filename=mark._filename, context=context)

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


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.FillMagnitudes, RenderContext)
def _render(axes, mark, context):
    magnitudes = numpy.ma.column_stack(
        [mark._table[mark._baseline[0]]] + [mark._table[key] for key in mark._magnitudes])
    boundaries = numpy.ma.cumsum(magnitudes, axis=1)
    not_null = numpy.invert(
        numpy.ma.any(numpy.ma.getmaskarray(boundaries), axis=1))
    segments = _flat_contiguous(not_null)

    if mark._coordinate_axes.tolist() == ["x", "y"]:
        position = axes.project("x", mark._table[mark._position[0]])
        boundaries = axes.project("y", boundaries)
    elif mark._coordinate_axes.tolist() == ["y", "x"]:
        position = axes.project("y", mark._table[mark._position[0]])
        boundaries = axes.project("x", boundaries)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-FillMagnitudes"})

    _render_table(owner=mark, key="data", label="fill data", table=mark._table, filename=mark._filename, context=context)

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


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.AxisLines, RenderContext)
def _render(axes, mark, context):
    if mark._coordinate_axes[0] == "x":
        p1 = "x1"
        p2 = "x2"
        b1 = "y1"
        b2 = "y2"
        position = axes.project("x", mark._table[mark._coordinates[0]])
        boundary1 = axes._ymin_range
        boundary2 = axes._ymax_range
    elif mark._coordinate_axes[0] == "y":
        p1 = "y1"
        p2 = "y2"
        b1 = "x1"
        b2 = "x2"
        position = axes.project("y", mark._table[mark._coordinates[0]])
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


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.Graph, RenderContext)
def _render(axes, mark, context): # pragma: no cover
    # Project edge coordinates
    for i in range(2):
        if mark._coordinate_axes[i] == "x":
            x = axes.project("x", mark._ecoordinates.T[i])
        elif mark._coordinate_axes[i] == "y":
            y = axes.project("y", mark._ecoordinates.T[i])

    mark_xml = xml.SubElement(context.parent, "g", id=context.get_id(mark), attrib={"class": "toyplot-mark-Graph"})
    _render_table(owner=mark, key="vertex_data", label="graph vertex data", table=mark._vtable, filename=mark._vfilename, context=context)
    _render_table(owner=mark, key="edge_data", label="graph edge data", table=mark._etable, filename=mark._efilename, context=context)

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
            x = axes.project("x", mark._vtable[mark._vcoordinates[i]])
        elif mark._coordinate_axes[i] == "y":
            y = axes.project("y", mark._vtable[mark._vcoordinates[i]])

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
            cx=vx,
            cy=vy,
            default=toyplot.marker.create(size=vsize, mstyle=vstyle, lstyle=mark._vlstyle),
            marker=vmarker,
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


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.Plot, RenderContext)
def _render(axes, mark, context):
    position = mark._table[mark._coordinates[0]]
    series = numpy.ma.column_stack([mark._table[key] for key in mark._series])

    if mark._coordinate_axes[0] == "x":
        position = axes.project("x", position)
        series = axes.project("y", series)
    elif mark._coordinate_axes[0] == "y":
        position = axes.project("y", position)
        series = axes.project("x", series)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(toyplot.style.combine({"fill":"none"}, mark._style)),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-Plot"})

    _render_table(owner=mark, key="data", label="plot data", table=mark._table, filename=mark._filename, context=context)

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
            _draw_marker(
                series_xml,
                cx=dx,
                cy=dy,
                default=toyplot.marker.create(size=dsize, mstyle=dstyle, lstyle=mark._mlstyle),
                marker=dmarker,
                extra_class="toyplot-Datum",
                title=dtitle,
                )


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.Rect, RenderContext)
def _render(axes, mark, context):
    if mark._coordinate_axes.tolist() == ["x", "y"]:
        x1 = axes.project("x", mark._table[mark._left[0]])
        x2 = axes.project("x", mark._table[mark._right[0]])
        y1 = axes.project("y", mark._table[mark._top[0]])
        y2 = axes.project("y", mark._table[mark._bottom[0]])
    elif mark._coordinate_axes.tolist() == ["y", "x"]:
        x1 = axes.project("x", mark._table[mark._top[0]])
        x2 = axes.project("x", mark._table[mark._bottom[0]])
        y1 = axes.project("y", mark._table[mark._left[0]])
        y2 = axes.project("y", mark._table[mark._right[0]])
    mark_xml = xml.SubElement(
        context.parent,
        "g",
        style=_css_style(
            mark._style),
        id=context.get_id(mark),
        attrib={
            "class": "toyplot-mark-Rect"})

    _render_table(owner=mark, key="data", label="rect data", table=mark._table, filename=mark._filename, context=context)

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


@dispatch(toyplot.coordinates.Cartesian, toyplot.mark.Scatterplot, RenderContext)
def _render(axes, mark, context):
    dimension1 = numpy.ma.column_stack([mark._table[key] for key in mark._coordinates[0::2]])
    dimension2 = numpy.ma.column_stack([mark._table[key] for key in mark._coordinates[1::2]])

    if mark._coordinate_axes[0] == "x":
        X = axes.project("x", dimension1)
        Y = axes.project("y", dimension2)
    elif mark._coordinate_axes[0] == "y":
        X = axes.project("x", dimension2)
        Y = axes.project("y", dimension1)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        id=context.get_id(mark),
        attrib={"class": "toyplot-mark-Scatterplot"},
        )

    _render_table(owner=mark, key="data", label="scatterplot", table=mark._table, filename=mark._filename, context=context)

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
            _draw_marker(
                series_xml,
                cx=dx,
                cy=dy,
                default=toyplot.marker.create(size=dsize, mstyle=dstyle, lstyle=mark._mlstyle),
                marker=dmarker,
                extra_class="toyplot-Datum",
                title=dtitle,
                )


@dispatch((toyplot.canvas.Canvas, toyplot.coordinates.Cartesian), toyplot.mark.Text, RenderContext)
def _render(parent, mark, context):
    x = mark._table[mark._coordinates[numpy.where(mark._coordinate_axes == "x")[0][0]]]
    y = mark._table[mark._coordinates[numpy.where(mark._coordinate_axes == "y")[0][0]]]

    if isinstance(parent, toyplot.coordinates.Cartesian):
        x = parent.project("x", x)
        y = parent.project("y", y)

    mark_xml = xml.SubElement(
        context.parent,
        "g",
        id=context.get_id(mark),
        attrib={"class": "toyplot-mark-Text"},
        )

    _render_table(owner=mark, key="data", label="text data", table=mark._table, filename=mark._filename, context=context)

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


@dispatch((toyplot.canvas.Canvas), toyplot.mark.Image, RenderContext)
def _render(parent, mark, context):
    encoded = base64.standard_b64encode(mark.to_png()).decode("ascii")

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
