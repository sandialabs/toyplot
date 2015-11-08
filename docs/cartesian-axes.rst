
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _cartesian-axes:

Cartesian Axes
==============

In Toyplot, :class:`cartesian axes<toyplot.axes.Cartesian>` provide a
traditional mapping of two-dimensional data values on the plane to
canvas coordinates. The axes *range* (the area on the canvas that they
occupy) is specified when they are created (see :ref:`canvas-layout`).
Their *domain* is implicitly defined to include all of the data in the
plot (but can be manually overridden by the caller if desired).

Cartesian axes are either created for you implicitly when using the
:ref:`convenience-api`:

.. code:: python

    import numpy
    y = numpy.linspace(0, 1, 20) ** 2

.. code:: python

    import toyplot
    canvas, axes, mark = toyplot.plot(y, width=300)



.. raw:: html

    <div align="center" class="toyplot" id="t72634ab38d1349c891124b0eac0f254c"><svg height="300.0px" id="t73495d9dac034b34b9f9d390f8f9e735" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tbc4c3aae94b84ac6b136b09f936b35ca"><clipPath id="t37b9ec1a22c54be48ed3883470889f93"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t37b9ec1a22c54be48ed3883470889f93)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tce01551a8bd34522a932f26ff2145009" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t46c211c7590d467297fdd69c0a0c918c" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t8e4d2622b9fc4153af9d5e4f8533503b" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t72634ab38d1349c891124b0eac0f254c text");
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
          var text = document.querySelectorAll("#t72634ab38d1349c891124b0eac0f254c text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tce01551a8bd34522a932f26ff2145009", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t72634ab38d1349c891124b0eac0f254c .toyplot-mark-popup");
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
      var axes = {"tbc4c3aae94b84ac6b136b09f936b35ca": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


... or explicitly using :meth:`toyplot.canvas.Canvas.axes`:

.. code:: python

    canvas = toyplot.Canvas(width=300)
    axes = canvas.axes()
    axes.plot(y);



.. raw:: html

    <div align="center" class="toyplot" id="ta719d11fd6524ea39b0ff37dedb4d306"><svg height="300.0px" id="t7c5c754c54204de29ee3855de1284242" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t23685d96a55f4c6c8790685c2c4a4c64"><clipPath id="t0c10b605f39f4ec0ae76cb7425380e23"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t0c10b605f39f4ec0ae76cb7425380e23)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t872f749f023c44a4b2ad058a34b13f97" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tb75a792624cd4deda8bbaa9aeea42294" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t982aaa2840a04771b24ce7eb76675281" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#ta719d11fd6524ea39b0ff37dedb4d306 text");
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
          var text = document.querySelectorAll("#ta719d11fd6524ea39b0ff37dedb4d306 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t872f749f023c44a4b2ad058a34b13f97", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#ta719d11fd6524ea39b0ff37dedb4d306 .toyplot-mark-popup");
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
      var axes = {"t23685d96a55f4c6c8790685c2c4a4c64": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Properties
----------

Axes objects contain sets of nested properties that can be used to
adjust behavior. The list of available properties includes the
following:

-  axes.show - set to *False* to hide the axes completely (the plotted
   data will still be visible).
-  axes.aspect - set to "expand-domain" to expand the domain so that its
   aspect ratio matches the aspect ratio of the range.
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
-  axes.x.ticks.above - length of X axis ticks above the axis. Defaults
   to CSS pixels, supports all :ref:`units`.
-  axes.x.ticks.below - length of X axis ticks below the axis. Defaults
   to CSS pixels, supports all :ref:`units`.
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

    <div align="center" class="toyplot" id="tebe430a748414903b730288c582a32e0"><svg height="300.0px" id="td3d60742e0af47aa9bc2e91afdf62871" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc2fd1b4df4f2400e9679d3a39740b79f"><clipPath id="t411fe421c5664da0ac59b7ef63ffeb23"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t411fe421c5664da0ac59b7ef63ffeb23)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="520.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t454441cc73924c769e3d150e2f0added" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 150.0 L 60.204081632653057 137.2122838315494 L 70.408163265306115 124.63454160904925 L 80.612244897959187 112.4732995120626 L 90.816326530612244 100.92824479960623 L 101.0204081632653 90.188946950878403 L 111.22448979591836 80.431744939651352 L 121.42857142857143 71.816851753197028 L 131.63265306122449 64.485723699465396 L 141.83673469387753 58.558737698418767 L 152.0408163265306 54.133214696333944 L 162.24489795918367 51.281821658554989 L 172.44897959183672 50.051378379931208 L 182.65306122448979 50.462088705080177 L 192.85714285714286 52.507208781817653 L 203.0612244897959 56.153157795023972 L 213.26530612244898 61.340069362699978 L 223.46938775510202 67.982774540304391 L 233.67346938775509 75.972200292468429 L 243.87755102040813 85.177160469221121 L 254.08163265306121 95.446509878945093 L 264.28571428571428 106.61162608824417 L 274.48979591836735 118.48917819763791 L 284.69387755102036 130.88413712986275 L 294.89795918367344 143.59297800192866 L 305.10204081632656 156.40702199807123 L 315.30612244897958 169.11586287013719 L 325.51020408163265 181.51082180236202 L 335.71428571428572 193.38837391175579 L 345.91836734693879 204.55349012105484 L 356.12244897959187 214.82283953077882 L 366.32653061224488 224.02779970753153 L 376.5306122448979 232.01722545969557 L 386.73469387755097 238.65993063730002 L 396.93877551020404 243.84684220497604 L 407.14285714285717 247.49279121818236 L 417.34693877551018 249.53791129491984 L 427.55102040816325 249.94862162006879 L 437.75510204081627 248.71817834144503 L 447.9591836734694 245.86678530366606 L 458.16326530612241 241.44126230158125 L 468.36734693877548 235.51427630053465 L 478.57142857142856 228.183148246803 L 488.77551020408157 219.56825506034869 L 498.97959183673464 209.81105304912163 L 509.18367346938771 199.07175520039385 L 519.38775510204073 187.52670048793749 L 529.59183673469374 175.36545839095083 L 539.79591836734687 162.78771616845069 L 550.0 150.00000000000003" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t91bf701142ab4b61827d70bd16ca89c9" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="-5" y2="0"></line><line style="" x1="125.0" x2="125.0" y1="-5" y2="0"></line><line style="" x1="250.0" x2="250.0" y1="-5" y2="0"></line><line style="" x1="375.0" x2="375.0" y1="-5" y2="0"></line><line style="" x1="500.0" x2="500.0" y1="-5" y2="0"></line></g><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">π / 2</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">π</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(375.0,0) rotate(0)" x="0" y="0">3 π / 2</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">2 π</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="250.0" y="0">x</text></g><g class="toyplot-axes-Axis" id="t95e37fc0230a40fa9f43c58b9de62424" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="0.05137837993121064" x2="199.9486216200688" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-1.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" x="100.0" y="0">sin(x)</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="300.0" y="50.0">Trigonometry 101</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tebe430a748414903b730288c582a32e0 text");
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
          var text = document.querySelectorAll("#tebe430a748414903b730288c582a32e0 text");
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
      var data_tables = [{"data": [[0.0, 0.1282282715750936, 0.2564565431501872, 0.38468481472528077, 0.5129130863003744, 0.6411413578754679, 0.7693696294505615, 0.8975979010256552, 1.0258261726007487, 1.1540544441758422, 1.2822827157509358, 1.4105109873260295, 1.538739258901123, 1.6669675304762166, 1.7951958020513104, 1.9234240736264039, 2.0516523452014974, 2.179880616776591, 2.3081088883516845, 2.436337159926778, 2.5645654315018716, 2.6927937030769655, 2.821021974652059, 2.9492502462271526, 3.077478517802246, 3.2057067893773397, 3.333935060952433, 3.4621633325275267, 3.5903916041026207, 3.7186198756777142, 3.8468481472528078, 3.9750764188279013, 4.103304690402995, 4.231532961978089, 4.359761233553182, 4.487989505128276, 4.616217776703369, 4.744446048278463, 4.872674319853556, 5.00090259142865, 5.129130863003743, 5.257359134578837, 5.385587406153931, 5.513815677729024, 5.642043949304118, 5.770272220879211, 5.898500492454305, 6.026728764029398, 6.154957035604492, 6.283185307179586], [0.0, 0.127877161684506, 0.25365458390950735, 0.3752670048793741, 0.49071755200393785, 0.5981105304912159, 0.6956825506034864, 0.7818314824680297, 0.8551427630053461, 0.9144126230158124, 0.9586678530366606, 0.9871817834144501, 0.9994862162006879, 0.9953791129491982, 0.9749279121818236, 0.9384684220497604, 0.8865993063730001, 0.8201722545969561, 0.7402779970753157, 0.6482283953077888, 0.545534901210549, 0.43388373911755823, 0.3151082180236208, 0.19115862870137254, 0.06407021998071323, -0.06407021998071254, -0.19115862870137187, -0.3151082180236202, -0.433883739117558, -0.5455349012105485, -0.6482283953077882, -0.7402779970753153, -0.8201722545969556, -0.8865993063730001, -0.9384684220497602, -0.9749279121818235, -0.9953791129491981, -0.9994862162006879, -0.9871817834144503, -0.9586678530366608, -0.9144126230158128, -0.8551427630053465, -0.7818314824680299, -0.6956825506034869, -0.5981105304912162, -0.49071755200393863, -0.3752670048793746, -0.25365458390950835, -0.12787716168450664, -2.4492935982947064e-16]], "title": "Plot Data", "names": ["x", "y0"], "id": "t454441cc73924c769e3d150e2f0added", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tebe430a748414903b730288c582a32e0 .toyplot-mark-popup");
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
      var axes = {"tc2fd1b4df4f2400e9679d3a39740b79f": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 6.2831853071795862, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -1.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="ta2534b39ebee4cf39a5d9ed3e3656c75"><svg height="300.0px" id="t645f39273e334175bdba730ccb0a804d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="ta45acc85d0ce4c1a97ac2cf6f8967919"><clipPath id="t59ba6da57ff0474fa1ae01cff15de92a"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t59ba6da57ff0474fa1ae01cff15de92a)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t25fc17c65b1f4bca9c64d5ef57b9c2ea" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 52.020202020202021 249.9814490172617 L 54.040404040404042 249.92579606904675 L 56.060606060606062 249.8330411553552 L 58.080808080808083 249.70318427618705 L 60.101010101010104 249.53622543154225 L 62.121212121212125 249.33216462142082 L 64.141414141414145 249.09100184582277 L 66.161616161616166 248.81273710474809 L 68.181818181818187 248.49737039819686 L 70.202020202020208 248.14490172616894 L 72.222222222222229 247.75533108866441 L 74.242424242424249 247.32865848568329 L 76.26262626262627 246.86488391722554 L 78.282828282828277 246.36400738329112 L 80.303030303030312 245.82602888388013 L 82.323232323232332 245.25094841899249 L 84.343434343434339 244.63876598862825 L 86.36363636363636 243.98948159278737 L 88.383838383838381 243.30309523146988 L 90.404040404040416 242.57960690467579 L 92.424242424242408 241.81901661240508 L 94.444444444444457 241.02132435465768 L 96.464646464646478 240.1865301314337 L 98.484848484848484 239.31463394273311 L 100.50505050505049 238.40563578855591 L 102.52525252525253 237.45953566890205 L 104.54545454545453 236.47633358377161 L 106.56565656565655 235.45602953316452 L 108.5858585858586 234.39862351708078 L 110.60606060606062 233.30411553552051 L 112.62626262626262 232.17250558848355 L 114.64646464646464 231.00379367597 L 116.66666666666667 229.79797979797979 L 118.68686868686868 228.555063954513 L 120.7070707070707 227.27504614556958 L 122.72727272727272 225.95792637114951 L 124.74747474747474 224.60370463125281 L 126.76767676767676 223.21238092587956 L 128.78787878787878 221.78395525502961 L 130.80808080808083 220.31842761870305 L 132.82828282828282 218.81579801689998 L 134.84848484848484 217.27606644962015 L 136.86868686868686 215.69923291686379 L 138.88888888888889 214.08529741863074 L 140.90909090909088 212.43425995492112 L 142.92929292929293 210.74612052573485 L 144.94949494949495 209.02087913107198 L 146.96969696969697 207.25853577093244 L 148.98989898989899 205.45909044531632 L 151.01010101010098 203.62254315422359 L 153.03030303030303 201.74889389765423 L 155.05050505050505 199.83814267560822 L 157.07070707070707 197.89028948808561 L 159.09090909090907 195.90533433508642 L 161.11111111111111 193.88327721661054 L 163.13131313131311 191.8241181326581 L 165.15151515151516 189.727857083229 L 167.17171717171718 187.59449406832329 L 169.1919191919192 185.42402908794094 L 171.21212121212122 183.21646214208198 L 173.23232323232324 180.97179323074641 L 175.25252525252523 178.69002235393421 L 177.27272727272728 176.37114951164534 L 179.29292929292927 174.01517470387995 L 181.31313131313132 171.62209793063786 L 183.33333333333334 169.19191919191917 L 185.35353535353534 166.72463848772389 L 187.37373737373736 164.22025581805195 L 189.39393939393941 161.6787711829034 L 191.4141414141414 159.10018458227825 L 193.43434343434342 156.48449601617648 L 195.45454545454544 153.83170548459807 L 197.47474747474746 151.14181298754303 L 199.49494949494948 148.41481852501136 L 201.51515151515153 145.6507220970031 L 203.53535353535352 142.8495237035182 L 205.55555555555557 140.0112233445567 L 207.57575757575756 137.13582102011856 L 209.59595959595958 134.22331673020381 L 211.61616161616163 131.27371047481239 L 213.63636363636363 128.28700225394439 L 215.65656565656565 125.26319206759982 L 217.6767676767677 122.20227991577855 L 219.69696969696969 119.1042657984807 L 221.71717171717174 115.96914971570618 L 223.73737373737373 112.7969316674551 L 225.75757575757572 109.58761165372739 L 227.77777777777777 106.34118967452298 L 229.79797979797979 103.05766572984206 L 231.81818181818178 99.737039819684497 L 233.83838383838386 96.379311944050229 L 235.85858585858585 92.98448210293941 L 237.8787878787879 89.552550296351939 L 239.8989898989899 86.083516524287859 L 241.91919191919192 82.577380786747185 L 243.93939393939394 79.034143083729816 L 245.95959595959596 75.453803415235939 L 247.97979797979798 71.83636178126531 L 250.0 68.181818181818187" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t37cc68a7b47d4da1b8ecc992535d48c7" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">10</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="100.0" y="0">Days</text></g><g class="toyplot-axes-Axis" id="t07944e8af99a4283a1fe18c1a3db1762" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="0" x2="181.8181818181818" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(18.181818181818183,0) rotate(0)" x="0" y="0">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(109.09090909090908,0) rotate(0)" x="0" y="0">100</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">150</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" x="100.0" y="0">Users</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="50.0">Toyplot Users</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#ta2534b39ebee4cf39a5d9ed3e3656c75 text");
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
          var text = document.querySelectorAll("#ta2534b39ebee4cf39a5d9ed3e3656c75 text");
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
      var data_tables = [{"data": [[0.0, 0.10101010101010101, 0.20202020202020202, 0.30303030303030304, 0.40404040404040403, 0.5050505050505051, 0.6060606060606061, 0.7070707070707071, 0.8080808080808081, 0.9090909090909091, 1.0101010101010102, 1.1111111111111112, 1.2121212121212122, 1.3131313131313131, 1.4141414141414141, 1.5151515151515151, 1.6161616161616161, 1.7171717171717171, 1.8181818181818181, 1.9191919191919191, 2.0202020202020203, 2.121212121212121, 2.2222222222222223, 2.323232323232323, 2.4242424242424243, 2.525252525252525, 2.6262626262626263, 2.727272727272727, 2.8282828282828283, 2.929292929292929, 3.0303030303030303, 3.131313131313131, 3.2323232323232323, 3.3333333333333335, 3.4343434343434343, 3.5353535353535355, 3.6363636363636362, 3.7373737373737375, 3.8383838383838382, 3.9393939393939394, 4.040404040404041, 4.141414141414141, 4.242424242424242, 4.343434343434343, 4.444444444444445, 4.545454545454545, 4.646464646464646, 4.747474747474747, 4.848484848484849, 4.94949494949495, 5.05050505050505, 5.151515151515151, 5.252525252525253, 5.353535353535354, 5.454545454545454, 5.555555555555555, 5.656565656565657, 5.757575757575758, 5.858585858585858, 5.959595959595959, 6.0606060606060606, 6.161616161616162, 6.262626262626262, 6.363636363636363, 6.4646464646464645, 6.565656565656566, 6.666666666666667, 6.767676767676767, 6.8686868686868685, 6.96969696969697, 7.070707070707071, 7.171717171717171, 7.2727272727272725, 7.373737373737374, 7.474747474747475, 7.575757575757575, 7.6767676767676765, 7.777777777777778, 7.878787878787879, 7.979797979797979, 8.080808080808081, 8.181818181818182, 8.282828282828282, 8.383838383838384, 8.484848484848484, 8.585858585858587, 8.686868686868687, 8.787878787878787, 8.88888888888889, 8.98989898989899, 9.09090909090909, 9.191919191919192, 9.292929292929292, 9.393939393939394, 9.494949494949495, 9.595959595959595, 9.696969696969697, 9.797979797979798, 9.8989898989899, 10.0], [40.0, 40.01020304050607, 40.04081216202428, 40.09182736455464, 40.16324864809713, 40.25507601265177, 40.36730945821855, 40.49994898479747, 40.65299459238853, 40.82644628099173, 41.02030405060708, 41.23456790123457, 41.4692378328742, 41.72431384552597, 41.99979593918988, 42.29568411386593, 42.61197836955413, 42.94867870625446, 43.30578512396694, 43.68329762269156, 44.08121620242832, 44.499540863177224, 44.93827160493827, 45.397408427711454, 45.876951331496784, 46.376900316294254, 46.897255382103864, 47.438016528925615, 47.999183756759514, 48.58075706560555, 49.182736455463726, 49.805121926334046, 50.447913478216506, 51.111111111111114, 51.794714825017856, 52.49872461993674, 53.22314049586777, 53.96796245281094, 54.73319049076625, 55.5188246097337, 56.3248648097133, 57.15131109070502, 57.99816345270891, 58.86542189572492, 59.75308641975309, 60.66115702479338, 61.58963371084583, 62.53851647791042, 63.50780532598715, 64.49750025507602, 65.50760126517702, 66.53810835629017, 67.58902152841547, 68.6603407815529, 69.75206611570248, 70.8641975308642, 71.99673502703806, 73.14967860422406, 74.3230282624222, 75.51678400163249, 76.7309458218549, 77.96551372308949, 79.22048770533618, 80.49586776859505, 81.79165391286602, 83.10784613814917, 84.44444444444446, 85.80144883175186, 87.17885930007142, 88.57667584940313, 89.99489847974696, 91.43352719110294, 92.89256198347107, 94.37200285685134, 95.87184981124375, 97.3921028466483, 98.93276196306499, 100.49382716049382, 102.0752984389348, 103.6771757983879, 105.29945923885319, 106.94214876033058, 108.6052443628201, 110.2887460463218, 111.99265381083562, 113.7169676563616, 115.4616875828997, 117.22681359044994, 119.01234567901236, 120.81828384858687, 122.64462809917353, 124.49137843077237, 126.35853484338332, 128.24609733700643, 130.15406591164168, 132.08244056728904, 134.0312213039486, 136.00040812162024, 137.99000102030408, 140.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t25fc17c65b1f4bca9c64d5ef57b9c2ea", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#ta2534b39ebee4cf39a5d9ed3e3656c75 .toyplot-mark-popup");
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
      var axes = {"ta45acc85d0ce4c1a97ac2cf6f8967919": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 10.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 40.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


And the same properties can be used with the :ref:`convenience-api`,
as in the following example where we specify a minimum value for an axis
- for example, if we wanted the previous figure to include
:math:`y = 0`:

.. code:: python

    toyplot.plot(x, y, label="Toyplot Users", xlabel="Days", ylabel="Users", ymin=0, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t278fec611d8b4f06b7d03904199695ad"><svg height="300.0px" id="ta1f0bd8522f44a03ba20799007715ecc" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tfe08a22379524016a83b915fe01fa830"><clipPath id="tfc6123f195bb421dad952faa266ec0c0"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tfc6123f195bb421dad952faa266ec0c0)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t829ad3d199b74947858f418698823b5b" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 196.66666666666669 L 52.020202020202021 196.65306261265857 L 54.040404040404042 196.61225045063429 L 56.060606060606062 196.54423018059381 L 58.080808080808083 196.44900180253714 L 60.101010101010104 196.3265653164643 L 62.121212121212125 196.17692072237529 L 64.141414141414145 196.00006802027002 L 66.161616161616166 195.79600721014862 L 68.181818181818187 195.56473829201101 L 70.202020202020208 195.30626126585724 L 72.222222222222229 195.02057613168725 L 74.242424242424249 194.70768288950109 L 76.26262626262627 194.36758153929873 L 78.282828282828277 194.00027208108014 L 80.303030303030312 193.60575451484542 L 82.323232323232332 193.18402884059449 L 84.343434343434339 192.7350950583274 L 86.36363636363636 192.25895316804409 L 88.383838383838381 191.75560316974457 L 90.404040404040416 191.22504506342892 L 92.424242424242408 190.66727884909702 L 94.444444444444457 190.08230452674897 L 96.464646464646478 189.47012209638473 L 98.484848484848484 188.83073155800429 L 100.50505050505049 188.16413291160768 L 102.52525252525253 187.47032615719485 L 104.54545454545453 186.74931129476585 L 106.56565656565655 186.00108832432065 L 108.5858585858586 185.22565724585928 L 110.60606060606062 184.42301805938169 L 112.62626262626262 183.59317076488793 L 114.64646464646464 182.736115362378 L 116.66666666666667 181.85185185185185 L 118.68686868686868 180.94038023330953 L 120.7070707070707 180.00170050675101 L 122.72727272727272 179.03581267217632 L 124.74747474747474 178.04271672958541 L 126.76767676767676 177.02241267897836 L 128.78787878787878 175.97490052035508 L 130.80808080808083 174.9001802537156 L 132.82828282828282 173.79825187905996 L 134.84848484848484 172.66911539638812 L 136.86868686868686 171.51277080570011 L 138.88888888888889 170.32921810699588 L 140.90909090909088 169.11845730027548 L 142.92929292929293 167.88048838553888 L 144.94949494949495 166.61531136278612 L 146.96969696969697 165.32292623201715 L 148.98989898989899 164.00333299323196 L 151.01010101010098 162.65653164643066 L 153.03030303030303 161.28252219161311 L 155.05050505050505 159.88130462877939 L 157.07070707070707 158.45287895792947 L 159.09090909090907 156.99724517906336 L 161.11111111111111 155.51440329218104 L 163.13131313131311 154.00435329728259 L 165.15151515151516 152.46709519436791 L 167.17171717171718 150.90262898343707 L 169.1919191919192 149.31095466449003 L 171.21212121212122 147.69207223752682 L 173.23232323232324 146.04598170254735 L 175.25252525252523 144.37268305955175 L 177.27272727272728 142.67217630853995 L 179.29292929292927 140.94446144951195 L 181.31313131313132 139.18953848246778 L 183.33333333333334 137.40740740740739 L 185.35353535353534 135.59806822433086 L 187.37373737373736 133.7615209332381 L 189.39393939393941 131.89776553412915 L 191.4141414141414 130.00680202700406 L 193.43434343434342 128.08863041186277 L 195.45454545454544 126.14325068870525 L 197.47474747474746 124.17066285753155 L 199.49494949494948 122.17086691834166 L 201.51515151515153 120.14386287113561 L 203.53535353535352 118.08965071591335 L 205.55555555555557 116.00823045267489 L 207.57575757575756 113.89960208142026 L 209.59595959595958 111.76376560214946 L 211.61616161616163 109.60072101486243 L 213.63636363636363 107.41046831955924 L 215.65656565656565 105.19300751623986 L 217.6767676767677 102.94833860490427 L 219.69696969696969 100.6764615855525 L 221.71717171717174 98.377376458184514 L 223.73737373737373 96.051083222800401 L 225.75757575757572 93.69758187940009 L 227.77777777777777 91.316872427983526 L 229.79797979797979 88.908954868550836 L 231.81818181818178 86.473829201101964 L 233.83838383838386 84.011495425636838 L 235.85858585858585 81.521953542155572 L 237.8787878787879 79.005203550658095 L 239.8989898989899 76.461245451144435 L 241.91919191919192 73.890079243614622 L 243.93939393939394 71.291704928068526 L 245.95959595959596 68.666122504506347 L 247.97979797979798 66.013331972927887 L 250.0 63.333333333333329" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="te170c2c0c70445fb8c63c8ebcc2297e6" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">10</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="100.0" y="0">Days</text></g><g class="toyplot-axes-Axis" id="t40aedb983cbb479da3d0e78d766f41a6" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="53.333333333333336" x2="186.66666666666666" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0) rotate(0)" x="0" y="0">100</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">150</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" x="100.0" y="0">Users</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="50.0">Toyplot Users</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t278fec611d8b4f06b7d03904199695ad text");
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
          var text = document.querySelectorAll("#t278fec611d8b4f06b7d03904199695ad text");
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
      var data_tables = [{"data": [[0.0, 0.10101010101010101, 0.20202020202020202, 0.30303030303030304, 0.40404040404040403, 0.5050505050505051, 0.6060606060606061, 0.7070707070707071, 0.8080808080808081, 0.9090909090909091, 1.0101010101010102, 1.1111111111111112, 1.2121212121212122, 1.3131313131313131, 1.4141414141414141, 1.5151515151515151, 1.6161616161616161, 1.7171717171717171, 1.8181818181818181, 1.9191919191919191, 2.0202020202020203, 2.121212121212121, 2.2222222222222223, 2.323232323232323, 2.4242424242424243, 2.525252525252525, 2.6262626262626263, 2.727272727272727, 2.8282828282828283, 2.929292929292929, 3.0303030303030303, 3.131313131313131, 3.2323232323232323, 3.3333333333333335, 3.4343434343434343, 3.5353535353535355, 3.6363636363636362, 3.7373737373737375, 3.8383838383838382, 3.9393939393939394, 4.040404040404041, 4.141414141414141, 4.242424242424242, 4.343434343434343, 4.444444444444445, 4.545454545454545, 4.646464646464646, 4.747474747474747, 4.848484848484849, 4.94949494949495, 5.05050505050505, 5.151515151515151, 5.252525252525253, 5.353535353535354, 5.454545454545454, 5.555555555555555, 5.656565656565657, 5.757575757575758, 5.858585858585858, 5.959595959595959, 6.0606060606060606, 6.161616161616162, 6.262626262626262, 6.363636363636363, 6.4646464646464645, 6.565656565656566, 6.666666666666667, 6.767676767676767, 6.8686868686868685, 6.96969696969697, 7.070707070707071, 7.171717171717171, 7.2727272727272725, 7.373737373737374, 7.474747474747475, 7.575757575757575, 7.6767676767676765, 7.777777777777778, 7.878787878787879, 7.979797979797979, 8.080808080808081, 8.181818181818182, 8.282828282828282, 8.383838383838384, 8.484848484848484, 8.585858585858587, 8.686868686868687, 8.787878787878787, 8.88888888888889, 8.98989898989899, 9.09090909090909, 9.191919191919192, 9.292929292929292, 9.393939393939394, 9.494949494949495, 9.595959595959595, 9.696969696969697, 9.797979797979798, 9.8989898989899, 10.0], [40.0, 40.01020304050607, 40.04081216202428, 40.09182736455464, 40.16324864809713, 40.25507601265177, 40.36730945821855, 40.49994898479747, 40.65299459238853, 40.82644628099173, 41.02030405060708, 41.23456790123457, 41.4692378328742, 41.72431384552597, 41.99979593918988, 42.29568411386593, 42.61197836955413, 42.94867870625446, 43.30578512396694, 43.68329762269156, 44.08121620242832, 44.499540863177224, 44.93827160493827, 45.397408427711454, 45.876951331496784, 46.376900316294254, 46.897255382103864, 47.438016528925615, 47.999183756759514, 48.58075706560555, 49.182736455463726, 49.805121926334046, 50.447913478216506, 51.111111111111114, 51.794714825017856, 52.49872461993674, 53.22314049586777, 53.96796245281094, 54.73319049076625, 55.5188246097337, 56.3248648097133, 57.15131109070502, 57.99816345270891, 58.86542189572492, 59.75308641975309, 60.66115702479338, 61.58963371084583, 62.53851647791042, 63.50780532598715, 64.49750025507602, 65.50760126517702, 66.53810835629017, 67.58902152841547, 68.6603407815529, 69.75206611570248, 70.8641975308642, 71.99673502703806, 73.14967860422406, 74.3230282624222, 75.51678400163249, 76.7309458218549, 77.96551372308949, 79.22048770533618, 80.49586776859505, 81.79165391286602, 83.10784613814917, 84.44444444444446, 85.80144883175186, 87.17885930007142, 88.57667584940313, 89.99489847974696, 91.43352719110294, 92.89256198347107, 94.37200285685134, 95.87184981124375, 97.3921028466483, 98.93276196306499, 100.49382716049382, 102.0752984389348, 103.6771757983879, 105.29945923885319, 106.94214876033058, 108.6052443628201, 110.2887460463218, 111.99265381083562, 113.7169676563616, 115.4616875828997, 117.22681359044994, 119.01234567901236, 120.81828384858687, 122.64462809917353, 124.49137843077237, 126.35853484338332, 128.24609733700643, 130.15406591164168, 132.08244056728904, 134.0312213039486, 136.00040812162024, 137.99000102030408, 140.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t829ad3d199b74947858f418698823b5b", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t278fec611d8b4f06b7d03904199695ad .toyplot-mark-popup");
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
      var axes = {"tfe08a22379524016a83b915fe01fa830": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 10.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Scale
-----

An important property of each axis is its scale, used to specify linear
or logarithmic mappings from *domain* to *range*:

.. code:: python

    x = numpy.linspace(-1000, 1000)

.. code:: python

    canvas = toyplot.Canvas(width=700)
    
    axes = canvas.axes(grid=(2, 2, 0, 0), xscale="linear", yscale="linear")
    axes.plot(x, x, marker="o")
    
    axes = canvas.axes(grid=(2, 2, 0, 1), xscale="log", yscale="linear")
    axes.plot(x, x, marker="o")
    
    axes = canvas.axes(grid=(2, 2, 1, 0), xscale="linear", yscale="log")
    axes.plot(x, x, marker="o")
    
    axes = canvas.axes(grid=(2, 2, 1, 1), xscale="log", yscale="log")
    axes.plot(x, x, marker="o");



.. raw:: html

    <div align="center" class="toyplot" id="t808b0c2139c74febbe911bba9ea794fd"><svg height="700.0px" id="t205bde667c5444c390e2706129289c18" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 700.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tea35774218794e1ea93b1b661cb13624"><clipPath id="t8e7c7727daed4885b374c99c68c461fb"><rect height="270.0" width="270.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t8e7c7727daed4885b374c99c68c461fb)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tecbb8e53027c400ba59c6360d8d0eb63" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 300.0 L 55.102040816326536 294.89795918367344 L 60.204081632653057 289.79591836734693 L 65.306122448979593 284.69387755102042 L 70.408163265306115 279.59183673469386 L 75.510204081632651 274.48979591836735 L 80.612244897959187 269.38775510204084 L 85.714285714285722 264.28571428571428 L 90.816326530612244 259.18367346938777 L 95.918367346938766 254.08163265306121 L 101.0204081632653 248.9795918367347 L 106.12244897959184 243.87755102040816 L 111.22448979591836 238.77551020408163 L 116.32653061224489 233.67346938775512 L 121.42857142857142 228.57142857142856 L 126.53061224489795 223.46938775510205 L 131.63265306122449 218.36734693877554 L 136.73469387755102 213.265306122449 L 141.83673469387753 208.16326530612247 L 146.93877551020407 203.06122448979593 L 152.0408163265306 197.95918367346937 L 157.14285714285711 192.85714285714283 L 162.24489795918367 187.75510204081633 L 167.34693877551018 182.65306122448982 L 172.44897959183672 177.55102040816328 L 177.55102040816328 172.44897959183672 L 182.65306122448979 167.34693877551021 L 187.75510204081633 162.24489795918367 L 192.85714285714283 157.14285714285717 L 197.95918367346937 152.0408163265306 L 203.06122448979588 146.9387755102041 L 208.16326530612244 141.83673469387756 L 213.26530612244898 136.73469387755102 L 218.36734693877551 131.63265306122449 L 223.46938775510202 126.53061224489797 L 228.57142857142853 121.42857142857144 L 233.67346938775506 116.32653061224491 L 238.77551020408163 111.22448979591839 L 243.87755102040816 106.12244897959184 L 248.9795918367347 101.0204081632653 L 254.08163265306121 95.918367346938794 L 259.18367346938771 90.816326530612258 L 264.28571428571428 85.714285714285722 L 269.38775510204084 80.612244897959187 L 274.48979591836735 75.510204081632651 L 279.59183673469386 70.408163265306115 L 284.69387755102036 65.306122448979607 L 289.79591836734693 60.204081632653072 L 294.89795918367344 55.102040816326536 L 300.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="300.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="55.102040816326536" cy="294.89795918367344" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.204081632653057" cy="289.79591836734693" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.306122448979593" cy="284.69387755102042" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.408163265306115" cy="279.59183673469386" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="75.510204081632651" cy="274.48979591836735" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.612244897959187" cy="269.38775510204084" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="85.714285714285722" cy="264.28571428571428" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.816326530612244" cy="259.18367346938777" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="95.918367346938766" cy="254.08163265306121" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="101.0204081632653" cy="248.9795918367347" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="106.12244897959184" cy="243.87755102040816" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.22448979591836" cy="238.77551020408163" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="116.32653061224489" cy="233.67346938775512" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="121.42857142857142" cy="228.57142857142856" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="126.53061224489795" cy="223.46938775510205" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="131.63265306122449" cy="218.36734693877554" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="136.73469387755102" cy="213.265306122449" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="141.83673469387753" cy="208.16326530612247" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="146.93877551020407" cy="203.06122448979593" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="152.0408163265306" cy="197.95918367346937" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="157.14285714285711" cy="192.85714285714283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="162.24489795918367" cy="187.75510204081633" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="167.34693877551018" cy="182.65306122448982" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="172.44897959183672" cy="177.55102040816328" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.55102040816328" cy="172.44897959183672" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.65306122448979" cy="167.34693877551021" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="187.75510204081633" cy="162.24489795918367" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="192.85714285714283" cy="157.14285714285717" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="197.95918367346937" cy="152.0408163265306" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="203.06122448979588" cy="146.9387755102041" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="208.16326530612244" cy="141.83673469387756" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="213.26530612244898" cy="136.73469387755102" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.36734693877551" cy="131.63265306122449" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="223.46938775510202" cy="126.53061224489797" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="228.57142857142853" cy="121.42857142857144" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="233.67346938775506" cy="116.32653061224491" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="238.77551020408163" cy="111.22448979591839" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="243.87755102040816" cy="106.12244897959184" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="248.9795918367347" cy="101.0204081632653" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="254.08163265306121" cy="95.918367346938794" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="259.18367346938771" cy="90.816326530612258" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.28571428571428" cy="85.714285714285722" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="269.38775510204084" cy="80.612244897959187" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="274.48979591836735" cy="75.510204081632651" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.59183673469386" cy="70.408163265306115" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="284.69387755102036" cy="65.306122448979607" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="289.79591836734693" cy="60.204081632653072" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="294.89795918367344" cy="55.102040816326536" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="300.0" cy="50.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="200.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="245.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tc74f8a7c1b5a474da96ce76f6514905c" transform="translate(50.0,310.0) rotate(0.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-1000</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0) rotate(0)" x="0" y="0">-500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0) rotate(0)" x="0" y="0">500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1000</text></g></g><g class="toyplot-axes-Axis" id="t0ed547a67cc547d492dcf3dc34733139" transform="translate(40.0,300.0) rotate(-90.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0) rotate(0)" x="0" y="0">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0) rotate(0)" x="0" y="0">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1000</text></g></g></g><g class="toyplot-axes-Cartesian" id="tdf23dc0055934dfd876df776c6e6e89a"><clipPath id="t117ecc651c8147e98207b59df1a756d8"><rect height="270.0" width="270.0" x="390.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t117ecc651c8147e98207b59df1a756d8)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="390.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t11c4af90d84341af909bb21a6039ea96" style="fill:none"><g class="toyplot-Series"><path d="M 400.0 300.0 L 400.60327406975989 294.89795918367344 L 401.23278554177233 289.79591836734693 L 401.89092081496426 284.69387755102042 L 402.58040744362592 279.59183673469386 L 403.30438243340046 274.48979591836735 L 404.06647853205061 269.38775510204084 L 404.87093452260797 264.28571428571428 L 405.72273800502091 259.18367346938777 L 406.62781287314141 254.08163265306121 L 407.59326940431862 248.9795918367347 L 408.62774386231757 243.87755102040816 L 409.74186904521588 238.77551020408163 L 410.94894146703069 233.67346938775512 L 412.2658928431531 228.57142857142856 L 413.71474930252282 223.46938775510205 L 415.32490528834131 218.36734693877554 L 417.13682736576106 213.265306122449 L 419.2084242573892 208.16326530612247 L 421.62677982900965 203.06122448979593 L 424.53178568630631 197.95918367346937 L 428.16993466714189 192.85714285714283 L 433.04086918974986 187.75510204081633 L 440.43582751029504 182.65306122448982 L 456.33986933428378 177.55102040816328 L 593.66013066571622 172.44897959183672 L 609.5641724897049 167.34693877551021 L 616.95913081025014 162.24489795918367 L 621.83006533285811 157.14285714285717 L 625.46821431369381 152.0408163265306 L 628.37322017099041 146.9387755102041 L 630.7915757426108 141.83673469387756 L 632.86317263423894 136.73469387755102 L 634.67509471165863 131.63265306122449 L 636.28525069747718 126.53061224489797 L 637.7341071568469 121.42857142857144 L 639.05105853296936 116.32653061224491 L 640.25813095478418 111.22448979591839 L 641.37225613768248 106.12244897959184 L 642.40673059568132 101.0204081632653 L 643.37218712685853 95.918367346938794 L 644.2772619949792 90.816326530612258 L 645.12906547739215 85.714285714285722 L 645.93352146794939 80.612244897959187 L 646.69561756659948 75.510204081632651 L 647.41959255637403 70.408163265306115 L 648.10907918503574 65.306122448979607 L 648.76721445822773 60.204081632653072 L 649.39672593024011 55.102040816326536 L 650.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="300.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.60327406975989" cy="294.89795918367344" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.23278554177233" cy="289.79591836734693" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.89092081496426" cy="284.69387755102042" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="402.58040744362592" cy="279.59183673469386" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="403.30438243340046" cy="274.48979591836735" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="404.06647853205061" cy="269.38775510204084" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="404.87093452260797" cy="264.28571428571428" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="405.72273800502091" cy="259.18367346938777" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="406.62781287314141" cy="254.08163265306121" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="407.59326940431862" cy="248.9795918367347" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="408.62774386231757" cy="243.87755102040816" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="409.74186904521588" cy="238.77551020408163" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.94894146703069" cy="233.67346938775512" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="412.2658928431531" cy="228.57142857142856" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="413.71474930252282" cy="223.46938775510205" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="415.32490528834131" cy="218.36734693877554" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="417.13682736576106" cy="213.265306122449" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="419.2084242573892" cy="208.16326530612247" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="421.62677982900965" cy="203.06122448979593" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="424.53178568630631" cy="197.95918367346937" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="428.16993466714189" cy="192.85714285714283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="433.04086918974986" cy="187.75510204081633" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.43582751029504" cy="182.65306122448982" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="456.33986933428378" cy="177.55102040816328" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="593.66013066571622" cy="172.44897959183672" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="609.5641724897049" cy="167.34693877551021" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="616.95913081025014" cy="162.24489795918367" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="621.83006533285811" cy="157.14285714285717" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="625.46821431369381" cy="152.0408163265306" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="628.37322017099041" cy="146.9387755102041" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="630.7915757426108" cy="141.83673469387756" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="632.86317263423894" cy="136.73469387755102" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="634.67509471165863" cy="131.63265306122449" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="636.28525069747718" cy="126.53061224489797" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="637.7341071568469" cy="121.42857142857144" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="639.05105853296936" cy="116.32653061224491" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="640.25813095478418" cy="111.22448979591839" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="641.37225613768248" cy="106.12244897959184" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="642.40673059568132" cy="101.0204081632653" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="643.37218712685853" cy="95.918367346938794" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="644.2772619949792" cy="90.816326530612258" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="645.12906547739215" cy="85.714285714285722" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="645.93352146794939" cy="80.612244897959187" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="646.69561756659948" cy="75.510204081632651" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="647.41959255637403" cy="70.408163265306115" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="648.10907918503574" cy="65.306122448979607" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="648.76721445822773" cy="60.204081632653072" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="649.39672593024011" cy="55.102040816326536" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="650.0" cy="50.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="td08da70840eb4bc69c0f9cbe3737fe70" transform="translate(400.0,310.0) rotate(0.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-10 ³</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(33.33333333333333,0) rotate(0)" x="0" y="0">-10 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">-10 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">-10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(183.33333333333334,0) rotate(0)" x="0" y="0">10 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(216.66666666666666,0) rotate(0)" x="0" y="0">10 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">10 ³</text></g></g><g class="toyplot-axes-Axis" id="t1bd6835eb4704571b3a3ab85ccf06c3b" transform="translate(390.0,300.0) rotate(-90.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0) rotate(0)" x="0" y="0">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0) rotate(0)" x="0" y="0">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1000</text></g></g></g><g class="toyplot-axes-Cartesian" id="td438489ef4254b6f8a05b0bd71385efb"><clipPath id="tdc2f789197db4760ba7d0e45948e6c3d"><rect height="270.0" width="270.0" x="40.0" y="390.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tdc2f789197db4760ba7d0e45948e6c3d)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="40.0" y="390.0"></rect><g class="toyplot-mark-Plot" id="t488a11dc598c4a4192186b3943648670" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 650.0 L 55.102040816326536 649.39672593024011 L 60.204081632653057 648.76721445822773 L 65.306122448979593 648.10907918503585 L 70.408163265306115 647.41959255637403 L 75.510204081632651 646.69561756659948 L 80.612244897959187 645.93352146794928 L 85.714285714285722 645.12906547739215 L 90.816326530612244 644.2772619949792 L 95.918367346938766 643.37218712685865 L 101.0204081632653 642.40673059568132 L 106.12244897959184 641.37225613768248 L 111.22448979591836 640.25813095478406 L 116.32653061224489 639.05105853296936 L 121.42857142857142 637.73410715684679 L 126.53061224489795 636.28525069747707 L 131.63265306122449 634.67509471165863 L 136.73469387755102 632.86317263423894 L 141.83673469387753 630.7915757426108 L 146.93877551020407 628.37322017099041 L 152.0408163265306 625.46821431369381 L 157.14285714285711 621.83006533285811 L 162.24489795918367 616.95913081025014 L 167.34693877551018 609.56417248970502 L 172.44897959183672 593.66013066571622 L 177.55102040816328 456.33986933428378 L 182.65306122448979 440.43582751029504 L 187.75510204081633 433.04086918974986 L 192.85714285714283 428.16993466714189 L 197.95918367346937 424.53178568630631 L 203.06122448979588 421.62677982900965 L 208.16326530612244 419.2084242573892 L 213.26530612244898 417.13682736576106 L 218.36734693877551 415.32490528834131 L 223.46938775510202 413.71474930252282 L 228.57142857142853 412.2658928431531 L 233.67346938775506 410.94894146703069 L 238.77551020408163 409.74186904521588 L 243.87755102040816 408.62774386231757 L 248.9795918367347 407.59326940431862 L 254.08163265306121 406.62781287314141 L 259.18367346938771 405.72273800502091 L 264.28571428571428 404.87093452260797 L 269.38775510204084 404.06647853205061 L 274.48979591836735 403.30438243340046 L 279.59183673469386 402.58040744362592 L 284.69387755102036 401.89092081496426 L 289.79591836734693 401.23278554177233 L 294.89795918367344 400.60327406975983 L 300.0 400.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="650.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="55.102040816326536" cy="649.39672593024011" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.204081632653057" cy="648.76721445822773" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.306122448979593" cy="648.10907918503585" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.408163265306115" cy="647.41959255637403" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="75.510204081632651" cy="646.69561756659948" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.612244897959187" cy="645.93352146794928" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="85.714285714285722" cy="645.12906547739215" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.816326530612244" cy="644.2772619949792" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="95.918367346938766" cy="643.37218712685865" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="101.0204081632653" cy="642.40673059568132" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="106.12244897959184" cy="641.37225613768248" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.22448979591836" cy="640.25813095478406" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="116.32653061224489" cy="639.05105853296936" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="121.42857142857142" cy="637.73410715684679" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="126.53061224489795" cy="636.28525069747707" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="131.63265306122449" cy="634.67509471165863" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="136.73469387755102" cy="632.86317263423894" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="141.83673469387753" cy="630.7915757426108" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="146.93877551020407" cy="628.37322017099041" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="152.0408163265306" cy="625.46821431369381" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="157.14285714285711" cy="621.83006533285811" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="162.24489795918367" cy="616.95913081025014" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="167.34693877551018" cy="609.56417248970502" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="172.44897959183672" cy="593.66013066571622" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.55102040816328" cy="456.33986933428378" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.65306122448979" cy="440.43582751029504" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="187.75510204081633" cy="433.04086918974986" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="192.85714285714283" cy="428.16993466714189" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="197.95918367346937" cy="424.53178568630631" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="203.06122448979588" cy="421.62677982900965" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="208.16326530612244" cy="419.2084242573892" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="213.26530612244898" cy="417.13682736576106" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.36734693877551" cy="415.32490528834131" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="223.46938775510202" cy="413.71474930252282" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="228.57142857142853" cy="412.2658928431531" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="233.67346938775506" cy="410.94894146703069" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="238.77551020408163" cy="409.74186904521588" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="243.87755102040816" cy="408.62774386231757" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="248.9795918367347" cy="407.59326940431862" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="254.08163265306121" cy="406.62781287314141" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="259.18367346938771" cy="405.72273800502091" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.28571428571428" cy="404.87093452260797" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="269.38775510204084" cy="404.06647853205061" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="274.48979591836735" cy="403.30438243340046" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.59183673469386" cy="402.58040744362592" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="284.69387755102036" cy="401.89092081496426" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="289.79591836734693" cy="401.23278554177233" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="294.89795918367344" cy="400.60327406975983" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="300.0" cy="400.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="200.0" y="410.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="245.0" y="417.0"></text></g><g class="toyplot-axes-Axis" id="t3d3cac2872014acfaaadf237dde78aa0" transform="translate(50.0,660.0) rotate(0.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-1000</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0) rotate(0)" x="0" y="0">-500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0) rotate(0)" x="0" y="0">500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1000</text></g></g><g class="toyplot-axes-Axis" id="te1e1af46f4b94f28ac5fe391ac9d0248" transform="translate(40.0,650.0) rotate(-90.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-10 ³</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(33.33333333333333,0) rotate(0)" x="0" y="0">-10 ²</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">-10 ¹</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">-10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(183.33333333333334,0) rotate(0)" x="0" y="0">10 ¹</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(216.66666666666666,0) rotate(0)" x="0" y="0">10 ²</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">10 ³</text></g></g></g><g class="toyplot-axes-Cartesian" id="ta73a4e4f3cef48d48f20a70369afa2e8"><clipPath id="t57381236a1cf40c4a1d5b6ea6958494b"><rect height="270.0" width="270.0" x="390.0" y="390.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t57381236a1cf40c4a1d5b6ea6958494b)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="390.0" y="390.0"></rect><g class="toyplot-mark-Plot" id="t17e49a8ca0ed4fdd85d5f2fccda66721" style="fill:none"><g class="toyplot-Series"><path d="M 400.0 650.0 L 400.60327406975989 649.39672593024011 L 401.23278554177233 648.76721445822773 L 401.89092081496426 648.10907918503585 L 402.58040744362592 647.41959255637403 L 403.30438243340046 646.69561756659948 L 404.06647853205061 645.93352146794928 L 404.87093452260797 645.12906547739215 L 405.72273800502091 644.2772619949792 L 406.62781287314141 643.37218712685865 L 407.59326940431862 642.40673059568132 L 408.62774386231757 641.37225613768248 L 409.74186904521588 640.25813095478406 L 410.94894146703069 639.05105853296936 L 412.2658928431531 637.73410715684679 L 413.71474930252282 636.28525069747707 L 415.32490528834131 634.67509471165863 L 417.13682736576106 632.86317263423894 L 419.2084242573892 630.7915757426108 L 421.62677982900965 628.37322017099041 L 424.53178568630631 625.46821431369381 L 428.16993466714189 621.83006533285811 L 433.04086918974986 616.95913081025014 L 440.43582751029504 609.56417248970502 L 456.33986933428378 593.66013066571622 L 593.66013066571622 456.33986933428378 L 609.5641724897049 440.43582751029504 L 616.95913081025014 433.04086918974986 L 621.83006533285811 428.16993466714189 L 625.46821431369381 424.53178568630631 L 628.37322017099041 421.62677982900965 L 630.7915757426108 419.2084242573892 L 632.86317263423894 417.13682736576106 L 634.67509471165863 415.32490528834131 L 636.28525069747718 413.71474930252282 L 637.7341071568469 412.2658928431531 L 639.05105853296936 410.94894146703069 L 640.25813095478418 409.74186904521588 L 641.37225613768248 408.62774386231757 L 642.40673059568132 407.59326940431862 L 643.37218712685853 406.62781287314141 L 644.2772619949792 405.72273800502091 L 645.12906547739215 404.87093452260797 L 645.93352146794939 404.06647853205061 L 646.69561756659948 403.30438243340046 L 647.41959255637403 402.58040744362592 L 648.10907918503574 401.89092081496426 L 648.76721445822773 401.23278554177233 L 649.39672593024011 400.60327406975983 L 650.0 400.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="650.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.60327406975989" cy="649.39672593024011" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.23278554177233" cy="648.76721445822773" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.89092081496426" cy="648.10907918503585" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="402.58040744362592" cy="647.41959255637403" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="403.30438243340046" cy="646.69561756659948" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="404.06647853205061" cy="645.93352146794928" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="404.87093452260797" cy="645.12906547739215" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="405.72273800502091" cy="644.2772619949792" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="406.62781287314141" cy="643.37218712685865" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="407.59326940431862" cy="642.40673059568132" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="408.62774386231757" cy="641.37225613768248" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="409.74186904521588" cy="640.25813095478406" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.94894146703069" cy="639.05105853296936" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="412.2658928431531" cy="637.73410715684679" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="413.71474930252282" cy="636.28525069747707" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="415.32490528834131" cy="634.67509471165863" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="417.13682736576106" cy="632.86317263423894" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="419.2084242573892" cy="630.7915757426108" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="421.62677982900965" cy="628.37322017099041" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="424.53178568630631" cy="625.46821431369381" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="428.16993466714189" cy="621.83006533285811" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="433.04086918974986" cy="616.95913081025014" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.43582751029504" cy="609.56417248970502" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="456.33986933428378" cy="593.66013066571622" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="593.66013066571622" cy="456.33986933428378" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="609.5641724897049" cy="440.43582751029504" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="616.95913081025014" cy="433.04086918974986" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="621.83006533285811" cy="428.16993466714189" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="625.46821431369381" cy="424.53178568630631" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="628.37322017099041" cy="421.62677982900965" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="630.7915757426108" cy="419.2084242573892" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="632.86317263423894" cy="417.13682736576106" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="634.67509471165863" cy="415.32490528834131" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="636.28525069747718" cy="413.71474930252282" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="637.7341071568469" cy="412.2658928431531" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="639.05105853296936" cy="410.94894146703069" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="640.25813095478418" cy="409.74186904521588" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="641.37225613768248" cy="408.62774386231757" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="642.40673059568132" cy="407.59326940431862" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="643.37218712685853" cy="406.62781287314141" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="644.2772619949792" cy="405.72273800502091" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="645.12906547739215" cy="404.87093452260797" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="645.93352146794939" cy="404.06647853205061" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="646.69561756659948" cy="403.30438243340046" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="647.41959255637403" cy="402.58040744362592" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="648.10907918503574" cy="401.89092081496426" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="648.76721445822773" cy="401.23278554177233" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="649.39672593024011" cy="400.60327406975983" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="650.0" cy="400.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="550.0" y="410.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="417.0"></text></g><g class="toyplot-axes-Axis" id="tca860da3618c4b30badf969d37eca731" transform="translate(400.0,660.0) rotate(0.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-10 ³</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(33.33333333333333,0) rotate(0)" x="0" y="0">-10 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">-10 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">-10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(183.33333333333334,0) rotate(0)" x="0" y="0">10 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(216.66666666666666,0) rotate(0)" x="0" y="0">10 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">10 ³</text></g></g><g class="toyplot-axes-Axis" id="t0dc8af86937e446eab13d04fcea4db59" transform="translate(390.0,650.0) rotate(-90.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-10 ³</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(33.33333333333333,0) rotate(0)" x="0" y="0">-10 ²</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">-10 ¹</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">-10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(183.33333333333334,0) rotate(0)" x="0" y="0">10 ¹</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(216.66666666666666,0) rotate(0)" x="0" y="0">10 ²</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">10 ³</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t808b0c2139c74febbe911bba9ea794fd text");
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
          var text = document.querySelectorAll("#t808b0c2139c74febbe911bba9ea794fd text");
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
      var data_tables = [{"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tecbb8e53027c400ba59c6360d8d0eb63", "filename": "toyplot"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t11c4af90d84341af909bb21a6039ea96", "filename": "toyplot"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t488a11dc598c4a4192186b3943648670", "filename": "toyplot"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t17e49a8ca0ed4fdd85d5f2fccda66721", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t808b0c2139c74febbe911bba9ea794fd .toyplot-mark-popup");
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
      var axes = {"ta73a4e4f3cef48d48f20a70369afa2e8": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 500.0, "min": -Infinity}, "max": 500.0, "min": 400.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 550.0, "min": 500.0}, "max": 550.0, "min": 500.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 550.0}, "max": 650.0, "min": 550.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 550.0, "min": Infinity}, "max": 550.0, "min": 650.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 500.0, "min": 550.0}, "max": 500.0, "min": 550.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": -Infinity, "min": 500.0}, "max": 400.0, "min": 500.0}, "scale": ["log", 10]}]}, "td438489ef4254b6f8a05b0bd71385efb": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 550.0, "min": Infinity}, "max": 550.0, "min": 650.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 500.0, "min": 550.0}, "max": 500.0, "min": 550.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": -Infinity, "min": 500.0}, "max": 400.0, "min": 500.0}, "scale": ["log", 10]}]}, "tdf23dc0055934dfd876df776c6e6e89a": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 500.0, "min": -Infinity}, "max": 500.0, "min": 400.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 550.0, "min": 500.0}, "max": 550.0, "min": 500.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 550.0}, "max": 650.0, "min": 550.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 300.0}, "scale": "linear"}]}, "tea35774218794e1ea93b1b661cb13624": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 300.0}, "scale": "linear"}]}};
    
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


