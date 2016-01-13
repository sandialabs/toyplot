
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _text:

Text
====

Alignment
---------

By default, text in Toyplot is centered vertically and horizontally on
its coordinates. For example, in the following figure we rendered some
text, then plotted its coordinates using a black dot:

.. code:: python

    import toyplot
    
    canvas = toyplot.Canvas(width=500, height=150)
    axes = canvas.axes(show=False)
    axes.text(0, 0, "Text!", style={"font-size":"24px"})
    axes.scatterplot(0, 0, color="black");



.. raw:: html

    <div align="center" class="toyplot" id="t6c01187d60914d2d9e7a669865a68314"><svg height="150.0px" id="tf888eda8a6a6496cbc2f62e0a70d02f7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 150.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t271fd87cc7f44e449315e5ec54a7153a"><clipPath id="t31aaac3e2e674e73a982cf8100485f93"><rect height="70.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t31aaac3e2e674e73a982cf8100485f93)" style="cursor:crosshair"><rect height="70.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Text" id="t44de2f8e8ce143d0aa2d2abb2e6a8f8f" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(250.0,75.0)"><tspan style="dominant-baseline:inherit">Text!</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t747e96818d404d979870360e5ebf8f92" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="75.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t747e96818d404d979870360e5ebf8f92", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#t6c01187d60914d2d9e7a669865a68314 .toyplot-mark-popup");
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
      var axes = {"t271fd87cc7f44e449315e5ec54a7153a": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 100.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
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
    axes.scatterplot(0, 1, color="black")
    
    axes.text(0, 0, "Left Justified", style={"text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black")
    
    axes.text(0, -1, "Right Justified", style={"text-anchor":"end", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black");



.. raw:: html

    <div align="center" class="toyplot" id="t93c599cc18194385a366f6a828983c77"><svg height="300.0px" id="te040caf625bd42769da62bc2e71d3cf8" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t048e4d1b4dd247f0960cd5a9d5760274"><clipPath id="t4c5f675942694dfc801eafd246ab52a0"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t4c5f675942694dfc801eafd246ab52a0)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t99f8bf79cca641c68b100d5533cdeeef" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 250.0 250.0 L 250.0 50.0" style="stroke:rgb(50.2%,50.2%,50.2%);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t1ac5e5d5915b4040bc219c9e0c017ae3" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(250.0,100.0)"><tspan style="dominant-baseline:inherit">Centered</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="ta3a2f4e069b04ea5a6541579e5a41fcc" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="100.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="tc06401d45beb44c290de33ff0ed54f7b" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(250.0,150.0)"><tspan style="dominant-baseline:inherit">Left Justified</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tc6e9302efbfb4c8fab40f59c883b0585" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t5a2092e401a048f2a3f20091bc034078" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:end"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:end" transform="translate(250.0,200.0)"><tspan style="dominant-baseline:inherit">Right Justified</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t5fe6ade81c9f43ea841c1a346b3a490d" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="200.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0.0, 0.0], [-2.0, 2.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t99f8bf79cca641c68b100d5533cdeeef", "filename": "toyplot"}, {"data": [[0.0], [1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "ta3a2f4e069b04ea5a6541579e5a41fcc", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tc6e9302efbfb4c8fab40f59c883b0585", "filename": "toyplot"}, {"data": [[0.0], [-1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t5fe6ade81c9f43ea841c1a346b3a490d", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#t93c599cc18194385a366f6a828983c77 .toyplot-mark-popup");
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
      var axes = {"t048e4d1b4dd247f0960cd5a9d5760274": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -1.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": -2.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
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
    axes.scatterplot(0, 1, color="black")
    
    axes.text(0, 0, "Shifted +20px", style={"-toyplot-anchor-shift":"20px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black")
    
    axes.text(0, -1, "Shifted +40px", style={"-toyplot-anchor-shift":"40px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black");
    
    axes.text(0, -2, "Shifted -20px", style={"-toyplot-anchor-shift":"-20px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, -2, color="black");




.. raw:: html

    <div align="center" class="toyplot" id="tbb6e26d13bc04b9eac90efbd53894200"><svg height="300.0px" id="t96eea53ad3a04740bed9473e0708d711" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tfebbe05421474933a66830dda692bd22"><clipPath id="t2140ea4a22674008b01092efce508737"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2140ea4a22674008b01092efce508737)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t89168dc8107f403897107f6e4e259dcd" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 183.33333333333334 250.0 L 183.33333333333334 50.0" style="stroke:rgb(50.2%,50.2%,50.2%);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="tb7d979e45f7b4b9abf4bf473f7e0c44c" style="-toyplot-anchor-shift:0;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(183.33333333333334,89.999999999999986)"><tspan style="dominant-baseline:inherit">Shifted +0px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="te717726a112348febe8a377a88891dba" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="183.33333333333334" cy="89.999999999999986" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="td6c84f99e7774607bdde596c1fdd9370" style="-toyplot-anchor-shift:20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(203.33333333333334,130.0)"><tspan style="dominant-baseline:inherit">Shifted +20px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t399492986d6d408096579c0d17cfef8b" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="183.33333333333334" cy="130.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t1004305a81a94f7b81316b2a32b28f39" style="-toyplot-anchor-shift:40px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(223.33333333333334,170.0)"><tspan style="dominant-baseline:inherit">Shifted +40px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t607244a368c4418580f1176ed88d8dd0" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="183.33333333333334" cy="170.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="teb6730086fa74bf98c79690045d59348" style="-toyplot-anchor-shift:-20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(163.33333333333334,210.0)"><tspan style="dominant-baseline:inherit">Shifted -20px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t02581db12b3249d4a98b07d209adf30a" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="183.33333333333334" cy="210.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0.0, 0.0], [-3.0, 2.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t89168dc8107f403897107f6e4e259dcd", "filename": "toyplot"}, {"data": [[0.0], [1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "te717726a112348febe8a377a88891dba", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t399492986d6d408096579c0d17cfef8b", "filename": "toyplot"}, {"data": [[0.0], [-1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t607244a368c4418580f1176ed88d8dd0", "filename": "toyplot"}, {"data": [[0.0], [-2.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t02581db12b3249d4a98b07d209adf30a", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#tbb6e26d13bc04b9eac90efbd53894200 .toyplot-mark-popup");
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
      var axes = {"tfebbe05421474933a66830dda692bd22": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": -3.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
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
    axes.scatterplot(-1, 0, color="black")
    
    axes.text(0, 0, "Central", style={"alignment-baseline":"central", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black")
    
    axes.text(1, 0, "Middle", style={"alignment-baseline":"middle", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black")
    
    axes.text(2, 0, "Alpha", style={"alignment-baseline":"alphabetic", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black");




.. raw:: html

    <div align="center" class="toyplot" id="ta87ad3e036b940b7aa77fea901e0381e"><svg height="300.0px" id="t2d5d33813d3f4e84a00fe571d277135c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tb38fae50182c47fc8a0b57337dd6192b"><clipPath id="tebe19f781a104184881ef5814caa2dbd"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tebe19f781a104184881ef5814caa2dbd)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="520.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t972647f92a7b4c21a7dc3fa51d104386" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 50.0 150.0 L 550.0 150.0" style="stroke:rgb(50.2%,50.2%,50.2%);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t3933671d0669447988fd30560d48d181" style="alignment-baseline:hanging;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:hanging;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(150.0,150.0)"><tspan style="dominant-baseline:inherit">Hanging</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t94b1d408d975414eb7bb01c416a481bd" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="150.0" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t81358e4ef14543408edacb5c2a1d7f00" style="alignment-baseline:central;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:central;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(250.0,150.0)"><tspan style="dominant-baseline:inherit">Central</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tae4dc7b385174c728903ba752de80dd7" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t78a6be9f836f46e3b72c22fdd72359b3" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(350.0,150.0)"><tspan style="dominant-baseline:inherit">Middle</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t46b19f05f833457ca38a502d92b7a518" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="350.0" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t5604a15cd900411199d39c5d17ca8568" style="alignment-baseline:alphabetic;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:alphabetic;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(450.0,150.0)"><tspan style="dominant-baseline:inherit">Alpha</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tb0e493c22eba4394a5572d7f69687f28" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="450.0" cy="150.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-2.0, 3.0], [0.0, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t972647f92a7b4c21a7dc3fa51d104386", "filename": "toyplot"}, {"data": [[-1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t94b1d408d975414eb7bb01c416a481bd", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tae4dc7b385174c728903ba752de80dd7", "filename": "toyplot"}, {"data": [[1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t46b19f05f833457ca38a502d92b7a518", "filename": "toyplot"}, {"data": [[2.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tb0e493c22eba4394a5572d7f69687f28", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#ta87ad3e036b940b7aa77fea901e0381e .toyplot-mark-popup");
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
      var axes = {"tb38fae50182c47fc8a0b57337dd6192b": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0, "min": -2.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
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
    axes.scatterplot(-1, 0, color="black")
    
    axes.text(0, 0, "Shift 0%", style={"baseline-shift":"0", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black")
    
    axes.text(1, 0, "Shift 66%", style={"baseline-shift":"66%", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black");
    
    axes.text(2, 0, "Shift 100%", style={"baseline-shift":"100%", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black");




.. raw:: html

    <div align="center" class="toyplot" id="t7eb5259bbe5344bea75fd83262664b27"><svg height="300.0px" id="t13fff4d00d1746c9a0b814a756ffa70d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 300.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td1cd2ae3983a4165bae4dc3610191759"><clipPath id="taa46b87682a14807afa4a8d698820966"><rect height="220.0" width="620.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#taa46b87682a14807afa4a8d698820966)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="620.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t01d0725171124dc0afc38bac5a7d5c57" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 61.764705882352949 150.0 L 650.0 150.0" style="stroke:rgb(50.2%,50.2%,50.2%);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t48c5222dea7c41fab3d69f2079cffc2d" style="alignment-baseline:middle;baseline-shift:-100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(179.41176470588238,150.0)translate(0,24.0)"><tspan style="dominant-baseline:inherit">Shift -100%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t0ffb573554ab4f748e2c6e04e1c0ef4f" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="179.41176470588238" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t5dbd7a7a9f7d4df9abcc60d98e8ab530" style="alignment-baseline:middle;baseline-shift:0;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(297.05882352941182,150.0)"><tspan style="dominant-baseline:inherit">Shift 0%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t8d00addcd6654d368374a223c8e414f9" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="297.05882352941182" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t0c5dbe9d0d0a47a6b9dc6ef76d5cf300" style="alignment-baseline:middle;baseline-shift:66%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(414.70588235294122,150.0)translate(0,-15.84)"><tspan style="dominant-baseline:inherit">Shift 66%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t597851068f10419dad5f7b7164b5deae" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="414.70588235294122" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t5b33875c132b4d128176092e6bc1554f" style="alignment-baseline:middle;baseline-shift:100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(532.35294117647061,150.0)translate(0,-24.0)"><tspan style="dominant-baseline:inherit">Shift 100%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t8eb2fa0def504f4488eb59a9217da1aa" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="532.35294117647061" cy="150.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-2.0, 3.0], [0.0, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t01d0725171124dc0afc38bac5a7d5c57", "filename": "toyplot"}, {"data": [[-1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t0ffb573554ab4f748e2c6e04e1c0ef4f", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t8d00addcd6654d368374a223c8e414f9", "filename": "toyplot"}, {"data": [[1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t597851068f10419dad5f7b7164b5deae", "filename": "toyplot"}, {"data": [[2.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t8eb2fa0def504f4488eb59a9217da1aa", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#t7eb5259bbe5344bea75fd83262664b27 .toyplot-mark-popup");
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
      var axes = {"td1cd2ae3983a4165bae4dc3610191759": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0, "min": -2.1000000000000001}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 650.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
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

Rich Text
---------

In addition to positioning text using styles, you can use (a limited
subset of) HTML markup to format your text. For example, you can create
text with superscripts and subscripts:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "100<sup>-53</sup>", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="ted7a2a2bef4642f8b0cc88b30e03c0d0"><svg height="150.0px" id="t305450dc402b478286d98ec7a7ce8bf4" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="tc967a3553420483cb7ea9c99aa13b43c" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">100</tspan><tspan dy="-9.6" style="dominant-baseline:inherit;font-size:22.4px">-53</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#ted7a2a2bef4642f8b0cc88b30e03c0d0 .toyplot-mark-popup");
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
    </script></div></div>


Note that you can use rich text formatting anywhere that text is
displayed, including tick labels ... for example,
:class:`toyplot.locator.Log` uses superscripts to format tick labels
for logarithmic scales.

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "H<sub>2</sub>O", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="t8d7723b0fb1045529fb7a272beef0b40"><svg height="150.0px" id="t201057d57aea42759691ce0bc72a7128" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="tcf458bbd9808429aadc9bedce5969e61" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">H</tspan><tspan dy="6.4" style="dominant-baseline:inherit;font-size:22.4px">2</tspan><tspan dy="-6.4" style="dominant-baseline:inherit">O</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#t8d7723b0fb1045529fb7a272beef0b40 .toyplot-mark-popup");
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
    </script></div></div>


Note that you are free to nest superscripts and subscripts:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "W<sup>X<sub>Y</sub><sup>Z</sup></sup>", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="t7279208155bb4987be51155d13036e0a"><svg height="150.0px" id="t65c0772921664fdda2e2fa36984afdf6" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t0e6554ba8df34e4abee7f58006bb0cf5" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">W</tspan><tspan dy="-9.6" style="dominant-baseline:inherit;font-size:22.4px">X</tspan><tspan dy="4.48" style="dominant-baseline:inherit;font-size:15.68px">Y</tspan><tspan dy="-11.2" style="dominant-baseline:inherit;font-size:15.68px">Z</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#t7279208155bb4987be51155d13036e0a .toyplot-mark-popup");
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
    </script></div></div>


There are a variety of tags to alter the inline appearance of text:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(
        300,
        100,
        "normal <b>bold</b> <i>italic</i> <strong>strong</strong> <em>emphasis</em> <small>small</small> <code>code</code>",
        style={"font-size":"24px"});



.. raw:: html

    <div align="center" class="toyplot" id="t89fd5c2ae4f445e1ad3817c127f9204a"><svg height="150.0px" id="tfa33b5227a31402d9e6338c8d731ced0" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t191603c470124218a6e6fc4017203e0a" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">normal </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">bold</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-style:italic">italic</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">strong</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-style:italic">emphasis</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-size:19.2px">small</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-family:monospace">code</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#t89fd5c2ae4f445e1ad3817c127f9204a .toyplot-mark-popup");
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
    </script></div></div>


And these tags can be nested as well:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "foo <b>bar <i>baz <code>blah</code></i></b>", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="t552442eccc994db7961086ca0fa1b65d"><svg height="150.0px" id="t3618223cc3e647b39739d6e1b729feeb" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t87f7125caf774be6938e79b42bac77d7" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">foo </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">bar </tspan><tspan style="dominant-baseline:inherit;font-style:italic;font-weight:bold">baz </tspan><tspan style="dominant-baseline:inherit;font-family:monospace;font-style:italic;font-weight:bold">blah</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#t552442eccc994db7961086ca0fa1b65d .toyplot-mark-popup");
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
    </script></div></div>


Finally, you can insert line breaks into your text using the <br> tag:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    canvas.text(300, 100, "0.567832<br><small>(243, 128, 19)</small>", style={"font-size":"16px"});



.. raw:: html

    <div align="center" class="toyplot" id="t5aa2e236b2854e9cbae68dd298714132"><svg height="200.0px" id="t0ac1f3baa03d44f8818e319781130ef6" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t0b66adcf741e4e3ab1e6802d7629a837" style="alignment-baseline:middle;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">0.567832</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(243, 128, 19)</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
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
          var popup = document.querySelector("#t5aa2e236b2854e9cbae68dd298714132 .toyplot-mark-popup");
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
    </script></div></div>


Note that additional style attributes currently aren't allowed in
rich-text, although this may change in the future.

