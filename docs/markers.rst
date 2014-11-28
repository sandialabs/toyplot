
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

    <div align="center" class="toyplot" id="t776b2699b0764998a0e508dbac6e7e90"><svg height="300px" id="te505d0b1c2584f128c5ee379179203c3" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t4e9a062ee4d64cf8a61b7ff3debeb0fa"><toyplot:axes>{"x": [{"domain": {"max": 20.0, "min": 0}, "range": {"max": 240, "min": 60}, "scale": "linear"}], "y": [{"domain": {"max": 1.0, "min": 0.0}, "range": {"max": 240, "min": 60}, "scale": "linear"}]}</toyplot:axes><clipPath id="t97ac9d2bc3c84820b1a6019c9bbb1a77"><rect height="200" width="200" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t97ac9d2bc3c84820b1a6019c9bbb1a77)" style="cursor:crosshair"><rect height="200" style="pointer-events:all;visibility:hidden" width="200" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t3b3b72ce18a24344a1d77ab2a94c144d" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="240.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="69.0" cy="239.50138504155126" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.0" cy="238.00554016620498" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="87.0" cy="235.51246537396122" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="96.0" cy="232.02216066481995" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="105.0" cy="227.53462603878117" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="114.0" cy="222.04986149584488" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="123.0" cy="215.56786703601108" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="132.0" cy="208.08864265927977" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="141.0" cy="199.61218836565098" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="150.0" cy="190.13850415512465" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="159.0" cy="179.66759002770084" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="168.0" cy="168.19944598337952" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="177.0" cy="155.73407202216069" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.0" cy="142.27146814404432" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="195.0" cy="127.81163434903047" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="204.0" cy="112.35457063711914" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="213.0" cy="95.900277008310283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="222.0" cy="78.448753462603904" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="231.0" cy="60.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90" x="150" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250" y2="250"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250">20</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t776b2699b0764998a0e508dbac6e7e90 text");
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
              var text = document.querySelectorAll("#t776b2699b0764998a0e508dbac6e7e90 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t776b2699b0764998a0e508dbac6e7e90";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t776b2699b0764998a0e508dbac6e7e90";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
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

    <div align="center" class="toyplot" id="t9296b691f4754149b7c2db699f8eaa75"><svg height="300px" id="tf1e4bcb46869403baabf05e7407e0737" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tfa7fb13519fc4959baa32be3f3015232"><toyplot:axes>{"x": [{"domain": {"max": 20.0, "min": 0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 1.0, "min": 0.0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="td5387eb92ecf439c9fab470f7648c56b"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td5387eb92ecf439c9fab470f7648c56b)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t23377568457344538feb8f8e77a13bba" style="fill:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620498 L 87.0 235.51246537396122 L 96.0 232.02216066481995 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601108 L 132.0 208.08864265927977 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770084 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404432 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="te3fab0b36f344539a9c32b6fb4ffa23f"><toyplot:axes>{"x": [{"domain": {"max": 20.0, "min": 0}, "range": {"max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"max": 1.0, "min": 0.0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="tb99352f139c4482da599b7bcaf906095"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb99352f139c4482da599b7bcaf906095)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t6bf29b384c4c42d6962b6ac336cfd586" style="fill:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 360.0 240.0 L 369.0 239.50138504155126 L 378.0 238.00554016620498 L 387.0 235.51246537396122 L 396.0 232.02216066481995 L 405.0 227.53462603878117 L 414.0 222.04986149584488 L 423.0 215.56786703601108 L 432.0 208.08864265927977 L 441.0 199.61218836565098 L 450.0 190.13850415512465 L 459.0 179.66759002770084 L 468.0 168.19944598337952 L 477.0 155.73407202216069 L 486.0 142.27146814404432 L 495.0 127.81163434903047 L 504.0 112.35457063711914 L 513.0 95.900277008310283 L 522.0 78.448753462603904 L 531.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="360.0" cy="240.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="369.0" cy="239.50138504155126" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="378.0" cy="238.00554016620498" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="387.0" cy="235.51246537396122" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="396.0" cy="232.02216066481995" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="405.0" cy="227.53462603878117" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="414.0" cy="222.04986149584488" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="423.0" cy="215.56786703601108" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="432.0" cy="208.08864265927977" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="441.0" cy="199.61218836565098" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="450.0" cy="190.13850415512465" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="459.0" cy="179.66759002770084" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="468.0" cy="168.19944598337952" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="477.0" cy="155.73407202216069" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="486.0" cy="142.27146814404432" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="495.0" cy="127.81163434903047" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="504.0" cy="112.35457063711914" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="513.0" cy="95.900277008310283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="522.0" cy="78.448753462603904" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="531.0" cy="60.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t9296b691f4754149b7c2db699f8eaa75 text");
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
              var text = document.querySelectorAll("#t9296b691f4754149b7c2db699f8eaa75 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t9296b691f4754149b7c2db699f8eaa75";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t9296b691f4754149b7c2db699f8eaa75";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
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

    <div align="center" class="toyplot" id="tc4c325785da14035a2a1d803266e1a01"><svg height="300px" id="t274a705c9487495382c92da6b3eb6baf" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t6bb87fe7a56d4155b1ab173c63ebb540"><toyplot:axes>{"x": [{"domain": {"max": 20.0, "min": 0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 1.0, "min": 0.0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t757cc2e2407e4e0b95fcbe3e6ae3de99"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t757cc2e2407e4e0b95fcbe3e6ae3de99)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t1d5c8d0a54cb4545a77108d693d17e06" style="fill:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620498 L 87.0 235.51246537396122 L 96.0 232.02216066481995 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601108 L 132.0 208.08864265927977 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770084 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404432 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="240.0" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="69.0" cy="239.50138504155126" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.0" cy="238.00554016620498" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="87.0" cy="235.51246537396122" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="96.0" cy="232.02216066481995" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="105.0" cy="227.53462603878117" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="114.0" cy="222.04986149584488" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="123.0" cy="215.56786703601108" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="132.0" cy="208.08864265927977" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="141.0" cy="199.61218836565098" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="150.0" cy="190.13850415512465" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="159.0" cy="179.66759002770084" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="168.0" cy="168.19944598337952" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="177.0" cy="155.73407202216069" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.0" cy="142.27146814404432" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="195.0" cy="127.81163434903047" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="204.0" cy="112.35457063711914" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="213.0" cy="95.900277008310283" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="222.0" cy="78.448753462603904" r="3.1622776601683795"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="231.0" cy="60.0" r="3.1622776601683795"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t1e482184aabb40fa82793feaa1c1f1b6"><toyplot:axes>{"x": [{"domain": {"max": 20.0, "min": 0}, "range": {"max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"max": 1.0, "min": 0.0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t25eb1e8082f34c3dad37d4a9d1c4af00"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t25eb1e8082f34c3dad37d4a9d1c4af00)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t779b8004d3ac489689af1eb1624eaa6d" style="fill:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 360.0 240.0 L 369.0 239.50138504155126 L 378.0 238.00554016620498 L 387.0 235.51246537396122 L 396.0 232.02216066481995 L 405.0 227.53462603878117 L 414.0 222.04986149584488 L 423.0 215.56786703601108 L 432.0 208.08864265927977 L 441.0 199.61218836565098 L 450.0 190.13850415512465 L 459.0 179.66759002770084 L 468.0 168.19944598337952 L 477.0 155.73407202216069 L 486.0 142.27146814404432 L 495.0 127.81163434903047 L 504.0 112.35457063711914 L 513.0 95.900277008310283 L 522.0 78.448753462603904 L 531.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="360.0" cy="240.0" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="369.0" cy="239.50138504155126" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="378.0" cy="238.00554016620498" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="387.0" cy="235.51246537396122" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="396.0" cy="232.02216066481995" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="405.0" cy="227.53462603878117" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="414.0" cy="222.04986149584488" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="423.0" cy="215.56786703601108" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="432.0" cy="208.08864265927977" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="441.0" cy="199.61218836565098" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="450.0" cy="190.13850415512465" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="459.0" cy="179.66759002770084" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="468.0" cy="168.19944598337952" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="477.0" cy="155.73407202216069" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="486.0" cy="142.27146814404432" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="495.0" cy="127.81163434903047" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="504.0" cy="112.35457063711914" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="513.0" cy="95.900277008310283" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="522.0" cy="78.448753462603904" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="531.0" cy="60.0" r="5.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#tc4c325785da14035a2a1d803266e1a01 text");
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
              var text = document.querySelectorAll("#tc4c325785da14035a2a1d803266e1a01 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="tc4c325785da14035a2a1d803266e1a01";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="tc4c325785da14035a2a1d803266e1a01";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
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

    <div align="center" class="toyplot" id="tca2530ea2d574fc79263572cd9785992"><svg height="300px" id="tc66d63b35cca4049bc966789b91064c3" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t476228657cd1414a9ebdc1c04543afb6"><toyplot:axes>{"x": [{"domain": {"max": 20.0, "min": 0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 1.0, "min": 0.0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t63900cfdef9c4c9c809a3f2fc433b52a"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t63900cfdef9c4c9c809a3f2fc433b52a)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t6974bfe169b44b4a88c660234c123272" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 60.0, 240.0)" x1="60.0" x2="60.0" y1="235.0" y2="245.0"></line><line transform="rotate(45, 60.0, 240.0)" x1="55.0" x2="65.0" y1="240.0" y2="240.0"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 69.0, 239.50138504155126)" x1="69.0" x2="69.0" y1="234.50138504155126" y2="244.50138504155126"></line><line transform="rotate(45, 69.0, 239.50138504155126)" x1="64.0" x2="74.0" y1="239.50138504155126" y2="239.50138504155126"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 78.0, 238.00554016620498)" x1="78.0" x2="78.0" y1="233.00554016620498" y2="243.00554016620498"></line><line transform="rotate(45, 78.0, 238.00554016620498)" x1="73.0" x2="83.0" y1="238.00554016620498" y2="238.00554016620498"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 87.0, 235.51246537396122)" x1="87.0" x2="87.0" y1="230.51246537396122" y2="240.51246537396122"></line><line transform="rotate(45, 87.0, 235.51246537396122)" x1="82.0" x2="92.0" y1="235.51246537396122" y2="235.51246537396122"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 96.0, 232.02216066481995)" x1="96.0" x2="96.0" y1="227.02216066481995" y2="237.02216066481995"></line><line transform="rotate(45, 96.0, 232.02216066481995)" x1="91.0" x2="101.0" y1="232.02216066481995" y2="232.02216066481995"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 105.0, 227.53462603878117)" x1="105.0" x2="105.0" y1="222.53462603878117" y2="232.53462603878117"></line><line transform="rotate(45, 105.0, 227.53462603878117)" x1="100.0" x2="110.0" y1="227.53462603878117" y2="227.53462603878117"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 114.0, 222.04986149584488)" x1="114.0" x2="114.0" y1="217.04986149584488" y2="227.04986149584488"></line><line transform="rotate(45, 114.0, 222.04986149584488)" x1="109.0" x2="119.0" y1="222.04986149584488" y2="222.04986149584488"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 123.0, 215.56786703601108)" x1="123.0" x2="123.0" y1="210.56786703601108" y2="220.56786703601108"></line><line transform="rotate(45, 123.0, 215.56786703601108)" x1="118.0" x2="128.0" y1="215.56786703601108" y2="215.56786703601108"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 132.0, 208.08864265927977)" x1="132.0" x2="132.0" y1="203.08864265927977" y2="213.08864265927977"></line><line transform="rotate(45, 132.0, 208.08864265927977)" x1="127.0" x2="137.0" y1="208.08864265927977" y2="208.08864265927977"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 141.0, 199.61218836565098)" x1="141.0" x2="141.0" y1="194.61218836565098" y2="204.61218836565098"></line><line transform="rotate(45, 141.0, 199.61218836565098)" x1="136.0" x2="146.0" y1="199.61218836565098" y2="199.61218836565098"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 150.0, 190.13850415512465)" x1="150.0" x2="150.0" y1="185.13850415512465" y2="195.13850415512465"></line><line transform="rotate(45, 150.0, 190.13850415512465)" x1="145.0" x2="155.0" y1="190.13850415512465" y2="190.13850415512465"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 159.0, 179.66759002770084)" x1="159.0" x2="159.0" y1="174.66759002770084" y2="184.66759002770084"></line><line transform="rotate(45, 159.0, 179.66759002770084)" x1="154.0" x2="164.0" y1="179.66759002770084" y2="179.66759002770084"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 168.0, 168.19944598337952)" x1="168.0" x2="168.0" y1="163.19944598337952" y2="173.19944598337952"></line><line transform="rotate(45, 168.0, 168.19944598337952)" x1="163.0" x2="173.0" y1="168.19944598337952" y2="168.19944598337952"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 177.0, 155.73407202216069)" x1="177.0" x2="177.0" y1="150.73407202216069" y2="160.73407202216069"></line><line transform="rotate(45, 177.0, 155.73407202216069)" x1="172.0" x2="182.0" y1="155.73407202216069" y2="155.73407202216069"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 186.0, 142.27146814404432)" x1="186.0" x2="186.0" y1="137.27146814404432" y2="147.27146814404432"></line><line transform="rotate(45, 186.0, 142.27146814404432)" x1="181.0" x2="191.0" y1="142.27146814404432" y2="142.27146814404432"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 195.0, 127.81163434903047)" x1="195.0" x2="195.0" y1="122.81163434903047" y2="132.81163434903047"></line><line transform="rotate(45, 195.0, 127.81163434903047)" x1="190.0" x2="200.0" y1="127.81163434903047" y2="127.81163434903047"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 204.0, 112.35457063711914)" x1="204.0" x2="204.0" y1="107.35457063711914" y2="117.35457063711914"></line><line transform="rotate(45, 204.0, 112.35457063711914)" x1="199.0" x2="209.0" y1="112.35457063711914" y2="112.35457063711914"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 213.0, 95.900277008310283)" x1="213.0" x2="213.0" y1="90.900277008310283" y2="100.90027700831028"></line><line transform="rotate(45, 213.0, 95.900277008310283)" x1="208.0" x2="218.0" y1="95.900277008310283" y2="95.900277008310283"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 222.0, 78.448753462603904)" x1="222.0" x2="222.0" y1="73.448753462603904" y2="83.448753462603904"></line><line transform="rotate(45, 222.0, 78.448753462603904)" x1="217.0" x2="227.0" y1="78.448753462603904" y2="78.448753462603904"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(45, 231.0, 60.0)" x1="231.0" x2="231.0" y1="55.0" y2="65.0"></line><line transform="rotate(45, 231.0, 60.0)" x1="226.0" x2="236.0" y1="60.0" y2="60.0"></line></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t0f7ddbeabc764e0696be6f7cd1f3cf16"><toyplot:axes>{"x": [{"domain": {"max": 20.0, "min": 0}, "range": {"max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"max": 1.0, "min": 0.0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="te61c30b45f0c451a8ef87f3853781f07"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te61c30b45f0c451a8ef87f3853781f07)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="teaec4428fd0441a9b0f93568630c6174" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], ["^", "^", "^", "^", "^", "^", "^", "^", "^", "^", "^", "^", "^", "^", "^", "^", "^", "^", "^", "^"], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="355.0,245.0 360.0,235.0 365.0,245.0" transform="rotate(0, 360.0, 240.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="364.0,244.50138504155126 369.0,234.50138504155126 374.0,244.50138504155126" transform="rotate(0, 369.0, 239.50138504155126)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="373.0,243.00554016620498 378.0,233.00554016620498 383.0,243.00554016620498" transform="rotate(0, 378.0, 238.00554016620498)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="382.0,240.51246537396122 387.0,230.51246537396122 392.0,240.51246537396122" transform="rotate(0, 387.0, 235.51246537396122)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="391.0,237.02216066481995 396.0,227.02216066481995 401.0,237.02216066481995" transform="rotate(0, 396.0, 232.02216066481995)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="400.0,232.53462603878117 405.0,222.53462603878117 410.0,232.53462603878117" transform="rotate(0, 405.0, 227.53462603878117)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="409.0,227.04986149584488 414.0,217.04986149584488 419.0,227.04986149584488" transform="rotate(0, 414.0, 222.04986149584488)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="418.0,220.56786703601108 423.0,210.56786703601108 428.0,220.56786703601108" transform="rotate(0, 423.0, 215.56786703601108)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="427.0,213.08864265927977 432.0,203.08864265927977 437.0,213.08864265927977" transform="rotate(0, 432.0, 208.08864265927977)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="436.0,204.61218836565098 441.0,194.61218836565098 446.0,204.61218836565098" transform="rotate(0, 441.0, 199.61218836565098)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="445.0,195.13850415512465 450.0,185.13850415512465 455.0,195.13850415512465" transform="rotate(0, 450.0, 190.13850415512465)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="454.0,184.66759002770084 459.0,174.66759002770084 464.0,184.66759002770084" transform="rotate(0, 459.0, 179.66759002770084)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="463.0,173.19944598337952 468.0,163.19944598337952 473.0,173.19944598337952" transform="rotate(0, 468.0, 168.19944598337952)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="472.0,160.73407202216069 477.0,150.73407202216069 482.0,160.73407202216069" transform="rotate(0, 477.0, 155.73407202216069)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="481.0,147.27146814404432 486.0,137.27146814404432 491.0,147.27146814404432" transform="rotate(0, 486.0, 142.27146814404432)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="490.0,132.81163434903047 495.0,122.81163434903047 500.0,132.81163434903047" transform="rotate(0, 495.0, 127.81163434903047)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="499.0,117.35457063711914 504.0,107.35457063711914 509.0,117.35457063711914" transform="rotate(0, 504.0, 112.35457063711914)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="508.0,100.90027700831028 513.0,90.900277008310283 518.0,100.90027700831028" transform="rotate(0, 513.0, 95.900277008310283)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="517.0,83.448753462603904 522.0,73.448753462603904 527.0,83.448753462603904" transform="rotate(0, 522.0, 78.448753462603904)"></polygon></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:#292724"><polygon points="526.0,65.0 531.0,55.0 536.0,65.0" transform="rotate(0, 531.0, 60.0)"></polygon></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#tca2530ea2d574fc79263572cd9785992 text");
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
              var text = document.querySelectorAll("#tca2530ea2d574fc79263572cd9785992 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="tca2530ea2d574fc79263572cd9785992";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="tca2530ea2d574fc79263572cd9785992";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
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

    <div align="center" class="toyplot" id="ta1a018a485f746fd800730f079102dcf"><svg height="300px" id="tccba4c2c87c545bda2b8c5fde0ed9789" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t4792927097cb4ddba6a17a373207917c"><toyplot:axes>{"x": [{"domain": {"max": 20.0, "min": 0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 1.0, "min": 0.0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t889a529e9e9f496b85f5d216bdbb4bf4"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t889a529e9e9f496b85f5d216bdbb4bf4)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t7c201ccfe0004bf891d5e75e9620059f" style="fill:none;stroke:darkgreen"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620498 L 87.0 235.51246537396122 L 96.0 232.02216066481995 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601108 L 132.0 208.08864265927977 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770084 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404432 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:darkgreen;stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="240.0" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="69.0" cy="239.50138504155126" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.0" cy="238.00554016620498" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="87.0" cy="235.51246537396122" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="96.0" cy="232.02216066481995" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="105.0" cy="227.53462603878117" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="114.0" cy="222.04986149584488" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="123.0" cy="215.56786703601108" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="132.0" cy="208.08864265927977" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="141.0" cy="199.61218836565098" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="150.0" cy="190.13850415512465" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="159.0" cy="179.66759002770084" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="168.0" cy="168.19944598337952" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="177.0" cy="155.73407202216069" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.0" cy="142.27146814404432" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="195.0" cy="127.81163434903047" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="204.0" cy="112.35457063711914" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="213.0" cy="95.900277008310283" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="222.0" cy="78.448753462603904" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="231.0" cy="60.0" r="3.5355339059327378"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t694a4726e1344ea0b03857793f0fabbc"><toyplot:axes>{"x": [{"domain": {"max": 20.0, "min": 0}, "range": {"max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"max": 1.0, "min": 0.0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="tfc7c3633710b4d6a8f37f45e6dcef8db"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tfc7c3633710b4d6a8f37f45e6dcef8db)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t532f4e14bcd94d038e1284a6346d9156" style="fill:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 360.0 240.0 L 369.0 239.50138504155126 L 378.0 238.00554016620498 L 387.0 235.51246537396122 L 396.0 232.02216066481995 L 405.0 227.53462603878117 L 414.0 222.04986149584488 L 423.0 215.56786703601108 L 432.0 208.08864265927977 L 441.0 199.61218836565098 L 450.0 190.13850415512465 L 459.0 179.66759002770084 L 468.0 168.19944598337952 L 477.0 155.73407202216069 L 486.0 142.27146814404432 L 495.0 127.81163434903047 L 504.0 112.35457063711914 L 513.0 95.900277008310283 L 522.0 78.448753462603904 L 531.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="360.0" cy="240.0" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="369.0" cy="239.50138504155126" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="378.0" cy="238.00554016620498" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="387.0" cy="235.51246537396122" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="396.0" cy="232.02216066481995" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="405.0" cy="227.53462603878117" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="414.0" cy="222.04986149584488" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="423.0" cy="215.56786703601108" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="432.0" cy="208.08864265927977" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="441.0" cy="199.61218836565098" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="450.0" cy="190.13850415512465" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="459.0" cy="179.66759002770084" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="468.0" cy="168.19944598337952" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="477.0" cy="155.73407202216069" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="486.0" cy="142.27146814404432" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="495.0" cy="127.81163434903047" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="504.0" cy="112.35457063711914" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="513.0" cy="95.900277008310283" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="522.0" cy="78.448753462603904" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:darkgreen"><circle cx="531.0" cy="60.0" r="3.5355339059327378"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#ta1a018a485f746fd800730f079102dcf text");
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
              var text = document.querySelectorAll("#ta1a018a485f746fd800730f079102dcf text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="ta1a018a485f746fd800730f079102dcf";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="ta1a018a485f746fd800730f079102dcf";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
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

    <div align="center" class="toyplot" id="tf857a38408314f2abe2ccbc0a0eb2c06"><svg height="150px" id="t8b14389c7d224a9ca497b1d730ed9dce" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="800px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t1071649c59df419eb8a04a5eef3f150c"><toyplot:axes>{"x": [{"domain": {"max": 20.0, "min": -1}, "range": {"max": 740, "min": 60}, "scale": "linear"}], "y": [{"domain": {"max": 0.0, "min": -0.5}, "range": {"max": 90, "min": 60}, "scale": "linear"}]}</toyplot:axes><clipPath id="t9389993e9f6c4a87826bcc36a30c276a"><rect height="50" width="700" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9389993e9f6c4a87826bcc36a30c276a)" style="cursor:crosshair"><rect height="50" style="pointer-events:all;visibility:hidden" width="700" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t63c17c0d8d1d43f7a01a06ed8811e3ff" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [null, "", "|", "-", "+", "x", "*", "^", "&gt;", "v", "&lt;", "s", "d", "o", "oo", "o|", "o-", "o+", "ox", "o*"], [200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><line transform="rotate(0, 157.14285714285714, 60.0)" x1="157.14285714285714" x2="157.14285714285714" y1="52.928932188134524" y2="67.071067811865476"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><line transform="rotate(90, 189.52380952380952, 60.0)" x1="189.52380952380952" x2="189.52380952380952" y1="52.928932188134524" y2="67.071067811865476"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><line transform="rotate(0, 221.9047619047619, 60.0)" x1="221.9047619047619" x2="221.9047619047619" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(0, 221.9047619047619, 60.0)" x1="214.83369409289642" x2="228.97582971662737" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><line transform="rotate(45, 254.28571428571428, 60.0)" x1="254.28571428571428" x2="254.28571428571428" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(45, 254.28571428571428, 60.0)" x1="247.2146464738488" x2="261.35678209757975" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><line transform="rotate(0, 286.66666666666663, 60.0)" x1="286.66666666666663" x2="286.66666666666663" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(-60, 286.66666666666663, 60.0)" x1="286.66666666666663" x2="286.66666666666663" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(60, 286.66666666666663, 60.0)" x1="286.66666666666663" x2="286.66666666666663" y1="52.928932188134524" y2="67.071067811865476"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><polygon points="311.97655123575356,67.071067811865476 319.04761904761904,52.928932188134524 326.11868685948451,67.071067811865476" transform="rotate(0, 319.04761904761904, 60.0)"></polygon></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><polygon points="344.35750361670591,67.071067811865476 351.42857142857139,52.928932188134524 358.49963924043686,67.071067811865476" transform="rotate(90, 351.42857142857139, 60.0)"></polygon></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><polygon points="376.73845599765832,67.071067811865476 383.8095238095238,52.928932188134524 390.88059162138927,67.071067811865476" transform="rotate(180, 383.8095238095238, 60.0)"></polygon></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><polygon points="409.11940837861073,67.071067811865476 416.1904761904762,52.928932188134524 423.26154400234168,67.071067811865476" transform="rotate(-90, 416.1904761904762, 60.0)"></polygon></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><rect height="14.142135623730951" transform="rotate(0, 448.57142857142856, 60.0)" width="14.142135623730951" x="441.50036075956308" y="52.928932188134524"></rect></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><rect height="14.142135623730951" transform="rotate(45, 480.95238095238096, 60.0)" width="14.142135623730951" x="473.88131314051549" y="52.928932188134524"></rect></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="513.33333333333326" cy="60.0" r="7.0710678118654755"></circle></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="545.71428571428578" cy="60.0" r="7.0710678118654755"></circle><circle cx="545.71428571428578" cy="60.0" r="3.5355339059327378"></circle></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="578.09523809523807" cy="60.0" r="7.0710678118654755"></circle><line transform="rotate(0, 578.09523809523807, 60.0)" x1="578.09523809523807" x2="578.09523809523807" y1="52.928932188134524" y2="67.071067811865476"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="610.47619047619048" cy="60.0" r="7.0710678118654755"></circle><line transform="rotate(90, 610.47619047619048, 60.0)" x1="610.47619047619048" x2="610.47619047619048" y1="52.928932188134524" y2="67.071067811865476"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="642.85714285714278" cy="60.0" r="7.0710678118654755"></circle><line transform="rotate(0, 642.85714285714278, 60.0)" x1="642.85714285714278" x2="642.85714285714278" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(0, 642.85714285714278, 60.0)" x1="635.78607504527736" x2="649.92821066900819" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="675.2380952380953" cy="60.0" r="7.0710678118654755"></circle><line transform="rotate(45, 675.2380952380953, 60.0)" x1="675.2380952380953" x2="675.2380952380953" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(45, 675.2380952380953, 60.0)" x1="668.16702742622988" x2="682.30916304996072" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="fill:#feb;opacity:1.0;stroke:#292724"><circle cx="707.61904761904759" cy="60.0" r="7.0710678118654755"></circle><line transform="rotate(0, 707.61904761904759, 60.0)" x1="707.61904761904759" x2="707.61904761904759" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(-60, 707.61904761904759, 60.0)" x1="707.61904761904759" x2="707.61904761904759" y1="52.928932188134524" y2="67.071067811865476"></line><line transform="rotate(60, 707.61904761904759, 60.0)" x1="707.61904761904759" x2="707.61904761904759" y1="52.928932188134524" y2="67.071067811865476"></line></g></g></g><g class="toyplot-mark-Text" id="te22dbc15a8bf4e4d8ab1b62df37b9e43" style="alignment-baseline:middle;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle"><toyplot:data-table title="Text Data">{"data": [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0], [-0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5], ["None", "''", "'|'", "'-'", "'+'", "'x'", "'*'", "'^'", "'&gt;'", "'v'", "'&lt;'", "'s'", "'d'", "'o'", "'oo'", "'o|'", "'o-'", "'o+'", "'ox'", "'o*'"], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], ["#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724", "#292724"], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null], [0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902, 0.1607843137254902], [0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825, 0.15294117647058825], [0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353, 0.1411764705882353], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y", "text", "angle", "fill", "opacity", "title", "toyplot:fill:red", "toyplot:fill:green", "toyplot:fill:blue", "toyplot:fill:alpha"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 92.38095238095238, 90.0)" x="92.38095238095238" y="90.0">None</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 124.76190476190476, 90.0)" x="124.76190476190476" y="90.0">''</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 157.14285714285714, 90.0)" x="157.14285714285714" y="90.0">'|'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 189.52380952380952, 90.0)" x="189.52380952380952" y="90.0">'-'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 221.9047619047619, 90.0)" x="221.9047619047619" y="90.0">'+'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 254.28571428571428, 90.0)" x="254.28571428571428" y="90.0">'x'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 286.66666666666663, 90.0)" x="286.66666666666663" y="90.0">'*'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 319.04761904761904, 90.0)" x="319.04761904761904" y="90.0">'^'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 351.42857142857139, 90.0)" x="351.42857142857139" y="90.0">'&gt;'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 383.8095238095238, 90.0)" x="383.8095238095238" y="90.0">'v'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 416.1904761904762, 90.0)" x="416.1904761904762" y="90.0">'&lt;'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 448.57142857142856, 90.0)" x="448.57142857142856" y="90.0">'s'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 480.95238095238096, 90.0)" x="480.95238095238096" y="90.0">'d'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 513.33333333333326, 90.0)" x="513.33333333333326" y="90.0">'o'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 545.71428571428578, 90.0)" x="545.71428571428578" y="90.0">'oo'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 578.09523809523807, 90.0)" x="578.09523809523807" y="90.0">'o|'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 610.47619047619048, 90.0)" x="610.47619047619048" y="90.0">'o-'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 642.85714285714278, 90.0)" x="642.85714285714278" y="90.0">'o+'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 675.2380952380953, 90.0)" x="675.2380952380953" y="90.0">'ox'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(0.0, 707.61904761904759, 90.0)" x="707.61904761904759" y="90.0">'o*'</text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90" x="650" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="695.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#tf857a38408314f2abe2ccbc0a0eb2c06 text");
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
              var text = document.querySelectorAll("#tf857a38408314f2abe2ccbc0a0eb2c06 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="tf857a38408314f2abe2ccbc0a0eb2c06";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="tf857a38408314f2abe2ccbc0a0eb2c06";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
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
    canvas.axes(grid=(1, 2, 0)).scatterplot(y, marker={"shape":"|", "angle":-45}, size=100)
    canvas.axes(grid=(1, 2, 1)).scatterplot(y, marker={"shape":"o", "label":"A"}, size=200, mlstyle={"fill":"white"});


.. raw:: html

    <div align="center" class="toyplot" id="t0b989d78e3a84bc2a43da3d3776ae069"><svg height="300px" id="t0a6278ea0b8e490981525a0d0c211b56" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tb63100a151fe45308401daee3f8fb48f"><toyplot:axes>{"x": [{"domain": {"max": 9, "min": 0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"max": 100.0, "min": 0.0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="tce3ec9136f414d83bdad3a63d2d4624e"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tce3ec9136f414d83bdad3a63d2d4624e)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="ta37e7e8dcbf2490f8190f2387748b07a" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0.0, 1.234567901234568, 4.938271604938272, 11.111111111111109, 19.75308641975309, 30.864197530864207, 44.444444444444436, 60.49382716049382, 79.01234567901236, 100.0], [{"angle": -45, "shape": "|"}, {"angle": -45, "shape": "|"}, {"angle": -45, "shape": "|"}, {"angle": -45, "shape": "|"}, {"angle": -45, "shape": "|"}, {"angle": -45, "shape": "|"}, {"angle": -45, "shape": "|"}, {"angle": -45, "shape": "|"}, {"angle": -45, "shape": "|"}, {"angle": -45, "shape": "|"}], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 60.0, 240.0)" x1="60.0" x2="60.0" y1="235.0" y2="245.0"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 80.0, 237.77777777777777)" x1="80.0" x2="80.0" y1="232.77777777777777" y2="242.77777777777777"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 100.0, 231.11111111111111)" x1="100.0" x2="100.0" y1="226.11111111111111" y2="236.11111111111111"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 120.0, 220.0)" x1="120.0" x2="120.0" y1="215.0" y2="225.0"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 140.0, 204.44444444444446)" x1="140.0" x2="140.0" y1="199.44444444444446" y2="209.44444444444446"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 160.0, 184.44444444444446)" x1="160.0" x2="160.0" y1="179.44444444444446" y2="189.44444444444446"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 180.0, 160.0)" x1="180.0" x2="180.0" y1="155.0" y2="165.0"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 200.0, 131.11111111111114)" x1="200.0" x2="200.0" y1="126.11111111111114" y2="136.11111111111114"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 220.0, 97.777777777777771)" x1="220.0" x2="220.0" y1="92.777777777777771" y2="102.77777777777777"></line></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><line transform="rotate(-45, 240.0, 60.0)" x1="240.0" x2="240.0" y1="55.0" y2="65.0"></line></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="240.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="120.0" y="250.0">3</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="180.0" y="250.0">6</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">9</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">100</text></g></g><g class="toyplot-axes-Cartesian" id="t34f09e703fb145078b3a22cc145ea42d"><toyplot:axes>{"x": [{"domain": {"max": 9, "min": 0}, "range": {"max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"max": 100.0, "min": 0.0}, "range": {"max": 240.0, "min": 60.0}, "scale": "linear"}]}</toyplot:axes><clipPath id="t60c3f4ce6fb94158bc9c8859a11d1bbc"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t60c3f4ce6fb94158bc9c8859a11d1bbc)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t1d4272d51d0d4b6d94a6ee544715db79" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0.0, 1.234567901234568, 4.938271604938272, 11.111111111111109, 19.75308641975309, 30.864197530864207, 44.444444444444436, 60.49382716049382, 79.01234567901236, 100.0], [{"label": "A", "shape": "o"}, {"label": "A", "shape": "o"}, {"label": "A", "shape": "o"}, {"label": "A", "shape": "o"}, {"label": "A", "shape": "o"}, {"label": "A", "shape": "o"}, {"label": "A", "shape": "o"}, {"label": "A", "shape": "o"}, {"label": "A", "shape": "o"}, {"label": "A", "shape": "o"}], [200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="360.0" cy="240.0" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="360.0" y="240.0">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="380.0" cy="237.77777777777777" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="380.0" y="237.77777777777777">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="400.0" cy="231.11111111111111" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="400.0" y="231.11111111111111">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="420.0" cy="220.0" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="420.0" y="220.0">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="440.0" cy="204.44444444444446" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="440.0" y="204.44444444444446">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="460.0" cy="184.44444444444446" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="460.0" y="184.44444444444446">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="480.0" cy="160.0" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="480.0" y="160.0">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="500.0" cy="131.11111111111114" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="500.0" y="131.11111111111114">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="520.0" cy="97.777777777777771" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="520.0" y="97.777777777777771">A</text></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="540.0" cy="60.0" r="7.0710678118654755"></circle><text style="alignment-baseline:middle;fill:white;font-size:10.606601717798213px;stroke:none;text-anchor:middle" x="540.0" y="60.0">A</text></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="540.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="420.0" y="250.0">3</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="480.0" y="250.0">6</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">9</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">100</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t0b989d78e3a84bc2a43da3d3776ae069 text");
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
              var text = document.querySelectorAll("#t0b989d78e3a84bc2a43da3d3776ae069 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t0b989d78e3a84bc2a43da3d3776ae069";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t0b989d78e3a84bc2a43da3d3776ae069";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
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

    <div align="center" class="toyplot" id="tcfb6a8b3282e401ba89a4612079aea28"><svg height="400px" id="t3289a076537c48608d5efa1c9f9c75c0" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="400px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t7ddc401bd05f47d78deb492b8b59a3e7"><toyplot:axes>{"x": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 340, "min": 60}, "scale": "linear"}], "y": [{"domain": {"max": 0.5, "min": -0.5}, "range": {"max": 340, "min": 60}, "scale": "linear"}]}</toyplot:axes><clipPath id="t96f695a3dd3a4b62a2534eed5f156f3d"><rect height="300" width="300" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t96f695a3dd3a4b62a2534eed5f156f3d)" style="cursor:crosshair"><rect height="300" style="pointer-events:all;visibility:hidden" width="300" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t7bf7e024334e48ac9731c2d946e0b7ac" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0.0], [0.0], [{"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}], [0.1], [0.0], [0.2784313725490196], [0.07058823529411765], [1.0], [0.0], [0.2784313725490196], [0.07058823529411765], [1.0], [1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 200.0 200.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(200.0, 200.0) scale(0.31622776601683794) translate(-200.0, -200.0)"></path></g></g></g><g class="toyplot-mark-AxisLines" id="t865216d0db024585a90da0737b88d601" style="stroke-width:0.1"><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgba(16.1%,15.3%,14.1%,1);stroke-width:0.1" x1="50" x2="350" y1="200.0" y2="200.0"></line></g></g><g class="toyplot-mark-AxisLines" id="tc3dd733763bd48588b657050af50f99a" style="stroke-width:0.1"><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgba(16.1%,15.3%,14.1%,1);stroke-width:0.1" x1="200.0" x2="200.0" y1="50" y2="350"></line></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90" x="250" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="295.0" y="67.0"></text></g><line style="" x1="200.0" x2="200.0" y1="350" y2="350"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="350">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="200.0" y="350">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="340.0" y="350">0.5</text></g><line style="" x1="50" x2="50" y1="200.0" y2="200.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 340.0)" x="50" y="340.0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 200.0)" x="50" y="200.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">0.5</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#tcfb6a8b3282e401ba89a4612079aea28 text");
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
              var text = document.querySelectorAll("#tcfb6a8b3282e401ba89a4612079aea28 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="tcfb6a8b3282e401ba89a4612079aea28";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="tcfb6a8b3282e401ba89a4612079aea28";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
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

    <div align="center" class="toyplot" id="t140bc6e9f9964217b2a546dd083bc10a"><svg height="600px" id="t6394cc2521744a2a80351386c08531f4" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="te5ae1b6c5b484dfba318b3b30fde850e"><toyplot:axes>{"x": [{"domain": {"max": 100.0, "min": 0.0}, "range": {"max": 525, "min": 75}, "scale": "linear"}], "y": [{"domain": {"max": 100.0, "min": 0.0}, "range": {"max": 525, "min": 75}, "scale": "linear"}]}</toyplot:axes><clipPath id="tfadc9fc10e7248bdb621f9e5dbe0532f"><rect height="500" width="500" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tfadc9fc10e7248bdb621f9e5dbe0532f)" style="cursor:crosshair"><rect height="500" style="pointer-events:all;visibility:hidden" width="500" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="tca2fdb8939fa4978a20209ec3e175a55" style="stroke:none"><toyplot:data-table title="Plot Data">{"data": [[0.0, 11.11111111111111, 22.22222222222222, 33.33333333333333, 44.44444444444444, 55.55555555555556, 66.66666666666666, 77.77777777777777, 88.88888888888889, 100.0], [0.0, 1.234567901234568, 4.938271604938272, 11.111111111111109, 19.75308641975309, 30.864197530864207, 44.444444444444436, 60.49382716049382, 79.01234567901236, 100.0], [{"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}, {"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}, {"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}, {"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}, {"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}, {"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}, {"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}, {"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}, {"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}, {"path": "m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z", "shape": "path"}], [0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196], [0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196, 0.2784313725490196], [0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765, 0.07058823529411765], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 75.0 525.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(75.0, 525.0) scale(0.1224744871391589) translate(-75.0, -525.0)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 125.0 519.44444444444434m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(125.0, 519.44444444444434) scale(0.1224744871391589) translate(-125.0, -519.44444444444434)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 175.0 502.77777777777777m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(175.0, 502.77777777777777) scale(0.1224744871391589) translate(-175.0, -502.77777777777777)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 224.99999999999997 475.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(224.99999999999997, 475.0) scale(0.1224744871391589) translate(-224.99999999999997, -475.0)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 275.0 436.11111111111114m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(275.0, 436.11111111111114) scale(0.1224744871391589) translate(-275.0, -436.11111111111114)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 325.0 386.11111111111109m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(325.0, 386.11111111111109) scale(0.1224744871391589) translate(-325.0, -386.11111111111109)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 374.99999999999994 325.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(374.99999999999994, 325.0) scale(0.1224744871391589) translate(-374.99999999999994, -325.0)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 424.99999999999994 252.77777777777783m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(424.99999999999994, 252.77777777777783) scale(0.1224744871391589) translate(-424.99999999999994, -252.77777777777783)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 475.0 169.4444444444444m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(475.0, 169.4444444444444) scale(0.1224744871391589) translate(-475.0, -169.4444444444444)"></path></g><g class="toyplot-Datum" style="fill:rgba(0%,27.8%,7.06%,1);opacity:1.0;stroke:rgba(0%,27.8%,7.06%,1)"><path d="M 525.0 75.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(525.0, 75.0) scale(0.1224744871391589) translate(-525.0, -75.0)"></path></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90" x="450" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="75.0" x2="525.0" y1="550" y2="550"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="75.0" y="550">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="300.0" y="550">50</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="525.0" y="550">100</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="300.0" y="550">Years</text><line style="" x1="50" x2="50" y1="75.0" y2="525.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 525.0)" x="50" y="525.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 300.0)" x="50" y="300.0">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 75.0)" x="50" y="75.0">100</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 300.0)" x="50" y="300.0">Oak Tree Population</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t140bc6e9f9964217b2a546dd083bc10a text");
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
              var text = document.querySelectorAll("#t140bc6e9f9964217b2a546dd083bc10a text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t140bc6e9f9964217b2a546dd083bc10a";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t140bc6e9f9964217b2a546dd083bc10a";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-axes-Cartesian .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