Note that Toyplot handles negative values correctly, and provides
sensible results for values near zero by rendering them using a small
linear region around the origin.

The scale can be specified in two ways:

-  As a string - "linear", "log" (base 10), "log10" (base 10), or "log2"
   (base 2).
-  As a tuple - ("log", 2), ("log", 10).

For example, the following are all equivalent

.. code:: python

    canvas = toyplot.Canvas(width=700)
    axes = canvas.axes(grid=(2,2,0), xscale="log")
    axes.plot(x, x)
    axes = canvas.axes(grid=(2,2,1), xscale="log10")
    axes.plot(x, x)
    axes = canvas.axes(grid=(2,2,2), xscale=("log", 10))
    axes.plot(x, x);



.. raw:: html

    <div align="center" class="toyplot" id="t0378efb8b5ce45ff92057f311d6c328f"><svg height="700.0px" id="tf6e0ab6ee15245e78d4e4cc377cc5e0e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 700.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t423df3bd62c04ebca999160574b1c452"><clipPath id="t35581fe140b64a57939d7803c6a64069"><rect height="270.0" width="270.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t35581fe140b64a57939d7803c6a64069)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="ta46e53cfec114319ac8d9db4de7e8f0e" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 300.0 L 50.603274069759877 294.89795918367344 L 51.23278554177233 289.79591836734693 L 51.890920814964247 284.69387755102042 L 52.58040744362593 279.59183673469386 L 53.304382433400477 274.48979591836735 L 54.066478532050624 269.38775510204084 L 54.870934522607939 264.28571428571428 L 55.722738005020879 259.18367346938777 L 56.627812873141366 254.08163265306121 L 57.59326940431859 248.9795918367347 L 58.627743862317551 243.87755102040816 L 59.741869045215864 238.77551020408163 L 60.948941467030693 233.67346938775512 L 62.265892843153139 228.57142857142856 L 63.714749302522819 223.46938775510205 L 65.324905288341327 218.36734693877554 L 67.136827365761079 213.265306122449 L 69.208424257389225 208.16326530612247 L 71.626779829009621 203.06122448979593 L 74.531785686306293 197.95918367346937 L 78.169934667141888 192.85714285714283 L 83.040869189749827 187.75510204081633 L 90.435827510295027 182.65306122448982 L 106.33986933428378 177.55102040816328 L 243.66013066571622 172.44897959183672 L 259.56417248970496 167.34693877551021 L 266.95913081025014 162.24489795918367 L 271.83006533285811 157.14285714285717 L 275.46821431369369 152.0408163265306 L 278.37322017099041 146.9387755102041 L 280.79157574261075 141.83673469387756 L 282.86317263423894 136.73469387755102 L 284.67509471165869 131.63265306122449 L 286.28525069747718 126.53061224489797 L 287.73410715684685 121.42857142857144 L 289.05105853296931 116.32653061224491 L 290.25813095478418 111.22448979591839 L 291.37225613768243 106.12244897959184 L 292.40673059568138 101.0204081632653 L 293.37218712685865 95.918367346938794 L 294.27726199497914 90.816326530612258 L 295.12906547739209 85.714285714285722 L 295.93352146794939 80.612244897959187 L 296.69561756659948 75.510204081632651 L 297.41959255637408 70.408163265306115 L 298.10907918503574 65.306122448979607 L 298.76721445822767 60.204081632653072 L 299.39672593024011 55.102040816326536 L 300.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="200.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="245.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tabb2e22adb494034b8e0702256140014" transform="translate(50.0,310.0) rotate(0.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-10 ³</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(33.33333333333333,0) rotate(0)" x="0" y="0">-10 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">-10 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">-10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(183.33333333333334,0) rotate(0)" x="0" y="0">10 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(216.66666666666666,0) rotate(0)" x="0" y="0">10 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">10 ³</text></g></g><g class="toyplot-axes-Axis" id="t795e952717cf489d85b342004a3643ec" transform="translate(40.0,300.0) rotate(-90.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0) rotate(0)" x="0" y="0">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0) rotate(0)" x="0" y="0">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1000</text></g></g></g><g class="toyplot-axes-Cartesian" id="tad9f289d277f4a44acaeb320c9c49959"><clipPath id="t8641f8ea300e46d093e63217e8e77295"><rect height="270.0" width="270.0" x="390.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t8641f8ea300e46d093e63217e8e77295)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="390.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tf993b59521814d6a91eda61c23af6482" style="fill:none"><g class="toyplot-Series"><path d="M 400.0 300.0 L 400.60327406975989 294.89795918367344 L 401.23278554177233 289.79591836734693 L 401.89092081496426 284.69387755102042 L 402.58040744362592 279.59183673469386 L 403.30438243340046 274.48979591836735 L 404.06647853205061 269.38775510204084 L 404.87093452260797 264.28571428571428 L 405.72273800502091 259.18367346938777 L 406.62781287314141 254.08163265306121 L 407.59326940431862 248.9795918367347 L 408.62774386231757 243.87755102040816 L 409.74186904521588 238.77551020408163 L 410.94894146703069 233.67346938775512 L 412.2658928431531 228.57142857142856 L 413.71474930252282 223.46938775510205 L 415.32490528834131 218.36734693877554 L 417.13682736576106 213.265306122449 L 419.2084242573892 208.16326530612247 L 421.62677982900965 203.06122448979593 L 424.53178568630631 197.95918367346937 L 428.16993466714189 192.85714285714283 L 433.04086918974986 187.75510204081633 L 440.43582751029504 182.65306122448982 L 456.33986933428378 177.55102040816328 L 593.66013066571622 172.44897959183672 L 609.5641724897049 167.34693877551021 L 616.95913081025014 162.24489795918367 L 621.83006533285811 157.14285714285717 L 625.46821431369381 152.0408163265306 L 628.37322017099041 146.9387755102041 L 630.7915757426108 141.83673469387756 L 632.86317263423894 136.73469387755102 L 634.67509471165863 131.63265306122449 L 636.28525069747718 126.53061224489797 L 637.7341071568469 121.42857142857144 L 639.05105853296936 116.32653061224491 L 640.25813095478418 111.22448979591839 L 641.37225613768248 106.12244897959184 L 642.40673059568132 101.0204081632653 L 643.37218712685853 95.918367346938794 L 644.2772619949792 90.816326530612258 L 645.12906547739215 85.714285714285722 L 645.93352146794939 80.612244897959187 L 646.69561756659948 75.510204081632651 L 647.41959255637403 70.408163265306115 L 648.10907918503574 65.306122448979607 L 648.76721445822773 60.204081632653072 L 649.39672593024011 55.102040816326536 L 650.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t6b1312ad718947db8b2c122795ee26f3" transform="translate(400.0,310.0) rotate(0.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-10 ³</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(33.33333333333333,0) rotate(0)" x="0" y="0">-10 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">-10 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">-10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(183.33333333333334,0) rotate(0)" x="0" y="0">10 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(216.66666666666666,0) rotate(0)" x="0" y="0">10 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">10 ³</text></g></g><g class="toyplot-axes-Axis" id="te5dc68463c5a4cf6973ae03bc2d0a913" transform="translate(390.0,300.0) rotate(-90.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0) rotate(0)" x="0" y="0">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0) rotate(0)" x="0" y="0">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1000</text></g></g></g><g class="toyplot-axes-Cartesian" id="t8d44fb179e2d4c9791f0ce8ff8376902"><clipPath id="t3f75467c42e7415c845133a9be87d02b"><rect height="270.0" width="270.0" x="40.0" y="390.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t3f75467c42e7415c845133a9be87d02b)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="40.0" y="390.0"></rect><g class="toyplot-mark-Plot" id="t5d365b48ea1745f69825974d5009e4c5" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 650.0 L 50.603274069759877 644.89795918367338 L 51.23278554177233 639.79591836734699 L 51.890920814964247 634.69387755102048 L 52.58040744362593 629.59183673469386 L 53.304382433400477 624.48979591836735 L 54.066478532050624 619.38775510204084 L 54.870934522607939 614.28571428571422 L 55.722738005020879 609.18367346938783 L 56.627812873141366 604.08163265306121 L 57.59326940431859 598.9795918367347 L 58.627743862317551 593.87755102040819 L 59.741869045215864 588.77551020408157 L 60.948941467030693 583.67346938775518 L 62.265892843153139 578.57142857142856 L 63.714749302522819 573.46938775510205 L 65.324905288341327 568.36734693877554 L 67.136827365761079 563.26530612244903 L 69.208424257389225 558.16326530612241 L 71.626779829009621 553.0612244897959 L 74.531785686306293 547.9591836734694 L 78.169934667141888 542.85714285714278 L 83.040869189749827 537.75510204081627 L 90.435827510295027 532.65306122448987 L 106.33986933428378 527.55102040816325 L 243.66013066571622 522.44897959183675 L 259.56417248970496 517.34693877551024 L 266.95913081025014 512.24489795918362 L 271.83006533285811 507.14285714285717 L 275.46821431369369 502.0408163265306 L 278.37322017099041 496.9387755102041 L 280.79157574261075 491.83673469387759 L 282.86317263423894 486.73469387755108 L 284.67509471165869 481.63265306122446 L 286.28525069747718 476.53061224489795 L 287.73410715684685 471.42857142857144 L 289.05105853296931 466.32653061224494 L 290.25813095478418 461.22448979591843 L 291.37225613768243 456.12244897959187 L 292.40673059568138 451.0204081632653 L 293.37218712685865 445.91836734693879 L 294.27726199497914 440.81632653061223 L 295.12906547739209 435.71428571428572 L 295.93352146794939 430.61224489795921 L 296.69561756659948 425.51020408163265 L 297.41959255637408 420.40816326530614 L 298.10907918503574 415.30612244897964 L 298.76721445822767 410.20408163265307 L 299.39672593024011 405.10204081632651 L 300.0 400.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="200.0" y="410.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="245.0" y="417.0"></text></g><g class="toyplot-axes-Axis" id="te2328c6d83e74be99317f0750a6394e8" transform="translate(50.0,660.0) rotate(0.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-10 ³</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(33.33333333333333,0) rotate(0)" x="0" y="0">-10 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">-10 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">-10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">10 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(183.33333333333334,0) rotate(0)" x="0" y="0">10 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(216.66666666666666,0) rotate(0)" x="0" y="0">10 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">10 ³</text></g></g><g class="toyplot-axes-Axis" id="tf99a78e0f902492b89fa85ef563d49e9" transform="translate(40.0,650.0) rotate(-90.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(62.5,0) rotate(0)" x="0" y="0">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(187.5,0) rotate(0)" x="0" y="0">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1000</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t0378efb8b5ce45ff92057f311d6c328f text");
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
          var text = document.querySelectorAll("#t0378efb8b5ce45ff92057f311d6c328f text");
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
      var data_tables = [{"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "ta46e53cfec114319ac8d9db4de7e8f0e", "filename": "toyplot"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tf993b59521814d6a91eda61c23af6482", "filename": "toyplot"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t5d365b48ea1745f69825974d5009e4c5", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t0378efb8b5ce45ff92057f311d6c328f .toyplot-mark-popup");
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
      var axes = {"t423df3bd62c04ebca999160574b1c452": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 150.0, "min": -Infinity}, "max": 150.0, "min": 50.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 200.0, "min": 150.0}, "max": 200.0, "min": 150.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 200.0}, "max": 300.0, "min": 200.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 300.0}, "scale": "linear"}]}, "t8d44fb179e2d4c9791f0ce8ff8376902": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 150.0, "min": -Infinity}, "max": 150.0, "min": 50.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 200.0, "min": 150.0}, "max": 200.0, "min": 150.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 200.0}, "max": 300.0, "min": 200.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 400.0, "min": 650.0}, "scale": "linear"}]}, "tad9f289d277f4a44acaeb320c9c49959": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 500.0, "min": -Infinity}, "max": 500.0, "min": 400.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 550.0, "min": 500.0}, "max": 550.0, "min": 500.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 550.0}, "max": 650.0, "min": 550.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 300.0}, "scale": "linear"}]}};
    
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


