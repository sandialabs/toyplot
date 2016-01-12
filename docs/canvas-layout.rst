
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

    <div align="center" class="toyplot" id="t7cbb4174b1464077bc483e67de823ac0"><svg height="300.0px" id="t1ade833eff8c4412a2a3128fe763b98d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t6db34a4269ab4bd180a1f263031908d7"><clipPath id="tcd3d304305ba42e692ca9c46d4e10f7f"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tcd3d304305ba42e692ca9c46d4e10f7f)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t4f15694b6b9a446484eef18d9c20f2cc" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tc37d11439d954e4a95d087ad483a39cd" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t1dda0c42aedf4e7bb2e2a5dfa83bfeb0" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t4f15694b6b9a446484eef18d9c20f2cc", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t7cbb4174b1464077bc483e67de823ac0 .toyplot-mark-popup");
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
      var axes = {"t6db34a4269ab4bd180a1f263031908d7": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t2b62ab8a6b8e4fe99a73b8757222cb03"><svg height="300.0px" id="t220e432c35994759a97d9729e38c3b24" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td06445d84cbc432684b7571d24de6c2c"><clipPath id="t088a2f0ceda44ed9bd0881061fd9bfb4"><rect height="260.0" width="260.0" x="20.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t088a2f0ceda44ed9bd0881061fd9bfb4)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="20.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="t49a1e2e4b4114384a23aeecdddd96611" style="fill:none"><g class="toyplot-Series"><path d="M 30.0 270.0 L 42.0 269.33518005540168 L 54.0 267.34072022160666 L 66.0 264.016620498615 L 78.0 259.36288088642664 L 90.0 253.37950138504155 L 102.0 246.06648199445985 L 114.0 237.42382271468145 L 126.0 227.45152354570638 L 138.0 216.14958448753464 L 150.0 203.51800554016617 L 162.0 189.55678670360109 L 174.0 174.26592797783934 L 186.0 157.64542936288092 L 198.0 139.6952908587258 L 210.0 120.41551246537395 L 222.0 99.806094182825504 L 234.0 77.867036011080387 L 246.0 54.598337950138536 L 258.0 30.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="170.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="215.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="ta02c7c2556404874ba6187735bab34a4" transform="translate(30.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t7a33e0b7d72f46088296f215aa9a0300" transform="translate(30.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t7234a537d96f4f8ebf93b776dd48ea0a"><clipPath id="t2c8b0e5387ac4d7c89457b33e1b75f34"><rect height="260.0" width="260.0" x="320.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2c8b0e5387ac4d7c89457b33e1b75f34)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="320.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="t92092cfe5fe2452395ef17e2e7d9a273" style="fill:none"><g class="toyplot-Series"><path d="M 330.0 30.0 L 342.0 30.664819944598332 L 354.0 32.659279778393355 L 366.0 35.983379501385038 L 378.0 40.637119113573412 L 390.0 46.62049861495845 L 402.0 53.933518005540151 L 414.0 62.576177285318565 L 426.0 72.54847645429362 L 438.0 83.850415512465361 L 450.0 96.4819944598338 L 462.0 110.44321329639889 L 474.0 125.73407202216066 L 486.0 142.35457063711908 L 498.0 160.3047091412742 L 510.0 179.58448753462605 L 522.0 200.19390581717448 L 534.0 222.13296398891964 L 546.0 245.40166204986147 L 558.0 270.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="470.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="515.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="tbfd5a395d3c245098f24eead322744e8" transform="translate(330.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tf3a5ba6bf0a74fc280e092d59d6c7cad" transform="translate(330.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t49a1e2e4b4114384a23aeecdddd96611", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t92092cfe5fe2452395ef17e2e7d9a273", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t2b62ab8a6b8e4fe99a73b8757222cb03 .toyplot-mark-popup");
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
      var axes = {"t7234a537d96f4f8ebf93b776dd48ea0a": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 570.0, "min": 330.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}, "td06445d84cbc432684b7571d24de6c2c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 270.0, "min": 30.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t7916e390529d433baa5e1f111bc7a5d2"><svg height="300.0px" id="t74fdc7aed12d487b8ceb10c5909776df" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t3798ad5f5e23479193171db57c28f843"><clipPath id="t77aba9f4357e498ebb3270d6aadf6467"><rect height="260.0" width="260.0" x="20.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t77aba9f4357e498ebb3270d6aadf6467)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="20.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="t4195aab021e34af6b2dc9051df1c4d18" style="fill:none"><g class="toyplot-Series"><path d="M 30.0 270.0 L 42.0 269.33518005540168 L 54.0 267.34072022160666 L 66.0 264.016620498615 L 78.0 259.36288088642664 L 90.0 253.37950138504155 L 102.0 246.06648199445985 L 114.0 237.42382271468145 L 126.0 227.45152354570638 L 138.0 216.14958448753464 L 150.0 203.51800554016617 L 162.0 189.55678670360109 L 174.0 174.26592797783934 L 186.0 157.64542936288092 L 198.0 139.6952908587258 L 210.0 120.41551246537395 L 222.0 99.806094182825504 L 234.0 77.867036011080387 L 246.0 54.598337950138536 L 258.0 30.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="170.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="215.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="t9f5ec23d2d534f55a6f20b3f519d540d" transform="translate(30.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t020111c87cd14f5fa6d91598b24bfeca" transform="translate(30.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t811baafdb6564a11b07e01f147366252"><clipPath id="t1910b870647c48f7b5be76fce98f2025"><rect height="260.0" width="260.0" x="320.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t1910b870647c48f7b5be76fce98f2025)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="320.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="t06df1d4119cb4a6daadd4e7b653e0c9d" style="fill:none"><g class="toyplot-Series"><path d="M 330.0 30.0 L 342.0 30.664819944598332 L 354.0 32.659279778393355 L 366.0 35.983379501385038 L 378.0 40.637119113573412 L 390.0 46.62049861495845 L 402.0 53.933518005540151 L 414.0 62.576177285318565 L 426.0 72.54847645429362 L 438.0 83.850415512465361 L 450.0 96.4819944598338 L 462.0 110.44321329639889 L 474.0 125.73407202216066 L 486.0 142.35457063711908 L 498.0 160.3047091412742 L 510.0 179.58448753462605 L 522.0 200.19390581717448 L 534.0 222.13296398891964 L 546.0 245.40166204986147 L 558.0 270.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="470.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="515.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="t44ab05f2e1d145e38fe9e9b006c70e98" transform="translate(330.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t1739bc0a4e4d410bbe5a03564a1fbd84" transform="translate(330.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t4195aab021e34af6b2dc9051df1c4d18", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t06df1d4119cb4a6daadd4e7b653e0c9d", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t7916e390529d433baa5e1f111bc7a5d2 .toyplot-mark-popup");
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
      var axes = {"t3798ad5f5e23479193171db57c28f843": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 270.0, "min": 30.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}, "t811baafdb6564a11b07e01f147366252": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 570.0, "min": 330.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t1eda48b561ec47e896d05e2a4d978e1e"><svg height="192.0px" id="t6181477434bf4791b9be5eeb2397653b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 755.9055119999999 192.0" width="755.9055119999999px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t0463518cf5fa4c76b221c45dd20d830b"><clipPath id="t14549237cb3f419c8db5d982278609b4"><rect height="154.40000000000003" width="171.1811024" x="27.795275600000004" y="9.200000000000003"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t14549237cb3f419c8db5d982278609b4)" style="cursor:crosshair"><rect height="154.40000000000003" style="pointer-events:all;visibility:hidden" width="171.1811024" x="27.795275600000004" y="9.200000000000003"></rect><g class="toyplot-mark-Plot" id="t169682c84daf4fbcbf0343c4d0ce5672" style="fill:none"><g class="toyplot-Series"><path d="M 37.795275600000004 153.60000000000002 L 45.35433072 153.22770083102495 L 52.913385840000004 152.11080332409975 L 60.47244096 150.2493074792244 L 68.031496079999997 147.6432132963989 L 75.590551199999993 144.29252077562327 L 83.149606320000004 140.19722991689756 L 90.708661439999986 135.3573407202216 L 98.267716559999997 129.77285318559558 L 105.82677168000001 123.44376731301942 L 113.38582679999999 116.3700831024931 L 120.94488192 108.55180055401662 L 128.50393703999998 99.988919667590054 L 136.06299215999999 90.681440443213333 L 143.62204727999998 80.629362880886447 L 151.18110239999999 69.832686980609424 L 158.74015752 58.291412742382292 L 166.29921263999998 46.005540166205023 L 173.85826775999999 32.975069252077589 L 181.41732287999997 19.200000000000003" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="88.97637799999998" y="29.200000000000003"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="133.97637799999998" y="36.2"></text></g><g class="toyplot-axes-Axis" id="t0fdd6ab6900a472da09a8c95f4aa79ed" transform="translate(37.7952756,153.6) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="143.62204727999998" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(113.38582679999999,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(151.1811024,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t0c81a1b1cae1413e8631553031106749" transform="translate(37.7952756,153.6) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="134.40000000000003" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(67.20000000000002,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(134.40000000000003,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t44d785a2564f4cc4bbf44efd86361673"><clipPath id="t88f62ef9d3184022a9d046ba64ccd1fb"><rect height="154.40000000000003" width="511.3385827999999" x="216.7716536" y="9.200000000000003"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t88f62ef9d3184022a9d046ba64ccd1fb)" style="cursor:crosshair"><rect height="154.40000000000003" style="pointer-events:all;visibility:hidden" width="511.3385827999999" x="216.7716536" y="9.200000000000003"></rect><g class="toyplot-mark-Plot" id="te1df9f8b52274e7581348df45b81989c" style="fill:none"><g class="toyplot-Series"><path d="M 226.77165360000001 19.200000000000003 L 251.33858273999999 19.572299168975068 L 275.90551188000001 20.689196675900281 L 300.47244102000002 22.550692520775623 L 325.03937016000003 25.156786703601114 L 349.60629929999999 28.507479224376734 L 374.17322844 32.602770083102492 L 398.74015757999996 37.442659279778404 L 423.30708672000003 43.027146814404432 L 447.87401585999999 49.356232686980618 L 472.440945 56.429916897506935 L 497.00787414000001 64.248199445983389 L 521.57480327999997 72.811080332409972 L 546.14173241999993 82.118559556786693 L 570.70866155999988 92.170637119113579 L 595.27559069999995 102.9673130193906 L 619.84251984000002 114.50858725761772 L 644.40944897999998 126.794459833795 L 668.97637811999994 139.82493074792245 L 693.54330726000001 153.60000000000002" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="618.1102364" y="29.200000000000003"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="663.1102364" y="36.2"></text></g><g class="toyplot-axes-Axis" id="tf49e8e6d393e4d93be52e243e5fdb17e" transform="translate(226.7716536,153.6) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="466.7716536599999" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(122.83464569999998,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.66929139999996,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(368.5039370999999,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(491.3385827999999,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t4458041d4dd5459e83958ac2c24924ea" transform="translate(226.7716536,153.6) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="134.40000000000003" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(67.20000000000002,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(134.40000000000003,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t169682c84daf4fbcbf0343c4d0ce5672", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "te1df9f8b52274e7581348df45b81989c", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t1eda48b561ec47e896d05e2a4d978e1e .toyplot-mark-popup");
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
      var axes = {"t0463518cf5fa4c76b221c45dd20d830b": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 188.97637799999998, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 19.200000000000003, "min": 153.60000000000002}, "scale": "linear"}]}, "t44d785a2564f4cc4bbf44efd86361673": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 718.1102364, "min": 226.7716536}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 19.200000000000003, "min": 153.60000000000002}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t5ec6c075ffbd4fbc84f5090eed6faa2c"><svg height="300.0px" id="te48aa860aacf4e9d8e3b4789c327ec73" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc6a56978284143d09dfe24c0d436bf8d"><clipPath id="t93ba42bed403421a8b3f41db290be1cb"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t93ba42bed403421a8b3f41db290be1cb)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t5582b22b609a45dab00ca37b988379ef" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t3239dc3b8268475aab1902a194479802" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t215fe7d14ee04d559588b6a82e750e93" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="t970e8fbc254941728bbc94c5b496e33f"><clipPath id="tff3ce03ddce94bffb284c95998c5dc06"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tff3ce03ddce94bffb284c95998c5dc06)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t9a5bc0d2e1944d58bbcc8125235f9405" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 50.0 L 360.0 50.554016620498615 L 370.0 52.21606648199446 L 380.0 54.986149584487535 L 390.0 58.86426592797784 L 400.0 63.850415512465375 L 410.0 69.944598337950126 L 420.0 77.146814404432135 L 430.0 85.45706371191136 L 440.0 94.875346260387801 L 450.0 105.4016620498615 L 460.0 117.03601108033241 L 470.0 129.77839335180056 L 480.0 143.62880886426589 L 490.0 158.58725761772851 L 500.0 174.65373961218839 L 510.0 191.82825484764541 L 520.0 210.11080332409966 L 530.0 229.50138504155123 L 540.0 250.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tb4ef6232fa274c1a961ec8ead96c3f3e" transform="translate(350.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t96f51c3fe23a4bdbae387e07d9f6b054" transform="translate(350.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t5582b22b609a45dab00ca37b988379ef", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t9a5bc0d2e1944d58bbcc8125235f9405", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t5ec6c075ffbd4fbc84f5090eed6faa2c .toyplot-mark-popup");
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
      var axes = {"t970e8fbc254941728bbc94c5b496e33f": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "tc6a56978284143d09dfe24c0d436bf8d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t15bb6fbd35294e7b840ddd50a2f5f950"><svg height="300.0px" id="te174d449df924336aff7cf5fef1092b7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t7d36420d64164ca59c6f799a24bce5ba"><clipPath id="t68280e0e776142aca29d5b6069152300"><rect height="270.0" width="270.0" x="15.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t68280e0e776142aca29d5b6069152300)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="15.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="t176e3a7327f0495abb78c8fe5f104c11" style="fill:none"><g class="toyplot-Series"><path d="M 25.0 275.0 L 37.5 274.30747922437678 L 50.0 272.22991689750694 L 62.5 268.7673130193906 L 75.0 263.91966759002764 L 87.5 257.6869806094183 L 100.0 250.06925207756234 L 112.5 241.06648199445985 L 125.0 230.6786703601108 L 137.5 218.90581717451525 L 150.0 205.74792243767311 L 162.5 191.20498614958447 L 175.0 175.27700831024933 L 187.5 157.96398891966763 L 200.0 139.26592797783937 L 212.5 119.18282548476454 L 225.0 97.714681440443243 L 237.5 74.861495844875392 L 250.0 50.623268698060976 L 262.5 25.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="175.0" y="35.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="220.0" y="42.0"></text></g><g class="toyplot-axes-Axis" id="t49606f6370f44a0ba856fac5b6a17dd1" transform="translate(25.0,275.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="237.5" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t244187af2c4d4ba5bbc01fb5156cf44d" transform="translate(25.0,275.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="tf714f386478f4899a133dc091e3c2893"><clipPath id="t5e0e2b3d703f4324abb0aba149f47142"><rect height="270.0" width="270.0" x="315.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t5e0e2b3d703f4324abb0aba149f47142)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="315.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="tf76676abf58344799458a9f0c1f25fea" style="fill:none"><g class="toyplot-Series"><path d="M 325.0 25.0 L 337.5 25.692520775623262 L 350.0 27.770083102493075 L 362.5 31.232686980609415 L 375.0 36.080332409972307 L 387.5 42.313019390581722 L 400.0 49.930747922437654 L 412.5 58.933518005540179 L 425.0 69.321329639889186 L 437.5 81.094182825484751 L 450.0 94.252077562326889 L 462.5 108.79501385041551 L 475.0 124.72299168975069 L 487.5 142.03601108033237 L 500.0 160.73407202216066 L 512.5 180.81717451523545 L 525.0 202.28531855955674 L 537.5 225.13850415512462 L 550.0 249.37673130193903 L 562.5 275.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="475.0" y="35.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="520.0" y="42.0"></text></g><g class="toyplot-axes-Axis" id="te6d0b8156d84414e94a521f3ea7c2420" transform="translate(325.0,275.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="237.5" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tfac9f80c6f1049f9b7d00c6eecceeefd" transform="translate(325.0,275.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t176e3a7327f0495abb78c8fe5f104c11", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tf76676abf58344799458a9f0c1f25fea", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t15bb6fbd35294e7b840ddd50a2f5f950 .toyplot-mark-popup");
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
      var axes = {"t7d36420d64164ca59c6f799a24bce5ba": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 275.0, "min": 25.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}, "tf714f386478f4899a133dc091e3c2893": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 575.0, "min": 325.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="te13512bfec6849b7acecfc59ffa5b2a6"><svg height="480.0px" id="t576fe862863542278f171335dae4aa80" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 480.0 480.0" width="480.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t8b7367027c15412e8d1feed5bc9ee2c0"><clipPath id="t2d9595f072444e319496088ff1447837"><rect height="400.0" width="400.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2d9595f072444e319496088ff1447837)" style="cursor:crosshair"><rect height="400.0" style="pointer-events:all;visibility:hidden" width="400.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t59d9b2822b8c49be94adf70287223d0a" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 430.0 L 57.600000000000001 375.71428571428578 L 65.200000000000003 353.228406614032 L 72.799999999999997 335.97438473197525 L 80.400000000000006 321.42857142857144 L 88.0 308.61345265001137 L 95.599999999999994 297.02769967748463 L 103.2 286.37350025649368 L 110.8 276.45681322806394 L 118.39999999999999 267.14285714285711 L 126.0 258.33349844800227 L 133.59999999999999 249.95465423784975 L 141.19999999999999 241.94876946395047 L 148.80000000000001 234.27007361766917 L 156.40000000000001 226.88145614655744 L 164.0 219.75233263445455 L 171.59999999999999 212.85714285714289 L 179.20000000000002 206.17426603789841 L 186.79999999999998 199.68521984209599 L 194.40000000000001 193.37405735064914 L 202.0 187.22690530002285 L 209.59999999999999 181.23160513096869 L 217.19999999999999 175.37743018101384 L 224.80000000000001 169.65486016302384 L 232.40000000000001 164.05539935496921 L 240.0 158.57142857142856 L 247.59999999999999 153.19608354782028 L 255.20000000000002 147.92315419592572 L 262.80000000000001 142.74700051298731 L 270.39999999999998 137.66248189841266 L 278.0 132.66489735433839 L 285.60000000000002 127.74993458922738 L 293.19999999999999 122.91362645612796 L 300.80000000000001 118.1523134736499 L 308.40000000000003 113.46261142268371 L 316.0 108.8413832031637 L 323.59999999999997 104.28571428571431 L 331.19999999999999 99.792891212382386 L 338.80000000000001 95.360382695969861 L 346.40000000000003 90.985822944086976 L 354.0 86.666996896004548 L 361.59999999999997 82.401827110788219 L 369.19999999999999 78.188362086430459 L 376.80000000000001 74.024765823605691 L 384.39999999999998 69.909308475699476 L 392.0 65.840357950034274 L 399.60000000000002 61.81637234462832 L 407.19999999999999 57.835893121086208 L 414.80000000000001 53.897538927900932 L 422.39999999999998 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="330.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="375.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t3f00f84574ab4c6ab7b0f95702115365" transform="translate(50.0,430.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="372.4" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(76.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(152.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(228.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(304.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(380.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">50</tspan></text></g></g><g class="toyplot-axes-Axis" id="t40de5f72f67c499a82200ab1b40b2e54" transform="translate(50.0,430.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="380.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(190.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(380.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g><g class="toyplot-axes-Cartesian" id="tb7f1e700a42147cfaab4b5548a198180"><clipPath id="t9649b8c3195a4fde925b24c90ac42b6f"><rect height="164.0" width="164.0" x="230.0" y="230.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9649b8c3195a4fde925b24c90ac42b6f)" style="cursor:crosshair"><rect height="164.0" style="pointer-events:all;visibility:hidden" width="164.0" x="230.0" y="230.0"></rect><g class="toyplot-mark-Scatterplot" id="tf2c19c7b54b9473fada007bf8974b8ae" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.69486020426905" cy="292.34937164086591" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="309.52805058066855" cy="264.64984394587344" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="281.87895013330666" cy="297.50764015353104" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="330.48575274467896" cy="251.85551038259217" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.95956327928627" cy="263.78924721341804" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="339.47135852224909" cy="298.22466959820792" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.81496734216023" cy="298.98129624974621" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="299.3491717762297" cy="252.41602956679304" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.64359433663213" cy="298.32308028249213" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="284.62713870748303" cy="296.23350756117145" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="321.79464367804462" cy="324.03153541510358" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="289.65584043444767" cy="304.1682134138531" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="304.5144252546678" cy="309.90570706773286" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="292.99839491694513" cy="256.52383150081607" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="286.81353430235845" cy="304.93122734522672" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="366.59375126434145" cy="267.67436444313569" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="271.86908626058971" cy="358.86373610548964" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.20500461939469" cy="309.74414739618419" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="284.39016798881983" cy="334.27556817640266" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="340.70985275292543" cy="264.42158604025485" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="248.28511942061698" cy="272.18146362014232" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="276.94730924491614" cy="371.59575718185471" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.1123940376217" cy="297.98243120637017" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="322.26043243998163" cy="262.11054661685444" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="323.32701785386843" cy="301.772359520012" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="272.64519153639782" cy="240.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="284.43312729169764" cy="325.79790405984733" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="335.19903086826343" cy="327.03808355804301" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="303.36360093138262" cy="272.74385139094176" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="289.13856984282597" cy="269.19062124179572" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="326.54728040253838" cy="260.07838541610874" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.04851358765507" cy="289.74906047341739" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="289.54377669009455" cy="261.65890491256124" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="304.66170584420587" cy="293.78656748188246" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="320.01638458111262" cy="326.15824601829451" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.37713419961051" cy="285.80797704495762" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="314.01630268862476" cy="270.83285543163964" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="321.13212890167449" cy="298.47173117738896" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="256.69942211425075" cy="325.76484617325031" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="327.19752082992522" cy="326.92287441113456" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="261.08516127815642" cy="280.58473099868047" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="261.17929150322624" cy="299.52274851211189" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="328.99389178759469" cy="294.57526024100696" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="333.64025398597738" cy="298.51930992564974" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="285.11781974346025" cy="326.39972521819999" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="317.1484598713588" cy="293.63984744032183" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="322.53646170848975" cy="304.16131415013729" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="327.00660915544813" cy="240.39826820036239" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.50302311941891" cy="265.51764006253563" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.58456337049012" cy="310.28155285580539" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="296.52687736915954" cy="262.25075068240926" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="276.71343270977104" cy="311.62092557901963" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="277.20003643952106" cy="269.5199359214248" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="325.8189600251506" cy="326.40926034293557" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="304.57002939587068" cy="312.35972637620512" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="324.40624604203805" cy="293.90809233571508" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="280.09933001119157" cy="261.6743057053805" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="326.10048757352388" cy="313.01546733602908" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="255.99585555255004" cy="309.08941701670392" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="300.60246331237579" cy="306.39812986370782" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="295.47591566523988" cy="314.30208664565754" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.6472152817621" cy="255.9840338734399" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="252.25149122241143" cy="295.83243095965258" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="278.89602003761479" cy="254.92146681660242" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="322.45526316562785" cy="316.10719343189277" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="301.81663941257113" cy="304.38722942728708" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="288.85913603640051" cy="280.37940389059736" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.66407875540978" cy="260.29078590310411" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="321.65830531939986" cy="282.63441776376038" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="285.05242689926217" cy="271.43351680990253" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="244.81765923967046" cy="259.09312573042689" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.57616674053452" cy="302.04171725337829" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="332.76868768017346" cy="335.61748057368106" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="301.01255530185358" cy="282.58035338360708" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="277.53233701075885" cy="313.08715794863082" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="313.02152699657825" cy="307.46186608102437" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="330.78155119529538" cy="310.48283701149126" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="317.56542546241531" cy="300.20179264511444" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="324.38749815920721" cy="256.76915784987341" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="244.82978295283309" cy="352.69556817082855" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="267.64037013757888" cy="274.15434246382688" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.29701059067872" cy="284.07034478326511" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="275.90711955536534" cy="300.38162630392083" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="323.55865930743118" cy="324.60777254035042" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="294.64498347346239" cy="336.60223409225921" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="326.2397476680344" cy="299.51537728044514" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="319.84746577234876" cy="317.68085355251492" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="318.47909372903416" cy="257.82890968044893" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.46579988434195" cy="347.77307004684599" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="288.3138434834965" cy="288.8382242501076" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="277.92635707400348" cy="332.10136867309359" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="342.28784462898602" cy="299.44579190801164" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="296.14308431948876" cy="287.9854017196688" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="308.39547652092108" cy="289.11026149519597" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="320.00745086620702" cy="262.22646321197294" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="287.48390743939774" cy="280.34827215565576" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="309.79631063063556" cy="290.9983610697476" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="281.63759575997426" cy="262.96299910725401" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="278.87002826699904" cy="290.82551224455381" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="382.65654943617113" cy="299.14965888038557" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="284.0" y="250.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="329.0" y="257.0"></text></g><g class="toyplot-axes-Axis" id="t1b8f125c7b1249f3bf0c1384b0b2914e" transform="translate(240.0,384.0) rotate(0.0) translate(0,10.0)"><line style="" x1="4.817659239670477" x2="142.65654943617113" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-2</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(28.8,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-1</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(57.6,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(86.39999999999999,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">1</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(115.2,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">2</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">3</tspan></text></g></g><g class="toyplot-axes-Axis" id="tc38fcb25a883421a8db9638fdcadf2c8" transform="translate(240.0,384.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="12.404242818145278" x2="144.0" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-4</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(46.11512515201411,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-2</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(92.23025030402822,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(138.34537545604232,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">2</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.14285714285714285, 0.20203050891044214, 0.24743582965269675, 0.2857142857142857, 0.3194382824999699, 0.3499271061118826, 0.3779644730092272, 0.40406101782088427, 0.42857142857142855, 0.4517539514526256, 0.4738035414793428, 0.4948716593053935, 0.5150787536377127, 0.5345224838248488, 0.5532833351724881, 0.5714285714285714, 0.5890150893739515, 0.6060915267313264, 0.6226998490772391, 0.6388765649999398, 0.6546536707079771, 0.6700593942604899, 0.6851187890446742, 0.6998542122237652, 0.7142857142857143, 0.7284313590846835, 0.7423074889580902, 0.7559289460184544, 0.769309258162072, 0.7824607964359516, 0.7953949089757174, 0.8081220356417685, 0.8206518066482897, 0.8329931278350429, 0.8451542547285166, 0.8571428571428571, 0.8689660757568884, 0.8806305718527109, 0.8921425711997711, 0.9035079029052512, 0.9147320339189784, 0.9258200997725514, 0.9367769320431429, 0.9476070829586856, 0.9583148474999098, 0.9689042833036097, 0.9793792286287205, 0.989743318610787, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t59d9b2822b8c49be94adf70287223d0a", "filename": "toyplot"}, {"data": [[-0.6217062429073239, 0.41416842293988, -0.5458697870379622, 1.1418664147457975, 0.012484836086326964, 1.4538666153558717, 0.31996414382500915, 0.060735131119086835, -0.6234863077558288, -0.4504465726568409, 0.8400917943765498, -0.27583887380389993, 0.24008421023152005, -0.1597779542727398, -0.3745300589458873, 2.395616363345189, -0.8934345048406354, 0.26406266039564824, -0.45867472261042264, 1.4968698872543562, -1.7123222423396873, -0.7171073178848564, 0.2955692374174215, 0.8562650152771415, 0.8932992310370989, -0.8664864049861877, -0.45718308014938663, 1.3055219051480353, 0.20012503233967407, -0.2937996582352088, 1.0051139028659166, -0.53998216709531, -0.2797299760383841, 0.24519811959048143, 0.7783466868441878, 0.6172616041531435, 0.570010510021693, 0.8170878090859192, -1.4201589543662918, 1.027691695483514, -1.2678763445084573, -1.264607933915756, 1.0900656870692598, 1.2513977078464358, -0.433409036685408, 0.6787659677555128, 0.8658493648781164, 1.0210628178975059, 0.6563549694242669, -0.6255359940802039, -0.037261202459737776, -0.7252280309107266, -0.7083320680721847, 0.9798250008732843, 0.2420149095788427, 0.9307724320152093, -0.6076621523891805, 0.9896002629695788, -1.444588348869791, 0.10425219834638168, -0.07375292829027992, 0.001639419505629188, -1.5746009992218246, -0.6494437486939303, 0.8630299710287436, 0.14641109071427502, -0.3035022209583173, 0.4536138456739502, 0.8353578235902732, -0.43567962155339784, -1.8327201652892195, -0.625827543731441, 1.2211349888949123, 0.11849150353658379, -0.696793853793096, 0.5354696873811905, 1.1521371942810883, 0.6932439396671984, 0.9301214638613601, -1.8322992030266287, -1.0402649257785122, -0.5313537989347664, -0.7532250154387028, 0.901342337063583, -0.10260474050477823, 0.9944356829178614, 0.7724814504287753, 0.724968532258132, -0.004659726238127385, -0.32243599015637237, -0.6831126015971036, 1.5516612718397906, -0.05058735001775117, 0.3748429347542034, 0.7780364884099651, -0.3512532139097985, 0.42348300800818006, -0.5542501472231149, -0.6503462407292009, 2.953352410978164], [-0.025138040631287616, 1.176182680224771, -0.24885069437174062, 1.7310693262484336, 1.213506518319908, -0.27994805959902114, -0.312762744544323, 1.7067597669724606, -0.28421610328142555, -0.19359192241093517, -1.3991845674400287, -0.537717882235425, -0.7865513673432583, 1.5286055531225788, -0.570809581709662, 1.0450100774272195, -2.909847308810242, -0.7795445698547513, -1.8434653853942495, 1.1860821613544952, 0.8495384545204443, -3.4620314798124965, -0.26944224871639455, 1.2863112907684249, -0.43381037310719955, 2.24523947513176, -1.4757914784663364, -1.5295777142884275, 0.8251478551695557, 0.97925044677841, 1.3744455501484805, 0.0876367229143745, 1.3058988643813942, -0.0874688197966483, -1.491419407795786, 0.25856040209635023, 0.908027212126854, -0.2906630507593641, -1.4743577672278652, -1.5245811260094773, 0.485091113183406, -0.3362453767861684, -0.12167420280383548, -0.2927265276816965, -1.5018922927379588, -0.08110561288451276, -0.5374186631096789, 2.227966695363753, 1.1385466068626529, -0.8028516934004287, 1.280230679901918, -0.8609399114763462, 0.964968161799521, -1.502305828414342, -0.8929814941349707, -0.0927393185075168, 1.3052309363309547, -0.9214207950221447, -0.7511490975526799, -0.6344287311165271, -0.9772211123968582, 1.5520164243105778, -0.1761973430751205, 1.5980996585351346, -1.055508085717861, -0.5472165451019798, 0.49399609207726286, 1.3652338008018106, 0.39619677501026423, 0.8819766971913369, 1.4171759854420647, -0.44549234219991535, -1.9016637484196104, 0.39854153196257236, -0.9245299967153183, -0.6805626715020291, -0.8115813305865957, -0.3656953297360559, 1.517965818404362, -2.642335601346441, 0.7639752542827275, 0.3339210242767972, -0.3734946649092158, -1.424175809395779, -1.944372231388356, -0.3359256885432108, -1.1237572822855677, 1.47200467975052, -2.42884824301201, 0.1271394335893348, -1.7491709648048221, -0.3329077905236729, 0.16412610673085046, 0.11534125482730742, 1.2812840206596965, 0.49534626666050235, 0.03345490763307526, 1.249340666159272, 0.04095131253814707, -0.32006458445408603]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tf2c19c7b54b9473fada007bf8974b8ae", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#te13512bfec6849b7acecfc59ffa5b2a6 .toyplot-mark-popup");
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
      var axes = {"t8b7367027c15412e8d1feed5bc9ee2c0": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 430.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 430.0}, "scale": "linear"}]}, "tb7f1e700a42147cfaab4b5548a198180": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0, "min": -2.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 384.0, "min": 240.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.2452394751317599, "min": -4.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 240.0, "min": 384.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t8324aa2b758344f894da433907302827"><svg height="453.5433072px" id="te73177d5b2b04c0593c1d74b8855c290" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 453.5433072 453.5433072" width="453.5433072px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t83c3628099e6495db1be9bd02aef34a2"><clipPath id="t47309ce2eaaa469785b57a5b41963562"><rect height="95.59055120000002" width="95.59055120000002" x="27.795275600000004" y="27.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t47309ce2eaaa469785b57a5b41963562)" style="cursor:crosshair"><rect height="95.59055120000002" style="pointer-events:all;visibility:hidden" width="95.59055120000002" x="27.795275600000004" y="27.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="54.795275600000004"></text></g><g class="toyplot-axes-Axis" id="te0c2bde041ef40faa628bf3cece68b8e" transform="translate(37.7952756,113.3858268) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t6ba7f943309f484d859b3693b8dd7ef1" transform="translate(37.7952756,113.3858268) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(75.59055120000001,37.795275600000004)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">top-left</tspan></text></g><g class="toyplot-axes-Cartesian" id="t1d7fcd1bcd3e4273941ae7c5ad2cbea6"><clipPath id="t0e2b1598e8e247a997c210448ebccf52"><rect height="95.59055120000002" width="95.5905512" x="178.976378" y="27.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t0e2b1598e8e247a997c210448ebccf52)" style="cursor:crosshair"><rect height="95.59055120000002" style="pointer-events:all;visibility:hidden" width="95.5905512" x="178.976378" y="27.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="164.5669292" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="209.5669292" y="54.795275600000004"></text></g><g class="toyplot-axes-Axis" id="td97b904f4cee4d9fbc02a109601042cf" transform="translate(188.976378,113.3858268) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t3d9ce1d8dfce4b2d83aba6d7f81c59f1" transform="translate(188.976378,113.3858268) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(226.7716536,37.795275600000004)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">top</tspan></text></g><g class="toyplot-axes-Cartesian" id="tb2e1e04aabb04532ac5b491ed011ecfc"><clipPath id="t375e1dadd6454892b85021771a51e284"><rect height="95.59055120000002" width="95.5905512" x="330.1574804" y="27.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t375e1dadd6454892b85021771a51e284)" style="cursor:crosshair"><rect height="95.59055120000002" style="pointer-events:all;visibility:hidden" width="95.5905512" x="330.1574804" y="27.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="315.7480316" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.7480316" y="54.795275600000004"></text></g><g class="toyplot-axes-Axis" id="t1d5f9098c70240379687c8d324d3d0f3" transform="translate(340.1574804,113.3858268) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t147701a6f7934b8da9f4946c2e14b034" transform="translate(340.1574804,113.3858268) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(377.952756,37.795275600000004)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">top-right</tspan></text></g><g class="toyplot-axes-Cartesian" id="t14048787e839479690fc9d655136d475"><clipPath id="t5f39e16750604ec088142baa968d8200"><rect height="95.5905512" width="95.5905512" x="330.1574804" y="178.976378"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t5f39e16750604ec088142baa968d8200)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.5905512" x="330.1574804" y="178.976378"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="315.7480316" y="198.976378"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.7480316" y="205.976378"></text></g><g class="toyplot-axes-Axis" id="tf336edc9eeac48698869623a302dfa2f" transform="translate(340.1574804,264.5669292) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="tf765241894994d96a6fce5ad7c78a80d" transform="translate(340.1574804,264.5669292) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(377.952756,188.976378)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">right</tspan></text></g><g class="toyplot-axes-Cartesian" id="t28cea9c71640434da848a6680ec5b8f2"><clipPath id="t6de36940290f46c88a9225413e91e620"><rect height="95.5905512" width="95.5905512" x="330.1574804" y="330.1574804"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t6de36940290f46c88a9225413e91e620)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.5905512" x="330.1574804" y="330.1574804"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="315.7480316" y="350.1574804"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.7480316" y="357.1574804"></text></g><g class="toyplot-axes-Axis" id="t9a9b789bbac6498b8dfa766b059e5e52" transform="translate(340.1574804,415.7480316) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t684d3a6b22aa43709838c1818ff1b81d" transform="translate(340.1574804,415.7480316) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(377.952756,340.1574804)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">bottom-right</tspan></text></g><g class="toyplot-axes-Cartesian" id="t212a9c64ea9744ccac585fe1382e2618"><clipPath id="t06d4174f45a14ac4b3ce00453895b099"><rect height="95.5905512" width="95.5905512" x="178.976378" y="330.1574804"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t06d4174f45a14ac4b3ce00453895b099)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.5905512" x="178.976378" y="330.1574804"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="164.5669292" y="350.1574804"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="209.5669292" y="357.1574804"></text></g><g class="toyplot-axes-Axis" id="t61185a1dab27475c983fc775d7d419f6" transform="translate(188.976378,415.7480316) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="tef89e82bdf3b46298540ee2554026f82" transform="translate(188.976378,415.7480316) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(226.7716536,340.1574804)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">bottom</tspan></text></g><g class="toyplot-axes-Cartesian" id="t9e4d419fca214e688080647708691c85"><clipPath id="tca042caaf1844956a469485805a45ab3"><rect height="95.5905512" width="95.59055120000002" x="27.795275600000004" y="330.1574804"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tca042caaf1844956a469485805a45ab3)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.59055120000002" x="27.795275600000004" y="330.1574804"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="350.1574804"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="357.1574804"></text></g><g class="toyplot-axes-Axis" id="t12e9b6b761d84cc5b754b71cc9612864" transform="translate(37.7952756,415.7480316) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="t219ae10eda4b40ef9ff3aab386b45b2f" transform="translate(37.7952756,415.7480316) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(75.59055120000001,340.1574804)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">bottom-left</tspan></text></g><g class="toyplot-axes-Cartesian" id="t0b19af58e3e541ba816bda589de19beb"><clipPath id="t25dcb503c1d54168a5dbe6edea5491e2"><rect height="95.5905512" width="95.59055120000002" x="27.795275600000004" y="178.976378"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t25dcb503c1d54168a5dbe6edea5491e2)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.59055120000002" x="27.795275600000004" y="178.976378"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="198.976378"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="205.976378"></text></g><g class="toyplot-axes-Axis" id="tbb144e468e594e43b0cf6540db71a18b" transform="translate(37.7952756,264.5669292) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><g class="toyplot-axes-Axis" id="tba6bb469055a4c0caf3b094d91b9b3d9" transform="translate(37.7952756,264.5669292) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(75.59055120000001,188.976378)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">left</tspan></text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"t0b19af58e3e541ba816bda589de19beb": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 113.38582680000002, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 188.976378, "min": 264.5669292}, "scale": "linear"}]}, "t14048787e839479690fc9d655136d475": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 415.7480316, "min": 340.1574804}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 188.976378, "min": 264.5669292}, "scale": "linear"}]}, "t1d7fcd1bcd3e4273941ae7c5ad2cbea6": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 264.5669292, "min": 188.976378}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 37.795275600000004, "min": 113.38582680000002}, "scale": "linear"}]}, "t212a9c64ea9744ccac585fe1382e2618": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 264.5669292, "min": 188.976378}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 340.1574804, "min": 415.7480316}, "scale": "linear"}]}, "t28cea9c71640434da848a6680ec5b8f2": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 415.7480316, "min": 340.1574804}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 340.1574804, "min": 415.7480316}, "scale": "linear"}]}, "t83c3628099e6495db1be9bd02aef34a2": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 113.38582680000002, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 37.795275600000004, "min": 113.38582680000002}, "scale": "linear"}]}, "t9e4d419fca214e688080647708691c85": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 113.38582680000002, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 340.1574804, "min": 415.7480316}, "scale": "linear"}]}, "tb2e1e04aabb04532ac5b491ed011ecfc": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 415.7480316, "min": 340.1574804}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 37.795275600000004, "min": 113.38582680000002}, "scale": "linear"}]}};
    
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


