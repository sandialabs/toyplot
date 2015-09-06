
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

    <div align="center" class="toyplot" id="tc99e1e5835cb4d8485ada25f90ec015a"><svg height="300.0px" id="t48a502fa1ff0441395b83176cdabbbc2" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t4df01679a68a4784aa72ab3ab8967405"><clipPath id="t1d667b982d514f9883f910dd4a4a7640"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t1d667b982d514f9883f910dd4a4a7640)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t1fc1259e471c4b9aa31629aa875bc37c" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tc99e1e5835cb4d8485ada25f90ec015a text");
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
          var text = document.querySelectorAll("#tc99e1e5835cb4d8485ada25f90ec015a text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t1fc1259e471c4b9aa31629aa875bc37c", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tc99e1e5835cb4d8485ada25f90ec015a .toyplot-mark-popup");
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
      var axes = {"t4df01679a68a4784aa72ab3ab8967405": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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
    axes1 = canvas.axes(bounds=(20, 280, 20, 280))
    axes1.plot(y)
    axes2 = canvas.axes(bounds=(320, 580, 20, 280))
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="t4364256a258a4620afb50ab6c17a314f"><svg height="300.0px" id="t0be2eb1fbcd54fb781b56eb66d541078" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tb064f14162234919a361a0df446d5f90"><clipPath id="t28c50cd8caa548d4b96675b3a4cfaa1a"><rect height="260.0" width="260.0" x="20.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t28c50cd8caa548d4b96675b3a4cfaa1a)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="20.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="t38181acc657e484daec01b7933a0c3d1" style="fill:none"><g class="toyplot-Series"><path d="M 30.0 270.0 L 42.0 269.33518005540168 L 54.0 267.34072022160666 L 66.0 264.016620498615 L 78.0 259.36288088642664 L 90.0 253.37950138504155 L 102.0 246.06648199445985 L 114.0 237.42382271468145 L 126.0 227.45152354570638 L 138.0 216.14958448753464 L 150.0 203.51800554016617 L 162.0 189.55678670360109 L 174.0 174.26592797783934 L 186.0 157.64542936288092 L 198.0 139.6952908587258 L 210.0 120.41551246537395 L 222.0 99.806094182825504 L 234.0 77.867036011080387 L 246.0 54.598337950138536 L 258.0 30.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="180.0" y="30.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="225.0" y="37.0"></text></g><line style="" x1="30.0" x2="258.0" y1="280.0" y2="280.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="30.0" y="280.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="90.0" y="280.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="280.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="210.0" y="280.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="270.0" y="280.0">20</text></g><line style="" x1="20.0" x2="20.0" y1="30.0" y2="270.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 270.0)" x="20.0" y="270.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 150.0)" x="20.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 30.0)" x="20.0" y="30.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t616da7b90aab4c4095c716bf6a034718"><clipPath id="t8e430b1026834271bf47b669c639247e"><rect height="260.0" width="260.0" x="320.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t8e430b1026834271bf47b669c639247e)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="320.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="tfd8c02ba212645a8851ba99cf7b88c09" style="fill:none"><g class="toyplot-Series"><path d="M 330.0 30.0 L 342.0 30.664819944598332 L 354.0 32.659279778393355 L 366.0 35.983379501385038 L 378.0 40.637119113573412 L 390.0 46.62049861495845 L 402.0 53.933518005540151 L 414.0 62.576177285318565 L 426.0 72.54847645429362 L 438.0 83.850415512465361 L 450.0 96.4819944598338 L 462.0 110.44321329639889 L 474.0 125.73407202216066 L 486.0 142.35457063711908 L 498.0 160.3047091412742 L 510.0 179.58448753462605 L 522.0 200.19390581717448 L 534.0 222.13296398891964 L 546.0 245.40166204986147 L 558.0 270.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="480.0" y="30.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="525.0" y="37.0"></text></g><line style="" x1="330.0" x2="558.0" y1="280.0" y2="280.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.0" y="280.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="390.0" y="280.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="280.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="510.0" y="280.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="570.0" y="280.0">20</text></g><line style="" x1="320.0" x2="320.0" y1="30.0" y2="270.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 270.0)" x="320.0" y="270.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 150.0)" x="320.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 30.0)" x="320.0" y="30.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t4364256a258a4620afb50ab6c17a314f text");
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
          var text = document.querySelectorAll("#t4364256a258a4620afb50ab6c17a314f text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t38181acc657e484daec01b7933a0c3d1", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tfd8c02ba212645a8851ba99cf7b88c09", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t4364256a258a4620afb50ab6c17a314f .toyplot-mark-popup");
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
      var axes = {"t616da7b90aab4c4095c716bf6a034718": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 570.0, "min": 330.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}, "tb064f14162234919a361a0df446d5f90": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 270.0, "min": 30.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}};
    
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
    axes1 = canvas.axes(bounds=(20, 280, 20, -20))
    axes1.plot(y)
    axes2 = canvas.axes(bounds=(-280, -20, 20, -20))
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="t116839abcc8c41f2899bf52b975ed7e7"><svg height="300.0px" id="t2f8840eee3a142ffb81d7a83e0f25694" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t51c369360e764f5f8dc16b91a1e3846c"><clipPath id="t702d7b3def814165b7ce02f66d3f16bf"><rect height="260.0" width="260.0" x="20.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t702d7b3def814165b7ce02f66d3f16bf)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="20.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="t1aea3d3d877947499a8e1310da280e3a" style="fill:none"><g class="toyplot-Series"><path d="M 30.0 270.0 L 42.0 269.33518005540168 L 54.0 267.34072022160666 L 66.0 264.016620498615 L 78.0 259.36288088642664 L 90.0 253.37950138504155 L 102.0 246.06648199445985 L 114.0 237.42382271468145 L 126.0 227.45152354570638 L 138.0 216.14958448753464 L 150.0 203.51800554016617 L 162.0 189.55678670360109 L 174.0 174.26592797783934 L 186.0 157.64542936288092 L 198.0 139.6952908587258 L 210.0 120.41551246537395 L 222.0 99.806094182825504 L 234.0 77.867036011080387 L 246.0 54.598337950138536 L 258.0 30.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="180.0" y="30.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="225.0" y="37.0"></text></g><line style="" x1="30.0" x2="258.0" y1="280.0" y2="280.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="30.0" y="280.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="90.0" y="280.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="280.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="210.0" y="280.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="270.0" y="280.0">20</text></g><line style="" x1="20.0" x2="20.0" y1="30.0" y2="270.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 270.0)" x="20.0" y="270.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 150.0)" x="20.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 30.0)" x="20.0" y="30.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t0655d4a835324664bf1c761d60878746"><clipPath id="t88579cd14bc64d088bb4b7ba4bf5163e"><rect height="260.0" width="260.0" x="320.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t88579cd14bc64d088bb4b7ba4bf5163e)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="320.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="tab7a87b1562b4ab9a0d87c4c782614d6" style="fill:none"><g class="toyplot-Series"><path d="M 330.0 30.0 L 342.0 30.664819944598332 L 354.0 32.659279778393355 L 366.0 35.983379501385038 L 378.0 40.637119113573412 L 390.0 46.62049861495845 L 402.0 53.933518005540151 L 414.0 62.576177285318565 L 426.0 72.54847645429362 L 438.0 83.850415512465361 L 450.0 96.4819944598338 L 462.0 110.44321329639889 L 474.0 125.73407202216066 L 486.0 142.35457063711908 L 498.0 160.3047091412742 L 510.0 179.58448753462605 L 522.0 200.19390581717448 L 534.0 222.13296398891964 L 546.0 245.40166204986147 L 558.0 270.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="480.0" y="30.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="525.0" y="37.0"></text></g><line style="" x1="330.0" x2="558.0" y1="280.0" y2="280.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.0" y="280.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="390.0" y="280.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="280.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="510.0" y="280.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="570.0" y="280.0">20</text></g><line style="" x1="320.0" x2="320.0" y1="30.0" y2="270.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 270.0)" x="320.0" y="270.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 150.0)" x="320.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 30.0)" x="320.0" y="30.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t116839abcc8c41f2899bf52b975ed7e7 text");
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
          var text = document.querySelectorAll("#t116839abcc8c41f2899bf52b975ed7e7 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t1aea3d3d877947499a8e1310da280e3a", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tab7a87b1562b4ab9a0d87c4c782614d6", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t116839abcc8c41f2899bf52b975ed7e7 .toyplot-mark-popup");
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
      var axes = {"t0655d4a835324664bf1c761d60878746": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 570.0, "min": 330.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}, "t51c369360e764f5f8dc16b91a1e3846c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 270.0, "min": 30.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}};
    
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
    axes1 = canvas.axes(bounds=("1cm", "5cm", "10%", "90%"))
    axes1.plot(y)
    axes2 = canvas.axes(bounds=("6cm", "-1cm", "10%", "90%"))
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="t92fc273e92d44876a43c510d2e3cb4fe"><svg height="192.0px" id="t0b5e3a513c6e40a4805d73e1bbc9e459" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 755.9055119999999 192.0" width="755.9055119999999px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t4b3d6d003c7342c89cc1fe2b976b2815"><clipPath id="t2d02a6ec9a164aef82edda54f9299ab8"><rect height="153.60000000000002" width="151.1811024" x="37.795275600000004" y="19.200000000000003"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2d02a6ec9a164aef82edda54f9299ab8)" style="cursor:crosshair"><rect height="153.60000000000002" style="pointer-events:all;visibility:hidden" width="151.1811024" x="37.795275600000004" y="19.200000000000003"></rect><g class="toyplot-mark-Plot" id="t95252c639e35405ebe71816b06e6e0cc" style="fill:none"><g class="toyplot-Series"><path d="M 47.795275600000004 162.80000000000001 L 54.35433072 162.42991689750693 L 60.913385840000004 161.31966759002771 L 67.47244096 159.46925207756234 L 74.031496080000011 156.87867036011082 L 80.590551199999993 153.54792243767315 L 87.149606320000004 149.47700831024935 L 93.708661439999986 144.66592797783935 L 100.26771656 139.11468144044323 L 106.82677168000001 132.82326869806096 L 113.38582679999999 125.79168975069251 L 119.94488192 118.01994459833796 L 126.50393704 109.50803324099725 L 133.06299215999999 100.25595567867038 L 139.62204727999998 90.263711911357362 L 146.18110239999999 79.531301939058181 L 152.74015752 68.058725761772877 L 159.29921263999998 55.845983379501419 L 165.85826775999999 42.893074792243787 L 172.41732287999997 29.200000000000003" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="88.97637799999998" y="29.200000000000003"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="133.97637799999998" y="36.2"></text></g><line style="" x1="47.795275600000004" x2="172.41732287999997" y1="172.8" y2="172.8"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="47.795275600000004" y="172.8">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="80.5905512" y="172.8">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="113.38582679999999" y="172.8">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="146.1811024" y="172.8">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="178.97637799999998" y="172.8">20</text></g><line style="" x1="37.795275600000004" x2="37.795275600000004" y1="29.200000000000003" y2="162.8"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 162.8)" x="37.795275600000004" y="162.8">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 96.0)" x="37.795275600000004" y="96.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 29.200000000000003)" x="37.795275600000004" y="29.200000000000003">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t4aa6b95bf6894f6bb598b6fd29593126"><clipPath id="tf1670ed6cb0a4a908339ba62440c614e"><rect height="153.60000000000002" width="491.3385827999999" x="226.7716536" y="19.200000000000003"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf1670ed6cb0a4a908339ba62440c614e)" style="cursor:crosshair"><rect height="153.60000000000002" style="pointer-events:all;visibility:hidden" width="491.3385827999999" x="226.7716536" y="19.200000000000003"></rect><g class="toyplot-mark-Plot" id="t56f9b6952ace443f9e112cfe7b2643da" style="fill:none"><g class="toyplot-Series"><path d="M 236.77165360000001 29.200000000000003 L 260.33858273999999 29.570083102493072 L 283.90551188000001 30.680332409972301 L 307.47244102000002 32.530747922437676 L 331.03937016000003 35.121329639889204 L 354.60629929999999 38.45207756232687 L 378.17322844 42.52299168975069 L 401.74015757999996 47.334072022160669 L 425.30708672000003 52.885318559556787 L 448.87401585999999 59.176731301939057 L 472.440945 66.208310249307488 L 496.00787414000001 73.980055401662057 L 519.57480327999997 82.491966759002764 L 543.14173241999993 91.744044321329639 L 566.70866155999988 101.73628808864265 L 590.27559069999995 112.46869806094185 L 613.84251984000002 123.94127423822714 L 637.40944897999998 136.1540166204986 L 660.97637811999994 149.10692520775623 L 684.54330726000001 162.80000000000001" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="618.1102364" y="29.200000000000003"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="663.1102364" y="36.2"></text></g><line style="" x1="236.7716536" x2="684.54330726" y1="172.8" y2="172.8"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="236.7716536" y="172.8">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="354.6062993" y="172.8">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="472.440945" y="172.8">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="590.2755907" y="172.8">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="708.1102364" y="172.8">20</text></g><line style="" x1="226.7716536" x2="226.7716536" y1="29.200000000000003" y2="162.8"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 226.7716536, 162.8)" x="226.7716536" y="162.8">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 226.7716536, 96.0)" x="226.7716536" y="96.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 226.7716536, 29.200000000000003)" x="226.7716536" y="29.200000000000003">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t92fc273e92d44876a43c510d2e3cb4fe text");
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
          var text = document.querySelectorAll("#t92fc273e92d44876a43c510d2e3cb4fe text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t95252c639e35405ebe71816b06e6e0cc", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t56f9b6952ace443f9e112cfe7b2643da", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t92fc273e92d44876a43c510d2e3cb4fe .toyplot-mark-popup");
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
      var axes = {"t4aa6b95bf6894f6bb598b6fd29593126": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 708.1102364, "min": 236.7716536}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 29.200000000000003, "min": 162.8}, "scale": "linear"}]}, "t4b3d6d003c7342c89cc1fe2b976b2815": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 178.97637799999998, "min": 47.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 29.200000000000003, "min": 162.8}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t07ef028062f1412396e2ff74cbec7ef7"><svg height="300.0px" id="tb5164e9abeef4e3eaabbb3132041ac50" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t7ec95d45ddb7430f80b33c7231ad83b8"><clipPath id="tafdf0df0db6b4b05b6d64bb7a0117fa6"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tafdf0df0db6b4b05b6d64bb7a0117fa6)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tab865b168f044ff4953e37400262bf52" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t0596fbd6214f4cc7bcea606b15e15b35"><clipPath id="t9768e5992ce14c55be02e20d9e1a3f14"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9768e5992ce14c55be02e20d9e1a3f14)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t6017c56e384e45f19e8085a6b5d674ee" style="fill:none"><g class="toyplot-Series"><path d="M 360.0 60.0 L 369.0 60.498614958448755 L 378.0 61.99445983379502 L 387.0 64.48753462603878 L 396.0 67.97783933518005 L 405.0 72.46537396121883 L 414.0 77.95013850415512 L 423.0 84.43213296398892 L 432.0 91.911357340720215 L 441.0 100.38781163434902 L 450.0 109.86149584487535 L 459.0 120.33240997229916 L 468.0 131.80055401662048 L 477.0 144.26592797783931 L 486.0 157.72853185595568 L 495.0 172.18836565096953 L 504.0 187.64542936288086 L 513.0 204.0997229916897 L 522.0 221.55124653739611 L 531.0 240.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t07ef028062f1412396e2ff74cbec7ef7 text");
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
          var text = document.querySelectorAll("#t07ef028062f1412396e2ff74cbec7ef7 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tab865b168f044ff4953e37400262bf52", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t6017c56e384e45f19e8085a6b5d674ee", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t07ef028062f1412396e2ff74cbec7ef7 .toyplot-mark-popup");
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
      var axes = {"t0596fbd6214f4cc7bcea606b15e15b35": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "t7ec95d45ddb7430f80b33c7231ad83b8": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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
    axes1 = canvas.axes(grid=(1, 2, 0), gutter=15)
    axes1.plot(y)
    axes2 = canvas.axes(grid=(1, 2, 1), gutter=15)
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="ta3fa89b2051444a5bd740877ed731ff8"><svg height="300.0px" id="t67705e687e814ef1b26cad776c03fd8c" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t119883c296814738a860f9570de8dd0c"><clipPath id="t797efdba2f044952af8a9e0976f26508"><rect height="270.0" width="270.0" x="15.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t797efdba2f044952af8a9e0976f26508)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="15.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="t71f60f6aa02847469e101021b2002a5a" style="fill:none"><g class="toyplot-Series"><path d="M 25.0 275.0 L 37.5 274.30747922437678 L 50.0 272.22991689750694 L 62.5 268.7673130193906 L 75.0 263.91966759002764 L 87.5 257.6869806094183 L 100.0 250.06925207756234 L 112.5 241.06648199445985 L 125.0 230.6786703601108 L 137.5 218.90581717451525 L 150.0 205.74792243767311 L 162.5 191.20498614958447 L 175.0 175.27700831024933 L 187.5 157.96398891966763 L 200.0 139.26592797783937 L 212.5 119.18282548476454 L 225.0 97.714681440443243 L 237.5 74.861495844875392 L 250.0 50.623268698060976 L 262.5 25.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="185.0" y="25.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="230.0" y="32.0"></text></g><line style="" x1="25.0" x2="262.5" y1="285.0" y2="285.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="25.0" y="285.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="87.5" y="285.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="285.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="212.5" y="285.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="275.0" y="285.0">20</text></g><line style="" x1="15.0" x2="15.0" y1="25.0" y2="275.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 275.0)" x="15.0" y="275.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 150.0)" x="15.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 25.0)" x="15.0" y="25.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t90b08890ad0b4d41ac0749efb859b152"><clipPath id="t96dc56965da140cd85ff7d770a367685"><rect height="270.0" width="270.0" x="315.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t96dc56965da140cd85ff7d770a367685)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="315.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="t95ce598131d8483bb765a7e7310a2270" style="fill:none"><g class="toyplot-Series"><path d="M 325.0 25.0 L 337.5 25.692520775623262 L 350.0 27.770083102493075 L 362.5 31.232686980609415 L 375.0 36.080332409972307 L 387.5 42.313019390581722 L 400.0 49.930747922437654 L 412.5 58.933518005540179 L 425.0 69.321329639889186 L 437.5 81.094182825484751 L 450.0 94.252077562326889 L 462.5 108.79501385041551 L 475.0 124.72299168975069 L 487.5 142.03601108033237 L 500.0 160.73407202216066 L 512.5 180.81717451523545 L 525.0 202.28531855955674 L 537.5 225.13850415512462 L 550.0 249.37673130193903 L 562.5 275.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="485.0" y="25.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="530.0" y="32.0"></text></g><line style="" x1="325.0" x2="562.5" y1="285.0" y2="285.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="325.0" y="285.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="387.5" y="285.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="285.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="512.5" y="285.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="575.0" y="285.0">20</text></g><line style="" x1="315.0" x2="315.0" y1="25.0" y2="275.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 315.0, 275.0)" x="315.0" y="275.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 315.0, 150.0)" x="315.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 315.0, 25.0)" x="315.0" y="25.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#ta3fa89b2051444a5bd740877ed731ff8 text");
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
          var text = document.querySelectorAll("#ta3fa89b2051444a5bd740877ed731ff8 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t71f60f6aa02847469e101021b2002a5a", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t95ce598131d8483bb765a7e7310a2270", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#ta3fa89b2051444a5bd740877ed731ff8 .toyplot-mark-popup");
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
      var axes = {"t119883c296814738a860f9570de8dd0c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 275.0, "min": 25.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}, "t90b08890ad0b4d41ac0749efb859b152": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 575.0, "min": 325.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="tf84bb92556134a50999db26855e0ea36"><svg height="480.0px" id="t6c02a1ba861648e987a946022bdfd9d9" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 480.0 480.0" width="480.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t72ba7e18cf9d469697d61674aacfa0d3"><clipPath id="tcc8f4366a58f464ca62fe8b9863de376"><rect height="380.0" width="380.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tcc8f4366a58f464ca62fe8b9863de376)" style="cursor:crosshair"><rect height="380.0" style="pointer-events:all;visibility:hidden" width="380.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t77f9e290ed9b49f9888142266bee9e19" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 420.0 L 67.200000000000003 368.57142857142856 L 74.399999999999991 347.26901679224085 L 81.599999999999994 330.92310132502917 L 88.800000000000011 317.14285714285717 L 96.0 305.00221830001078 L 103.19999999999999 294.02624179972224 L 110.40000000000001 283.93278971667826 L 117.59999999999999 274.53803358448164 L 124.8 265.71428571428572 L 132.0 257.36857747705477 L 139.20000000000002 249.43072506743661 L 146.40000000000001 241.84620265005836 L 153.59999999999999 234.57164869042342 L 160.80000000000001 227.57190582305444 L 168.0 220.8179993379043 L 175.19999999999999 214.28571428571428 L 182.40000000000001 207.95456782537747 L 189.59999999999999 201.80705037672249 L 196.80000000000001 195.82805433219391 L 204.0 190.00443660002168 L 211.20000000000002 184.32467854512825 L 218.40000000000001 178.77861806622366 L 225.60000000000002 173.35723594391732 L 232.80000000000001 168.05248359944454 L 240.0 162.85714285714286 L 247.19999999999999 157.76471072951395 L 254.40000000000001 152.76930397508752 L 261.60000000000002 147.8655794333564 L 268.80000000000001 143.0486670616541 L 276.0 138.31411328305745 L 283.19999999999999 133.65783276874174 L 290.40000000000003 129.07606716896333 L 297.59999999999997 124.5653496066157 L 304.80000000000001 120.12247397938457 L 312.0 115.74446829773404 L 319.19999999999999 111.42857142857144 L 326.40000000000003 107.17221272752016 L 333.59999999999997 102.97299413302409 L 340.80000000000001 98.828674368082389 L 348.0 94.73715495410957 L 355.19999999999999 90.69646778916777 L 362.40000000000003 86.704764081881493 L 369.59999999999997 82.760304464468533 L 376.80000000000001 78.861450134873195 L 384.0 75.006654900032473 L 391.20000000000005 71.194458010700515 L 398.39999999999998 67.423477693660615 L 405.59999999999997 63.692405300116675 L 412.79999999999995 60.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="330.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="375.0" y="67.0"></text></g><line style="" x1="60.0" x2="412.79999999999995" y1="430.0" y2="430.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="430.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="132.0" y="430.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="204.0" y="430.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="276.0" y="430.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="348.0" y="430.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="420.0" y="430.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="420.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 420.0)" x="50.0" y="420.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t5c03950c35b640558755e97278f92174"><clipPath id="t68ae98f003ed4a89a58f53e7189cbc49"><rect height="144.0" width="144.0" x="240.0" y="240.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t68ae98f003ed4a89a58f53e7189cbc49)" style="cursor:crosshair"><rect height="144.0" style="pointer-events:all;visibility:hidden" width="144.0" x="240.0" y="240.0"></rect><g class="toyplot-mark-Scatterplot" id="t5aaf5f4b7c1f44578db425d63d885ea5" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="336.7329493859844" cy="299.8915141391787" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="323.48035519958239" cy="307.77600780466247" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.92577751738025" cy="373.51407587917635" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="329.71469568005546" cy="348.07747013908255" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="320.17212131870838" cy="299.12911024144626" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="276.21405034403489" cy="284.89477497297048" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="324.54345523073169" cy="297.23169088484337" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="374.0" cy="335.40005176432101" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.66859890167541" cy="312.0418563525472" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="311.83809300013979" cy="310.39178304700101" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.72843333552885" cy="280.95323874279995" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.6526205698483" cy="272.09900174266562" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="333.3435173762233" cy="276.42080511146344" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="294.1349314539068" cy="329.08830265948518" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="275.06239496663437" cy="336.978259349729" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.40262655440523" cy="296.13901902807731" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="327.59008996626039" cy="286.43091600445337" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="324.33559809534984" cy="276.00057995040856" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="347.20172947505262" cy="273.75794119176652" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.24511006607787" cy="305.10132971701273" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.4793678392939" cy="258.64263252689079" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="280.12917553535362" cy="275.4483407520388" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="338.68642633035279" cy="312.06605683493211" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="326.53919387489719" cy="292.60838232678941" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="313.90653066403968" cy="329.56203815111513" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="339.85405267056842" cy="285.0649777305556" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="323.80292921817886" cy="324.45282748851025" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="330.33641893432713" cy="258.62356206115572" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.85759238285948" cy="325.30996332691814" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.4804213313501" cy="343.82967614691086" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="331.84832333170579" cy="315.97259520533248" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="276.49607513399445" cy="285.98357538330202" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="324.71357057647469" cy="322.71418173252158" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="295.68376727035138" cy="323.65986972583534" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.42447781575436" cy="306.9072830387268" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="312.80199099992524" cy="342.10564399957934" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.94073727575943" cy="261.34005759051098" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="328.48393659914666" cy="308.82134154957436" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="251.39109341279629" cy="272.42544364874243" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="280.36270871729448" cy="315.73607467331709" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="321.27310555500242" cy="298.25149503459954" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.07050004834952" cy="287.9470458824328" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="333.88046285180866" cy="329.57372105512172" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.97770190166528" cy="282.19375383272705" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="281.71382459673328" cy="286.44220510147289" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.22327817166081" cy="281.70697631324686" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.2904962028303" cy="313.87485522770902" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="301.85399436019219" cy="340.12848150781821" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="348.31622654543361" cy="314.74810272275857" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="320.76368047815549" cy="292.44301774343796" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="302.29573261019414" cy="319.83933860548433" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="347.6299322081631" cy="331.59616222408658" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="274.69577660834506" cy="281.59110546786917" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.88373421365583" cy="312.05756192781189" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.52131602841098" cy="253.17120178212446" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="322.17708781878548" cy="317.57685654308636" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="273.81441237765495" cy="261.35091159948433" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="295.56242430110854" cy="315.45408305009482" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="281.21113886111351" cy="359.58837764892456" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="319.98173729321115" cy="331.41643513593021" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="313.52866738099704" cy="326.31422724777076" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="275.65587624812849" cy="280.4130371797404" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="346.1164730929255" cy="278.29539762512076" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.51551685460618" cy="298.59251719026452" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="322.22758770901783" cy="355.79342621383501" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.54148801383496" cy="299.62992883603044" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="364.50050716765776" cy="299.43625737439959" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.74476400586752" cy="327.85369009141135" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="319.68455197067533" cy="336.44341226533652" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="356.11906495234092" cy="283.9318482073445" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="298.44288636946476" cy="296.3693442523678" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="317.18391109523736" cy="312.10467945071503" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.96757776059587" cy="310.90291321200874" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.98324837226681" cy="296.22316262723211" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="274.08888962421349" cy="320.73545619165873" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="269.49298170437078" cy="306.32259849760885" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="291.17524969818686" cy="374.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="288.11115899954655" cy="288.33870494871951" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="348.92336657625788" cy="307.58884164669433" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="304.77505586326447" cy="282.66025757546856" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="285.42529871073594" cy="292.48262005153589" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="301.69124922808226" cy="284.96106039301526" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="309.66808833463324" cy="299.05110747957781" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="289.82810848578146" cy="286.8895728626743" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="250.0" cy="305.84797951036467" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="291.87501547542917" cy="324.18840578301354" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="343.35601227302072" cy="336.20415025867544" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="327.52862056422669" cy="286.95149357668072" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="356.95670050896842" cy="344.91350701039323" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="294.43335657025" cy="333.88506065051422" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="336.75419951593216" cy="299.26545947174941" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="291.50407974182951" cy="267.28188085540205" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.87371099329044" cy="314.98241540986209" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.47331552011633" cy="329.97253736369692" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="365.40628682614749" cy="309.53430187885783" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.86243459934985" cy="318.70198583901606" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="355.98821150400897" cy="279.6884758366881" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="345.48264495203568" cy="318.87768885025065" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="278.29442797549456" cy="283.16760304432228" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="298.56769224306049" cy="277.25069524803985" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="284.0" y="250.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="329.0" y="257.0"></text></g><line style="" x1="250.0" x2="374.0" y1="384.0" y2="384.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="258.9990980165465" y="384.0">-2</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="287.44952708507094" y="384.0">-1</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="315.8999561535952" y="384.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="344.3503852221196" y="384.0">1</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="372.800814290644" y="384.0">2</text></g><line style="" x1="240.0" x2="240.0" y1="253.17120178212446" y2="374.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 240.0, 359.14192244497815)" x="240.0" y="359.14192244497815">-2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 240.0, 331.8564418337336)" x="240.0" y="331.8564418337336">-1</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 240.0, 304.570961222489)" x="240.0" y="304.570961222489">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 240.0, 277.28548061124457)" x="240.0" y="277.28548061124457">1</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 240.0, 250.0)" x="240.0" y="250.0">2</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tf84bb92556134a50999db26855e0ea36 text");
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
          var text = document.querySelectorAll("#tf84bb92556134a50999db26855e0ea36 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.14285714285714285, 0.20203050891044214, 0.24743582965269675, 0.2857142857142857, 0.3194382824999699, 0.3499271061118826, 0.3779644730092272, 0.40406101782088427, 0.42857142857142855, 0.4517539514526256, 0.4738035414793428, 0.4948716593053935, 0.5150787536377127, 0.5345224838248488, 0.5532833351724881, 0.5714285714285714, 0.5890150893739515, 0.6060915267313264, 0.6226998490772391, 0.6388765649999398, 0.6546536707079771, 0.6700593942604899, 0.6851187890446742, 0.6998542122237652, 0.7142857142857143, 0.7284313590846835, 0.7423074889580902, 0.7559289460184544, 0.769309258162072, 0.7824607964359516, 0.7953949089757174, 0.8081220356417685, 0.8206518066482897, 0.8329931278350429, 0.8451542547285166, 0.8571428571428571, 0.8689660757568884, 0.8806305718527109, 0.8921425711997711, 0.9035079029052512, 0.9147320339189784, 0.9258200997725514, 0.9367769320431429, 0.9476070829586856, 0.9583148474999098, 0.9689042833036097, 0.9793792286287205, 0.989743318610787, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t77f9e290ed9b49f9888142266bee9e19", "filename": "toyplot"}, {"data": [[0.7322558539349894, 0.2664423453062642, -1.159004616654285, 0.48557227355646176, 0.1501617130210357, -1.394914140450211, 0.3038090939267777, 2.0421500043625955, -0.3596204903369689, -0.14276983815155384, -0.18177310456761667, -0.18443783645963488, 0.6131212004084116, -0.7650156926374027, -1.4353935080768538, -0.19322483980643734, 0.4108948158394661, 0.2965031536584886, 1.1002214850983578, -1.288375862424861, 1.2857244295892751, -1.257301973621763, 0.8009183313852716, 0.37395702172634315, -0.07006662306407807, 0.8419590600647353, 0.2777804526444527, 0.5074251339394884, -1.2668478104117826, -0.014746168545812592, 0.560566842057041, -1.3850012920611665, 0.30978845351159395, -0.7105758874339704, 1.2837951081225476, -0.1088899273261711, -0.3149062833554127, 0.4423125013419726, -2.267412649047434, -1.2490935497214266, 0.18886004806696047, -0.2048987061392, 0.6319942189591029, 0.7760074793562737, -1.2016033738726002, -1.1836966641459927, -0.19716609325132833, -0.49369947144110204, 1.1393947807873852, 0.17095434001524895, -0.4781728778372597, 1.1152723207844957, -1.4482797235151623, -0.1763144565538042, 0.9005614577237255, 0.22063398938804785, -1.4792586668754641, -0.7148409538394893, -1.2192722017981468, 0.14346993255478543, -0.08334808472964926, -1.4145333206939261, 1.0620759661146821, -0.18925687503764418, 0.22240900269666092, -0.6452791307836847, 1.7082537102342281, 0.9084153982361276, 0.13302420880770305, 1.413655614889878, -0.6135960108750624, 0.04512954579875272, -0.3139628710514438, -1.754515113325757, -1.4696111059934327, -1.6311520060892883, -0.8690451168893656, -0.9767443959146598, 1.1607350575671105, -0.39102750484134585, -1.0711493091882542, -0.4994197764571691, -0.21904301702980372, -0.9163955877438044, -2.316307989411046, -0.8444491511991173, 0.9650489296065133, 0.4087342367534501, 1.4430975454354593, -0.754526391557816, 0.7330027716667603, -0.8574871174352751, -1.2662812597143502, 0.020152925115474094, 1.74009082792086, -0.1770631136040951, 1.4090562660358836, 1.0397976328296814, -1.3217912491767974, -0.6092092273472951], [0.17149952936441684, -0.11746344613965133, -2.526732647262785, -1.5944930395935266, 0.19944127276248858, 0.7211229492292639, 0.2689807975975742, -1.1298716332351146, -0.2738047841817871, -0.2133303755006302, 0.8655783937320889, 1.1900820052420664, 1.0316899493947245, -0.898549004370198, -1.1877121971560443, 0.30902670598138005, 0.664824104676391, 1.0470910034220344, 1.1292826565797887, -0.019437755269193977, 1.683251592668332, 1.06733030967571, -0.27469172045128987, 0.4384228764792145, -0.9159111867843404, 0.7148850984099903, -0.7286610248612478, 1.6839505162462902, -0.7600746492214031, -1.4388133925060131, -0.41786450989412877, 0.6812189275319938, -0.6649404776310066, -0.699599496718398, -0.08562509304948591, -1.3756284271431145, 1.584392235853172, -0.15577443504270588, 1.178118063293311, -0.40919614390911024, 0.23160545632042803, 0.6092586594646755, -0.9163393597079913, 0.8201141005572105, 0.6644103645931446, 0.8379542671430826, -0.34098332874465614, -1.3031663540013179, -0.3729874377244955, 0.4444834104938968, -0.5595788324396622, -0.9904608750215754, 0.8422008789960512, -0.27438038611046445, 1.8837769498251902, -0.476659931554861, 1.5839944415416845, -0.3988612838698083, -2.016362372732494, -0.9838739619773437, -0.796880448436051, 0.8853765263270825, 0.9629870175913253, 0.21910715509848017, -1.8772791918584273, 0.18108650739405868, 0.1881844751517183, -0.8533010358383543, -1.1681103036797003, 0.7564137611942602, 0.3005853951035521, -0.2761072211101645, -0.23206305506344158, 0.30594288274389914, -0.5924211194765672, -0.06419668028123082, -2.5445415371902507, 0.5949045393424416, -0.11060389469414784, 0.8030169583302448, 0.44303200457357766, 0.7186936198364928, 0.20230003720867323, 0.6480145470675035, -0.0468021181693725, -0.7189700940228264, -1.1593414639414545, 0.6457451820931919, -1.478535282654275, -1.074347923193428, 0.19444413775703076, 1.3666272146117133, -0.3815748872344365, -0.9309557893856438, -0.18190409496849252, -0.5178953897811682, 0.9119313579379178, -0.5243348223034677, 0.7844229860970936, 1.001274867161048]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t5aaf5f4b7c1f44578db425d63d885ea5", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tf84bb92556134a50999db26855e0ea36 .toyplot-mark-popup");
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
      var axes = {"t5c03950c35b640558755e97278f92174": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0421500043625955, "min": -2.3163079894110461}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 374.0, "min": 250.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": -2.5445415371902507}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 250.0, "min": 374.0}, "scale": "linear"}]}, "t72ba7e18cf9d469697d61674aacfa0d3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 420.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 420.0}, "scale": "linear"}]}};
    
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

    canvas = toyplot.Canvas(width="10cm")
    for position in ["top-left", "top", "top-right", "right", "bottom-right", "bottom", "bottom-left", "left"]:
        canvas.axes(corner=(position, "1cm", "2cm", "2cm"), label=position)



