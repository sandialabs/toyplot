
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

    <div align="center" class="toyplot" id="t77ec10743dd44b28a7dee832c1d8571e"><svg height="150.0px" id="ta01c6a73ac4941bb9f59a52f74c488d7" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t48d010dfa0454ac094ab5112e52955df"><toyplot:axes>{"x": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 60.0, "min": 90.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="te07a654fbb4942bea18e54b9d30df646"><rect height="50.0" width="400.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te07a654fbb4942bea18e54b9d30df646)" style="cursor:crosshair"><rect height="50.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50" y="50"></rect><g class="toyplot-mark-Text" id="td0e9d68a8d014b9ca973b3d95cf6b1ed" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[0.0], [0.0], ["Text!"], [0.0], [null], [1.0], [null], [0.4], [0.7607843137254902], [0.6470588235294118], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 250.0, 75.0)" x="250.0" y="75.0">Text!</text></g></g><g class="toyplot-mark-Plot" id="ta1f2a822942f450fbe92a938fb615da3" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="250.0" cy="75.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t77ec10743dd44b28a7dee832c1d8571e text");
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
              var text = document.querySelectorAll("#t77ec10743dd44b28a7dee832c1d8571e text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t77ec10743dd44b28a7dee832c1d8571e";
    
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
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t77ec10743dd44b28a7dee832c1d8571e";
    
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
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
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

    <div align="center" class="toyplot" id="td2e83acb706d48d3aec614e473d3675e"><svg height="300.0px" id="tf5e2462079c84bc08af80e068d2f940a" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t2df354d19e2e4d0d84e8c526e869b2b6"><toyplot:axes>{"x": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 2.0, "min": -2.0}, "range": {"max": 60.0, "min": 240.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t56ee094b9b2c4050a4653ff6691803d6"><rect height="200.0" width="400.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t56ee094b9b2c4050a4653ff6691803d6)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="ta9cae7f8b1b5481e9c39fa8a5d350223" style="fill:none;stroke-width:1"><toyplot:data-table title="Plot Data">{"data": [[0.0, 0.0], [-2.0, 2.0], [null, null], [20.0, 20.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 250.0 240.0 L 250.0 60.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t6a45a1fd5f5b4af4a1f988084857efb6" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[0.0], [1.0], ["Centered"], [0.0], [null], [1.0], [null], [0.4], [0.7607843137254902], [0.6470588235294118], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 250.0, 105.0)" x="250.0" y="105.0">Centered</text></g></g><g class="toyplot-mark-Plot" id="td86a04db1fb44486b37d1475432ef73c" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0.0], [1.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="250.0" cy="105.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#td2e83acb706d48d3aec614e473d3675e text");
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
              var text = document.querySelectorAll("#td2e83acb706d48d3aec614e473d3675e text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="td2e83acb706d48d3aec614e473d3675e";
    
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
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="td2e83acb706d48d3aec614e473d3675e";
    
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
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
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

    <div align="center" class="toyplot" id="ta7ba29a33c444ca5a29061ff2486703c"><svg height="300.0px" id="t6183c48b93234f669c4728888f8da200" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t24b5c69ed141448dac1cfc29fdaca886"><toyplot:axes>{"x": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 2.0, "min": -3.0}, "range": {"max": 60.0, "min": 240.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t2f07b7970abc499ca15e33014c2fc5f9"><rect height="200.0" width="400.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2f07b7970abc499ca15e33014c2fc5f9)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t7b517a4742314473b5cbc6e2e6ae0e69" style="fill:none;stroke-width:1"><toyplot:data-table title="Plot Data">{"data": [[0.0, 0.0], [-3.0, 2.0], [null, null], [20.0, 20.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 250.0 240.0 L 250.0 60.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#ta7ba29a33c444ca5a29061ff2486703c text");
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
              var text = document.querySelectorAll("#ta7ba29a33c444ca5a29061ff2486703c text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="ta7ba29a33c444ca5a29061ff2486703c";
    
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
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="ta7ba29a33c444ca5a29061ff2486703c";
    
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
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
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

    <div align="center" class="toyplot" id="tca9cf51a2a534cb592aae70de14372fb"><svg height="300.0px" id="t77ac7bed32ec485598eec1b0ed3b1e54" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="ta5288c1df6f646edaf3fbdee10914afe"><toyplot:axes>{"x": [{"domain": {"max": 3.0, "min": -2.0}, "range": {"max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 60.0, "min": 240.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t03d586e87e3e497bac7ea40c213ea321"><rect height="200.0" width="500.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t03d586e87e3e497bac7ea40c213ea321)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="tb9793a1792844d8a9a8eb5d684577524" style="fill:none;stroke-width:1"><toyplot:data-table title="Plot Data">{"data": [[-2.0, 3.0], [0.0, 0.0], [null, null], [20.0, 20.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 150.0 L 540.0 150.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t64d561648c45488d95f50f69822df9ad" style="alignment-baseline:hanging;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[-1.0], [0.0], ["Hanging"], [0.0], [null], [1.0], [null], [0.4], [0.7607843137254902], [0.6470588235294118], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:hanging;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 156.0, 150.0)" x="156.0" y="150.0">Hanging</text></g></g><g class="toyplot-mark-Plot" id="tdc6c6948521c484c817fcd03ebbe1ac1" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[-1.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="156.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tc7134f1e1749479bac97d2970e440125" style="alignment-baseline:central;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[0.0], [0.0], ["Central"], [0.0], [null], [1.0], [null], [0.9882352941176471], [0.5529411764705883], [0.3843137254901961], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:central;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 252.0, 150.0)" x="252.0" y="150.0">Central</text></g></g><g class="toyplot-mark-Plot" id="t376104c7c4264d06803e38d72c376717" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="252.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t2baecf31b45042d886c8a1794b9bf894" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[1.0], [0.0], ["Middle"], [0.0], [null], [1.0], [null], [0.5529411764705883], [0.6274509803921569], [0.796078431372549], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 348.0, 150.0)" x="348.0" y="150.0">Middle</text></g></g><g class="toyplot-mark-Plot" id="t4e3c09d99c10486c90c7c761263c422c" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[1.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="348.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#tca9cf51a2a534cb592aae70de14372fb text");
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
              var text = document.querySelectorAll("#tca9cf51a2a534cb592aae70de14372fb text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="tca9cf51a2a534cb592aae70de14372fb";
    
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
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="tca9cf51a2a534cb592aae70de14372fb";
    
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
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
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

    <div align="center" class="toyplot" id="t3f444814f96d41ccb04998e6e4b79a03"><svg height="300.0px" id="t4a02022bb95d43f8a121381790e77f08" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tadf4a15408b44290ae99bb30cad312bd"><toyplot:axes>{"x": [{"domain": {"max": 3.0344827586206899, "min": -2.1379310344827589}, "range": {"max": 640.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 60.0, "min": 240.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t04ca688a35e94f6d9fa3958cfe8521f9"><rect height="200.0" width="600.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t04ca688a35e94f6d9fa3958cfe8521f9)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="600.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t4580a802be874b9aa8e12006a8f5164b" style="fill:none;stroke-width:1"><toyplot:data-table title="Plot Data">{"data": [[-2.0, 3.0], [0.0, 0.0], [null, null], [20.0, 20.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [0.5019607843137255, 0.5019607843137255], [1.0, 1.0], [1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 75.466666666666697 150.0 L 636.13333333333333 150.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="tbd577e265903412b8280878bf3eb4a08" style="alignment-baseline:middle;baseline-shift:-100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[-1.0], [0.0], ["Shift -100%"], [0.0], [null], [1.0], [null], [0.4], [0.7607843137254902], [0.6470588235294118], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:-100%;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 187.60000000000002, 150.0)" x="187.60000000000002" y="150.0">Shift -100%</text></g></g><g class="toyplot-mark-Plot" id="t2baa342a346f4c37a612416586341e1e" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[-1.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="187.60000000000002" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t0da6c80d556d4cefa85c5bb15f3c85e0" style="alignment-baseline:middle;baseline-shift:0;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[0.0], [0.0], ["Shift 0%"], [0.0], [null], [1.0], [null], [0.9882352941176471], [0.5529411764705883], [0.3843137254901961], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:0;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 299.73333333333335, 150.0)" x="299.73333333333335" y="150.0">Shift 0%</text></g></g><g class="toyplot-mark-Plot" id="tb74cd4e247aa4c6383356009d39e8d74" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="299.73333333333335" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tb6c92b87ea1144bd9260808399eee7f3" style="alignment-baseline:middle;baseline-shift:66%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[1.0], [0.0], ["Shift 66%"], [0.0], [null], [1.0], [null], [0.5529411764705883], [0.6274509803921569], [0.796078431372549], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:66%;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 411.86666666666667, 150.0)" x="411.86666666666667" y="150.0">Shift 66%</text></g></g><g class="toyplot-mark-Plot" id="t83859b8462a24702a8867a71b8e25465" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[1.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="411.86666666666667" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t81036b7aeae2487bbdedf2a714705653" style="alignment-baseline:middle;baseline-shift:100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[2.0], [0.0], ["Shift 100%"], [0.0], [null], [1.0], [null], [0.9058823529411765], [0.5411764705882353], [0.7647058823529411], [1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:100%;fill:rgba(90.6%,54.1%,76.5%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 524.0, 150.0)" x="524.0" y="150.0">Shift 100%</text></g></g><g class="toyplot-mark-Plot" id="td59939e089e74b28a36ab47ea0824111" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[2.0], [0.0], ["o"], [7.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="524.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t3f444814f96d41ccb04998e6e4b79a03 text");
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
              var text = document.querySelectorAll("#t3f444814f96d41ccb04998e6e4b79a03 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t3f444814f96d41ccb04998e6e4b79a03";
    
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
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t3f444814f96d41ccb04998e6e4b79a03";
    
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
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


Of course, you're free to combine all four styles in any way that you
like.
