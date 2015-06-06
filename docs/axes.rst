
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _axes:

Axes
====

In Toyplot, axes are used to map data values into canvas coordinates.
The axes *range* (the area on the canvas that they occupy) is specified
when they are created. Their *domain* is implicitly defined to include
all of the data in the plot (but can be manually overridden by the
caller if desired).

Layout
------

When using Toyplot's :ref:`convenience` API, axes are created
automatically and returned from the function within a
``(canvas, axes, mark)`` tuple. By default, the axes are sized to fill
the entire canvas:

.. code:: python

    import numpy
    y = numpy.linspace(0, 1, 20) ** 2

.. code:: python

    import toyplot
    toyplot.plot(y, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t8cefa45c89184067b9b136c1bc2d7099"><svg height="300.0px" id="te020356710bf48548a251f5be8b0394d" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t414d5d1caeed41beb35dfda67379421f"><clipPath id="t8deecf8642bf4773a9f262a6c57f54d3"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t8deecf8642bf4773a9f262a6c57f54d3)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t4a744fabe3f24a93af3330e8749ef455" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t8cefa45c89184067b9b136c1bc2d7099 text");
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
          var text = document.querySelectorAll("#t8cefa45c89184067b9b136c1bc2d7099 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t4a744fabe3f24a93af3330e8749ef455", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t8cefa45c89184067b9b136c1bc2d7099 .toyplot-mark-popup");
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
      var axes = {"t414d5d1caeed41beb35dfda67379421f": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t245796c3978a466eb0dedf6b48db6cff"><svg height="300.0px" id="t924498b278e9427aa044940c8e6fb921" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t8a6d2720154c4e35b552f39fc4e68fd7"><clipPath id="t533afb8666fe495f947458589745533f"><rect height="260.0" width="260.0" x="20.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t533afb8666fe495f947458589745533f)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="20.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="t1f7db52511ee42269c751c549f4922e0" style="fill:none"><g class="toyplot-Series"><path d="M 30.0 270.0 L 42.0 269.33518005540168 L 54.0 267.34072022160666 L 66.0 264.016620498615 L 78.0 259.36288088642664 L 90.0 253.37950138504155 L 102.0 246.06648199445985 L 114.0 237.42382271468145 L 126.0 227.45152354570638 L 138.0 216.14958448753464 L 150.0 203.51800554016617 L 162.0 189.55678670360109 L 174.0 174.26592797783934 L 186.0 157.64542936288092 L 198.0 139.6952908587258 L 210.0 120.41551246537395 L 222.0 99.806094182825504 L 234.0 77.867036011080387 L 246.0 54.598337950138536 L 258.0 30.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="180.0" y="30.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="225.0" y="37.0"></text></g><line style="" x1="30.0" x2="258.0" y1="280.0" y2="280.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="30.0" y="280.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="90.0" y="280.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="280.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="210.0" y="280.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="270.0" y="280.0">20</text></g><line style="" x1="20.0" x2="20.0" y1="30.0" y2="270.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 270.0)" x="20.0" y="270.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 150.0)" x="20.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 30.0)" x="20.0" y="30.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t872873a1b27b40edb6fb526c83117021"><clipPath id="te7c35a24647b4c42a1666d22dfbe6454"><rect height="260.0" width="260.0" x="320.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te7c35a24647b4c42a1666d22dfbe6454)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="320.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="tcddb990ca2ea40aaa9d76689f958099c" style="fill:none"><g class="toyplot-Series"><path d="M 330.0 30.0 L 342.0 30.664819944598332 L 354.0 32.659279778393355 L 366.0 35.983379501385038 L 378.0 40.637119113573412 L 390.0 46.62049861495845 L 402.0 53.933518005540151 L 414.0 62.576177285318565 L 426.0 72.54847645429362 L 438.0 83.850415512465361 L 450.0 96.4819944598338 L 462.0 110.44321329639889 L 474.0 125.73407202216066 L 486.0 142.35457063711908 L 498.0 160.3047091412742 L 510.0 179.58448753462605 L 522.0 200.19390581717448 L 534.0 222.13296398891964 L 546.0 245.40166204986147 L 558.0 270.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="480.0" y="30.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="525.0" y="37.0"></text></g><line style="" x1="330.0" x2="558.0" y1="280.0" y2="280.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.0" y="280.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="390.0" y="280.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="280.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="510.0" y="280.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="570.0" y="280.0">20</text></g><line style="" x1="320.0" x2="320.0" y1="30.0" y2="270.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 270.0)" x="320.0" y="270.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 150.0)" x="320.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 30.0)" x="320.0" y="30.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t245796c3978a466eb0dedf6b48db6cff text");
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
          var text = document.querySelectorAll("#t245796c3978a466eb0dedf6b48db6cff text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t1f7db52511ee42269c751c549f4922e0", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "names": ["x", "y0"], "id": "tcddb990ca2ea40aaa9d76689f958099c", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t245796c3978a466eb0dedf6b48db6cff .toyplot-mark-popup");
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
      var axes = {"t872873a1b27b40edb6fb526c83117021": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 570.0, "min": 330.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}, "t8a6d2720154c4e35b552f39fc4e68fd7": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 270.0, "min": 30.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="tfb229ac1ca4a49edbe20e2dd04b2a588"><svg height="300.0px" id="t49b4880aac264609961919ebb2c42fd1" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td33e691f7a9c4c5c9e55de17db26ed0a"><clipPath id="t1bb48b038a7b4c7bb5792a689676c246"><rect height="260.0" width="260.0" x="20.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t1bb48b038a7b4c7bb5792a689676c246)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="20.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="tb051dc0f64f849ecb56853441473b3b2" style="fill:none"><g class="toyplot-Series"><path d="M 30.0 270.0 L 42.0 269.33518005540168 L 54.0 267.34072022160666 L 66.0 264.016620498615 L 78.0 259.36288088642664 L 90.0 253.37950138504155 L 102.0 246.06648199445985 L 114.0 237.42382271468145 L 126.0 227.45152354570638 L 138.0 216.14958448753464 L 150.0 203.51800554016617 L 162.0 189.55678670360109 L 174.0 174.26592797783934 L 186.0 157.64542936288092 L 198.0 139.6952908587258 L 210.0 120.41551246537395 L 222.0 99.806094182825504 L 234.0 77.867036011080387 L 246.0 54.598337950138536 L 258.0 30.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="180.0" y="30.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="225.0" y="37.0"></text></g><line style="" x1="30.0" x2="258.0" y1="280.0" y2="280.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="30.0" y="280.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="90.0" y="280.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="280.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="210.0" y="280.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="270.0" y="280.0">20</text></g><line style="" x1="20.0" x2="20.0" y1="30.0" y2="270.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 270.0)" x="20.0" y="270.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 150.0)" x="20.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 20.0, 30.0)" x="20.0" y="30.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t9039921d73474d4d9a4627230e3d4208"><clipPath id="t73b2b235f6eb4dd482820e88bb92b81b"><rect height="260.0" width="260.0" x="320.0" y="20.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t73b2b235f6eb4dd482820e88bb92b81b)" style="cursor:crosshair"><rect height="260.0" style="pointer-events:all;visibility:hidden" width="260.0" x="320.0" y="20.0"></rect><g class="toyplot-mark-Plot" id="teda51fa617af4adcacc9759f12eaa4e0" style="fill:none"><g class="toyplot-Series"><path d="M 330.0 30.0 L 342.0 30.664819944598332 L 354.0 32.659279778393355 L 366.0 35.983379501385038 L 378.0 40.637119113573412 L 390.0 46.62049861495845 L 402.0 53.933518005540151 L 414.0 62.576177285318565 L 426.0 72.54847645429362 L 438.0 83.850415512465361 L 450.0 96.4819944598338 L 462.0 110.44321329639889 L 474.0 125.73407202216066 L 486.0 142.35457063711908 L 498.0 160.3047091412742 L 510.0 179.58448753462605 L 522.0 200.19390581717448 L 534.0 222.13296398891964 L 546.0 245.40166204986147 L 558.0 270.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="480.0" y="30.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="525.0" y="37.0"></text></g><line style="" x1="330.0" x2="558.0" y1="280.0" y2="280.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.0" y="280.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="390.0" y="280.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="280.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="510.0" y="280.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="570.0" y="280.0">20</text></g><line style="" x1="320.0" x2="320.0" y1="30.0" y2="270.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 270.0)" x="320.0" y="270.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 150.0)" x="320.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 320.0, 30.0)" x="320.0" y="30.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tfb229ac1ca4a49edbe20e2dd04b2a588 text");
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
          var text = document.querySelectorAll("#tfb229ac1ca4a49edbe20e2dd04b2a588 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "tb051dc0f64f849ecb56853441473b3b2", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "names": ["x", "y0"], "id": "teda51fa617af4adcacc9759f12eaa4e0", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tfb229ac1ca4a49edbe20e2dd04b2a588 .toyplot-mark-popup");
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
      var axes = {"t9039921d73474d4d9a4627230e3d4208": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 570.0, "min": 330.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}, "td33e691f7a9c4c5c9e55de17db26ed0a": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 270.0, "min": 30.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 30.0, "min": 270.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t922c51335b054f00892ac0d6a87ae239"><svg height="192.0px" id="t47dc8a11d8bd421ba97f23926b862eb3" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="755.9055119999999px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t2f8ef93efa404642a24af72d92146002"><clipPath id="t2309aceb63864c729d7d665103723b25"><rect height="153.60000000000002" width="151.1811024" x="37.795275600000004" y="19.200000000000003"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2309aceb63864c729d7d665103723b25)" style="cursor:crosshair"><rect height="153.60000000000002" style="pointer-events:all;visibility:hidden" width="151.1811024" x="37.795275600000004" y="19.200000000000003"></rect><g class="toyplot-mark-Plot" id="t1b2473a359154a8ca38c0c62c6f76b80" style="fill:none"><g class="toyplot-Series"><path d="M 47.795275600000004 162.80000000000001 L 54.35433072 162.42991689750693 L 60.913385840000004 161.31966759002771 L 67.47244096 159.46925207756234 L 74.031496080000011 156.87867036011082 L 80.590551199999993 153.54792243767315 L 87.149606320000004 149.47700831024935 L 93.708661439999986 144.66592797783935 L 100.26771656 139.11468144044323 L 106.82677168000001 132.82326869806096 L 113.38582679999999 125.79168975069251 L 119.94488192 118.01994459833796 L 126.50393704 109.50803324099725 L 133.06299215999999 100.25595567867038 L 139.62204727999998 90.263711911357362 L 146.18110239999999 79.531301939058181 L 152.74015752 68.058725761772877 L 159.29921263999998 55.845983379501419 L 165.85826775999999 42.893074792243787 L 172.41732287999997 29.200000000000003" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="88.97637799999998" y="29.200000000000003"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="133.97637799999998" y="36.2"></text></g><line style="" x1="47.795275600000004" x2="172.41732287999997" y1="172.8" y2="172.8"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="47.795275600000004" y="172.8">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="80.5905512" y="172.8">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="113.38582679999999" y="172.8">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="146.1811024" y="172.8">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="178.97637799999998" y="172.8">20</text></g><line style="" x1="37.795275600000004" x2="37.795275600000004" y1="29.200000000000003" y2="162.8"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 162.8)" x="37.795275600000004" y="162.8">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 96.0)" x="37.795275600000004" y="96.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 29.200000000000003)" x="37.795275600000004" y="29.200000000000003">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="te13d8130ff154645885fe5bb55087e9d"><clipPath id="tca9adea7cc574edb8de14e9adf4f7931"><rect height="153.60000000000002" width="491.3385827999999" x="226.7716536" y="19.200000000000003"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tca9adea7cc574edb8de14e9adf4f7931)" style="cursor:crosshair"><rect height="153.60000000000002" style="pointer-events:all;visibility:hidden" width="491.3385827999999" x="226.7716536" y="19.200000000000003"></rect><g class="toyplot-mark-Plot" id="tc383a37b95ae466e85075062d4784fb7" style="fill:none"><g class="toyplot-Series"><path d="M 236.77165360000001 29.200000000000003 L 260.33858273999999 29.570083102493072 L 283.90551188000001 30.680332409972301 L 307.47244102000002 32.530747922437676 L 331.03937016000003 35.121329639889204 L 354.60629929999999 38.45207756232687 L 378.17322844 42.52299168975069 L 401.74015757999996 47.334072022160669 L 425.30708672000003 52.885318559556787 L 448.87401585999999 59.176731301939057 L 472.440945 66.208310249307488 L 496.00787414000001 73.980055401662057 L 519.57480327999997 82.491966759002764 L 543.14173241999993 91.744044321329639 L 566.70866155999988 101.73628808864265 L 590.27559069999995 112.46869806094185 L 613.84251984000002 123.94127423822714 L 637.40944897999998 136.1540166204986 L 660.97637811999994 149.10692520775623 L 684.54330726000001 162.80000000000001" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="618.1102364" y="29.200000000000003"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="663.1102364" y="36.2"></text></g><line style="" x1="236.7716536" x2="684.54330726" y1="172.8" y2="172.8"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="236.7716536" y="172.8">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="354.6062993" y="172.8">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="472.440945" y="172.8">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="590.2755907" y="172.8">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="708.1102364" y="172.8">20</text></g><line style="" x1="226.7716536" x2="226.7716536" y1="29.200000000000003" y2="162.8"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 226.7716536, 162.8)" x="226.7716536" y="162.8">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 226.7716536, 96.0)" x="226.7716536" y="96.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 226.7716536, 29.200000000000003)" x="226.7716536" y="29.200000000000003">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t922c51335b054f00892ac0d6a87ae239 text");
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
          var text = document.querySelectorAll("#t922c51335b054f00892ac0d6a87ae239 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t1b2473a359154a8ca38c0c62c6f76b80", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "names": ["x", "y0"], "id": "tc383a37b95ae466e85075062d4784fb7", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t922c51335b054f00892ac0d6a87ae239 .toyplot-mark-popup");
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
      var axes = {"t2f8ef93efa404642a24af72d92146002": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 178.97637799999998, "min": 47.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 29.200000000000003, "min": 162.8}, "scale": "linear"}]}, "te13d8130ff154645885fe5bb55087e9d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 708.1102364, "min": 236.7716536}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 29.200000000000003, "min": 162.8}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="tbb331cecadf84699affb66a724965803"><svg height="300.0px" id="t76b00f620f6f48c19d683fa70b3133d1" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tb2ca5ffcfaac49bfbb56d8e1bae7120b"><clipPath id="t74286c8733c94850a93697284029a619"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t74286c8733c94850a93697284029a619)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t4d6a6ec431bb48af9f55e8415a96da0c" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="te2443e08df0b4665bd03df62ff33f4c2"><clipPath id="tfb879512ce7f43f2bed2b0f0862df3cd"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tfb879512ce7f43f2bed2b0f0862df3cd)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="te15669d1426f42dd8ef1d24dc4cee9f8" style="fill:none"><g class="toyplot-Series"><path d="M 360.0 60.0 L 369.0 60.498614958448755 L 378.0 61.99445983379502 L 387.0 64.48753462603878 L 396.0 67.97783933518005 L 405.0 72.46537396121883 L 414.0 77.95013850415512 L 423.0 84.43213296398892 L 432.0 91.911357340720215 L 441.0 100.38781163434902 L 450.0 109.86149584487535 L 459.0 120.33240997229916 L 468.0 131.80055401662048 L 477.0 144.26592797783931 L 486.0 157.72853185595568 L 495.0 172.18836565096953 L 504.0 187.64542936288086 L 513.0 204.0997229916897 L 522.0 221.55124653739611 L 531.0 240.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tbb331cecadf84699affb66a724965803 text");
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
          var text = document.querySelectorAll("#tbb331cecadf84699affb66a724965803 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t4d6a6ec431bb48af9f55e8415a96da0c", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "names": ["x", "y0"], "id": "te15669d1426f42dd8ef1d24dc4cee9f8", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tbb331cecadf84699affb66a724965803 .toyplot-mark-popup");
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
      var axes = {"tb2ca5ffcfaac49bfbb56d8e1bae7120b": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "te2443e08df0b4665bd03df62ff33f4c2": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


You can also use the *gutter* argument to control the space between
cells in the grid:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(grid=(1, 2, 0), gutter=15)
    axes1.plot(y)
    axes2 = canvas.axes(grid=(1, 2, 1), gutter=15)
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="t832308c7ab5b42128b5883292d63c952"><svg height="300.0px" id="ta59415cfbca648fda4901157ffd1c0d4" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc93430f7a6114131931891e27f6cab71"><clipPath id="td3a10505d5754b7b8c4d5dd5be6fe7d1"><rect height="270.0" width="270.0" x="15.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td3a10505d5754b7b8c4d5dd5be6fe7d1)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="15.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="t0bae8c66b1924a998a21eb2b92034e74" style="fill:none"><g class="toyplot-Series"><path d="M 25.0 275.0 L 37.5 274.30747922437678 L 50.0 272.22991689750694 L 62.5 268.7673130193906 L 75.0 263.91966759002764 L 87.5 257.6869806094183 L 100.0 250.06925207756234 L 112.5 241.06648199445985 L 125.0 230.6786703601108 L 137.5 218.90581717451525 L 150.0 205.74792243767311 L 162.5 191.20498614958447 L 175.0 175.27700831024933 L 187.5 157.96398891966763 L 200.0 139.26592797783937 L 212.5 119.18282548476454 L 225.0 97.714681440443243 L 237.5 74.861495844875392 L 250.0 50.623268698060976 L 262.5 25.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="185.0" y="25.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="230.0" y="32.0"></text></g><line style="" x1="25.0" x2="262.5" y1="285.0" y2="285.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="25.0" y="285.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="87.5" y="285.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="285.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="212.5" y="285.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="275.0" y="285.0">20</text></g><line style="" x1="15.0" x2="15.0" y1="25.0" y2="275.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 275.0)" x="15.0" y="275.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 150.0)" x="15.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 25.0)" x="15.0" y="25.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t89f0ae44716e40e88b725d870552a0d1"><clipPath id="t7d67d00ff56a420a83a7d334fbcd8a93"><rect height="270.0" width="270.0" x="315.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t7d67d00ff56a420a83a7d334fbcd8a93)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="315.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="t2af9077e2007487ea03189ecc1c99bad" style="fill:none"><g class="toyplot-Series"><path d="M 325.0 25.0 L 337.5 25.692520775623262 L 350.0 27.770083102493075 L 362.5 31.232686980609415 L 375.0 36.080332409972307 L 387.5 42.313019390581722 L 400.0 49.930747922437654 L 412.5 58.933518005540179 L 425.0 69.321329639889186 L 437.5 81.094182825484751 L 450.0 94.252077562326889 L 462.5 108.79501385041551 L 475.0 124.72299168975069 L 487.5 142.03601108033237 L 500.0 160.73407202216066 L 512.5 180.81717451523545 L 525.0 202.28531855955674 L 537.5 225.13850415512462 L 550.0 249.37673130193903 L 562.5 275.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="485.0" y="25.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="530.0" y="32.0"></text></g><line style="" x1="325.0" x2="562.5" y1="285.0" y2="285.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="325.0" y="285.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="387.5" y="285.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="285.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="512.5" y="285.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="575.0" y="285.0">20</text></g><line style="" x1="315.0" x2="315.0" y1="25.0" y2="275.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 315.0, 275.0)" x="315.0" y="275.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 315.0, 150.0)" x="315.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 315.0, 25.0)" x="315.0" y="25.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t832308c7ab5b42128b5883292d63c952 text");
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
          var text = document.querySelectorAll("#t832308c7ab5b42128b5883292d63c952 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t0bae8c66b1924a998a21eb2b92034e74", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "names": ["x", "y0"], "id": "t2af9077e2007487ea03189ecc1c99bad", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t832308c7ab5b42128b5883292d63c952 .toyplot-mark-popup");
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
      var axes = {"t89f0ae44716e40e88b725d870552a0d1": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 575.0, "min": 325.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}, "tc93430f7a6114131931891e27f6cab71": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 275.0, "min": 25.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="tcdb884241af5480dac668a034db762bc"><svg height="480.0px" id="tae844c2714074f0d83c6ba7f3897e065" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="480.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t2303d2c886b242aba2b77257886c8a2d"><clipPath id="t224f45ad0978410f9ec5985c5eab5000"><rect height="380.0" width="380.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t224f45ad0978410f9ec5985c5eab5000)" style="cursor:crosshair"><rect height="380.0" style="pointer-events:all;visibility:hidden" width="380.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t3a852160c96a42d3b8d899153b603eac" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 420.0 L 67.200000000000003 368.57142857142856 L 74.399999999999991 347.26901679224085 L 81.599999999999994 330.92310132502917 L 88.800000000000011 317.14285714285717 L 96.0 305.00221830001078 L 103.19999999999999 294.02624179972224 L 110.40000000000001 283.93278971667826 L 117.59999999999999 274.53803358448164 L 124.8 265.71428571428572 L 132.0 257.36857747705477 L 139.20000000000002 249.43072506743661 L 146.40000000000001 241.84620265005836 L 153.59999999999999 234.57164869042342 L 160.80000000000001 227.57190582305444 L 168.0 220.8179993379043 L 175.19999999999999 214.28571428571428 L 182.40000000000001 207.95456782537747 L 189.59999999999999 201.80705037672249 L 196.80000000000001 195.82805433219391 L 204.0 190.00443660002168 L 211.20000000000002 184.32467854512825 L 218.40000000000001 178.77861806622366 L 225.60000000000002 173.35723594391732 L 232.80000000000001 168.05248359944454 L 240.0 162.85714285714286 L 247.19999999999999 157.76471072951395 L 254.40000000000001 152.76930397508752 L 261.60000000000002 147.8655794333564 L 268.80000000000001 143.0486670616541 L 276.0 138.31411328305745 L 283.19999999999999 133.65783276874174 L 290.40000000000003 129.07606716896333 L 297.59999999999997 124.5653496066157 L 304.80000000000001 120.12247397938457 L 312.0 115.74446829773404 L 319.19999999999999 111.42857142857144 L 326.40000000000003 107.17221272752016 L 333.59999999999997 102.97299413302409 L 340.80000000000001 98.828674368082389 L 348.0 94.73715495410957 L 355.19999999999999 90.69646778916777 L 362.40000000000003 86.704764081881493 L 369.59999999999997 82.760304464468533 L 376.80000000000001 78.861450134873195 L 384.0 75.006654900032473 L 391.20000000000005 71.194458010700515 L 398.39999999999998 67.423477693660615 L 405.59999999999997 63.692405300116675 L 412.79999999999995 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="330.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="375.0" y="67.0"></text></g><line style="" x1="60.0" x2="412.79999999999995" y1="430.0" y2="430.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="430.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="132.0" y="430.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="204.0" y="430.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="276.0" y="430.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="348.0" y="430.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="420.0" y="430.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="420.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 420.0)" x="50.0" y="420.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t27f12f1382c24d43b5624e5699c4f649"><clipPath id="t91caac8672244d8ca54edb0eb25c8e57"><rect height="144.0" width="144.0" x="240.0" y="240.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t91caac8672244d8ca54edb0eb25c8e57)" style="cursor:crosshair"><rect height="144.0" style="pointer-events:all;visibility:hidden" width="144.0" x="240.0" y="240.0"></rect><g class="toyplot-mark-Plot" id="t960b4b83aaa6442799f3800662149732" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="308.18596922092735" cy="334.3130949981599" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="289.27182707097182" cy="304.91489571821955" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="374.0" cy="296.82792235694353" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="274.94494256913788" cy="296.22464198037483" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="306.6914132859165" cy="304.53663993855787" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="330.13558998073188" cy="296.55550852031422" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="317.31461802025092" cy="333.95444473587537" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="321.04961729617685" cy="343.55153596997877" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="293.070750042035" cy="347.32756479136356" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="304.60370590960486" cy="311.08341951673719" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="330.0947522777542" cy="339.76889548435565" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="286.0661070514135" cy="316.18146485764174" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="304.54632925696131" cy="283.30750702295137" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="294.02682964741712" cy="340.95523345686996" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="295.23557763153195" cy="269.25321578032288" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="299.43590379048874" cy="315.31861315893292" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="302.24004347023947" cy="268.38303662725173" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="335.44430730631882" cy="332.00184779915151" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="317.85845946925156" cy="337.78181066740359" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="304.24190022045047" cy="301.81298504109583" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="281.51605179598505" cy="308.15825687624078" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="307.66726938938109" cy="313.57473289530992" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="307.2519785095559" cy="320.05890024907563" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="255.13373937063341" cy="308.43596256758724" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="281.25305201398982" cy="305.21730316795521" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="353.4907802990092" cy="345.11595279735684" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="318.77264131410288" cy="341.29952480327779" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="338.41057251035176" cy="291.35108112636703" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="343.14668970618197" cy="312.63518091584643" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="275.95230600989584" cy="326.99661834156524" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="315.10154938478348" cy="352.66234661845567" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="305.71739237479767" cy="308.06928341540691" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="305.94837745147794" cy="316.62480862111755" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="299.56414071018798" cy="347.34315247543634" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="334.7799628907884" cy="293.40216385806491" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="275.14974946406068" cy="323.62606005920736" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="299.3895310885905" cy="307.1337779352499" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="287.50671582965407" cy="348.82200636916423" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="322.14256395531288" cy="326.30078110964564" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="324.85379700118176" cy="315.17125506620249" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="274.29434868471685" cy="360.1070873780651" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="258.3109551231102" cy="305.03708316526979" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="332.67719859503404" cy="292.71533765980359" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="313.45693291729327" cy="327.6084664867642" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="269.91647084326314" cy="322.33377124086292" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="313.44501629589706" cy="313.58081907754263" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="278.02257199281576" cy="370.56370360661822" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="285.67996618049028" cy="322.88161748451751" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="288.65510335445265" cy="250.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="308.47139686672165" cy="296.73953082305218" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="313.54695389316635" cy="296.33614731852902" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="285.58057894712709" cy="323.77002155840285" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="262.84447865143511" cy="339.41955160558058" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="283.48140759572402" cy="316.87395215878428" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="320.83575442493049" cy="321.24999811681283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="319.73414850449291" cy="339.10546050893231" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="289.04005232284766" cy="278.98940636101781" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="336.76464811324934" cy="338.38199714058635" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="265.81875003172587" cy="299.78854296618715" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="279.913605253676" cy="334.99901343494116" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="274.12222377171804" cy="309.95759854148332" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="323.11616739095518" cy="293.19742280848573" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="302.72678075607462" cy="271.74916822613255" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="358.10089269907667" cy="329.29373785838811" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="367.81726341458022" cy="339.16904267275021" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="307.0476250901786" cy="354.4907436325617" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="287.56265149414389" cy="262.43025692775382" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="304.51821467957831" cy="329.02711380896596" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="323.05164188091339" cy="299.11504334112772" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="302.71478340641443" cy="312.01310571149719" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="315.96240642461981" cy="311.01512518433447" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="329.58719098917993" cy="326.5204985226805" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="293.04957388677133" cy="302.06079154325982" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="299.31314891610964" cy="341.621877891439" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="304.24610945433756" cy="293.873329651539" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="309.38480609886631" cy="275.82494133785644" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="264.93132384358717" cy="374.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="297.46270286764872" cy="293.73513612847421" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="301.39016754140005" cy="274.76635123153937" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="304.43719724730778" cy="323.13758405953308" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="315.71295272209284" cy="320.48667222965719" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="286.63698577214802" cy="317.92914511398965" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="322.35063280968376" cy="338.01766784076216" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="287.78379744771053" cy="313.37130367590078" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="310.8713344678622" cy="326.67459407228637" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="295.63231171876635" cy="328.32582337883457" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="305.26633550416193" cy="337.01440006208435" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="299.55824282292895" cy="317.90645347226155" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="316.17803447404799" cy="331.5452991892825" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="306.62596247045246" cy="354.17947058628164" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="282.1603513156453" cy="333.32882233403836" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="271.43163938973191" cy="345.1684358212741" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="303.89493235960902" cy="337.02469518176576" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="316.14661770505961" cy="284.40139871506432" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="274.13039406798464" cy="292.58969436639711" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="330.99762062129156" cy="350.47433325041106" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="325.8034047054532" cy="305.99904672748409" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="280.49757924584151" cy="333.65249497686978" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="287.00277059310656" cy="319.69598053266509" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="315.64930904704397" cy="292.15112588755892" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="284.0" y="250.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="329.0" y="257.0"></text></g><line style="" x1="255.1337393706334" x2="374.0" y1="384.0" y2="384.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="250.0" y="384.0">-2</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="308.38947866940873" y="384.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="366.7789573388175" y="384.0">2</text></g><line style="" x1="240.0" x2="240.0" y1="250.0" y2="374.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 240.0, 367.9337312440569)" x="240.0" y="367.9337312440569">-2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 240.0, 314.4136824121976)" x="240.0" y="314.4136824121976">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 240.0, 260.89363358033836)" x="240.0" y="260.89363358033836">2</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tcdb884241af5480dac668a034db762bc text");
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
          var text = document.querySelectorAll("#tcdb884241af5480dac668a034db762bc text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.14285714285714285, 0.20203050891044214, 0.24743582965269675, 0.2857142857142857, 0.3194382824999699, 0.3499271061118826, 0.3779644730092272, 0.40406101782088427, 0.42857142857142855, 0.4517539514526256, 0.4738035414793428, 0.4948716593053935, 0.5150787536377127, 0.5345224838248488, 0.5532833351724881, 0.5714285714285714, 0.5890150893739515, 0.6060915267313264, 0.6226998490772391, 0.6388765649999398, 0.6546536707079771, 0.6700593942604899, 0.6851187890446742, 0.6998542122237652, 0.7142857142857143, 0.7284313590846835, 0.7423074889580902, 0.7559289460184544, 0.769309258162072, 0.7824607964359516, 0.7953949089757174, 0.8081220356417685, 0.8206518066482897, 0.8329931278350429, 0.8451542547285166, 0.8571428571428571, 0.8689660757568884, 0.8806305718527109, 0.8921425711997711, 0.9035079029052512, 0.9147320339189784, 0.9258200997725514, 0.9367769320431429, 0.9476070829586856, 0.9583148474999098, 0.9689042833036097, 0.9793792286287205, 0.989743318610787, 1.0]], "names": ["x", "y0"], "id": "t3a852160c96a42d3b8d899153b603eac", "title": "Plot Data"}, {"data": [[-0.008713446887994244, -0.8185400877903809, 2.809175677953333, -1.4319590130966988, -0.07270425349686993, 0.9310800424527621, 0.382138167450283, 0.5420556457802783, -0.6558856568195198, -0.16209139240814002, 0.9293315381028232, -0.9557959810014035, -0.16454802731699045, -0.6149502166011138, -0.5631965440362959, -0.38335566111206654, -0.2632938047788682, 1.158377727179662, 0.40542324643171235, -0.17758244051300826, -1.150610841448699, -0.030922064063831467, -0.048703130502893766, -2.2801941596490467, -1.1618714224638285, 1.9310543036767047, 0.4445647949471246, 1.2853811390797507, 1.4881624150800614, -1.3888278076246694, 0.28738356928040476, -0.1144078674575959, -0.10451802591661667, -0.3778650777646228, 1.1299332012706438, -1.423190014828945, -0.38534115160431825, -0.8941149722362375, 0.5888511765866133, 0.7049351487187915, -1.4598147971885782, -2.14415870322437, 1.0399013863070328, 0.21696778098394923, -1.6472577210345207, 0.21645755972201125, -1.3001874382423106, -0.9723289626156731, -0.8449456890465142, 0.003507404038350149, 0.2208221130453279, -0.9765843197291489, -1.9500516640952397, -1.0664622994285478, 0.5328989074380323, 0.4857326222809642, -0.8284637398508996, 1.2149093505567976, -1.8227054602898192, -1.2192210850587628, -1.4671844859116674, 0.6305369159453532, -0.24245369381508872, 2.128440566798231, 2.5444560432557273, -0.057452712792126694, -0.8917200345794641, -0.16575177917535927, 0.6277741960379228, -0.242967371532958, 0.3242419665230987, 0.907599828035328, -0.6567923336620858, -0.3886115255750003, -0.17740221823739244, 0.04261587241996412, -1.8607014404030833, -0.46784009939639964, -0.2996820355100971, -0.16922061611810807, 0.31356137353735747, -0.93135327600798, 0.5977598386911727, -0.8822514642733872, 0.10626297130109771, -0.5462100039833937, -0.13372028815882903, -0.37811760130968025, 0.3334742826159079, -0.07550659121915741, -1.1230245564559806, -1.5823843662368449, -0.19243819315664565, 0.332129144343385, -1.4668346670550505, 0.967988688505261, 0.7455934884535905, -1.194217693802612, -0.915691857662839, 0.31083641021780434], [-0.743624604995376, 0.3549618096881732, 0.6571653217470798, 0.6797094109150094, 0.3690969156126819, 0.6673452017201007, -0.7302221410547585, -1.0888575101761147, -1.2299645870118507, 0.12444917253057411, -0.9475033609111608, -0.06606056922697794, 1.1624120705483907, -0.9918358306456835, 1.6876093209015066, -0.03381651424042111, 1.7201271968027383, -0.6572552070051184, -0.87324764327552, 0.47087764851219166, 0.23376008327679598, 0.0313508502028213, -0.21095712579086884, 0.22338245106577553, 0.34366109317777827, -1.1473184743016476, -1.004701713765091, 0.8618303528939205, 0.06646113130197596, -0.47021391811127355, -1.429320975637432, 0.23708494798734334, -0.08262795932292455, -1.2305470858851877, 0.7851830860671788, -0.34425894026934584, 0.27204401475112977, -1.285810633882835, -0.4442110557407369, -0.028309864080464743, -1.7075247860636196, 0.3503957657582001, 0.8108492135559296, -0.49307817771317086, -0.29596717497576797, 0.031123414601939653, -2.0982798939823, -0.31643973640319656, 2.4070860852374114, 0.6604684403286433, 0.6755425485676101, -0.34963866253558373, -0.9344486688322114, -0.09193824745249789, -0.25546746887666266, -0.9227113440911595, 1.3237759241390135, -0.8956761158304822, 0.546529376008508, -0.7692568101877225, 0.16652017208406134, 0.7928340899077188, 1.5943376404644778, -0.5560553762922854, -0.925087357013632, -1.4976466612080948, 1.942577655254276, -0.5460918558829604, 0.5716975004687571, 0.08970756765346673, 0.12700127529928687, -0.452421713908302, 0.4616173242945317, -1.0167477823019109, 0.7675760097001779, 1.4420293671843638, -2.2266914507122793, 0.7727401874646255, 1.4815880047200962, -0.32600499580046594, -0.2269426112273831, -0.13136993625832774, -0.8820614309497258, 0.038952832033901964, -0.4581801372643786, -0.5198852120013522, -0.8445701430837641, -0.13052196835757532, -0.6401943627109256, -1.4860146446806806, -0.7068431488642812, -1.1492797215375068, -0.8449548631991661, 1.1215342419219796, 0.8155443996085873, -1.3475567240793445, 0.3144479823308568, -0.7189385280687451, -0.1973951158775124, 0.8319333412635567]], "names": ["x", "y0"], "id": "t960b4b83aaa6442799f3800662149732", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tcdb884241af5480dac668a034db762bc .toyplot-mark-popup");
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
      var axes = {"t2303d2c886b242aba2b77257886c8a2d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 420.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 420.0}, "scale": "linear"}]}, "t27f12f1382c24d43b5624e5699c4f649": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.8091756779533328, "min": -2.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 374.0, "min": 250.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.4070860852374114, "min": -2.2266914507122793}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 374.0}, "scale": "linear"}]}};
    
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


Here are all the positions supported by the *corner* argument:

.. code:: python

    canvas = toyplot.Canvas(width="10cm")
    for position in ["top-left", "top", "top-right", "right", "bottom-right", "bottom", "bottom-left", "left"]:
        canvas.axes(corner=(position, "1cm", "2cm", "2cm"), label=position)



.. raw:: html

    <div align="center" class="toyplot" id="tf7cb15b842a3468aaf6a709c2aa2e118"><svg height="377.95275599999997px" id="td1730e0e13524d24bcade7bb2b5f367a" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="377.95275599999997px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t8712f860d91b4db4916ca3c4dad5417f"><clipPath id="te900141a42b4417095198ec30167b4b0"><rect height="75.59055120000002" width="75.59055120000002" x="37.795275600000004" y="37.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te900141a42b4417095198ec30167b4b0)" style="cursor:crosshair"><rect height="75.59055120000002" style="pointer-events:all;visibility:hidden" width="75.59055120000002" x="37.795275600000004" y="37.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="54.795275600000004"></text></g><line style="" x1="37.795275600000004" x2="113.38582680000002" y1="113.38582680000002" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="47.795275600000004" y="113.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="75.59055120000001" y="113.38582680000002">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="103.38582680000002" y="113.38582680000002">0.5</text></g><line style="" x1="37.795275600000004" x2="37.795275600000004" y1="37.795275600000004" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 103.38582680000002)" x="37.795275600000004" y="103.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 75.59055120000001)" x="37.795275600000004" y="75.59055120000001">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 47.795275600000004)" x="37.795275600000004" y="47.795275600000004">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="75.59055120000001" y="37.795275600000004">top-left</text></g><g class="toyplot-axes-Cartesian" id="t5708d8a7bfbe4f539f0979ed14bc3b20"><clipPath id="tfc454fcd911944bb8a47ce2b6c0e1a63"><rect height="75.59055120000002" width="75.5905512" x="151.1811024" y="37.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tfc454fcd911944bb8a47ce2b6c0e1a63)" style="cursor:crosshair"><rect height="75.59055120000002" style="pointer-events:all;visibility:hidden" width="75.5905512" x="151.1811024" y="37.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="126.77165359999998" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="171.77165359999998" y="54.795275600000004"></text></g><line style="" x1="151.1811024" x2="226.77165359999998" y1="113.38582680000002" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="161.1811024" y="113.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="188.97637799999998" y="113.38582680000002">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="216.77165359999998" y="113.38582680000002">0.5</text></g><line style="" x1="151.1811024" x2="151.1811024" y1="37.795275600000004" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 103.38582680000002)" x="151.1811024" y="103.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 75.59055120000001)" x="151.1811024" y="75.59055120000001">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 47.795275600000004)" x="151.1811024" y="47.795275600000004">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="188.97637799999998" y="37.795275600000004">top</text></g><g class="toyplot-axes-Cartesian" id="taba553e342f4424a9b05684c5d571c36"><clipPath id="td56b7354502a47b8a3b9b37cdac616e5"><rect height="75.59055120000002" width="75.5905512" x="264.56692919999995" y="37.795275600000004"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td56b7354502a47b8a3b9b37cdac616e5)" style="cursor:crosshair"><rect height="75.59055120000002" style="pointer-events:all;visibility:hidden" width="75.5905512" x="264.56692919999995" y="37.795275600000004"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="240.15748039999994" y="47.795275600000004"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="285.15748039999994" y="54.795275600000004"></text></g><line style="" x1="264.56692919999995" x2="340.15748039999994" y1="113.38582680000002" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="274.56692919999995" y="113.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="302.3622048" y="113.38582680000002">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.15748039999994" y="113.38582680000002">0.5</text></g><line style="" x1="264.56692919999995" x2="264.56692919999995" y1="37.795275600000004" y2="113.38582680000002"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 103.38582680000002)" x="264.56692919999995" y="103.38582680000002">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 75.59055120000001)" x="264.56692919999995" y="75.59055120000001">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 47.795275600000004)" x="264.56692919999995" y="47.795275600000004">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="302.3622048" y="37.795275600000004">top-right</text></g><g class="toyplot-axes-Cartesian" id="tecf2b41b70db4058b61e975954e54164"><clipPath id="t77226567ff17459086c5e99acde2a53a"><rect height="75.5905512" width="75.5905512" x="264.56692919999995" y="151.1811024"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t77226567ff17459086c5e99acde2a53a)" style="cursor:crosshair"><rect height="75.5905512" style="pointer-events:all;visibility:hidden" width="75.5905512" x="264.56692919999995" y="151.1811024"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="240.15748039999994" y="161.1811024"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="285.15748039999994" y="168.1811024"></text></g><line style="" x1="264.56692919999995" x2="340.15748039999994" y1="226.77165359999998" y2="226.77165359999998"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="274.56692919999995" y="226.77165359999998">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="302.3622048" y="226.77165359999998">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.15748039999994" y="226.77165359999998">0.5</text></g><line style="" x1="264.56692919999995" x2="264.56692919999995" y1="151.1811024" y2="226.77165359999998"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 216.77165359999998)" x="264.56692919999995" y="216.77165359999998">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 188.97637799999998)" x="264.56692919999995" y="188.97637799999998">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 161.1811024)" x="264.56692919999995" y="161.1811024">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="302.3622048" y="151.1811024">right</text></g><g class="toyplot-axes-Cartesian" id="t82622626dd5c49eb95befea0a1ff629f"><clipPath id="t521dead3c947409da07425ab6d7fe0ef"><rect height="75.5905512" width="75.5905512" x="264.56692919999995" y="264.56692919999995"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t521dead3c947409da07425ab6d7fe0ef)" style="cursor:crosshair"><rect height="75.5905512" style="pointer-events:all;visibility:hidden" width="75.5905512" x="264.56692919999995" y="264.56692919999995"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="240.15748039999994" y="274.56692919999995"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="285.15748039999994" y="281.56692919999995"></text></g><line style="" x1="264.56692919999995" x2="340.15748039999994" y1="340.15748039999994" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="274.56692919999995" y="340.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="302.3622048" y="340.15748039999994">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.15748039999994" y="340.15748039999994">0.5</text></g><line style="" x1="264.56692919999995" x2="264.56692919999995" y1="264.56692919999995" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 330.15748039999994)" x="264.56692919999995" y="330.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 302.3622048)" x="264.56692919999995" y="302.3622048">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 264.56692919999995, 274.56692919999995)" x="264.56692919999995" y="274.56692919999995">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="302.3622048" y="264.56692919999995">bottom-right</text></g><g class="toyplot-axes-Cartesian" id="t99674707542b42db8d49a47d92e1718b"><clipPath id="tc41ea0f4cf9048c7b3780d3de7580220"><rect height="75.5905512" width="75.5905512" x="151.1811024" y="264.56692919999995"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tc41ea0f4cf9048c7b3780d3de7580220)" style="cursor:crosshair"><rect height="75.5905512" style="pointer-events:all;visibility:hidden" width="75.5905512" x="151.1811024" y="264.56692919999995"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="126.77165359999998" y="274.56692919999995"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="171.77165359999998" y="281.56692919999995"></text></g><line style="" x1="151.1811024" x2="226.77165359999998" y1="340.15748039999994" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="161.1811024" y="340.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="188.97637799999998" y="340.15748039999994">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="216.77165359999998" y="340.15748039999994">0.5</text></g><line style="" x1="151.1811024" x2="151.1811024" y1="264.56692919999995" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 330.15748039999994)" x="151.1811024" y="330.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 302.3622048)" x="151.1811024" y="302.3622048">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 151.1811024, 274.56692919999995)" x="151.1811024" y="274.56692919999995">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="188.97637799999998" y="264.56692919999995">bottom</text></g><g class="toyplot-axes-Cartesian" id="tcaf9d85df9434a04a0d8e05222d98635"><clipPath id="td1bb7520b19748cf81c747a953d85a65"><rect height="75.5905512" width="75.59055120000002" x="37.795275600000004" y="264.56692919999995"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td1bb7520b19748cf81c747a953d85a65)" style="cursor:crosshair"><rect height="75.5905512" style="pointer-events:all;visibility:hidden" width="75.59055120000002" x="37.795275600000004" y="264.56692919999995"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="274.56692919999995"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="281.56692919999995"></text></g><line style="" x1="37.795275600000004" x2="113.38582680000002" y1="340.15748039999994" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="47.795275600000004" y="340.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="75.59055120000001" y="340.15748039999994">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="103.38582680000002" y="340.15748039999994">0.5</text></g><line style="" x1="37.795275600000004" x2="37.795275600000004" y1="264.56692919999995" y2="340.15748039999994"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 330.15748039999994)" x="37.795275600000004" y="330.15748039999994">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 302.3622048)" x="37.795275600000004" y="302.3622048">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 274.56692919999995)" x="37.795275600000004" y="274.56692919999995">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="75.59055120000001" y="264.56692919999995">bottom-left</text></g><g class="toyplot-axes-Cartesian" id="tb5dea852b32941efa00b293a51a91190"><clipPath id="td3cfc54115ad40759549a7024b35c01c"><rect height="75.5905512" width="75.59055120000002" x="37.795275600000004" y="151.1811024"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td3cfc54115ad40759549a7024b35c01c)" style="cursor:crosshair"><rect height="75.5905512" style="pointer-events:all;visibility:hidden" width="75.59055120000002" x="37.795275600000004" y="151.1811024"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="13.385826800000018" y="161.1811024"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="58.38582680000002" y="168.1811024"></text></g><line style="" x1="37.795275600000004" x2="113.38582680000002" y1="226.77165359999998" y2="226.77165359999998"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="47.795275600000004" y="226.77165359999998">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="75.59055120000001" y="226.77165359999998">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="103.38582680000002" y="226.77165359999998">0.5</text></g><line style="" x1="37.795275600000004" x2="37.795275600000004" y1="151.1811024" y2="226.77165359999998"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 216.77165359999998)" x="37.795275600000004" y="216.77165359999998">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 188.97637799999998)" x="37.795275600000004" y="188.97637799999998">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 37.795275600000004, 161.1811024)" x="37.795275600000004" y="161.1811024">0.5</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="75.59055120000001" y="151.1811024">left</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tf7cb15b842a3468aaf6a709c2aa2e118 text");
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
          var text = document.querySelectorAll("#tf7cb15b842a3468aaf6a709c2aa2e118 text");
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
      var axes = {"t5708d8a7bfbe4f539f0979ed14bc3b20": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 216.77165359999998, "min": 161.1811024}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 47.795275600000004, "min": 103.38582680000002}, "scale": "linear"}]}, "t82622626dd5c49eb95befea0a1ff629f": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 330.15748039999994, "min": 274.56692919999995}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 274.56692919999995, "min": 330.15748039999994}, "scale": "linear"}]}, "t8712f860d91b4db4916ca3c4dad5417f": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 103.38582680000002, "min": 47.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 47.795275600000004, "min": 103.38582680000002}, "scale": "linear"}]}, "t99674707542b42db8d49a47d92e1718b": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 216.77165359999998, "min": 161.1811024}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 274.56692919999995, "min": 330.15748039999994}, "scale": "linear"}]}, "taba553e342f4424a9b05684c5d571c36": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 330.15748039999994, "min": 274.56692919999995}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 47.795275600000004, "min": 103.38582680000002}, "scale": "linear"}]}, "tb5dea852b32941efa00b293a51a91190": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 103.38582680000002, "min": 47.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 161.1811024, "min": 216.77165359999998}, "scale": "linear"}]}, "tcaf9d85df9434a04a0d8e05222d98635": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 103.38582680000002, "min": 47.795275600000004}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 274.56692919999995, "min": 330.15748039999994}, "scale": "linear"}]}, "tecf2b41b70db4058b61e975954e54164": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 330.15748039999994, "min": 274.56692919999995}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 161.1811024, "min": 216.77165359999998}, "scale": "linear"}]}};
    
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


