
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _text:

Text
====

Alignment
---------

By default, text in Toyplot is centered vertically and horizontally
around its *anchor*. To illustrate this, the following figures display
the anchor as a small black dot:

.. code:: python

    import toyplot
    
    canvas = toyplot.Canvas(width=500, height=150)
    axes = canvas.axes(show=False)
    axes.text(0, 0, "Text!", style={"font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3);



.. raw:: html

    <div align="center" class="toyplot" id="tce32a0e716bc4f35b5c17716fe9dd5f9"><svg height="150.0px" id="tcc000e18e57048df81e2d9e61bdde80b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 150.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t6fc029e69c48494fab340610dc13730d"><clipPath id="tbf74205aa9fd419ebd0a8dbef06e8c52"><rect height="70.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tbf74205aa9fd419ebd0a8dbef06e8c52)" style="cursor:crosshair"><rect height="70.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Text" id="t4c9f07fae01449bb95b99356f0ba2cce" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(250.0,75.0)"><tspan style="dominant-baseline:inherit">Text!</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t72c8c2430a8d42d1b9c07892d228ab1f" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="75.0" r="1.5"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t72c8c2430a8d42d1b9c07892d228ab1f", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tce32a0e716bc4f35b5c17716fe9dd5f9 .toyplot-mark-popup");
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
      var axes = {"t6fc029e69c48494fab340610dc13730d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 100.0}, "scale": "linear"}]}};
    
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


To control horizontal alignment, use the CSS ``text-anchor`` attribute
to change the position of the text along its baseline, relative to the
anchor:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes(show=False, ymin=-1.5, ymax=1.5)
    
    axes.vlines(0, color="lightgray")
    
    axes.text(0, 1, "Centered", style={"text-anchor":"middle", "font-size":"24px"})
    axes.scatterplot(0, 1, color="black", size=3)
    
    axes.text(0, 0, "Left Justified", style={"text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes.text(0, -1, "Right Justified", style={"text-anchor":"end", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black", size=3);



.. raw:: html

    <div align="center" class="toyplot" id="t0bf31b0b984845dc995e2d596e9f2fdb"><svg height="300.0px" id="tc807f9a0e6274c8781a29712bf5e7b72" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tdec49c91b53a4400a0a630be9760f21d"><clipPath id="tc8fb9df1ed2843d6891b408d26c7b152"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tc8fb9df1ed2843d6891b408d26c7b152)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-AxisLines" id="te7b04a6275b14536822bb962d5d483d4" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="256.89655172413791" x2="256.89655172413791" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="tb149f065b931400888b470aae6c6f79f" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(256.89655172413791,83.333333333333329)"><tspan style="dominant-baseline:inherit">Centered</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t89a12d18580547e8ad668ae1857f6bcc" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="256.89655172413791" cy="83.333333333333329" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tac525740b06c4e92b5daef4290f7be93" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(256.89655172413791,150.0)"><tspan style="dominant-baseline:inherit">Left Justified</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t78706abf850b4cf9a8a370cf69350611" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="256.89655172413791" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t0bcbe111342c43839d2f4a62ccca2a59" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:end"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:end" transform="translate(256.89655172413791,216.66666666666669)"><tspan style="dominant-baseline:inherit">Right Justified</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t225867fdcdcc4d099a837edf4e100691" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="256.89655172413791" cy="216.66666666666669" r="1.5"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0.0], [1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t89a12d18580547e8ad668ae1857f6bcc", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t78706abf850b4cf9a8a370cf69350611", "filename": "toyplot"}, {"data": [[0.0], [-1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t225867fdcdcc4d099a837edf4e100691", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t0bf31b0b984845dc995e2d596e9f2fdb .toyplot-mark-popup");
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
      var axes = {"tdec49c91b53a4400a0a630be9760f21d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.84000000000000008, "min": -0.89999999999999991}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.5, "min": -1.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


In addition, the text can be shifted along its baseline in arbitrary
amounts, using the ``-toyplot-anchor-shift`` attribute (note that this
is non-standard CSS, provided by Toyplot for symmetry with the standard
``baseline-shift`` attribute which we will explore below):

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes(show=False, ymin=-2.5, ymax=1.5)
    
    axes.vlines(0, color="lightgray")
    
    axes.text(0, 1, "Shifted +0px", style={"-toyplot-anchor-shift":"0", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 1, color="black", size=3)
    
    axes.text(0, 0, "Shifted +20px", style={"-toyplot-anchor-shift":"20px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes.text(0, -1, "Shifted +40px", style={"-toyplot-anchor-shift":"40px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black", size=3);
    
    axes.text(0, -2, "Shifted -20px", style={"-toyplot-anchor-shift":"-20px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, -2, color="black", size=3);




.. raw:: html

    <div align="center" class="toyplot" id="t38ec126659404f56ba2f8613ac3c1210"><svg height="300.0px" id="t8ff9a59a02dd4a84b9819a32caca9168" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tad13c97d35d946d1bcb00459da26b13c"><clipPath id="t969137e04bfd406f8cdc020368080cae"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t969137e04bfd406f8cdc020368080cae)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-AxisLines" id="t186c282403cf42c8a1ca1a83f6a4284a" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="194.92753623188409" x2="194.92753623188409" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t393ce5b6618644f6a6000eb38e86ce84" style="-toyplot-anchor-shift:0;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(194.92753623188409,75.0)"><tspan style="dominant-baseline:inherit">Shifted +0px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t7c6d887475e5496ea376f93fee96de45" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="194.92753623188409" cy="75.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t59b004836fff4e328539efeb4a1d4fb3" style="-toyplot-anchor-shift:20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(194.92753623188409,125.0)translate(20.0,0)"><tspan style="dominant-baseline:inherit">Shifted +20px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t44cb52e8b7df431886f9836269231798" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="194.92753623188409" cy="125.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t2dd8a9898deb49c0a244e07dd77c02e2" style="-toyplot-anchor-shift:40px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(194.92753623188409,175.0)translate(40.0,0)"><tspan style="dominant-baseline:inherit">Shifted +40px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t72aeaa29eea743b3adb9d051da8250af" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="194.92753623188409" cy="175.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tf2cc4cd643f9446faaa8754e3c899402" style="-toyplot-anchor-shift:-20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(194.92753623188409,225.0)translate(-20.0,0)"><tspan style="dominant-baseline:inherit">Shifted -20px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tc8a7d68369dd4b43ae35f61007ec316b" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="194.92753623188409" cy="225.0" r="1.5"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0.0], [1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t7c6d887475e5496ea376f93fee96de45", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t44cb52e8b7df431886f9836269231798", "filename": "toyplot"}, {"data": [[0.0], [-1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t72aeaa29eea743b3adb9d051da8250af", "filename": "toyplot"}, {"data": [[0.0], [-2.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tc8a7d68369dd4b43ae35f61007ec316b", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t38ec126659404f56ba2f8613ac3c1210 .toyplot-mark-popup");
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
      var axes = {"tad13c97d35d946d1bcb00459da26b13c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.87999999999999989, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.5, "min": -2.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Vertically, the text baseline always passes through its anchor point -
so to alter the vertical alongment of text, you change the baseline
using the CSS ``alignment-baseline`` attribute. Note that CSS typography
is a complex topic and there are many different types of baseline to
accomodate different writing modes and fonts. The following baselines
are the most useful for Western scripts. Note the subtle difference
between the "central" and "middle" baselines - the former centers
upper-case letters in Western scripts while the latter centers
lower-case letters, and is the Toyplot default:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes(show=False)
    
    axes.hlines(0, color="lightgray")
    
    axes.text(-1, 0, "Hanging", style={"alignment-baseline":"hanging", "font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=3)
    
    axes.text(0, 0, "Central", style={"alignment-baseline":"central", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes.text(1, 0, "Middle", style={"alignment-baseline":"middle", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black", size=3)
    
    axes.text(2, 0, "Alpha", style={"alignment-baseline":"alphabetic", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black", size=3);




.. raw:: html

    <div align="center" class="toyplot" id="t89bf660570664ea8a3d938c4ba190f89"><svg height="300.0px" id="t22188ff0abda44319717f9607845c71e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t068833c5f34c45ef97a6f4ec2b40e4d1"><clipPath id="t897d172b5bd34c03af70303b4dc28c26"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t897d172b5bd34c03af70303b4dc28c26)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="520.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-AxisLines" id="tc5066cf5d9eb42669b803c3c35374bdf" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="550.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t5bca9dad7e7941deab8f9c7455588ac2" style="alignment-baseline:hanging;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:hanging;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(115.21739130434783,150.0)"><tspan style="dominant-baseline:inherit">Hanging</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tb2dc540c280e4f3b8701a38fecb737d5" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="115.21739130434783" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tea1ff18094924a54ae839f4d650e499e" style="alignment-baseline:central;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:central;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(244.61697722567285,150.0)"><tspan style="dominant-baseline:inherit">Central</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tef48591e4539402289099ef1ad1ef0bb" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="244.61697722567285" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tbed97a9ac6014588876a60f0bb971c9e" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(374.0165631469979,150.0)"><tspan style="dominant-baseline:inherit">Middle</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tfeb439b7fe3c42ff9286acf00835ee05" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="374.0165631469979" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t6420cc688801445e8499523ec2ebf4d8" style="alignment-baseline:alphabetic;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:alphabetic;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(503.41614906832291,150.0)"><tspan style="dominant-baseline:inherit">Alpha</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t42f2891319004bbd8924c76b48abb57d" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="503.41614906832291" cy="150.0" r="1.5"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tb2dc540c280e4f3b8701a38fecb737d5", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tef48591e4539402289099ef1ad1ef0bb", "filename": "toyplot"}, {"data": [[1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tfeb439b7fe3c42ff9286acf00835ee05", "filename": "toyplot"}, {"data": [[2.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t42f2891319004bbd8924c76b48abb57d", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t89bf660570664ea8a3d938c4ba190f89 .toyplot-mark-popup");
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
      var axes = {"t068833c5f34c45ef97a6f4ec2b40e4d1": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.3600000000000003, "min": -1.504}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


As you might expect, you can also shift text perpendicular to its
baseline by arbitrary amounts, using ``baseline-shift``. While you are
free to use any of Toyplot's supported CSS length units for the shift,
percentages are especially useful, because they represent a distance
relative to the font height:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=300)
    axes = canvas.axes(show=False)
    
    axes.hlines(0, color="lightgray")
    
    axes.text(-1, 0, "Shift -100%", style={"baseline-shift":"-100%", "font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=3)
    
    axes.text(0, 0, "Shift 0%", style={"baseline-shift":"0", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes.text(1, 0, "Shift 66%", style={"baseline-shift":"66%", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black", size=3)
    
    axes.text(2, 0, "Shift 100%", style={"baseline-shift":"100%", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black", size=3);




.. raw:: html

    <div align="center" class="toyplot" id="t6e89c590a2f940609280844d4cbd1457"><svg height="300.0px" id="t6a680d07e28943fb962ad7a19243377b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 300.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="te32542fef2fe468db4113ffe5c37c48b"><clipPath id="t701c7eb2f7354d509feaf37d41a25b48"><rect height="220.0" width="620.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t701c7eb2f7354d509feaf37d41a25b48)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="620.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-AxisLines" id="te6143f9ce1d14bfaa3cf492862e8b7ef" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="650.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t5fd23de372df49878bf305da24e47425" style="alignment-baseline:middle;baseline-shift:-100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(142.95774647887322,150.0)translate(0,24.0)"><tspan style="dominant-baseline:inherit">Shift -100%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="ta07d86faccc94e96b33593419cf34cff" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="142.95774647887322" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t01f73b2cfc8d4b239d774aa0ab298138" style="alignment-baseline:middle;baseline-shift:0;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(283.80281690140845,150.0)"><tspan style="dominant-baseline:inherit">Shift 0%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tb4acf1ace1704ce4b0e2c682678e1dc8" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="283.80281690140845" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tb180689aa8144044a38bc8cb95e33e42" style="alignment-baseline:middle;baseline-shift:66%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(424.64788732394368,150.0)translate(0,-15.84)"><tspan style="dominant-baseline:inherit">Shift 66%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t1543d850ec924cc8a805e6aebce52173" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="424.64788732394368" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t06ee606d30684b27a58d07ca4ec3b8df" style="alignment-baseline:middle;baseline-shift:100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(565.49295774647896,150.0)translate(0,-24.0)"><tspan style="dominant-baseline:inherit">Shift 100%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t7fcdfb189921422c8abac95ed566e865" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="565.49295774647896" cy="150.0" r="1.5"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "ta07d86faccc94e96b33593419cf34cff", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tb4acf1ace1704ce4b0e2c682678e1dc8", "filename": "toyplot"}, {"data": [[1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t1543d850ec924cc8a805e6aebce52173", "filename": "toyplot"}, {"data": [[2.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t7fcdfb189921422c8abac95ed566e865", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t6e89c590a2f940609280844d4cbd1457 .toyplot-mark-popup");
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
      var axes = {"te32542fef2fe468db4113ffe5c37c48b": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.5999999999999996, "min": -1.6599999999999999}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 650.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

One final thing to keep in mind is that ``-toyplot-anchor-shift`` and
``baseline-shift`` move the text relative to its baseline, not the
canvas. This is important because it affects their behavior when text is
rotated. In the following example, look carefully and note that the text
with ``-toyplot-anchor-shift`` is shifted *along its rotated baseline*,
not simply moved left or right on the canvas. Similarly, the
``baseline-shift`` text is shifted *perpendicular to its rotated
baseline*, not merely up or down:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    
    axes = canvas.axes(grid=(1,3,0), xshow=False, yshow=False, label="default")
    axes.vlines(0, color="lightgray")
    axes.text(0, 0, "a + b", angle=45, style={"font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes = canvas.axes(grid=(1,3,1), xshow=False, yshow=False, label="-toyplot-anchor-shift")
    axes.vlines(0, color="lightgray")
    axes.text(0, 0, "a + b", angle=45, style={"-toyplot-anchor-shift":"20px", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes = canvas.axes(grid=(1,3,2), xshow=False, yshow=False, label="baseline-shift")
    axes.vlines(0, color="lightgray")
    axes.text(0, 0, "a + b", angle=45, style={"baseline-shift":"-20px", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3);




.. raw:: html

    <div align="center" class="toyplot" id="t111d5b131ce648369d35d45883c10aba"><svg height="300.0px" id="t85589ac7a33c48c1b54bdaa2d6562d78" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t8c4b6580710048198de2d884258836de"><clipPath id="ta70ebf9bf42f41d7b8ef524e6e62198c"><rect height="220.0" width="86.66666666666666" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta70ebf9bf42f41d7b8ef524e6e62198c)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="86.66666666666666" x="40.0" y="40.0"></rect><g class="toyplot-mark-AxisLines" id="t39c65d9961b4401688188b2a84fe0185" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="83.333333333333329" x2="83.333333333333329" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="ta382f4c08acd40ecafb80907e297c2a9" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(83.333333333333329,150.0)rotate(-45.0)"><tspan style="dominant-baseline:inherit">a + b</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t205730336d2c4dc086a59505b71aab2a" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="83.333333333333329" cy="150.0" r="1.5"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="16.666666666666657" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="61.66666666666666" y="67.0"></text></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(83.33333333333333,50.0)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">default</tspan></text></g><g class="toyplot-axes-Cartesian" id="te3df40451a574370ad22bcaca767529c"><clipPath id="t01c5e743c66f4321a0b50301b64b03d8"><rect height="220.0" width="86.66666666666666" x="206.66666666666666" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t01c5e743c66f4321a0b50301b64b03d8)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="86.66666666666666" x="206.66666666666666" y="40.0"></rect><g class="toyplot-mark-AxisLines" id="t6c8c556040d04320bc10200308945b53" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="240.7407407407407" x2="240.7407407407407" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t234ac3be8b2a4f2d89d1315d5d3d67a8" style="-toyplot-anchor-shift:20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(240.7407407407407,150.0)rotate(-45.0)translate(20.0,0)"><tspan style="dominant-baseline:inherit">a + b</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="ta0736f82ce0c420ab484f5a9fab7bde1" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="240.7407407407407" cy="150.0" r="1.5"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="183.33333333333331" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="228.33333333333331" y="67.0"></text></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(250.0,50.0)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">-toyplot-anchor-shift</tspan></text></g><g class="toyplot-axes-Cartesian" id="t84a37100434248b5a322926b48b08547"><clipPath id="t967c5592355b4ff888a7dab9fff7a7a7"><rect height="220.0" width="86.66666666666669" x="373.3333333333333" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t967c5592355b4ff888a7dab9fff7a7a7)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="86.66666666666669" x="373.3333333333333" y="40.0"></rect><g class="toyplot-mark-AxisLines" id="t38c4ecc4e6fd4af5afd49b301e86f817" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="407.40740740740739" x2="407.40740740740739" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t03741dea5c5341219cef881eb4d86b6c" style="alignment-baseline:middle;baseline-shift:-20px;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(407.40740740740739,150.0)rotate(-45.0)translate(0,20.0)"><tspan style="dominant-baseline:inherit">a + b</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tf75937a0cc194054ab9794240b97f086" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="407.40740740740739" cy="150.0" r="1.5"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(416.66666666666663,50.0)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">baseline-shift</tspan></text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t205730336d2c4dc086a59505b71aab2a", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "ta0736f82ce0c420ab484f5a9fab7bde1", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tf75937a0cc194054ab9794240b97f086", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t111d5b131ce648369d35d45883c10aba .toyplot-mark-popup");
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
      var axes = {"t84a37100434248b5a322926b48b08547": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.97580735803743512, "min": -0.55154328932550745}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 383.3333333333333}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "t8c4b6580710048198de2d884258836de": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.76367532368147151, "min": -0.76367532368147151}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 116.66666666666666, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "te3df40451a574370ad22bcaca767529c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.97580735803743623, "min": -0.55154328932550722}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 283.3333333333333, "min": 216.66666666666666}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Rich Text
---------

In addition to positioning text using styles, you can use (a limited
subset of) HTML markup to format your text. For example, you can create
text with superscripts and subscripts:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "100<sup>-53</sup>", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="tce0438bad8524b4e80bd599d405e2157"><svg height="150.0px" id="t7f9758092ced43e39a0abd003c6c9c71" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="tba9ce8e2f41f4fc38f690911308b496e" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">100</tspan><tspan dy="-9.6" style="dominant-baseline:inherit;font-size:22.4px">-53</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#tce0438bad8524b4e80bd599d405e2157 .toyplot-mark-popup");
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


.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "H<sub>2</sub>O", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="tcc4980afebf94a65ac9077e93a107e66"><svg height="150.0px" id="t210f4beb77f5493790ab2b31425870f8" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t76f430a08f654b2989bfa41b915d9bc2" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">H</tspan><tspan dy="6.4" style="dominant-baseline:inherit;font-size:22.4px">2</tspan><tspan dy="-6.4" style="dominant-baseline:inherit">O</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#tcc4980afebf94a65ac9077e93a107e66 .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="tb0eacd04ff934684a11e5c7edf74b48e"><svg height="150.0px" id="t2fd3054f798449bb90ede0b6619657b4" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t04cfa59aa12b4d928b0689f2df50e7af" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">W</tspan><tspan dy="-9.6" style="dominant-baseline:inherit;font-size:22.4px">X</tspan><tspan dy="4.48" style="dominant-baseline:inherit;font-size:15.68px">Y</tspan><tspan dy="-11.2" style="dominant-baseline:inherit;font-size:15.68px">Z</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#tb0eacd04ff934684a11e5c7edf74b48e .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="tb5c0109083ed4b23b4a3e1ad953180fa"><svg height="150.0px" id="td82a74d0bcfa42e69dfc7f5968107bea" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t420efa1f16834f99917886812c7f71f5" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">normal </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">bold</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-style:italic">italic</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">strong</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-style:italic">emphasis</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-size:19.2px">small</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-family:monospace">code</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#tb5c0109083ed4b23b4a3e1ad953180fa .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="t78db9cc873a94ffba712070b53a7b650"><svg height="150.0px" id="te65ee0f108954d75bc3a9e260373688a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t1f3e42fc06f14c08a081f42c9e1e446e" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">foo </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">bar </tspan><tspan style="dominant-baseline:inherit;font-style:italic;font-weight:bold">baz </tspan><tspan style="dominant-baseline:inherit;font-family:monospace;font-style:italic;font-weight:bold">blah</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#t78db9cc873a94ffba712070b53a7b650 .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="t6f19ff5eead34bb9a625d5f624f36bb6"><svg height="200.0px" id="t33373ad5fc134d868e3cd3d6b1ebd73a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="tab73021873b24691a32e8ce425cf1563" style="alignment-baseline:middle;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">0.567832</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(243, 128, 19)</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#t6f19ff5eead34bb9a625d5f624f36bb6 .toyplot-mark-popup");
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


Note that additional tags and style attributes currently aren't allowed
in rich-text. We expect that the set of tags and attributes will expand
in the future.

Keep in mind that you can use rich text formatting anywhere that text is
displayed, including table cells, axis labels and tick labels. You can
also use rich text in format strings for tick locators - as an example,
the :class:`toyplot.locator.Log` locator uses superscript tags to
format tick labels for :ref:`log-scales`.

Axes Text
---------

In addition to all the above, :ref:`cartesian-axes` and
:ref:`number-lines` provide additional parameters that affect text
layout and alignment.

First, tick labels have a parameter ``location`` that controls whether
they appear above or below an axis:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    
    numberline1 = canvas.numberline(grid=(2, 1, 0))
    numberline1.axis.ticks.labels.location="above"
    
    numberline2 = canvas.numberline(grid=(2, 1, 1))
    numberline2.axis.ticks.labels.location="below"



.. raw:: html

    <div align="center" class="toyplot" id="t6be1a8367d3246c7933c5f2d03c4bfc2"><svg height="200.0px" id="tb5480979173a47aaac644cf367e2b759" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="te0f7e53b95d24eaba0af55478110733e"><g class="toyplot-coordinate-events"></g><g class="toyplot-axes-Axis" id="t3ecdf869f023441dba9e11ec67bf60ab" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g></g><g class="toyplot-axes-NumberLine" id="t40e876809e3648009a3354f337b52136"><g class="toyplot-coordinate-events"></g><g class="toyplot-axes-Axis" id="t056c4bbb83f84d58977425083196f42b" transform="translate(50.0,150.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul></div></div>


Note that although the location can be specified explicitly, in most
cases the defaults should just work ... note how the location of the Y
axis labels automatically changes from "above" to "below" when the Y
axis spine is repositioned in the following example:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    
    axis1 = canvas.axes(grid=(1, 2, 0))
    
    axis2 = canvas.axes(grid=(1, 2, 1))
    axis2.y.spine.position="high"



.. raw:: html

    <div align="center" class="toyplot" id="t0248579aa2bb400fa30503e1adf61578"><svg height="300.0px" id="t755d9211b82d48efba4da0267296483c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t94b6accc2e214600b7266628866dd9af"><clipPath id="tcfac5d5df9d54e29b00e59b9d6d612a0"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tcfac5d5df9d54e29b00e59b9d6d612a0)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t6f472c837341496d8a279561f3c1226e" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t38f248be29e04355bad78a240a45a55b" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="tec2555a0eacc403ebbaab6982662c335"><clipPath id="ta349b1c99a3c42c5820d5783ae8858b4"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta349b1c99a3c42c5820d5783ae8858b4)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tcd86825f907b4e92a29db29949689f1c" transform="translate(350.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="tb7cecf04f4b847aca3a28be6be909472" transform="translate(550.0,250.0) rotate(-90.0) translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"t94b6accc2e214600b7266628866dd9af": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "tec2555a0eacc403ebbaab6982662c335": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


In addition to positioning tick labels above or below an axis, you can
also adjust their ``offset`` - the distance from the axis spine to the
text anchor. The ``offset`` parameter is specified so that increasing
values move text further from the axis, whether its location is above or
below - in the following example, note that both offsets are positive:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    
    axis1 = canvas.axes(grid=(1, 2, 0))
    axis1.y.ticks.labels.offset=30
    
    axis2 = canvas.axes(grid=(1, 2, 1))
    axis2.y.spine.position="high"
    axis2.y.ticks.labels.offset=30



.. raw:: html

    <div align="center" class="toyplot" id="td4ecec59d2b446e3bf7a950cd6a646a0"><svg height="300.0px" id="t06dfb8730c7e4e68a1f9c921592493a3" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t91861b375aee49b9b4c0e43063dd5b5b"><clipPath id="te4c85121dac241efbc8cf3f66559e1fb"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te4c85121dac241efbc8cf3f66559e1fb)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="ta6f28919de364bdd85b7084433bd0994" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t5ffaaed8b9b74e478a5a40a1359a0e9d" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-30.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-30.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-30.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t6566ef3fb46a454a956d897e2b576c8a"><clipPath id="tfc60c1a8321d4aefb57922f3e6a12681"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tfc60c1a8321d4aefb57922f3e6a12681)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="te4c48744ddcd40eab204730e5563ba48" transform="translate(350.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t56c7757c3a6c4dba98459dbd4f631d5b" transform="translate(550.0,250.0) rotate(-90.0) translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,30.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,30.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,30.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"t6566ef3fb46a454a956d897e2b576c8a": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "t91861b375aee49b9b4c0e43063dd5b5b": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


The default text alignment parameters have been carefully chosen to
provide good quality layout even if you change the label font size, and
regardless of label location:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=400)
    
    numberline1 = canvas.numberline(grid=(4, 1, 0))
    numberline1.axis.ticks.labels.location="above"
    
    numberline2 = canvas.numberline(grid=(4, 1, 1))
    numberline2.axis.ticks.labels.location="above"
    numberline2.axis.ticks.labels.style = {"font-size":"16px"}
    
    numberline3 = canvas.numberline(grid=(4, 1, 2))
    numberline3.axis.ticks.labels.location="below"
    
    numberline4 = canvas.numberline(grid=(4, 1, 3))
    numberline4.axis.ticks.labels.location="below"
    numberline4.axis.ticks.labels.style = {"font-size":"16px"}



.. raw:: html

    <div align="center" class="toyplot" id="tf23b6524d4f44ecc921629c80841950a"><svg height="400.0px" id="tf2627cd5e17f42489cc46d60df3b9e45" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 400.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="tb09cb1969f8242b7a9d077230e49e069"><g class="toyplot-coordinate-events"></g><g class="toyplot-axes-Axis" id="tbf44f9322a794e3baeb328ce9e5be2db" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g></g><g class="toyplot-axes-NumberLine" id="t332fbf7d319b467ab7ea6d3d6a873331"><g class="toyplot-coordinate-events"></g><g class="toyplot-axes-Axis" id="tf71a688edddb4bb9a7bf2fab79ea9518" transform="translate(50.0,150.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g></g><g class="toyplot-axes-NumberLine" id="t5fc2621411f14c2285d52d0f3f626574"><g class="toyplot-coordinate-events"></g><g class="toyplot-axes-Axis" id="tbe172b7b33714abcb2160ca4a7c14ed0" transform="translate(50.0,250.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g></g><g class="toyplot-axes-NumberLine" id="tea3c33f431bc4f7f8be3e7774003e7a1"><g class="toyplot-coordinate-events"></g><g class="toyplot-axes-Axis" id="t5ef6cba7744f4caf85c6933812850974" transform="translate(50.0,350.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul></div></div>


Similarly, alignment parameters are automatically adjusted when you
rotate tick labels, adjusting the anchor and baseline to provide good
results:

.. code:: python

    import numpy
    
    colormap = toyplot.color.brewer.map("BlueRed", domain_min=0, domain_max=1)
    
    canvas = toyplot.Canvas()
    numberline = canvas.color_scale(x1="50%", x2="50%", y1="-10%", y2="10%", colormap=colormap)
    numberline.axis.ticks.show = True
    numberline.axis.ticks.labels.angle=-90



.. raw:: html

    <div align="center" class="toyplot" id="t15473e7771f04aabb42548657d730520"><svg height="600px" id="t29d38d8d6ef8448997065462fe3cca00" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t3997143f9724464a9c48b9d78ee2521e"><g class="toyplot-coordinate-events"><g class="toyplot-color-Map" id="ta8f96173fcfc4bd781ef2ad8b89cb173" transform="translate(300.0,540.0) rotate(-90.0) translate(0,-0.0)"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t77433de9ea5c4e4c9835589f31580dd2" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t77433de9ea5c4e4c9835589f31580dd2);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-axes-Axis" id="t86acac8dc99f489ca45e8100e190c254" transform="translate(300.0,540.0) rotate(-90.0) translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="-3" y2="3"></line><line style="" x1="240.0" x2="240.0" y1="-3" y2="3"></line><line style="" x1="480.0" x2="480.0" y1="-3" y2="3"></line></g><g><text style="dominant-baseline:central;font-size:10px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(0.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:central;font-size:10px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(240.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:central;font-size:10px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(480.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul></div></div>


Of-course, you are free to override any of these behaviors. For example,
suppose we use rich text to add multi-line tick labels to the preceding
example:

.. code:: python

    def format_color(color):
        return "(%.2f, %.2f, %.2f)" % (color["r"], color["g"], color["b"])
    
    values = numpy.linspace(colormap.domain.min, colormap.domain.max, 4)
    labels = ["%.4f<br><small>%s</small>" % (value, format_color(colormap.color(value))) for value in values]
    locator = toyplot.locator.Explicit(values, labels)

.. code:: python

    canvas = toyplot.Canvas()
    numberline = canvas.color_scale(x1="50%", x2="50%", y1="-10%", y2="10%", colormap=colormap)
    numberline.axis.ticks.show = True
    numberline.axis.ticks.labels.angle=-90
    
    numberline.axis.ticks.locator = locator
    numberline.axis.ticks.labels.style = {"font-size":"16px"}



.. raw:: html

    <div align="center" class="toyplot" id="tc11e4e13ee684bf5b17e47bf4df7fb19"><svg height="600px" id="t5b0253b3298045a28a3aa32f31bedd42" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t99f2f4f33e784f48ae5dd45e8aa1522b"><g class="toyplot-coordinate-events"><g class="toyplot-color-Map" id="tdafbac6f0f2e433492ab34a0e849b6b4" transform="translate(300.0,540.0) rotate(-90.0) translate(0,-0.0)"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t8dc6e890be424a7a8091f9b04fe6e9fd" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t8dc6e890be424a7a8091f9b04fe6e9fd);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-axes-Axis" id="tf27a0db9b8d541e39b099bace971963b" transform="translate(300.0,540.0) rotate(-90.0) translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="-3" y2="3"></line><line style="" x1="160.0" x2="160.0" y1="-3" y2="3"></line><line style="" x1="320.0" x2="320.0" y1="-3" y2="3"></line><line style="" x1="480.0" x2="480.0" y1="-3" y2="3"></line></g><g><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(0.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">0.0000</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.02, 0.19, 0.38)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(160.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">0.3333</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.65, 0.81, 0.89)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(320.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">0.6667</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.97, 0.72, 0.60)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(480.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">1.0000</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.40, 0.00, 0.12)</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul></div></div>


We might choose to center the labels horizontally and vertically,
overriding the defaults:

.. code:: python

    canvas = toyplot.Canvas()
    numberline = canvas.color_scale(x1="50%", x2="50%", y1="-10%", y2="10%", colormap=colormap)
    numberline.axis.ticks.labels.angle=-90
    numberline.axis.ticks.show = True
    numberline.axis.ticks.locator = locator
    numberline.axis.ticks.labels.style = {"font-size":"16px"}
    
    numberline.axis.ticks.labels.style = {"baseline-shift":"10px"}
    numberline.axis.ticks.labels.style = {"text-anchor":"middle"}
    numberline.axis.ticks.labels.offset = 60



.. raw:: html

    <div align="center" class="toyplot" id="t29a35c6dbf78424eb00cd28a449a7e8f"><svg height="600px" id="t3788bf62252c40f1bd1b050dd3d82c82" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="tf5528a135dc340c6beabfb6d55f83c40"><g class="toyplot-coordinate-events"><g class="toyplot-color-Map" id="tb662ef1e238a46f0a39f6526e676c4e3" transform="translate(300.0,540.0) rotate(-90.0) translate(0,-0.0)"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t07b66f4ee4364363bf55f3899397146b" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t07b66f4ee4364363bf55f3899397146b);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-axes-Axis" id="t74a3b252e83d443ea879521602c6661b" transform="translate(300.0,540.0) rotate(-90.0) translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="-3" y2="3"></line><line style="" x1="160.0" x2="160.0" y1="-3" y2="3"></line><line style="" x1="320.0" x2="320.0" y1="-3" y2="3"></line><line style="" x1="480.0" x2="480.0" y1="-3" y2="3"></line></g><g><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,60.0)rotate(90)translate(0,-10.0)"><tspan style="dominant-baseline:inherit">0.0000</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.02, 0.19, 0.38)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.0,60.0)rotate(90)translate(0,-10.0)"><tspan style="dominant-baseline:inherit">0.3333</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.65, 0.81, 0.89)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(320.0,60.0)rotate(90)translate(0,-10.0)"><tspan style="dominant-baseline:inherit">0.6667</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.97, 0.72, 0.60)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(480.0,60.0)rotate(90)translate(0,-10.0)"><tspan style="dominant-baseline:inherit">1.0000</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.40, 0.00, 0.12)</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul></div></div>

