
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
Axes
====

In Toyplot, axes are used to map data values into canvas coordinates.
The axes *range* (the area on the canvas that they occupy) is specified
when they are created. Their *domain* is implicitly defined to include
all of the data in the plot (but can be manually overridden by the
caller if desired).

When using Toyplot's convenience APIs - :py:func:`toyplot.bars`,
:py:func:`toyplot.fill`, :py:func:`toyplot.plot`, and
:py:func:`toyplot.scatterplot`, the axes are created automatically and
returned from the function within a ``(canvas, axes, mark)`` tuple. By
default, the axes are sized to fill the entire canvas:

.. code:: python

    import numpy
    y = numpy.linspace(0, 1, 20) ** 2
.. code:: python

    import toyplot
    canvas, axes, mark = toyplot.plot(y, width=300)


.. raw:: html

    <div align="center" class="toyplot" id="tc05e2122a2284aaf86aacf6513b77c0c"><svg height="300px" id="tae007de44bc04f7aa45b2ea1bde393b5" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="300px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="t1aad5ad4e6284cd2a51e870daaffc275"><toyplot:axes>{"y": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 1.0, "min": 0.0}}], "x": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 20.0, "min": 0}}]}</toyplot:axes><clipPath id="tddf9bcef40f54b94a25ea3f53f8ffed6"><rect height="200" width="200" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tddf9bcef40f54b94a25ea3f53f8ffed6)" style="cursor:crosshair;"><rect height="200" style="pointer-events:all;visibility:hidden;" width="200" x="50" y="50"></rect><g class="toyplot-PlotMark" id="t966d1f4d70cd4a08ad73676893974dce" style="fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.501385042 L 78.0 238.005540166 L 87.0 235.512465374 L 96.0 232.022160665 L 105.0 227.534626039 L 114.0 222.049861496 L 123.0 215.567867036 L 132.0 208.088642659 L 141.0 199.612188366 L 150.0 190.138504155 L 159.0 179.667590028 L 168.0 168.199445983 L 177.0 155.734072022 L 186.0 142.271468144 L 195.0 127.811634349 L 204.0 112.354570637 L 213.0 95.9002770083 L 222.0 78.4487534626 L 231.0 60.0" style="stroke:rgba(40%,76.1%,64.7%,1);stroke-width:2.0;stroke-opacity:1.0;fill:none;"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="150" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250" y2="250"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="250">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="105.0" y="250">5</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="150.0" y="250">10</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="195.0" y="250">15</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="240.0" y="250">20</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">0.0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">0.5</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#tc05e2122a2284aaf86aacf6513b77c0c text");
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
              var text = document.querySelectorAll("#tc05e2122a2284aaf86aacf6513b77c0c text");
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
          var root_id="tc05e2122a2284aaf86aacf6513b77c0c";
    
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
          var root_id="tc05e2122a2284aaf86aacf6513b77c0c";
    
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
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


If you need greater control over the positioning of the axes within the
canvas, or want to add multiple axes to one canvas, it's necessary to
create the canvas and axes explicitly, then use the axes to plot your
data:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(grid=(1, 2, 0))
    axes1.plot(y)
    axes2 = canvas.axes(grid=(1, 2, 1))
    axes2.plot(1 - y);


