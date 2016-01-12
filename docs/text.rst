
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

    <div align="center" class="toyplot" id="t4c5646d4fcab41b4b5eaaeef1a007e90"><svg height="150.0px" id="tb6ac967b752341d99292b57915b8fb06" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 150.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t636255f30534474988ba127f89210ddf"><clipPath id="t9e0c27ce7f7b4fd38bd5ca97fd34243f"><rect height="70.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9e0c27ce7f7b4fd38bd5ca97fd34243f)" style="cursor:crosshair"><rect height="70.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Text" id="t03cfdfa6b47a405e8e8df6c1e9cc1050" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(250.0,75.0)"><tspan style="dominant-baseline:inherit">Text!</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t14bd1db5cb5648f99c927d00529cbaf9" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="75.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t14bd1db5cb5648f99c927d00529cbaf9", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t4c5646d4fcab41b4b5eaaeef1a007e90 .toyplot-mark-popup");
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
      var axes = {"t636255f30534474988ba127f89210ddf": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 100.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="tfd258553dee242e0971bf15b0319a551"><svg height="300.0px" id="td47af7f16c544ce7905e0f9284391c55" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tb37aab1455d3439c98926e575d5ab70e"><clipPath id="t4b29b46d0dfc47f1968ed40fed72c0c1"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t4b29b46d0dfc47f1968ed40fed72c0c1)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t63f94359752e471fb2f83d47b04af503" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 250.0 250.0 L 250.0 50.0" style="stroke:rgb(50.2%,50.2%,50.2%);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="tb439df2632354239a818bb343aebc5c5" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(250.0,100.0)"><tspan style="dominant-baseline:inherit">Centered</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t8e6850054efd441d9cdfa0c13f1e770a" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="100.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="tbe973ac047144b7ba3409851dc760caa" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(250.0,150.0)"><tspan style="dominant-baseline:inherit">Left Justified</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t700af3e4033541c388fc5069577a3bb3" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t061aea00381b48fc90effaa0746a794f" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:end"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:end" transform="translate(250.0,200.0)"><tspan style="dominant-baseline:inherit">Right Justified</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tf7d736347f434da1af498be86a23124b" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="200.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0.0, 0.0], [-2.0, 2.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t63f94359752e471fb2f83d47b04af503", "filename": "toyplot"}, {"data": [[0.0], [1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t8e6850054efd441d9cdfa0c13f1e770a", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t700af3e4033541c388fc5069577a3bb3", "filename": "toyplot"}, {"data": [[0.0], [-1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tf7d736347f434da1af498be86a23124b", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tfd258553dee242e0971bf15b0319a551 .toyplot-mark-popup");
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
      var axes = {"tb37aab1455d3439c98926e575d5ab70e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -1.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": -2.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t62d1f16d97d64d4a904bd9c3238222f6"><svg height="300.0px" id="t4bd6868507ab400796c5bb00e5159b75" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t53c681b9716d4acf9983c7506403362f"><clipPath id="t433e6c82f021432bb20937ab87ae7eed"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t433e6c82f021432bb20937ab87ae7eed)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="td491df0c6016413db4aa2157ec590fa0" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 183.33333333333334 250.0 L 183.33333333333334 50.0" style="stroke:rgb(50.2%,50.2%,50.2%);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="td732792ebd454ff7b31803097bb6be19" style="-toyplot-anchor-shift:0;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(183.33333333333334,89.999999999999986)"><tspan style="dominant-baseline:inherit">Shifted +0px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t8c1ed9352d0b4d8796cf51a35fb10e4b" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="183.33333333333334" cy="89.999999999999986" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="tecec05f1a66d4ce0a26f0c2ff36a0ada" style="-toyplot-anchor-shift:20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(203.33333333333334,130.0)"><tspan style="dominant-baseline:inherit">Shifted +20px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t4e4aec443d4440b89f5304853a8905a2" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="183.33333333333334" cy="130.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="tca89d919fcb54116bac03657df0333ad" style="-toyplot-anchor-shift:40px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(223.33333333333334,170.0)"><tspan style="dominant-baseline:inherit">Shifted +40px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tf0566caf2d5f4ee29ebd4c61944f01ae" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="183.33333333333334" cy="170.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t22f505eb179341a0b0451c0917560948" style="-toyplot-anchor-shift:-20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(163.33333333333334,210.0)"><tspan style="dominant-baseline:inherit">Shifted -20px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t88fbd799af464adb9441a8b94bf2d949" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="183.33333333333334" cy="210.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0.0, 0.0], [-3.0, 2.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "td491df0c6016413db4aa2157ec590fa0", "filename": "toyplot"}, {"data": [[0.0], [1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t8c1ed9352d0b4d8796cf51a35fb10e4b", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t4e4aec443d4440b89f5304853a8905a2", "filename": "toyplot"}, {"data": [[0.0], [-1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tf0566caf2d5f4ee29ebd4c61944f01ae", "filename": "toyplot"}, {"data": [[0.0], [-2.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t88fbd799af464adb9441a8b94bf2d949", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t62d1f16d97d64d4a904bd9c3238222f6 .toyplot-mark-popup");
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
      var axes = {"t53c681b9716d4acf9983c7506403362f": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": -3.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t8117fa4ed50240b68150cfd5a287201c"><svg height="300.0px" id="t2b5e4fd51db84d6486f08b6248617377" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t005cfc68fb5e4c649bb0e394d406e929"><clipPath id="tb08e0e4ecd764d6fb07e9275cde64c24"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb08e0e4ecd764d6fb07e9275cde64c24)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="520.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t037b00f8db1f452785fb60325fa306be" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 50.0 150.0 L 550.0 150.0" style="stroke:rgb(50.2%,50.2%,50.2%);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t0b55cc523b3240d1b515f9fd2b0089cb" style="alignment-baseline:hanging;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:hanging;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(150.0,150.0)"><tspan style="dominant-baseline:inherit">Hanging</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tfafd4a7be62846d28e07e5dd9022204e" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="150.0" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="tf8a87ee5578c454987bcba917351c3c8" style="alignment-baseline:central;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:central;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(250.0,150.0)"><tspan style="dominant-baseline:inherit">Central</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tadbc3ab46aa34968853ff9b2bad6b124" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t91e2abe7040c4dfaa0af17a8ec592ab9" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(350.0,150.0)"><tspan style="dominant-baseline:inherit">Middle</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tb7ad224bf2c1421d99dea15f555417bb" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="350.0" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="tdbf46c76f28247028bc73e6a09c53192" style="alignment-baseline:alphabetic;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:alphabetic;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(450.0,150.0)"><tspan style="dominant-baseline:inherit">Alpha</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t4a37bdd64f374d48bd3e141c9e730a56" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="450.0" cy="150.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-2.0, 3.0], [0.0, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t037b00f8db1f452785fb60325fa306be", "filename": "toyplot"}, {"data": [[-1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tfafd4a7be62846d28e07e5dd9022204e", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tadbc3ab46aa34968853ff9b2bad6b124", "filename": "toyplot"}, {"data": [[1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tb7ad224bf2c1421d99dea15f555417bb", "filename": "toyplot"}, {"data": [[2.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t4a37bdd64f374d48bd3e141c9e730a56", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t8117fa4ed50240b68150cfd5a287201c .toyplot-mark-popup");
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
      var axes = {"t005cfc68fb5e4c649bb0e394d406e929": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0, "min": -2.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t58edb32fe5ee47fe837e22c3edd768b4"><svg height="300.0px" id="t4605022448b843f4a0cdfce1433345ad" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 300.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td74c161d33b94010b895adc0846db18e"><clipPath id="tfe9d35e08fcd4f68a8dc1b1c769c51d7"><rect height="220.0" width="620.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tfe9d35e08fcd4f68a8dc1b1c769c51d7)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="620.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t0ed3a0ac42694023ba209108739cbf0c" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 61.764705882352949 150.0 L 650.0 150.0" style="stroke:rgb(50.2%,50.2%,50.2%);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="tc9b6d5e559b5478e8bd8c2c2ff09e553" style="alignment-baseline:middle;baseline-shift:-100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(179.41176470588238,150.0)translate(0,24.0)"><tspan style="dominant-baseline:inherit">Shift -100%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t570edbc4c15a42aeb7dac9c4f921fab1" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="179.41176470588238" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="tc2726167cd974061b392c22d99ecbfb2" style="alignment-baseline:middle;baseline-shift:0;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(297.05882352941182,150.0)"><tspan style="dominant-baseline:inherit">Shift 0%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t0477baf6c1cd47228fe7bff92a259fb5" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="297.05882352941182" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t4b0197605b3b488b86678644662d5dd9" style="alignment-baseline:middle;baseline-shift:66%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(414.70588235294122,150.0)translate(0,-15.84)"><tspan style="dominant-baseline:inherit">Shift 66%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t02d7e0a07daa412786e688b8e7f0b295" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="414.70588235294122" cy="150.0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Text" id="t5481d59276344e0990481c261c513897" style="alignment-baseline:middle;baseline-shift:100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(532.35294117647061,150.0)translate(0,-24.0)"><tspan style="dominant-baseline:inherit">Shift 100%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="ta9baf28e606746fbb3c82df0cb53b1ac" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="532.35294117647061" cy="150.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-2.0, 3.0], [0.0, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t0ed3a0ac42694023ba209108739cbf0c", "filename": "toyplot"}, {"data": [[-1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t570edbc4c15a42aeb7dac9c4f921fab1", "filename": "toyplot"}, {"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t0477baf6c1cd47228fe7bff92a259fb5", "filename": "toyplot"}, {"data": [[1.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t02d7e0a07daa412786e688b8e7f0b295", "filename": "toyplot"}, {"data": [[2.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "ta9baf28e606746fbb3c82df0cb53b1ac", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t58edb32fe5ee47fe837e22c3edd768b4 .toyplot-mark-popup");
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
      var axes = {"td74c161d33b94010b895adc0846db18e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0, "min": -2.1000000000000001}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 650.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t86c9fb58f55845e588081dfb4e827878"><svg height="150.0px" id="t188c3df42a9d421ca22d87fe9203753e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="tcc8758c314bc408fa7af494e80979c05" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">100</tspan><tspan dy="-9.6" style="dominant-baseline:inherit;font-size:22.4px">-53</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#t86c9fb58f55845e588081dfb4e827878 .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="t07f9cd92903e4dbf856563fcbe7f6730"><svg height="150.0px" id="t1663050caa984f248b6d1b23aadd0fcb" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t45583ad2ae2f497c9c92e2ef3db0eb63" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">H</tspan><tspan dy="6.4" style="dominant-baseline:inherit;font-size:22.4px">2</tspan><tspan dy="-6.4" style="dominant-baseline:inherit">O</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#t07f9cd92903e4dbf856563fcbe7f6730 .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="tfe4d6ed4433d4c45b6460f1e13b8fc3f"><svg height="150.0px" id="tc5901e5323b840c3a60a000c5c6094f9" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t53933894db8644959b061c4bf4ed87e7" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">W</tspan><tspan dy="-9.6" style="dominant-baseline:inherit;font-size:22.4px">X</tspan><tspan dy="4.48" style="dominant-baseline:inherit;font-size:15.68px">Y</tspan><tspan dy="-11.2" style="dominant-baseline:inherit;font-size:15.68px">Z</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#tfe4d6ed4433d4c45b6460f1e13b8fc3f .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="t80c25c995a05470b901ca8d2f887742d"><svg height="150.0px" id="tb63fa00f55f14d1ea43ce5635edf4082" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t3b842fa9696e40f386df2dcda84764f6" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">normal </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">bold</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-style:italic">italic</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">strong</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-style:italic">emphasis</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-size:19.2px">small</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-family:monospace">code</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#t80c25c995a05470b901ca8d2f887742d .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="t71972b39eba14aeb9733b3a4f7d4f670"><svg height="150.0px" id="tf81014338c1c444f882c27e3bc572b8f" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t6afe42f21bef414a9e6b63d14b51f835" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">foo </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">bar </tspan><tspan style="dominant-baseline:inherit;font-style:italic;font-weight:bold">baz </tspan><tspan style="dominant-baseline:inherit;font-family:monospace;font-style:italic;font-weight:bold">blah</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#t71972b39eba14aeb9733b3a4f7d4f670 .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="tf4ca2cb536f84344a14c2d55d5d1eb7d"><svg height="200.0px" id="t24b1bbf0865f4457a093dba1672c8397" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-mark-Text" id="t9eb6f827bc224676924cbab83be71dac" style="alignment-baseline:middle;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">0.567832</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(243, 128, 19)</tspan></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
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
          var popup = document.querySelector("#tf4ca2cb536f84344a14c2d55d5d1eb7d .toyplot-mark-popup");
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

