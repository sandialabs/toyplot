# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import json
import numpy
import toyplot.svg
import uuid
import xml.etree.ElementTree as xml

def render(canvas, fobj=None):
  """Render the HTML representation of a canvas.

  Generates HTML markup with an embedded SVG representation of the canvas, plus
  JavaScript code for interactivity.  If the canvas contains animation, the
  markup will include an HTML user interface to control playback.

  Parameters
  ----------
  canvas : :class:`toyplot.Canvas`
    The canvas to be rendered.

  fobj : file-like object or string, optional
    The file to write.  Use a string filepath to write data directly to disk.
    If `None` (the default), the HTML tree will be returned to the caller
    instead.

  Returns
  -------
  html : xml.etree.ElementTree.Element or `None`
    HTML representation of `canvas`, as a DOM tree, or `None` if the caller
    specifies the `fobj` parameter.

  Notes
  -----
  The output HTML embeds an SVG representation of the canvas generated with
  :func:`toyplot.svg.render`.

  Note that the output HTML is a fragment wrapped in a <div>, suitable for
  embedding in a larger document.  It is the caller's responsibility to
  supply the <html>, <body> etc. if the result is intended as a standalone
  HTML document.
  """
  svg, svg_animation = toyplot.svg.render(canvas, animation=True)

  root = xml.Element("div", align="center", attrib={"class":"toyplot"}, id="t" + uuid.uuid4().hex)
  root.append(svg)

  controls = xml.SubElement(root, "div", attrib={"class":"toyplot-controls"})
  mark_popup = xml.SubElement(controls, "ul", attrib={"class":"toyplot-mark-popup"}, onmouseleave="this.style.visibility='hidden'", style=toyplot.svg._css_style({
    "background":"rgba(0%,0%,0%,0.75)",
    "border":"0",
    "border-radius":"6px",
    "color":"white",
    "cursor":"default",
    "list-style":"none",
    "margin":"0",
    "padding":"5px",
    "position":"fixed",
    "visibility":"hidden",
    }))
  xml.SubElement(mark_popup, "li", attrib={"class":"toyplot-mark-popup-title"}, style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;")
  xml.SubElement(mark_popup, "li", attrib={"class":"toyplot-mark-popup-save-csv"}, style="border-radius:3px;padding:5px;list-style:none;margin:0;", onmouseover="this.style.color='steelblue';this.style.background='white'", onmouseout="this.style.color='white';this.style.background='steelblue'").text = "Save as .csv"

  if svg.find(".//text") is not None:
    xml.SubElement(controls, "script").text = """
    (function()
    {
      // Workaround for browsers that don't support alignment-baseline
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#%s text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#%s text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    """ % (root.get("id"), root.get("id"))

  if list(svg.iter("toyplot:data-table")):
    xml.SubElement(controls, "script").text = """
    // Allow users to extract embedded raw data
    (function()
    {
      var root_id="%s";

      function save_csv(dataset)
      {
        uri = "data:text/csv;charset=utf-8,";
        data = JSON.parse(dataset.textContent);
        uri += data.names.join(",") + "\\n";
        for(var i = 0; i != data.data[0].length; ++i)
        {
          for(var j = 0; j != data.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data.data[j][i];
          }
          uri += "\\n";
        }

        uri = encodeURI(uri);
        window.open(uri);
      }

      function open_popup(dataset)
      {
        return function(e)
        {
          var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
          popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
          popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
          popup.style.left = (e.clientX - 50) + "px";
          popup.style.top = (e.clientY - 20) + "px";
          popup.style.visibility = "visible";
          e.stopPropagation();
          e.preventDefault();
        }

      }

      var datasets = document.querySelectorAll("#" + root_id + " toyplot\\\\:data-table");
      for(var i = 0; i != datasets.length; ++i)
      {
        var dataset = datasets[i];
        var mark = dataset.parentElement;
        mark.oncontextmenu = open_popup(dataset);
      }
    })();
    """ % (root.get("id"),)

  if svg.find(".//*[@class='toyplot-coordinates']") is not None:
    xml.SubElement(controls, "script").text = """
    (function()
    {
      var root_id=%s;

      function sign(x)
      {
        if(x < 0)
          return -1;
        if(x > 0)
          return 1;
        return 0;
      }

      function log_n(x, base)
      {
        return Math.log(x) / Math.log(base);
      }

      function mix(a, b, amount)
      {
        return ((1.0 - amount) * a) + (amount * b);
      }

      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };

      function display_coordinates(e)
      {
        var x = null;
        var y = null;

        var axes = e.currentTarget.parentElement;
        var data = JSON.parse(axes.querySelector("toyplot\\\\:axes").textContent);

        point = d3_mousePoint(e.target, e);

        for(var i = 0; i != data["x"].length; ++i)
        {
          var segment = data["x"][i];
          if(segment.range.min <= point[0] && point[0] < segment.range.max)
          {
            var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
            }
          }
        }

        for(var i = 0; i != data["y"].length; ++i)
        {
          var segment = data["y"][i];
          if(segment.range.min <= point[1] && point[1] < segment.range.max)
          {
            var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
            }
          }
        }

        if(x !== null && y !== null)
          text = "x=" + x + " y=" + y;
        else if(x !== null)
          text = "x=" + x;
        else if(y !== null)
          text = "y=" + y;
        else
          text = null;

        if(text !== null)
        {
          var coordinates = axes.querySelectorAll(".toyplot-coordinates");
          for(var i = 0; i != coordinates.length; ++i)
          {
            coordinates[i].style.visibility = "visible";
            coordinates[i].querySelector("text").textContent = text;
          }
        }
      }

      function clear_coordinates(e)
      {
        var axes = e.currentTarget.parentElement;
        var coordinates = axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }

      var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
      for(var i = 0; i != axes.length; ++i)
      {
        axes[i].onmousemove = display_coordinates;
        axes[i].onmouseout = clear_coordinates;
      }
    })();
    """ % (json.dumps(root.get("id")),)

  if len(svg_animation) > 1:
    times = numpy.array(sorted(svg_animation.keys()))
    durations = times[1:] - times[:-1]
    changes = [change for time, change in sorted(svg_animation.iteritems())]

    vcr_controls = xml.SubElement(controls, "div", attrib={"class":"toyplot-vcr-controls"})
    xml.SubElement(vcr_controls, "input", title="Frame", type="range", min="0", max=str(len(times)-2), step="1", value="0", id="%s-current-frame" % root.get("id"))
    xml.SubElement(vcr_controls, "button", title="Rewind", style="width:40px;height:24px", id="%s-rewind" % root.get("id")).append(xml.XML("""<svg width="20" height="20"><polygon points="10,5 0,10 10,15" stroke="none" fill="black"/><polygon points="20,5 10,10 20,15" stroke="none" fill="black"/></svg>"""))
    xml.SubElement(vcr_controls, "button", title="Reverse Play", style="width:40px;height:24px", id="%s-reverse-play" % root.get("id")).append(xml.XML("""<svg width="20" height="20"><polygon points="15,5 5,10 15,15" stroke="none" fill="black"/></svg>"""))
    xml.SubElement(vcr_controls, "button", title="Frame Rewind", style="width:40px;height:24px", id="%s-frame-rewind" % root.get("id")).append(xml.XML("""<svg width="20" height="20"><polygon points="15,5 5,10 15,15" stroke="none" fill="black"/><rect x="17" y="5" width="2" height="10" stroke="none" fill="black"/></svg>"""))
    xml.SubElement(vcr_controls, "button", title="Stop", style="width:40px;height:24px", id="%s-stop" % root.get("id")).append(xml.XML("""<svg width="20" height="20"><rect x="5" y="5" width="10" height="10" stroke="none" fill="black"/></svg>"""))
    xml.SubElement(vcr_controls, "button", title="Frame Advance", style="width:40px;height:24px", id="%s-frame-advance" % root.get("id")).append(xml.XML("""<svg width="20" height="20"><polygon points="5,5 15,10 5,15" stroke="none" fill="black"/><rect x="1" y="5" width="2" height="10" stroke="none" fill="black"/></svg>"""))
    xml.SubElement(vcr_controls, "button", title="Play", style="width:40px;height:24px", id="%s-forward-play" % root.get("id")).append(xml.XML("""<svg width="20" height="20"><polygon points="5,5 15,10 5,15" stroke="none" fill="black"/></svg>"""))
    xml.SubElement(vcr_controls, "button", title="Fast Forward", style="width:40px;height:24px", id="%s-fast-forward" % root.get("id")).append(xml.XML("""<svg width="20" height="20"><polygon points="0,5 10,10 0,15" stroke="none" fill="black"/><polygon points="10,5 20,10 10,15" stroke="none" fill="black"/></svg>"""))

    xml.SubElement(controls, "script").text = """
    (function()
    {
      var root_id = %s;
      var frame_durations = %s;
      var state_changes = %s;

      var current_frame = null;
      var timeout = null;

      function on_set_frame()
      {
        if(timeout !== null)
          window.clearTimeout(timeout);
        timeout = null;
        set_current_frame(document.getElementById(root_id + "-current-frame").valueAsNumber);
        for(var frame = 0; frame <= current_frame; ++frame)
          render_changes(frame);
      }

      function on_frame_rewind()
      {
        if(timeout !== null)
          window.clearTimeout(timeout);
        set_current_frame((current_frame - 1 + frame_durations.length) %% frame_durations.length);
        for(var frame = 0; frame <= current_frame; ++frame)
          render_changes(frame);
      }

      function on_rewind()
      {
        render_changes(0);
        set_current_frame(0);
      }

      function on_play_reverse()
      {
        if(timeout !== null)
          window.clearTimeout(timeout);
        timeout = window.setTimeout(play_reverse, frame_durations[(current_frame - 1 + frame_durations.length) %% frame_durations.length] * 1000);
      }

      function on_stop()
      {
        if(timeout !== null)
          window.clearTimeout(timeout);
        timeout = null;
      }

      function on_play_forward()
      {
        if(timeout !== null)
          window.clearTimeout(timeout);
        timeout = window.setTimeout(play_forward, frame_durations[current_frame] * 1000);
      }

      function on_fast_forward()
      {
        for(var frame = 0; frame != frame_durations.length; ++frame)
          render_changes(frame);
        set_current_frame(frame_durations.length - 1);
      }

      function on_frame_advance()
      {
        if(timeout !== null)
          window.clearTimeout(timeout);
        set_current_frame((current_frame + 1) %% frame_durations.length);
        render_changes(current_frame);
      }

      function set_current_frame(frame)
      {
        current_frame = frame;
        document.getElementById(root_id + "-current-frame").value = frame;
      }

      function play_reverse()
      {
        set_current_frame((current_frame - 1 + frame_durations.length) %% frame_durations.length);
        for(var frame = 0; frame <= current_frame; ++frame)
          render_changes(frame);
        timeout = window.setTimeout(play_reverse, frame_durations[(current_frame - 1 + frame_durations.length) %% frame_durations.length] * 1000);
      }

      function play_forward()
      {
        set_current_frame((current_frame + 1) %% frame_durations.length);
        render_changes(current_frame);
        timeout = window.setTimeout(play_forward, frame_durations[current_frame] * 1000);
      }

      var item_cache = {};
      function get_item(id)
      {
        if(!(id in item_cache))
          item_cache[id] = document.getElementById(id);
        return item_cache[id];
      }

      function render_changes(frame)
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
          else if(type == "set-datum-text")
          {
            for(var i = 0; i != type_changes.length; ++i)
            {
              var datum_text = type_changes[i];
              var datum = get_item(datum_text[0]).querySelectorAll(".toyplot-Series")[datum_text[1]].querySelectorAll(".toyplot-Datum")[datum_text[2]];
              datum.textContent = datum_text[3];
            }
          }
        }
      }

      set_current_frame(0);
      render_changes(current_frame);

      document.getElementById(root_id + "-current-frame").oninput = on_set_frame;
      document.getElementById(root_id + "-rewind").onclick = on_rewind;
      document.getElementById(root_id + "-reverse-play").onclick = on_play_reverse;
      document.getElementById(root_id + "-frame-rewind").onclick = on_frame_rewind;
      document.getElementById(root_id + "-stop").onclick = on_stop;
      document.getElementById(root_id + "-frame-advance").onclick = on_frame_advance;
      document.getElementById(root_id + "-forward-play").onclick = on_play_forward;
      document.getElementById(root_id + "-fast-forward").onclick = on_fast_forward;

    })();
    """ % (
      json.dumps(root.get("id")),
      json.dumps(durations.tolist()),
      json.dumps(changes),
      )

  if isinstance(fobj, basestring):
    with open(fobj, "w") as file:
      file.write(xml.tostring(root, method="html"))
  elif fobj is not None:
    fobj.write(xml.tostring(root, method="html"))
  else:
    return root