Properties
----------

Axes objects contain sets of nested properties that can be used to
adjust behavior. The list of available properties includes the
following:

-  axes.show - set to *False* to hide the axes completely (the plotted
   data will still be visible).
-  axes.padding - a small gap between the axes and their contents.
   Defaults to CSS pixels, supports all :ref:`units`.
-  axes.label.text - optional label at the top of the axes.
-  axes.label.style - styles the axes label text.
-  axes.coordinates.show - set to *False* to disable interactive mouse
   coordinates.
-  axes.coordinates.style - styles the interactive mouse coordinates
   background.
-  axes.coordinates.label.style - styles the interactive mouse
   coordinates text.
-  axes.x.show - set to *False* to hide the X axis completely.
-  axes.x.scale - "linear", "log" (base 10), "log10", "log2", or a
   ("log", base) tuple.
-  axes.x.domain.min - override the minimum domain value for the axis.
-  axes.x.domain.max - override the maximum domain value for the axis.
-  axes.x.label.text - optional label below the X axis.
-  axes.x.label.style - styles the X axis label.
-  axes.x.spine.show - set to *False* to hide the X axis spine.
-  axes.x.spine.position - set to "low", "high", or a Y axis domain
   value to position the spine. Defaults to "low".
-  axes.x.spine.style - styles the X axis spine.
-  axes.x.ticks.show - set to *True* to display X axis tick marks.
-  axes.x.ticks.locator - assign an instance of
   :py:class:`toyplot.locator.Basic`,
   :py:class:`toyplot.locator.Explicit`,
   :py:class:`toyplot.locator.Extended`,
   :py:class:`toyplot.locator.Heckbert`, or
   :py:class:`toyplot.locator.Log` to control the positioning and
   formatting of ticks and tick labels. By default, an appropriate
   locator is automatically chosen based on the axis scale and domain.
