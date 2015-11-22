# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Support functions for rendering using ReportLab."""

from __future__ import absolute_import
from __future__ import division

import numpy
import reportlab.pdfgen.canvas
import reportlab.pdfbase
import toyplot.color
import toyplot.units


def render(svg, canvas):
    """Render the SVG representation of a toyplot canvas to a ReportLab canvas.

    Parameters
    ----------
    svg: xml.etree.ElementTree.Element
      SVG representation of a :class:`toyplot.canvas.Canvas` returned by
      :func:`toyplot.svg.render()`.

    canvas: reportlab.pdfgen.canvas.Canvas
      ReportLab canvas that will be used to render the plot.
    """
    def get_fill(style):
        if "fill" not in style:
            return None

        color = toyplot.color.css(style["fill"])
        if color is None:
            return color

        fill_opacity = float(style.get("fill-opacity", 1.0))
        opacity = float(style.get("opacity", 1.0))
        return toyplot.color.rgba(
            color["r"],
            color["g"],
            color["b"],
            color["a"] * fill_opacity * opacity,
            )

    def get_stroke(style):
        if "stroke" not in style:
            return None

        color = toyplot.color.css(style["stroke"])
        if color is None:
            return None

        stroke_opacity = float(style.get("stroke-opacity", 1.0))
        opacity = float(style.get("opacity", 1.0))
        return toyplot.color.rgba(
            color["r"],
            color["g"],
            color["b"],
            color["a"] * stroke_opacity * opacity,
            )

    def set_fill_color(canvas, color):
        canvas.setFillColorRGB(color["r"], color["g"], color["b"])
        canvas.setFillAlpha(numpy.asscalar(color["a"]))

    def set_stroke_color(canvas, color):
        canvas.setStrokeColorRGB(color["r"], color["g"], color["b"])
        canvas.setStrokeAlpha(numpy.asscalar(color["a"]))

    def render_element(root, element, canvas, styles):
        canvas.saveState()

        current_style = {}
        if len(styles):
            current_style.update(styles[-1])

        current_style.update(dict(
            [declaration.split(":") for declaration in element.get("style", "").split(";") if declaration != ""]))
        styles.append(current_style)

        if "stroke-width" in current_style:
            canvas.setLineWidth(float(current_style["stroke-width"]))

        if "stroke-dasharray" in current_style:
            canvas.setDash([float(length) for length in current_style["stroke-dasharray"].split(",")])

        if current_style.get("visibility") != "hidden":

            if "transform" in element.attrib:
                for transformation in element.get("transform").split(")")[::1]:
                    if transformation:
                        type, arguments = transformation.split("(")
                        arguments = arguments.split(",")
                        if type.strip() == "translate":
                            if len(arguments) == 2:
                                canvas.translate(float(arguments[0]), float(arguments[1]))
                        elif type.strip() == "rotate":
                            if len(arguments) == 1:
                                canvas.rotate(float(arguments[0]))
                            if len(arguments) == 3:
                                canvas.translate(float(arguments[1]), float(arguments[2]))
                                canvas.rotate(float(arguments[0]))
                                canvas.translate(-float(arguments[1]), -float(arguments[2]))

            if element.tag == "svg":
                if "background-color" in current_style:
                    set_fill_color(canvas, toyplot.color.css(current_style["background-color"]))
                    canvas.rect(
                        0,
                        0,
                        float(element.get("width")[:-2]),
                        float(element.get("height")[:-2]),
                        stroke=0,
                        fill=1,
                        )
                for child in element:
                    render_element(root, child, canvas, styles)

            elif element.tag == "g":
                if element.get("clip-path", None) is not None:
                    clip_id = element.get("clip-path")[5:-1]
                    clip_path = root.find(".//*[@id='%s']" % clip_id)
                    for child in clip_path:
                        if child.tag == "rect":
                            x = float(child.get("x"))
                            y = float(child.get("y"))
                            width = float(child.get("width"))
                            height = float(child.get("height"))
                            path = canvas.beginPath()
                            path.moveTo(x, y)
                            path.lineTo(x + width, y)
                            path.lineTo(x + width, y + height)
                            path.lineTo(x, y + height)
                            path.close()
                            canvas.clipPath(path, stroke=0, fill=1)
                        else:
                            toyplot.log.error("Unhandled clip tag: %s" % child.tag) # pragma: no cover

                for child in element:
                    render_element(root, child, canvas, styles)

            elif element.tag == "clipPath":
                pass

            elif element.tag == "line":
                stroke = get_stroke(current_style)
                if stroke is not None:
                    set_stroke_color(canvas, stroke)
                    canvas.line(
                        float(element.get("x1")),
                        float(element.get("y1")),
                        float(element.get("x2")),
                        float(element.get("y2")),
                        )
            elif element.tag == "path":
                stroke = get_stroke(current_style)
                if stroke is not None:
                    set_stroke_color(canvas, stroke)
                    path = canvas.beginPath()
                    commands = element.get("d").split()
                    while len(commands):
                        command = commands.pop(0)
                        if command == "L":
                            path.lineTo(
                                float(commands.pop(0)), float(commands.pop(0)))
                        elif command == "M":
                            path.moveTo(
                                float(commands.pop(0)), float(commands.pop(0)))
                    canvas.drawPath(path)
            elif element.tag == "polygon":
                fill = get_fill(current_style)
                if fill is not None:
                    set_fill_color(canvas, fill)
                stroke = get_stroke(current_style)
                if stroke is not None:
                    set_stroke_color(canvas, stroke)

                points = [point.split(",") for point in element.get("points").split()]
                path = canvas.beginPath()
                for point in points[:1]:
                    path.moveTo(float(point[0]), float(point[1]))
                for point in points[1:]:
                    path.lineTo(float(point[0]), float(point[1]))
                path.close()
                canvas.drawPath(path, stroke=stroke is not None, fill=fill is not None)
            elif element.tag == "rect":
                fill = get_fill(current_style)
                if fill is not None:
                    set_fill_color(canvas, fill)
                stroke = get_stroke(current_style)
                if stroke is not None:
                    set_stroke_color(canvas, stroke)

                x = float(element.get("x"))
                y = float(element.get("y"))
                width = float(element.get("width"))
                height = float(element.get("height"))
                canvas.rect(x, y, width, height, stroke=stroke is not None, fill=fill is not None)
            elif element.tag == "circle":
                fill = get_fill(current_style)
                if fill is not None:
                    set_fill_color(canvas, fill)
                stroke = get_stroke(current_style)
                if stroke is not None:
                    set_stroke_color(canvas, stroke)

                cx = float(element.get("cx"))
                cy = float(element.get("cy"))
                r = float(element.get("r"))
                canvas.circle(cx, cy, r, stroke=stroke is not None, fill=fill is not None)
            elif element.tag == "text":
                if element.text is not None and element.text != "":

