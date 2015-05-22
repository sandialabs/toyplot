
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _text:

Text
====

Alignment
---------

By default, a text datum in Toyplot is centered vertically and
horizontally on its coordinates. For example, in the following figure we
rendered some text, then plotted its coordinates using a black dot:

.. code:: python

    import toyplot
    
    canvas = toyplot.Canvas(width=500, height=150)
    axes = canvas.axes(show=False)
    axes.text(0, 0, "Text!", style={"font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7);



.. raw:: html

    <div align="center" class="toyplot" id="t39153f1804b24cf8bd7c03ad7800672f"><svg height="150.0px" id="tcd027c4e36d146ddaff179142d171172" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="te968e50c093147e386ffd4bd75a4c85d"><toyplot:axes>{"x": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 60.0, "min": 90.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t79e89f13b2e745038c7edff00489f89e"><rect height="50.0" width="400.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t79e89f13b2e745038c7edff00489f89e)" style="cursor:crosshair"><rect height="50.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50" y="50"></rect><g class="toyplot-mark-Text" id="t2b650f96dd3e483b80ce333e0150330f" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[0.0], [0.0], ["Text!"], [0.0], [null], [1.0], [null], [0.4], [0.7607843137254902], [0.6470588235294118], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 250.0, 75.0)" x="250.0" y="75.0">Text!</text></g></g><g class="toyplot-mark-Plot" id="ta4dfb55f5c4a483da2d2df4a96faa9ec" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="250.0" cy="75.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    // Workaround for browsers that don't support alignment-baseline.
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t39153f1804b24cf8bd7c03ad7800672f text");
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
          var text = document.querySelectorAll("#t39153f1804b24cf8bd7c03ad7800672f text");
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
    </script><script>
    // Allow users to extract embedded raw data.
    (function()
    {
      function save_csv(dataset)
      {
        uri = "data:text/csv;charset=utf-8,";
        data = JSON.parse(dataset.textContent);
        uri += data.names.join(",") + "\n";
        for(var i = 0; i != data.data[0].length; ++i)
        {
          for(var j = 0; j != data.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data.data[j][i];
          }
          uri += "\n";
        }
    
        uri = encodeURI(uri);
        window.open(uri);
      }
    
      function open_popup(dataset)
      {
        return function(e)
        {
          var popup = document.querySelector("#t39153f1804b24cf8bd7c03ad7800672f .toyplot-mark-popup");
          popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
          popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
          popup.style.left = (e.clientX - 50) + "px";
          popup.style.top = (e.clientY - 20) + "px";
          popup.style.visibility = "visible";
          e.stopPropagation();
          e.preventDefault();
        }
    
      }
    
      var datasets = document.querySelectorAll("#t39153f1804b24cf8bd7c03ad7800672f toyplot\\:data-table");
      for(var i = 0; i != datasets.length; ++i)
      {
        var dataset = datasets[i];
        var mark = dataset.parentElement;
        mark.oncontextmenu = open_popup(dataset);
      }
    })();
    </script><script>
    // Display mouse coordinates.
    (function()
    {
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
        var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
        point = d3_mousePoint(e.target, e);
    
        for(var i = 0; i != data["x"].length; ++i)
        {
          var segment = data["x"][i];
          if(Math.min(segment.range.min, segment.range.max) <= point[0] && point[0] < Math.max(segment.range.min, segment.range.max))
          {
            var amount = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              x = Number(mix(segment.domain.min, segment.domain.max, amount)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), amount))).toFixed(2);
            }
          }
        }
    
        for(var i = 0; i != data["y"].length; ++i)
        {
          var segment = data["y"][i];
          if(Math.min(segment.range.min, segment.range.max) <= point[1] && point[1] < Math.max(segment.range.min, segment.range.max))
          {
            var amount = (point[1] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              y = Number(mix(segment.domain.min, segment.domain.max, amount)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), amount))).toFixed(2);
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
    
      var axes = document.querySelectorAll("#t39153f1804b24cf8bd7c03ad7800672f .toyplot-axes-Cartesian .toyplot-coordinate-events");
      for(var i = 0; i != axes.length; ++i)
      {
        axes[i].onmousemove = display_coordinates;
        axes[i].onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


To control the horizontal alignment, use the ``text-anchor`` CSS
attribute to change the text justification relative to its X coordinate:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes(show=False)
    
    axes.plot([0, 0], [-2, 2], color="gray", style={"stroke-width":1})
    
    axes.text(0, 1, "Centered", style={"text-anchor":"middle", "font-size":"24px"})
    axes.scatterplot(0, 1, color="black", size=7)
    
    axes.text(0, 0, "Left Justified", style={"text-anchor":"begin", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7)
    
    axes.text(0, -1, "Right Justified", style={"text-anchor":"end", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black", size=7);


::


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-2-0549153a840e> in <module>()
          7 axes.scatterplot(0, 1, color="black", size=7)
          8 
    ----> 9 axes.text(0, 0, "Left Justified", style={"text-anchor":"begin", "font-size":"24px"})
         10 axes.scatterplot(0, 0, color="black", size=7)
         11 


    /Users/tshead/src/toyplot/toyplot/axes.pyc in text(self, a, b, text, angle, fill, colormap, palette, opacity, title, style)
       1180 
       1181     self._update_domain(table["x"], table["y"])
    -> 1182     self._expand_domain_range(table["x"], table["y"], toyplot.text.extents(table["text"], table["angle"], style))
       1183 
       1184     self._children.append(toyplot.mark.Text(table=table, coordinates=["x", "y"], axes=["x", "y"], text="text", angle="angle", fill="toyplot:fill", opacity="opacity", title="title", style=style))


    /Users/tshead/src/toyplot/toyplot/text.pyc in extents(text, angle, style)
         42     right = x
         43   else:
    ---> 44     raise ValueError("Unknown text-anchor value: %s" % text_anchor)
         45 
         46   # Compute top/bottom extents relative to the text baseline.


    ValueError: Unknown text-anchor value: begin



.. raw:: html

    <div align="center" class="toyplot" id="t5ee52189f9f04d5cbb60e1f921c4be04"><svg height="300.0px" id="t96be0b323b704f1695624fd161747556" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="te6751cf0d7074c3380062766353d0875"><toyplot:axes>{"x": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 2.0, "min": -2.0}, "range": {"max": 60.0, "min": 240.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t3cd0d7c3c2a14344bb3d6041393ab49d"><rect height="200.0" width="400.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t3cd0d7c3c2a14344bb3d6041393ab49d)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="tbfbaadea86fb40c08157cbeebe83b247" style="fill:none;stroke-width:1"><toyplot:data-table title="Plot Data">{"data": [[0.0, 0.0], [-2.0, 2.0], [null, null], [20.0, 20.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 250.0 240.0 L 250.0 60.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t7a0220ab8d1348dc881cf9b4301c414f" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[0.0], [1.0], ["Centered"], [0.0], [null], [1.0], [null], [0.4], [0.7607843137254902], [0.6470588235294118], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 250.0, 105.0)" x="250.0" y="105.0">Centered</text></g></g><g class="toyplot-mark-Plot" id="t69d48c6e5057482585e2d06ebb0100b8" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0.0], [1.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="250.0" cy="105.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    // Workaround for browsers that don't support alignment-baseline.
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t5ee52189f9f04d5cbb60e1f921c4be04 text");
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
          var text = document.querySelectorAll("#t5ee52189f9f04d5cbb60e1f921c4be04 text");
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
    </script><script>
    // Allow users to extract embedded raw data.
    (function()
    {
      function save_csv(dataset)
      {
        uri = "data:text/csv;charset=utf-8,";
        data = JSON.parse(dataset.textContent);
        uri += data.names.join(",") + "\n";
        for(var i = 0; i != data.data[0].length; ++i)
        {
          for(var j = 0; j != data.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data.data[j][i];
          }
          uri += "\n";
        }
    
        uri = encodeURI(uri);
        window.open(uri);
      }
    
      function open_popup(dataset)
      {
        return function(e)
        {
          var popup = document.querySelector("#t5ee52189f9f04d5cbb60e1f921c4be04 .toyplot-mark-popup");
          popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
          popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
          popup.style.left = (e.clientX - 50) + "px";
          popup.style.top = (e.clientY - 20) + "px";
          popup.style.visibility = "visible";
          e.stopPropagation();
          e.preventDefault();
        }
    
      }
    
      var datasets = document.querySelectorAll("#t5ee52189f9f04d5cbb60e1f921c4be04 toyplot\\:data-table");
      for(var i = 0; i != datasets.length; ++i)
      {
        var dataset = datasets[i];
        var mark = dataset.parentElement;
        mark.oncontextmenu = open_popup(dataset);
      }
    })();
    </script><script>
    // Display mouse coordinates.
    (function()
    {
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
        var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
        point = d3_mousePoint(e.target, e);
    
        for(var i = 0; i != data["x"].length; ++i)
        {
          var segment = data["x"][i];
          if(Math.min(segment.range.min, segment.range.max) <= point[0] && point[0] < Math.max(segment.range.min, segment.range.max))
          {
            var amount = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              x = Number(mix(segment.domain.min, segment.domain.max, amount)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), amount))).toFixed(2);
            }
          }
        }
    
        for(var i = 0; i != data["y"].length; ++i)
        {
          var segment = data["y"][i];
          if(Math.min(segment.range.min, segment.range.max) <= point[1] && point[1] < Math.max(segment.range.min, segment.range.max))
          {
            var amount = (point[1] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              y = Number(mix(segment.domain.min, segment.domain.max, amount)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), amount))).toFixed(2);
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
    
      var axes = document.querySelectorAll("#t5ee52189f9f04d5cbb60e1f921c4be04 .toyplot-axes-Cartesian .toyplot-coordinate-events");
      for(var i = 0; i != axes.length; ++i)
      {
        axes[i].onmousemove = display_coordinates;
        axes[i].onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


After the anchor has been established, the text can be shifted in
arbitrary amounts, using the ``-toyplot-anchor-shift`` attribute. Note
that this is non-standard CSS, provided by Toyplot for symmetry with the
standard ``baseline-shift`` attribute, below:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes(show=False)
    
    axes.plot([0, 0], [-3, 2], color="gray", style={"stroke-width":1})
    
    axes.text(0, 1, "Shifted +0px", style={"-toyplot-anchor-shift":"0", "text-anchor":"begin", "font-size":"24px"})
    axes.scatterplot(0, 1, color="black", size=7)
    
    axes.text(0, 0, "Shifted +20px", style={"-toyplot-anchor-shift":"20px", "text-anchor":"begin", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7)
    
    axes.text(0, -1, "Shifted +40px", style={"-toyplot-anchor-shift":"40px", "text-anchor":"begin", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black", size=7);
    
    axes.text(0, -2, "Shifted -20px", style={"-toyplot-anchor-shift":"-20px", "text-anchor":"begin", "font-size":"24px"})
    axes.scatterplot(0, -2, color="black", size=7);



::


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-3-ddb8b709d4c8> in <module>()
          4 axes.plot([0, 0], [-3, 2], color="gray", style={"stroke-width":1})
          5 
    ----> 6 axes.text(0, 1, "Shifted +0px", style={"-toyplot-anchor-shift":"0", "text-anchor":"begin", "font-size":"24px"})
          7 axes.scatterplot(0, 1, color="black", size=7)
          8 


    /Users/tshead/src/toyplot/toyplot/axes.pyc in text(self, a, b, text, angle, fill, colormap, palette, opacity, title, style)
       1180 
       1181     self._update_domain(table["x"], table["y"])
    -> 1182     self._expand_domain_range(table["x"], table["y"], toyplot.text.extents(table["text"], table["angle"], style))
       1183 
       1184     self._children.append(toyplot.mark.Text(table=table, coordinates=["x", "y"], axes=["x", "y"], text="text", angle="angle", fill="toyplot:fill", opacity="opacity", title="title", style=style))


    /Users/tshead/src/toyplot/toyplot/text.pyc in extents(text, angle, style)
         42     right = x
         43   else:
    ---> 44     raise ValueError("Unknown text-anchor value: %s" % text_anchor)
         45 
         46   # Compute top/bottom extents relative to the text baseline.


    ValueError: Unknown text-anchor value: begin



.. raw:: html

    <div align="center" class="toyplot" id="tea78908084564d69a274b2c44d690905"><svg height="300.0px" id="tc56d9bf84fbe4902a3fcc2fcdcc7259a" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t55b56fd81f6641c2b47d2a2c135ecaea"><toyplot:axes>{"x": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 2.0, "min": -3.0}, "range": {"max": 60.0, "min": 240.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="tb6b83d35d675487c9047152ad29fd7de"><rect height="200.0" width="400.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb6b83d35d675487c9047152ad29fd7de)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="tc807ba20508640b4bd448400dd77175d" style="fill:none;stroke-width:1"><toyplot:data-table title="Plot Data">{"data": [[0.0, 0.0], [-3.0, 2.0], [null, null], [20.0, 20.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 250.0 240.0 L 250.0 60.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    // Workaround for browsers that don't support alignment-baseline.
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tea78908084564d69a274b2c44d690905 text");
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
          var text = document.querySelectorAll("#tea78908084564d69a274b2c44d690905 text");
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
    </script><script>
    // Allow users to extract embedded raw data.
    (function()
    {
      function save_csv(dataset)
      {
        uri = "data:text/csv;charset=utf-8,";
        data = JSON.parse(dataset.textContent);
        uri += data.names.join(",") + "\n";
        for(var i = 0; i != data.data[0].length; ++i)
        {
          for(var j = 0; j != data.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data.data[j][i];
          }
          uri += "\n";
        }
    
        uri = encodeURI(uri);
        window.open(uri);
      }
    
      function open_popup(dataset)
      {
        return function(e)
        {
          var popup = document.querySelector("#tea78908084564d69a274b2c44d690905 .toyplot-mark-popup");
          popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
          popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
          popup.style.left = (e.clientX - 50) + "px";
          popup.style.top = (e.clientY - 20) + "px";
          popup.style.visibility = "visible";
          e.stopPropagation();
          e.preventDefault();
        }
    
      }
    
      var datasets = document.querySelectorAll("#tea78908084564d69a274b2c44d690905 toyplot\\:data-table");
      for(var i = 0; i != datasets.length; ++i)
      {
        var dataset = datasets[i];
        var mark = dataset.parentElement;
        mark.oncontextmenu = open_popup(dataset);
      }
    })();
    </script><script>
    // Display mouse coordinates.
    (function()
    {
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
        var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
        point = d3_mousePoint(e.target, e);
    
        for(var i = 0; i != data["x"].length; ++i)
        {
          var segment = data["x"][i];
          if(Math.min(segment.range.min, segment.range.max) <= point[0] && point[0] < Math.max(segment.range.min, segment.range.max))
          {
            var amount = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              x = Number(mix(segment.domain.min, segment.domain.max, amount)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), amount))).toFixed(2);
            }
          }
        }
    
        for(var i = 0; i != data["y"].length; ++i)
        {
          var segment = data["y"][i];
          if(Math.min(segment.range.min, segment.range.max) <= point[1] && point[1] < Math.max(segment.range.min, segment.range.max))
          {
            var amount = (point[1] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              y = Number(mix(segment.domain.min, segment.domain.max, amount)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), amount))).toFixed(2);
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
    
      var axes = document.querySelectorAll("#tea78908084564d69a274b2c44d690905 .toyplot-axes-Cartesian .toyplot-coordinate-events");
      for(var i = 0; i != axes.length; ++i)
      {
        axes[i].onmousemove = display_coordinates;
        axes[i].onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


To control vertical alignment, set the text baseline with
``alignment-baseline``. By default, the text baseline will line-up with
the text Y coordinate. CSS typography is a complex topic and there are
many baseline types to accomodate different writing modes and fonts. The
following baselines are likely to be the most useful for Western
scripts. Note the subtle difference between the "central" and "middle"
baselines - the former tends to center the upper-case letters in Western
scripts while the latter tends to center lower-case letters, and is the
Toyplot default:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes(show=False)
    
    axes.plot([-2, 3], [0, 0], color="gray", style={"stroke-width":1})
    
    axes.text(-1, 0, "Hanging", style={"alignment-baseline":"hanging", "font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=7)
    
    axes.text(0, 0, "Central", style={"alignment-baseline":"central", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7)
    
    axes.text(1, 0, "Middle", style={"alignment-baseline":"middle", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black", size=7)
    
    axes.text(2, 0, "Alpha", style={"alignment-baseline":"alphabetic", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black", size=7);



::


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-4-6c0b77bf693b> in <module>()
         13 axes.scatterplot(1, 0, color="black", size=7)
         14 
    ---> 15 axes.text(2, 0, "Alpha", style={"alignment-baseline":"alphabetic", "font-size":"24px"})
         16 axes.scatterplot(2, 0, color="black", size=7);


    /Users/tshead/src/toyplot/toyplot/axes.pyc in text(self, a, b, text, angle, fill, colormap, palette, opacity, title, style)
       1180 
       1181     self._update_domain(table["x"], table["y"])
    -> 1182     self._expand_domain_range(table["x"], table["y"], toyplot.text.extents(table["text"], table["angle"], style))
       1183 
       1184     self._children.append(toyplot.mark.Text(table=table, coordinates=["x", "y"], axes=["x", "y"], text="text", angle="angle", fill="toyplot:fill", opacity="opacity", title="title", style=style))


    /Users/tshead/src/toyplot/toyplot/text.pyc in extents(text, angle, style)
         55     bottom = y
         56   else:
    ---> 57     raise ValueError("Unknown alignment-baseline value: %s" % alignment_baseline)
         58 
         59   # Compute axis-aligned extents regardless of the text rotation angle.


    ValueError: Unknown alignment-baseline value: alphabetic



.. raw:: html

    <div align="center" class="toyplot" id="t6295ea05f9fd4d88a7acd1701c4c5eb3"><svg height="300.0px" id="t459dbc3c9e54486798d6537d4b85dff4" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td8a01d32874743919f47ef0a88992b42"><toyplot:axes>{"x": [{"domain": {"max": 3.0, "min": -2.0}, "range": {"max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 60.0, "min": 240.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t71baec22c0644a6898a32c801b9559e7"><rect height="200.0" width="500.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t71baec22c0644a6898a32c801b9559e7)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="tcf447ab51b044b18abc69d5065589a32" style="fill:none;stroke-width:1"><toyplot:data-table title="Plot Data">{"data": [[-2.0, 3.0], [0.0, 0.0], [null, null], [20.0, 20.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 150.0 L 540.0 150.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t3074014f36194e04b02f491000193a23" style="alignment-baseline:hanging;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[-1.0], [0.0], ["Hanging"], [0.0], [null], [1.0], [null], [0.4], [0.7607843137254902], [0.6470588235294118], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:hanging;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 156.0, 150.0)" x="156.0" y="150.0">Hanging</text></g></g><g class="toyplot-mark-Plot" id="t96be0b323b704f1695624fd161747556" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[-1.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="156.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tb15e3e3aa01e40d19e83993beea07916" style="alignment-baseline:central;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[0.0], [0.0], ["Central"], [0.0], [null], [1.0], [null], [0.9882352941176471], [0.5529411764705883], [0.3843137254901961], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:central;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 252.0, 150.0)" x="252.0" y="150.0">Central</text></g></g><g class="toyplot-mark-Plot" id="tf9567b5249684cc7a5127b39b0a91924" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="252.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t7605f5d5314f422884703a9c85a94abd" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[1.0], [0.0], ["Middle"], [0.0], [null], [1.0], [null], [0.5529411764705883], [0.6274509803921569], [0.796078431372549], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 348.0, 150.0)" x="348.0" y="150.0">Middle</text></g></g><g class="toyplot-mark-Plot" id="t9c9f021e37824f378427b94e82b91796" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[1.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="348.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    // Workaround for browsers that don't support alignment-baseline.
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t6295ea05f9fd4d88a7acd1701c4c5eb3 text");
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
          var text = document.querySelectorAll("#t6295ea05f9fd4d88a7acd1701c4c5eb3 text");
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
    </script><script>
    // Allow users to extract embedded raw data.
    (function()
    {
      function save_csv(dataset)
      {
        uri = "data:text/csv;charset=utf-8,";
        data = JSON.parse(dataset.textContent);
        uri += data.names.join(",") + "\n";
        for(var i = 0; i != data.data[0].length; ++i)
        {
          for(var j = 0; j != data.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data.data[j][i];
          }
          uri += "\n";
        }
    
        uri = encodeURI(uri);
        window.open(uri);
      }
    
      function open_popup(dataset)
      {
        return function(e)
        {
          var popup = document.querySelector("#t6295ea05f9fd4d88a7acd1701c4c5eb3 .toyplot-mark-popup");
          popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
          popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
          popup.style.left = (e.clientX - 50) + "px";
          popup.style.top = (e.clientY - 20) + "px";
          popup.style.visibility = "visible";
          e.stopPropagation();
          e.preventDefault();
        }
    
      }
    
      var datasets = document.querySelectorAll("#t6295ea05f9fd4d88a7acd1701c4c5eb3 toyplot\\:data-table");
      for(var i = 0; i != datasets.length; ++i)
      {
        var dataset = datasets[i];
        var mark = dataset.parentElement;
        mark.oncontextmenu = open_popup(dataset);
      }
    })();
    </script><script>
    // Display mouse coordinates.
    (function()
    {
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
        var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
        point = d3_mousePoint(e.target, e);
    
        for(var i = 0; i != data["x"].length; ++i)
        {
          var segment = data["x"][i];
          if(Math.min(segment.range.min, segment.range.max) <= point[0] && point[0] < Math.max(segment.range.min, segment.range.max))
          {
            var amount = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              x = Number(mix(segment.domain.min, segment.domain.max, amount)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), amount))).toFixed(2);
            }
          }
        }
    
        for(var i = 0; i != data["y"].length; ++i)
        {
          var segment = data["y"][i];
          if(Math.min(segment.range.min, segment.range.max) <= point[1] && point[1] < Math.max(segment.range.min, segment.range.max))
          {
            var amount = (point[1] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              y = Number(mix(segment.domain.min, segment.domain.max, amount)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), amount))).toFixed(2);
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
    
      var axes = document.querySelectorAll("#t6295ea05f9fd4d88a7acd1701c4c5eb3 .toyplot-axes-Cartesian .toyplot-coordinate-events");
      for(var i = 0; i != axes.length; ++i)
      {
        axes[i].onmousemove = display_coordinates;
        axes[i].onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


Of course, you can shift the text relative to its baseline by arbitrary
amounts, using ``baseline-shift``. While you are free to use any CSS
length units for the shift, percentages are especially useful, because
they represent a distance relative to the font height:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=300)
    axes = canvas.axes(show=False)
    
    axes.plot([-2, 3], [0, 0], color="gray", style={"stroke-width":1})
    
    axes.text(-1, 0, "Shift -100%", style={"baseline-shift":"-100%", "font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=7)
    
    axes.text(0, 0, "Shift 0%", style={"baseline-shift":"0", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7)
    
    axes.text(1, 0, "Shift 66%", style={"baseline-shift":"66%", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black", size=7);
    
    axes.text(2, 0, "Shift 100%", style={"baseline-shift":"100%", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black", size=7);




.. raw:: html

    <div align="center" class="toyplot" id="t6b3f0b8fd88d4bd3bd2e0c63fb40e766"><svg height="300.0px" id="t876e7412e47a488da0cd167ba88624b6" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t756294853e694e85ba62571c8434920e"><toyplot:axes>{"x": [{"domain": {"max": 3.0344827586206899, "min": -2.1379310344827589}, "range": {"max": 640.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 60.0, "min": 240.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="td23f3f1984d44fe1bded237c5ca55475"><rect height="200.0" width="600.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td23f3f1984d44fe1bded237c5ca55475)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="600.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="tbd3d7523911c47ee9dc7700df1700183" style="fill:none;stroke-width:1"><toyplot:data-table title="Plot Data">{"data": [[-2.0, 3.0], [0.0, 0.0], [null, null], [20.0, 20.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 75.466666666666697 150.0 L 636.13333333333333 150.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="tdc71ed9a369240afb35227d1ed8e1a2e" style="alignment-baseline:middle;baseline-shift:-100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[-1.0], [0.0], ["Shift -100%"], [0.0], [null], [1.0], [null], [0.4], [0.7607843137254902], [0.6470588235294118], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:-100%;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 187.60000000000002, 150.0)" x="187.60000000000002" y="150.0">Shift -100%</text></g></g><g class="toyplot-mark-Plot" id="tc3090c7599cc4d4f936bb4d6cdc2c96f" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[-1.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="187.60000000000002" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t80a2567b8bc243d9a8416eb4c979426b" style="alignment-baseline:middle;baseline-shift:0;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[0.0], [0.0], ["Shift 0%"], [0.0], [null], [1.0], [null], [0.9882352941176471], [0.5529411764705883], [0.3843137254901961], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:0;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 299.73333333333335, 150.0)" x="299.73333333333335" y="150.0">Shift 0%</text></g></g><g class="toyplot-mark-Plot" id="tf0ce324de562417aabd950c868c1429b" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="299.73333333333335" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t5493db31b8c644968187e2f32faf57fd" style="alignment-baseline:middle;baseline-shift:66%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[1.0], [0.0], ["Shift 66%"], [0.0], [null], [1.0], [null], [0.5529411764705883], [0.6274509803921569], [0.796078431372549], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:66%;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 411.86666666666667, 150.0)" x="411.86666666666667" y="150.0">Shift 66%</text></g></g><g class="toyplot-mark-Plot" id="t22bfe373fddb47b6a7ae6f594dcb0721" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[1.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="411.86666666666667" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t5d65abee0f6a49db94ef1be91c1bfc0d" style="alignment-baseline:middle;baseline-shift:100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[2.0], [0.0], ["Shift 100%"], [0.0], [null], [1.0], [null], [0.9058823529411765], [0.5411764705882353], [0.7647058823529411], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:100%;fill:rgba(90.6%,54.1%,76.5%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 524.0, 150.0)" x="524.0" y="150.0">Shift 100%</text></g></g><g class="toyplot-mark-Plot" id="tc3bd49181a96448aa52a8c86bd41bcca" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[2.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="524.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    // Workaround for browsers that don't support alignment-baseline.
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t6b3f0b8fd88d4bd3bd2e0c63fb40e766 text");
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
          var text = document.querySelectorAll("#t6b3f0b8fd88d4bd3bd2e0c63fb40e766 text");
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
    </script><script>
    // Allow users to extract embedded raw data.
    (function()
    {
      function save_csv(dataset)
      {
        uri = "data:text/csv;charset=utf-8,";
        data = JSON.parse(dataset.textContent);
        uri += data.names.join(",") + "\n";
        for(var i = 0; i != data.data[0].length; ++i)
        {
          for(var j = 0; j != data.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data.data[j][i];
          }
          uri += "\n";
        }
    
        uri = encodeURI(uri);
        window.open(uri);
      }
    
      function open_popup(dataset)
      {
        return function(e)
        {
          var popup = document.querySelector("#t6b3f0b8fd88d4bd3bd2e0c63fb40e766 .toyplot-mark-popup");
          popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
          popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
          popup.style.left = (e.clientX - 50) + "px";
          popup.style.top = (e.clientY - 20) + "px";
          popup.style.visibility = "visible";
          e.stopPropagation();
          e.preventDefault();
        }
    
      }
    
      var datasets = document.querySelectorAll("#t6b3f0b8fd88d4bd3bd2e0c63fb40e766 toyplot\\:data-table");
      for(var i = 0; i != datasets.length; ++i)
      {
        var dataset = datasets[i];
        var mark = dataset.parentElement;
        mark.oncontextmenu = open_popup(dataset);
      }
    })();
    </script><script>
    // Display mouse coordinates.
    (function()
    {
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
        var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
        point = d3_mousePoint(e.target, e);
    
        for(var i = 0; i != data["x"].length; ++i)
        {
          var segment = data["x"][i];
          if(Math.min(segment.range.min, segment.range.max) <= point[0] && point[0] < Math.max(segment.range.min, segment.range.max))
          {
            var amount = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              x = Number(mix(segment.domain.min, segment.domain.max, amount)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), amount))).toFixed(2);
            }
          }
        }
    
        for(var i = 0; i != data["y"].length; ++i)
        {
          var segment = data["y"][i];
          if(Math.min(segment.range.min, segment.range.max) <= point[1] && point[1] < Math.max(segment.range.min, segment.range.max))
          {
            var amount = (point[1] - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              y = Number(mix(segment.domain.min, segment.domain.max, amount)).toFixed(2);
            }
            else if(segment.scale == "log")
            {
              y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), amount))).toFixed(2);
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
    
      var axes = document.querySelectorAll("#t6b3f0b8fd88d4bd3bd2e0c63fb40e766 .toyplot-axes-Cartesian .toyplot-coordinate-events");
      for(var i = 0; i != axes.length; ++i)
      {
        axes[i].onmousemove = display_coordinates;
        axes[i].onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


Of course, you're free to combine all four styles in any way that you
like.