-  axes.x.ticks.length - length of X axis ticks. Defaults to CSS pixels,
   supports all :ref:`units`.
-  axes.x.ticks.style - styles the X axis ticks.
-  axes.x.ticks.labels.show - set to *False* to hide X axis tick labels.
-  axes.x.ticks.labels.angle - set the angle of X axis tick labels in
   degrees.
-  axes.x.ticks.labels.offset - offsets labels from the axis. Defaults
   to CSS pixels, supports all :ref:`units`.
-  axes.x.ticks.labels.style - style X axis tick label text.
-  ... and equivalent properties for the Y axis.

In the following example we override several of the defaults:

.. code:: python

    x = numpy.linspace(0, 2 * numpy.pi)
    y = numpy.sin(x)

.. code:: python

    import toyplot.locator
    
    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes()
    axes.label.text = "Trigonometry 101"
    axes.x.label.text = "x"
    axes.y.label.text = "sin(x)"
    axes.x.ticks.show = True
    axes.x.ticks.locator = toyplot.locator.Explicit(
        [0, numpy.pi / 2, numpy.pi, 3 * numpy.pi / 2, 2 * numpy.pi],
        ["0", u"\u03c0 / 2", u"\u03c0", u"3 \u03c0 / 2", u"2 \u03c0"])
    mark = axes.plot(x, y)