Of course, you are free to specify any base you like, using the tuple
notation:

.. code:: python

    toyplot.plot(x, x, xscale=("log", 4), width=400);



.. raw:: html

    <div align="center" class="toyplot" id="t158984fdf4d14f26bb942568648b80ea"><svg height="400.0px" id="tf665e05d3d4940019ee2075e7f367e26" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 400.0 400.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="te14f7e14b6fa42c085cb7af366768baa"><clipPath id="t12213230a1284f02a9261dcfac8fe13c"><rect height="320.0" width="320.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t12213230a1284f02a9261dcfac8fe13c)" style="cursor:crosshair"><rect height="320.0" style="pointer-events:all;visibility:hidden" width="320.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t96b06b8181fc49dba5d2465123e3fd66" style="fill:none"><g class="toyplot-Series"><path d="M 50.410588584054956 350.0 L 51.132040493305816 343.87755102040813 L 51.884869557481359 337.75510204081633 L 52.671929657012285 331.63265306122452 L 53.49648265802044 325.51020408163265 L 54.362280087090461 319.38775510204079 L 55.273666325890076 313.26530612244892 L 56.23571051009786 307.14285714285717 L 57.254377281136016 301.02040816326536 L 58.336750988794947 294.89795918367349 L 59.491334771906594 288.77551020408163 L 60.728456687475848 282.65306122448982 L 62.060832436140743 276.53061224489795 L 63.504363240753307 270.40816326530614 L 65.079297640092335 264.28571428571428 L 66.81197655211443 258.16326530612247 L 68.737552618433369 252.04081632653066 L 70.904419566135232 245.91836734693879 L 73.381830095744363 239.79591836734696 L 76.273927289789867 233.67346938775509 L 79.748006696129693 227.55102040816325 L 84.098847648746215 221.42857142857142 L 89.923969574789112 215.30612244897958 L 98.767556704783573 209.18367346938777 L 117.78710671343744 203.06122448979593 L 282.21289328656258 196.93877551020407 L 301.2324432952164 190.81632653061226 L 310.07603042521089 184.69387755102042 L 315.90115235125381 178.57142857142856 L 320.25199330387028 172.44897959183675 L 323.72607271021013 166.32653061224494 L 326.61816990425564 160.20408163265307 L 329.09558043386471 154.08163265306123 L 331.26244738156663 147.9591836734694 L 333.1880234478856 141.83673469387753 L 334.92070235990769 135.71428571428572 L 336.49563675924668 129.59183673469391 L 337.93916756385926 123.46938775510206 L 339.27154331252416 117.34693877551021 L 340.50866522809338 111.22448979591837 L 341.66324901120504 105.10204081632656 L 342.74562271886401 98.979591836734713 L 343.76428948990213 92.857142857142861 L 344.72633367410992 86.734693877551024 L 345.63771991290952 80.612244897959187 L 346.50351734197955 74.489795918367349 L 347.32807034298776 68.36734693877554 L 348.11513044251865 62.244897959183689 L 348.86795950669421 56.122448979591844 L 349.58941141594505 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="250.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="295.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t706df3b44c72465cb77a2ab3478c1f10" transform="translate(50.0,360.0) rotate(0.0)"><line style="" x1="0.41058858405495613" x2="299.58941141594505" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-4 ⁵</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(24.0,0) rotate(0)" x="0" y="0">-4 ⁴</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(48.0,0) rotate(0)" x="0" y="0">-4 ³</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(72.0,0) rotate(0)" x="0" y="0">-4 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(96.0,0) rotate(0)" x="0" y="0">-4 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">-4 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(180.0,0) rotate(0)" x="0" y="0">4 ⁰</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.0,0) rotate(0)" x="0" y="0">4 ¹</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(228.0,0) rotate(0)" x="0" y="0">4 ²</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(252.0,0) rotate(0)" x="0" y="0">4 ³</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(276.0,0) rotate(0)" x="0" y="0">4 ⁴</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,0) rotate(0)" x="0" y="0">4 ⁵</text></g></g><g class="toyplot-axes-Axis" id="t5666c342794a42eea4d597d11f4f5bdb" transform="translate(40.0,350.0) rotate(-90.0)"><line style="" x1="0" x2="300.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(75.0,0) rotate(0)" x="0" y="0">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(225.0,0) rotate(0)" x="0" y="0">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,0) rotate(0)" x="0" y="0">1000</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t158984fdf4d14f26bb942568648b80ea text");
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
          var text = document.querySelectorAll("#t158984fdf4d14f26bb942568648b80ea text");
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
      var data_tables = [{"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t96b06b8181fc49dba5d2465123e3fd66", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t158984fdf4d14f26bb942568648b80ea .toyplot-mark-popup");
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
      var axes = {"te14f7e14b6fa42c085cb7af366768baa": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1024.0}, "range": {"bounds": {"max": 170.0, "min": -Infinity}, "max": 170.0, "min": 50.0}, "scale": ["log", 4]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 230.0, "min": 170.0}, "max": 230.0, "min": 170.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1024.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 230.0}, "max": 350.0, "min": 230.0}, "scale": ["log", 4]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 350.0}, "scale": "linear"}]}};
    
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


