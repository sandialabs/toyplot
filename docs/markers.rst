
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _markers:

Markers
=======

In Toyplot, markers are used to show the individual datums in
scatterplots:

.. code:: python

    import numpy
    import toyplot

.. code:: python

    y = numpy.linspace(0, 1, 20) ** 2
    toyplot.scatterplot(y, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t9a48006e1a944043bfaa41938a9b640b"><svg height="300.0px" id="t3374a8b718574f91adcddea5884fe0bc" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="te51269b3e07f4d409f152a39bd220534"><clipPath id="t48607af58e9c4473b4b7b51b36677358"><rect height="200.0" width="200.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t48607af58e9c4473b4b7b51b36677358)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t2b57715f73414b509be009ff05a60cfb" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="240.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="69.0" cy="239.50138504155126" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.0" cy="238.00554016620501" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="87.0" cy="235.51246537396122" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="96.0" cy="232.02216066481992" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="105.0" cy="227.53462603878117" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="114.0" cy="222.04986149584488" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="123.0" cy="215.56786703601105" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="132.0" cy="208.0886426592798" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="141.0" cy="199.61218836565098" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="150.0" cy="190.13850415512465" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="159.0" cy="179.66759002770081" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="168.0" cy="168.19944598337952" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="177.0" cy="155.73407202216069" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.0" cy="142.27146814404435" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="195.0" cy="127.81163434903047" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="204.0" cy="112.35457063711914" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="213.0" cy="95.900277008310283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="222.0" cy="78.448753462603904" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="231.0" cy="60.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t9a48006e1a944043bfaa41938a9b640b text");
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
          var text = document.querySelectorAll("#t9a48006e1a944043bfaa41938a9b640b text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t2b57715f73414b509be009ff05a60cfb", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t9a48006e1a944043bfaa41938a9b640b .toyplot-mark-popup");
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
      var axes = {"te51269b3e07f4d409f152a39bd220534": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Markers can also be added to regular plots to highlight the datums (they
are turned-off by default):

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.axes(grid=(1, 2, 0)).plot(y)
    canvas.axes(grid=(1, 2, 1)).plot(y, marker="o");



.. raw:: html

    <div align="center" class="toyplot" id="t601be05a8ba14d7e9b06b4f449316a50"><svg height="300.0px" id="te9bd9a8c798a46afbe2ac56ccaeccafc" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t7fd4dc968cb646f391af9a9ed7fff439"><clipPath id="taf56142317d04ce68154f5f8d7ba1080"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#taf56142317d04ce68154f5f8d7ba1080)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t63622ba9a11c4c89a1e548458bd1afcb" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t8009658a14b340e6a55f480b8daa67f6"><clipPath id="t85163076e6f54e4ead1c58e742b60f2c"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t85163076e6f54e4ead1c58e742b60f2c)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tb35d19c7aac34233b94590d68b312108" style="fill:none"><g class="toyplot-Series"><path d="M 360.0 240.0 L 369.0 239.50138504155126 L 378.0 238.00554016620501 L 387.0 235.51246537396122 L 396.0 232.02216066481992 L 405.0 227.53462603878117 L 414.0 222.04986149584488 L 423.0 215.56786703601105 L 432.0 208.0886426592798 L 441.0 199.61218836565098 L 450.0 190.13850415512465 L 459.0 179.66759002770081 L 468.0 168.19944598337952 L 477.0 155.73407202216069 L 486.0 142.27146814404435 L 495.0 127.81163434903047 L 504.0 112.35457063711914 L 513.0 95.900277008310283 L 522.0 78.448753462603904 L 531.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="360.0" cy="240.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="369.0" cy="239.50138504155126" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="378.0" cy="238.00554016620501" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="387.0" cy="235.51246537396122" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="396.0" cy="232.02216066481992" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="405.0" cy="227.53462603878117" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="414.0" cy="222.04986149584488" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="423.0" cy="215.56786703601105" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="432.0" cy="208.0886426592798" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="441.0" cy="199.61218836565098" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="450.0" cy="190.13850415512465" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="459.0" cy="179.66759002770081" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="468.0" cy="168.19944598337952" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="477.0" cy="155.73407202216069" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="486.0" cy="142.27146814404435" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="495.0" cy="127.81163434903047" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="504.0" cy="112.35457063711914" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="513.0" cy="95.900277008310283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="522.0" cy="78.448753462603904" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="531.0" cy="60.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t601be05a8ba14d7e9b06b4f449316a50 text");
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
          var text = document.querySelectorAll("#t601be05a8ba14d7e9b06b4f449316a50 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t63622ba9a11c4c89a1e548458bd1afcb", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "tb35d19c7aac34233b94590d68b312108", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t601be05a8ba14d7e9b06b4f449316a50 .toyplot-mark-popup");
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
      var axes = {"t7fd4dc968cb646f391af9a9ed7fff439": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "t8009658a14b340e6a55f480b8daa67f6": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


You can use the *size* argument to control the size of the markers (note
that the *size* argument is treated as an approximation of the *area* of
the marker):

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.axes(grid=(1, 2, 0)).plot(y, marker="o", size=40)
    canvas.axes(grid=(1, 2, 1)).plot(y, marker="o", size=100);



.. raw:: html

    <div align="center" class="toyplot" id="t01444e5f9d9f44f2bdd8b48eff5514f7"><svg height="300.0px" id="t29d304e41dc14f92a5a0184a7774b145" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t14b4825c999d4226b6c67bb29194ce3a"><clipPath id="t4fcc332851574af995a53d3387e1c2dc"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t4fcc332851574af995a53d3387e1c2dc)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t5485bb02af6e45209c59583924d7e01c" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="240.0" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="69.0" cy="239.50138504155126" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.0" cy="238.00554016620501" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="87.0" cy="235.51246537396122" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="96.0" cy="232.02216066481992" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="105.0" cy="227.53462603878117" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="114.0" cy="222.04986149584488" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="123.0" cy="215.56786703601105" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="132.0" cy="208.0886426592798" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="141.0" cy="199.61218836565098" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="150.0" cy="190.13850415512465" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="159.0" cy="179.66759002770081" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="168.0" cy="168.19944598337952" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="177.0" cy="155.73407202216069" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.0" cy="142.27146814404435" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="195.0" cy="127.81163434903047" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="204.0" cy="112.35457063711914" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="213.0" cy="95.900277008310283" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="222.0" cy="78.448753462603904" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="231.0" cy="60.0" r="3.1622776601683795"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="tf064860b31e44ac5a229f22b90a2dba0"><clipPath id="t004e3a0e9d5a4433a49d21a21816a1f1"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t004e3a0e9d5a4433a49d21a21816a1f1)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t8f10df6cba0242bfb997a2e671be8ec9" style="fill:none"><g class="toyplot-Series"><path d="M 360.0 240.0 L 369.0 239.50138504155126 L 378.0 238.00554016620501 L 387.0 235.51246537396122 L 396.0 232.02216066481992 L 405.0 227.53462603878117 L 414.0 222.04986149584488 L 423.0 215.56786703601105 L 432.0 208.0886426592798 L 441.0 199.61218836565098 L 450.0 190.13850415512465 L 459.0 179.66759002770081 L 468.0 168.19944598337952 L 477.0 155.73407202216069 L 486.0 142.27146814404435 L 495.0 127.81163434903047 L 504.0 112.35457063711914 L 513.0 95.900277008310283 L 522.0 78.448753462603904 L 531.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="360.0" cy="240.0" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="369.0" cy="239.50138504155126" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="378.0" cy="238.00554016620501" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="387.0" cy="235.51246537396122" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="396.0" cy="232.02216066481992" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="405.0" cy="227.53462603878117" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="414.0" cy="222.04986149584488" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="423.0" cy="215.56786703601105" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="432.0" cy="208.0886426592798" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="441.0" cy="199.61218836565098" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="450.0" cy="190.13850415512465" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="459.0" cy="179.66759002770081" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="468.0" cy="168.19944598337952" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="477.0" cy="155.73407202216069" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="486.0" cy="142.27146814404435" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="495.0" cy="127.81163434903047" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="504.0" cy="112.35457063711914" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="513.0" cy="95.900277008310283" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="522.0" cy="78.448753462603904" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="531.0" cy="60.0" r="5.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t01444e5f9d9f44f2bdd8b48eff5514f7 text");
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
          var text = document.querySelectorAll("#t01444e5f9d9f44f2bdd8b48eff5514f7 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t5485bb02af6e45209c59583924d7e01c", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t8f10df6cba0242bfb997a2e671be8ec9", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t01444e5f9d9f44f2bdd8b48eff5514f7 .toyplot-mark-popup");
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
      var axes = {"t14b4825c999d4226b6c67bb29194ce3a": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "tf064860b31e44ac5a229f22b90a2dba0": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


By default, the markers are small circles, but there are many
alternatives:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.axes(grid=(1, 2, 0)).scatterplot(y, marker="x", size=100)
    canvas.axes(grid=(1, 2, 1)).scatterplot(y, marker="^", size=100, mstyle={"stroke":toyplot.color.near_black});



.. raw:: html

    <div align="center" class="toyplot" id="tba224cd97b324d288bc4d8204959c1ef"><svg height="300.0px" id="te861843d482d4d3abe81bacffd7721f5" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t726b3e4cc0f240cd842c4a8c1de21e7c"><clipPath id="tcedc33908a6643b2a3b3fae3d1ac0c1d"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tcedc33908a6643b2a3b3fae3d1ac0c1d)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="td422412eeb6a421f832980d298aedf6e" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 60.0, 240.0)" x1="60.0" x2="60.0" y1="235.0" y2="245.0"></line><line transform="rotate(-45, 60.0, 240.0)" x1="55.0" x2="65.0" y1="240.0" y2="240.0"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 69.0, 239.50138504155126)" x1="69.0" x2="69.0" y1="234.50138504155126" y2="244.50138504155126"></line><line transform="rotate(-45, 69.0, 239.50138504155126)" x1="64.0" x2="74.0" y1="239.50138504155126" y2="239.50138504155126"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 78.0, 238.00554016620501)" x1="78.0" x2="78.0" y1="233.00554016620501" y2="243.00554016620501"></line><line transform="rotate(-45, 78.0, 238.00554016620501)" x1="73.0" x2="83.0" y1="238.00554016620501" y2="238.00554016620501"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 87.0, 235.51246537396122)" x1="87.0" x2="87.0" y1="230.51246537396122" y2="240.51246537396122"></line><line transform="rotate(-45, 87.0, 235.51246537396122)" x1="82.0" x2="92.0" y1="235.51246537396122" y2="235.51246537396122"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 96.0, 232.02216066481992)" x1="96.0" x2="96.0" y1="227.02216066481992" y2="237.02216066481992"></line><line transform="rotate(-45, 96.0, 232.02216066481992)" x1="91.0" x2="101.0" y1="232.02216066481992" y2="232.02216066481992"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 105.0, 227.53462603878117)" x1="105.0" x2="105.0" y1="222.53462603878117" y2="232.53462603878117"></line><line transform="rotate(-45, 105.0, 227.53462603878117)" x1="100.0" x2="110.0" y1="227.53462603878117" y2="227.53462603878117"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 114.0, 222.04986149584488)" x1="114.0" x2="114.0" y1="217.04986149584488" y2="227.04986149584488"></line><line transform="rotate(-45, 114.0, 222.04986149584488)" x1="109.0" x2="119.0" y1="222.04986149584488" y2="222.04986149584488"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 123.0, 215.56786703601105)" x1="123.0" x2="123.0" y1="210.56786703601105" y2="220.56786703601105"></line><line transform="rotate(-45, 123.0, 215.56786703601105)" x1="118.0" x2="128.0" y1="215.56786703601105" y2="215.56786703601105"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 132.0, 208.0886426592798)" x1="132.0" x2="132.0" y1="203.0886426592798" y2="213.0886426592798"></line><line transform="rotate(-45, 132.0, 208.0886426592798)" x1="127.0" x2="137.0" y1="208.0886426592798" y2="208.0886426592798"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 141.0, 199.61218836565098)" x1="141.0" x2="141.0" y1="194.61218836565098" y2="204.61218836565098"></line><line transform="rotate(-45, 141.0, 199.61218836565098)" x1="136.0" x2="146.0" y1="199.61218836565098" y2="199.61218836565098"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 150.0, 190.13850415512465)" x1="150.0" x2="150.0" y1="185.13850415512465" y2="195.13850415512465"></line><line transform="rotate(-45, 150.0, 190.13850415512465)" x1="145.0" x2="155.0" y1="190.13850415512465" y2="190.13850415512465"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 159.0, 179.66759002770081)" x1="159.0" x2="159.0" y1="174.66759002770081" y2="184.66759002770081"></line><line transform="rotate(-45, 159.0, 179.66759002770081)" x1="154.0" x2="164.0" y1="179.66759002770081" y2="179.66759002770081"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 168.0, 168.19944598337952)" x1="168.0" x2="168.0" y1="163.19944598337952" y2="173.19944598337952"></line><line transform="rotate(-45, 168.0, 168.19944598337952)" x1="163.0" x2="173.0" y1="168.19944598337952" y2="168.19944598337952"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 177.0, 155.73407202216069)" x1="177.0" x2="177.0" y1="150.73407202216069" y2="160.73407202216069"></line><line transform="rotate(-45, 177.0, 155.73407202216069)" x1="172.0" x2="182.0" y1="155.73407202216069" y2="155.73407202216069"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 186.0, 142.27146814404435)" x1="186.0" x2="186.0" y1="137.27146814404435" y2="147.27146814404435"></line><line transform="rotate(-45, 186.0, 142.27146814404435)" x1="181.0" x2="191.0" y1="142.27146814404435" y2="142.27146814404435"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 195.0, 127.81163434903047)" x1="195.0" x2="195.0" y1="122.81163434903047" y2="132.81163434903047"></line><line transform="rotate(-45, 195.0, 127.81163434903047)" x1="190.0" x2="200.0" y1="127.81163434903047" y2="127.81163434903047"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 204.0, 112.35457063711914)" x1="204.0" x2="204.0" y1="107.35457063711914" y2="117.35457063711914"></line><line transform="rotate(-45, 204.0, 112.35457063711914)" x1="199.0" x2="209.0" y1="112.35457063711914" y2="112.35457063711914"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 213.0, 95.900277008310283)" x1="213.0" x2="213.0" y1="90.900277008310283" y2="100.90027700831028"></line><line transform="rotate(-45, 213.0, 95.900277008310283)" x1="208.0" x2="218.0" y1="95.900277008310283" y2="95.900277008310283"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 222.0, 78.448753462603904)" x1="222.0" x2="222.0" y1="73.448753462603904" y2="83.448753462603904"></line><line transform="rotate(-45, 222.0, 78.448753462603904)" x1="217.0" x2="227.0" y1="78.448753462603904" y2="78.448753462603904"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 231.0, 60.0)" x1="231.0" x2="231.0" y1="55.0" y2="65.0"></line><line transform="rotate(-45, 231.0, 60.0)" x1="226.0" x2="236.0" y1="60.0" y2="60.0"></line></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t25cdcf1cfc1f40b892e52d63b4778668"><clipPath id="tde8a54ad40134b00beca4e510e860b2a"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tde8a54ad40134b00beca4e510e860b2a)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t2f9ca386b58449e3b29fb7b299b0ca24" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="355.0,245.0 360.0,235.0 365.0,245.0" transform="rotate(0, 360.0, 240.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="364.0,244.50138504155126 369.0,234.50138504155126 374.0,244.50138504155126" transform="rotate(0, 369.0, 239.50138504155126)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="373.0,243.00554016620501 378.0,233.00554016620501 383.0,243.00554016620501" transform="rotate(0, 378.0, 238.00554016620501)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="382.0,240.51246537396122 387.0,230.51246537396122 392.0,240.51246537396122" transform="rotate(0, 387.0, 235.51246537396122)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="391.0,237.02216066481992 396.0,227.02216066481992 401.0,237.02216066481992" transform="rotate(0, 396.0, 232.02216066481992)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="400.0,232.53462603878117 405.0,222.53462603878117 410.0,232.53462603878117" transform="rotate(0, 405.0, 227.53462603878117)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="409.0,227.04986149584488 414.0,217.04986149584488 419.0,227.04986149584488" transform="rotate(0, 414.0, 222.04986149584488)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="418.0,220.56786703601105 423.0,210.56786703601105 428.0,220.56786703601105" transform="rotate(0, 423.0, 215.56786703601105)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="427.0,213.0886426592798 432.0,203.0886426592798 437.0,213.0886426592798" transform="rotate(0, 432.0, 208.0886426592798)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="436.0,204.61218836565098 441.0,194.61218836565098 446.0,204.61218836565098" transform="rotate(0, 441.0, 199.61218836565098)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="445.0,195.13850415512465 450.0,185.13850415512465 455.0,195.13850415512465" transform="rotate(0, 450.0, 190.13850415512465)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="454.0,184.66759002770081 459.0,174.66759002770081 464.0,184.66759002770081" transform="rotate(0, 459.0, 179.66759002770081)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="463.0,173.19944598337952 468.0,163.19944598337952 473.0,173.19944598337952" transform="rotate(0, 468.0, 168.19944598337952)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="472.0,160.73407202216069 477.0,150.73407202216069 482.0,160.73407202216069" transform="rotate(0, 477.0, 155.73407202216069)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="481.0,147.27146814404435 486.0,137.27146814404435 491.0,147.27146814404435" transform="rotate(0, 486.0, 142.27146814404435)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="490.0,132.81163434903047 495.0,122.81163434903047 500.0,132.81163434903047" transform="rotate(0, 495.0, 127.81163434903047)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="499.0,117.35457063711914 504.0,107.35457063711914 509.0,117.35457063711914" transform="rotate(0, 504.0, 112.35457063711914)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="508.0,100.90027700831028 513.0,90.900277008310283 518.0,100.90027700831028" transform="rotate(0, 513.0, 95.900277008310283)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="517.0,83.448753462603904 522.0,73.448753462603904 527.0,83.448753462603904" transform="rotate(0, 522.0, 78.448753462603904)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="526.0,65.0 531.0,55.0 536.0,65.0" transform="rotate(0, 531.0, 60.0)"></polygon></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tba224cd97b324d288bc4d8204959c1ef text");
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
          var text = document.querySelectorAll("#tba224cd97b324d288bc4d8204959c1ef text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "td422412eeb6a421f832980d298aedf6e", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t2f9ca386b58449e3b29fb7b299b0ca24", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tba224cd97b324d288bc4d8204959c1ef .toyplot-mark-popup");
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
      var axes = {"t25cdcf1cfc1f40b892e52d63b4778668": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "t726b3e4cc0f240cd842c4a8c1de21e7c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Note the use of the *mstyle* argument to override the appearance of the
marker in the second example. For line plots, this allows you to style
the lines and the markers separately:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.axes(grid=(1, 2, 0)).plot(y, marker="o", size=50, style={"stroke":"darkgreen"})
    canvas.axes(grid=(1, 2, 1)).plot(y, marker="o", size=50, mstyle={"stroke":"darkgreen"});



.. raw:: html

    <div align="center" class="toyplot" id="t76a6e6be66a648b0ad1cab5d7b82cf2d"><svg height="300.0px" id="tbbe7f04d4e9e47cca68edb7e5c1aa397" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t5b06fd2a2a7144d69cd1acdbc8309f0e"><clipPath id="td262baffd3e24b9d83ff91ec0f3b34aa"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td262baffd3e24b9d83ff91ec0f3b34aa)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="td1842ea169724dddb7731f05145cccd4" style="fill:none;stroke:darkgreen"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:darkgreen;stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="240.0" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="69.0" cy="239.50138504155126" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.0" cy="238.00554016620501" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="87.0" cy="235.51246537396122" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="96.0" cy="232.02216066481992" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="105.0" cy="227.53462603878117" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="114.0" cy="222.04986149584488" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="123.0" cy="215.56786703601105" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="132.0" cy="208.0886426592798" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="141.0" cy="199.61218836565098" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="150.0" cy="190.13850415512465" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="159.0" cy="179.66759002770081" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="168.0" cy="168.19944598337952" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="177.0" cy="155.73407202216069" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.0" cy="142.27146814404435" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="195.0" cy="127.81163434903047" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="204.0" cy="112.35457063711914" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="213.0" cy="95.900277008310283" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="222.0" cy="78.448753462603904" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="231.0" cy="60.0" r="3.5355339059327378"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t0da0e93f0dd940edbe83899cfb4a660d"><clipPath id="t8f21dcb519b9499189e139ab1d76955c"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t8f21dcb519b9499189e139ab1d76955c)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t66e4b41b7c5d4c9bbf187d7620f56b3e" style="fill:none"><g class="toyplot-Series"><path d="M 360.0 240.0 L 369.0 239.50138504155126 L 378.0 238.00554016620501 L 387.0 235.51246537396122 L 396.0 232.02216066481992 L 405.0 227.53462603878117 L 414.0 222.04986149584488 L 423.0 215.56786703601105 L 432.0 208.0886426592798 L 441.0 199.61218836565098 L 450.0 190.13850415512465 L 459.0 179.66759002770081 L 468.0 168.19944598337952 L 477.0 155.73407202216069 L 486.0 142.27146814404435 L 495.0 127.81163434903047 L 504.0 112.35457063711914 L 513.0 95.900277008310283 L 522.0 78.448753462603904 L 531.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="360.0" cy="240.0" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="369.0" cy="239.50138504155126" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="378.0" cy="238.00554016620501" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="387.0" cy="235.51246537396122" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="396.0" cy="232.02216066481992" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="405.0" cy="227.53462603878117" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="414.0" cy="222.04986149584488" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="423.0" cy="215.56786703601105" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="432.0" cy="208.0886426592798" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="441.0" cy="199.61218836565098" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="450.0" cy="190.13850415512465" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="459.0" cy="179.66759002770081" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="468.0" cy="168.19944598337952" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="477.0" cy="155.73407202216069" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="486.0" cy="142.27146814404435" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="495.0" cy="127.81163434903047" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="504.0" cy="112.35457063711914" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="513.0" cy="95.900277008310283" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="522.0" cy="78.448753462603904" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="531.0" cy="60.0" r="3.5355339059327378"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t76a6e6be66a648b0ad1cab5d7b82cf2d text");
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
          var text = document.querySelectorAll("#t76a6e6be66a648b0ad1cab5d7b82cf2d text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "td1842ea169724dddb7731f05145cccd4", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t66e4b41b7c5d4c9bbf187d7620f56b3e", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t76a6e6be66a648b0ad1cab5d7b82cf2d .toyplot-mark-popup");
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
      var axes = {"t0da0e93f0dd940edbe83899cfb4a660d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "t5b06fd2a2a7144d69cd1acdbc8309f0e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


So far, we've been using string codes to specify different marker
shapes. Here is every builtin marker shape in Toyplot, with their string
codes:

.. code:: python

    markers = [None, "","|","-","+","x","*","^",">","v","<","s","d","o","oo","o|","o-","o+","ox","o*"]
    labels = [repr(marker) for marker in markers]
    mstyle = {"stroke":toyplot.color.near_black, "fill":"#feb"}
    
    canvas = toyplot.Canvas(800, 150)
    axes = canvas.axes(xmin=-1, show=False)
    axes.scatterplot(numpy.repeat(0, len(markers)), marker=markers, mstyle=mstyle, size=200)
    axes.text(numpy.arange(len(markers)), numpy.repeat(-0.5, len(markers)), text=labels, fill=toyplot.color.near_black, style={"font-size":"16px"});



.. raw:: html

    <div align="center" class="toyplot" id="t20c29a9a606b44a9b8212435c66cd49f"><svg height="150.0px" id="t09bcfc250a084d248c08f6d1c134523a" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tdaa8823fc5234a5eb0d0a59ed576778b"><clipPath id="t601dc55b35814c1cbe61b3e607a05cc9"><rect height="50.0" width="700.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t601dc55b35814c1cbe61b3e607a05cc9)" style="cursor:crosshair"><rect height="50.0" style="pointer-events:all;visibility:hidden" width="700.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t8d207ae0aa84411ca2a86396d9be407a" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><line transform="rotate(0, 157.63513513513513, 60.0)" x1="157.63513513513513" x2="157.63513513513513" y1="52.928932188134524" y2="67.071067811865476"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><line transform="rotate(-90, 190.18018018018017, 60.0)" x1="190.18018018018017" x2="190.18018018018017" y1="52.928932188134524" y2="67.071067811865476"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><line transform="rotate(0, 222.72522522522524, 60.0)" x1="222.72522522522524" x2="222.72522522522524" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(0, 222.72522522522524, 60.0)" x1="215.65415741335977" x2="229.79629303709072" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><line transform="rotate(-45, 255.27027027027026, 60.0)" x1="255.27027027027026" x2="255.27027027027026" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(-45, 255.27027027027026, 60.0)" x1="248.19920245840478" x2="262.34133808213574" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><line transform="rotate(0, 287.81531531531527, 60.0)" x1="287.81531531531527" x2="287.81531531531527" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(60, 287.81531531531527, 60.0)" x1="287.81531531531527" x2="287.81531531531527" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(-60, 287.81531531531527, 60.0)" x1="287.81531531531527" x2="287.81531531531527" y1="52.928932188134524" y2="67.071067811865476"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><polygon points="313.28929254849487,67.071067811865476 320.36036036036035,52.928932188134524 327.43142817222582,67.071067811865476" transform="rotate(0, 320.36036036036035, 60.0)"></polygon></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><polygon points="345.83433759353994,67.071067811865476 352.90540540540542,52.928932188134524 359.97647321727089,67.071067811865476" transform="rotate(-90, 352.90540540540542, 60.0)"></polygon></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><polygon points="378.37938263858501,67.071067811865476 385.45045045045049,52.928932188134524 392.52151826231596,67.071067811865476" transform="rotate(-180, 385.45045045045049, 60.0)"></polygon></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><polygon points="410.92442768363009,67.071067811865476 417.99549549549556,52.928932188134524 425.06656330736104,67.071067811865476" transform="rotate(90, 417.99549549549556, 60.0)"></polygon></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><rect height="14.142135623730951" transform="rotate(0, 450.54054054054052, 60.0)" width="14.142135623730951" x="443.46947272867504" y="52.928932188134524"></rect></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><rect height="14.142135623730951" transform="rotate(-45, 483.08558558558559, 60.0)" width="14.142135623730951" x="476.01451777372012" y="52.928932188134524"></rect></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="515.63063063063066" cy="60.0" r="7.0710678118654755"></circle></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="548.17567567567562" cy="60.0" r="7.0710678118654755"></circle><circle cx="548.17567567567562" cy="60.0" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="580.72072072072069" cy="60.0" r="7.0710678118654755"></circle><line transform="rotate(0, 580.72072072072069, 60.0)" x1="580.72072072072069" x2="580.72072072072069" y1="52.928932188134524" y2="67.071067811865476"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="613.26576576576565" cy="60.0" r="7.0710678118654755"></circle><line transform="rotate(-90, 613.26576576576565, 60.0)" x1="613.26576576576565" x2="613.26576576576565" y1="52.928932188134524" y2="67.071067811865476"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="645.81081081081084" cy="60.0" r="7.0710678118654755"></circle><line transform="rotate(0, 645.81081081081084, 60.0)" x1="645.81081081081084" x2="645.81081081081084" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(0, 645.81081081081084, 60.0)" x1="638.7397429989453" x2="652.88187862267637" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="678.35585585585579" cy="60.0" r="7.0710678118654755"></circle><line transform="rotate(-45, 678.35585585585579, 60.0)" x1="678.35585585585579" x2="678.35585585585579" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(-45, 678.35585585585579, 60.0)" x1="671.28478804399037" x2="685.42692366772121" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="710.90090090090098" cy="60.0" r="7.0710678118654755"></circle><line transform="rotate(0, 710.90090090090098, 60.0)" x1="710.90090090090098" x2="710.90090090090098" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(60, 710.90090090090098, 60.0)" x1="710.90090090090098" x2="710.90090090090098" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(-60, 710.90090090090098, 60.0)" x1="710.90090090090098" x2="710.90090090090098" y1="52.928932188134524" y2="67.071067811865476"></line></g></g></g><g class="toyplot-mark-Text" id="te6212d23b84f4d33a2a24ed72ff3551c" style="alignment-baseline:middle;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 92.545045045045043, 83.684210526315795)" x="92.545045045045043" y="83.684210526315795">None</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 125.09009009009009, 83.684210526315795)" x="125.09009009009009" y="83.684210526315795">''</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 157.63513513513513, 83.684210526315795)" x="157.63513513513513" y="83.684210526315795">'|'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 190.18018018018017, 83.684210526315795)" x="190.18018018018017" y="83.684210526315795">'-'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 222.72522522522524, 83.684210526315795)" x="222.72522522522524" y="83.684210526315795">'+'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 255.27027027027026, 83.684210526315795)" x="255.27027027027026" y="83.684210526315795">'x'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 287.81531531531527, 83.684210526315795)" x="287.81531531531527" y="83.684210526315795">'*'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 320.36036036036035, 83.684210526315795)" x="320.36036036036035" y="83.684210526315795">'^'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 352.90540540540542, 83.684210526315795)" x="352.90540540540542" y="83.684210526315795">'&gt;'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 385.45045045045049, 83.684210526315795)" x="385.45045045045049" y="83.684210526315795">'v'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 417.99549549549556, 83.684210526315795)" x="417.99549549549556" y="83.684210526315795">'&lt;'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 450.54054054054052, 83.684210526315795)" x="450.54054054054052" y="83.684210526315795">'s'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 483.08558558558559, 83.684210526315795)" x="483.08558558558559" y="83.684210526315795">'d'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 515.63063063063066, 83.684210526315795)" x="515.63063063063066" y="83.684210526315795">'o'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 548.17567567567562, 83.684210526315795)" x="548.17567567567562" y="83.684210526315795">'oo'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 580.72072072072069, 83.684210526315795)" x="580.72072072072069" y="83.684210526315795">'o|'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 613.26576576576565, 83.684210526315795)" x="613.26576576576565" y="83.684210526315795">'o-'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 645.81081081081084, 83.684210526315795)" x="645.81081081081084" y="83.684210526315795">'o+'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 678.35585585585579, 83.684210526315795)" x="678.35585585585579" y="83.684210526315795">'ox'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 710.90090090090098, 83.684210526315795)" x="710.90090090090098" y="83.684210526315795">'o*'</text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="650.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="695.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t20c29a9a606b44a9b8212435c66cd49f text");
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
          var text = document.querySelectorAll("#t20c29a9a606b44a9b8212435c66cd49f text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], "names": ["x", "y0"], "id": "t8d207ae0aa84411ca2a86396d9be407a", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t20c29a9a606b44a9b8212435c66cd49f .toyplot-mark-popup");
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
      var axes = {"tdaa8823fc5234a5eb0d0a59ed576778b": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 19.894117647058824, "min": -1}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 740.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.0, "min": -0.6333333333333333}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 90.0}, "scale": "linear"}]}};
    
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


