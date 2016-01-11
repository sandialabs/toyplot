
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _convenience-api:

Convenience API
===============

With Toyplot, a figure always consists of three parts:

-  A :py:class:`canvas <toyplot.canvas.Canvas>`
-  One or more sets of :py:mod:`axes <toyplot.axes>` added to the
   canvas.
-  One or more :py:mod:`marks <toyplot.mark>` added to the axes.

Creating these entities separately gives you the maximum flexibility,
allowing you to add multiple axes (even overlapping axes) to one canvas,
splitting the marks among the different axes, etc. However for simple
figures containing a single set of axes and a single mark, this way of
working can be tedious. Toyplot's convenience API combines the three
calls to create canvas, axes, and mark into a single function that can
handle many of your plotting needs with a minimum of code.

Consider the following verbose example:

.. code:: python

    import numpy
    y = numpy.linspace(0, 1, 20) ** 2

.. code:: python

    import toyplot
    canvas = toyplot.Canvas(width=300)
    axes = canvas.axes()
    axes.plot(y);



.. raw:: html

    <div align="center" class="toyplot" id="tf74abbd012cc492790271fc610ae32a1"><svg height="300.0px" id="t626131739fdb4ba999b28689b7531680" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t0949f104afd54f439a971803c782880e"><clipPath id="tc0e9ef21996d410da86a146621a2eb42"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tc0e9ef21996d410da86a146621a2eb42)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tf3ec999e43fd4a9caaff0051367ba1a8" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t3f35bb589d04446b906cf43a56ebabb2" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t761836cc03124faab765be86422d7a57" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tf3ec999e43fd4a9caaff0051367ba1a8", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tf74abbd012cc492790271fc610ae32a1 .toyplot-mark-popup");
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
      var axes = {"t0949f104afd54f439a971803c782880e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Using the convenience API, it can be reduced to a single call to
:py:func:`toyplot.plot`:

.. code:: python

    canvas, axes, mark = toyplot.plot(y, width=300)



.. raw:: html

    <div align="center" class="toyplot" id="t27a2fb1ce4ef454dbf2952255d019287"><svg height="300.0px" id="te5c01b3c4ad14ae09c1164db1f58c783" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t26a097097cbc4aa297f6a191bae9d4ad"><clipPath id="t1d3f643271e049489eac95b331b6f37f"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t1d3f643271e049489eac95b331b6f37f)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tcdbeac02aee846b9b2026e834f77ebd6" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="td115bea5268a46bcad5c91cf36766809" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tee151dfd9e034e7880a035f264727598" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tcdbeac02aee846b9b2026e834f77ebd6", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t27a2fb1ce4ef454dbf2952255d019287 .toyplot-mark-popup");
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
      var axes = {"t26a097097cbc4aa297f6a191bae9d4ad": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Of course, if you're using the convenience API there's a good chance you
don't need the function's return value (a (canvas, axes, mark) tuple) at
all, making it even more compact:

.. code:: python

    toyplot.plot(y, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t5e02072a9a3342c9b8b720ad5882ba50"><svg height="300.0px" id="t5bfbea8af29440289f01b83995e2714b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t0a16876f4dbc4e03a957ecdff32a3fc9"><clipPath id="ta5be78584e224c1da408b8bdbfcbfcf3"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta5be78584e224c1da408b8bdbfcbfcf3)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tc423cca9dce84c14accd45dc0b99b164" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t7b52e29ee48e41cab91e087dd12733f0" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tf481f0a2b85144e9bcd3f4d122d7141c" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tc423cca9dce84c14accd45dc0b99b164", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t5e02072a9a3342c9b8b720ad5882ba50 .toyplot-mark-popup");
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
      var axes = {"t0a16876f4dbc4e03a957ecdff32a3fc9": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


If you check the reference documentation for :py:func:`toyplot.plot`,
you will see that its parameters include the union of the parameters for
:py:class:`toyplot.canvas.Canvas`,
:py:meth:`toyplot.canvas.Canvas.axes`, and
:py:meth:`toyplot.axes.Cartesian.plot`, except where parameter names
might conflict.

Similar convenience API functions are provided for
:py:func:`bar <toyplot.bars>`, :py:func:`fill <toyplot.fill>`, and
:py:func:`scatter <toyplot.scatterplot>` plots:

.. code:: python

    toyplot.bars(y, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t5c72d93b27fc497787b7911a046e19dd"><svg height="300.0px" id="t91fbc218342640919b9092a64d2f4eb5" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t7ae48a3a207b4b248006aafc63db6463"><clipPath id="ta83c7e5702354ad8ab093c2a8260c73b"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta83c7e5702354ad8ab093c2a8260c73b)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarMagnitudes" id="te6edb4cdcbfd4ad4af97527f855d6886" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756113" x="50.0" y="250.0"></rect><rect class="toyplot-Datum" height="0.55401662049860079" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756113" x="59.756097560975611" y="249.4459833795014"></rect><rect class="toyplot-Datum" height="2.2160664819944884" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="69.512195121951223" y="247.78393351800551"></rect><rect class="toyplot-Datum" height="4.9861495844875208" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756184" x="79.268292682926827" y="245.01385041551248"></rect><rect class="toyplot-Datum" height="8.86426592797784" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="89.024390243902445" y="241.13573407202216"></rect><rect class="toyplot-Datum" height="13.850415512465389" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="98.780487804878049" y="236.14958448753461"></rect><rect class="toyplot-Datum" height="19.94459833795014" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756184" x="108.53658536585365" y="230.05540166204986"></rect><rect class="toyplot-Datum" height="27.146814404432149" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756184" x="118.29268292682927" y="222.85318559556785"></rect><rect class="toyplot-Datum" height="35.45706371191136" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="128.04878048780489" y="214.54293628808864"></rect><rect class="toyplot-Datum" height="44.875346260387801" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="137.80487804878049" y="205.1246537396122"></rect><rect class="toyplot-Datum" height="55.4016620498615" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="147.5609756097561" y="194.5983379501385"></rect><rect class="toyplot-Datum" height="67.036011080332429" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="157.3170731707317" y="182.96398891966757"></rect><rect class="toyplot-Datum" height="79.778393351800531" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="167.07317073170731" y="170.22160664819947"></rect><rect class="toyplot-Datum" height="93.628808864265892" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756326" x="176.82926829268291" y="156.37119113573411"></rect><rect class="toyplot-Datum" height="108.58725761772851" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="186.58536585365854" y="141.41274238227149"></rect><rect class="toyplot-Datum" height="124.65373961218837" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="196.34146341463415" y="125.34626038781163"></rect><rect class="toyplot-Datum" height="141.82825484764541" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="206.09756097560975" y="108.17174515235459"></rect><rect class="toyplot-Datum" height="160.11080332409966" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="215.85365853658536" y="89.889196675900322"></rect><rect class="toyplot-Datum" height="179.5013850415512" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756326" x="225.60975609756096" y="70.498614958448783"></rect><rect class="toyplot-Datum" height="200.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.7560975609756042" x="235.36585365853659" y="50.0"></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t86ac0af27b9a4a7892f40414964b876d" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="195.1219512195122" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(4.878048780487805,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(102.4390243902439,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tef8c534185e248c192b0e61b2fdd67b1" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Bar Data", "names": ["left", "right", "baseline", "magnitude0"], "id": "te6edb4cdcbfd4ad4af97527f855d6886", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t5c72d93b27fc497787b7911a046e19dd .toyplot-mark-popup");
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
      var axes = {"t7ae48a3a207b4b248006aafc63db6463": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


.. code:: python

    toyplot.fill(numpy.column_stack((y, y*2)), width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t81ec8b368c524d3e82da3137a8561b7e"><svg height="300.0px" id="t0b36cce93417457f995bf6ae65d2d6f8" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t4f9120d0b5604b1f994193852fa1b9df"><clipPath id="ta594c6b31df849e897018ff59c8e6524"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta594c6b31df849e897018ff59c8e6524)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-FillBoundaries" id="t4a233899e7f04c00b6c7316bb5d0eb0f" style="stroke:none"><polygon points="50.0,250.0 60.0,249.7229916897507 70.0,248.89196675900277 80.0,247.50692520775624 90.0,245.56786703601108 100.0,243.07479224376732 110.0,240.02770083102493 120.0,236.42659279778394 130.0,232.27146814404432 140.0,227.56232686980613 150.0,222.29916897506925 160.0,216.48199445983377 170.0,210.11080332409972 180.0,203.18559556786707 190.0,195.70637119113573 200.0,187.67313019390582 210.0,179.08587257617731 220.0,169.94459833795017 230.0,160.2493074792244 240.0,150.0 240.0,50.0 230.0,70.498614958448783 220.0,89.889196675900322 210.0,108.17174515235459 200.0,125.34626038781163 190.0,141.41274238227149 180.0,156.37119113573411 170.0,170.22160664819947 160.0,182.96398891966757 150.0,194.5983379501385 140.0,205.1246537396122 130.0,214.54293628808864 120.0,222.85318559556785 110.0,230.05540166204986 100.0,236.14958448753461 90.0,241.13573407202216 80.0,245.01385041551248 70.0,247.78393351800551 60.0,249.4459833795014 50.0,250.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t94fafcf568cf48adb0db500cadb8baf3" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tca25947117f44f5eaa74f547e378faa5" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">2.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], [0.0, 0.005540166204986149, 0.022160664819944595, 0.04986149584487534, 0.08864265927977838, 0.13850415512465372, 0.19944598337950137, 0.2714681440443213, 0.3545706371191135, 0.44875346260387805, 0.5540166204986149, 0.6703601108033241, 0.7977839335180055, 0.936288088642659, 1.0858725761772852, 1.2465373961218837, 1.418282548476454, 1.6011080332409968, 1.7950138504155122, 2.0]], "title": "Fill Data", "names": ["x", "y0", "y1"], "id": "t4a233899e7f04c00b6c7316bb5d0eb0f", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t81ec8b368c524d3e82da3137a8561b7e .toyplot-mark-popup");
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
      var axes = {"t4f9120d0b5604b1f994193852fa1b9df": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


.. code:: python

    numpy.random.seed(1234)
    toyplot.scatterplot(numpy.random.normal(size=50), width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t0fb9a659e0a54f84bc9f5f99746a04ab"><svg height="300.0px" id="tc0d557682e284060a0f4283b2c5b6e2b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td3cdd4d0f4de4ad09ea9eee32404f95d"><clipPath id="t548ac74b1ab44aa69292f011a0ba3f8a"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t548ac74b1ab44aa69292f011a0ba3f8a)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Scatterplot" id="tbf14d699136740538638b6451b1de231" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="132.85162791602949" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="54.0" cy="204.60553612191933" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="58.0" cy="91.360676094610227" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="62.0" cy="166.69483257897474" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.0" cy="184.30243074095708" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.0" cy="114.90775286998338" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="74.0" cy="116.09794002482474" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="78.0" cy="180.67396026351935" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="82.0" cy="152.52248079432022" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="86.0" cy="250.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.0" cy="103.56149057460654" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="94.0" cy="110.38504681828844" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="98.0" cy="112.05206664029386" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="102.0" cy="240.44250858461834" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="106.0" cy="167.61961069835075" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="110.0" cy="153.10854235297342" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="114.0" cy="135.69956924406154" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="118.0" cy="140.72202818496902" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="122.0" cy="96.175406829940982" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="126.0" cy="219.96837994992504" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="130.0" cy="161.94671051469098" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.0" cy="181.51329248472445" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="138.0" cy="144.85141465341349" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.0" cy="129.31213626689947" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="146.0" cy="96.305181020432798" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="150.0" cy="173.4563938438711" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="154.0" cy="124.04133275094105" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="158.0" cy="231.62752284854872" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="162.0" cy="161.10340972363301" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="166.0" cy="107.49215543643837" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="170.0" cy="170.37177906382271" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="174.0" cy="138.63530346894945" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="178.0" cy="107.98380352445203" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.0" cy="108.05460381661081" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="186.0" cy="115.91972708236" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="190.0" cy="158.46976130443468" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="194.0" cy="147.81704606186719" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="198.0" cy="167.13262651824013" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="202.0" cy="116.87114120469981" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="206.0" cy="50.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="210.0" cy="149.91100712335771" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="214.0" cy="177.64923278225569" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.0" cy="151.63999788950724" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="222.0" cy="242.76132131411853" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="226.0" cy="142.50463073848817" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="230.0" cy="191.9235598165954" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="234.0" cy="159.10439157599882" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="238.0" cy="152.4105680788665" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="242.0" cy="120.59437515356517" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="246.0" cy="143.90843338122988" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t65a55689959b41a180276998e09fb895" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(40.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(80.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">50</tspan></text></g></g><g class="toyplot-axes-Axis" id="te367b0765b954477b00462b2c8953ee9" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(10.474903864572891,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-2</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(96.80002360454914,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(183.12514334452538,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">2</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.47143516373249306, -1.1909756947064645, 1.4327069684260973, -0.3126518960917129, -0.7205887333650116, 0.8871629403077386, 0.8595884137174165, -0.6365235044173491, 0.015696372114428918, -2.2426849541854055, 1.150035724719818, 0.9919460223426778, 0.9533241281124304, -2.0212548201949705, -0.334077365808097, 0.002118364683486495, 0.405453411570191, 0.2890919409800353, 1.3211581921293856, -1.5469055532292402, -0.2026463246291819, -0.6559693441389339, 0.19342137647035826, 0.5534389109567419, 1.3181515541801367, -0.4693052847058996, 0.6755540851223808, -1.8170272265901968, -0.1831085401789987, 1.0589691875711504, -0.3978402281999914, 0.3374376536139724, 1.0475785728927218, 1.0459382556276653, 0.8637172916848387, -0.12209157484767426, 0.12471295376821585, -0.32279480560829565, 0.8416747129961416, 2.390960515463033, 0.07619958783723642, -0.5664459304649568, 0.036141936684072715, -2.0749776006900293, 0.24779219974854666, -0.8971567844396987, -0.1367948332613474, 0.018289191349219306, 0.7554139823981354, 0.2152685809694434]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tbf14d699136740538638b6451b1de231", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t0fb9a659e0a54f84bc9f5f99746a04ab .toyplot-mark-popup");
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
      var axes = {"td3cdd4d0f4de4ad09ea9eee32404f95d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.3909605154630329, "min": -2.2426849541854055}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


.. code:: python

    toyplot.matrix(numpy.random.normal(size=(10, 10)), width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t4fb5ba8f2000407eb4bf2502ec548255"><svg height="300.0px" id="ted027a8d9dd9426c9468268351019efe" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Table" id="te4e74d6e14044053aacdd8605fecbdb2"><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(96.0,80.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(108.0,80.0)"><tspan style="dominant-baseline:inherit">1</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(120.0,80.0)"><tspan style="dominant-baseline:inherit">2</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(132.0,80.0)"><tspan style="dominant-baseline:inherit">3</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(144.0,80.0)"><tspan style="dominant-baseline:inherit">4</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(156.0,80.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(168.0,80.0)"><tspan style="dominant-baseline:inherit">6</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(180.0,80.0)"><tspan style="dominant-baseline:inherit">7</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(192.0,80.0)"><tspan style="dominant-baseline:inherit">8</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(204.0,80.0)"><tspan style="dominant-baseline:inherit">9</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" transform="translate(85.0,96.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><rect height="12.0" style="fill:rgb(90.6%,53.1%,42.1%);fill-opacity:1.0;stroke:none" width="12.0" x="90.0" y="90.0"><title>0.841008794931</title></rect><rect height="12.0" style="fill:rgb(71.4%,84.4%,91.1%);fill-opacity:1.0;stroke:none" width="12.0" x="102.0" y="90.0"><title>-1.44581007704</title></rect><rect height="12.0" style="fill:rgb(73.2%,85.4%,91.6%);fill-opacity:1.0;stroke:none" width="12.0" x="114.0" y="90.0"><title>-1.4019732815</title></rect><rect height="12.0" style="fill:rgb(98.8%,87.6%,81.1%);fill-opacity:1.0;stroke:none" width="12.0" x="126.0" y="90.0"><title>-0.100918199949</title></rect><rect height="12.0" style="fill:rgb(97.1%,95.9%,95.3%);fill-opacity:1.0;stroke:none" width="12.0" x="138.0" y="90.0"><title>-0.548242449187</title></rect><rect height="12.0" style="fill:rgb(98.7%,88.5%,82.4%);fill-opacity:1.0;stroke:none" width="12.0" x="150.0" y="90.0"><title>-0.144619508369</title></rect><rect height="12.0" style="fill:rgb(97.1%,73%,61.6%);fill-opacity:1.0;stroke:none" width="12.0" x="162.0" y="90.0"><title>0.354020332199</title></rect><rect height="12.0" style="fill:rgb(99.1%,86.4%,79%);fill-opacity:1.0;stroke:none" width="12.0" x="174.0" y="90.0"><title>-0.0355130252781</title></rect><rect height="12.0" style="fill:rgb(95.8%,65.5%,51.9%);fill-opacity:1.0;stroke:none" width="12.0" x="186.0" y="90.0"><title>0.565738306063</title></rect><rect height="12.0" style="fill:rgb(75.2%,20.2%,22%);fill-opacity:1.0;stroke:none" width="12.0" x="198.0" y="90.0"><title>1.54565880463</title></rect><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" transform="translate(85.0,108.0)"><tspan style="dominant-baseline:inherit">1</tspan></text><rect height="12.0" style="fill:rgb(87.4%,92.4%,95.1%);fill-opacity:1.0;stroke:none" width="12.0" x="90.0" y="102.0"><title>-0.974236333767</title></rect><rect height="12.0" style="fill:rgb(99%,87.1%,80.1%);fill-opacity:1.0;stroke:none" width="12.0" x="102.0" y="102.0"><title>-0.0703448771041</title></rect><rect height="12.0" style="fill:rgb(97.3%,74.7%,63.7%);fill-opacity:1.0;stroke:none" width="12.0" x="114.0" y="102.0"><title>0.307968855216</title></rect><rect height="12.0" style="fill:rgb(98.4%,89.6%,84.5%);fill-opacity:1.0;stroke:none" width="12.0" x="126.0" y="102.0"><title>-0.208498763106</title></rect><rect height="12.0" style="fill:rgb(86.8%,44.3%,35.3%);fill-opacity:1.0;stroke:none" width="12.0" x="138.0" y="102.0"><title>1.03380073256</title></rect><rect height="12.0" style="fill:rgb(25.8%,57%,76.1%);fill-opacity:1.0;stroke:none" width="12.0" x="150.0" y="102.0"><title>-2.40045363381</title></rect><rect height="12.0" style="fill:rgb(57%,5.32%,14.8%);fill-opacity:1.0;stroke:none" width="12.0" x="162.0" y="102.0"><title>2.03060362084</title></rect><rect height="12.0" style="fill:rgb(83.2%,90.4%,94.3%);fill-opacity:1.0;stroke:none" width="12.0" x="174.0" y="102.0"><title>-1.14263128902</title></rect><rect height="12.0" style="fill:rgb(97.9%,78.1%,68.1%);fill-opacity:1.0;stroke:none" width="12.0" x="186.0" y="102.0"><title>0.211883386778</title></rect><rect height="12.0" style="fill:rgb(93.4%,59.3%,46.9%);fill-opacity:1.0;stroke:none" width="12.0" x="198.0" y="102.0"><title>0.704720624317</title></rect><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" transform="translate(85.0,120.0)"><tspan style="dominant-baseline:inherit">2</tspan></text><rect height="12.0" style="fill:rgb(92.2%,94.6%,96%);fill-opacity:1.0;stroke:none" width="12.0" x="90.0" y="114.0"><title>-0.785435211763</title></rect><rect height="12.0" style="fill:rgb(96.4%,69.2%,56.7%);fill-opacity:1.0;stroke:none" width="12.0" x="102.0" y="114.0"><title>0.462059737162</title></rect><rect height="12.0" style="fill:rgb(93.4%,59.4%,46.9%);fill-opacity:1.0;stroke:none" width="12.0" x="114.0" y="114.0"><title>0.704228225462</title></rect><rect height="12.0" style="fill:rgb(96.1%,67%,53.9%);fill-opacity:1.0;stroke:none" width="12.0" x="126.0" y="114.0"><title>0.523507967894</title></rect><rect height="12.0" style="fill:rgb(88.6%,93%,95.3%);fill-opacity:1.0;stroke:none" width="12.0" x="138.0" y="114.0"><title>-0.92625431353</title></rect><rect height="12.0" style="fill:rgb(58.1%,5.68%,15%);fill-opacity:1.0;stroke:none" width="12.0" x="150.0" y="114.0"><title>2.00784295078</title></rect><rect height="12.0" style="fill:rgb(97.8%,77.6%,67.4%);fill-opacity:1.0;stroke:none" width="12.0" x="162.0" y="114.0"><title>0.226962541871</title></rect><rect height="12.0" style="fill:rgb(82.9%,90.3%,94.3%);fill-opacity:1.0;stroke:none" width="12.0" x="174.0" y="114.0"><title>-1.15265910925</title></rect><rect height="12.0" style="fill:rgb(94.8%,62.7%,49.4%);fill-opacity:1.0;stroke:none" width="12.0" x="186.0" y="114.0"><title>0.631979445809</title></rect><rect height="12.0" style="fill:rgb(98.9%,84.3%,76%);fill-opacity:1.0;stroke:none" width="12.0" x="198.0" y="114.0"><title>0.0395126866934</title></rect><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" transform="translate(85.0,132.0)"><tspan style="dominant-baseline:inherit">3</tspan></text><rect height="12.0" style="fill:rgb(96.4%,69.1%,56.6%);fill-opacity:1.0;stroke:none" width="12.0" x="90.0" y="126.0"><title>0.464392325051</title></rect><rect height="12.0" style="fill:rgb(1.96%,18.8%,38%);fill-opacity:1.0;stroke:none" width="12.0" x="102.0" y="126.0"><title>-3.56351666062</title></rect><rect height="12.0" style="fill:rgb(80.6%,30.9%,27%);fill-opacity:1.0;stroke:none" width="12.0" x="114.0" y="126.0"><title>1.32110561547</title></rect><rect height="12.0" style="fill:rgb(98.3%,80.2%,70.8%);fill-opacity:1.0;stroke:none" width="12.0" x="126.0" y="126.0"><title>0.152630552205</title></rect><rect height="12.0" style="fill:rgb(98.2%,79.8%,70.3%);fill-opacity:1.0;stroke:none" width="12.0" x="138.0" y="126.0"><title>0.164529542932</title></rect><rect height="12.0" style="fill:rgb(97.5%,93.7%,91.5%);fill-opacity:1.0;stroke:none" width="12.0" x="150.0" y="126.0"><title>-0.430095690876</title></rect><rect height="12.0" style="fill:rgb(92.1%,56.5%,44.7%);fill-opacity:1.0;stroke:none" width="12.0" x="162.0" y="126.0"><title>0.767368735752</title></rect><rect height="12.0" style="fill:rgb(87.8%,46.5%,37%);fill-opacity:1.0;stroke:none" width="12.0" x="174.0" y="126.0"><title>0.98491984191</title></rect><rect height="12.0" style="fill:rgb(97.6%,76%,65.4%);fill-opacity:1.0;stroke:none" width="12.0" x="186.0" y="126.0"><title>0.270835848827</title></rect><rect height="12.0" style="fill:rgb(78.9%,27.5%,25.4%);fill-opacity:1.0;stroke:none" width="12.0" x="198.0" y="126.0"><title>1.39198619345</title></rect><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" transform="translate(85.0,144.0)"><tspan style="dominant-baseline:inherit">4</tspan></text><rect height="12.0" style="fill:rgb(98.7%,82.8%,74.1%);fill-opacity:1.0;stroke:none" width="12.0" x="90.0" y="138.0"><title>0.0798423130086</title></rect><rect height="12.0" style="fill:rgb(97.7%,93.2%,90.5%);fill-opacity:1.0;stroke:none" width="12.0" x="102.0" y="138.0"><title>-0.399964580697</title></rect><rect height="12.0" style="fill:rgb(86.1%,91.8%,94.9%);fill-opacity:1.0;stroke:none" width="12.0" x="114.0" y="138.0"><title>-1.02785055868</title></rect><rect height="12.0" style="fill:rgb(96.9%,96.6%,96.4%);fill-opacity:1.0;stroke:none" width="12.0" x="126.0" y="138.0"><title>-0.584718211261</title></rect><rect height="12.0" style="fill:rgb(91.1%,54.2%,42.9%);fill-opacity:1.0;stroke:none" width="12.0" x="138.0" y="138.0"><title>0.816593926548</title></rect><rect height="12.0" style="fill:rgb(98.9%,87.3%,80.5%);fill-opacity:1.0;stroke:none" width="12.0" x="150.0" y="138.0"><title>-0.0819470518267</title></rect><rect height="12.0" style="fill:rgb(97.9%,92.2%,88.8%);fill-opacity:1.0;stroke:none" width="12.0" x="162.0" y="138.0"><title>-0.344766014255</title></rect><rect height="12.0" style="fill:rgb(96%,66.8%,53.7%);fill-opacity:1.0;stroke:none" width="12.0" x="174.0" y="138.0"><title>0.528288145297</title></rect><rect height="12.0" style="fill:rgb(85%,91.3%,94.7%);fill-opacity:1.0;stroke:none" width="12.0" x="186.0" y="138.0"><title>-1.06898878348</title></rect><rect height="12.0" style="fill:rgb(97.2%,95.3%,94.1%);fill-opacity:1.0;stroke:none" width="12.0" x="198.0" y="138.0"><title>-0.511881309127</title></rect><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" transform="translate(85.0,156.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><rect height="12.0" style="fill:rgb(97.4%,75.3%,64.5%);fill-opacity:1.0;stroke:none" width="12.0" x="90.0" y="150.0"><title>0.291205359743</title></rect><rect height="12.0" style="fill:rgb(95.8%,65.4%,51.9%);fill-opacity:1.0;stroke:none" width="12.0" x="102.0" y="150.0"><title>0.566533696354</title></rect><rect height="12.0" style="fill:rgb(96.2%,67.7%,54.8%);fill-opacity:1.0;stroke:none" width="12.0" x="114.0" y="150.0"><title>0.503591759111</title></rect><rect height="12.0" style="fill:rgb(97.5%,75.5%,64.7%);fill-opacity:1.0;stroke:none" width="12.0" x="126.0" y="150.0"><title>0.285295684782</title></rect><rect height="12.0" style="fill:rgb(96.3%,68.4%,55.7%);fill-opacity:1.0;stroke:none" width="12.0" x="138.0" y="150.0"><title>0.48428811275</title></rect><rect height="12.0" style="fill:rgb(79.6%,28.9%,26.1%);fill-opacity:1.0;stroke:none" width="12.0" x="150.0" y="150.0"><title>1.36348151243</title></rect><rect height="12.0" style="fill:rgb(92.3%,94.7%,96%);fill-opacity:1.0;stroke:none" width="12.0" x="162.0" y="150.0"><title>-0.781105283625</title></rect><rect height="12.0" style="fill:rgb(97.4%,94.4%,92.7%);fill-opacity:1.0;stroke:none" width="12.0" x="174.0" y="150.0"><title>-0.468017666337</title></rect><rect height="12.0" style="fill:rgb(82.9%,35.5%,29.2%);fill-opacity:1.0;stroke:none" width="12.0" x="186.0" y="150.0"><title>1.22457435513</title></rect><rect height="12.0" style="fill:rgb(78.2%,87.9%,93.1%);fill-opacity:1.0;stroke:none" width="12.0" x="198.0" y="150.0"><title>-1.28110827514</title></rect><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" transform="translate(85.0,168.0)"><tspan style="dominant-baseline:inherit">6</tspan></text><rect height="12.0" style="fill:rgb(90%,51.5%,40.9%);fill-opacity:1.0;stroke:none" width="12.0" x="90.0" y="162.0"><title>0.875475504274</title></rect><rect height="12.0" style="fill:rgb(60.3%,78.8%,87.9%);fill-opacity:1.0;stroke:none" width="12.0" x="102.0" y="162.0"><title>-1.71071532403</title></rect><rect height="12.0" style="fill:rgb(97.5%,94.1%,92.2%);fill-opacity:1.0;stroke:none" width="12.0" x="114.0" y="162.0"><title>-0.450765103136</title></rect><rect height="12.0" style="fill:rgb(92.5%,57.3%,45.3%);fill-opacity:1.0;stroke:none" width="12.0" x="126.0" y="162.0"><title>0.749163805919</title></rect><rect height="12.0" style="fill:rgb(98.4%,89.5%,84.3%);fill-opacity:1.0;stroke:none" width="12.0" x="138.0" y="162.0"><title>-0.203932866101</title></rect><rect height="12.0" style="fill:rgb(98.5%,89.1%,83.6%);fill-opacity:1.0;stroke:none" width="12.0" x="150.0" y="162.0"><title>-0.182175411666</title></rect><rect height="12.0" style="fill:rgb(93.8%,60.4%,47.7%);fill-opacity:1.0;stroke:none" width="12.0" x="162.0" y="162.0"><title>0.680656004381</title></rect><rect height="12.0" style="fill:rgb(55.5%,76.1%,86.5%);fill-opacity:1.0;stroke:none" width="12.0" x="174.0" y="162.0"><title>-1.81849899039</title></rect><rect height="12.0" style="fill:rgb(98.9%,84%,75.6%);fill-opacity:1.0;stroke:none" width="12.0" x="186.0" y="162.0"><title>0.0470716353257</title></rect><rect height="12.0" style="fill:rgb(96.8%,71.6%,59.7%);fill-opacity:1.0;stroke:none" width="12.0" x="198.0" y="162.0"><title>0.394844209327</title></rect><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" transform="translate(85.0,180.0)"><tspan style="dominant-baseline:inherit">7</tspan></text><rect height="12.0" style="fill:rgb(98.3%,90.4%,85.7%);fill-opacity:1.0;stroke:none" width="12.0" x="90.0" y="174.0"><title>-0.248432054381</title></rect><rect height="12.0" style="fill:rgb(96.4%,96.6%,96.8%);fill-opacity:1.0;stroke:none" width="12.0" x="102.0" y="174.0"><title>-0.617706647997</title></rect><rect height="12.0" style="fill:rgb(94.8%,95.9%,96.5%);fill-opacity:1.0;stroke:none" width="12.0" x="114.0" y="174.0"><title>-0.682883996449</title></rect><rect height="12.0" style="fill:rgb(96.6%,70.1%,57.9%);fill-opacity:1.0;stroke:none" width="12.0" x="126.0" y="174.0"><title>0.436257604341</title></rect><rect height="12.0" style="fill:rgb(60.7%,79%,88%);fill-opacity:1.0;stroke:none" width="12.0" x="138.0" y="174.0"><title>-1.70301277411</title></rect><rect height="12.0" style="fill:rgb(96.8%,71.6%,59.8%);fill-opacity:1.0;stroke:none" width="12.0" x="150.0" y="174.0"><title>0.393710599139</title></rect><rect height="12.0" style="fill:rgb(97.3%,94.6%,93.1%);fill-opacity:1.0;stroke:none" width="12.0" x="162.0" y="174.0"><title>-0.479324003575</title></rect><rect height="12.0" style="fill:rgb(98.1%,91.3%,87.3%);fill-opacity:1.0;stroke:none" width="12.0" x="174.0" y="174.0"><title>-0.299016292966</title></rect><rect height="12.0" style="fill:rgb(93.6%,59.8%,47.2%);fill-opacity:1.0;stroke:none" width="12.0" x="186.0" y="174.0"><title>0.694103287679</title></rect><rect height="12.0" style="fill:rgb(93.9%,60.5%,47.8%);fill-opacity:1.0;stroke:none" width="12.0" x="198.0" y="174.0"><title>0.67862967371</title></rect><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" transform="translate(85.0,192.0)"><tspan style="dominant-baseline:inherit">8</tspan></text><rect height="12.0" style="fill:rgb(97.8%,77.1%,66.8%);fill-opacity:1.0;stroke:none" width="12.0" x="90.0" y="186.0"><title>0.239555995004</title></rect><rect height="12.0" style="fill:rgb(98.3%,80.3%,70.9%);fill-opacity:1.0;stroke:none" width="12.0" x="102.0" y="186.0"><title>0.151226629294</title></rect><rect height="12.0" style="fill:rgb(91.1%,54.2%,42.9%);fill-opacity:1.0;stroke:none" width="12.0" x="114.0" y="186.0"><title>0.81612723336</title></rect><rect height="12.0" style="fill:rgb(63.8%,7.5%,15.9%);fill-opacity:1.0;stroke:none" width="12.0" x="126.0" y="186.0"><title>1.8935344676</title></rect><rect height="12.0" style="fill:rgb(94.6%,62.3%,49.1%);fill-opacity:1.0;stroke:none" width="12.0" x="138.0" y="186.0"><title>0.639632763194</title></rect><rect height="12.0" style="fill:rgb(87.7%,92.5%,95.2%);fill-opacity:1.0;stroke:none" width="12.0" x="150.0" y="186.0"><title>-0.962028831905</title></rect><rect height="12.0" style="fill:rgb(41.6%,67.3%,81.7%);fill-opacity:1.0;stroke:none" width="12.0" x="162.0" y="186.0"><title>-2.08526564212</title></rect><rect height="12.0" style="fill:rgb(62%,6.91%,15.6%);fill-opacity:1.0;stroke:none" width="12.0" x="174.0" y="186.0"><title>1.93024676747</title></rect><rect height="12.0" style="fill:rgb(59.3%,78.3%,87.6%);fill-opacity:1.0;stroke:none" width="12.0" x="186.0" y="186.0"><title>-1.73534887447</title></rect><rect height="12.0" style="fill:rgb(83.2%,36.2%,29.5%);fill-opacity:1.0;stroke:none" width="12.0" x="198.0" y="186.0"><title>1.2103837049</title></rect><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" transform="translate(85.0,204.0)"><tspan style="dominant-baseline:inherit">9</tspan></text><rect height="12.0" style="fill:rgb(91.5%,55.1%,43.6%);fill-opacity:1.0;stroke:none" width="12.0" x="90.0" y="198.0"><title>0.797435419428</title></rect><rect height="12.0" style="fill:rgb(97.7%,92.8%,89.9%);fill-opacity:1.0;stroke:none" width="12.0" x="102.0" y="198.0"><title>-0.379810784047</title></rect><rect height="12.0" style="fill:rgb(93.4%,59.4%,46.9%);fill-opacity:1.0;stroke:none" width="12.0" x="114.0" y="198.0"><title>0.702562224002</title></rect><rect height="12.0" style="fill:rgb(90.5%,93.9%,95.7%);fill-opacity:1.0;stroke:none" width="12.0" x="126.0" y="198.0"><title>-0.850346271655</title></rect><rect height="12.0" style="fill:rgb(84%,37.8%,30.3%);fill-opacity:1.0;stroke:none" width="12.0" x="138.0" y="198.0"><title>1.1768124501</title></rect><rect height="12.0" style="fill:rgb(97.2%,95.5%,94.5%);fill-opacity:1.0;stroke:none" width="12.0" x="150.0" y="198.0"><title>-0.524336102632</title></rect><rect height="12.0" style="fill:rgb(93.4%,59.5%,47%);fill-opacity:1.0;stroke:none" width="12.0" x="162.0" y="198.0"><title>0.700907730916</title></rect><rect height="12.0" style="fill:rgb(87.8%,46.6%,37.1%);fill-opacity:1.0;stroke:none" width="12.0" x="174.0" y="198.0"><title>0.984188070722</title></rect><rect height="12.0" style="fill:rgb(98.8%,88%,81.7%);fill-opacity:1.0;stroke:none" width="12.0" x="186.0" y="198.0"><title>-0.121728408667</title></rect><rect height="12.0" style="fill:rgb(40.4%,0%,12.2%);fill-opacity:1.0;stroke:none" width="12.0" x="198.0" y="198.0"><title>2.36576862884</title></rect></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul></div></div>


.. code:: python

    columns = ["Year", "MPG", "Model"]
    canvas, table = toyplot.table(toyplot.data.read_csv("cars.csv").columns(columns)[:10], width=300)
    table.column(2).width = 130



.. raw:: html

    <div align="center" class="toyplot" id="t6512e17f252a49c4b0d16e6ba3775f95"><svg height="300.0px" id="t035b26d3aa754207a4961d8d21b3a572" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Table" id="td02390558259417e97eda065ae352133"><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:begin" transform="translate(55.0,59.090909090909093)"><tspan style="dominant-baseline:inherit">Year</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:begin" transform="translate(90.0,59.090909090909093)"><tspan style="dominant-baseline:inherit">MPG</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:begin" transform="translate(125.0,59.090909090909093)"><tspan style="dominant-baseline:inherit">Model</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(55.0,77.27272727272728)"><tspan style="dominant-baseline:inherit">70.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(90.0,77.27272727272728)"><tspan style="dominant-baseline:inherit">18.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(125.0,77.27272727272728)"><tspan style="dominant-baseline:inherit">chevrolet chevelle malibu</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(55.0,95.454545454545467)"><tspan style="dominant-baseline:inherit">70.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(90.0,95.454545454545467)"><tspan style="dominant-baseline:inherit">15.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(125.0,95.454545454545467)"><tspan style="dominant-baseline:inherit">buick skylark 320</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(55.0,113.63636363636365)"><tspan style="dominant-baseline:inherit">70.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(90.0,113.63636363636365)"><tspan style="dominant-baseline:inherit">18.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(125.0,113.63636363636365)"><tspan style="dominant-baseline:inherit">plymouth satellite</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(55.0,131.81818181818184)"><tspan style="dominant-baseline:inherit">70.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(90.0,131.81818181818184)"><tspan style="dominant-baseline:inherit">16.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(125.0,131.81818181818184)"><tspan style="dominant-baseline:inherit">amc rebel sst</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(55.0,150.00000000000003)"><tspan style="dominant-baseline:inherit">70.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(90.0,150.00000000000003)"><tspan style="dominant-baseline:inherit">17.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(125.0,150.00000000000003)"><tspan style="dominant-baseline:inherit">ford torino</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(55.0,168.18181818181822)"><tspan style="dominant-baseline:inherit">70.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(90.0,168.18181818181822)"><tspan style="dominant-baseline:inherit">15.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(125.0,168.18181818181822)"><tspan style="dominant-baseline:inherit">ford galaxie 500</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(55.0,186.3636363636364)"><tspan style="dominant-baseline:inherit">70.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(90.0,186.3636363636364)"><tspan style="dominant-baseline:inherit">14.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(125.0,186.3636363636364)"><tspan style="dominant-baseline:inherit">chevrolet impala</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(55.0,204.54545454545459)"><tspan style="dominant-baseline:inherit">70.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(90.0,204.54545454545459)"><tspan style="dominant-baseline:inherit">14.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(125.0,204.54545454545459)"><tspan style="dominant-baseline:inherit">plymouth fury iii</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(55.0,222.72727272727278)"><tspan style="dominant-baseline:inherit">70.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(90.0,222.72727272727278)"><tspan style="dominant-baseline:inherit">14.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(125.0,222.72727272727278)"><tspan style="dominant-baseline:inherit">pontiac catalina</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(55.0,240.90909090909096)"><tspan style="dominant-baseline:inherit">70.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(90.0,240.90909090909096)"><tspan style="dominant-baseline:inherit">15.0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(125.0,240.90909090909096)"><tspan style="dominant-baseline:inherit">amc ambassador dpl</tspan></text><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.0" y1="68.181818181818187" y2="68.181818181818187"></line></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul></div></div>


If you need greater control over the positioning of the axes within the
canvas, need to add multiple axes to one canvas, or need to add multiple
marks to one set of axes, you'll have to create the canvas and axes
explicitly.
