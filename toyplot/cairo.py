# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import absolute_import

import cairo
import numpy
import pango
import pangocairo
import toyplot.color.css

def render(svg, context):
  """Render the SVG representation of a canvas to a Cairo context.

  Parameters
  ----------
  svg : xml.etree.ElementTree.Element
    SVG representation of a :class:`toyplot.Canvas` returned by
    :func:`toyplot.svg.render()`.

  context : cairo.Context
    Cairo context that will be used to render the plot.
  """
  def push_style(new, styles, context):
    current_style = {}
    if len(styles):
      current_style.update(styles[-1])

    current_style.update(dict([declaration.split(":") for declaration in new.split(";") if declaration != ""]))
    styles.append(current_style)

    context.save()

    if "stroke-width" in current_style:
      context.set_line_width(float(current_style["stroke-width"]))

    if "stroke-dasharray" in current_style:
      context.set_dash([float(length) for length in current_style["stroke-dasharray"].split(",")])

    return current_style

  def pop_style(context, styles):
    context.restore()
    styles.pop()

  def get_color_rgba(style, name):
    if name not in style:
      return None
    color = toyplot.color.css.parse(style[name])
    return (color["r"], color["g"], color["b"], color["a"])

  def get_fill(style):
    if "fill" not in style:
      return None
    color = toyplot.color.css.parse(style["fill"])
    if color is None:
      return color

    fill_opacity = float(style.get("fill-opacity", 1.0))
    opacity = float(style.get("opacity", 1.0))
    return (color["r"], color["g"], color["b"], color["a"] * fill_opacity * opacity)

  def get_stroke(style):
    if "stroke" not in style:
      return None
    color = toyplot.color.css.parse(style["stroke"])
    if color is None:
      return color

    stroke_opacity = float(style.get("stroke-opacity", 1.0))
    opacity = float(style.get("opacity", 1.0))
    return (color["r"], color["g"], color["b"], color["a"] * stroke_opacity * opacity)

  def render_element(svg, element, context, styles):
    current_style = push_style(element.get("style", ""), styles, context)

    if current_style.get("visibility") != "hidden":

      if "transform" in element.attrib:
        transform = element.get("transform")
        type, value = transform.split("(")
        value = value[:-1].split(",")
        if type == "rotate":
          if len(value) == 3:
            context.translate(float(value[1]), float(value[2]))
            context.rotate(numpy.radians(float(value[0])))
            context.translate(-float(value[1]), -float(value[2]))

      if element.tag == "svg":
        if "background-color" in current_style:
          context.rectangle(0, 0, float(element.get("width")[:-2]), float(element.get("height")[:-2]))
          context.set_source_rgba(*get_color_rgba(current_style, "background-color"))
          context.fill()
          for child in element:
            render_element(svg, child, context, styles)

      elif element.tag == "g":
        if element.get("clip-path", None) is not None:
          clip_id = element.get("clip-path")[5:-1]
          clip_path = svg.find(".//*[@id='%s']" % clip_id)
          for child in clip_path:
            if child.tag == "rect":
              x = float(child.get("x"))
              y = float(child.get("y"))
              width = float(child.get("width"))
              height = float(child.get("height"))
              context.rectangle(x, y, width, height)
              context.clip()
            else:
              print "Unhandled clip tag: %s" % child.tag

        for child in element:
          render_element(svg, child, context, styles)

      elif element.tag == "clipPath":
        pass

      elif element.tag == "line":
        stroke = get_stroke(current_style)
        if stroke is not None:
          context.move_to(float(element.get("x1")), float(element.get("y1")))
          context.line_to(float(element.get("x2")), float(element.get("y2")))
          context.set_source_rgba(*stroke)
          context.stroke()
      elif element.tag == "polyline":
        stroke = get_stroke(current_style)
        if stroke is not None:
          points = [point.split(",") for point in element.get("points").split()]
          for point in points[:1]:
            context.move_to(float(point[0]), float(point[1]))
          for point in points[1:]:
            context.line_to(float(point[0]), float(point[1]))
          context.set_source_rgba(*stroke)
          context.stroke()
      elif element.tag == "path":
        stroke = get_stroke(current_style)
        if stroke is not None:
          commands = element.get("d").split()
          while len(commands):
            command = commands.pop(0)
            if command == "L":
              context.line_to(float(commands.pop(0)), float(commands.pop(0)))
            elif command == "M":
              context.move_to(float(commands.pop(0)), float(commands.pop(0)))
          context.set_source_rgba(*stroke)
          context.stroke()
      elif element.tag == "polygon":
        points = [point.split(",") for point in element.get("points").split()]
        for point in points[:1]:
          context.move_to(float(point[0]), float(point[1]))
        for point in points[1:]:
          context.line_to(float(point[0]), float(point[1]))
        context.close_path()

        fill = get_fill(current_style)
        if fill is not None:
          context.set_source_rgba(*fill)
          context.fill_preserve()
        stroke = get_stroke(current_style)
        if stroke is not None:
          context.set_source_rgba(*stroke)
          context.stroke_preserve()
        context.new_path()
      elif element.tag == "rect":
        x = float(element.get("x"))
        y = float(element.get("y"))
        width = float(element.get("width"))
        height = float(element.get("height"))
        context.rectangle(x, y, width, height)
        fill = get_fill(current_style)
        if fill is not None:
          context.set_source_rgba(*fill)
          context.fill_preserve()
        stroke = get_stroke(current_style)
        if stroke is not None:
          context.set_source_rgba(*stroke)
          context.stroke_preserve()
        context.new_path()
      elif element.tag == "circle":
        cx = float(element.get("cx"))
        cy = float(element.get("cy"))
        r = float(element.get("r"))
        context.arc(cx, cy, r, 0, numpy.pi * 2)
        fill = get_fill(current_style)
        if fill is not None:
          context.set_source_rgba(*fill)
          context.fill_preserve()
        stroke = get_stroke(current_style)
        if stroke is not None:
          context.set_source_rgba(*stroke)
          context.stroke_preserve()
        context.new_path()
      elif element.tag == "text":
        if element.text is not None and element.text != "":
          pangocairo_context = pangocairo.CairoContext(context)
          pangocairo_context.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
          layout = pangocairo_context.create_layout()
          layout.set_text(element.text)

          font_description = pango.FontDescription()
          if "font-family" in current_style:
            font_description.set_family(current_style["font-family"])
          if "font-weight" in current_style:
            font_description.set_weight(pango.WEIGHT_BOLD if current_style["font-weight"] == "bold" else pango.WEIGHT_NORMAL) 
          if "font-size" in current_style:
            size = current_style["font-size"].strip()
            if size[-2:] == "px":
              size = int(pango.SCALE * float(size[:-2]) * 0.8) # 0.8 is a "fudge factor" because Cairo otherwise renders text larger than SVG
            else:
              raise ValueError("font-size must use pixel units")
            font_description.set_size(size)
          layout.set_font_description(font_description)

          ink_extents, logical_extents = layout.get_pixel_extents()

          x = float(element.get("x"))
          y = float(element.get("y"))

          text_anchor = current_style.get("text-anchor", "start")
          if text_anchor == "start":
            pass
          elif text_anchor ==  "middle":
            x -= logical_extents[2] * 0.5
          elif text_anchor == "end":
            x -= logical_extents[2]

          alignment_baseline = current_style.get("alignment-baseline", "baseline")
          if alignment_baseline == "middle":
            y -= logical_extents[3] * 0.5

          baseline_shift = current_style.get("baseline-shift", "0").strip()
          if baseline_shift[-1] == "%":
            y -= ((ink_extents[3] + logical_extents[3]) * 0.5) * float(baseline_shift[:-1]) * 0.01
          else:
            y -= float(baseline_shift)

          context.new_path()
          context.move_to(x, y)
          pangocairo_context.update_layout(layout)
          pangocairo_context.layout_path(layout)

          fill = get_fill(current_style)
          if fill is not None:
            context.set_source_rgba(*fill)
            context.fill_preserve()
          stroke = get_stroke(current_style)
          if stroke is not None:
            context.set_source_rgba(*stroke)
            context.stroke()
          context.new_path()
      elif element.tag in ["title", "toyplot:axes", "toyplot:data-table"]:
        pass
      else:
        raise Exception("unhandled tag: %s" % element.tag)

    pop_style(context, styles)

  styles = []
  render_element(svg, svg, context, styles)

