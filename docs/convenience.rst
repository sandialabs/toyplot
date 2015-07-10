
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _convenience:

Convenience
===========

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

    <div align="center" class="toyplot" id="t572ba9a8466c493080b509cb203efbf2"><svg height="300.0px" id="t65e76f814cf54a65b59eec53f4dd8ee4" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t4c1fe22b4eef42a3b99d07b70c3831e3"><clipPath id="td2e988316f2d4758bd743d7431fd6c79"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td2e988316f2d4758bd743d7431fd6c79)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t0490652edb074fc4ae1cd46c52a6fc45" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t572ba9a8466c493080b509cb203efbf2 text");
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
          var text = document.querySelectorAll("#t572ba9a8466c493080b509cb203efbf2 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t0490652edb074fc4ae1cd46c52a6fc45", "title": "Plot Data"}];
    
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
          link.download = "toyplot.csv";
    
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
          var popup = document.querySelector("#t572ba9a8466c493080b509cb203efbf2 .toyplot-mark-popup");
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
      var axes = {"t4c1fe22b4eef42a3b99d07b70c3831e3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Using the convenience API, it can be reduced to a single call to
:py:func:`toyplot.plot`:

.. code:: python

    canvas, axes, mark = toyplot.plot(y, width=300)



.. raw:: html

    <div align="center" class="toyplot" id="tc037964aac3b4bd5b6762e9813c27d3b"><svg height="300.0px" id="t1a72f40aa7bc43028653eecdcdd8daae" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t628f19313d714e8ab5bbe10282773c6f"><clipPath id="t2c3b08e39abc405c9c99ea129bdadc3b"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2c3b08e39abc405c9c99ea129bdadc3b)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t0b32541228cd43568fc515999d45eff0" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tc037964aac3b4bd5b6762e9813c27d3b text");
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
          var text = document.querySelectorAll("#tc037964aac3b4bd5b6762e9813c27d3b text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "t0b32541228cd43568fc515999d45eff0", "title": "Plot Data"}];
    
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
          link.download = "toyplot.csv";
    
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
          var popup = document.querySelector("#tc037964aac3b4bd5b6762e9813c27d3b .toyplot-mark-popup");
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
      var axes = {"t628f19313d714e8ab5bbe10282773c6f": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Of course, if you're using the convenience API there's a good chance you
don't need the function's return value (a (canvas, axes, mark) tuple) at
all, making it even more compact:

.. code:: python

    toyplot.plot(y, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t0c91ad30475e4c04bd75a19336ac0c0a"><svg height="300.0px" id="tf831d29c3e424ae089773f138bfdbcb3" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t2be49b6da2c144d382acedabcc149dd8"><clipPath id="t1ab4ffa845b446f3875c600350788f75"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t1ab4ffa845b446f3875c600350788f75)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="te87c8c35701d44089308f65174ce4c6c" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t0c91ad30475e4c04bd75a19336ac0c0a text");
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
          var text = document.querySelectorAll("#t0c91ad30475e4c04bd75a19336ac0c0a text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["x", "y0"], "id": "te87c8c35701d44089308f65174ce4c6c", "title": "Plot Data"}];
    
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
          link.download = "toyplot.csv";
    
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
          var popup = document.querySelector("#t0c91ad30475e4c04bd75a19336ac0c0a .toyplot-mark-popup");
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
      var axes = {"t2be49b6da2c144d382acedabcc149dd8": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t249177288cd242bdb6b2b7b04cb2f0c7"><svg height="300.0px" id="t88e620c0a349457089def3cd4d060534" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t731ffe416a2743f7bf9039fc38500d26"><clipPath id="tf985e1a825684402bc843806ed2da766"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf985e1a825684402bc843806ed2da766)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-BarMagnitudes" id="t82fb9984c7f6473e9d1606b10b814280" style="stroke:white;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="0.0" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="60.0" y="240.0"></rect><rect class="toyplot-Datum" height="0.49861495844874071" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="68.780487804878049" y="239.50138504155126"></rect><rect class="toyplot-Datum" height="1.9944598337949913" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="77.560975609756099" y="238.00554016620501"></rect><rect class="toyplot-Datum" height="4.4875346260387801" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="86.341463414634148" y="235.51246537396122"></rect><rect class="toyplot-Datum" height="7.9778393351800787" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="95.121951219512198" y="232.02216066481992"></rect><rect class="toyplot-Datum" height="12.46537396121883" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780353" x="103.90243902439025" y="227.53462603878117"></rect><rect class="toyplot-Datum" height="17.95013850415512" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780637" x="112.68292682926828" y="222.04986149584488"></rect><rect class="toyplot-Datum" height="24.432132963988948" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="121.46341463414635" y="215.56786703601105"></rect><rect class="toyplot-Datum" height="31.911357340720201" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="130.2439024390244" y="208.0886426592798"></rect><rect class="toyplot-Datum" height="40.387811634349021" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="139.02439024390245" y="199.61218836565098"></rect><rect class="toyplot-Datum" height="49.86149584487535" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="147.80487804878049" y="190.13850415512465"></rect><rect class="toyplot-Datum" height="60.332409972299189" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780211" x="156.58536585365854" y="179.66759002770081"></rect><rect class="toyplot-Datum" height="71.800554016620481" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="165.36585365853657" y="168.19944598337952"></rect><rect class="toyplot-Datum" height="84.265927977839311" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780779" x="174.14634146341461" y="155.73407202216069"></rect><rect class="toyplot-Datum" height="97.728531855955652" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780211" x="182.92682926829269" y="142.27146814404435"></rect><rect class="toyplot-Datum" height="112.18836565096953" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="191.70731707317071" y="127.81163434903047"></rect><rect class="toyplot-Datum" height="127.64542936288086" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="200.48780487804876" y="112.35457063711914"></rect><rect class="toyplot-Datum" height="144.0997229916897" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="209.26829268292681" y="95.900277008310283"></rect><rect class="toyplot-Datum" height="161.55124653739608" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="218.04878048780486" y="78.448753462603904"></rect><rect class="toyplot-Datum" height="180.0" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:white;stroke-width:1.0" width="8.7804878048780495" x="226.82926829268291" y="60.0"></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="235.60975609756096" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="64.39024390243902" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="152.1951219512195" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t249177288cd242bdb6b2b7b04cb2f0c7 text");
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
          var text = document.querySelectorAll("#t249177288cd242bdb6b2b7b04cb2f0c7 text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["left", "right", "baseline", "magnitude0"], "id": "t82fb9984c7f6473e9d1606b10b814280", "title": "Bar Data"}];
    
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
          link.download = "toyplot.csv";
    
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
          var popup = document.querySelector("#t249177288cd242bdb6b2b7b04cb2f0c7 .toyplot-mark-popup");
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
      var axes = {"t731ffe416a2743f7bf9039fc38500d26": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


.. code:: python

    toyplot.fill(numpy.column_stack((y, y*2)), width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t372d82e7477540319e8517792238298f"><svg height="300.0px" id="tc051145e1fdc497bbfcd802838220a5c" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tde0002335f034f73ad36aaea473e5dc2"><clipPath id="tffccb77b547343f287b6b08913f03abe"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tffccb77b547343f287b6b08913f03abe)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-FillBoundaries" id="tef30a9cfdabf4103b3bdeac027a62a0a" style="stroke:none"><polygon points="60.0,240.0 69.0,239.75069252077563 78.0,239.00277008310249 87.0,237.75623268698061 96.0,236.01108033240996 105.0,233.76731301939057 114.0,231.02493074792247 123.0,227.78393351800554 132.0,224.04432132963987 141.0,219.80609418282549 150.0,215.06925207756231 159.0,209.83379501385039 168.0,204.09972299168976 177.0,197.86703601108036 186.0,191.13573407202219 195.0,183.90581717451522 204.0,176.17728531855957 213.0,167.95013850415515 222.0,159.22437673130196 231.0,150.0 231.0,60.0 222.0,78.448753462603904 213.0,95.900277008310283 204.0,112.35457063711914 195.0,127.81163434903047 186.0,142.27146814404435 177.0,155.73407202216069 168.0,168.19944598337952 159.0,179.66759002770081 150.0,190.13850415512465 141.0,199.61218836565098 132.0,208.0886426592798 123.0,215.56786703601105 114.0,222.04986149584488 105.0,227.53462603878117 96.0,232.02216066481992 87.0,235.51246537396122 78.0,238.00554016620501 69.0,239.50138504155126 60.0,240.0" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:none"></polygon></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">1.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">1.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">2.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t372d82e7477540319e8517792238298f text");
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
          var text = document.querySelectorAll("#t372d82e7477540319e8517792238298f text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], [0.0, 0.005540166204986149, 0.022160664819944595, 0.04986149584487534, 0.08864265927977838, 0.13850415512465372, 0.19944598337950137, 0.2714681440443213, 0.3545706371191135, 0.44875346260387805, 0.5540166204986149, 0.6703601108033241, 0.7977839335180055, 0.936288088642659, 1.0858725761772852, 1.2465373961218837, 1.418282548476454, 1.6011080332409968, 1.7950138504155122, 2.0]], "names": ["x", "y0", "y1"], "id": "tef30a9cfdabf4103b3bdeac027a62a0a", "title": "Fill Data"}];
    
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
          link.download = "toyplot.csv";
    
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
          var popup = document.querySelector("#t372d82e7477540319e8517792238298f .toyplot-mark-popup");
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
      var axes = {"tde0002335f034f73ad36aaea473e5dc2": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


.. code:: python

    numpy.random.seed(1234)
    toyplot.scatterplot(numpy.random.normal(size=50), width=300);



.. raw:: html

    <div align="center" class="toyplot" id="tf9befea56d6d487181828d098e23dd13"><svg height="300.0px" id="t0bb46ea1e4534c4d9341d866815f2a22" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tf6b1a8b2face48278b726ceb22ea5db8"><clipPath id="t7563f4d9434946b6bc095352ba7e0984"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t7563f4d9434946b6bc095352ba7e0984)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t41ee1d44cf1c41b198449868103a6bc0" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="134.56646512442651" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="63.599999999999994" cy="199.14498250972738" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="67.199999999999989" cy="97.224608485149204" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="70.799999999999997" cy="165.02534932107727" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="74.400000000000006" cy="180.87218766686138" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.0" cy="118.41697758298504" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="81.599999999999994" cy="119.48814602234226" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="85.200000000000003" cy="177.60656423716739" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="88.799999999999997" cy="152.27023271488821" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="92.400000000000006" cy="240.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="96.0" cy="108.20534151714588" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="99.599999999999994" cy="114.3465421364596" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="103.19999999999999" cy="115.84685997626447" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="106.80000000000001" cy="231.39825772615652" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="110.40000000000001" cy="165.85764962851567" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="114.0" cy="152.79768811767605" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="117.59999999999999" cy="137.12961231965539" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="121.2" cy="141.6498253664721" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="124.79999999999998" cy="101.55786614694689" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="128.40000000000001" cy="212.97154195493252" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="132.0" cy="160.75203946322188" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="135.59999999999999" cy="178.361963236252" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="139.19999999999999" cy="145.36627318807214" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="142.80000000000001" cy="131.38092264020952" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="146.39999999999998" cy="101.67466291838952" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="150.0" cy="171.11075445948399" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="153.60000000000002" cy="126.63719947584696" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="157.20000000000002" cy="223.46477056369383" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="160.80000000000001" cy="159.9930687512697" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="164.39999999999998" cy="111.74293989279454" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="168.0" cy="168.33460115744043" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="171.60000000000002" cy="139.7717731220545" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="175.19999999999999" cy="112.18542317200682" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="178.80000000000001" cy="112.24914343494973" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="182.40000000000001" cy="119.327754374124" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.0" cy="157.62278517399122" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="189.59999999999999" cy="148.03534145568045" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="193.19999999999999" cy="165.41936386641609" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="196.80000000000001" cy="120.18402708422984" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="200.40000000000001" cy="60.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="204.0" cy="149.91990641102194" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="207.59999999999999" cy="174.88430950403011" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="211.19999999999999" cy="151.47599810055652" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="214.80000000000001" cy="233.4851891827067" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="218.39999999999998" cy="143.25416766463934" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="222.0" cy="187.73120383493585" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="225.60000000000002" cy="158.19395241839894" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="229.19999999999999" cy="152.16951127097985" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="232.79999999999998" cy="123.53493763820866" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="236.39999999999998" cy="144.51759004310688" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="236.39999999999998" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="96.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="132.0" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="168.0" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="204.0" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 230.5725865218844)" x="50.0" y="230.5725865218844">-2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 152.87997875590574)" x="50.0" y="152.87997875590574">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 75.18737098992716)" x="50.0" y="75.18737098992716">2</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tf9befea56d6d487181828d098e23dd13 text");
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
          var text = document.querySelectorAll("#tf9befea56d6d487181828d098e23dd13 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.47143516373249306, -1.1909756947064645, 1.4327069684260973, -0.3126518960917129, -0.7205887333650116, 0.8871629403077386, 0.8595884137174165, -0.6365235044173491, 0.015696372114428918, -2.2426849541854055, 1.150035724719818, 0.9919460223426778, 0.9533241281124304, -2.0212548201949705, -0.334077365808097, 0.002118364683486495, 0.405453411570191, 0.2890919409800353, 1.3211581921293856, -1.5469055532292402, -0.2026463246291819, -0.6559693441389339, 0.19342137647035826, 0.5534389109567419, 1.3181515541801367, -0.4693052847058996, 0.6755540851223808, -1.8170272265901968, -0.1831085401789987, 1.0589691875711504, -0.3978402281999914, 0.3374376536139724, 1.0475785728927218, 1.0459382556276653, 0.8637172916848387, -0.12209157484767426, 0.12471295376821585, -0.32279480560829565, 0.8416747129961416, 2.390960515463033, 0.07619958783723642, -0.5664459304649568, 0.036141936684072715, -2.0749776006900293, 0.24779219974854666, -0.8971567844396987, -0.1367948332613474, 0.018289191349219306, 0.7554139823981354, 0.2152685809694434]], "names": ["x", "y0"], "id": "t41ee1d44cf1c41b198449868103a6bc0", "title": "Plot Data"}];
    
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
          link.download = "toyplot.csv";
    
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
          var popup = document.querySelector("#tf9befea56d6d487181828d098e23dd13 .toyplot-mark-popup");
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
      var axes = {"tf6b1a8b2face48278b726ceb22ea5db8": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.3909605154630329, "min": -2.2426849541854055}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


.. code:: python

    toyplot.matrix(numpy.random.normal(size=(10, 10)), width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t9f21107886c54c9ebaa504b4c6ed77ae"><svg height="300.0px" id="tbc413880251b4cf5b424e59c536800d2" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Table" id="t80584f2fa04b4691a3106f8ac81647cd"><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="79.0" y="60.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="97.0" y="60.0">1</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="115.0" y="60.0">2</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="133.0" y="60.0">3</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="151.0" y="60.0">4</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="169.0" y="60.0">5</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="187.0" y="60.0">6</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="205.0" y="60.0">7</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="223.0" y="60.0">8</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="241.0" y="60.0">9</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" x="65.0" y="79.0">0</text><rect height="18.0" style="fill:rgba(90.6%,53.1%,42.1%,1);stroke:none" width="18.0" x="70.0" y="70.0"><title>0.841008794931</title></rect><rect height="18.0" style="fill:rgba(71.4%,84.4%,91.1%,1);stroke:none" width="18.0" x="88.0" y="70.0"><title>-1.44581007704</title></rect><rect height="18.0" style="fill:rgba(73.2%,85.4%,91.6%,1);stroke:none" width="18.0" x="106.0" y="70.0"><title>-1.4019732815</title></rect><rect height="18.0" style="fill:rgba(98.8%,87.6%,81.1%,1);stroke:none" width="18.0" x="124.0" y="70.0"><title>-0.100918199949</title></rect><rect height="18.0" style="fill:rgba(97.1%,95.9%,95.3%,1);stroke:none" width="18.0" x="142.0" y="70.0"><title>-0.548242449187</title></rect><rect height="18.0" style="fill:rgba(98.7%,88.5%,82.4%,1);stroke:none" width="18.0" x="160.0" y="70.0"><title>-0.144619508369</title></rect><rect height="18.0" style="fill:rgba(97.1%,73%,61.6%,1);stroke:none" width="18.0" x="178.0" y="70.0"><title>0.354020332199</title></rect><rect height="18.0" style="fill:rgba(99.1%,86.4%,79%,1);stroke:none" width="18.0" x="196.0" y="70.0"><title>-0.0355130252781</title></rect><rect height="18.0" style="fill:rgba(95.8%,65.5%,51.9%,1);stroke:none" width="18.0" x="214.0" y="70.0"><title>0.565738306063</title></rect><rect height="18.0" style="fill:rgba(75.2%,20.2%,22%,1);stroke:none" width="18.0" x="232.0" y="70.0"><title>1.54565880463</title></rect><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" x="65.0" y="97.0">1</text><rect height="18.0" style="fill:rgba(87.4%,92.4%,95.1%,1);stroke:none" width="18.0" x="70.0" y="88.0"><title>-0.974236333767</title></rect><rect height="18.0" style="fill:rgba(99%,87.1%,80.1%,1);stroke:none" width="18.0" x="88.0" y="88.0"><title>-0.0703448771041</title></rect><rect height="18.0" style="fill:rgba(97.3%,74.7%,63.7%,1);stroke:none" width="18.0" x="106.0" y="88.0"><title>0.307968855216</title></rect><rect height="18.0" style="fill:rgba(98.4%,89.6%,84.5%,1);stroke:none" width="18.0" x="124.0" y="88.0"><title>-0.208498763106</title></rect><rect height="18.0" style="fill:rgba(86.8%,44.3%,35.3%,1);stroke:none" width="18.0" x="142.0" y="88.0"><title>1.03380073256</title></rect><rect height="18.0" style="fill:rgba(25.8%,57%,76.1%,1);stroke:none" width="18.0" x="160.0" y="88.0"><title>-2.40045363381</title></rect><rect height="18.0" style="fill:rgba(57%,5.32%,14.8%,1);stroke:none" width="18.0" x="178.0" y="88.0"><title>2.03060362084</title></rect><rect height="18.0" style="fill:rgba(83.2%,90.4%,94.3%,1);stroke:none" width="18.0" x="196.0" y="88.0"><title>-1.14263128902</title></rect><rect height="18.0" style="fill:rgba(97.9%,78.1%,68.1%,1);stroke:none" width="18.0" x="214.0" y="88.0"><title>0.211883386778</title></rect><rect height="18.0" style="fill:rgba(93.4%,59.3%,46.9%,1);stroke:none" width="18.0" x="232.0" y="88.0"><title>0.704720624317</title></rect><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" x="65.0" y="115.0">2</text><rect height="18.0" style="fill:rgba(92.2%,94.6%,96%,1);stroke:none" width="18.0" x="70.0" y="106.0"><title>-0.785435211763</title></rect><rect height="18.0" style="fill:rgba(96.4%,69.2%,56.7%,1);stroke:none" width="18.0" x="88.0" y="106.0"><title>0.462059737162</title></rect><rect height="18.0" style="fill:rgba(93.4%,59.4%,46.9%,1);stroke:none" width="18.0" x="106.0" y="106.0"><title>0.704228225462</title></rect><rect height="18.0" style="fill:rgba(96.1%,67%,53.9%,1);stroke:none" width="18.0" x="124.0" y="106.0"><title>0.523507967894</title></rect><rect height="18.0" style="fill:rgba(88.6%,93%,95.3%,1);stroke:none" width="18.0" x="142.0" y="106.0"><title>-0.92625431353</title></rect><rect height="18.0" style="fill:rgba(58.1%,5.68%,15%,1);stroke:none" width="18.0" x="160.0" y="106.0"><title>2.00784295078</title></rect><rect height="18.0" style="fill:rgba(97.8%,77.6%,67.4%,1);stroke:none" width="18.0" x="178.0" y="106.0"><title>0.226962541871</title></rect><rect height="18.0" style="fill:rgba(82.9%,90.3%,94.3%,1);stroke:none" width="18.0" x="196.0" y="106.0"><title>-1.15265910925</title></rect><rect height="18.0" style="fill:rgba(94.8%,62.7%,49.4%,1);stroke:none" width="18.0" x="214.0" y="106.0"><title>0.631979445809</title></rect><rect height="18.0" style="fill:rgba(98.9%,84.3%,76%,1);stroke:none" width="18.0" x="232.0" y="106.0"><title>0.0395126866934</title></rect><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" x="65.0" y="133.0">3</text><rect height="18.0" style="fill:rgba(96.4%,69.1%,56.6%,1);stroke:none" width="18.0" x="70.0" y="124.0"><title>0.464392325051</title></rect><rect height="18.0" style="fill:rgba(1.96%,18.8%,38%,1);stroke:none" width="18.0" x="88.0" y="124.0"><title>-3.56351666062</title></rect><rect height="18.0" style="fill:rgba(80.6%,30.9%,27%,1);stroke:none" width="18.0" x="106.0" y="124.0"><title>1.32110561547</title></rect><rect height="18.0" style="fill:rgba(98.3%,80.2%,70.8%,1);stroke:none" width="18.0" x="124.0" y="124.0"><title>0.152630552205</title></rect><rect height="18.0" style="fill:rgba(98.2%,79.8%,70.3%,1);stroke:none" width="18.0" x="142.0" y="124.0"><title>0.164529542932</title></rect><rect height="18.0" style="fill:rgba(97.5%,93.7%,91.5%,1);stroke:none" width="18.0" x="160.0" y="124.0"><title>-0.430095690876</title></rect><rect height="18.0" style="fill:rgba(92.1%,56.5%,44.7%,1);stroke:none" width="18.0" x="178.0" y="124.0"><title>0.767368735752</title></rect><rect height="18.0" style="fill:rgba(87.8%,46.5%,37%,1);stroke:none" width="18.0" x="196.0" y="124.0"><title>0.98491984191</title></rect><rect height="18.0" style="fill:rgba(97.6%,76%,65.4%,1);stroke:none" width="18.0" x="214.0" y="124.0"><title>0.270835848827</title></rect><rect height="18.0" style="fill:rgba(78.9%,27.5%,25.4%,1);stroke:none" width="18.0" x="232.0" y="124.0"><title>1.39198619345</title></rect><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" x="65.0" y="151.0">4</text><rect height="18.0" style="fill:rgba(98.7%,82.8%,74.1%,1);stroke:none" width="18.0" x="70.0" y="142.0"><title>0.0798423130086</title></rect><rect height="18.0" style="fill:rgba(97.7%,93.2%,90.5%,1);stroke:none" width="18.0" x="88.0" y="142.0"><title>-0.399964580697</title></rect><rect height="18.0" style="fill:rgba(86.1%,91.8%,94.9%,1);stroke:none" width="18.0" x="106.0" y="142.0"><title>-1.02785055868</title></rect><rect height="18.0" style="fill:rgba(96.9%,96.6%,96.4%,1);stroke:none" width="18.0" x="124.0" y="142.0"><title>-0.584718211261</title></rect><rect height="18.0" style="fill:rgba(91.1%,54.2%,42.9%,1);stroke:none" width="18.0" x="142.0" y="142.0"><title>0.816593926548</title></rect><rect height="18.0" style="fill:rgba(98.9%,87.3%,80.5%,1);stroke:none" width="18.0" x="160.0" y="142.0"><title>-0.0819470518267</title></rect><rect height="18.0" style="fill:rgba(97.9%,92.2%,88.8%,1);stroke:none" width="18.0" x="178.0" y="142.0"><title>-0.344766014255</title></rect><rect height="18.0" style="fill:rgba(96%,66.8%,53.7%,1);stroke:none" width="18.0" x="196.0" y="142.0"><title>0.528288145297</title></rect><rect height="18.0" style="fill:rgba(85%,91.3%,94.7%,1);stroke:none" width="18.0" x="214.0" y="142.0"><title>-1.06898878348</title></rect><rect height="18.0" style="fill:rgba(97.2%,95.3%,94.1%,1);stroke:none" width="18.0" x="232.0" y="142.0"><title>-0.511881309127</title></rect><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" x="65.0" y="169.0">5</text><rect height="18.0" style="fill:rgba(97.4%,75.3%,64.5%,1);stroke:none" width="18.0" x="70.0" y="160.0"><title>0.291205359743</title></rect><rect height="18.0" style="fill:rgba(95.8%,65.4%,51.9%,1);stroke:none" width="18.0" x="88.0" y="160.0"><title>0.566533696354</title></rect><rect height="18.0" style="fill:rgba(96.2%,67.7%,54.8%,1);stroke:none" width="18.0" x="106.0" y="160.0"><title>0.503591759111</title></rect><rect height="18.0" style="fill:rgba(97.5%,75.5%,64.7%,1);stroke:none" width="18.0" x="124.0" y="160.0"><title>0.285295684782</title></rect><rect height="18.0" style="fill:rgba(96.3%,68.4%,55.7%,1);stroke:none" width="18.0" x="142.0" y="160.0"><title>0.48428811275</title></rect><rect height="18.0" style="fill:rgba(79.6%,28.9%,26.1%,1);stroke:none" width="18.0" x="160.0" y="160.0"><title>1.36348151243</title></rect><rect height="18.0" style="fill:rgba(92.3%,94.7%,96%,1);stroke:none" width="18.0" x="178.0" y="160.0"><title>-0.781105283625</title></rect><rect height="18.0" style="fill:rgba(97.4%,94.4%,92.7%,1);stroke:none" width="18.0" x="196.0" y="160.0"><title>-0.468017666337</title></rect><rect height="18.0" style="fill:rgba(82.9%,35.5%,29.2%,1);stroke:none" width="18.0" x="214.0" y="160.0"><title>1.22457435513</title></rect><rect height="18.0" style="fill:rgba(78.2%,87.9%,93.1%,1);stroke:none" width="18.0" x="232.0" y="160.0"><title>-1.28110827514</title></rect><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" x="65.0" y="187.0">6</text><rect height="18.0" style="fill:rgba(90%,51.5%,40.9%,1);stroke:none" width="18.0" x="70.0" y="178.0"><title>0.875475504274</title></rect><rect height="18.0" style="fill:rgba(60.3%,78.8%,87.9%,1);stroke:none" width="18.0" x="88.0" y="178.0"><title>-1.71071532403</title></rect><rect height="18.0" style="fill:rgba(97.5%,94.1%,92.2%,1);stroke:none" width="18.0" x="106.0" y="178.0"><title>-0.450765103136</title></rect><rect height="18.0" style="fill:rgba(92.5%,57.3%,45.3%,1);stroke:none" width="18.0" x="124.0" y="178.0"><title>0.749163805919</title></rect><rect height="18.0" style="fill:rgba(98.4%,89.5%,84.3%,1);stroke:none" width="18.0" x="142.0" y="178.0"><title>-0.203932866101</title></rect><rect height="18.0" style="fill:rgba(98.5%,89.1%,83.6%,1);stroke:none" width="18.0" x="160.0" y="178.0"><title>-0.182175411666</title></rect><rect height="18.0" style="fill:rgba(93.8%,60.4%,47.7%,1);stroke:none" width="18.0" x="178.0" y="178.0"><title>0.680656004381</title></rect><rect height="18.0" style="fill:rgba(55.5%,76.1%,86.5%,1);stroke:none" width="18.0" x="196.0" y="178.0"><title>-1.81849899039</title></rect><rect height="18.0" style="fill:rgba(98.9%,84%,75.6%,1);stroke:none" width="18.0" x="214.0" y="178.0"><title>0.0470716353257</title></rect><rect height="18.0" style="fill:rgba(96.8%,71.6%,59.7%,1);stroke:none" width="18.0" x="232.0" y="178.0"><title>0.394844209327</title></rect><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" x="65.0" y="205.0">7</text><rect height="18.0" style="fill:rgba(98.3%,90.4%,85.7%,1);stroke:none" width="18.0" x="70.0" y="196.0"><title>-0.248432054381</title></rect><rect height="18.0" style="fill:rgba(96.4%,96.6%,96.8%,1);stroke:none" width="18.0" x="88.0" y="196.0"><title>-0.617706647997</title></rect><rect height="18.0" style="fill:rgba(94.8%,95.9%,96.5%,1);stroke:none" width="18.0" x="106.0" y="196.0"><title>-0.682883996449</title></rect><rect height="18.0" style="fill:rgba(96.6%,70.1%,57.9%,1);stroke:none" width="18.0" x="124.0" y="196.0"><title>0.436257604341</title></rect><rect height="18.0" style="fill:rgba(60.7%,79%,88%,1);stroke:none" width="18.0" x="142.0" y="196.0"><title>-1.70301277411</title></rect><rect height="18.0" style="fill:rgba(96.8%,71.6%,59.8%,1);stroke:none" width="18.0" x="160.0" y="196.0"><title>0.393710599139</title></rect><rect height="18.0" style="fill:rgba(97.3%,94.6%,93.1%,1);stroke:none" width="18.0" x="178.0" y="196.0"><title>-0.479324003575</title></rect><rect height="18.0" style="fill:rgba(98.1%,91.3%,87.3%,1);stroke:none" width="18.0" x="196.0" y="196.0"><title>-0.299016292966</title></rect><rect height="18.0" style="fill:rgba(93.6%,59.8%,47.2%,1);stroke:none" width="18.0" x="214.0" y="196.0"><title>0.694103287679</title></rect><rect height="18.0" style="fill:rgba(93.9%,60.5%,47.8%,1);stroke:none" width="18.0" x="232.0" y="196.0"><title>0.67862967371</title></rect><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" x="65.0" y="223.0">8</text><rect height="18.0" style="fill:rgba(97.8%,77.1%,66.8%,1);stroke:none" width="18.0" x="70.0" y="214.0"><title>0.239555995004</title></rect><rect height="18.0" style="fill:rgba(98.3%,80.3%,70.9%,1);stroke:none" width="18.0" x="88.0" y="214.0"><title>0.151226629294</title></rect><rect height="18.0" style="fill:rgba(91.1%,54.2%,42.9%,1);stroke:none" width="18.0" x="106.0" y="214.0"><title>0.81612723336</title></rect><rect height="18.0" style="fill:rgba(63.8%,7.5%,15.9%,1);stroke:none" width="18.0" x="124.0" y="214.0"><title>1.8935344676</title></rect><rect height="18.0" style="fill:rgba(94.6%,62.3%,49.1%,1);stroke:none" width="18.0" x="142.0" y="214.0"><title>0.639632763194</title></rect><rect height="18.0" style="fill:rgba(87.7%,92.5%,95.2%,1);stroke:none" width="18.0" x="160.0" y="214.0"><title>-0.962028831905</title></rect><rect height="18.0" style="fill:rgba(41.6%,67.3%,81.7%,1);stroke:none" width="18.0" x="178.0" y="214.0"><title>-2.08526564212</title></rect><rect height="18.0" style="fill:rgba(62%,6.91%,15.6%,1);stroke:none" width="18.0" x="196.0" y="214.0"><title>1.93024676747</title></rect><rect height="18.0" style="fill:rgba(59.3%,78.3%,87.6%,1);stroke:none" width="18.0" x="214.0" y="214.0"><title>-1.73534887447</title></rect><rect height="18.0" style="fill:rgba(83.2%,36.2%,29.5%,1);stroke:none" width="18.0" x="232.0" y="214.0"><title>1.2103837049</title></rect><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:end" x="65.0" y="241.0">9</text><rect height="18.0" style="fill:rgba(91.5%,55.1%,43.6%,1);stroke:none" width="18.0" x="70.0" y="232.0"><title>0.797435419428</title></rect><rect height="18.0" style="fill:rgba(97.7%,92.8%,89.9%,1);stroke:none" width="18.0" x="88.0" y="232.0"><title>-0.379810784047</title></rect><rect height="18.0" style="fill:rgba(93.4%,59.4%,46.9%,1);stroke:none" width="18.0" x="106.0" y="232.0"><title>0.702562224002</title></rect><rect height="18.0" style="fill:rgba(90.5%,93.9%,95.7%,1);stroke:none" width="18.0" x="124.0" y="232.0"><title>-0.850346271655</title></rect><rect height="18.0" style="fill:rgba(84%,37.8%,30.3%,1);stroke:none" width="18.0" x="142.0" y="232.0"><title>1.1768124501</title></rect><rect height="18.0" style="fill:rgba(97.2%,95.5%,94.5%,1);stroke:none" width="18.0" x="160.0" y="232.0"><title>-0.524336102632</title></rect><rect height="18.0" style="fill:rgba(93.4%,59.5%,47%,1);stroke:none" width="18.0" x="178.0" y="232.0"><title>0.700907730916</title></rect><rect height="18.0" style="fill:rgba(87.8%,46.6%,37.1%,1);stroke:none" width="18.0" x="196.0" y="232.0"><title>0.984188070722</title></rect><rect height="18.0" style="fill:rgba(98.8%,88%,81.7%,1);stroke:none" width="18.0" x="214.0" y="232.0"><title>-0.121728408667</title></rect><rect height="18.0" style="fill:rgba(40.4%,0%,12.2%,1);stroke:none" width="18.0" x="232.0" y="232.0"><title>2.36576862884</title></rect></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t9f21107886c54c9ebaa504b4c6ed77ae text");
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
          var text = document.querySelectorAll("#t9f21107886c54c9ebaa504b4c6ed77ae text");
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
    </script></div></div>


.. code:: python

    columns = ["Year", "MPG", "Model"]
    canvas, table = toyplot.table(toyplot.data.read_csv("cars.csv").columns(columns)[:10], width=300)
    table.column(2).width = 130



.. raw:: html

    <div align="center" class="toyplot" id="t41cfddbcaf094bd196d54563f2f367db"><svg height="300.0px" id="t1b44afcb90984c84906dda83493cd6f6" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Table" id="t559bd391bf5445da9621ab7ef500fa45"><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:begin" x="55.0" y="59.090909090909093">Year</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:begin" x="90.0" y="59.090909090909093">MPG</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:begin" x="125.0" y="59.090909090909093">Model</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="55.0" y="77.27272727272728">70.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="90.0" y="77.27272727272728">18.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="125.0" y="77.27272727272728">chevrolet chevelle malibu</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="55.0" y="95.454545454545467">70.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="90.0" y="95.454545454545467">15.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="125.0" y="95.454545454545467">buick skylark 320</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="55.0" y="113.63636363636365">70.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="90.0" y="113.63636363636365">18.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="125.0" y="113.63636363636365">plymouth satellite</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="55.0" y="131.81818181818184">70.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="90.0" y="131.81818181818184">16.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="125.0" y="131.81818181818184">amc rebel sst</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="55.0" y="150.00000000000003">70.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="90.0" y="150.00000000000003">17.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="125.0" y="150.00000000000003">ford torino</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="55.0" y="168.18181818181822">70.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="90.0" y="168.18181818181822">15.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="125.0" y="168.18181818181822">ford galaxie 500</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="55.0" y="186.3636363636364">70.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="90.0" y="186.3636363636364">14.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="125.0" y="186.3636363636364">chevrolet impala</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="55.0" y="204.54545454545459">70.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="90.0" y="204.54545454545459">14.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="125.0" y="204.54545454545459">plymouth fury iii</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="55.0" y="222.72727272727278">70.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="90.0" y="222.72727272727278">14.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="125.0" y="222.72727272727278">pontiac catalina</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="55.0" y="240.90909090909096">70.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="90.0" y="240.90909090909096">15.0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="125.0" y="240.90909090909096">amc ambassador dpl</text><line style="stroke:#292724;stroke-width:0.5" x1="50.0" x2="250.0" y1="68.181818181818187" y2="68.181818181818187"></line></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t41cfddbcaf094bd196d54563f2f367db text");
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
          var text = document.querySelectorAll("#t41cfddbcaf094bd196d54563f2f367db text");
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
    </script></div></div>


If you need greater control over the positioning of the axes within the
canvas, need to add multiple axes to one canvas, or need to add multiple
marks to one set of axes, you'll have to create the canvas and axes
explicitly.
