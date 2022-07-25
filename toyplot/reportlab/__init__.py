# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""Support functions for rendering using ReportLab."""


import base64
import io
import re

import numpy
import reportlab.lib.colors
import reportlab.lib.utils

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
    def get_fill(root, style):
        if "fill" not in style:
            return None, None # pragma: no cover

        gradient_id = re.match("^url[(]#(.*)[)]$", style["fill"])
        if gradient_id:
            gradient_id = gradient_id.group(1)
            gradient_xml = root.find(".//*[@id='%s']" % gradient_id)
            if gradient_xml.tag != "linearGradient":
                raise NotImplementedError("Only linear gradients are implemented.") # pragma: no cover
            if gradient_xml.get("gradientUnits") != "userSpaceOnUse":
                raise NotImplementedError("Only userSpaceOnUse gradients are implemented.") # pragma: no cover
            return None, gradient_xml

        color = toyplot.color.css(style["fill"])
        if color is None:
            return None, None

        fill_opacity = float(style.get("fill-opacity", 1.0))
        opacity = float(style.get("opacity", 1.0))
        fill = toyplot.color.rgba(
            color["r"],
            color["g"],
            color["b"],
            color["a"] * fill_opacity * opacity,
            )
        return fill, None

    def get_stroke(style):
        if "stroke" not in style:
            return None # pragma: no cover

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

    def get_line_cap(style):
        if "stroke-linecap" not in style:
            return 0
        elif style["stroke-linecap"] == "butt":
            return 0
        elif style["stroke-linecap"] == "round":
            return 1
        elif style["stroke-linecap"] == "square":
            return 2

    def get_font_family(style):
        if "font-family" not in style:
            return None # pragma: no cover

        bold = True if style.get("font-weight", "") == "bold" else False
        italic = True if style.get("font-style", "") == "italic" else False
        for font_family in style["font-family"].split(","):
            font_family = font_family.lower()
            if font_family in get_font_family.substitutions:
                font_family = get_font_family.substitutions[font_family]
                return get_font_family.font_table[(font_family, bold, italic)]

        raise ValueError("Unknown font family: %s" % style["font-family"]) # pragma: no cover

    get_font_family.font_table = {
        ("courier", False, False): "Courier",
        ("courier", True, False): "Courier-Bold",
        ("courier", False, True): "Courier-Oblique",
        ("courier", True, True): "Courier-BoldOblique",
        ("helvetica", False, False): "Helvetica",
        ("helvetica", True, False): "Helvetica-Bold",
        ("helvetica", False, True): "Helvetica-Oblique",
        ("helvetica", True, True): "Helvetica-BoldOblique",
        ("times", False, False): "Times-Roman",
        ("times", True, False): "Times-Bold",
        ("times", False, True): "Times-Italic",
        ("times", True, True): "Times-BoldItalic",
        }

    get_font_family.substitutions = {
        "courier": "courier",
        "helvetica": "helvetica",
        "monospace": "courier",
        "sans-serif": "helvetica",
        "serif": "times",
        "times": "times",
        }

    def set_fill_color(canvas, color):
        canvas.setFillColorRGB(color["r"], color["g"], color["b"])
        canvas.setFillAlpha(color["a"].item())

    def set_stroke_color(canvas, color):
        canvas.setStrokeColorRGB(color["r"], color["g"], color["b"])
        canvas.setStrokeAlpha(color["a"].item())

    def render_element(root, element, canvas, styles):
        canvas.saveState()

        current_style = {}
        if styles:
            current_style.update(styles[-1])
        for declaration in element.get("style", "").split(";"):
            if declaration == "":
                continue
            key, value = declaration.split(":")
            current_style[key] = value
        styles.append(current_style)

        if "stroke-width" in current_style:
            canvas.setLineWidth(float(current_style["stroke-width"]))

        if "stroke-dasharray" in current_style:
            canvas.setDash([float(length) for length in current_style["stroke-dasharray"].split(",")])

        if current_style.get("visibility") != "hidden":

            if "transform" in element.attrib:
                for transformation in element.get("transform").split(")")[::1]:
                    if transformation:
                        transform, arguments = transformation.split("(")
                        arguments = arguments.split(",")
                        if transform.strip() == "translate":
                            if len(arguments) == 2:
                                canvas.translate(float(arguments[0]), float(arguments[1]))
                        elif transform.strip() == "rotate":
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

                if current_style["border-style"] != "none":
                    set_stroke_color(canvas, toyplot.color.css(current_style["border-color"]))
                    canvas.setLineWidth(float(current_style["border-width"]))
                    canvas.rect(
                        0,
                        0,
                        float(element.get("width")[:-2]),
                        float(element.get("height")[:-2]),
                        stroke=1,
                        fill=0,
                        )

                for child in element:
                    render_element(root, child, canvas, styles)

            elif element.tag == "a":
                # At the moment, it doesn't look like reportlab supports external hyperlinks.
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
                            toyplot.log.error("Unhandled clip tag: %s", child.tag) # pragma: no cover

                for child in element:
                    render_element(root, child, canvas, styles)

            elif element.tag == "clipPath":
                pass

            elif element.tag == "line":
                stroke = get_stroke(current_style)
                if stroke is not None:
                    set_stroke_color(canvas, stroke)
                    canvas.setLineCap(get_line_cap(current_style))
                    canvas.line(
                        float(element.get("x1", 0)),
                        float(element.get("y1", 0)),
                        float(element.get("x2", 0)),
                        float(element.get("y2", 0)),
                        )
            elif element.tag == "path":
                stroke = get_stroke(current_style)
                if stroke is not None:
                    set_stroke_color(canvas, stroke)
                    canvas.setLineCap(get_line_cap(current_style))
                    path = canvas.beginPath()
                    commands = element.get("d").split()
                    while commands:
                        command = commands.pop(0)
                        if command == "L":
                            path.lineTo(
                                float(commands.pop(0)), float(commands.pop(0)))
                        elif command == "M":
                            path.moveTo(
                                float(commands.pop(0)), float(commands.pop(0)))
                    canvas.drawPath(path)
            elif element.tag == "polygon":
                fill, fill_gradient = get_fill(root, current_style)
                if fill_gradient is not None:
                    raise NotImplementedError("Gradient <polygon> not implemented.") # pragma: no cover
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
                fill, fill_gradient = get_fill(root, current_style)
                if fill is not None:
                    set_fill_color(canvas, fill)
                stroke = get_stroke(current_style)
                if stroke is not None:
                    set_stroke_color(canvas, stroke)

                x = float(element.get("x", 0))
                y = float(element.get("y", 0))
                width = float(element.get("width"))
                height = float(element.get("height"))

                path = canvas.beginPath()
                path.moveTo(x, y)
                path.lineTo(x + width, y)
                path.lineTo(x + width, y + height)
                path.lineTo(x, y + height)
                path.close()

                if fill_gradient is not None:
                    pdf_colors = []
                    pdf_offsets = []
                    for stop in fill_gradient:
                        offset = float(stop.get("offset"))
                        color = toyplot.color.css(stop.get("stop-color"))
                        opacity = float(stop.get("stop-opacity"))
                        pdf_colors.append(reportlab.lib.colors.Color(color["r"], color["g"], color["b"], color["a"] * opacity))
                        pdf_offsets.append(offset)
                    canvas.saveState()
                    canvas.clipPath(path, stroke=0, fill=1)
                    canvas.setFillAlpha(1)
                    canvas.linearGradient(
                        float(fill_gradient.get("x1")),
                        float(fill_gradient.get("y1")),
                        float(fill_gradient.get("x2")),
                        float(fill_gradient.get("y2")),
                        pdf_colors,
                        pdf_offsets,
                        )
                    canvas.restoreState()

                canvas.drawPath(path, stroke=stroke is not None, fill=fill is not None)
            elif element.tag == "circle":
                fill, fill_gradient = get_fill(root, current_style)
                if fill_gradient is not None:
                    raise NotImplementedError("Gradient <circle> not implemented.") # pragma: no cover
                if fill is not None:
                    set_fill_color(canvas, fill)
                stroke = get_stroke(current_style)
                if stroke is not None:
                    set_stroke_color(canvas, stroke)

                cx = float(element.get("cx", 0))
                cy = float(element.get("cy", 0))
                r = float(element.get("r"))
                canvas.circle(cx, cy, r, stroke=stroke is not None, fill=fill is not None)
            elif element.tag == "text":
                x = float(element.get("x", 0))
                y = float(element.get("y", 0))
                fill, fill_gradient = get_fill(element, current_style)
                stroke = get_stroke(current_style)
                font_family = get_font_family(current_style)
                font_size = toyplot.units.convert(current_style["font-size"], target="px")
                text = element.text

                canvas.saveState()
                canvas.setFont(font_family, font_size)
                if fill is not None:
                    set_fill_color(canvas, fill)
                if stroke is not None:
                    set_stroke_color(canvas, stroke)
                canvas.translate(x, y)
                canvas.scale(1, -1)
                canvas.drawString(0, 0, text)
                canvas.restoreState()

            elif element.tag == "image":
                import PIL.Image
                image = element.get("xlink:href")
                if not image.startswith("data:image/png;base64,"):
                    raise ValueError("Unsupported image type.") # pragma: no cover
                image = base64.standard_b64decode(image[22:])
                image = io.BytesIO(image)
                image = PIL.Image.open(image)
                image = reportlab.lib.utils.ImageReader(image)

                x = float(element.get("x", 0))
                y = float(element.get("y", 0))
                width = float(element.get("width"))
                height = float(element.get("height"))

                canvas.saveState()
                path = canvas.beginPath()
                set_fill_color(canvas, toyplot.color.rgb(1, 1, 1))
                canvas.rect(x, y, width, height, stroke=0, fill=1)
                canvas.translate(x, y + height)
                canvas.scale(1, -1)
                canvas.drawImage(image=image, x=0, y=0, width=width, height=height, mask=None)
                canvas.restoreState()

            elif element.tag in ["defs", "title"]:
                pass

            else:
                raise Exception("unhandled tag: %s" % element.tag) # pragma: no cover

        styles.pop()
        canvas.restoreState()

    render_element(svg, svg, canvas, [])