.. raw:: html

    <div align="center" class="toyplot" id="tefd5d9983525482699e0b9cfc37dff89"><svg height="300.0px" id="t803631e38a324bf3a8773b8dc3c9f5fd" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc87d289dd8134836a0578f48dc5f2811"><clipPath id="t520e68fd69c14aa6b911f107b29cad63"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t520e68fd69c14aa6b911f107b29cad63)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t18f541cefe6c453b9a0d6db009bec6f7" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 150.0 L 69.795918367346943 138.49105544839446 L 79.591836734693871 127.17108744814433 L 89.387755102040813 116.22596956085634 L 99.183673469387742 105.83542031964561 L 108.97959183673468 96.170052255790551 L 118.77551020408163 87.388570445686213 L 128.57142857142856 79.635166577877328 L 138.36734693877551 73.037151329518849 L 148.16326530612244 67.702863928576889 L 157.95918367346937 63.719893226700549 L 167.75510204081633 61.153639492699497 L 177.55102040816325 60.04624054193809 L 187.34693877551018 60.415879834572159 L 197.14285714285714 62.256487903635886 L 206.9387755102041 65.537842015521576 L 216.73469387755102 70.20606242642998 L 226.53061224489795 76.18449708627395 L 236.32653061224488 83.374980263221573 L 246.12244897959181 91.659444422299003 L 255.91836734693874 100.90185889105058 L 265.71428571428572 110.95046347941975 L 275.51020408163265 121.64026037787411 L 285.30612244897958 132.79572341687648 L 295.10204081632651 144.23368020173581 L 304.89795918367349 155.76631979826411 L 314.69387755102036 167.20427658312349 L 324.48979591836735 178.3597396221258 L 334.28571428571428 189.04953652058023 L 344.08163265306121 199.09814110894936 L 353.87755102040819 208.34055557770094 L 363.67346938775506 216.6250197367784 L 373.46938775510199 223.81550291372602 L 383.26530612244892 229.79393757357002 L 393.0612244897959 234.46215798447844 L 402.85714285714289 237.74351209636413 L 412.65306122448976 239.58412016542783 L 422.44897959183675 239.95375945806191 L 432.24489795918362 238.84636050730055 L 442.0408163265306 236.28010677329945 L 451.83673469387747 232.29713607142313 L 461.63265306122446 226.96284867048118 L 471.42857142857139 220.3648334221227 L 481.22448979591832 212.61142955431384 L 491.0204081632653 203.82994774420948 L 500.81632653061223 194.16457968035448 L 510.61224489795916 183.7740304391437 L 520.40816326530603 172.82891255185575 L 530.20408163265301 161.50894455160562 L 540.0 150.00000000000003" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="540.0" y1="250.0" y2="250.0"></line><g><line style="" x1="60.0" x2="60.0" y1="250.0" y2="245.0"></line><line style="" x1="180.0" x2="180.0" y1="250.0" y2="245.0"></line><line style="" x1="300.0" x2="300.0" y1="250.0" y2="245.0"></line><line style="" x1="420.0" x2="420.0" y1="250.0" y2="245.0"></line><line style="" x1="540.0" x2="540.0" y1="250.0" y2="245.0"></line></g><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="180.0" y="250.0">&#960; / 2</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="300.0" y="250.0">&#960;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="420.0" y="250.0">3 &#960; / 2</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">2 &#960;</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="300.0" y="250.0">x</text><line style="" x1="50.0" x2="50.0" y1="60.04624054193809" y2="239.9537594580619"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">-1.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">sin(x)</text><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="300.0" y="50.0">Trigonometry 101</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tefd5d9983525482699e0b9cfc37dff89 text");
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
          var text = document.querySelectorAll("#tefd5d9983525482699e0b9cfc37dff89 text");
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
      var data_tables = [{"data": [[0.0, 0.1282282715750936, 0.2564565431501872, 0.38468481472528077, 0.5129130863003744, 0.6411413578754679, 0.7693696294505615, 0.8975979010256552, 1.0258261726007487, 1.1540544441758422, 1.2822827157509358, 1.4105109873260295, 1.538739258901123, 1.6669675304762166, 1.7951958020513104, 1.9234240736264039, 2.0516523452014974, 2.179880616776591, 2.3081088883516845, 2.436337159926778, 2.5645654315018716, 2.6927937030769655, 2.821021974652059, 2.9492502462271526, 3.077478517802246, 3.2057067893773397, 3.333935060952433, 3.4621633325275267, 3.5903916041026207, 3.7186198756777142, 3.8468481472528078, 3.9750764188279013, 4.103304690402995, 4.231532961978089, 4.359761233553182, 4.487989505128276, 4.616217776703369, 4.744446048278463, 4.872674319853556, 5.00090259142865, 5.129130863003743, 5.257359134578837, 5.385587406153931, 5.513815677729024, 5.642043949304118, 5.770272220879211, 5.898500492454305, 6.026728764029398, 6.154957035604492, 6.283185307179586], [0.0, 0.127877161684506, 0.25365458390950735, 0.3752670048793741, 0.49071755200393785, 0.5981105304912159, 0.6956825506034864, 0.7818314824680297, 0.8551427630053461, 0.9144126230158124, 0.9586678530366606, 0.9871817834144501, 0.9994862162006879, 0.9953791129491982, 0.9749279121818236, 0.9384684220497604, 0.8865993063730001, 0.8201722545969561, 0.7402779970753157, 0.6482283953077888, 0.545534901210549, 0.43388373911755823, 0.3151082180236208, 0.19115862870137254, 0.06407021998071323, -0.06407021998071254, -0.19115862870137187, -0.3151082180236202, -0.433883739117558, -0.5455349012105485, -0.6482283953077882, -0.7402779970753153, -0.8201722545969556, -0.8865993063730001, -0.9384684220497602, -0.9749279121818235, -0.9953791129491981, -0.9994862162006879, -0.9871817834144503, -0.9586678530366608, -0.9144126230158128, -0.8551427630053465, -0.7818314824680299, -0.6956825506034869, -0.5981105304912162, -0.49071755200393863, -0.3752670048793746, -0.25365458390950835, -0.12787716168450664, -2.4492935982947064e-16]], "names": ["x", "y0"], "id": "t18f541cefe6c453b9a0d6db009bec6f7", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tefd5d9983525482699e0b9cfc37dff89 .toyplot-mark-popup");
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
      var axes = {"tc87d289dd8134836a0578f48dc5f2811": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 6.2831853071795862, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -1.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


As a convenience, some of the most common properties can also be set
when the axes are created:

.. code:: python

    x = numpy.linspace(0, 10, 100)
    y = 40 + x ** 2

.. code:: python

    canvas = toyplot.Canvas(300, 300)
    axes = canvas.axes(label="Toyplot Users", xlabel="Days", ylabel="Users")
    mark = axes.plot(x, y)



.. raw:: html

    <div align="center" class="toyplot" id="t6bad958cffc449f59b2ceaf94c4c48cc"><svg height="300.0px" id="t989f2e2846784198ba6d812c3df8a5e6" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="taab44af2152e49568571828904e7afb3"><clipPath id="t1d99916962e6450c80a05e72ac3765b2"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t1d99916962e6450c80a05e72ac3765b2)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tdad6a8debeb44f83b7d56fce2cafb6dd" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 61.81818181818182 239.9833041155355 L 63.63636363636364 239.9332164621421 L 65.454545454545467 239.84973703981967 L 67.272727272727266 239.73286584856831 L 69.090909090909093 239.58260288838801 L 70.909090909090907 239.39894815927875 L 72.72727272727272 239.18190166124052 L 74.545454545454547 238.93146339427329 L 76.363636363636374 238.64763335837719 L 78.181818181818187 238.33041155355207 L 80.0 237.97979797979795 L 81.818181818181813 237.59579263711495 L 83.63636363636364 237.17839552550299 L 85.454545454545453 236.72760664496198 L 87.27272727272728 236.24342599549212 L 89.090909090909093 235.72585357709323 L 90.909090909090907 235.17488938976544 L 92.72727272727272 234.59053343350863 L 94.545454545454533 233.9727857083229 L 96.363636363636374 233.32164621420819 L 98.181818181818187 232.63711495116456 L 100.0 231.91919191919192 L 101.81818181818181 231.16787711829033 L 103.63636363636364 230.38317054845979 L 105.45454545454544 229.5650722097003 L 107.27272727272728 228.71358210201186 L 109.09090909090909 227.82870022539444 L 110.90909090909091 226.91042657984806 L 112.72727272727272 225.95876116537275 L 114.54545454545456 224.97370398196847 L 116.36363636363635 223.95525502963517 L 118.18181818181817 222.90341430837302 L 120.00000000000001 221.81818181818181 L 121.81818181818181 220.6995575590617 L 123.63636363636363 219.5475415310126 L 125.45454545454547 218.36213373403456 L 127.27272727272728 217.14333416812752 L 129.09090909090907 215.89114283329161 L 130.90909090909091 214.60555972952668 L 132.72727272727275 213.28658485683277 L 134.54545454545453 211.93421821520997 L 136.36363636363637 210.54845980465814 L 138.18181818181819 209.12930962517743 L 140.0 207.67676767676764 L 141.81818181818181 206.190833959429 L 143.63636363636363 204.67150847316137 L 145.45454545454547 203.11879121796477 L 147.27272727272728 201.53268219383921 L 149.09090909090909 199.91318140078468 L 150.90909090909088 198.26028883880127 L 152.72727272727272 196.57400450788884 L 154.54545454545456 194.85432840804739 L 156.36363636363637 193.10126053927706 L 158.18181818181819 191.31480090157777 L 160.0 189.49494949494948 L 161.81818181818181 187.64170631939228 L 163.63636363636363 185.75507137490609 L 165.45454545454544 183.83504466149094 L 167.27272727272728 181.88162617914685 L 169.09090909090909 179.89481592787379 L 170.90909090909091 177.87461390767174 L 172.72727272727272 175.82102011854079 L 174.54545454545453 173.73403456048084 L 176.36363636363635 171.61365723349195 L 178.18181818181816 169.4598881375741 L 180.00000000000003 167.27272727272725 L 181.81818181818181 165.0521746389515 L 183.63636363636363 162.79823023624675 L 185.45454545454547 160.51089406461304 L 187.27272727272725 158.19016612405042 L 189.09090909090909 155.83604641455881 L 190.90909090909093 153.44853493613826 L 192.72727272727272 151.02763168878874 L 194.54545454545456 148.57333667251024 L 196.36363636363637 146.08564988730279 L 198.18181818181816 143.56457133316638 L 200.0 141.01010101010104 L 201.81818181818181 138.4222389181067 L 203.63636363636363 135.80098505718342 L 205.45454545454547 133.14633942733116 L 207.27272727272725 130.45830202854995 L 209.09090909090907 127.73687286083984 L 210.90909090909091 124.98205192420068 L 212.72727272727272 122.19383921863263 L 214.54545454545456 119.37223474413555 L 216.36363636363637 116.5172385007096 L 218.18181818181816 113.62885048835464 L 220.0 110.7070707070707 L 221.81818181818181 107.75189915685786 L 223.63636363636363 104.76333583771606 L 225.45454545454547 101.7413807496452 L 227.27272727272728 98.686033892645469 L 229.09090909090909 95.597295266716742 L 230.90909090909091 92.475164871859064 L 232.72727272727272 89.319642708072465 L 234.54545454545456 86.130728775356843 L 236.36363636363637 82.908423073712342 L 238.18181818181819 79.652725603138776 L 240.0 76.363636363636374" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="240.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">10</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="250.0">Days</text><line style="" x1="50.0" x2="50.0" y1="76.36363636363637" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 223.63636363636365)" x="50.0" y="223.63636363636365">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 141.8181818181818)" x="50.0" y="141.8181818181818">100</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">150</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">Users</text><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="50.0">Toyplot Users</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t6bad958cffc449f59b2ceaf94c4c48cc text");
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
          var text = document.querySelectorAll("#t6bad958cffc449f59b2ceaf94c4c48cc text");
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
      var data_tables = [{"data": [[0.0, 0.10101010101010101, 0.20202020202020202, 0.30303030303030304, 0.40404040404040403, 0.5050505050505051, 0.6060606060606061, 0.7070707070707071, 0.8080808080808081, 0.9090909090909091, 1.0101010101010102, 1.1111111111111112, 1.2121212121212122, 1.3131313131313131, 1.4141414141414141, 1.5151515151515151, 1.6161616161616161, 1.7171717171717171, 1.8181818181818181, 1.9191919191919191, 2.0202020202020203, 2.121212121212121, 2.2222222222222223, 2.323232323232323, 2.4242424242424243, 2.525252525252525, 2.6262626262626263, 2.727272727272727, 2.8282828282828283, 2.929292929292929, 3.0303030303030303, 3.131313131313131, 3.2323232323232323, 3.3333333333333335, 3.4343434343434343, 3.5353535353535355, 3.6363636363636362, 3.7373737373737375, 3.8383838383838382, 3.9393939393939394, 4.040404040404041, 4.141414141414141, 4.242424242424242, 4.343434343434343, 4.444444444444445, 4.545454545454545, 4.646464646464646, 4.747474747474747, 4.848484848484849, 4.94949494949495, 5.05050505050505, 5.151515151515151, 5.252525252525253, 5.353535353535354, 5.454545454545454, 5.555555555555555, 5.656565656565657, 5.757575757575758, 5.858585858585858, 5.959595959595959, 6.0606060606060606, 6.161616161616162, 6.262626262626262, 6.363636363636363, 6.4646464646464645, 6.565656565656566, 6.666666666666667, 6.767676767676767, 6.8686868686868685, 6.96969696969697, 7.070707070707071, 7.171717171717171, 7.2727272727272725, 7.373737373737374, 7.474747474747475, 7.575757575757575, 7.6767676767676765, 7.777777777777778, 7.878787878787879, 7.979797979797979, 8.080808080808081, 8.181818181818182, 8.282828282828282, 8.383838383838384, 8.484848484848484, 8.585858585858587, 8.686868686868687, 8.787878787878787, 8.88888888888889, 8.98989898989899, 9.09090909090909, 9.191919191919192, 9.292929292929292, 9.393939393939394, 9.494949494949495, 9.595959595959595, 9.696969696969697, 9.797979797979798, 9.8989898989899, 10.0], [40.0, 40.01020304050607, 40.04081216202428, 40.09182736455464, 40.16324864809713, 40.25507601265177, 40.36730945821855, 40.49994898479747, 40.65299459238853, 40.82644628099173, 41.02030405060708, 41.23456790123457, 41.4692378328742, 41.72431384552597, 41.99979593918988, 42.29568411386593, 42.61197836955413, 42.94867870625446, 43.30578512396694, 43.68329762269156, 44.08121620242832, 44.499540863177224, 44.93827160493827, 45.397408427711454, 45.876951331496784, 46.376900316294254, 46.897255382103864, 47.438016528925615, 47.999183756759514, 48.58075706560555, 49.182736455463726, 49.805121926334046, 50.447913478216506, 51.111111111111114, 51.794714825017856, 52.49872461993674, 53.22314049586777, 53.96796245281094, 54.73319049076625, 55.5188246097337, 56.3248648097133, 57.15131109070502, 57.99816345270891, 58.86542189572492, 59.75308641975309, 60.66115702479338, 61.58963371084583, 62.53851647791042, 63.50780532598715, 64.49750025507602, 65.50760126517702, 66.53810835629017, 67.58902152841547, 68.6603407815529, 69.75206611570248, 70.8641975308642, 71.99673502703806, 73.14967860422406, 74.3230282624222, 75.51678400163249, 76.7309458218549, 77.96551372308949, 79.22048770533618, 80.49586776859505, 81.79165391286602, 83.10784613814917, 84.44444444444446, 85.80144883175186, 87.17885930007142, 88.57667584940313, 89.99489847974696, 91.43352719110294, 92.89256198347107, 94.37200285685134, 95.87184981124375, 97.3921028466483, 98.93276196306499, 100.49382716049382, 102.0752984389348, 103.6771757983879, 105.29945923885319, 106.94214876033058, 108.6052443628201, 110.2887460463218, 111.99265381083562, 113.7169676563616, 115.4616875828997, 117.22681359044994, 119.01234567901236, 120.81828384858687, 122.64462809917353, 124.49137843077237, 126.35853484338332, 128.24609733700643, 130.15406591164168, 132.08244056728904, 134.0312213039486, 136.00040812162024, 137.99000102030408, 140.0]], "names": ["x", "y0"], "id": "tdad6a8debeb44f83b7d56fce2cafb6dd", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t6bad958cffc449f59b2ceaf94c4c48cc .toyplot-mark-popup");
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
      var axes = {"taab44af2152e49568571828904e7afb3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 10.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 40.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


And the same properties can be used with the :ref:`convenience` API,
as in the following example where we specify a minimum value for an axis
- for example, if we wanted the previous figure to include
:math:`y = 0`:

.. code:: python

    toyplot.plot(x, y, label="Toyplot Users", xlabel="Days", ylabel="Users", ymin=0, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="tdb019dcbe12a4588a41c53ae187be9dd"><svg height="300.0px" id="tdfbb0baa31e349fbb154607b95d677a2" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t2511971194da42149c5c684126d97307"><clipPath id="t014a57aed29c4f75a60d30c13e6f0cf7"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t014a57aed29c4f75a60d30c13e6f0cf7)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tc1bf63680e204bd2b35a2a03e5d13967" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 192.0 L 61.81818181818182 191.98775635139273 L 63.63636363636364 191.95102540557085 L 65.454545454545467 191.88980716253442 L 67.272727272727266 191.80410162228341 L 69.090909090909093 191.69390878481786 L 70.909090909090907 191.55922865013775 L 72.72727272727272 191.40006121824302 L 74.545454545454547 191.21640648913376 L 76.363636363636374 191.00826446280993 L 78.181818181818187 190.77563513927151 L 80.0 190.5185185185185 L 81.818181818181813 190.23691460055096 L 83.63636363636364 189.93082338536885 L 85.454545454545453 189.60024487297213 L 87.27272727272728 189.24517906336089 L 89.090909090909093 188.86562595653504 L 90.909090909090907 188.46158555249465 L 92.72727272727272 188.03305785123968 L 94.545454545454533 187.58004285277013 L 96.363636363636374 187.102540557086 L 98.181818181818187 186.60055096418733 L 100.0 186.07407407407408 L 101.81818181818181 185.52310988674625 L 103.63636363636364 184.94765840220384 L 105.45454545454544 184.3477196204469 L 107.27272727272728 183.72329354147536 L 109.09090909090909 183.07438016528926 L 110.90909090909091 182.40097949188859 L 112.72727272727272 181.70309152127334 L 114.54545454545456 180.98071625344349 L 116.36363636363635 180.23385368839917 L 118.18181818181817 179.46250382614019 L 120.00000000000001 178.66666666666666 L 121.81818181818181 177.84634220997856 L 123.63636363636363 177.00153045607593 L 125.45454545454547 176.1322314049587 L 127.27272727272728 175.23844505662686 L 129.09090909090907 174.32017141108048 L 130.90909090909091 173.37741046831954 L 132.72727272727275 172.41016222834406 L 134.54545454545453 171.418426691154 L 136.36363636363637 170.40220385674931 L 138.18181818181819 169.36149372513012 L 140.0 168.2962962962963 L 141.81818181818181 167.20661157024793 L 143.63636363636363 166.09243954698499 L 145.45454545454547 164.95378022650749 L 147.27272727272728 163.79063360881543 L 149.09090909090909 162.6029996939088 L 150.90909090909088 161.39087848178758 L 152.72727272727272 160.1542699724518 L 154.54545454545456 158.89317416590143 L 156.36363636363637 157.60759106213649 L 158.18181818181819 156.29752066115705 L 160.0 154.96296296296293 L 161.81818181818181 153.60391796755434 L 163.63636363636363 152.22038567493112 L 165.45454545454544 150.81236608509337 L 167.27272727272728 149.37985919804103 L 169.09090909090909 147.92286501377413 L 170.90909090909091 146.4413835322926 L 172.72727272727272 144.93541475359658 L 174.54545454545453 143.40495867768595 L 176.36363636363635 141.85001530456077 L 178.18181818181816 140.270584634221 L 180.00000000000003 138.66666666666666 L 181.81818181818181 137.03826140189778 L 183.63636363636363 135.38536883991429 L 185.45454545454547 133.70798898071624 L 187.27272727272725 132.00612182430365 L 189.09090909090909 130.2797673706765 L 190.90909090909093 128.52892561983472 L 192.72727272727272 126.7535965717784 L 194.54545454545456 124.95378022650749 L 196.36363636363637 123.12947658402204 L 198.18181818181816 121.28068564432202 L 200.0 119.4074074074074 L 201.81818181818181 117.50964187327824 L 203.63636363636363 115.58738904193451 L 205.45454545454547 113.64064891337618 L 207.27272727272725 111.6694214876033 L 209.09090909090907 109.67370676461587 L 210.90909090909091 107.65350474441385 L 212.72727272727272 105.60881542699724 L 214.54545454545456 103.53963881236606 L 216.36363636363637 101.44597490052035 L 218.18181818181816 99.327823691460083 L 220.0 97.185185185185162 L 221.81818181818181 95.018059381695764 L 223.63636363636363 92.82644628099176 L 225.45454545454547 90.610345883073165 L 227.27272727272728 88.369758187940008 L 229.09090909090909 86.104683195592287 L 230.90909090909091 83.815120906029989 L 232.72727272727272 81.501071319253157 L 234.54545454545456 79.162534435261676 L 236.36363636363637 76.799510254055718 L 238.18181818181819 74.411998775635112 L 240.0 72.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="240.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">10</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="250.0">Days</text><line style="" x1="50.0" x2="50.0" y1="72.0" y2="192.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 180.00000000000003)" x="50.0" y="180.00000000000003">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 120.00000000000001)" x="50.0" y="120.00000000000001">100</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">150</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">Users</text><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="50.0">Toyplot Users</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tdb019dcbe12a4588a41c53ae187be9dd text");
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
          var text = document.querySelectorAll("#tdb019dcbe12a4588a41c53ae187be9dd text");
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
      var data_tables = [{"data": [[0.0, 0.10101010101010101, 0.20202020202020202, 0.30303030303030304, 0.40404040404040403, 0.5050505050505051, 0.6060606060606061, 0.7070707070707071, 0.8080808080808081, 0.9090909090909091, 1.0101010101010102, 1.1111111111111112, 1.2121212121212122, 1.3131313131313131, 1.4141414141414141, 1.5151515151515151, 1.6161616161616161, 1.7171717171717171, 1.8181818181818181, 1.9191919191919191, 2.0202020202020203, 2.121212121212121, 2.2222222222222223, 2.323232323232323, 2.4242424242424243, 2.525252525252525, 2.6262626262626263, 2.727272727272727, 2.8282828282828283, 2.929292929292929, 3.0303030303030303, 3.131313131313131, 3.2323232323232323, 3.3333333333333335, 3.4343434343434343, 3.5353535353535355, 3.6363636363636362, 3.7373737373737375, 3.8383838383838382, 3.9393939393939394, 4.040404040404041, 4.141414141414141, 4.242424242424242, 4.343434343434343, 4.444444444444445, 4.545454545454545, 4.646464646464646, 4.747474747474747, 4.848484848484849, 4.94949494949495, 5.05050505050505, 5.151515151515151, 5.252525252525253, 5.353535353535354, 5.454545454545454, 5.555555555555555, 5.656565656565657, 5.757575757575758, 5.858585858585858, 5.959595959595959, 6.0606060606060606, 6.161616161616162, 6.262626262626262, 6.363636363636363, 6.4646464646464645, 6.565656565656566, 6.666666666666667, 6.767676767676767, 6.8686868686868685, 6.96969696969697, 7.070707070707071, 7.171717171717171, 7.2727272727272725, 7.373737373737374, 7.474747474747475, 7.575757575757575, 7.6767676767676765, 7.777777777777778, 7.878787878787879, 7.979797979797979, 8.080808080808081, 8.181818181818182, 8.282828282828282, 8.383838383838384, 8.484848484848484, 8.585858585858587, 8.686868686868687, 8.787878787878787, 8.88888888888889, 8.98989898989899, 9.09090909090909, 9.191919191919192, 9.292929292929292, 9.393939393939394, 9.494949494949495, 9.595959595959595, 9.696969696969697, 9.797979797979798, 9.8989898989899, 10.0], [40.0, 40.01020304050607, 40.04081216202428, 40.09182736455464, 40.16324864809713, 40.25507601265177, 40.36730945821855, 40.49994898479747, 40.65299459238853, 40.82644628099173, 41.02030405060708, 41.23456790123457, 41.4692378328742, 41.72431384552597, 41.99979593918988, 42.29568411386593, 42.61197836955413, 42.94867870625446, 43.30578512396694, 43.68329762269156, 44.08121620242832, 44.499540863177224, 44.93827160493827, 45.397408427711454, 45.876951331496784, 46.376900316294254, 46.897255382103864, 47.438016528925615, 47.999183756759514, 48.58075706560555, 49.182736455463726, 49.805121926334046, 50.447913478216506, 51.111111111111114, 51.794714825017856, 52.49872461993674, 53.22314049586777, 53.96796245281094, 54.73319049076625, 55.5188246097337, 56.3248648097133, 57.15131109070502, 57.99816345270891, 58.86542189572492, 59.75308641975309, 60.66115702479338, 61.58963371084583, 62.53851647791042, 63.50780532598715, 64.49750025507602, 65.50760126517702, 66.53810835629017, 67.58902152841547, 68.6603407815529, 69.75206611570248, 70.8641975308642, 71.99673502703806, 73.14967860422406, 74.3230282624222, 75.51678400163249, 76.7309458218549, 77.96551372308949, 79.22048770533618, 80.49586776859505, 81.79165391286602, 83.10784613814917, 84.44444444444446, 85.80144883175186, 87.17885930007142, 88.57667584940313, 89.99489847974696, 91.43352719110294, 92.89256198347107, 94.37200285685134, 95.87184981124375, 97.3921028466483, 98.93276196306499, 100.49382716049382, 102.0752984389348, 103.6771757983879, 105.29945923885319, 106.94214876033058, 108.6052443628201, 110.2887460463218, 111.99265381083562, 113.7169676563616, 115.4616875828997, 117.22681359044994, 119.01234567901236, 120.81828384858687, 122.64462809917353, 124.49137843077237, 126.35853484338332, 128.24609733700643, 130.15406591164168, 132.08244056728904, 134.0312213039486, 136.00040812162024, 137.99000102030408, 140.0]], "names": ["x", "y0"], "id": "tc1bf63680e204bd2b35a2a03e5d13967", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tdb019dcbe12a4588a41c53ae187be9dd .toyplot-mark-popup");
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
      var axes = {"t2511971194da42149c5c684126d97307": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 10.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Scale
-----

An important property of each axis is its scale, used to specify linear
or logarithmic mappings from *domain* to *range*:

.. code:: python

    x = numpy.linspace(-1000, 1000)

.. code:: python

    canvas = toyplot.Canvas(700, 700)
    
    axes = canvas.axes(grid=(2, 2, 0, 0), xscale="linear", yscale="linear")
    axes.plot(x, x, marker="o")
    
    axes = canvas.axes(grid=(2, 2, 0, 1), xscale="log", yscale="linear")
    axes.plot(x, x, marker="o")
    
    axes = canvas.axes(grid=(2, 2, 1, 0), xscale="linear", yscale="log")
    axes.plot(x, x, marker="o")
    
    axes = canvas.axes(grid=(2, 2, 1, 1), xscale="log", yscale="log")
    axes.plot(x, x, marker="o");



.. raw:: html

    <div align="center" class="toyplot" id="t11e4e3c183a64e47b9cce059d74dadfb"><svg height="700.0px" id="t888608684f40494b8a7a7fae69740b9b" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t5f67581296ec4ad0a88a0a6f07d442b3"><clipPath id="ta208de709dc74d43889b880e475365ed"><rect height="250.0" width="250.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta208de709dc74d43889b880e475365ed)" style="cursor:crosshair"><rect height="250.0" style="pointer-events:all;visibility:hidden" width="250.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tf997d7746dbe4dbdafb73157257167cf" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 290.0 L 64.693877551020421 285.30612244897958 L 69.387755102040813 280.61224489795921 L 74.081632653061234 275.91836734693879 L 78.775510204081627 271.22448979591837 L 83.469387755102034 266.53061224489795 L 88.163265306122454 261.83673469387753 L 92.857142857142861 257.14285714285711 L 97.551020408163268 252.44897959183675 L 102.24489795918367 247.75510204081633 L 106.93877551020407 243.0612244897959 L 111.63265306122449 238.36734693877551 L 116.32653061224488 233.67346938775509 L 121.0204081632653 228.9795918367347 L 125.71428571428571 224.28571428571428 L 130.40816326530611 219.59183673469391 L 135.10204081632654 214.89795918367349 L 139.79591836734693 210.20408163265307 L 144.48979591836735 205.51020408163265 L 149.18367346938777 200.81632653061226 L 153.87755102040813 196.12244897959184 L 158.57142857142856 191.42857142857142 L 163.26530612244898 186.73469387755102 L 167.9591836734694 182.0408163265306 L 172.65306122448979 177.34693877551021 L 177.34693877551021 172.65306122448979 L 182.0408163265306 167.9591836734694 L 186.73469387755102 163.26530612244898 L 191.42857142857142 158.57142857142858 L 196.12244897959184 153.87755102040816 L 200.8163265306122 149.18367346938777 L 205.51020408163265 144.48979591836735 L 210.20408163265307 139.79591836734696 L 214.89795918367346 135.10204081632654 L 219.59183673469389 130.40816326530614 L 224.28571428571425 125.71428571428575 L 228.9795918367347 121.02040816326532 L 233.67346938775509 116.32653061224491 L 238.36734693877551 111.63265306122449 L 243.0612244897959 106.93877551020408 L 247.7551020408163 102.2448979591837 L 252.44897959183675 97.551020408163282 L 257.14285714285711 92.857142857142861 L 261.83673469387753 88.163265306122454 L 266.53061224489795 83.469387755102048 L 271.22448979591837 78.775510204081627 L 275.91836734693879 74.081632653061234 L 280.61224489795916 69.387755102040828 L 285.30612244897958 64.693877551020421 L 290.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="290.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="64.693877551020421" cy="285.30612244897958" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="69.387755102040813" cy="280.61224489795921" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="74.081632653061234" cy="275.91836734693879" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.775510204081627" cy="271.22448979591837" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="83.469387755102034" cy="266.53061224489795" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="88.163265306122454" cy="261.83673469387753" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="92.857142857142861" cy="257.14285714285711" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="97.551020408163268" cy="252.44897959183675" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="102.24489795918367" cy="247.75510204081633" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="106.93877551020407" cy="243.0612244897959" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="111.63265306122449" cy="238.36734693877551" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="116.32653061224488" cy="233.67346938775509" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="121.0204081632653" cy="228.9795918367347" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="125.71428571428571" cy="224.28571428571428" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="130.40816326530611" cy="219.59183673469391" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="135.10204081632654" cy="214.89795918367349" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="139.79591836734693" cy="210.20408163265307" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="144.48979591836735" cy="205.51020408163265" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="149.18367346938777" cy="200.81632653061226" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="153.87755102040813" cy="196.12244897959184" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="158.57142857142856" cy="191.42857142857142" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="163.26530612244898" cy="186.73469387755102" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="167.9591836734694" cy="182.0408163265306" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="172.65306122448979" cy="177.34693877551021" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="177.34693877551021" cy="172.65306122448979" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="182.0408163265306" cy="167.9591836734694" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.73469387755102" cy="163.26530612244898" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="191.42857142857142" cy="158.57142857142858" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="196.12244897959184" cy="153.87755102040816" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="200.8163265306122" cy="149.18367346938777" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="205.51020408163265" cy="144.48979591836735" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="210.20408163265307" cy="139.79591836734696" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="214.89795918367346" cy="135.10204081632654" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="219.59183673469389" cy="130.40816326530614" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="224.28571428571425" cy="125.71428571428575" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="228.9795918367347" cy="121.02040816326532" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="233.67346938775509" cy="116.32653061224491" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="238.36734693877551" cy="111.63265306122449" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="243.0612244897959" cy="106.93877551020408" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="247.7551020408163" cy="102.2448979591837" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="252.44897959183675" cy="97.551020408163282" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="257.14285714285711" cy="92.857142857142861" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="261.83673469387753" cy="88.163265306122454" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="266.53061224489795" cy="83.469387755102048" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="271.22448979591837" cy="78.775510204081627" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="275.91836734693879" cy="74.081632653061234" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="280.61224489795916" cy="69.387755102040828" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="285.30612244897958" cy="64.693877551020421" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="290.0" cy="60.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="200.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="245.0" y="67.0"></text></g><line style="" x1="60.0" x2="290.0" y1="300.0" y2="300.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="300.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="117.5" y="300.0">-500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="175.0" y="300.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="232.5" y="300.0">500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="290.0" y="300.0">1000</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="290.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 290.0)" x="50.0" y="290.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 232.5)" x="50.0" y="232.5">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 175.0)" x="50.0" y="175.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 117.5)" x="50.0" y="117.5">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1000</text></g></g><g class="toyplot-axes-Cartesian" id="td151720478204a97aaff3278a434cf44"><clipPath id="tc68c829fdeef4b72832abd848aa41abb"><rect height="250.0" width="250.0" x="400.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tc68c829fdeef4b72832abd848aa41abb)" style="cursor:crosshair"><rect height="250.0" style="pointer-events:all;visibility:hidden" width="250.0" x="400.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t0662e31805964256bc9ed2ea0886ba4a" style="fill:none"><g class="toyplot-Series"><path d="M 410.0 290.0 L 410.5550121441791 285.30612244897958 L 411.1341626984306 280.61224489795921 L 411.73964714976711 275.91836734693879 L 412.3739748481359 271.22448979591837 L 413.04003183872845 266.53061224489795 L 413.7411602494866 261.83673469387753 L 414.48125976079928 257.14285714285711 L 415.2649189646192 252.44897959183675 L 416.09758784329006 247.75510204081633 L 416.98580785197305 243.0612244897959 L 417.93752435333215 238.36734693877551 L 418.96251952159855 233.67346938775509 L 420.07302614966829 228.9795918367347 L 421.28462141570083 224.28571428571428 L 422.61756935832096 219.59183673469391 L 424.09891286527397 214.89795918367349 L 425.76588117650022 210.20408163265307 L 427.67175031679807 205.51020408163265 L 429.89663744268887 200.81632653061226 L 432.56924283140177 196.12244897959184 L 435.9163398937705 191.42857142857142 L 440.39759965456983 186.73469387755102 L 447.20096130947144 182.0408163265306 L 461.83267978754105 177.34693877551021 L 588.16732021245889 172.65306122448979 L 602.7990386905285 167.9591836734694 L 609.60240034543017 163.26530612244898 L 614.08366010622944 158.57142857142858 L 617.43075716859823 153.87755102040816 L 620.10336255731113 149.18367346938777 L 622.32824968320188 144.48979591836735 L 624.23411882349978 139.79591836734696 L 625.90108713472591 135.10204081632654 L 627.38243064167909 130.40816326530614 L 628.71537858429906 125.71428571428575 L 629.92697385033171 121.02040816326532 L 631.03748047840145 116.32653061224491 L 632.06247564666785 111.63265306122449 L 633.01419214802695 106.93877551020408 L 633.90241215670994 102.2448979591837 L 634.73508103538074 97.551020408163282 L 635.51874023920072 92.857142857142861 L 636.2588397505134 88.163265306122454 L 636.9599681612716 83.469387755102048 L 637.62602515186416 78.775510204081627 L 638.26035285023283 74.081632653061234 L 638.8658373015694 69.387755102040828 L 639.44498785582084 64.693877551020421 L 640.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="410.0" cy="290.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="410.5550121441791" cy="285.30612244897958" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="411.1341626984306" cy="280.61224489795921" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="411.73964714976711" cy="275.91836734693879" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="412.3739748481359" cy="271.22448979591837" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="413.04003183872845" cy="266.53061224489795" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="413.7411602494866" cy="261.83673469387753" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="414.48125976079928" cy="257.14285714285711" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="415.2649189646192" cy="252.44897959183675" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="416.09758784329006" cy="247.75510204081633" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="416.98580785197305" cy="243.0612244897959" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="417.93752435333215" cy="238.36734693877551" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="418.96251952159855" cy="233.67346938775509" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="420.07302614966829" cy="228.9795918367347" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="421.28462141570083" cy="224.28571428571428" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="422.61756935832096" cy="219.59183673469391" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="424.09891286527397" cy="214.89795918367349" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="425.76588117650022" cy="210.20408163265307" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="427.67175031679807" cy="205.51020408163265" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="429.89663744268887" cy="200.81632653061226" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="432.56924283140177" cy="196.12244897959184" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="435.9163398937705" cy="191.42857142857142" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="440.39759965456983" cy="186.73469387755102" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="447.20096130947144" cy="182.0408163265306" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="461.83267978754105" cy="177.34693877551021" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="588.16732021245889" cy="172.65306122448979" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="602.7990386905285" cy="167.9591836734694" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="609.60240034543017" cy="163.26530612244898" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="614.08366010622944" cy="158.57142857142858" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="617.43075716859823" cy="153.87755102040816" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="620.10336255731113" cy="149.18367346938777" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="622.32824968320188" cy="144.48979591836735" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="624.23411882349978" cy="139.79591836734696" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="625.90108713472591" cy="135.10204081632654" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="627.38243064167909" cy="130.40816326530614" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="628.71537858429906" cy="125.71428571428575" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="629.92697385033171" cy="121.02040816326532" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="631.03748047840145" cy="116.32653061224491" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="632.06247564666785" cy="111.63265306122449" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="633.01419214802695" cy="106.93877551020408" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="633.90241215670994" cy="102.2448979591837" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="634.73508103538074" cy="97.551020408163282" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="635.51874023920072" cy="92.857142857142861" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="636.2588397505134" cy="88.163265306122454" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="636.9599681612716" cy="83.469387755102048" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="637.62602515186416" cy="78.775510204081627" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="638.26035285023283" cy="74.081632653061234" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="638.8658373015694" cy="69.387755102040828" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="639.44498785582084" cy="64.693877551020421" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="640.0" cy="60.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g><line style="" x1="410.0" x2="640.0" y1="300.0" y2="300.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="410.0" y="300.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="440.6666666666667" y="300.0">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="471.3333333333333" y="300.0">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="502.0" y="300.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="525.0" y="300.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="548.0" y="300.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="578.6666666666667" y="300.0">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="609.3333333333333" y="300.0">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="640.0" y="300.0">10&#8202;&#179;</text></g><line style="" x1="400.0" x2="400.0" y1="60.0" y2="290.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 290.0)" x="400.0" y="290.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 232.5)" x="400.0" y="232.5">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 175.0)" x="400.0" y="175.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 117.5)" x="400.0" y="117.5">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 60.0)" x="400.0" y="60.0">1000</text></g></g><g class="toyplot-axes-Cartesian" id="t51968c50a272493d81b3b2680f178fc1"><clipPath id="tab420f328ae24e5bae42067d9ca2becb"><rect height="250.0" width="250.0" x="50.0" y="400.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tab420f328ae24e5bae42067d9ca2becb)" style="cursor:crosshair"><rect height="250.0" style="pointer-events:all;visibility:hidden" width="250.0" x="50.0" y="400.0"></rect><g class="toyplot-mark-Plot" id="tca678927286d4f6595166490a6bdde5a" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 640.0 L 64.693877551020421 639.44498785582084 L 69.387755102040813 638.8658373015694 L 74.081632653061234 638.26035285023283 L 78.775510204081627 637.62602515186416 L 83.469387755102034 636.9599681612716 L 88.163265306122454 636.2588397505134 L 92.857142857142861 635.51874023920072 L 97.551020408163268 634.73508103538074 L 102.24489795918367 633.90241215670994 L 106.93877551020407 633.01419214802695 L 111.63265306122449 632.06247564666785 L 116.32653061224488 631.03748047840145 L 121.0204081632653 629.92697385033171 L 125.71428571428571 628.71537858429906 L 130.40816326530611 627.38243064167909 L 135.10204081632654 625.90108713472591 L 139.79591836734693 624.23411882349978 L 144.48979591836735 622.32824968320188 L 149.18367346938777 620.10336255731113 L 153.87755102040813 617.43075716859823 L 158.57142857142856 614.08366010622944 L 163.26530612244898 609.60240034543006 L 167.9591836734694 602.79903869052862 L 172.65306122448979 588.16732021245889 L 177.34693877551021 461.832679787541 L 182.0408163265306 447.20096130947144 L 186.73469387755102 440.39759965456983 L 191.42857142857142 435.91633989377056 L 196.12244897959184 432.56924283140177 L 200.8163265306122 429.89663744268887 L 205.51020408163265 427.67175031679812 L 210.20408163265307 425.76588117650022 L 214.89795918367346 424.09891286527397 L 219.59183673469389 422.61756935832102 L 224.28571428571425 421.28462141570088 L 228.9795918367347 420.07302614966829 L 233.67346938775509 418.96251952159855 L 238.36734693877551 417.93752435333215 L 243.0612244897959 416.98580785197305 L 247.7551020408163 416.09758784329006 L 252.44897959183675 415.2649189646192 L 257.14285714285711 414.48125976079928 L 261.83673469387753 413.7411602494866 L 266.53061224489795 413.04003183872845 L 271.22448979591837 412.3739748481359 L 275.91836734693879 411.73964714976711 L 280.61224489795916 411.1341626984306 L 285.30612244897958 410.55501214417905 L 290.0 410.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="640.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="64.693877551020421" cy="639.44498785582084" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="69.387755102040813" cy="638.8658373015694" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="74.081632653061234" cy="638.26035285023283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.775510204081627" cy="637.62602515186416" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="83.469387755102034" cy="636.9599681612716" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="88.163265306122454" cy="636.2588397505134" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="92.857142857142861" cy="635.51874023920072" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="97.551020408163268" cy="634.73508103538074" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="102.24489795918367" cy="633.90241215670994" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="106.93877551020407" cy="633.01419214802695" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="111.63265306122449" cy="632.06247564666785" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="116.32653061224488" cy="631.03748047840145" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="121.0204081632653" cy="629.92697385033171" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="125.71428571428571" cy="628.71537858429906" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="130.40816326530611" cy="627.38243064167909" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="135.10204081632654" cy="625.90108713472591" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="139.79591836734693" cy="624.23411882349978" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="144.48979591836735" cy="622.32824968320188" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="149.18367346938777" cy="620.10336255731113" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="153.87755102040813" cy="617.43075716859823" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="158.57142857142856" cy="614.08366010622944" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="163.26530612244898" cy="609.60240034543006" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="167.9591836734694" cy="602.79903869052862" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="172.65306122448979" cy="588.16732021245889" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="177.34693877551021" cy="461.832679787541" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="182.0408163265306" cy="447.20096130947144" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.73469387755102" cy="440.39759965456983" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="191.42857142857142" cy="435.91633989377056" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="196.12244897959184" cy="432.56924283140177" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="200.8163265306122" cy="429.89663744268887" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="205.51020408163265" cy="427.67175031679812" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="210.20408163265307" cy="425.76588117650022" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="214.89795918367346" cy="424.09891286527397" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="219.59183673469389" cy="422.61756935832102" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="224.28571428571425" cy="421.28462141570088" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="228.9795918367347" cy="420.07302614966829" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="233.67346938775509" cy="418.96251952159855" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="238.36734693877551" cy="417.93752435333215" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="243.0612244897959" cy="416.98580785197305" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="247.7551020408163" cy="416.09758784329006" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="252.44897959183675" cy="415.2649189646192" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="257.14285714285711" cy="414.48125976079928" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="261.83673469387753" cy="413.7411602494866" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="266.53061224489795" cy="413.04003183872845" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="271.22448979591837" cy="412.3739748481359" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="275.91836734693879" cy="411.73964714976711" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="280.61224489795916" cy="411.1341626984306" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="285.30612244897958" cy="410.55501214417905" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="290.0" cy="410.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="200.0" y="410.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="245.0" y="417.0"></text></g><line style="" x1="60.0" x2="290.0" y1="650.0" y2="650.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="650.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="117.5" y="650.0">-500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="175.0" y="650.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="232.5" y="650.0">500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="290.0" y="650.0">1000</text></g><line style="" x1="50.0" x2="50.0" y1="410.0" y2="640.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 640.0)" x="50.0" y="640.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 609.3333333333334)" x="50.0" y="609.3333333333334">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 578.6666666666667)" x="50.0" y="578.6666666666667">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 548.0)" x="50.0" y="548.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 525.0)" x="50.0" y="525.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 502.0)" x="50.0" y="502.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 471.33333333333337)" x="50.0" y="471.33333333333337">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 440.66666666666663)" x="50.0" y="440.66666666666663">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 410.0)" x="50.0" y="410.0">10&#8202;&#179;</text></g></g><g class="toyplot-axes-Cartesian" id="ta3e6dffc3d274159922b58a5bfa82bb9"><clipPath id="tddfba6c02fa24820b7072427164b6020"><rect height="250.0" width="250.0" x="400.0" y="400.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tddfba6c02fa24820b7072427164b6020)" style="cursor:crosshair"><rect height="250.0" style="pointer-events:all;visibility:hidden" width="250.0" x="400.0" y="400.0"></rect><g class="toyplot-mark-Plot" id="t785ff3dd0eda4f19b67c93d0bd483853" style="fill:none"><g class="toyplot-Series"><path d="M 410.0 640.0 L 410.5550121441791 639.44498785582084 L 411.1341626984306 638.8658373015694 L 411.73964714976711 638.26035285023283 L 412.3739748481359 637.62602515186416 L 413.04003183872845 636.9599681612716 L 413.7411602494866 636.2588397505134 L 414.48125976079928 635.51874023920072 L 415.2649189646192 634.73508103538074 L 416.09758784329006 633.90241215670994 L 416.98580785197305 633.01419214802695 L 417.93752435333215 632.06247564666785 L 418.96251952159855 631.03748047840145 L 420.07302614966829 629.92697385033171 L 421.28462141570083 628.71537858429906 L 422.61756935832096 627.38243064167909 L 424.09891286527397 625.90108713472591 L 425.76588117650022 624.23411882349978 L 427.67175031679807 622.32824968320188 L 429.89663744268887 620.10336255731113 L 432.56924283140177 617.43075716859823 L 435.9163398937705 614.08366010622944 L 440.39759965456983 609.60240034543006 L 447.20096130947144 602.79903869052862 L 461.83267978754105 588.16732021245889 L 588.16732021245889 461.832679787541 L 602.7990386905285 447.20096130947144 L 609.60240034543017 440.39759965456983 L 614.08366010622944 435.91633989377056 L 617.43075716859823 432.56924283140177 L 620.10336255731113 429.89663744268887 L 622.32824968320188 427.67175031679812 L 624.23411882349978 425.76588117650022 L 625.90108713472591 424.09891286527397 L 627.38243064167909 422.61756935832102 L 628.71537858429906 421.28462141570088 L 629.92697385033171 420.07302614966829 L 631.03748047840145 418.96251952159855 L 632.06247564666785 417.93752435333215 L 633.01419214802695 416.98580785197305 L 633.90241215670994 416.09758784329006 L 634.73508103538074 415.2649189646192 L 635.51874023920072 414.48125976079928 L 636.2588397505134 413.7411602494866 L 636.9599681612716 413.04003183872845 L 637.62602515186416 412.3739748481359 L 638.26035285023283 411.73964714976711 L 638.8658373015694 411.1341626984306 L 639.44498785582084 410.55501214417905 L 640.0 410.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="410.0" cy="640.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="410.5550121441791" cy="639.44498785582084" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="411.1341626984306" cy="638.8658373015694" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="411.73964714976711" cy="638.26035285023283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="412.3739748481359" cy="637.62602515186416" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="413.04003183872845" cy="636.9599681612716" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="413.7411602494866" cy="636.2588397505134" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="414.48125976079928" cy="635.51874023920072" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="415.2649189646192" cy="634.73508103538074" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="416.09758784329006" cy="633.90241215670994" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="416.98580785197305" cy="633.01419214802695" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="417.93752435333215" cy="632.06247564666785" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="418.96251952159855" cy="631.03748047840145" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="420.07302614966829" cy="629.92697385033171" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="421.28462141570083" cy="628.71537858429906" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="422.61756935832096" cy="627.38243064167909" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="424.09891286527397" cy="625.90108713472591" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="425.76588117650022" cy="624.23411882349978" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="427.67175031679807" cy="622.32824968320188" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="429.89663744268887" cy="620.10336255731113" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="432.56924283140177" cy="617.43075716859823" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="435.9163398937705" cy="614.08366010622944" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="440.39759965456983" cy="609.60240034543006" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="447.20096130947144" cy="602.79903869052862" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="461.83267978754105" cy="588.16732021245889" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="588.16732021245889" cy="461.832679787541" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="602.7990386905285" cy="447.20096130947144" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="609.60240034543017" cy="440.39759965456983" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="614.08366010622944" cy="435.91633989377056" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="617.43075716859823" cy="432.56924283140177" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="620.10336255731113" cy="429.89663744268887" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="622.32824968320188" cy="427.67175031679812" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="624.23411882349978" cy="425.76588117650022" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="625.90108713472591" cy="424.09891286527397" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="627.38243064167909" cy="422.61756935832102" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="628.71537858429906" cy="421.28462141570088" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="629.92697385033171" cy="420.07302614966829" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="631.03748047840145" cy="418.96251952159855" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="632.06247564666785" cy="417.93752435333215" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="633.01419214802695" cy="416.98580785197305" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="633.90241215670994" cy="416.09758784329006" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="634.73508103538074" cy="415.2649189646192" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="635.51874023920072" cy="414.48125976079928" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="636.2588397505134" cy="413.7411602494866" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="636.9599681612716" cy="413.04003183872845" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="637.62602515186416" cy="412.3739748481359" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="638.26035285023283" cy="411.73964714976711" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="638.8658373015694" cy="411.1341626984306" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="639.44498785582084" cy="410.55501214417905" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="640.0" cy="410.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="550.0" y="410.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="417.0"></text></g><line style="" x1="410.0" x2="640.0" y1="650.0" y2="650.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="410.0" y="650.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="440.6666666666667" y="650.0">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="471.3333333333333" y="650.0">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="502.0" y="650.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="525.0" y="650.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="548.0" y="650.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="578.6666666666667" y="650.0">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="609.3333333333333" y="650.0">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="640.0" y="650.0">10&#8202;&#179;</text></g><line style="" x1="400.0" x2="400.0" y1="410.0" y2="640.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 640.0)" x="400.0" y="640.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 609.3333333333334)" x="400.0" y="609.3333333333334">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 578.6666666666667)" x="400.0" y="578.6666666666667">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 548.0)" x="400.0" y="548.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 525.0)" x="400.0" y="525.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 502.0)" x="400.0" y="502.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 471.33333333333337)" x="400.0" y="471.33333333333337">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 440.66666666666663)" x="400.0" y="440.66666666666663">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 410.0)" x="400.0" y="410.0">10&#8202;&#179;</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t11e4e3c183a64e47b9cce059d74dadfb text");
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
          var text = document.querySelectorAll("#t11e4e3c183a64e47b9cce059d74dadfb text");
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
      var data_tables = [{"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "names": ["x", "y0"], "id": "tf997d7746dbe4dbdafb73157257167cf", "title": "Plot Data"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "names": ["x", "y0"], "id": "t0662e31805964256bc9ed2ea0886ba4a", "title": "Plot Data"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "names": ["x", "y0"], "id": "tca678927286d4f6595166490a6bdde5a", "title": "Plot Data"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "names": ["x", "y0"], "id": "t785ff3dd0eda4f19b67c93d0bd483853", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t11e4e3c183a64e47b9cce059d74dadfb .toyplot-mark-popup");
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
      var axes = {"t51968c50a272493d81b3b2680f178fc1": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 290.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 548.0, "min": -Infinity}, "max": 548.0, "min": 640.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 502.0, "min": 548.0}, "max": 502.0, "min": 548.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 502.0}, "max": 410.0, "min": 502.0}, "scale": ["log", 10]}]}, "t5f67581296ec4ad0a88a0a6f07d442b3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 290.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 290.0}, "scale": "linear"}]}, "ta3e6dffc3d274159922b58a5bfa82bb9": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 502.0, "min": -Infinity}, "max": 502.0, "min": 410.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 548.0, "min": 502.0}, "max": 548.0, "min": 502.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 548.0}, "max": 640.0, "min": 548.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 548.0, "min": -Infinity}, "max": 548.0, "min": 640.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 502.0, "min": 548.0}, "max": 502.0, "min": 548.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 502.0}, "max": 410.0, "min": 502.0}, "scale": ["log", 10]}]}, "td151720478204a97aaff3278a434cf44": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 502.0, "min": -Infinity}, "max": 502.0, "min": 410.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 548.0, "min": 502.0}, "max": 548.0, "min": 502.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 548.0}, "max": 640.0, "min": 548.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 290.0}, "scale": "linear"}]}};
    
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


