
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
Axes
====

In Toyplot, axes are used to map data coordinates into canvas
coordinates. The axes *range* (the area on the canvas that they occupy)
is specified when they are created. Their *domain* is implicitly defined
to include all of the data in the plot (but can be manually overridden
by the caller if desired).

When using Toyplot's convenience API - :py:func:`toyplot.bars`,
:py:func:`toyplot.fill`, :py:func:`toyplot.plot`, and
:py:func:`toyplot.scatterplot`, axes are created for you
automatically, and returned from the function as part of a
``(canvas, axes, mark)`` tuple. In this case, the axes are sized to fill
the canvas:

.. code:: python

    import numpy
    import toyplot
.. code:: python

    y = numpy.linspace(0, 1, 20) ** 2
.. code:: python

    canvas, axes, mark = toyplot.plot(y, width=300)


.. raw:: html

    <div align="center" class="toyplot" id="t293854de31b548a3b8d9ac58bf7e0ea6"><svg height="300px" id="tb1d85276b2fa4c1c84b883b2253f8723" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="300px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="t9aa499515d8549769cfef8e8ccd0155c"><toyplot:axes>{"y": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 1.0, "min": 0.0}}], "x": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 20.0, "min": 0}}]}</toyplot:axes><clipPath id="t3ecfa2a95be142ca9332a32da201a7ed"><rect height="200" width="200" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t3ecfa2a95be142ca9332a32da201a7ed)" style="cursor:crosshair;"><rect height="200" style="pointer-events:all;visibility:hidden;" width="200" x="50" y="50"></rect><g class="toyplot-PlotMark" id="tab789e3dcc4f4fdda5b1f6a1dd1c1556" style="fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.501385042 L 78.0 238.005540166 L 87.0 235.512465374 L 96.0 232.022160665 L 105.0 227.534626039 L 114.0 222.049861496 L 123.0 215.567867036 L 132.0 208.088642659 L 141.0 199.612188366 L 150.0 190.138504155 L 159.0 179.667590028 L 168.0 168.199445983 L 177.0 155.734072022 L 186.0 142.271468144 L 195.0 127.811634349 L 204.0 112.354570637 L 213.0 95.9002770083 L 222.0 78.4487534626 L 231.0 60.0" style="stroke:rgba(40%,76.1%,64.7%,1);stroke-width:2.0;stroke-opacity:1.0;fill:none;"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="150" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250" y2="250"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="250">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="105.0" y="250">5</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="150.0" y="250">10</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="195.0" y="250">15</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="240.0" y="250">20</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">0.0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">0.5</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t293854de31b548a3b8d9ac58bf7e0ea6 text");
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
              var text = document.querySelectorAll("#t293854de31b548a3b8d9ac58bf7e0ea6 text");
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
          var root_id="t293854de31b548a3b8d9ac58bf7e0ea6";
    
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
          var root_id="t293854de31b548a3b8d9ac58bf7e0ea6";
    
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
canvas, or want to add multiple axes to one canvas, it is easier to
create the canvas and axes explicitly, then use the axes to plot your
data:

.. code:: python

    canvas = toyplot.Canvas(width=300)
    axes = canvas.axes()
    mark = axes.plot(y)