.. raw:: html

    <div align="center" class="toyplot" id="t7d53daba98664d90889d232bf64134b1"><svg height="377.95275599999997px" id="tf07adab8fb7c49b980f269cd979b4443" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 377.95275599999997 377.95275599999997" width="377.95275599999997px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t7ab54236628c4f4e813fad9248b2c32c"><clipPath id="tb34d13d4d82b47de9cc1d44546672045"><rect height="75.59055120000002" width="75.59055120000002" x="37.795275600000004" y="37.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb34d13d4d82b47de9cc1d44546672045)" style="cursor:crosshair"><rect height="75.59055120000002" style="pointer-events:all;visibility:hidden" width="75.59055120000002" x="37.795275600000004" y="37.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="54.795275600000004"></text></g><line style="" x1="37.795275600000004" x2="113.38582680000002" y1="113.38582680000002" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="47.795275600000004" y="113.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="75.59055120000001" y="113.38582680000002">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="103.38582680000002" y="113.38582680000002">0.5</text></g><line style="" x1="37.795275600000004" x2="37.795275600000004" y1="37.795275600000004" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 103.38582680000002)" x="37.795275600000004" y="103.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 75.59055120000001)" x="37.795275600000004" y="75.59055120000001">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 47.795275600000004)" x="37.795275600000004" y="47.795275600000004">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="75.59055120000001" y="37.795275600000004">top-left</text></g><g class="toyplot-axes-Cartesian" id="t51b9d304bb964ccf854cc75c94200bb6"><clipPath id="t37831b4e8766495ca17bb4c8eeae27a1"><rect height="75.59055120000002" width="75.5905512" x="151.1811024" y="37.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t37831b4e8766495ca17bb4c8eeae27a1)" style="cursor:crosshair"><rect height="75.59055120000002" style="pointer-events:all;visibility:hidden" width="75.5905512" x="151.1811024" y="37.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="126.77165359999998" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="171.77165359999998" y="54.795275600000004"></text></g><line style="" x1="151.1811024" x2="226.77165359999998" y1="113.38582680000002" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="161.1811024" y="113.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="188.97637799999998" y="113.38582680000002">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="216.77165359999998" y="113.38582680000002">0.5</text></g><line style="" x1="151.1811024" x2="151.1811024" y1="37.795275600000004" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 103.38582680000002)" x="151.1811024" y="103.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 75.59055120000001)" x="151.1811024" y="75.59055120000001">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 47.795275600000004)" x="151.1811024" y="47.795275600000004">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="188.97637799999998" y="37.795275600000004">top</text></g><g class="toyplot-axes-Cartesian" id="tb029abceab2046d6ac24b855fe5113a2"><clipPath id="t437f918b9e2d4e4eb34d653f297f280c"><rect height="75.59055120000002" width="75.5905512" x="264.56692919999995" y="37.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t437f918b9e2d4e4eb34d653f297f280c)" style="cursor:crosshair"><rect height="75.59055120000002" style="pointer-events:all;visibility:hidden" width="75.5905512" x="264.56692919999995" y="37.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="240.15748039999994" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="285.15748039999994" y="54.795275600000004"></text></g><line style="" x1="264.56692919999995" x2="340.15748039999994" y1="113.38582680000002" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="274.56692919999995" y="113.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="302.3622048" y="113.38582680000002">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.15748039999994" y="113.38582680000002">0.5</text></g><line style="" x1="264.56692919999995" x2="264.56692919999995" y1="37.795275600000004" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 103.38582680000002)" x="264.56692919999995" y="103.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 75.59055120000001)" x="264.56692919999995" y="75.59055120000001">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 47.795275600000004)" x="264.56692919999995" y="47.795275600000004">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="302.3622048" y="37.795275600000004">top-right</text></g><g class="toyplot-axes-Cartesian" id="t57277bcb4b274f298349c702ea82d9ab"><clipPath id="t16c81da3de9a42c9abc087b1182ce521"><rect height="75.5905512" width="75.5905512" x="264.56692919999995" y="151.1811024"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t16c81da3de9a42c9abc087b1182ce521)" style="cursor:crosshair"><rect height="75.5905512" style="pointer-events:all;visibility:hidden" width="75.5905512" x="264.56692919999995" y="151.1811024"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="240.15748039999994" y="161.1811024"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="285.15748039999994" y="168.1811024"></text></g><line style="" x1="264.56692919999995" x2="340.15748039999994" y1="226.77165359999998" y2="226.77165359999998"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="274.56692919999995" y="226.77165359999998">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="302.3622048" y="226.77165359999998">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.15748039999994" y="226.77165359999998">0.5</text></g><line style="" x1="264.56692919999995" x2="264.56692919999995" y1="151.1811024" y2="226.77165359999998"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 216.77165359999998)" x="264.56692919999995" y="216.77165359999998">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 188.97637799999998)" x="264.56692919999995" y="188.97637799999998">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 161.1811024)" x="264.56692919999995" y="161.1811024">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="302.3622048" y="151.1811024">right</text></g><g class="toyplot-axes-Cartesian" id="ta8842f391f684a2d8379c79a7fd02b99"><clipPath id="t508797d54e6e45ba860af984524791f5"><rect height="75.5905512" width="75.5905512" x="264.56692919999995" y="264.56692919999995"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t508797d54e6e45ba860af984524791f5)" style="cursor:crosshair"><rect height="75.5905512" style="pointer-events:all;visibility:hidden" width="75.5905512" x="264.56692919999995" y="264.56692919999995"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="240.15748039999994" y="274.56692919999995"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="285.15748039999994" y="281.56692919999995"></text></g><line style="" x1="264.56692919999995" x2="340.15748039999994" y1="340.15748039999994" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="274.56692919999995" y="340.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="302.3622048" y="340.15748039999994">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.15748039999994" y="340.15748039999994">0.5</text></g><line style="" x1="264.56692919999995" x2="264.56692919999995" y1="264.56692919999995" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 330.15748039999994)" x="264.56692919999995" y="330.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 302.3622048)" x="264.56692919999995" y="302.3622048">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 274.56692919999995)" x="264.56692919999995" y="274.56692919999995">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="302.3622048" y="264.56692919999995">bottom-right</text></g><g class="toyplot-axes-Cartesian" id="t667b20d55a2a4179a0ba9f2784ede68d"><clipPath id="t7b678425386046afb37641c5b83d47f6"><rect height="75.5905512" width="75.5905512" x="151.1811024" y="264.56692919999995"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t7b678425386046afb37641c5b83d47f6)" style="cursor:crosshair"><rect height="75.5905512" style="pointer-events:all;visibility:hidden" width="75.5905512" x="151.1811024" y="264.56692919999995"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="126.77165359999998" y="274.56692919999995"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="171.77165359999998" y="281.56692919999995"></text></g><line style="" x1="151.1811024" x2="226.77165359999998" y1="340.15748039999994" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="161.1811024" y="340.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="188.97637799999998" y="340.15748039999994">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="216.77165359999998" y="340.15748039999994">0.5</text></g><line style="" x1="151.1811024" x2="151.1811024" y1="264.56692919999995" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 330.15748039999994)" x="151.1811024" y="330.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 302.3622048)" x="151.1811024" y="302.3622048">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 274.56692919999995)" x="151.1811024" y="274.56692919999995">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="188.97637799999998" y="264.56692919999995">bottom</text></g><g class="toyplot-axes-Cartesian" id="t802ea058f9d941768d253f7e66bf8e78"><clipPath id="tf9e5122824e14b8cbb044323630ea87d"><rect height="75.5905512" width="75.59055120000002" x="37.795275600000004" y="264.56692919999995"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf9e5122824e14b8cbb044323630ea87d)" style="cursor:crosshair"><rect height="75.5905512" style="pointer-events:all;visibility:hidden" width="75.59055120000002" x="37.795275600000004" y="264.56692919999995"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="274.56692919999995"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="281.56692919999995"></text></g><line style="" x1="37.795275600000004" x2="113.38582680000002" y1="340.15748039999994" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="47.795275600000004" y="340.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="75.59055120000001" y="340.15748039999994">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="103.38582680000002" y="340.15748039999994">0.5</text></g><line style="" x1="37.795275600000004" x2="37.795275600000004" y1="264.56692919999995" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 330.15748039999994)" x="37.795275600000004" y="330.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 302.3622048)" x="37.795275600000004" y="302.3622048">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 274.56692919999995)" x="37.795275600000004" y="274.56692919999995">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="75.59055120000001" y="264.56692919999995">bottom-left</text></g><g class="toyplot-axes-Cartesian" id="t07c72684cf6647739548332c9c87b7e6"><clipPath id="t8db690a070e04a8a925d010b4784109e"><rect height="75.5905512" width="75.59055120000002" x="37.795275600000004" y="151.1811024"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t8db690a070e04a8a925d010b4784109e)" style="cursor:crosshair"><rect height="75.5905512" style="pointer-events:all;visibility:hidden" width="75.59055120000002" x="37.795275600000004" y="151.1811024"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="161.1811024"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="168.1811024"></text></g><line style="" x1="37.795275600000004" x2="113.38582680000002" y1="226.77165359999998" y2="226.77165359999998"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="47.795275600000004" y="226.77165359999998">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="75.59055120000001" y="226.77165359999998">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="103.38582680000002" y="226.77165359999998">0.5</text></g><line style="" x1="37.795275600000004" x2="37.795275600000004" y1="151.1811024" y2="226.77165359999998"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 216.77165359999998)" x="37.795275600000004" y="216.77165359999998">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 188.97637799999998)" x="37.795275600000004" y="188.97637799999998">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 161.1811024)" x="37.795275600000004" y="161.1811024">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="75.59055120000001" y="151.1811024">left</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t7d53daba98664d90889d232bf64134b1 text");
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
          var text = document.querySelectorAll("#t7d53daba98664d90889d232bf64134b1 text");
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
      var axes = {"t07c72684cf6647739548332c9c87b7e6": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 103.38582680000002, "min": 47.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 161.1811024, "min": 216.77165359999998}, "scale": "linear"}]}, "t51b9d304bb964ccf854cc75c94200bb6": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 216.77165359999998, "min": 161.1811024}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 47.795275600000004, "min": 103.38582680000002}, "scale": "linear"}]}, "t57277bcb4b274f298349c702ea82d9ab": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 330.15748039999994, "min": 274.56692919999995}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 161.1811024, "min": 216.77165359999998}, "scale": "linear"}]}, "t667b20d55a2a4179a0ba9f2784ede68d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 216.77165359999998, "min": 161.1811024}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 274.56692919999995, "min": 330.15748039999994}, "scale": "linear"}]}, "t7ab54236628c4f4e813fad9248b2c32c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 103.38582680000002, "min": 47.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 47.795275600000004, "min": 103.38582680000002}, "scale": "linear"}]}, "t802ea058f9d941768d253f7e66bf8e78": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 103.38582680000002, "min": 47.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 274.56692919999995, "min": 330.15748039999994}, "scale": "linear"}]}, "ta8842f391f684a2d8379c79a7fd02b99": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 330.15748039999994, "min": 274.56692919999995}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 274.56692919999995, "min": 330.15748039999994}, "scale": "linear"}]}, "tb029abceab2046d6ac24b855fe5113a2": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 330.15748039999994, "min": 274.56692919999995}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 47.795275600000004, "min": 103.38582680000002}, "scale": "linear"}]}};
    
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