.. raw:: html

    <div align="center" class="toyplot" id="t3d9810c779c8422ca02dd9040572ec23"><svg height="300px" id="tefaf0c26c7314412b3b1e641a763c223" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="t23def8960a9746cca28c86654a81d87a"><toyplot:axes>{"y": [{"range": {"max": 240.0, "min": 60.0}, "scale": "linear", "domain": {"max": 1.0, "min": 0.0}}], "x": [{"range": {"max": 240.0, "min": 60.0}, "scale": "linear", "domain": {"max": 20.0, "min": 0}}]}</toyplot:axes><clipPath id="t2957ceea79b3446492bb69879c57af15"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2957ceea79b3446492bb69879c57af15)" style="cursor:crosshair;"><rect height="200.0" style="pointer-events:all;visibility:hidden;" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-PlotMark" id="t2761425b7fa54dc781d4990297d81f02" style="fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.501385042 L 78.0 238.005540166 L 87.0 235.512465374 L 96.0 232.022160665 L 105.0 227.534626039 L 114.0 222.049861496 L 123.0 215.567867036 L 132.0 208.088642659 L 141.0 199.612188366 L 150.0 190.138504155 L 159.0 179.667590028 L 168.0 168.199445983 L 177.0 155.734072022 L 186.0 142.271468144 L 195.0 127.811634349 L 204.0 112.354570637 L 213.0 95.9002770083 L 222.0 78.4487534626 L 231.0 60.0" style="stroke:rgba(40%,76.1%,64.7%,1);stroke-width:2.0;stroke-opacity:1.0;fill:none;"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14.0" style="opacity:0.75;stroke:none;fill:white;" width="90.0" x="150.0" y="60.0"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="250.0">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="105.0" y="250.0">5</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="150.0" y="250.0">10</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="195.0" y="250.0">15</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-Axes2D" id="t4a3cc594109141238c66e6e4fcaebd1d"><toyplot:axes>{"y": [{"range": {"max": 240.0, "min": 60.0}, "scale": "linear", "domain": {"max": 1.0, "min": 0.0}}], "x": [{"range": {"max": 540.0, "min": 360.0}, "scale": "linear", "domain": {"max": 20.0, "min": 0}}]}</toyplot:axes><clipPath id="t1833297778c34ed091504165da0a9ebd"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t1833297778c34ed091504165da0a9ebd)" style="cursor:crosshair;"><rect height="200.0" style="pointer-events:all;visibility:hidden;" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-PlotMark" id="t28bfe30d65a94d64bcd6ff1d92fc9cdd" style="fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 360.0 60.0 L 369.0 60.4986149584 L 378.0 61.9944598338 L 387.0 64.487534626 L 396.0 67.9778393352 L 405.0 72.4653739612 L 414.0 77.9501385042 L 423.0 84.432132964 L 432.0 91.9113573407 L 441.0 100.387811634 L 450.0 109.861495845 L 459.0 120.332409972 L 468.0 131.800554017 L 477.0 144.265927978 L 486.0 157.728531856 L 495.0 172.188365651 L 504.0 187.645429363 L 513.0 204.099722992 L 522.0 221.551246537 L 531.0 240.0" style="stroke:rgba(40%,76.1%,64.7%,1);stroke-width:2.0;stroke-opacity:1.0;fill:none;"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14.0" style="opacity:0.75;stroke:none;fill:white;" width="90.0" x="450.0" y="60.0"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="360.0" y="250.0">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="405.0" y="250.0">5</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="450.0" y="250.0">10</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="495.0" y="250.0">15</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t3d9810c779c8422ca02dd9040572ec23 text");
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
              var text = document.querySelectorAll("#t3d9810c779c8422ca02dd9040572ec23 text");
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
          var root_id="t3d9810c779c8422ca02dd9040572ec23";
    
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
          var root_id="t3d9810c779c8422ca02dd9040572ec23";
    
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
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


The axes object contains a set of nested properties that can be used to
adjust its behavior. The list of available properties includes the
following:

-  axes.show - set to *False* to hide the axes completely (the plotted
   data will still be visible).
-  axes.padding - controls a small gap, measured in canvas drawing
   units, between the axes and their contents.
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
   ("log", ) tuple.
-  axes.x.label.text - optional label below the X axis.
-  axes.x.label.style - styles the X axis label.
-  axes.x.spine.show - set to *False* to hide the X axis spine.
-  axes.x.spine.position - set to "low", "high", or a Y axis domain
   value to position the spine. Defaults to "low".
-  axes.x.spine.style - styles the X axis spine.
-  axes.x.ticks.show - set to *False* to hide the X axis ticks and tick
   labels.
-  axes.x.ticks.locator - :py:class:`toyplot.BasicTickLocator`,
   :py:class:`toyplot.ExtendedTickLocator`,
   :py:class:`toyplot.ExplicitTickLocator`,
   :py:class:`toyplot.HeckbertTickLocator`,
   :py:class:`toyplot.PositiveLogTickLocator`,
   :py:class:`toyplot.NegativeLogTickLocator`, or
   :py:class:`toyplot.SymmetricLogTickLocator` to control the
   positioning and formatting of ticks and tick labels. By default, an
   appropriate locator is automatically chosen based on the axis scale.
