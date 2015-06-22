
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

    <div align="center" class="toyplot" id="t10b3562564a34be086607a639c3a2e1b"><svg height="150.0px" id="t29cd165904794b72a3d600312e3cfe4a" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="te8c836ea781348cda8abac21cb5d4ea0"><clipPath id="tb23180f3673f415aa0c42cb544dd4f6e"><rect height="50.0" width="400.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb23180f3673f415aa0c42cb544dd4f6e)" style="cursor:crosshair"><rect height="50.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Text" id="t6af45b2049b24715ba96e80523508c2f" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 250.0, 75.0)" x="250.0" y="75.0">Text!</text></g></g><g class="toyplot-mark-Plot" id="td6c932afa96146939a114ea44edc7ac4" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="250.0" cy="75.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t10b3562564a34be086607a639c3a2e1b text");
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
          var text = document.querySelectorAll("#t10b3562564a34be086607a639c3a2e1b text");
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
    (function()
    {
      var data_tables = [{"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "td6c932afa96146939a114ea44edc7ac4", "title": "Plot Data"}];
    
      function save_csv(data_table)
      {
        uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
          }
          uri += "\n";
        }
    
        uri = encodeURI(uri);
        window.open(uri);
      }
    
      function open_popup(data_table)
      {
        return function(e)
        {
          var popup = document.querySelector("#t10b3562564a34be086607a639c3a2e1b .toyplot-mark-popup");
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
    </script><script>
    (function()
    {
      var axes = {"te8c836ea781348cda8abac21cb5d4ea0": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 90.0}, "scale": "linear"}]}};
    
      function sign(x)
      {
        return x < 0 ? -1 : x > 0 ? 1 : 0;
      }
    
      function log_n(x, base)
      {
        return Math.log(Math.abs(x)) / Math.log(base);
      }
    
      function mix(a, b, amount)
      {
        return ((1.0 - amount) * a) + (amount * b);
      }
    
      function to_domain(projection, range)
      {
        for(var i = 0; i != projection.length; ++i)
        {
          var segment = projection[i];
          if(Math.min(segment.range.bounds.min, segment.range.bounds.max) <= point[0] && point[0] < Math.max(segment.range.bounds.min, segment.range.bounds.max))
          {
            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              return mix(segment.domain.min, segment.domain.max, amount)
            }
            else if(segment.scale[0] == "log")
            {
              var base = segment.scale[1];
              return sign(segment.domain.min) * Math.pow(base, mix(log_n(Math.abs(segment.domain.min), base), log_n(Math.abs(segment.domain.max), base), amount));
            }
          }
        }
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
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
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
    
    axes.text(0, 0, "Left Justified", style={"text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7)
    
    axes.text(0, -1, "Right Justified", style={"text-anchor":"end", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black", size=7);



.. raw:: html

    <div align="center" class="toyplot" id="t2359eabd0ed44dc886fa18ce575c229b"><svg height="300.0px" id="t88baca359b8e48eda14aa1fb4899bc41" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t47eb24f3062e46e287fbfbf03dc20161"><clipPath id="t1a962a1f969043faa6bd943e5634c66f"><rect height="200.0" width="400.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t1a962a1f969043faa6bd943e5634c66f)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t1109ac3bd69b4687a1876574761a6f1f" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 256.55172413793105 240.0 L 256.55172413793105 60.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="te3253d945db64335a53e09c015d44325" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 256.55172413793105, 105.0)" x="256.55172413793105" y="105.0">Centered</text></g></g><g class="toyplot-mark-Plot" id="t3fc2cd49b0a54f92818c706222ba6bdb" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="256.55172413793105" cy="105.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t906181a646d14bc6b9d2fc261d0266bf" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 256.55172413793105, 150.0)" x="256.55172413793105" y="150.0">Left Justified</text></g></g><g class="toyplot-mark-Plot" id="t5f3e1035f5684ff4ada8446b523b30b5" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="256.55172413793105" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t052d150b71f34d44a2c5aa8a77d436ce" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:end"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:end" transform="rotate(-0.0, 256.55172413793105, 195.0)" x="256.55172413793105" y="195.0">Right Justified</text></g></g><g class="toyplot-mark-Plot" id="tecfe378fe98949ff8315a1896ff3c938" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="256.55172413793105" cy="195.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t2359eabd0ed44dc886fa18ce575c229b text");
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
          var text = document.querySelectorAll("#t2359eabd0ed44dc886fa18ce575c229b text");
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
    (function()
    {
      var data_tables = [{"data": [[0.0, 0.0], [-2.0, 2.0]], "names": ["x", "y0"], "id": "t1109ac3bd69b4687a1876574761a6f1f", "title": "Plot Data"}, {"data": [[0.0], [1.0]], "names": ["x", "y0"], "id": "t3fc2cd49b0a54f92818c706222ba6bdb", "title": "Plot Data"}, {"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "t5f3e1035f5684ff4ada8446b523b30b5", "title": "Plot Data"}, {"data": [[0.0], [-1.0]], "names": ["x", "y0"], "id": "tecfe378fe98949ff8315a1896ff3c938", "title": "Plot Data"}];
    
      function save_csv(data_table)
      {
        uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
          }
          uri += "\n";
        }
    
        uri = encodeURI(uri);
        window.open(uri);
      }
    
      function open_popup(data_table)
      {
        return function(e)
        {
          var popup = document.querySelector("#t2359eabd0ed44dc886fa18ce575c229b .toyplot-mark-popup");
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
    </script><script>
    (function()
    {
      var axes = {"t47eb24f3062e46e287fbfbf03dc20161": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.88421052631578956, "min": -0.94736842105263164}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": -2.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
      {
        return x < 0 ? -1 : x > 0 ? 1 : 0;
      }
    
      function log_n(x, base)
      {
        return Math.log(Math.abs(x)) / Math.log(base);
      }
    
      function mix(a, b, amount)
      {
        return ((1.0 - amount) * a) + (amount * b);
      }
    
      function to_domain(projection, range)
      {
        for(var i = 0; i != projection.length; ++i)
        {
          var segment = projection[i];
          if(Math.min(segment.range.bounds.min, segment.range.bounds.max) <= point[0] && point[0] < Math.max(segment.range.bounds.min, segment.range.bounds.max))
          {
            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              return mix(segment.domain.min, segment.domain.max, amount)
            }
            else if(segment.scale[0] == "log")
            {
              var base = segment.scale[1];
              return sign(segment.domain.min) * Math.pow(base, mix(log_n(Math.abs(segment.domain.min), base), log_n(Math.abs(segment.domain.max), base), amount));
            }
          }
        }
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
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
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
    
    axes.text(0, 1, "Shifted +0px", style={"-toyplot-anchor-shift":"0", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 1, color="black", size=7)
    
    axes.text(0, 0, "Shifted +20px", style={"-toyplot-anchor-shift":"20px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7)
    
    axes.text(0, -1, "Shifted +40px", style={"-toyplot-anchor-shift":"40px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black", size=7);
    
    axes.text(0, -2, "Shifted -20px", style={"-toyplot-anchor-shift":"-20px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, -2, color="black", size=7);




.. raw:: html

    <div align="center" class="toyplot" id="tae7e60bb966849dbad114f83ae1ce0ab"><svg height="300.0px" id="t9e3b5b5700e349369d9f1d6aeb647442" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t5d8d5ac6ab23444dbe65b6872efe6225"><clipPath id="t55b3428e0bfd46adac5607758d9eb869"><rect height="200.0" width="400.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t55b3428e0bfd46adac5607758d9eb869)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t1f7155e02f7f4d6d9d9e895a88085ca3" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 193.21033210332104 240.0 L 193.21033210332104 60.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t8d0a2e6b550544eeb5474c5a4759728f" style="-toyplot-anchor-shift:0;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="0" style="-toyplot-anchor-shift:0;alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 193.21033210332104, 95.999999999999986)" x="193.21033210332104" y="95.999999999999986">Shifted +0px</text></g></g><g class="toyplot-mark-Plot" id="t718fa62d151e42fd9727cb4f19c92a1a" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="193.21033210332104" cy="95.999999999999986" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t4841b0d2afee4f77bdd16a00ace49afe" style="-toyplot-anchor-shift:20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="20px" style="-toyplot-anchor-shift:20px;alignment-baseline:middle;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 193.21033210332104, 132.0)" x="193.21033210332104" y="132.0">Shifted +20px</text></g></g><g class="toyplot-mark-Plot" id="tecb942d118294b5bac7f3ed315e2ecfd" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="193.21033210332104" cy="132.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tfaf1cf5a5510483d8fc6bc25f492c645" style="-toyplot-anchor-shift:40px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="40px" style="-toyplot-anchor-shift:40px;alignment-baseline:middle;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 193.21033210332104, 168.0)" x="193.21033210332104" y="168.0">Shifted +40px</text></g></g><g class="toyplot-mark-Plot" id="tb86f80024b7a447a91d654ca8e8e2104" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="193.21033210332104" cy="168.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t7eac0c09daeb4ab5a31b9cc3b7596016" style="-toyplot-anchor-shift:-20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="-20px" style="-toyplot-anchor-shift:-20px;alignment-baseline:middle;fill:rgba(90.6%,54.1%,76.5%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 193.21033210332104, 204.0)" x="193.21033210332104" y="204.0">Shifted -20px</text></g></g><g class="toyplot-mark-Plot" id="t526a7ff5d84743bc9c62f583dab9c07d" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="193.21033210332104" cy="204.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tae7e60bb966849dbad114f83ae1ce0ab text");
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
          var text = document.querySelectorAll("#tae7e60bb966849dbad114f83ae1ce0ab text");
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
    (function()
    {
      var data_tables = [{"data": [[0.0, 0.0], [-3.0, 2.0]], "names": ["x", "y0"], "id": "t1f7155e02f7f4d6d9d9e895a88085ca3", "title": "Plot Data"}, {"data": [[0.0], [1.0]], "names": ["x", "y0"], "id": "t718fa62d151e42fd9727cb4f19c92a1a", "title": "Plot Data"}, {"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "tecb942d118294b5bac7f3ed315e2ecfd", "title": "Plot Data"}, {"data": [[0.0], [-1.0]], "names": ["x", "y0"], "id": "tb86f80024b7a447a91d654ca8e8e2104", "title": "Plot Data"}, {"data": [[0.0], [-2.0]], "names": ["x", "y0"], "id": "t526a7ff5d84743bc9c62f583dab9c07d", "title": "Plot Data"}];
    
      function save_csv(data_table)
      {
        uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
          }
          uri += "\n";
        }
    
        uri = encodeURI(uri);
        window.open(uri);
      }
    
      function open_popup(data_table)
      {
        return function(e)
        {
          var popup = document.querySelector("#tae7e60bb966849dbad114f83ae1ce0ab .toyplot-mark-popup");
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
    </script><script>
    (function()
    {
      var axes = {"t5d8d5ac6ab23444dbe65b6872efe6225": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.9263157894736842, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": -3.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
      {
        return x < 0 ? -1 : x > 0 ? 1 : 0;
      }
    
      function log_n(x, base)
      {
        return Math.log(Math.abs(x)) / Math.log(base);
      }
    
      function mix(a, b, amount)
      {
        return ((1.0 - amount) * a) + (amount * b);
      }
    
      function to_domain(projection, range)
      {
        for(var i = 0; i != projection.length; ++i)
        {
          var segment = projection[i];
          if(Math.min(segment.range.bounds.min, segment.range.bounds.max) <= point[0] && point[0] < Math.max(segment.range.bounds.min, segment.range.bounds.max))
          {
            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              return mix(segment.domain.min, segment.domain.max, amount)
            }
            else if(segment.scale[0] == "log")
            {
              var base = segment.scale[1];
              return sign(segment.domain.min) * Math.pow(base, mix(log_n(Math.abs(segment.domain.min), base), log_n(Math.abs(segment.domain.max), base), amount));
            }
          }
        }
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
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
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




.. raw:: html

    <div align="center" class="toyplot" id="tc82fbf7f67cf4257a61aa8b8861c8a78"><svg height="300.0px" id="tcba8999796714a9fa1837a3cdccb1ac0" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t5f062918a3664a0f93a047470e2584ce"><clipPath id="tcb821e3f8a1349b3b4207f34f2c0c5f3"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tcb821e3f8a1349b3b4207f34f2c0c5f3)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tef591067b50b4795b9f2d71befeffabf" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 60.0 150.0 L 540.0 150.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t7f26250482f94d10838b181b22d69e31" style="alignment-baseline:hanging;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:hanging;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 156.0, 150.0)" x="156.0" y="150.0">Hanging</text></g></g><g class="toyplot-mark-Plot" id="t96a06528997246acad17f336835d2ae7" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="156.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="te55bf2d5520c4e5ea27cb5e5a2b809ff" style="alignment-baseline:central;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:central;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 252.0, 150.0)" x="252.0" y="150.0">Central</text></g></g><g class="toyplot-mark-Plot" id="td3a47a8e51e543d18ed4b09712987428" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="252.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tcb2dc5b2547e44ad95d652b1fb9c4e23" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 348.0, 150.0)" x="348.0" y="150.0">Middle</text></g></g><g class="toyplot-mark-Plot" id="t545f2392a4da4cdfa07c754751365b3d" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="348.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t540297b6cceb4457b7e56d03e9dc7bfb" style="alignment-baseline:alphabetic;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:alphabetic;fill:rgba(90.6%,54.1%,76.5%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 444.0, 150.0)" x="444.0" y="150.0">Alpha</text></g></g><g class="toyplot-mark-Plot" id="t206ff69a29c54200aabd38b0771cfbaf" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="444.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tc82fbf7f67cf4257a61aa8b8861c8a78 text");
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
          var text = document.querySelectorAll("#tc82fbf7f67cf4257a61aa8b8861c8a78 text");
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
    (function()
    {
      var data_tables = [{"data": [[-2.0, 3.0], [0.0, 0.0]], "names": ["x", "y0"], "id": "tef591067b50b4795b9f2d71befeffabf", "title": "Plot Data"}, {"data": [[-1.0], [0.0]], "names": ["x", "y0"], "id": "t96a06528997246acad17f336835d2ae7", "title": "Plot Data"}, {"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "td3a47a8e51e543d18ed4b09712987428", "title": "Plot Data"}, {"data": [[1.0], [0.0]], "names": ["x", "y0"], "id": "t545f2392a4da4cdfa07c754751365b3d", "title": "Plot Data"}, {"data": [[2.0], [0.0]], "names": ["x", "y0"], "id": "t206ff69a29c54200aabd38b0771cfbaf", "title": "Plot Data"}];
    
      function save_csv(data_table)
      {
        uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
          }
          uri += "\n";
        }
    
        uri = encodeURI(uri);
        window.open(uri);
      }
    
      function open_popup(data_table)
      {
        return function(e)
        {
          var popup = document.querySelector("#tc82fbf7f67cf4257a61aa8b8861c8a78 .toyplot-mark-popup");
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
    </script><script>
    (function()
    {
      var axes = {"t5f062918a3664a0f93a047470e2584ce": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0, "min": -2.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
      {
        return x < 0 ? -1 : x > 0 ? 1 : 0;
      }
    
      function log_n(x, base)
      {
        return Math.log(Math.abs(x)) / Math.log(base);
      }
    
      function mix(a, b, amount)
      {
        return ((1.0 - amount) * a) + (amount * b);
      }
    
      function to_domain(projection, range)
      {
        for(var i = 0; i != projection.length; ++i)
        {
          var segment = projection[i];
          if(Math.min(segment.range.bounds.min, segment.range.bounds.max) <= point[0] && point[0] < Math.max(segment.range.bounds.min, segment.range.bounds.max))
          {
            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              return mix(segment.domain.min, segment.domain.max, amount)
            }
            else if(segment.scale[0] == "log")
            {
              var base = segment.scale[1];
              return sign(segment.domain.min) * Math.pow(base, mix(log_n(Math.abs(segment.domain.min), base), log_n(Math.abs(segment.domain.max), base), amount));
            }
          }
        }
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
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
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

    <div align="center" class="toyplot" id="t048437ac152f40d6a016e66344d6783a"><svg height="300.0px" id="tdcfd7cef49634ee294a16322ad81ad4f" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tbcdb7f94d2c148ccbb1d31776507b8af"><clipPath id="t396c5431732d4968a5c4be4ea7f83638"><rect height="200.0" width="600.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t396c5431732d4968a5c4be4ea7f83638)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="600.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t2b34d4a3991b4979bcc21949cda070a1" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 75.466666666666697 150.0 L 636.13333333333333 150.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="tbee9afe07136405d8d314e89150db281" style="alignment-baseline:middle;baseline-shift:-100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:-100%;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 187.60000000000002, 150.0)" x="187.60000000000002" y="150.0">Shift -100%</text></g></g><g class="toyplot-mark-Plot" id="t72148b397f6547769e39503f91be565b" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="187.60000000000002" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="td70a08dd96b94bcc9f7c17d77ead52f1" style="alignment-baseline:middle;baseline-shift:0;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:0;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 299.73333333333335, 150.0)" x="299.73333333333335" y="150.0">Shift 0%</text></g></g><g class="toyplot-mark-Plot" id="t7d293a448d26435abc94b4fc07a5a9cc" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="299.73333333333335" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t1cda709cb6534ad19a13c2461c936368" style="alignment-baseline:middle;baseline-shift:66%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:66%;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 411.86666666666667, 150.0)" x="411.86666666666667" y="150.0">Shift 66%</text></g></g><g class="toyplot-mark-Plot" id="t2430c231db564da797db73af01abbfeb" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="411.86666666666667" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tdb1f635dedf94011979006239ff7ecf5" style="alignment-baseline:middle;baseline-shift:100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:100%;fill:rgba(90.6%,54.1%,76.5%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 524.0, 150.0)" x="524.0" y="150.0">Shift 100%</text></g></g><g class="toyplot-mark-Plot" id="tae5d829077a442abbf8ceb2176718a3f" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="524.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t048437ac152f40d6a016e66344d6783a text");
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
          var text = document.querySelectorAll("#t048437ac152f40d6a016e66344d6783a text");
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
    (function()
    {
      var data_tables = [{"data": [[-2.0, 3.0], [0.0, 0.0]], "names": ["x", "y0"], "id": "t2b34d4a3991b4979bcc21949cda070a1", "title": "Plot Data"}, {"data": [[-1.0], [0.0]], "names": ["x", "y0"], "id": "t72148b397f6547769e39503f91be565b", "title": "Plot Data"}, {"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "t7d293a448d26435abc94b4fc07a5a9cc", "title": "Plot Data"}, {"data": [[1.0], [0.0]], "names": ["x", "y0"], "id": "t2430c231db564da797db73af01abbfeb", "title": "Plot Data"}, {"data": [[2.0], [0.0]], "names": ["x", "y0"], "id": "tae5d829077a442abbf8ceb2176718a3f", "title": "Plot Data"}];
    
      function save_csv(data_table)
      {
        uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
          }
          uri += "\n";
        }
    
        uri = encodeURI(uri);
        window.open(uri);
      }
    
      function open_popup(data_table)
      {
        return function(e)
        {
          var popup = document.querySelector("#t048437ac152f40d6a016e66344d6783a .toyplot-mark-popup");
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
    </script><script>
    (function()
    {
      var axes = {"tbcdb7f94d2c148ccbb1d31776507b8af": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0344827586206899, "min": -2.1379310344827589}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 640.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
      {
        return x < 0 ? -1 : x > 0 ? 1 : 0;
      }
    
      function log_n(x, base)
      {
        return Math.log(Math.abs(x)) / Math.log(base);
      }
    
      function mix(a, b, amount)
      {
        return ((1.0 - amount) * a) + (amount * b);
      }
    
      function to_domain(projection, range)
      {
        for(var i = 0; i != projection.length; ++i)
        {
          var segment = projection[i];
          if(Math.min(segment.range.bounds.min, segment.range.bounds.max) <= point[0] && point[0] < Math.max(segment.range.bounds.min, segment.range.bounds.max))
          {
            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
            if(segment.scale == "linear")
            {
              return mix(segment.domain.min, segment.domain.max, amount)
            }
            else if(segment.scale[0] == "log")
            {
              var base = segment.scale[1];
              return sign(segment.domain.min) * Math.pow(base, mix(log_n(Math.abs(segment.domain.min), base), log_n(Math.abs(segment.domain.max), base), amount));
            }
          }
        }
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
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


Of course, you're free to combine all four styles in any way that you
like.