There are several items worth noting - first, you can pass a sequence of
marker codes to the *marker* argument, to specify markers on a
per-series or per-datum basis. Second, you can pass an empty string or
*None* to produce an invisible marker, if you need to hide a datum or
declutter the display. Third, note that several of the marker shapes
contain internal details that require a contrasting stroke and fill to
be visible.

So far, we've been using the marker shape code to specify our markers,
but this is actually a shortcut. A full marker specification takes the
form of a Python dictionary:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.axes(grid=(1, 2, 0)).scatterplot(y, marker={"shape":"|", "angle":45}, size=100)
    canvas.axes(grid=(1, 2, 1)).scatterplot(y, marker={"shape":"o", "label":"A"}, size=200, mlstyle={"fill":"white"});



.. raw:: html

    <div align="center" class="toyplot" id="tdeecc3937a2c456bb47a631770368d2f"><svg height="300.0px" id="t6ffac00073a64e69b0730a08d54e11f4" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t387dd90b6ad1471cb0cb72f12bf9ef60"><clipPath id="tb02f3def1eaa4724a8c47c1a7c1d8b79"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb02f3def1eaa4724a8c47c1a7c1d8b79)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="te887e6ee2bda458eb138df93bd72933a" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 60.0, 240.0)" x1="60.0" x2="60.0" y1="235.0" y2="245.0"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 69.0, 239.50138504155126)" x1="69.0" x2="69.0" y1="234.50138504155126" y2="244.50138504155126"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 78.0, 238.00554016620501)" x1="78.0" x2="78.0" y1="233.00554016620501" y2="243.00554016620501"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 87.0, 235.51246537396122)" x1="87.0" x2="87.0" y1="230.51246537396122" y2="240.51246537396122"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 96.0, 232.02216066481992)" x1="96.0" x2="96.0" y1="227.02216066481992" y2="237.02216066481992"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 105.0, 227.53462603878117)" x1="105.0" x2="105.0" y1="222.53462603878117" y2="232.53462603878117"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 114.0, 222.04986149584488)" x1="114.0" x2="114.0" y1="217.04986149584488" y2="227.04986149584488"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 123.0, 215.56786703601105)" x1="123.0" x2="123.0" y1="210.56786703601105" y2="220.56786703601105"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 132.0, 208.0886426592798)" x1="132.0" x2="132.0" y1="203.0886426592798" y2="213.0886426592798"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 141.0, 199.61218836565098)" x1="141.0" x2="141.0" y1="194.61218836565098" y2="204.61218836565098"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 150.0, 190.13850415512465)" x1="150.0" x2="150.0" y1="185.13850415512465" y2="195.13850415512465"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 159.0, 179.66759002770081)" x1="159.0" x2="159.0" y1="174.66759002770081" y2="184.66759002770081"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 168.0, 168.19944598337952)" x1="168.0" x2="168.0" y1="163.19944598337952" y2="173.19944598337952"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 177.0, 155.73407202216069)" x1="177.0" x2="177.0" y1="150.73407202216069" y2="160.73407202216069"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 186.0, 142.27146814404435)" x1="186.0" x2="186.0" y1="137.27146814404435" y2="147.27146814404435"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 195.0, 127.81163434903047)" x1="195.0" x2="195.0" y1="122.81163434903047" y2="132.81163434903047"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 204.0, 112.35457063711914)" x1="204.0" x2="204.0" y1="107.35457063711914" y2="117.35457063711914"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 213.0, 95.900277008310283)" x1="213.0" x2="213.0" y1="90.900277008310283" y2="100.90027700831028"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 222.0, 78.448753462603904)" x1="222.0" x2="222.0" y1="73.448753462603904" y2="83.448753462603904"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 231.0, 60.0)" x1="231.0" x2="231.0" y1="55.0" y2="65.0"></line></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t3edd643cc2964ff492835cb7d3fb253c"><clipPath id="ta79c10f07b834d54ad8f00b5a4bc2823"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta79c10f07b834d54ad8f00b5a4bc2823)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tb686e82f48f84ecf898ff2d53d133d02" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="360.0" cy="240.0" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="360.0" y="240.0">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="369.0" cy="239.50138504155126" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="369.0" y="239.50138504155126">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="378.0" cy="238.00554016620501" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="378.0" y="238.00554016620501">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="387.0" cy="235.51246537396122" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="387.0" y="235.51246537396122">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="396.0" cy="232.02216066481992" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="396.0" y="232.02216066481992">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="405.0" cy="227.53462603878117" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="405.0" y="227.53462603878117">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="414.0" cy="222.04986149584488" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="414.0" y="222.04986149584488">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="423.0" cy="215.56786703601105" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="423.0" y="215.56786703601105">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="432.0" cy="208.0886426592798" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="432.0" y="208.0886426592798">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="441.0" cy="199.61218836565098" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="441.0" y="199.61218836565098">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="450.0" cy="190.13850415512465" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="450.0" y="190.13850415512465">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="459.0" cy="179.66759002770081" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="459.0" y="179.66759002770081">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="468.0" cy="168.19944598337952" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="468.0" y="168.19944598337952">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="477.0" cy="155.73407202216069" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="477.0" y="155.73407202216069">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="486.0" cy="142.27146814404435" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="486.0" y="142.27146814404435">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="495.0" cy="127.81163434903047" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="495.0" y="127.81163434903047">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="504.0" cy="112.35457063711914" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="504.0" y="112.35457063711914">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="513.0" cy="95.900277008310283" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="513.0" y="95.900277008310283">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="522.0" cy="78.448753462603904" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="522.0" y="78.448753462603904">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="531.0" cy="60.0" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="531.0" y="60.0">A</text></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tdeecc3937a2c456bb47a631770368d2f text");
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
          var text = document.querySelectorAll("#tdeecc3937a2c456bb47a631770368d2f text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "te887e6ee2bda458eb138df93bd72933a", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "tb686e82f48f84ecf898ff2d53d133d02", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tdeecc3937a2c456bb47a631770368d2f .toyplot-mark-popup");
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
      var axes = {"t387dd90b6ad1471cb0cb72f12bf9ef60": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "t3edd643cc2964ff492835cb7d3fb253c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Using the full marker specification allows you to control additional
parameters such as the marker angle and label. Also note the *mlstyle*
argument which controls the style of the marker label, independently of
the marker itself.

You can also use custom marker shapes, specifying the shape as an SVG
path:

.. code:: python

    custom_marker = {"shape":"path", "path":"m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z"}
    canvas, axes, mark = toyplot.scatterplot(0, 0, size=0.1, marker=custom_marker, color="#004712", width=400);
    axes.hlines(0, style={"stroke-width":0.1})
    axes.vlines(0, style={"stroke-width":0.1});



.. raw:: html

    <div align="center" class="toyplot" id="t3f5901888e9847e6a00963f33cc575ad"><svg height="400.0px" id="ta262bc29408543489856b5834ee56436" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t8d65479803e7499db7249f679b604008"><clipPath id="t8ebdfa04310948508f900bb856037499"><rect height="300.0" width="300.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t8ebdfa04310948508f900bb856037499)" style="cursor:crosshair"><rect height="300.0" style="pointer-events:all;visibility:hidden" width="300.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="td8f92bb7e7104003932fe95662b121b7" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 200.0 200.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(200.0, 200.0) scale(0.31622776601683794) translate(-200.0, -200.0)"></path></g></g></g><g class="toyplot-mark-AxisLines" id="tc6688e79a22148ff91f659fb61ed1297" style="stroke-width:0.1"><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgba(16.1%,15.3%,14.1%,1);stroke-width:0.1" x1="50" x2="350.0" y1="200.0" y2="200.0"></line></g></g><g class="toyplot-mark-AxisLines" id="tb8a8988cb88f4f878c11f26365a1ff17" style="stroke-width:0.1"><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgba(16.1%,15.3%,14.1%,1);stroke-width:0.1" x1="200.0" x2="200.0" y1="50" y2="350.0"></line></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="250.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="295.0" y="67.0"></text></g><line style="" x1="200.0" x2="200.0" y1="350.0" y2="350.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="350.0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="200.0" y="350.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="340.0" y="350.0">0.5</text></g><line style="" x1="50" x2="50" y1="200.0" y2="200.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 340.0)" x="50" y="340.0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 200.0)" x="50" y="200.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">0.5</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t3f5901888e9847e6a00963f33cc575ad text");
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
          var text = document.querySelectorAll("#t3f5901888e9847e6a00963f33cc575ad text");
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
      var data_tables = [{"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "td8f92bb7e7104003932fe95662b121b7", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t3f5901888e9847e6a00963f33cc575ad .toyplot-mark-popup");
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
      var axes = {"t8d65479803e7499db7249f679b604008": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 340.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 340.0}, "scale": "linear"}]}};
    
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