-  axes.x.ticks.length - controls the length of X axis ticks measured in
   canvas drawing units.
-  axes.x.ticks.style - styles the X axis ticks.
-  axes.x.ticks.labels.show - set to *False* to hide X axis tick labels.
-  axes.x.ticks.labels.angle - set the angle of X axis tick labels in
   degrees.
-  axes.x.ticks.labels.style - style X axis tick label text.
-  ... and equivalent properties for the Y axis.

For example, to override several of the axes default properties:

.. code:: python

    x = numpy.linspace(0, 2 * numpy.pi)
    y = numpy.sin(x)
.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes()
    axes.label.text = "Trigonometry 101"
    axes.x.label.text = "x"
    axes.y.label.text = "sin(x)"
    axes.x.ticks.show = True
    axes.x.ticks.locator = toyplot.ExplicitTickLocator(
        [0, numpy.pi / 2, numpy.pi, 3 * numpy.pi / 2, 2 * numpy.pi],
        ["0", "pi / 2", "pi", "3 pi / 2", "2 pi"])
    mark = axes.plot(x, y)


.. raw:: html

    <div align="center" class="toyplot" id="t9ee92135a2d14b1ea3a3ac60570c146d"><svg height="300px" id="t3ff93a00feb14bad87f9ff59000329a6" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="t1e877da38e2c4e008fa5d8358d0dfde4"><toyplot:axes>{"y": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 1.0, "min": -1.0}}], "x": [{"range": {"max": 540, "min": 60}, "scale": "linear", "domain": {"max": 6.2831853071795862, "min": 0.0}}]}</toyplot:axes><clipPath id="t83c605415fb14de3969944c74693cbed"><rect height="200" width="500" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t83c605415fb14de3969944c74693cbed)" style="cursor:crosshair;"><rect height="200" style="pointer-events:all;visibility:hidden;" width="500" x="50" y="50"></rect><g class="toyplot-PlotMark" id="t94920ef61fbb4d8cbbaa52517868f8a7" style="fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0.0, 0.1282282715750936, 0.2564565431501872, 0.38468481472528077, 0.5129130863003744, 0.6411413578754679, 0.7693696294505615, 0.8975979010256552, 1.0258261726007487, 1.1540544441758422, 1.2822827157509358, 1.4105109873260295, 1.538739258901123, 1.6669675304762166, 1.7951958020513104, 1.9234240736264039, 2.0516523452014974, 2.179880616776591, 2.3081088883516845, 2.436337159926778, 2.5645654315018716, 2.6927937030769655, 2.821021974652059, 2.9492502462271526, 3.077478517802246, 3.2057067893773397, 3.333935060952433, 3.4621633325275267, 3.5903916041026207, 3.7186198756777142, 3.8468481472528078, 3.9750764188279013, 4.103304690402995, 4.231532961978089, 4.359761233553182, 4.487989505128276, 4.616217776703369, 4.744446048278463, 4.872674319853556, 5.00090259142865, 5.129130863003743, 5.257359134578837, 5.385587406153931, 5.513815677729024, 5.642043949304118, 5.770272220879211, 5.898500492454305, 6.026728764029398, 6.154957035604492, 6.283185307179586], [0.0, 0.127877161684506, 0.25365458390950735, 0.3752670048793741, 0.49071755200393785, 0.5981105304912159, 0.6956825506034864, 0.7818314824680297, 0.8551427630053461, 0.9144126230158124, 0.9586678530366606, 0.9871817834144501, 0.9994862162006879, 0.9953791129491982, 0.9749279121818236, 0.9384684220497604, 0.8865993063730001, 0.8201722545969561, 0.7402779970753157, 0.6482283953077888, 0.545534901210549, 0.43388373911755823, 0.3151082180236208, 0.19115862870137254, 0.06407021998071323, -0.06407021998071254, -0.19115862870137187, -0.3151082180236202, -0.433883739117558, -0.5455349012105485, -0.6482283953077882, -0.7402779970753153, -0.8201722545969556, -0.8865993063730001, -0.9384684220497602, -0.9749279121818235, -0.9953791129491981, -0.9994862162006879, -0.9871817834144503, -0.9586678530366608, -0.9144126230158128, -0.8551427630053465, -0.7818314824680299, -0.6956825506034869, -0.5981105304912162, -0.49071755200393863, -0.3752670048793746, -0.25365458390950835, -0.12787716168450664, -2.4492935982947064e-16]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 150.0 L 69.7959183673 138.491055448 L 79.5918367347 127.171087448 L 89.387755102 116.225969561 L 99.1836734694 105.83542032 L 108.979591837 96.1700522558 L 118.775510204 87.3885704457 L 128.571428571 79.6351665779 L 138.367346939 73.0371513295 L 148.163265306 67.7028639286 L 157.959183673 63.7198932267 L 167.755102041 61.1536394927 L 177.551020408 60.0462405419 L 187.346938776 60.4158798346 L 197.142857143 62.2564879036 L 206.93877551 65.5378420155 L 216.734693878 70.2060624264 L 226.530612245 76.1844970863 L 236.326530612 83.3749802632 L 246.12244898 91.6594444223 L 255.918367347 100.901858891 L 265.714285714 110.950463479 L 275.510204082 121.640260378 L 285.306122449 132.795723417 L 295.102040816 144.233680202 L 304.897959184 155.766319798 L 314.693877551 167.204276583 L 324.489795918 178.359739622 L 334.285714286 189.049536521 L 344.081632653 199.098141109 L 353.87755102 208.340555578 L 363.673469388 216.625019737 L 373.469387755 223.815502914 L 383.265306122 229.793937574 L 393.06122449 234.462157984 L 402.857142857 237.743512096 L 412.653061224 239.584120165 L 422.448979592 239.953759458 L 432.244897959 238.846360507 L 442.040816327 236.280106773 L 451.836734694 232.297136071 L 461.632653061 226.96284867 L 471.428571429 220.364833422 L 481.224489796 212.611429554 L 491.020408163 203.829947744 L 500.816326531 194.16457968 L 510.612244898 183.774030439 L 520.408163265 172.828912552 L 530.204081633 161.508944552 L 540.0 150.0" style="stroke:rgba(40%,76.1%,64.7%,1);stroke-width:2.0;stroke-opacity:1.0;fill:none;"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="450" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="540.0" y1="250" y2="250"></line><g><line style="" x1="60.0" x2="60.0" y1="250" y2="245"></line><line style="" x1="180.0" x2="180.0" y1="250" y2="245"></line><line style="" x1="300.0" x2="300.0" y1="250" y2="245"></line><line style="" x1="420.0" x2="420.0" y1="250" y2="245"></line><line style="" x1="540.0" x2="540.0" y1="250" y2="245"></line></g><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="250">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="180.0" y="250">pi / 2</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="300.0" y="250">pi</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="420.0" y="250">3 pi / 2</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="540.0" y="250">2 pi</text></g><text style="stroke:none;font-weight:bold;baseline-shift:-200%;text-anchor:middle;alignment-baseline:middle;" x="300.0" y="250">x</text><line style="" x1="50" x2="50" y1="60.0462405419" y2="239.953759458"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">-1.0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 195.0)" x="50" y="195.0">-0.5</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">0.0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 105.0)" x="50" y="105.0">0.5</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">1.0</text></g><text style="stroke:none;font-weight:bold;baseline-shift:200%;text-anchor:middle;alignment-baseline:middle;" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">sin(x)</text><text style="stroke:none;baseline-shift:100%;alignment-baseline:middle;font-weight:bold;font-size:14px;text-anchor:middle;" x="300.0" y="50">Trigonometry 101</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t9ee92135a2d14b1ea3a3ac60570c146d text");
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
              var text = document.querySelectorAll("#t9ee92135a2d14b1ea3a3ac60570c146d text");
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
          var root_id="t9ee92135a2d14b1ea3a3ac60570c146d";
    
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
          var root_id="t9ee92135a2d14b1ea3a3ac60570c146d";
    
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
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