Shared Axes
-----------

It may occasionally be useful to display multiple domains in a single
plot, although this is a technique that should be used with care to
avoid confusion when your plot is viewed by others. For example,
consider the following data:

.. code:: python

    import toyplot.data
    data = toyplot.data.read_csv("deliveries.csv")
    data[5:10]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">Date</th><th style="text-align:left;border:none;padding-right:1em;">Delivered</th><th style="text-align:left;border:none;padding-right:1em;">On Time</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">15jul2005</td><td style="border:none;padding-right:1em;">306</td><td style="border:none;padding-right:1em;">1.0000</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">15aug2005</td><td style="border:none;padding-right:1em;">323</td><td style="border:none;padding-right:1em;">0.9905</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">15sep2005</td><td style="border:none;padding-right:1em;">531</td><td style="border:none;padding-right:1em;">0.9959</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">15oct2005</td><td style="border:none;padding-right:1em;">677</td><td style="border:none;padding-right:1em;">0.9600</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">15nov2005</td><td style="border:none;padding-right:1em;">695</td><td style="border:none;padding-right:1em;">0.9624</td></tr></table>



The ``Delivered`` and ``On Time`` series have completely different
domains, and it would make little sense to plot counts and percentages
on a single set of axes. But with shared axes you can display the data
using a separate Y axis for each series:

