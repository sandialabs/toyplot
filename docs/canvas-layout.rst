
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _canvas-layout:

Canvas Layout
=============

In Toyplot, ``axes`` (including :ref:`cartesian-axes`,
:ref:`table-axes`, and others) are used to map data values into canvas
coordinates. The axes *range* (the area on the canvas that they occupy)
is specified when they are created. By default, axes are sized to fill
the entire canvas:

.. code:: python

    import numpy
    y = numpy.linspace(0, 1, 20) ** 2

.. code:: python

    import toyplot
    toyplot.plot(y, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t326590473c1a406ab63da6cbdfd76250"><svg height="300.0px" id="te2b8c4ceec724fde89e699f1103ab4f4" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td256aa88fbcc486f8647da7e6dea6145"><clipPath id="ta4ea8d66f37d49faa4119210b6d38843"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta4ea8d66f37d49faa4119210b6d38843)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tcbdb2d99f3d14c76a5d0108157705ad1" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tbf988a45b66b4be78f06609f82ebbdb7" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tf240d59a4065413fbbc419312c7ce337" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tcbdb2d99f3d14c76a5d0108157705ad1", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t326590473c1a406ab63da6cbdfd76250 .toyplot-mark-popup");
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
      var axes = {"td256aa88fbcc486f8647da7e6dea6145": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


If you need greater control over the positioning of the axes within the
canvas, or want to add multiple axes to one canvas, it's necessary to
create the canvas and axes explicitly, then use the axes to plot your
data. For example, you can use the *bounds* argument to specify explicit
(xmin, xmax, ymin, ymax) bounds for the axes using canvas coordinates
(note that canvas coordinates always *increase* from top to bottom,
unlike cartesian coordinates):

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(bounds=(30, 270, 30, 270))
    axes1.plot(y)
    axes2 = canvas.axes(bounds=(330, 570, 30, 270))
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="t569d121e8219451ebd523e9d926088eb"><svg height="300.0px" id="t2de155222ce542f18d0d3756e02d17bc" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t99d62cb876184b378a0897fd684d9e7e"><clipPath id="td73d9dec35ea43559be4265dcf0c0687"><rect height="260.0" width="260.0" x="20.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td73d9dec35ea43559be4265dcf0c0687)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="20.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="ta68e26c61abf4dc2afbbe3955ead895f" style="fill:none"><g class="toyplot-Series"><path d="M 30.0 270.0 L 42.0 269.33518005540168 L 54.0 267.34072022160666 L 66.0 264.016620498615 L 78.0 259.36288088642664 L 90.0 253.37950138504155 L 102.0 246.06648199445985 L 114.0 237.42382271468145 L 126.0 227.45152354570638 L 138.0 216.14958448753464 L 150.0 203.51800554016617 L 162.0 189.55678670360109 L 174.0 174.26592797783934 L 186.0 157.64542936288092 L 198.0 139.6952908587258 L 210.0 120.41551246537395 L 222.0 99.806094182825504 L 234.0 77.867036011080387 L 246.0 54.598337950138536 L 258.0 30.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="170.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="215.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="t401f22a6676f42368ac000b865d002c0" transform="translate(30.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="te7079a4cb8fc415ab830542917b33937" transform="translate(30.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t3a1e473d651641caa6f7990b2931c144"><clipPath id="taba6c422286f4e939b6c8b9002ab5fad"><rect height="260.0" width="260.0" x="320.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#taba6c422286f4e939b6c8b9002ab5fad)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="320.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="tcaa07cbba8d34528a87f0d233f583d39" style="fill:none"><g class="toyplot-Series"><path d="M 330.0 30.0 L 342.0 30.664819944598332 L 354.0 32.659279778393355 L 366.0 35.983379501385038 L 378.0 40.637119113573412 L 390.0 46.62049861495845 L 402.0 53.933518005540151 L 414.0 62.576177285318565 L 426.0 72.54847645429362 L 438.0 83.850415512465361 L 450.0 96.4819944598338 L 462.0 110.44321329639889 L 474.0 125.73407202216066 L 486.0 142.35457063711908 L 498.0 160.3047091412742 L 510.0 179.58448753462605 L 522.0 200.19390581717448 L 534.0 222.13296398891964 L 546.0 245.40166204986147 L 558.0 270.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="470.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="515.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="taf93a7eb420b4bc887318f35d0781cba" transform="translate(330.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tbb5089e7d4964fc9a67f61c2f0ad506f" transform="translate(330.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "ta68e26c61abf4dc2afbbe3955ead895f", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tcaa07cbba8d34528a87f0d233f583d39", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t569d121e8219451ebd523e9d926088eb .toyplot-mark-popup");
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
      var axes = {"t3a1e473d651641caa6f7990b2931c144": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 570.0, "min": 330.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}, "t99d62cb876184b378a0897fd684d9e7e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 270.0, "min": 30.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}};
    
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


You can also use *negative* values to specify values relative to the
right and bottom sides of the canvas, instead of the (default) left and
top sides, greatly simplifying the layout:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(bounds=(30, 270, 30, -30))
    axes1.plot(y)
    axes2 = canvas.axes(bounds=(-270, -30, 30, -30))
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="td531ecaf4e774f02aec692993da8368e"><svg height="300.0px" id="t55bde401252b4469b7792d631df837b2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t3ce7a82d9a5d4096b8e67c3e028c54f5"><clipPath id="tb719274068494719a84db18234201e01"><rect height="260.0" width="260.0" x="20.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb719274068494719a84db18234201e01)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="20.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="td5372d6aa97c41c09a3dfd1d6fca4aaa" style="fill:none"><g class="toyplot-Series"><path d="M 30.0 270.0 L 42.0 269.33518005540168 L 54.0 267.34072022160666 L 66.0 264.016620498615 L 78.0 259.36288088642664 L 90.0 253.37950138504155 L 102.0 246.06648199445985 L 114.0 237.42382271468145 L 126.0 227.45152354570638 L 138.0 216.14958448753464 L 150.0 203.51800554016617 L 162.0 189.55678670360109 L 174.0 174.26592797783934 L 186.0 157.64542936288092 L 198.0 139.6952908587258 L 210.0 120.41551246537395 L 222.0 99.806094182825504 L 234.0 77.867036011080387 L 246.0 54.598337950138536 L 258.0 30.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="170.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="215.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="t5cbac71d6c814e15aa8d47b99903e988" transform="translate(30.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t046daaf9b9ff4d5bb9f15c639d51b834" transform="translate(30.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t2c6d775ade2f470b8670541bce6f9bc3"><clipPath id="tdf6b90ca2e634a95ab0cfea5794e39e5"><rect height="260.0" width="260.0" x="320.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tdf6b90ca2e634a95ab0cfea5794e39e5)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="320.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="tcb08499aebfe49c5b213c1896b9ca8cd" style="fill:none"><g class="toyplot-Series"><path d="M 330.0 30.0 L 342.0 30.664819944598332 L 354.0 32.659279778393355 L 366.0 35.983379501385038 L 378.0 40.637119113573412 L 390.0 46.62049861495845 L 402.0 53.933518005540151 L 414.0 62.576177285318565 L 426.0 72.54847645429362 L 438.0 83.850415512465361 L 450.0 96.4819944598338 L 462.0 110.44321329639889 L 474.0 125.73407202216066 L 486.0 142.35457063711908 L 498.0 160.3047091412742 L 510.0 179.58448753462605 L 522.0 200.19390581717448 L 534.0 222.13296398891964 L 546.0 245.40166204986147 L 558.0 270.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="470.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="515.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="t050b51952ff64f408a5cb0d52d55297e" transform="translate(330.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t3f50c49b32bb493eaddfb63cf2db080d" transform="translate(330.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "td5372d6aa97c41c09a3dfd1d6fca4aaa", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tcb08499aebfe49c5b213c1896b9ca8cd", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#td531ecaf4e774f02aec692993da8368e .toyplot-mark-popup");
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
      var axes = {"t2c6d775ade2f470b8670541bce6f9bc3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 570.0, "min": 330.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}, "t3ce7a82d9a5d4096b8e67c3e028c54f5": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 270.0, "min": 30.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}};
    
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


Furthermore, the bounds parameters can use any :ref:`units`, including
"%" units, so you can use real-world units and relative dimensioning in
any combination that makes sense:

.. code:: python

    canvas = toyplot.Canvas(width="20cm", height="2in")
    axes1 = canvas.axes(bounds=("1cm", "5cm", "10%", "80%"))
    axes1.plot(y)
    axes2 = canvas.axes(bounds=("6cm", "-1cm", "10%", "80%"))
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="t391843615be54ebeb6f76fe6eef78099"><svg height="192.0px" id="t3b27a8497c3d41098177e80a51752432" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 755.9055119999999 192.0" width="755.9055119999999px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tbd9eca3e57c845f4a15ef72264e0d9e7"><clipPath id="t6f91b542e2074ec5a0fdd1666ed59706"><rect height="154.40000000000003" width="171.1811024" x="27.795275600000004" y="9.200000000000003"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t6f91b542e2074ec5a0fdd1666ed59706)" style="cursor:crosshair"><rect height="154.40000000000003" style="pointer-events:all;visibility:hidden" width="171.1811024" x="27.795275600000004" y="9.200000000000003"></rect><g class="toyplot-mark-Plot" id="t91f4dbda0d71458c83990729be5a711f" style="fill:none"><g class="toyplot-Series"><path d="M 37.795275600000004 153.60000000000002 L 45.35433072 153.22770083102495 L 52.913385840000004 152.11080332409975 L 60.47244096 150.2493074792244 L 68.031496079999997 147.6432132963989 L 75.590551199999993 144.29252077562327 L 83.149606320000004 140.19722991689756 L 90.708661439999986 135.3573407202216 L 98.267716559999997 129.77285318559558 L 105.82677168000001 123.44376731301942 L 113.38582679999999 116.3700831024931 L 120.94488192 108.55180055401662 L 128.50393703999998 99.988919667590054 L 136.06299215999999 90.681440443213333 L 143.62204727999998 80.629362880886447 L 151.18110239999999 69.832686980609424 L 158.74015752 58.291412742382292 L 166.29921263999998 46.005540166205023 L 173.85826775999999 32.975069252077589 L 181.41732287999997 19.200000000000003" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="88.97637799999998" y="29.200000000000003"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="133.97637799999998" y="36.2"></text></g><g class="toyplot-axes-Axis" id="t7540524ffd27429c96b02ba0b980e66e" transform="translate(37.7952756,153.6) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="143.62204727999998" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(113.38582679999999,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(151.1811024,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t21a7e2766b1e46dd8196d3ea25339ce2" transform="translate(37.7952756,153.6) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="134.40000000000003" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(67.20000000000002,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(134.40000000000003,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t11d49315b6ec4b37b532320ebcaf5427"><clipPath id="td9be42dfb18843689d5c758dcb288044"><rect height="154.40000000000003" width="511.3385827999999" x="216.7716536" y="9.200000000000003"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td9be42dfb18843689d5c758dcb288044)" style="cursor:crosshair"><rect height="154.40000000000003" style="pointer-events:all;visibility:hidden" width="511.3385827999999" x="216.7716536" y="9.200000000000003"></rect><g class="toyplot-mark-Plot" id="tb0689a52ce8c4dc49fecc8d539555fb9" style="fill:none"><g class="toyplot-Series"><path d="M 226.77165360000001 19.200000000000003 L 251.33858273999999 19.572299168975068 L 275.90551188000001 20.689196675900281 L 300.47244102000002 22.550692520775623 L 325.03937016000003 25.156786703601114 L 349.60629929999999 28.507479224376734 L 374.17322844 32.602770083102492 L 398.74015757999996 37.442659279778404 L 423.30708672000003 43.027146814404432 L 447.87401585999999 49.356232686980618 L 472.440945 56.429916897506935 L 497.00787414000001 64.248199445983389 L 521.57480327999997 72.811080332409972 L 546.14173241999993 82.118559556786693 L 570.70866155999988 92.170637119113579 L 595.27559069999995 102.9673130193906 L 619.84251984000002 114.50858725761772 L 644.40944897999998 126.794459833795 L 668.97637811999994 139.82493074792245 L 693.54330726000001 153.60000000000002" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="618.1102364" y="29.200000000000003"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="663.1102364" y="36.2"></text></g><g class="toyplot-axes-Axis" id="ta3cb59d6c06e44e483a3868bf08d83cf" transform="translate(226.7716536,153.6) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="466.7716536599999" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(122.83464569999998,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.66929139999996,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(368.5039370999999,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(491.3385827999999,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="td5f8d4d8d8a64104ae957f91078eb5c5" transform="translate(226.7716536,153.6) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="134.40000000000003" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(67.20000000000002,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(134.40000000000003,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t91f4dbda0d71458c83990729be5a711f", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tb0689a52ce8c4dc49fecc8d539555fb9", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t391843615be54ebeb6f76fe6eef78099 .toyplot-mark-popup");
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
      var axes = {"t11d49315b6ec4b37b532320ebcaf5427": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 718.1102364, "min": 226.7716536}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 19.200000000000003, "min": 153.60000000000002}, "scale": "linear"}]}, "tbd9eca3e57c845f4a15ef72264e0d9e7": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 188.97637799999998, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 19.200000000000003, "min": 153.60000000000002}, "scale": "linear"}]}};
    
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


