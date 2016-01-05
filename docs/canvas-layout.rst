
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

    <div align="center" class="toyplot" id="t45640fa7171748d588fc81cc4b666ca1"><svg height="300.0px" id="t277ca91db50e4cc3a7116d9faa704905" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t24b3fac7b9994b8cb5a228ada37a0740"><clipPath id="t40ae1c74a5a548ceb11f47568a685bca"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t40ae1c74a5a548ceb11f47568a685bca)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tb538d97630fa443d91909f5d59e0cd64" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t8a0686069c474ab0895f6d1fd75304a2" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t5d210af703a1445484e65057c1f6d32c" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t45640fa7171748d588fc81cc4b666ca1 text");
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
          var text = document.querySelectorAll("#t45640fa7171748d588fc81cc4b666ca1 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tb538d97630fa443d91909f5d59e0cd64", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t45640fa7171748d588fc81cc4b666ca1 .toyplot-mark-popup");
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
      var axes = {"t24b3fac7b9994b8cb5a228ada37a0740": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="tdf607a0e58ab47558e004acad48041eb"><svg height="300.0px" id="t4d2bd2e98818485cb17590555da284ad" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc8851cadc9c04b30ae328479433835e1"><clipPath id="t00566e4236d24b2a9857e78dee84855c"><rect height="260.0" width="260.0" x="20.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t00566e4236d24b2a9857e78dee84855c)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="20.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="t7642adc34b4c4b1a88016128529ac1ae" style="fill:none"><g class="toyplot-Series"><path d="M 30.0 270.0 L 42.0 269.33518005540168 L 54.0 267.34072022160666 L 66.0 264.016620498615 L 78.0 259.36288088642664 L 90.0 253.37950138504155 L 102.0 246.06648199445985 L 114.0 237.42382271468145 L 126.0 227.45152354570638 L 138.0 216.14958448753464 L 150.0 203.51800554016617 L 162.0 189.55678670360109 L 174.0 174.26592797783934 L 186.0 157.64542936288092 L 198.0 139.6952908587258 L 210.0 120.41551246537395 L 222.0 99.806094182825504 L 234.0 77.867036011080387 L 246.0 54.598337950138536 L 258.0 30.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="170.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="215.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="td58a603b1f604cfb81e7d302924202aa" transform="translate(30.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="tcb91da7289b74f49a26c10f37ca14b5a" transform="translate(30.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="tbe71999a5ee542dd863a5f5b46371d3c"><clipPath id="t9c84ad7c0e7d4aa785291378627960da"><rect height="260.0" width="260.0" x="320.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9c84ad7c0e7d4aa785291378627960da)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="320.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="t64d164be23514c2a9fe4d00eae827e6c" style="fill:none"><g class="toyplot-Series"><path d="M 330.0 30.0 L 342.0 30.664819944598332 L 354.0 32.659279778393355 L 366.0 35.983379501385038 L 378.0 40.637119113573412 L 390.0 46.62049861495845 L 402.0 53.933518005540151 L 414.0 62.576177285318565 L 426.0 72.54847645429362 L 438.0 83.850415512465361 L 450.0 96.4819944598338 L 462.0 110.44321329639889 L 474.0 125.73407202216066 L 486.0 142.35457063711908 L 498.0 160.3047091412742 L 510.0 179.58448753462605 L 522.0 200.19390581717448 L 534.0 222.13296398891964 L 546.0 245.40166204986147 L 558.0 270.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="470.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="515.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="t3c7724664f034664875d39844f17b752" transform="translate(330.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t87dd9d7ebb9747e0a744f5f99ce7bf77" transform="translate(330.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tdf607a0e58ab47558e004acad48041eb text");
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
          var text = document.querySelectorAll("#tdf607a0e58ab47558e004acad48041eb text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t7642adc34b4c4b1a88016128529ac1ae", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t64d164be23514c2a9fe4d00eae827e6c", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tdf607a0e58ab47558e004acad48041eb .toyplot-mark-popup");
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
      var axes = {"tbe71999a5ee542dd863a5f5b46371d3c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 570.0, "min": 330.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}, "tc8851cadc9c04b30ae328479433835e1": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 270.0, "min": 30.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t0dc579fe1d1a442cb1c41b7ab6153b49"><svg height="300.0px" id="t4fcac98e07604783bce494dda8faa855" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tbc686e4765d647b7998bfdc46f5a9388"><clipPath id="t7174c684b26344a389ebb7beacab3d54"><rect height="260.0" width="260.0" x="20.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t7174c684b26344a389ebb7beacab3d54)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="20.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="t64a9224680c84e03afb9284b52d688df" style="fill:none"><g class="toyplot-Series"><path d="M 30.0 270.0 L 42.0 269.33518005540168 L 54.0 267.34072022160666 L 66.0 264.016620498615 L 78.0 259.36288088642664 L 90.0 253.37950138504155 L 102.0 246.06648199445985 L 114.0 237.42382271468145 L 126.0 227.45152354570638 L 138.0 216.14958448753464 L 150.0 203.51800554016617 L 162.0 189.55678670360109 L 174.0 174.26592797783934 L 186.0 157.64542936288092 L 198.0 139.6952908587258 L 210.0 120.41551246537395 L 222.0 99.806094182825504 L 234.0 77.867036011080387 L 246.0 54.598337950138536 L 258.0 30.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="170.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="215.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="t7f152e10bad741f28c261c1524ac5228" transform="translate(30.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t742349dc064f492fa384ffdeaff66971" transform="translate(30.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="t85ea21b2a30e4d58bd463231df0841be"><clipPath id="t36700767831f423e86bbbe76d7cab461"><rect height="260.0" width="260.0" x="320.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t36700767831f423e86bbbe76d7cab461)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="320.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="tc945c289a8d64ebfab15c77608e3a820" style="fill:none"><g class="toyplot-Series"><path d="M 330.0 30.0 L 342.0 30.664819944598332 L 354.0 32.659279778393355 L 366.0 35.983379501385038 L 378.0 40.637119113573412 L 390.0 46.62049861495845 L 402.0 53.933518005540151 L 414.0 62.576177285318565 L 426.0 72.54847645429362 L 438.0 83.850415512465361 L 450.0 96.4819944598338 L 462.0 110.44321329639889 L 474.0 125.73407202216066 L 486.0 142.35457063711908 L 498.0 160.3047091412742 L 510.0 179.58448753462605 L 522.0 200.19390581717448 L 534.0 222.13296398891964 L 546.0 245.40166204986147 L 558.0 270.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="470.0" y="40.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="515.0" y="47.0"></text></g><g class="toyplot-axes-Axis" id="t1db62c4aa3964f8e92813c65185a81c8" transform="translate(330.0,270.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="228.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t0ac23cd652594bfeb265244afa734234" transform="translate(330.0,270.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="240.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(240.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t0dc579fe1d1a442cb1c41b7ab6153b49 text");
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
          var text = document.querySelectorAll("#t0dc579fe1d1a442cb1c41b7ab6153b49 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t64a9224680c84e03afb9284b52d688df", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tc945c289a8d64ebfab15c77608e3a820", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t0dc579fe1d1a442cb1c41b7ab6153b49 .toyplot-mark-popup");
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
      var axes = {"t85ea21b2a30e4d58bd463231df0841be": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 570.0, "min": 330.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}, "tbc686e4765d647b7998bfdc46f5a9388": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 270.0, "min": 30.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="tdea0c209d1804cb18bf78edd9225c312"><svg height="192.0px" id="tb73383705a024532b63ee8a507b2dd01" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 755.9055119999999 192.0" width="755.9055119999999px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="ta3e044833d06445fa2aadc34dd066a83"><clipPath id="t66aabad9d3f74036afeb2ff207232165"><rect height="154.40000000000003" width="171.1811024" x="27.795275600000004" y="9.200000000000003"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t66aabad9d3f74036afeb2ff207232165)" style="cursor:crosshair"><rect height="154.40000000000003" style="pointer-events:all;visibility:hidden" width="171.1811024" x="27.795275600000004" y="9.200000000000003"></rect><g class="toyplot-mark-Plot" id="te98d2edac0714b4ebbf2251d9e4c7bac" style="fill:none"><g class="toyplot-Series"><path d="M 37.795275600000004 153.60000000000002 L 45.35433072 153.22770083102495 L 52.913385840000004 152.11080332409975 L 60.47244096 150.2493074792244 L 68.031496079999997 147.6432132963989 L 75.590551199999993 144.29252077562327 L 83.149606320000004 140.19722991689756 L 90.708661439999986 135.3573407202216 L 98.267716559999997 129.77285318559558 L 105.82677168000001 123.44376731301942 L 113.38582679999999 116.3700831024931 L 120.94488192 108.55180055401662 L 128.50393703999998 99.988919667590054 L 136.06299215999999 90.681440443213333 L 143.62204727999998 80.629362880886447 L 151.18110239999999 69.832686980609424 L 158.74015752 58.291412742382292 L 166.29921263999998 46.005540166205023 L 173.85826775999999 32.975069252077589 L 181.41732287999997 19.200000000000003" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="88.97637799999998" y="29.200000000000003"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="133.97637799999998" y="36.2"></text></g><g class="toyplot-axes-Axis" id="td897bb70f41547878db19b9f04dba047" transform="translate(37.7952756,153.6) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="143.62204727999998" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(113.38582679999999,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(151.1811024,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t3a58e5e439c84477946f4ff459676e2d" transform="translate(37.7952756,153.6) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="134.40000000000003" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(67.20000000000002,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(134.40000000000003,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="t0db3cb77f70f49b4bdc34b18a17807f1"><clipPath id="t002827daf0eb4ce78f1b5ef778eae34a"><rect height="154.40000000000003" width="511.3385827999999" x="216.7716536" y="9.200000000000003"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t002827daf0eb4ce78f1b5ef778eae34a)" style="cursor:crosshair"><rect height="154.40000000000003" style="pointer-events:all;visibility:hidden" width="511.3385827999999" x="216.7716536" y="9.200000000000003"></rect><g class="toyplot-mark-Plot" id="t629848087b1a48e28cec17c8fd50385b" style="fill:none"><g class="toyplot-Series"><path d="M 226.77165360000001 19.200000000000003 L 251.33858273999999 19.572299168975068 L 275.90551188000001 20.689196675900281 L 300.47244102000002 22.550692520775623 L 325.03937016000003 25.156786703601114 L 349.60629929999999 28.507479224376734 L 374.17322844 32.602770083102492 L 398.74015757999996 37.442659279778404 L 423.30708672000003 43.027146814404432 L 447.87401585999999 49.356232686980618 L 472.440945 56.429916897506935 L 497.00787414000001 64.248199445983389 L 521.57480327999997 72.811080332409972 L 546.14173241999993 82.118559556786693 L 570.70866155999988 92.170637119113579 L 595.27559069999995 102.9673130193906 L 619.84251984000002 114.50858725761772 L 644.40944897999998 126.794459833795 L 668.97637811999994 139.82493074792245 L 693.54330726000001 153.60000000000002" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="618.1102364" y="29.200000000000003"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="663.1102364" y="36.2"></text></g><g class="toyplot-axes-Axis" id="tb46c91c41ab741988eec24c62c6a2a44" transform="translate(226.7716536,153.6) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="466.7716536599999" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(122.83464569999998,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.66929139999996,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(368.5039370999999,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(491.3385827999999,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t83918fd20e03418ea56580a2c21874dc" transform="translate(226.7716536,153.6) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="134.40000000000003" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(67.20000000000002,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(134.40000000000003,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tdea0c209d1804cb18bf78edd9225c312 text");
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
          var text = document.querySelectorAll("#tdea0c209d1804cb18bf78edd9225c312 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "te98d2edac0714b4ebbf2251d9e4c7bac", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t629848087b1a48e28cec17c8fd50385b", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tdea0c209d1804cb18bf78edd9225c312 .toyplot-mark-popup");
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
      var axes = {"t0db3cb77f70f49b4bdc34b18a17807f1": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 718.1102364, "min": 226.7716536}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 19.200000000000003, "min": 153.60000000000002}, "scale": "linear"}]}, "ta3e044833d06445fa2aadc34dd066a83": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 188.97637799999998, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 19.200000000000003, "min": 153.60000000000002}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t11e63083c84d48f9bda875b30f7344a3"><svg height="300.0px" id="tb29b5f4cb9b64911b6a75ed576d21e25" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t7b7bf8daf6554e3c8346cb8bc6540c0e"><clipPath id="tedd620e735c24dfa87ef8484ca10f565"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tedd620e735c24dfa87ef8484ca10f565)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tcca1d73d251b432da50ca0e8719857ef" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t9523faa4e117466b8ec7b165364e993a" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="tf6b30d326fc44338967a415a6d84b779" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="tf32f227aaf5247409305bd9faf08e3a1"><clipPath id="tb1cba5d36bf04cbe9fb49d76761a9b4f"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb1cba5d36bf04cbe9fb49d76761a9b4f)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tff7ca78fd9c34cc3bab1289caa32782d" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 50.0 L 360.0 50.554016620498615 L 370.0 52.21606648199446 L 380.0 54.986149584487535 L 390.0 58.86426592797784 L 400.0 63.850415512465375 L 410.0 69.944598337950126 L 420.0 77.146814404432135 L 430.0 85.45706371191136 L 440.0 94.875346260387801 L 450.0 105.4016620498615 L 460.0 117.03601108033241 L 470.0 129.77839335180056 L 480.0 143.62880886426589 L 490.0 158.58725761772851 L 500.0 174.65373961218839 L 510.0 191.82825484764541 L 520.0 210.11080332409966 L 530.0 229.50138504155123 L 540.0 250.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t80b9ed2816a4439ab9339cf449c7bdfa" transform="translate(350.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t91adb69f13bb40f2b76351e6ca59ff55" transform="translate(350.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t11e63083c84d48f9bda875b30f7344a3 text");
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
          var text = document.querySelectorAll("#t11e63083c84d48f9bda875b30f7344a3 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tcca1d73d251b432da50ca0e8719857ef", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tff7ca78fd9c34cc3bab1289caa32782d", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t11e63083c84d48f9bda875b30f7344a3 .toyplot-mark-popup");
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
      var axes = {"t7b7bf8daf6554e3c8346cb8bc6540c0e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "tf32f227aaf5247409305bd9faf08e3a1": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="ta492487dfeda456cbcd2e632ae4054d5"><svg height="300.0px" id="t9d06809ae5384184ba6ff5bb48e602b5" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t30e1a0f2b1f94464a6d35f5e1b3aab49"><clipPath id="t2a41ba2e080c48d7904b36a5f6eee757"><rect height="270.0" width="270.0" x="15.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2a41ba2e080c48d7904b36a5f6eee757)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="15.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="t43a597ed8c5b4211b0524c9c7a18b638" style="fill:none"><g class="toyplot-Series"><path d="M 25.0 275.0 L 37.5 274.30747922437678 L 50.0 272.22991689750694 L 62.5 268.7673130193906 L 75.0 263.91966759002764 L 87.5 257.6869806094183 L 100.0 250.06925207756234 L 112.5 241.06648199445985 L 125.0 230.6786703601108 L 137.5 218.90581717451525 L 150.0 205.74792243767311 L 162.5 191.20498614958447 L 175.0 175.27700831024933 L 187.5 157.96398891966763 L 200.0 139.26592797783937 L 212.5 119.18282548476454 L 225.0 97.714681440443243 L 237.5 74.861495844875392 L 250.0 50.623268698060976 L 262.5 25.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="175.0" y="35.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="220.0" y="42.0"></text></g><g class="toyplot-axes-Axis" id="t9f445140f9514e3297b48d39b06b3ace" transform="translate(25.0,275.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="237.5" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t875c02bd97bc4a8aacce28edad0cf2a1" transform="translate(25.0,275.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="t9d96397c412f4720819bf46772821fa0"><clipPath id="t6ba0203c81f14b27b02a590597f364f6"><rect height="270.0" width="270.0" x="315.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t6ba0203c81f14b27b02a590597f364f6)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="315.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="tbb1efc9983514bb69bd4d2233dbddb0b" style="fill:none"><g class="toyplot-Series"><path d="M 325.0 25.0 L 337.5 25.692520775623262 L 350.0 27.770083102493075 L 362.5 31.232686980609415 L 375.0 36.080332409972307 L 387.5 42.313019390581722 L 400.0 49.930747922437654 L 412.5 58.933518005540179 L 425.0 69.321329639889186 L 437.5 81.094182825484751 L 450.0 94.252077562326889 L 462.5 108.79501385041551 L 475.0 124.72299168975069 L 487.5 142.03601108033237 L 500.0 160.73407202216066 L 512.5 180.81717451523545 L 525.0 202.28531855955674 L 537.5 225.13850415512462 L 550.0 249.37673130193903 L 562.5 275.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="475.0" y="35.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="520.0" y="42.0"></text></g><g class="toyplot-axes-Axis" id="t9858e1180bce4db287554812e234a3aa" transform="translate(325.0,275.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="237.5" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t29725e831e26438bb4e323037990d37c" transform="translate(325.0,275.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#ta492487dfeda456cbcd2e632ae4054d5 text");
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
          var text = document.querySelectorAll("#ta492487dfeda456cbcd2e632ae4054d5 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t43a597ed8c5b4211b0524c9c7a18b638", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tbb1efc9983514bb69bd4d2233dbddb0b", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#ta492487dfeda456cbcd2e632ae4054d5 .toyplot-mark-popup");
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
      var axes = {"t30e1a0f2b1f94464a6d35f5e1b3aab49": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 275.0, "min": 25.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}, "t9d96397c412f4720819bf46772821fa0": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 575.0, "min": 325.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t82c42b3959cb45199c9047272f08570b"><svg height="480.0px" id="t1462924d8446407f9f06470b7e50a77a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 480.0 480.0" width="480.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="taaf1115a864f4b9b92f65b86572dffb8"><clipPath id="t4480eb47cac24a8788dfa206bb4090e8"><rect height="400.0" width="400.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t4480eb47cac24a8788dfa206bb4090e8)" style="cursor:crosshair"><rect height="400.0" style="pointer-events:all;visibility:hidden" width="400.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t24eb1628a5624dec82aafa6a3e3e8fda" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 430.0 L 57.600000000000001 375.71428571428578 L 65.200000000000003 353.228406614032 L 72.799999999999997 335.97438473197525 L 80.400000000000006 321.42857142857144 L 88.0 308.61345265001137 L 95.599999999999994 297.02769967748463 L 103.2 286.37350025649368 L 110.8 276.45681322806394 L 118.39999999999999 267.14285714285711 L 126.0 258.33349844800227 L 133.59999999999999 249.95465423784975 L 141.19999999999999 241.94876946395047 L 148.80000000000001 234.27007361766917 L 156.40000000000001 226.88145614655744 L 164.0 219.75233263445455 L 171.59999999999999 212.85714285714289 L 179.20000000000002 206.17426603789841 L 186.79999999999998 199.68521984209599 L 194.40000000000001 193.37405735064914 L 202.0 187.22690530002285 L 209.59999999999999 181.23160513096869 L 217.19999999999999 175.37743018101384 L 224.80000000000001 169.65486016302384 L 232.40000000000001 164.05539935496921 L 240.0 158.57142857142856 L 247.59999999999999 153.19608354782028 L 255.20000000000002 147.92315419592572 L 262.80000000000001 142.74700051298731 L 270.39999999999998 137.66248189841266 L 278.0 132.66489735433839 L 285.60000000000002 127.74993458922738 L 293.19999999999999 122.91362645612796 L 300.80000000000001 118.1523134736499 L 308.40000000000003 113.46261142268371 L 316.0 108.8413832031637 L 323.59999999999997 104.28571428571431 L 331.19999999999999 99.792891212382386 L 338.80000000000001 95.360382695969861 L 346.40000000000003 90.985822944086976 L 354.0 86.666996896004548 L 361.59999999999997 82.401827110788219 L 369.19999999999999 78.188362086430459 L 376.80000000000001 74.024765823605691 L 384.39999999999998 69.909308475699476 L 392.0 65.840357950034274 L 399.60000000000002 61.81637234462832 L 407.19999999999999 57.835893121086208 L 414.80000000000001 53.897538927900932 L 422.39999999999998 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="330.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="375.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t5b8aa0c6a2e648b98099b2e4a21c06f4" transform="translate(50.0,430.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="372.4" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(76.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(152.0,0) rotate(0)" x="0" y="0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(228.0,0) rotate(0)" x="0" y="0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(304.0,0) rotate(0)" x="0" y="0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(380.0,0) rotate(0)" x="0" y="0">50</text></g></g><g class="toyplot-axes-Axis" id="te9bc66305c3d4ce6b109a3569ac86d62" transform="translate(50.0,430.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="380.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(190.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(380.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="tc989931747ed457c80c3c9746fa33661"><clipPath id="t881e914d1d794697835abb971f640079"><rect height="164.0" width="164.0" x="230.0" y="230.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t881e914d1d794697835abb971f640079)" style="cursor:crosshair"><rect height="164.0" style="pointer-events:all;visibility:hidden" width="164.0" x="230.0" y="230.0"></rect><g class="toyplot-mark-Scatterplot" id="t635b7ca802324fb7a7bf1a2de912c6c9" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="290.49275905975912" cy="276.39411546706367" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.27736764784908" cy="330.81107628211896" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="334.20187402410465" cy="290.55733479985554" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="317.51825655654568" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="330.15973848066574" cy="298.30449636780747" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="359.78478824679871" cy="265.94361778043066" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="340.29633707464518" cy="289.12097770484786" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="302.13135520827285" cy="362.4666661679139" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="339.02820129806412" cy="319.20055483632365" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="322.15472197483996" cy="298.00077913509216" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="312.83099035124098" cy="319.33667849511897" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="314.78691041523189" cy="356.69277772975295" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="314.84620857001426" cy="287.81683468613255" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="332.89977004713865" cy="298.71580332039844" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.92150119025604" cy="308.88803915281278" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="269.75728731367354" cy="284.85043525011531" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="250.82396696351685" cy="340.29290758637001" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.16953244623835" cy="290.47839442702758" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="309.30211445021445" cy="297.84994075805662" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.89586636631333" cy="310.89126409666585" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.24258820783092" cy="325.84598733562223" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="317.54468781722079" cy="258.13720290093721" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="342.15926433712877" cy="318.21924971202924" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.48181663630135" cy="332.46438099244534" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="346.60405053563898" cy="280.39399359114975" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="335.03798662218685" cy="262.44840801645688" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="321.3619622085846" cy="312.578491293703" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="294.37321923118338" cy="306.26792296072927" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="340.81900036064894" cy="343.73105411764584" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="336.31547474617946" cy="384.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="335.78078042008474" cy="268.76093496973124" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="321.0507118393831" cy="246.46868215316096" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="268.32322126844372" cy="262.08191384840518" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.2677224442005" cy="288.16024141040293" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.14578143824366" cy="268.48668468606473" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="327.89321279315783" cy="278.06448054106909" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.60378752125837" cy="313.78337029790697" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="344.15139729886005" cy="264.64510949410737" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.02888132557086" cy="318.68509206040329" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="299.50320426689234" cy="277.53750173924925" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="322.57057468728499" cy="287.47167541502972" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="298.65250808764165" cy="294.81395749586102" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="287.38558806489982" cy="316.17727700499751" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="319.13574466833217" cy="277.52044983537303" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="319.17495304690112" cy="287.77168685614998" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="335.56584185029925" cy="322.11675919206226" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="314.16943400123267" cy="323.90976331483051" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.35514827161387" cy="331.42985084250006" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="330.05777382592055" cy="240.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="345.82862672017461" cy="295.28731186449704" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="371.12784057373528" cy="287.89808768641058" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="368.45123969603344" cy="311.80105976056734" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="321.13570912787327" cy="257.52836555088174" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="354.82738748895076" cy="263.8137367707817" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="363.2245038210969" cy="261.32373902889572" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="287.4837825029382" cy="365.78631599178368" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="292.87151954103581" cy="304.65519131130236" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.99431800019977" cy="323.56205769674784" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="334.22721752914117" cy="321.46774192715469" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="295.6311506878875" cy="327.90072358841826" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.24892941176324" cy="317.6215188792799" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="349.89822692346752" cy="285.99065486581804" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="293.584780541231" cy="371.83094557100316" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.142783670548" cy="288.59709976568274" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="336.20885729808276" cy="341.21283423190658" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="302.47908057755876" cy="343.05461040033202" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="384.0" cy="331.29229390850372" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="353.71884120363882" cy="328.29981338887637" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="269.69538672406856" cy="305.64787193716484" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="268.83523708602979" cy="315.10219714135246" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.91949616933346" cy="311.80085961647012" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="307.10303265704511" cy="338.63147693603605" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="300.33607788139409" cy="327.23533905059514" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="362.90965001301265" cy="296.90068162179256" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="296.89565254107583" cy="346.43097860747736" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="300.90007943144462" cy="255.32566561131978" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="302.47194007630424" cy="314.36104572351417" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="280.96702222064198" cy="299.09408705123411" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.7285191806526" cy="286.10069407342104" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="340.24286844759018" cy="322.16955036281456" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="333.40674827285272" cy="351.49823871980146" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.85262741263023" cy="265.19147954931429" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.79335307948708" cy="303.44373572412769" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="288.52496822882586" cy="275.69302548963157" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="356.62381041315592" cy="367.69393434422187" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="285.76387560412445" cy="304.37925176446549" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.56111701191276" cy="280.89912761952854" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="304.95749823987887" cy="296.95348936253981" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.54152504673016" cy="365.47016307708265" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="329.22399686548897" cy="308.99463496013612" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="331.60151566985894" cy="297.46075324844696" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="349.27009621879688" cy="377.1049551233275" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="295.18346319866669" cy="309.92615889715756" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="302.16311639915125" cy="371.29250756131199" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.17740118662812" cy="337.0212469254318" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.93880800532054" cy="322.07257273057456" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.17414396200866" cy="288.93059885072353" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="327.26064592937621" cy="299.92380910421252" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="276.83243686859851" cy="270.75166877797722" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="256.77296513950893" cy="309.56488701153211" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="284.0" y="250.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="329.0" y="257.0"></text></g><g class="toyplot-axes-Axis" id="t07106ac03c6244ea9b4b3c0a860b3f28" transform="translate(240.0,384.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="144.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(12.073096178410712,0) rotate(0)" x="0" y="0">-2</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(43.85186272234113,0) rotate(0)" x="0" y="0">-1</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.63062926627154,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(107.40939581020197,0) rotate(0)" x="0" y="0">1</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(139.18816235413237,0) rotate(0)" x="0" y="0">2</text></g></g><g class="toyplot-axes-Axis" id="t5e7713e8d0bd48af8d8cae6cc312eca6" transform="translate(240.0,384.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="144.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(17.65278210013972,0) rotate(0)" x="0" y="0">-2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(77.51233782721155,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(137.37189355428342,0) rotate(0)" x="0" y="0">2</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t82c42b3959cb45199c9047272f08570b text");
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
          var text = document.querySelectorAll("#t82c42b3959cb45199c9047272f08570b text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.14285714285714285, 0.20203050891044214, 0.24743582965269675, 0.2857142857142857, 0.3194382824999699, 0.3499271061118826, 0.3779644730092272, 0.40406101782088427, 0.42857142857142855, 0.4517539514526256, 0.4738035414793428, 0.4948716593053935, 0.5150787536377127, 0.5345224838248488, 0.5532833351724881, 0.5714285714285714, 0.5890150893739515, 0.6060915267313264, 0.6226998490772391, 0.6388765649999398, 0.6546536707079771, 0.6700593942604899, 0.6851187890446742, 0.6998542122237652, 0.7142857142857143, 0.7284313590846835, 0.7423074889580902, 0.7559289460184544, 0.769309258162072, 0.7824607964359516, 0.7953949089757174, 0.8081220356417685, 0.8206518066482897, 0.8329931278350429, 0.8451542547285166, 0.8571428571428571, 0.8689660757568884, 0.8806305718527109, 0.8921425711997711, 0.9035079029052512, 0.9147320339189784, 0.9258200997725514, 0.9367769320431429, 0.9476070829586856, 0.9583148474999098, 0.9689042833036097, 0.9793792286287205, 0.989743318610787, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t24eb1628a5624dec82aafa6a3e3e8fda", "filename": "toyplot"}, {"data": [[-0.7910272468178489, 1.1531831586640633, 0.5843916167155364, -2.3799107860816773, 0.4571955048761698, 1.3894233094128812, 0.7761694518343318, -0.4247891131752235, 0.7362643228914545, 0.2052972288760687, -0.0880977841339548, -0.02654976711803326, -0.02468379932786014, 0.54341759164864, 1.1105173599232996, -1.4435217895944283, -2.0393070389678933, 0.6777765634859301, -0.19914287130397798, 1.1097106947587698, -0.012210702322388354, 0.06023073766262334, 0.8347912130001801, 0.026784783130367164, 0.9746577554087971, 0.610702033670404, 0.18035101942645268, -0.6689186632118731, 0.7926163861507155, 0.6509014580950933, 0.6340759363947618, 0.1705567321380737, -1.4886483379532964, 0.02004776293152387, -0.01525697441269833, 0.38587348914045155, 0.817311717214764, 0.8974787612716776, 1.0824287975981632, -0.5074905905200857, 0.21838309587692176, -0.5342599170788965, -0.8888023127746709, 0.11029740242482994, 0.11153119413020457, 0.6273123456969172, -0.045980238503560346, 0.6836174391888594, 0.4539869267646107, 0.9502570658983212, 1.746361402376814, 1.6621353241241623, 0.17323138876367591, 1.233426041520343, 1.4976627393335873, -0.8857123741547249, -0.7161734768331545, 1.4274842502530187, 0.5851891147871349, -0.6293346392389754, -0.2952191313510909, 1.0783174233595572, -0.6937288989666965, -1.1481831916063634, 0.6475464679651485, -0.4138470469120417, 2.1514167530453334, 1.1985428032492957, -1.4454696496386321, -1.4725364534067924, -0.27411803679969654, -0.26834259276356903, -0.4812820964506125, 1.4877550606435088, -0.5895438609707161, -0.4635343481460685, -0.4140717410091088, -1.0907788695231841, 0.003080356005816241, 0.7744869250131234, 0.5593709555091697, 1.4230255942704562, -0.15221724166347017, -0.8529488078140246, 1.289955073939579, -0.9398336345389563, -0.1595251422785973, -0.3358573093653057, -1.5761815094459077, 0.42775000660979573, 0.5025647040614216, 1.058551687524521, -0.6434222687447304, -0.42378966623840086, -0.5806779207158345, -0.2735103405897023, -1.1471963599929562, 0.36596815823633344, -1.2208841505550285, -1.8521066274047737], [1.0054717693841746, -0.8126827476044929, 0.5322567860532352, -0.36854915643045993, 0.27341217974593335, 1.3546390012387453, 0.5802476900137223, -1.870344786732475, -0.4247573343677771, 0.283559840517093, -0.4293054355737392, -1.6774302764916444, 0.6238211179443112, 0.25966978063872154, -0.08020029386682358, 0.7229330943025221, -1.1294853429155323, 0.5348943055559824, 0.28859958313474, -0.14713112619664392, -0.6467914747345449, 1.615463351993588, -0.39197041798073773, -0.8679222057075432, 0.8718296774741243, 1.4714193455470146, -0.20350398685501525, 0.007341825691493995, -1.24435911668532, -2.5898066527799553, 1.260508092478042, 2.0053266112860086, 1.483664480466584, 0.6123473700990678, 1.2696712170731175, 0.9496622982407078, -0.2437608510956255, 1.398024164077031, -0.40753492869972874, 0.9672694720801721, 0.6353534210798912, 0.39003646235375944, -0.323744963173085, 0.9678392024655399, 0.6253295765165219, -0.5221922157436077, -0.5820992464921625, -0.8333569591941152, 2.221455250217268, 0.3742209634618432, 0.6211063299947147, -0.17752880131637497, 1.6358055460730592, 1.4258016079029208, 1.5089962695285108, -1.9812594029052275, 0.061225675307085656, -0.5704818659800864, -0.5005075487919602, -0.7154433792747188, -0.37199930975953066, 0.6848365998714055, -2.1832197918790377, 0.597751259253485, -1.1602215097434632, -1.221758089694807, -0.8287609700550193, -0.7287775845026265, 0.02805868588308958, -0.2878248882381214, -0.1775221141936648, -1.0739743846348122, -0.69321185651311, 0.3203157936790412, -1.3345677544554262, 1.7094011453990918, -0.2630618772589703, 0.2470307382589055, 0.6811600203757365, -0.5239560501092704, -1.5038727234207225, 1.3797690985801196, 0.10170227331921479, 1.0288962659049548, -2.044995871686783, 0.07044524078782727, 0.8549523711779679, 0.318551405684314, -1.9706962468356242, -0.08376182405289373, 0.3016029375660411, -2.359432578234188, -0.11488547426067931, -2.165229748246032, -1.0201741186272901, -0.5207158779742737, 0.5866085409025061, 0.21930844587299012, 1.1939946082376078, -0.10281482384447307]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t635b7ca802324fb7a7bf1a2de912c6c9", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t82c42b3959cb45199c9047272f08570b .toyplot-mark-popup");
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
      var axes = {"taaf1115a864f4b9b92f65b86572dffb8": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 430.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 430.0}, "scale": "linear"}]}, "tc989931747ed457c80c3c9746fa33661": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.1514167530453334, "min": -2.3799107860816773}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 384.0, "min": 240.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.221455250217268, "min": -2.5898066527799553}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 240.0, "min": 384.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="tc70654d7604c479eae424a0c21fff230"><svg height="453.5433072px" id="t5e45043ed02d4979af68de77908d9de6" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 453.5433072 453.5433072" width="453.5433072px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t174be8dc5b6f43a199377e7f2f5d7b53"><clipPath id="tde2146d4aff2427abf3c65de95549a41"><rect height="95.59055120000002" width="95.59055120000002" x="27.795275600000004" y="27.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tde2146d4aff2427abf3c65de95549a41)" style="cursor:crosshair"><rect height="95.59055120000002" style="pointer-events:all;visibility:hidden" width="95.59055120000002" x="27.795275600000004" y="27.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="54.795275600000004"></text></g><g class="toyplot-axes-Axis" id="t0d2ae7ee63bb4cd3a2a4d97fa3d4e8a8" transform="translate(37.7952756,113.3858268) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0) rotate(0)" x="0" y="0">0.5</text></g></g><g class="toyplot-axes-Axis" id="t9387b4d891fa4547a52d9814a6a82e37" transform="translate(37.7952756,113.3858268) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0) rotate(0)" x="0" y="0">0.5</text></g></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="75.59055120000001" y="37.795275600000004">top-left</text></g><g class="toyplot-axes-Cartesian" id="t5daf07f7a3d74bad8bab436d3c35772e"><clipPath id="t12937b21753646c5911b757bf6218f8b"><rect height="95.59055120000002" width="95.5905512" x="178.976378" y="27.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t12937b21753646c5911b757bf6218f8b)" style="cursor:crosshair"><rect height="95.59055120000002" style="pointer-events:all;visibility:hidden" width="95.5905512" x="178.976378" y="27.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="164.5669292" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="209.5669292" y="54.795275600000004"></text></g><g class="toyplot-axes-Axis" id="t78178eb545404b09b957fc5c312c2576" transform="translate(188.976378,113.3858268) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">0.5</text></g></g><g class="toyplot-axes-Axis" id="tf9a0919d5a0d422583897df6915fb4b5" transform="translate(188.976378,113.3858268) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0) rotate(0)" x="0" y="0">0.5</text></g></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="226.7716536" y="37.795275600000004">top</text></g><g class="toyplot-axes-Cartesian" id="t970c37e1072649a3954b90ad6d022023"><clipPath id="t1aee9b935889437f8eeebdfb37523f89"><rect height="95.59055120000002" width="95.5905512" x="330.1574804" y="27.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t1aee9b935889437f8eeebdfb37523f89)" style="cursor:crosshair"><rect height="95.59055120000002" style="pointer-events:all;visibility:hidden" width="95.5905512" x="330.1574804" y="27.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="315.7480316" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.7480316" y="54.795275600000004"></text></g><g class="toyplot-axes-Axis" id="t3f08762dac154d10861d46b58393f0d5" transform="translate(340.1574804,113.3858268) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">0.5</text></g></g><g class="toyplot-axes-Axis" id="t02f19b566b74422f9365f930e04bdada" transform="translate(340.1574804,113.3858268) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0) rotate(0)" x="0" y="0">0.5</text></g></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="377.952756" y="37.795275600000004">top-right</text></g><g class="toyplot-axes-Cartesian" id="tf907a409f6fe47489b70dd666df10897"><clipPath id="t0d7d68f4bfdb46eaaf46474aa2e0f623"><rect height="95.5905512" width="95.5905512" x="330.1574804" y="178.976378"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t0d7d68f4bfdb46eaaf46474aa2e0f623)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.5905512" x="330.1574804" y="178.976378"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="315.7480316" y="198.976378"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.7480316" y="205.976378"></text></g><g class="toyplot-axes-Axis" id="t98146798cc644b5498e599863a8ed559" transform="translate(340.1574804,264.5669292) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">0.5</text></g></g><g class="toyplot-axes-Axis" id="td9d484ddaf304d558342ebd5afe60373" transform="translate(340.1574804,264.5669292) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">0.5</text></g></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="377.952756" y="188.976378">right</text></g><g class="toyplot-axes-Cartesian" id="td71f87d3c3db467dbf5fb80d8a2a20f4"><clipPath id="te4bc2bfe9dc243d7817a20766e6af3de"><rect height="95.5905512" width="95.5905512" x="330.1574804" y="330.1574804"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te4bc2bfe9dc243d7817a20766e6af3de)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.5905512" x="330.1574804" y="330.1574804"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="315.7480316" y="350.1574804"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.7480316" y="357.1574804"></text></g><g class="toyplot-axes-Axis" id="te4c58b76d1e44e51854aeb3eac6ddb02" transform="translate(340.1574804,415.7480316) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">0.5</text></g></g><g class="toyplot-axes-Axis" id="t55849f106806466989151d62ce393c1d" transform="translate(340.1574804,415.7480316) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">0.5</text></g></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="377.952756" y="340.1574804">bottom-right</text></g><g class="toyplot-axes-Cartesian" id="t1b2ed5c2a61043f0b95b749e05706bcd"><clipPath id="td1021ac2bbed49838599da9132dff4e8"><rect height="95.5905512" width="95.5905512" x="178.976378" y="330.1574804"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td1021ac2bbed49838599da9132dff4e8)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.5905512" x="178.976378" y="330.1574804"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="164.5669292" y="350.1574804"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="209.5669292" y="357.1574804"></text></g><g class="toyplot-axes-Axis" id="t61e08c9fcf9642a8a138fb22f873de39" transform="translate(188.976378,415.7480316) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">0.5</text></g></g><g class="toyplot-axes-Axis" id="t47828709c0d3472daa4c1e66828c15ad" transform="translate(188.976378,415.7480316) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">0.5</text></g></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="226.7716536" y="340.1574804">bottom</text></g><g class="toyplot-axes-Cartesian" id="t3f1ae4098ee64145bfe5abecc986ac85"><clipPath id="t62f2a6a0d9974394809c211d0974ab3e"><rect height="95.5905512" width="95.59055120000002" x="27.795275600000004" y="330.1574804"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t62f2a6a0d9974394809c211d0974ab3e)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.59055120000002" x="27.795275600000004" y="330.1574804"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="350.1574804"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="357.1574804"></text></g><g class="toyplot-axes-Axis" id="t80f4c96e091d4323b0e74d544edbcf4f" transform="translate(37.7952756,415.7480316) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0) rotate(0)" x="0" y="0">0.5</text></g></g><g class="toyplot-axes-Axis" id="t9930b151bc534a8ebeaba3df9e37b896" transform="translate(37.7952756,415.7480316) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">0.5</text></g></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="75.59055120000001" y="340.1574804">bottom-left</text></g><g class="toyplot-axes-Cartesian" id="tb96c04627fc64f58bbd355a5525ffc51"><clipPath id="t10251a6bba6f4072a4adc3a218f500a9"><rect height="95.5905512" width="95.59055120000002" x="27.795275600000004" y="178.976378"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t10251a6bba6f4072a4adc3a218f500a9)" style="cursor:crosshair"><rect height="95.5905512" style="pointer-events:all;visibility:hidden" width="95.59055120000002" x="27.795275600000004" y="178.976378"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="198.976378"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="205.976378"></text></g><g class="toyplot-axes-Axis" id="t29b208108d5c4c2fac23e187b3ca51a8" transform="translate(37.7952756,264.5669292) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="75.590551200000021" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.79527560000001,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.59055120000002,0) rotate(0)" x="0" y="0">0.5</text></g></g><g class="toyplot-axes-Axis" id="t8d504030a292471190053ddd91145b27" transform="translate(37.7952756,264.5669292) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="75.590551199999993" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(37.7952756,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.5905512,0) rotate(0)" x="0" y="0">0.5</text></g></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="75.59055120000001" y="188.976378">left</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tc70654d7604c479eae424a0c21fff230 text");
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
          var text = document.querySelectorAll("#tc70654d7604c479eae424a0c21fff230 text");
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
      var axes = {"t174be8dc5b6f43a199377e7f2f5d7b53": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 113.38582680000002, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 37.795275600000004, "min": 113.38582680000002}, "scale": "linear"}]}, "t1b2ed5c2a61043f0b95b749e05706bcd": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 264.5669292, "min": 188.976378}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 340.1574804, "min": 415.7480316}, "scale": "linear"}]}, "t3f1ae4098ee64145bfe5abecc986ac85": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 113.38582680000002, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 340.1574804, "min": 415.7480316}, "scale": "linear"}]}, "t5daf07f7a3d74bad8bab436d3c35772e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 264.5669292, "min": 188.976378}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 37.795275600000004, "min": 113.38582680000002}, "scale": "linear"}]}, "t970c37e1072649a3954b90ad6d022023": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 415.7480316, "min": 340.1574804}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 37.795275600000004, "min": 113.38582680000002}, "scale": "linear"}]}, "tb96c04627fc64f58bbd355a5525ffc51": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 113.38582680000002, "min": 37.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 188.976378, "min": 264.5669292}, "scale": "linear"}]}, "td71f87d3c3db467dbf5fb80d8a2a20f4": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 415.7480316, "min": 340.1574804}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 340.1574804, "min": 415.7480316}, "scale": "linear"}]}, "tf907a409f6fe47489b70dd666df10897": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 415.7480316, "min": 340.1574804}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 188.976378, "min": 264.5669292}, "scale": "linear"}]}};
    
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