Note that Toyplot handles negative values correctly, and provides
sensible results for values near zero by rendering them using a small
linear region around the origin.

The scale can be specified in two ways:

-  As a string - "linear", "log" (base 10), "log10" (base 10), or "log2"
   (base 2).
-  As a tuple - ("log", 2), ("log", 10), or ("log", :math:`N`) to use
   any base.

For example, the following are all equivalent

.. code:: python

    canvas = toyplot.Canvas(width=900, height=300)
    axes = canvas.axes(grid=(1,3,0), xscale="log")
    axes.plot(x, x)
    axes = canvas.axes(grid=(1,3,1), xscale="log10")
    axes.plot(x, x)
    axes = canvas.axes(grid=(1,3,2), xscale=("log", 10))
    axes.plot(x, x);



.. raw:: html

    <div align="center" class="toyplot" id="t3075b26b5c21433d96d1668057263f9d"><svg height="300.0px" id="t7e7d3a96bc194d9d8867ba5effdfc2ae" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="900.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t37858e7c342244419cabd3190ba7eec3"><clipPath id="td3281ec324b14372b00d36225eaa8564"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td3281ec324b14372b00d36225eaa8564)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="ta7d195284a444923bb4fd3f01bf7195a" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 60.434357330227115 236.32653061224491 L 60.887605590076078 232.65306122448982 L 61.361462986774256 228.9795918367347 L 61.857893359410667 225.30612244897958 L 62.379155352048343 221.63265306122449 L 62.927864543076453 217.9591836734694 L 63.507072856277716 214.28571428571428 L 64.120371363615035 210.61224489795919 L 64.772025268661778 206.9387755102041 L 65.467153971109383 203.26530612244898 L 66.211975580868639 199.59183673469389 L 67.014145712555418 195.91836734693877 L 67.883237856262099 192.24489795918367 L 68.831442847070264 188.57142857142858 L 69.874619497816425 184.89795918367349 L 71.033931807605754 181.2244897959184 L 72.33851570334798 177.55102040816325 L 73.830065465320246 173.87755102040816 L 75.571281476886924 170.20408163265307 L 77.662885694140527 166.53061224489795 L 80.282352960342166 162.85714285714286 L 83.789425816619882 159.18367346938777 L 89.11379580741243 155.51020408163265 L 100.56470592068432 151.83673469387756 L 199.43529407931567 148.16326530612244 L 210.88620419258757 144.48979591836735 L 216.21057418338012 140.81632653061226 L 219.71764703965783 137.14285714285714 L 222.33711430585947 133.46938775510205 L 224.42871852311305 129.79591836734696 L 226.16993453467975 126.12244897959185 L 227.66148429665202 122.44897959183675 L 228.96606819239426 118.77551020408163 L 230.12538050218356 115.10204081632654 L 231.16855715292974 111.42857142857144 L 232.1167621437379 107.75510204081634 L 232.98585428744457 104.08163265306123 L 233.78802441913137 100.40816326530613 L 234.53284602889062 96.734693877551024 L 235.22797473133821 93.061224489795933 L 235.87962863638498 89.387755102040828 L 236.49292714372228 85.714285714285722 L 237.07213545692355 82.040816326530617 L 237.62084464795166 78.367346938775512 L 238.14210664058933 74.693877551020393 L 238.63853701322574 71.020408163265316 L 239.11239440992392 67.34693877551021 L 239.5656426697729 63.673469387755105 L 240.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="240.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="84.0" y="250.0">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="108.0" y="250.0">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="132.0" y="250.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="168.0" y="250.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="192.0" y="250.0">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="216.0" y="250.0">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">10&#8202;&#179;</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1000</text></g></g><g class="toyplot-axes-Cartesian" id="t0ec446bacdcf49f48ff9df9cb0730f24"><clipPath id="t4116e3f9cfc74f8e8f5230a69e5a4ff4"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t4116e3f9cfc74f8e8f5230a69e5a4ff4)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t502b32f131a14aa881a91936d6fbcaef" style="fill:none"><g class="toyplot-Series"><path d="M 360.0 240.0 L 360.4343573302271 236.32653061224491 L 360.88760559007608 232.65306122448982 L 361.36146298677431 228.9795918367347 L 361.85789335941064 225.30612244897958 L 362.37915535204837 221.63265306122449 L 362.92786454307645 217.9591836734694 L 363.50707285627772 214.28571428571428 L 364.12037136361505 210.61224489795919 L 364.77202526866176 206.9387755102041 L 365.46715397110938 203.26530612244898 L 366.21197558086863 199.59183673469389 L 367.01414571255543 195.91836734693877 L 367.8832378562621 192.24489795918367 L 368.83144284707026 188.57142857142858 L 369.87461949781641 184.89795918367349 L 371.03393180760577 181.2244897959184 L 372.33851570334798 177.55102040816325 L 373.83006546532022 173.87755102040816 L 375.57128147688695 170.20408163265307 L 377.66288569414053 166.53061224489795 L 380.28235296034217 162.85714285714286 L 383.78942581661988 159.18367346938777 L 389.11379580741243 155.51020408163265 L 400.56470592068433 151.83673469387756 L 499.43529407931567 148.16326530612244 L 510.88620419258757 144.48979591836735 L 516.21057418338012 140.81632653061226 L 519.71764703965778 137.14285714285714 L 522.33711430585947 133.46938775510205 L 524.42871852311305 129.79591836734696 L 526.16993453467978 126.12244897959185 L 527.66148429665202 122.44897959183675 L 528.96606819239423 118.77551020408163 L 530.12538050218359 115.10204081632654 L 531.16855715292968 111.42857142857144 L 532.1167621437379 107.75510204081634 L 532.98585428744457 104.08163265306123 L 533.78802441913137 100.40816326530613 L 534.53284602889062 96.734693877551024 L 535.22797473133824 93.061224489795933 L 535.87962863638495 89.387755102040828 L 536.49292714372234 85.714285714285722 L 537.07213545692355 82.040816326530617 L 537.62084464795169 78.367346938775512 L 538.1421066405893 74.693877551020393 L 538.63853701322569 71.020408163265316 L 539.11239440992381 67.34693877551021 L 539.56564266977284 63.673469387755105 L 540.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="540.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="384.0" y="250.0">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="408.0" y="250.0">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="432.0" y="250.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="468.0" y="250.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="492.00000000000006" y="250.0">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="516.0" y="250.0">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">10&#8202;&#179;</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 195.0)" x="350.0" y="195.0">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 105.0)" x="350.0" y="105.0">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1000</text></g></g><g class="toyplot-axes-Cartesian" id="tcd2252257cbc4c82a7366407b02bd5fe"><clipPath id="tbbc483f4280d4c848d153077b839ddb6"><rect height="200.0" width="200.0" x="650.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tbbc483f4280d4c848d153077b839ddb6)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="650.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t8b6335abe47844848d07f6d530ff969c" style="fill:none"><g class="toyplot-Series"><path d="M 660.0 240.0 L 660.43435733022716 236.32653061224491 L 660.88760559007619 232.65306122448982 L 661.3614629867742 228.9795918367347 L 661.8578933594107 225.30612244897958 L 662.37915535204831 221.63265306122449 L 662.92786454307634 217.9591836734694 L 663.50707285627766 214.28571428571428 L 664.12037136361505 210.61224489795919 L 664.77202526866176 206.9387755102041 L 665.46715397110938 203.26530612244898 L 666.21197558086863 199.59183673469389 L 667.01414571255532 195.91836734693877 L 667.88323785626221 192.24489795918367 L 668.83144284707021 188.57142857142858 L 669.87461949781641 184.89795918367349 L 671.03393180760577 181.2244897959184 L 672.33851570334787 177.55102040816325 L 673.83006546532033 173.87755102040816 L 675.57128147688695 170.20408163265307 L 677.66288569414053 166.53061224489795 L 680.28235296034211 162.85714285714286 L 683.78942581661977 159.18367346938777 L 689.11379580741254 155.51020408163265 L 700.56470592068433 151.83673469387756 L 799.43529407931567 148.16326530612244 L 810.88620419258757 144.48979591836735 L 816.21057418338012 140.81632653061226 L 819.71764703965789 137.14285714285714 L 822.33711430585947 133.46938775510205 L 824.42871852311305 129.79591836734696 L 826.16993453467967 126.12244897959185 L 827.66148429665202 122.44897959183675 L 828.96606819239423 118.77551020408163 L 830.12538050218359 115.10204081632654 L 831.16855715292968 111.42857142857144 L 832.1167621437379 107.75510204081634 L 832.98585428744457 104.08163265306123 L 833.78802441913137 100.40816326530613 L 834.53284602889062 96.734693877551024 L 835.22797473133824 93.061224489795933 L 835.87962863638495 89.387755102040828 L 836.49292714372223 85.714285714285722 L 837.07213545692355 82.040816326530617 L 837.62084464795169 78.367346938775512 L 838.1421066405893 74.693877551020393 L 838.6385370132258 71.020408163265316 L 839.11239440992392 67.34693877551021 L 839.56564266977296 63.673469387755105 L 840.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="750.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="795.0" y="67.0"></text></g><line style="" x1="660.0" x2="840.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="660.0" y="250.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="684.0" y="250.0">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="708.0" y="250.0">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="732.0" y="250.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="750.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="768.0" y="250.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="792.0" y="250.0">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="816.0" y="250.0">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="840.0" y="250.0">10&#8202;&#179;</text></g><line style="" x1="650.0" x2="650.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 650.0, 240.0)" x="650.0" y="240.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 650.0, 195.0)" x="650.0" y="195.0">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 650.0, 150.0)" x="650.0" y="150.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 650.0, 105.0)" x="650.0" y="105.0">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 650.0, 60.0)" x="650.0" y="60.0">1000</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t3075b26b5c21433d96d1668057263f9d text");
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
          var text = document.querySelectorAll("#t3075b26b5c21433d96d1668057263f9d text");
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
      var data_tables = [{"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "names": ["x", "y0"], "id": "ta7d195284a444923bb4fd3f01bf7195a", "title": "Plot Data"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "names": ["x", "y0"], "id": "t502b32f131a14aa881a91936d6fbcaef", "title": "Plot Data"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "names": ["x", "y0"], "id": "t8b6335abe47844848d07f6d530ff969c", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t3075b26b5c21433d96d1668057263f9d .toyplot-mark-popup");
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
      var axes = {"t0ec446bacdcf49f48ff9df9cb0730f24": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 432.0, "min": -Infinity}, "max": 432.0, "min": 360.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 468.0, "min": 432.0}, "max": 468.0, "min": 432.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 468.0}, "max": 540.0, "min": 468.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "t37858e7c342244419cabd3190ba7eec3": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 132.0, "min": -Infinity}, "max": 132.0, "min": 60.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 168.0, "min": 132.0}, "max": 168.0, "min": 132.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 168.0}, "max": 240.0, "min": 168.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "tcd2252257cbc4c82a7366407b02bd5fe": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 732.0, "min": -Infinity}, "max": 732.0, "min": 660.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 768.0, "min": 732.0}, "max": 768.0, "min": 732.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 768.0}, "max": 840.0, "min": 768.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Of course, in addition to the builtin "log2" and "log10" scales, you are