Of course, most of the time this level of control isn't necessary.
Instead, the *grid* argument allows us to easily position each set of
axes on a regular grid that covers the canvas. Note that you can control
the axes position on the grid in a variety of ways:

-  (rows, columns, n)

   -  fill cell :math:`n` (in left-to-right, top-to-bottom order) of an
      :math:`M \times N` grid.

-  (rows, columns, i, j)

   -  fill cell :math:`i,j` of an :math:`M \times N` grid.

-  (rows, columns, i, rowspan, j, colspan)

   -  fill cells :math:`[i, i + rowspan), [j, j + colspan)` of an
      :math:`M \times N` grid.

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(grid=(1, 2, 0))
    axes1.plot(y)
    axes2 = canvas.axes(grid=(1, 2, 1))
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="tc8d209ad4a1c4c47a6c6a5eb39fe4b69"><svg height="300.0px" id="t2561fd635ef54cd386332c610fcfebeb" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t63121211896a4b228749153bd5ce5f2a"><clipPath id="t84f7dc7b772945c788ba4ff79108b1cf"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t84f7dc7b772945c788ba4ff79108b1cf)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="te4e11fca90f646a7a95d51358999a1d2" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="ta6ffb92ab0cc43748a14119dd94ec2f9" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t79072429c0a54c1fb4bd5dae4de609fe" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t347b0c2d6b91418f9bf5c74818718ed7"><clipPath id="t809232571d08471589b059717f59bd43"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t809232571d08471589b059717f59bd43)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t62fe0f1f09514520a486ca397e94a9d6" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 50.0 L 360.0 50.554016620498615 L 370.0 52.21606648199446 L 380.0 54.986149584487535 L 390.0 58.86426592797784 L 400.0 63.850415512465375 L 410.0 69.944598337950126 L 420.0 77.146814404432135 L 430.0 85.45706371191136 L 440.0 94.875346260387801 L 450.0 105.4016620498615 L 460.0 117.03601108033241 L 470.0 129.77839335180056 L 480.0 143.62880886426589 L 490.0 158.58725761772851 L 500.0 174.65373961218839 L 510.0 191.82825484764541 L 520.0 210.11080332409966 L 530.0 229.50138504155123 L 540.0 250.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t2dc36704a8ea4fbcadd664da6a64f3fa" transform="translate(350.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tb440bafbf0d145f2adb334b897b19af3" transform="translate(350.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "te4e11fca90f646a7a95d51358999a1d2", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t62fe0f1f09514520a486ca397e94a9d6", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tc8d209ad4a1c4c47a6c6a5eb39fe4b69 .toyplot-mark-popup");
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
      var axes = {"t347b0c2d6b91418f9bf5c74818718ed7": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "t63121211896a4b228749153bd5ce5f2a": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


You can also use the *gutter* argument to control the space between
cells in the grid:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(grid=(1, 2, 0), gutter=25)
    axes1.plot(y)
    axes2 = canvas.axes(grid=(1, 2, 1), gutter=25)
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="t2217250fe7e34c9286243264d7e2913b"><svg height="300.0px" id="t9b65ba3875a244bfa0801ed31fcd2aaa" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="ta4bd98ecbeba4c7a9877898abf653470"><clipPath id="t078d6a82e7cb42919bf73072ec7dfa69"><rect height="270.0" width="270.0" x="15.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t078d6a82e7cb42919bf73072ec7dfa69)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="15.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="t08fcdb7d802642a6b3631e7f3342d553" style="fill:none"><g class="toyplot-Series"><path d="M 25.0 275.0 L 37.5 274.30747922437678 L 50.0 272.22991689750694 L 62.5 268.7673130193906 L 75.0 263.91966759002764 L 87.5 257.6869806094183 L 100.0 250.06925207756234 L 112.5 241.06648199445985 L 125.0 230.6786703601108 L 137.5 218.90581717451525 L 150.0 205.74792243767311 L 162.5 191.20498614958447 L 175.0 175.27700831024933 L 187.5 157.96398891966763 L 200.0 139.26592797783937 L 212.5 119.18282548476454 L 225.0 97.714681440443243 L 237.5 74.861495844875392 L 250.0 50.623268698060976 L 262.5 25.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="175.0" y="35.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="220.0" y="42.0"></text></g><g class="toyplot-axes-Axis" id="t186d6149fcbc42298f494e5249685bb4" transform="translate(25.0,275.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="237.5" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="teadb1b4d972e428cb6161f0dc8c8df9c" transform="translate(25.0,275.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t4f6f8fcf1b6f4bc7a0aa39a8959aad5e"><clipPath id="tab33b5dc310a4d8e8cc93fdaab410728"><rect height="270.0" width="270.0" x="315.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tab33b5dc310a4d8e8cc93fdaab410728)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="315.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="t06198b023a744d98b38170c97db15a36" style="fill:none"><g class="toyplot-Series"><path d="M 325.0 25.0 L 337.5 25.692520775623262 L 350.0 27.770083102493075 L 362.5 31.232686980609415 L 375.0 36.080332409972307 L 387.5 42.313019390581722 L 400.0 49.930747922437654 L 412.5 58.933518005540179 L 425.0 69.321329639889186 L 437.5 81.094182825484751 L 450.0 94.252077562326889 L 462.5 108.79501385041551 L 475.0 124.72299168975069 L 487.5 142.03601108033237 L 500.0 160.73407202216066 L 512.5 180.81717451523545 L 525.0 202.28531855955674 L 537.5 225.13850415512462 L 550.0 249.37673130193903 L 562.5 275.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="475.0" y="35.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="520.0" y="42.0"></text></g><g class="toyplot-axes-Axis" id="t0e2f4f42c25e4f898627dd23aa2b065e" transform="translate(325.0,275.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="237.5" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="teaf3b5c58bf34481b2ad2ceedbe05d82" transform="translate(325.0,275.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t08fcdb7d802642a6b3631e7f3342d553", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t06198b023a744d98b38170c97db15a36", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t2217250fe7e34c9286243264d7e2913b .toyplot-mark-popup");
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
      var axes = {"t4f6f8fcf1b6f4bc7a0aa39a8959aad5e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 575.0, "min": 325.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}, "ta4bd98ecbeba4c7a9877898abf653470": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 275.0, "min": 25.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}};
    
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


Sometimes, particularly when embedding axes to produce a
figure-within-a-figure, the *corner* argument can be used to position
axes relative to one of eight "corner" positions within the canvas. The
corner argument takes a (position, inset, width, height) tuple:

.. code:: python

    x = numpy.random.normal(size=100)
    y = numpy.random.normal(size=100)

.. code:: python

    canvas = toyplot.Canvas(width="5in")
    canvas.axes().plot(numpy.linspace(0, 1) ** 0.5)
    canvas.axes(corner=("bottom-right", "1in", "1.5in", "1.5in")).scatterplot(x, y);



.. raw:: html

    <div align="center" class="toyplot" id="t70fb016036764685a36bc03feca7fc2a"><svg height="480.0px" id="t6f31001ed9404678802c8f701bd141ba" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 480.0 480.0" width="480.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t75dd653e44604012b348be68e9b7c1e9"><clipPath id="tb60b47cffd4243d5a6747f5293402040"><rect height="400.0" width="400.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb60b47cffd4243d5a6747f5293402040)" style="cursor:crosshair"><rect height="400.0" style="pointer-events:all;visibility:hidden" width="400.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t26cb7aa0c8474d2fbaac899097908e31" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 430.0 L 57.600000000000001 375.71428571428578 L 65.200000000000003 353.228406614032 L 72.799999999999997 335.97438473197525 L 80.400000000000006 321.42857142857144 L 88.0 308.61345265001137 L 95.599999999999994 297.02769967748463 L 103.2 286.37350025649368 L 110.8 276.45681322806394 L 118.39999999999999 267.14285714285711 L 126.0 258.33349844800227 L 133.59999999999999 249.95465423784975 L 141.19999999999999 241.94876946395047 L 148.80000000000001 234.27007361766917 L 156.40000000000001 226.88145614655744 L 164.0 219.75233263445455 L 171.59999999999999 212.85714285714289 L 179.20000000000002 206.17426603789841 L 186.79999999999998 199.68521984209599 L 194.40000000000001 193.37405735064914 L 202.0 187.22690530002285 L 209.59999999999999 181.23160513096869 L 217.19999999999999 175.37743018101384 L 224.80000000000001 169.65486016302384 L 232.40000000000001 164.05539935496921 L 240.0 158.57142857142856 L 247.59999999999999 153.19608354782028 L 255.20000000000002 147.92315419592572 L 262.80000000000001 142.74700051298731 L 270.39999999999998 137.66248189841266 L 278.0 132.66489735433839 L 285.60000000000002 127.74993458922738 L 293.19999999999999 122.91362645612796 L 300.80000000000001 118.1523134736499 L 308.40000000000003 113.46261142268371 L 316.0 108.8413832031637 L 323.59999999999997 104.28571428571431 L 331.19999999999999 99.792891212382386 L 338.80000000000001 95.360382695969861 L 346.40000000000003 90.985822944086976 L 354.0 86.666996896004548 L 361.59999999999997 82.401827110788219 L 369.19999999999999 78.188362086430459 L 376.80000000000001 74.024765823605691 L 384.39999999999998 69.909308475699476 L 392.0 65.840357950034274 L 399.60000000000002 61.81637234462832 L 407.19999999999999 57.835893121086208 L 414.80000000000001 53.897538927900932 L 422.39999999999998 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="330.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="375.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tc7d56467dc4d452da87212a8d47dbb3f" transform="translate(50.0,430.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="372.4" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(76.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(152.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(228.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(304.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(380.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">50</tspan></text></g></g><g class="toyplot-axes-Axis" id="tbec1dd8fed074002bf96ebea765fdc10" transform="translate(50.0,430.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="380.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(190.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(380.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t6c0cd6932a2e492a92e43e462b454cd6"><clipPath id="te85f74151ebd448a9cea6914777d3240"><rect height="164.0" width="164.0" x="230.0" y="230.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te85f74151ebd448a9cea6914777d3240)" style="cursor:crosshair"><rect height="164.0" style="pointer-events:all;visibility:hidden" width="164.0" x="230.0" y="230.0"></rect><g class="toyplot-mark-Scatterplot" id="t7b596d1f447146cbbd45ad06800d95e4" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.97229273132155" cy="299.90607514438756" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.54906969621413" cy="267.30716505847039" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="304.54049822896809" cy="252.80129205616078" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="299.47567265052078" cy="254.43324862476936" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="296.82047158540058" cy="270.11675894328027" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="309.97252134748351" cy="308.30331234688629" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="309.77672726472622" cy="319.15402634186023" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="291.50967707291153" cy="259.07739213004038" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="291.45799538644371" cy="329.70005460949443" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="286.25263791359066" cy="370.41160932761977" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="299.83062688490622" cy="309.4247922595697" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="330.35024539982641" cy="384.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="317.75615377941034" cy="301.22445911382817" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="290.84408656943236" cy="321.2637035000788" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="330.34413952628228" cy="314.32343216176122" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="331.94268009113534" cy="267.49227875535661" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="384.0" cy="286.50683356044419" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="336.80555459898039" cy="334.49295758486704" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="308.07273726762003" cy="300.36976384489293" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="270.33227852079142" cy="297.11248669496229" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="290.9422188644225" cy="350.81530484090553" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="334.45691821901937" cy="264.43019790287639" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="317.77245250257045" cy="329.20905520484519" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="302.62612779768233" cy="263.04460163835387" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.73094446564517" cy="307.7296552816606" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="298.44220654125257" cy="369.50785741882112" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="338.42624003054084" cy="354.1741900007371" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="283.56464676754098" cy="342.20710716441147" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="365.45569265096418" cy="294.18520269351177" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="338.78460889366266" cy="269.46375644849081" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="288.80404037637163" cy="254.96091421649032" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="257.2503034640564" cy="247.92679957756141" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.46584361892735" cy="314.71669840186667" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="343.11701484573325" cy="340.35689502699677" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="335.8577344715867" cy="332.92009085569907" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="314.72815667388335" cy="339.84441277219992" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="267.75886962779504" cy="286.87295350751742" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="362.01722912436628" cy="377.44144601792283" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.03765524712458" cy="338.58492251531538" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="312.48854596573966" cy="282.37451180863826" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="287.76665543624881" cy="283.53136821110149" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="344.65626857456283" cy="366.57559129097137" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="271.96074781346312" cy="339.42324275817401" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="300.96619926636151" cy="300.20056005746318" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="290.71985664486738" cy="326.06841425045013" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.417513761073" cy="308.11408754218121" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="344.80068807553948" cy="298.45048600824714" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="257.44194246348286" cy="332.75661284758303" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="298.9009144931938" cy="309.68595483445523" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="272.04861598036894" cy="273.97670037993385" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="263.7848784936221" cy="275.23356857995009" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.41465137801464" cy="306.31872206139684" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="307.94659996833661" cy="297.37252319648712" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="318.10574332002841" cy="310.51263157425848" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="311.34432749695583" cy="295.97850298803132" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="330.13387213396726" cy="308.24569970527239" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="327.22032974323201" cy="286.69311906283838" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="299.83980248160549" cy="331.74936049178257" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="311.523032289561" cy="337.61626406602477" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.35292373978956" cy="274.02591063470163" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="293.71868525500577" cy="288.96103907185477" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="313.70788479376006" cy="379.2006671682027" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="285.18767612866827" cy="334.06314319315135" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="287.67258924088088" cy="371.31682930639579" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.21955737805558" cy="310.7590049938201" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.39160836455312" cy="293.81747266687773" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="296.95393610563701" cy="307.29440166338168" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="258.32173625137409" cy="305.82930690271689" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.18258086493694" cy="260.59508629086201" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="266.64012903126229" cy="320.60655283396608" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="290.43195434975655" cy="274.76019505701021" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="311.18669956828705" cy="338.77129292542156" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="277.81866055015462" cy="294.72211234453368" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="288.5539640577299" cy="307.34391947533538" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="299.48109801107591" cy="268.24110088301336" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.84132089432444" cy="263.10548979932531" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="323.87007503027542" cy="311.50042846402152" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="334.46716859799824" cy="317.98321446191761" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="346.81074036503321" cy="307.88306441365148" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.50921872614123" cy="355.39957077798169" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="290.06775753794579" cy="276.07059931165094" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.04515108550163" cy="276.74820288342357" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.63642828275653" cy="309.99775595958363" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.37875634910807" cy="291.77205133787879" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.70836989270464" cy="322.82612070191823" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.90546878117971" cy="245.39549639232638" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="344.42440483884889" cy="258.15452927323179" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="292.64210478749357" cy="284.33127094860043" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="315.82886328177653" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="321.25538021520526" cy="275.04351017297262" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="278.92554329866977" cy="271.54660734829264" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="319.39365527780978" cy="268.60174513263672" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="344.32415751931927" cy="329.00332674080983" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="324.45664695571247" cy="297.0645184574629" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="326.30216660357701" cy="313.7367918907949" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="309.77139738099447" cy="272.07162715585957" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="320.28996409554486" cy="329.40880806409263" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="291.13933221363993" cy="314.6894190038783" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="290.78970680583689" cy="319.14891064849974" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="278.85124410555557" cy="329.96841360444159" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="284.0" y="250.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="329.0" y="257.0"></text></g><g class="toyplot-axes-Axis" id="t04df5d07890843ea9252d8cb035a66f9" transform="translate(240.0,384.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="144.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(2.315923193401521,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-2</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(67.3238476593506,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(132.33177212529966,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">2</tspan></text></g></g><g class="toyplot-axes-Axis" id="t16e08261e8e74004b69fa8df8f534511" transform="translate(240.0,384.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="138.60450360767362" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(14.395912729561958,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-2</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(46.79693454717147,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-1</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(79.19795636478096,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(111.59897818239048,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">2</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.14285714285714285, 0.20203050891044214, 0.24743582965269675, 0.2857142857142857, 0.3194382824999699, 0.3499271061118826, 0.3779644730092272, 0.40406101782088427, 0.42857142857142855, 0.4517539514526256, 0.4738035414793428, 0.4948716593053935, 0.5150787536377127, 0.5345224838248488, 0.5532833351724881, 0.5714285714285714, 0.5890150893739515, 0.6060915267313264, 0.6226998490772391, 0.6388765649999398, 0.6546536707079771, 0.6700593942604899, 0.6851187890446742, 0.6998542122237652, 0.7142857142857143, 0.7284313590846835, 0.7423074889580902, 0.7559289460184544, 0.769309258162072, 0.7824607964359516, 0.7953949089757174, 0.8081220356417685, 0.8206518066482897, 0.8329931278350429, 0.8451542547285166, 0.8571428571428571, 0.8689660757568884, 0.8806305718527109, 0.8921425711997711, 0.9035079029052512, 0.9147320339189784, 0.9258200997725514, 0.9367769320431429, 0.9476070829586856, 0.9583148474999098, 0.9689042833036097, 0.9793792286287205, 0.989743318610787, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t26cb7aa0c8474d2fbaac899097908e31", "filename": "toyplot"}, {"data": [[-1.590250545135034, 0.3163161300885681, -0.10703885154187694, -0.30181608908851865, -0.40392675816975154, 0.10185964672354082, 0.09433002305205265, -0.6081631861175054, -0.6101507009817435, -0.8103323525117684, -0.2881656673398833, 0.8855227239464067, 0.40119363161348753, -0.6337597002712433, 0.885287911283403, 0.9467627460049126, 2.948723289143468, 1.1337735815220595, 0.02879993533179644, -1.4225792256271497, -0.6299858413226492, 1.043452424553294, 0.4018204291652477, -0.18065950806231887, 0.13102621081523816, -0.3415599402327544, 1.196100038060806, -0.913704024816798, 2.2355676430672253, 1.2098817756745606, -0.7122134507109034, -1.925670778088084, 0.12083126731813021, 1.3764924615125564, 1.0973234050558733, 0.2847464011257236, -1.5215444254138424, 2.10333516699429, 1.1426994413326488, 0.19861802806419057, -0.7521080077454941, 1.4356873112741377, -1.359953426309225, -0.24449513060208589, -0.6385371918457555, -0.3809663967762285, 1.4412412303602757, -1.9183009458329847, -0.3239194773311343, -1.3565742933947516, -1.6743716063621614, 1.1571975249888764, 0.023949092133844115, 0.4146377441386136, 0.1546149900429132, 0.8772016897172481, 0.7651560270280235, -0.2878128027939599, 0.1614874134464138, 1.6547627244651333, -0.5232116898098783, 0.2455099584725778, -0.8512874281302873, -0.7557254973108303, 0.34210097429600694, -0.0743078367241821, -0.3987941331346964, -1.8844668481010993, 0.10993787407732575, -1.5645676647236408, -0.6496090072234952, 0.1485531164342826, -1.1346765548810391, -0.7218305981854667, -0.3016074468114548, 1.3274332905772877, 0.6363157840699741, 1.0438466218401277, 1.5185415097495438, -1.6080589126911642, -0.6636148693857878, -0.08763149233608276, 0.1273914161473145, 0.3097664152459072, -0.062126186150279476, -1.0544244837616894, 1.4267705623693407, -0.5646135833619514, -2.5890631108602227, 0.5357628577709753, -1.0921093310537775, 0.46416678111225296, 1.4229153662392842, 0.6588734926207335, 0.7298463648907598, 0.09412505251286285, 0.49863599486959004, -0.6224054828187934, -0.6358509746828718, -1.0949666439784924], [0.15110537310803532, 1.157212843095296, 1.6049108534841505, 1.5545434120560635, 1.0704997171752093, -0.10806044116066571, -0.4429484596945986, 1.4112101699313673, -0.7684328943213671, -2.024922734280648, -0.14267292711856172, -2.4443042818402096, 0.11041579310460148, -0.5080598987749533, -0.293860748594277, 1.1514996375696103, 0.5646491699478324, -0.916357333320625, 0.13679444479486136, 0.237324519687757, -1.4201175958185026, 1.2460053253752967, -0.7532790696237013, 1.288769293509458, -0.09035553455448347, -1.9970300365167915, -1.5237836214993998, -1.154440861147883, 0.3276699420614307, 1.0906534795616332, 1.538257950607, 1.7553534076121855, -0.3059982127248578, -1.0973373491713192, -0.8678135948539212, -1.0815204944535395, 0.5533495279447441, -2.2418861599983653, -1.0426485643034822, 0.6921859425554208, 0.6564816240627698, -1.9065308496591704, -1.0685218298929953, 0.14201661921831826, -0.6563487637810589, -0.10222035359274148, 0.1960295469299018, -0.8627681364410262, -0.1507332462145333, 0.951369479296236, 0.9125784742751196, -0.046809586275256, 0.22929895484635757, -0.1762471557590151, 0.27232291305060674, -0.10628232928696729, 0.5588997987260607, -0.8316810811786808, -1.0127526414297123, 0.949850692171411, 0.48890447506673634, -2.296181396740675, -0.9030918753935512, -2.052860741417324, -0.18385103383880227, 0.3390192763109504, -0.07692220455862632, -0.03170465651609676, 1.3643692348100924, -0.48777811044704494, 0.9271883074342266, -1.048400556051004, 0.31109917913783236, -0.07845048388982821, 1.1283885723732103, 1.2868900885475232, -0.20673375261153124, -0.40681343017196947, -0.09509023498629288, -1.5616028231326826, 0.8867450071575506, 0.865831976217137, -0.1603564342387743, 0.40214757332926354, -0.5562811311371476, 1.8334775852842389, 1.4396926931679346, 0.6317940465535875, -0.3403232067380233, 0.9184442894968529, 1.0263699853086885, 1.1172579280480568, -0.7469296259180858, 0.23880497415519533, -0.27575513839875204, 1.0101661812891014, -0.7594440868991412, -0.3051562825492625, -0.44279057290358137, -0.7767153181429912]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t7b596d1f447146cbbd45ad06800d95e4", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t70fb016036764685a36bc03feca7fc2a .toyplot-mark-popup");
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
      var axes = {"t6c0cd6932a2e492a92e43e462b454cd6": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.948723289143468, "min": -2.5890631108602227}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 384.0, "min": 240.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": -2.4443042818402096}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 240.0, "min": 384.0}, "scale": "linear"}]}, "t75dd653e44604012b348be68e9b7c1e9": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 430.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 430.0}, "scale": "linear"}]}};
    
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


Here are all the positions supported by the *corner* argument:

.. code:: python

    canvas = toyplot.Canvas(width="12cm")
    for position in [
        "top-left",
        "top",
        "top-right",
        "right",
        "bottom-right",
        "bottom",
        "bottom-left",
        "left",
        ]:
        canvas.axes(corner=(position, "1cm", "2cm", "2cm"), label=position)



.. raw:: html

    <div align="center" class="toyplot" id="ta0eee5f2248e451097adb452d92a3921"><svg height="453.5433072px" id="t7b993abd1a71451eb6cda09c93252a66" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 453.5433072 453.5433072" width="453.5433072px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tb27f6a4239e6432d888aaa3bfb5e7967"><clipPath id="tdfd5e058fb1143e7862a6703e4bbf0da"><rect height="95.59055120000002" width="95.59055120000002" x="27.795275600000004" y="27.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tdfd5e058fb1143e7862a6703e4bbf0da)" style="cursor:crosshair"><rect height="95.59055120000002" style="pointer-events:all;visibility:hidden" width="95.59055120000002" x="27.795275600000004" y="27.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="54.795275600000004"></text></g><g class="toyplot-axes-Axis" id="t81a02ef7a2fb4a628598cf02cb6d0f9c" transform="translate(37.7952756,113.3858268) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="te87392332e1a41428ea891642cacdc56" transform="translate(37.7952756,113.3858268) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(75.59055120000001,37.795275600000004)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">top-left</tspan></text></g><g class="toyplot-axes-Cartesian" id="t1e3fc7251c2a417a816d9091be6364ba"><clipPath id="tef0afca1b9d5457a8a1129eb99ca8156"><rect height="95.59055120000002" width="95.5905512" x="178.976378" y="27.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tef0afca1b9d5457a8a1129eb99ca8156)" style="cursor:crosshair"><rect height="95.59055120000002" style="pointer-events:all;visibility:hidden" width="95.5905512" x="178.976378" y="27.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="164.5669292" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="209.5669292" y="54.795275600000004"></text></g><g class="toyplot-axes-Axis" id="t034e3dd7a2264881b61aa7ad5f535e68" transform="translate(188.976378,113.3858268) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t8e36d6d3d4e64b9f913fb40083620b24" transform="translate(188.976378,113.3858268) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(226.7716536,37.795275600000004)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">top</tspan></text></g><g class="toyplot-axes-Cartesian" id="t9fc8df0ef54043659e6575a9108942e3"><clipPath id="t0611c861bc36473c80e1b8f0385aa8b8"><rect height="95.59055120000002" width="95.5905512" x="330.1574804" y="27.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t0611c861bc36473c80e1b8f0385aa8b8)" style="cursor:crosshair"><rect height="95.59055120000002" style="pointer-events:all;visibility:hidden" width="95.5905512" x="330.1574804" y="27.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="315.7480316" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.7480316" y="54.795275600000004"></text></g><g class="toyplot-axes-Axis" id="t8efd09d597aa42aca96849aa24b1dc8c" transform="translate(340.1574804,113.3858268) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t522d660d83cf443298e61beae716215d" transform="translate(340.1574804,113.3858268) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(377.952756,37.795275600000004)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">top-right</tspan></text></g><g class="toyplot-axes-Cartesian" id="te18c362e586947639323a15a26c38eeb"><clipPath id="tda1144fe8cde42819bc7d5750bf39adf"><rect height="95.5905512" width="95.5905512" x="330.1574804" y="178.976378"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tda1144fe8cde42819bc7d5750bf39adf)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.5905512" x="330.1574804" y="178.976378"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="315.7480316" y="198.976378"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.7480316" y="205.976378"></text></g><g class="toyplot-axes-Axis" id="t47ab99a7580c4f00bd91c4600f81cc82" transform="translate(340.1574804,264.5669292) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t5de8ad9f049547f499d307ecd9d7f4fb" transform="translate(340.1574804,264.5669292) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(377.952756,188.976378)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">right</tspan></text></g><g class="toyplot-axes-Cartesian" id="tf59f57e0cfbb4f0592409f04d2663d51"><clipPath id="tf001479587be485fa4b88fe8c0a55540"><rect height="95.5905512" width="95.5905512" x="330.1574804" y="330.1574804"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf001479587be485fa4b88fe8c0a55540)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.5905512" x="330.1574804" y="330.1574804"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="315.7480316" y="350.1574804"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.7480316" y="357.1574804"></text></g><g class="toyplot-axes-Axis" id="tc4cc6fb987164b18a2d76ce9f1b6b52c" transform="translate(340.1574804,415.7480316) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="tdf4b86e38da34e60b3fa1a0ebec7bc40" transform="translate(340.1574804,415.7480316) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(377.952756,340.1574804)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">bottom-right</tspan></text></g><g class="toyplot-axes-Cartesian" id="tf8b46ae49baa46aea68893d4a0fb1805"><clipPath id="t7ba3f4f80e5b4752a20816bc57bbb90c"><rect height="95.5905512" width="95.5905512" x="178.976378" y="330.1574804"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t7ba3f4f80e5b4752a20816bc57bbb90c)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.5905512" x="178.976378" y="330.1574804"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="164.5669292" y="350.1574804"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="209.5669292" y="357.1574804"></text></g><g class="toyplot-axes-Axis" id="t7375de2586e449fe8a10c03293303d50" transform="translate(188.976378,415.7480316) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="tbc2d7773c48248688e542249f3391a9b" transform="translate(188.976378,415.7480316) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(226.7716536,340.1574804)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">bottom</tspan></text></g><g class="toyplot-axes-Cartesian" id="tb1766c8b66fc41b8a1d75b6ee419cd1d"><clipPath id="t8211db09edf243e29245f6d49d644a4c"><rect height="95.5905512" width="95.59055120000002" x="27.795275600000004" y="330.1574804"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t8211db09edf243e29245f6d49d644a4c)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.59055120000002" x="27.795275600000004" y="330.1574804"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="350.1574804"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="357.1574804"></text></g><g class="toyplot-axes-Axis" id="t1fc01f99dd1d4dcabec7b1627948e86b" transform="translate(37.7952756,415.7480316) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="tb5637e8359d54171b64d1471aae8b3a5" transform="translate(37.7952756,415.7480316) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(75.59055120000001,340.1574804)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">bottom-left</tspan></text></g><g class="toyplot-axes-Cartesian" id="tba9aa66efd014b9d9f6b73c29f6353ae"><clipPath id="teaedb1ea0c0c4d75a2d1253371917f18"><rect height="95.5905512" width="95.59055120000002" x="27.795275600000004" y="178.976378"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#teaedb1ea0c0c4d75a2d1253371917f18)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.59055120000002" x="27.795275600000004" y="178.976378"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="198.976378"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="205.976378"></text></g><g class="toyplot-axes-Axis" id="tf359d3cdd2ee444395a03f6b7db1e78a" transform="translate(37.7952756,264.5669292) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t9024e2514e204bd2bcf4bd90fbc05dbd" transform="translate(37.7952756,264.5669292) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(75.59055120000001,188.976378)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">left</tspan></text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"t1e3fc7251c2a417a816d9091be6364ba": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 264.5669292, "min": 188.976378}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 37.795275600000004, "min": 113.38582680000002}, "scale": "linear"}]}, "t9fc8df0ef54043659e6575a9108942e3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 415.7480316, "min": 340.1574804}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 37.795275600000004, "min": 113.38582680000002}, "scale": "linear"}]}, "tb1766c8b66fc41b8a1d75b6ee419cd1d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 113.38582680000002, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 340.1574804, "min": 415.7480316}, "scale": "linear"}]}, "tb27f6a4239e6432d888aaa3bfb5e7967": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 113.38582680000002, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 37.795275600000004, "min": 113.38582680000002}, "scale": "linear"}]}, "tba9aa66efd014b9d9f6b73c29f6353ae": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 113.38582680000002, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 188.976378, "min": 264.5669292}, "scale": "linear"}]}, "te18c362e586947639323a15a26c38eeb": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 415.7480316, "min": 340.1574804}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 188.976378, "min": 264.5669292}, "scale": "linear"}]}, "tf59f57e0cfbb4f0592409f04d2663d51": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 415.7480316, "min": 340.1574804}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 340.1574804, "min": 415.7480316}, "scale": "linear"}]}, "tf8b46ae49baa46aea68893d4a0fb1805": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 264.5669292, "min": 188.976378}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 340.1574804, "min": 415.7480316}, "scale": "linear"}]}};
    
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