Note that the SVG path must contain only relative coordinates, or the
marker will not render correctly. In this example the marker was
exported as SVG from a drawing application, the path was run through an
`online conversion process <http://bl.ocks.org/themcmurder/6393419>`__
to convert absolute coordinates to relative coordinates, and the initial
"move" (m) command was adjusted to center the graphic. For custom
markers, the *size* argument currently acts as a simple scaling factor
on the marker (this may change in the future). Here is an (admittedly
silly) example of a custom marker at work:

.. code:: python

    x = numpy.linspace(0, 100, 10)
    y = (0.1 * x) ** 2
    canvas, axes, mark = toyplot.scatterplot(x, y, size=.015, color="#004712", marker=custom_marker, xlabel="Years", ylabel="Oak Tree Population", padding=25, width=600);



.. raw:: html

    <div align="center" class="toyplot" id="t917849858fd14f74b3ff7f20446de6fa"><svg height="600.0px" id="t9a27fd448007404dab6724a6c8990809" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc633f9f8611547b88834c04ac6b24d3d"><clipPath id="t103087e016ce4a48ab5922c08c17aec8"><rect height="500.0" width="500.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t103087e016ce4a48ab5922c08c17aec8)" style="cursor:crosshair"><rect height="500.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t4b6c2a1e6b8f488a9d3d961f03c37fc3" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 75.0 525.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(75.0, 525.0) scale(0.1224744871391589) translate(-75.0, -525.0)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 124.99999999999999 519.44444444444446m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(124.99999999999999, 519.44444444444446) scale(0.1224744871391589) translate(-124.99999999999999, -519.44444444444446)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 175.0 502.77777777777777m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(175.0, 502.77777777777777) scale(0.1224744871391589) translate(-175.0, -502.77777777777777)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 224.99999999999997 475.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(224.99999999999997, 475.0) scale(0.1224744871391589) translate(-224.99999999999997, -475.0)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 275.0 436.11111111111114m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(275.0, 436.11111111111114) scale(0.1224744871391589) translate(-275.0, -436.11111111111114)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 325.0 386.11111111111109m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(325.0, 386.11111111111109) scale(0.1224744871391589) translate(-325.0, -386.11111111111109)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 374.99999999999994 325.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(374.99999999999994, 325.0) scale(0.1224744871391589) translate(-374.99999999999994, -325.0)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 424.99999999999994 252.77777777777783m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(424.99999999999994, 252.77777777777783) scale(0.1224744871391589) translate(-424.99999999999994, -252.77777777777783)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 474.99999999999994 169.4444444444444m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(474.99999999999994, 169.4444444444444) scale(0.1224744871391589) translate(-474.99999999999994, -169.4444444444444)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 525.0 75.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(525.0, 75.0) scale(0.1224744871391589) translate(-525.0, -75.0)"></path></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="75.0" x2="525.0" y1="550.0" y2="550.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="75.0" y="550.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="300.0" y="550.0">50</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="525.0" y="550.0">100</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="300.0" y="550.0">Years</text><line style="" x1="50" x2="50" y1="75.0" y2="525.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 525.0)" x="50" y="525.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 300.0)" x="50" y="300.0">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 75.0)" x="50" y="75.0">100</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 300.0)" x="50" y="300.0">Oak Tree Population</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t917849858fd14f74b3ff7f20446de6fa text");
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
          var text = document.querySelectorAll("#t917849858fd14f74b3ff7f20446de6fa text");
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
      var data_tables = [{"data": [[0.0, 11.11111111111111, 22.22222222222222, 33.33333333333333, 44.44444444444444, 55.55555555555556, 66.66666666666666, 77.77777777777777, 88.88888888888889, 100.0], [0.0, 1.234567901234568, 4.938271604938272, 11.111111111111109, 19.75308641975309, 30.864197530864207, 44.444444444444436, 60.49382716049382, 79.01234567901236, 100.0]], "names": ["x", "y0"], "id": "t4b6c2a1e6b8f488a9d3d961f03c37fc3", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t917849858fd14f74b3ff7f20446de6fa .toyplot-mark-popup");
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
      var axes = {"tc633f9f8611547b88834c04ac6b24d3d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 100.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 525.0, "min": 75.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 100.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 75.0, "min": 525.0}, "scale": "linear"}]}};
    
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