free to specify any base you like, using the tuple notation:

.. code:: python

    toyplot.plot(x, x, xscale=("log", 4), width=400);



.. raw:: html

    <div align="center" class="toyplot" id="t7c3094354c2e4979b7f9178ba6a47aa7"><svg height="400.0px" id="t798360ac9e354d2e999751bd90f039ec" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tb59c22a0667d490aac57b1fd96e6309b"><clipPath id="t54bc85596ab44ac6a229856234fdc0d8"><rect height="300.0" width="300.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t54bc85596ab44ac6a229856234fdc0d8)" style="cursor:crosshair"><rect height="300.0" style="pointer-events:all;visibility:hidden" width="300.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t11f10101dc33490587558173d8f593c5" style="fill:none"><g class="toyplot-Series"><path d="M 60.383216011784626 340.0 L 61.056571127085434 334.28571428571428 L 61.759211586982602 328.57142857142861 L 62.493801013211467 322.85714285714289 L 63.263383814152412 317.14285714285717 L 64.071461414617758 311.42857142857139 L 64.922088570830738 305.71428571428567 L 65.819996476091333 299.99999999999994 L 66.770752129060284 294.28571428571428 L 67.780967589541945 288.57142857142856 L 68.858579120446151 282.85714285714283 L 70.013226241644119 277.14285714285717 L 71.256776940398026 271.42857142857144 L 72.604072358036419 265.71428571428572 L 74.074011130752837 260.0 L 75.691178115306798 254.28571428571433 L 77.488382443871146 248.57142857142861 L 79.510791595059544 242.85714285714289 L 81.823041422694729 237.14285714285714 L 84.522332137137226 231.42857142857142 L 87.764806249721047 225.71428571428572 L 91.825591138829793 220.0 L 97.262371603136501 214.28571428571428 L 105.51638625779799 208.57142857142858 L 123.26796626587495 202.85714285714286 L 276.73203373412503 197.14285714285714 L 294.48361374220195 191.42857142857144 L 302.7376283968635 185.71428571428572 L 308.17440886117021 180.0 L 312.23519375027894 174.28571428571428 L 315.47766786286275 168.57142857142861 L 318.1769585773053 162.85714285714289 L 320.48920840494043 157.14285714285717 L 322.51161755612884 151.42857142857144 L 324.3088218846932 145.71428571428572 L 325.92598886924713 140.00000000000003 L 327.39592764196362 134.28571428571431 L 328.74322305960197 128.57142857142858 L 329.98677375835587 122.85714285714286 L 331.14142087955389 117.14285714285714 L 332.219032410458 111.42857142857146 L 333.22924787093973 105.71428571428574 L 334.18000352390862 100.00000000000001 L 335.07791142916926 94.285714285714292 L 335.92853858538223 88.571428571428569 L 336.73661618584759 82.857142857142847 L 337.50619898678855 77.142857142857167 L 338.24078841301736 71.428571428571445 L 338.94342887291458 65.714285714285722 L 339.61678398821533 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="250.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="295.0" y="67.0"></text></g><line style="" x1="60.383216011784626" x2="339.61678398821533" y1="350.0" y2="350.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="350.0">-4&#8202;&#8309;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="82.4" y="350.0">-4&#8202;&#8308;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="104.8" y="350.0">-4&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="127.2" y="350.0">-4&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="149.6" y="350.0">-4&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="172.0" y="350.0">-4&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="200.0" y="350.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="228.0" y="350.0">4&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="250.4" y="350.0">4&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="272.79999999999995" y="350.0">4&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="295.2" y="350.0">4&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="317.59999999999997" y="350.0">4&#8202;&#8308;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="340.0" y="350.0">4&#8202;&#8309;</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="340.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 340.0)" x="50.0" y="340.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 270.0)" x="50.0" y="270.0">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 200.0)" x="50.0" y="200.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 130.0)" x="50.0" y="130.0">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1000</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t7c3094354c2e4979b7f9178ba6a47aa7 text");
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
          var text = document.querySelectorAll("#t7c3094354c2e4979b7f9178ba6a47aa7 text");
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
      var data_tables = [{"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "names": ["x", "y0"], "id": "t11f10101dc33490587558173d8f593c5", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t7c3094354c2e4979b7f9178ba6a47aa7 .toyplot-mark-popup");
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
      var axes = {"tb59c22a0667d490aac57b1fd96e6309b": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1024.0}, "range": {"bounds": {"max": 172.0, "min": -Infinity}, "max": 172.0, "min": 60.0}, "scale": ["log", 4]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 228.0, "min": 172.0}, "max": 228.0, "min": 172.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1024.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 228.0}, "max": 340.0, "min": 228.0}, "scale": ["log", 4]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 340.0}, "scale": "linear"}]}};
    
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