.. code:: python

    data["Delayed"] = 1.0 - data["On Time"].astype("float64")
    
    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes(xlabel="Date", ylabel="Deliveries", ymin=0)
    axes.plot(data["Delivered"], color="darkred", marker="o")
    axes.y.spine.style = {"stroke":"darkred"}
    
    axes = axes.share("x", ylabel="% Delayed", ymax=0.1)
    axes.plot(data["Delayed"].astype("float64"), color="steelblue", marker="o")
    axes.y.spine.style = {"stroke":"steelblue"}



.. raw:: html

    <div align="center" class="toyplot" id="t01a55b6e7e0946839acaf021d06f3fd3"><svg height="300.0px" id="t39a1c947452a4caca33ef471c8bda531" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t426d6243881c4c6b998aac97997cbd11"><clipPath id="t5a0ac063b6f64e1c93e103d23dd0bd23"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t5a0ac063b6f64e1c93e103d23dd0bd23)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="520.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="td793d4bc887d4bf4acf83ebea7788d22" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 127.11111111111111 L 91.666666666666657 137.33333333333331 L 133.33333333333331 119.77777777777779 L 175.0 141.55555555555554 L 216.66666666666666 160.22222222222223 L 258.33333333333337 181.99999999999997 L 300.0 178.22222222222223 L 341.66666666666669 132.0 L 383.33333333333331 99.555555555555557 L 425.0 95.555555555555543 L 466.66666666666669 57.333333333333329 L 508.33333333333331 126.22222222222221" style="fill:none;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="50.0" cy="127.11111111111111" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="91.666666666666657" cy="137.33333333333331" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="133.33333333333331" cy="119.77777777777779" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="175.0" cy="141.55555555555554" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="216.66666666666666" cy="160.22222222222223" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="258.33333333333337" cy="181.99999999999997" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="300.0" cy="178.22222222222223" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="341.66666666666669" cy="132.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="383.33333333333331" cy="99.555555555555557" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="425.0" cy="95.555555555555543" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="466.66666666666669" cy="57.333333333333329" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0"><circle cx="508.33333333333331" cy="126.22222222222221" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="ta2f5d0896aa146e58c5b280969b3754a" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="458.3333333333333" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(166.66666666666666,0) rotate(0)" x="0" y="0">4</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(333.3333333333333,0) rotate(0)" x="0" y="0">8</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">12</text></g></g><g class="toyplot-axes-Axis" id="tc9714d838816454bad77c026b74c1723" transform="translate(40.0,250.0) rotate(-90.0)"><line style="stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0" x1="68.0" x2="192.66666666666669" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">300</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0) rotate(0)" x="0" y="0">600</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">900</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" x="100.0" y="0">Deliveries</text></g></g><g class="toyplot-axes-Cartesian" id="tf23c654379304ae9a6965b9f1e735d3c"><clipPath id="ta7b5ce71712940e5ad477a9492a28bf1"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta7b5ce71712940e5ad477a9492a28bf1)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="520.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="te8c2e2f64ee7466c935440e2118a6550" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 91.666666666666657 250.0 L 133.33333333333331 250.0 L 175.0 250.0 L 216.66666666666666 250.0 L 258.33333333333337 250.0 L 300.0 231.00000000000009 L 341.66666666666669 241.80000000000001 L 383.33333333333331 169.99999999999994 L 425.0 174.80000000000007 L 466.66666666666669 95.800000000000111 L 508.33333333333331 227.60000000000002" style="fill:none;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="50.0" cy="250.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="91.666666666666657" cy="250.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="133.33333333333331" cy="250.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="175.0" cy="250.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="216.66666666666666" cy="250.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="258.33333333333337" cy="250.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="300.0" cy="231.00000000000009" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="341.66666666666669" cy="241.80000000000001" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="383.33333333333331" cy="169.99999999999994" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="425.0" cy="174.80000000000007" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="466.66666666666669" cy="95.800000000000111" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><circle cx="508.33333333333331" cy="227.60000000000002" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t179580e24c4741a8a9c954ed199bfab0" transform="translate(560.0,250.0) rotate(-90.0)"><line style="stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0" x1="0" x2="154.1999999999999" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.00</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.05</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">0.10</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="100.0" y="0">% Delayed</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t01a55b6e7e0946839acaf021d06f3fd3 text");
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
          var text = document.querySelectorAll("#t01a55b6e7e0946839acaf021d06f3fd3 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [553.0, 507.0, 586.0, 488.0, 404.0, 306.0, 323.0, 531.0, 677.0, 695.0, 867.0, 557.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "td793d4bc887d4bf4acf83ebea7788d22", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.009499999999999953, 0.0040999999999999925, 0.040000000000000036, 0.03759999999999997, 0.07709999999999995, 0.011199999999999988]], "title": "Plot Data", "names": ["x", "y0"], "id": "te8c2e2f64ee7466c935440e2118a6550", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t01a55b6e7e0946839acaf021d06f3fd3 .toyplot-mark-popup");
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
      var axes = {"t426d6243881c4c6b998aac97997cbd11": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 12.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 900.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "tf23c654379304ae9a6965b9f1e735d3c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 12.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.10000000000000001, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


For this example, we created a set of axes for the first series, then
used the :func:`toyplot.axes.Cartesian.share` function to create a
second set of overlapping axes for the second series. Axis sharing in
this case means that Toyplot has created two pairs of overlapping
Cartesian axes, but with a shared X axis. This ensures that any changes
that affect the X axis are reflected in both plots.

Note that we have used color to help reinforce the relationship between
the plots and their axes to avoid confusion.