#                    if "font-family" in current_style:
#                        font_description.set_family(
#                            current_style["font-family"])
#                    if "font-weight" in current_style:
#                        font_description.set_weight(
#                            pango.WEIGHT_BOLD if current_style["font-weight"] == "bold" else pango.WEIGHT_NORMAL)
#                    if "font-size" in current_style:
                    font_family = current_style["font-family"]
                    font_size = toyplot.units.convert(current_style["font-size"].strip(), "px")
                    canvas.setFont(font_family, font_size)

                    string_width = reportlab.pdfbase.pdfmetrics.stringWidth(element.text, canvas._fontname, canvas._fontsize)
                    ascent, descent = reportlab.pdfbase.pdfmetrics.getAscentDescent(canvas._fontname, canvas._fontsize)

                    x = float(element.get("x"))
                    y = float(element.get("y"))

                    text_anchor = current_style.get("text-anchor", "start")
                    if text_anchor == "start":
                        pass
                    elif text_anchor == "middle":
                        x -= string_width * 0.5
                    elif text_anchor == "end":
                        x -= string_width

                    dx = toyplot.units.convert(
                        element.get("dx", 0), "px", default="px")
                    x += dx

                    alignment_baseline = current_style.get("alignment-baseline", "middle")
                    if alignment_baseline == "hanging":
                        y += ascent
                    elif alignment_baseline == "central":
                        y += ascent * 0.5
                    elif alignment_baseline == "middle":
                        y += (ascent + descent) * 0.5
                    elif alignment_baseline == "alphabetic":
                        pass
                    else:
                        raise ValueError("Unsupported alignment-baseline: %s" % alignment_baseline) # pragma: no cover

                    baseline_shift = current_style.get("baseline-shift", "0").strip()
                    baseline_shift = toyplot.units.convert(baseline_shift, "px", "px", ascent - descent)
                    y -= baseline_shift

                    fill = get_fill(current_style)
                    if fill is not None:
                        set_fill_color(canvas, fill)
                    stroke = get_stroke(current_style)
                    if stroke is not None:
                        set_stroke_color(canvas, stroke)

                    canvas.translate(x, y)
                    canvas.scale(1, -1)
                    canvas.drawString(0, 0, element.text)

            elif element.tag in ["title"]:
                pass
            else:
                raise Exception("unhandled tag: %s" % element.tag) # pragma: no cover

        styles.pop()
        canvas.restoreState()

    render_element(svg, svg, canvas, [])