.. raw:: html

    <div align="center" class="toyplot" id="t405a2cef0fd447f8a34ab1823f5556d3"><svg height="300px" id="t2eae2e98a0e24e25b36f4c6e3278cff8" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="300px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="t8b2dfb284af4400bb87132bcb617daf9"><toyplot:axes>{"y": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 1.0, "min": 0.0}}], "x": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 20.0, "min": 0}}]}</toyplot:axes><clipPath id="t9e9f7c014a6a4190a57d4afae15bbecf"><rect height="200" width="200" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9e9f7c014a6a4190a57d4afae15bbecf)" style="cursor:crosshair;"><rect height="200" style="pointer-events:all;visibility:hidden;" width="200" x="50" y="50"></rect><g class="toyplot-PlotMark" id="t7244e03f3f98428584cc30b53aa3b33e" style="fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.501385042 L 78.0 238.005540166 L 87.0 235.512465374 L 96.0 232.022160665 L 105.0 227.534626039 L 114.0 222.049861496 L 123.0 215.567867036 L 132.0 208.088642659 L 141.0 199.612188366 L 150.0 190.138504155 L 159.0 179.667590028 L 168.0 168.199445983 L 177.0 155.734072022 L 186.0 142.271468144 L 195.0 127.811634349 L 204.0 112.354570637 L 213.0 95.9002770083 L 222.0 78.4487534626 L 231.0 60.0" style="stroke:rgba(40%,76.1%,64.7%,1);stroke-width:2.0;stroke-opacity:1.0;fill:none;"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="150" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250" y2="250"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="250">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="105.0" y="250">5</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="150.0" y="250">10</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="195.0" y="250">15</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="240.0" y="250">20</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">0.0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">0.5</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t405a2cef0fd447f8a34ab1823f5556d3 text");
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
              var text = document.querySelectorAll("#t405a2cef0fd447f8a34ab1823f5556d3 text");
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
          var root_id="t405a2cef0fd447f8a34ab1823f5556d3";
    
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
          var root_id="t405a2cef0fd447f8a34ab1823f5556d3";
    
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


In this case the axes still default to filling the entire canvas.

The axes object contains a set of nested properties that can be used to
adjust the behavior of the axes. For example, to enable tick marks for
the axes:

.. code:: python

    canvas = toyplot.Canvas(width=300)
    axes = canvas.axes()
    axes.x.ticks.show = True
    axes.y.ticks.show = True
    mark = axes.plot(y)


.. raw:: html

    <div align="center" class="toyplot" id="t8ae58b009248429db1dcc865d401b683"><svg height="300px" id="t500ba304b3e8481989a06d1d2acda991" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="300px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="tece727d2ab6b4d09a8b45f359a55077a"><toyplot:axes>{"y": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 1.0, "min": 0.0}}], "x": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 20.0, "min": 0}}]}</toyplot:axes><clipPath id="t70a577ceb80c4e62ac3e6b23ee0d6586"><rect height="200" width="200" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t70a577ceb80c4e62ac3e6b23ee0d6586)" style="cursor:crosshair;"><rect height="200" style="pointer-events:all;visibility:hidden;" width="200" x="50" y="50"></rect><g class="toyplot-PlotMark" id="td06d9a6c68414714aa2bd22e9d41c1ac" style="fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.501385042 L 78.0 238.005540166 L 87.0 235.512465374 L 96.0 232.022160665 L 105.0 227.534626039 L 114.0 222.049861496 L 123.0 215.567867036 L 132.0 208.088642659 L 141.0 199.612188366 L 150.0 190.138504155 L 159.0 179.667590028 L 168.0 168.199445983 L 177.0 155.734072022 L 186.0 142.271468144 L 195.0 127.811634349 L 204.0 112.354570637 L 213.0 95.9002770083 L 222.0 78.4487534626 L 231.0 60.0" style="stroke:rgba(40%,76.1%,64.7%,1);stroke-width:2.0;stroke-opacity:1.0;fill:none;"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="150" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250" y2="250"></line><g><line style="" x1="60.0" x2="60.0" y1="250" y2="245"></line><line style="" x1="105.0" x2="105.0" y1="250" y2="245"></line><line style="" x1="150.0" x2="150.0" y1="250" y2="245"></line><line style="" x1="195.0" x2="195.0" y1="250" y2="245"></line><line style="" x1="240.0" x2="240.0" y1="250" y2="245"></line></g><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="250">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="105.0" y="250">5</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="150.0" y="250">10</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="195.0" y="250">15</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="240.0" y="250">20</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><line style="" x1="50" x2="55" y1="240.0" y2="240.0"></line><line style="" x1="50" x2="55" y1="150.0" y2="150.0"></line><line style="" x1="50" x2="55" y1="60.0" y2="60.0"></line></g><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">0.0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">0.5</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t8ae58b009248429db1dcc865d401b683 text");
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
              var text = document.querySelectorAll("#t8ae58b009248429db1dcc865d401b683 text");
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
          var root_id="t8ae58b009248429db1dcc865d401b683";
    
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
          var root_id="t8ae58b009248429db1dcc865d401b683";
    
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

