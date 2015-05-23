
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

    <div align="center" class="toyplot" id="tcbda594c1374491b878b8043d1d8916f"><svg height="300.0px" id="t47e05c8b48214af59172e899d89c65c4" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t37b86849a51446e49de3bffd998e1ac9"><clipPath id="tf6954eba264a4cbe8f31e84ebaf8fb22"><rect height="200.0" width="200.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf6954eba264a4cbe8f31e84ebaf8fb22)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="tf113d0fd9f3a48c4b2db647dc6a5b1d7" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tcbda594c1374491b878b8043d1d8916f text");
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
          var text = document.querySelectorAll("#tcbda594c1374491b878b8043d1d8916f text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"], "id": "tf113d0fd9f3a48c4b2db647dc6a5b1d7", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tcbda594c1374491b878b8043d1d8916f .toyplot-mark-popup");
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
      var axes = {"t37b86849a51446e49de3bffd998e1ac9": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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
data:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes1 = canvas.axes(grid=(1, 2, 0))
    axes1.plot(y)
    axes2 = canvas.axes(grid=(1, 2, 1))
    axes2.plot(1 - y);



.. raw:: html

    <div align="center" class="toyplot" id="t80edca86180443f7a20ee235eb876d91"><svg height="300.0px" id="t632c627725454abc94ea16970dc2099e" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t04f0e810098b4cda99643bb984b69234"><clipPath id="tcef1f0a294d04e8f8119ba26415e1fff"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tcef1f0a294d04e8f8119ba26415e1fff)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tfd53c5a40672453b80efe0abd65bbaba" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.50138504155126 L 78.0 238.00554016620501 L 87.0 235.51246537396122 L 96.0 232.02216066481992 L 105.0 227.53462603878117 L 114.0 222.04986149584488 L 123.0 215.56786703601105 L 132.0 208.0886426592798 L 141.0 199.61218836565098 L 150.0 190.13850415512465 L 159.0 179.66759002770081 L 168.0 168.19944598337952 L 177.0 155.73407202216069 L 186.0 142.27146814404435 L 195.0 127.81163434903047 L 204.0 112.35457063711914 L 213.0 95.900277008310283 L 222.0 78.448753462603904 L 231.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="105.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">20</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="tfdb8bfa7fbde4346a24cc8d2b0deb626"><clipPath id="t28e96fbc71254fcf99db4f775f814a16"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t28e96fbc71254fcf99db4f775f814a16)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t09aa42c974e2442f989ed90ef7d50603" style="fill:none"><g class="toyplot-Series"><path d="M 360.0 60.0 L 369.0 60.498614958448755 L 378.0 61.99445983379502 L 387.0 64.48753462603878 L 396.0 67.97783933518005 L 405.0 72.46537396121883 L 414.0 77.95013850415512 L 423.0 84.43213296398892 L 432.0 91.911357340720215 L 441.0 100.38781163434902 L 450.0 109.86149584487535 L 459.0 120.33240997229916 L 468.0 131.80055401662048 L 477.0 144.26592797783931 L 486.0 157.72853185595568 L 495.0 172.18836565096953 L 504.0 187.64542936288086 L 513.0 204.0997229916897 L 522.0 221.55124653739611 L 531.0 240.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="531.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="405.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="250.0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">20</text></g><line style="" x1="350.0" x2="350.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 240.0)" x="350.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 150.0)" x="350.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 350.0, 60.0)" x="350.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t80edca86180443f7a20ee235eb876d91 text");
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
          var text = document.querySelectorAll("#t80edca86180443f7a20ee235eb876d91 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0], [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"], "id": "tfd53c5a40672453b80efe0abd65bbaba", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1.0, 0.997229916897507, 0.9889196675900277, 0.9750692520775623, 0.9556786703601108, 0.9307479224376731, 0.9002770083102494, 0.8642659279778393, 0.8227146814404432, 0.775623268698061, 0.7229916897506925, 0.6648199445983379, 0.6011080332409973, 0.5318559556786705, 0.4570637119113574, 0.3767313019390581, 0.29085872576177296, 0.1994459833795016, 0.1024930747922439, 0.0], [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"], "id": "t09aa42c974e2442f989ed90ef7d50603", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t80edca86180443f7a20ee235eb876d91 .toyplot-mark-popup");
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
      var axes = {"t04f0e810098b4cda99643bb984b69234": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "tfdb8bfa7fbde4346a24cc8d2b0deb626": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


The *grid* argument allows us to easily position each set of axes on a
regular grid that covers the canvas. Note that you can control the axes
position on the grid in a variety of ways:

-  (rows, columns, n)

   -  fill cell :math:`n` (in left-to-right, top-to-bottom order) of an
      :math:`M \times N` grid.

-  (rows, columns, i, j)

   -  fill cell :math:`i,j` of an :math:`M \times N` grid.

-  (rows, columns, i, rowspan, j, colspan)

   -  fill cells :math:`[i, i + rowspan), [j, j + colspan)` of an
      :math:`M \times N` grid.

You can also use the *gutter* argument to control the space between
cells in the grid. For example, to create a complex layout with minimal
separation between grid cells:

.. code:: python

    canvas = toyplot.Canvas(400, 400)
    axes = canvas.axes(grid=(3, 3, 0, 0), gutter=15) # Upper-left cell
    axes = canvas.axes(grid=(3, 3, 2, 2), gutter=15) # Lower-right cell
    axes = canvas.axes(grid=(3, 3, 0, 1, 1, 2), gutter=15) # Upper-right 1x2 cells
    axes = canvas.axes(grid=(3, 3, 1, 2, 0, 2), gutter=15) # Lower-left 2x2 cells



.. raw:: html

    <div align="center" class="toyplot" id="t18156cc451f44c47979097bcae3cc61a"><svg height="400.0px" id="t83123c0850d049da8895547be2714741" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t89db1b066f13471abe01b4f9fd6abc71"><clipPath id="te8393ee59efb46c392640f1eccfe6b98"><rect height="103.33333333333334" width="103.33333333333334" x="15.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te8393ee59efb46c392640f1eccfe6b98)" style="cursor:crosshair"><rect height="103.33333333333334" style="pointer-events:all;visibility:hidden" width="103.33333333333334" x="15.0" y="15.0"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="18.333333333333343" y="25.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="63.33333333333334" y="32.0"></text></g><line style="" x1="15.0" x2="118.33333333333334" y1="118.33333333333334" y2="118.33333333333334"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="25.0" y="118.33333333333334">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="66.66666666666667" y="118.33333333333334">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="108.33333333333334" y="118.33333333333334">0.5</text></g><line style="" x1="15.0" x2="15.0" y1="15.0" y2="118.33333333333334"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 108.33333333333334)" x="15.0" y="108.33333333333334">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 66.66666666666667)" x="15.0" y="66.66666666666667">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 25.0)" x="15.0" y="25.0">0.5</text></g></g><g class="toyplot-axes-Cartesian" id="t7af70aa7885b4d44a5ab45f2829ce68d"><clipPath id="t783634ab514a40009f64d3a9df7bc128"><rect height="103.33333333333331" width="103.33333333333331" x="281.6666666666667" y="281.6666666666667"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t783634ab514a40009f64d3a9df7bc128)" style="cursor:crosshair"><rect height="103.33333333333331" style="pointer-events:all;visibility:hidden" width="103.33333333333331" x="281.6666666666667" y="281.6666666666667"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="285.0" y="291.6666666666667"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.0" y="298.6666666666667"></text></g><line style="" x1="281.6666666666667" x2="385.0" y1="385.0" y2="385.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="291.6666666666667" y="385.0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="333.33333333333337" y="385.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="375.0" y="385.0">0.5</text></g><line style="" x1="281.6666666666667" x2="281.6666666666667" y1="281.6666666666667" y2="385.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 281.6666666666667, 375.0)" x="281.6666666666667" y="375.0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 281.6666666666667, 333.33333333333337)" x="281.6666666666667" y="333.33333333333337">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 281.6666666666667, 291.6666666666667)" x="281.6666666666667" y="291.6666666666667">0.5</text></g></g><g class="toyplot-axes-Cartesian" id="t7c9d312dc30a464c94873a4c3be53af5"><clipPath id="tcdfd2c83330a4016a9735e6b7a0b4431"><rect height="103.33333333333334" width="236.66666666666666" x="148.33333333333334" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tcdfd2c83330a4016a9735e6b7a0b4431)" style="cursor:crosshair"><rect height="103.33333333333334" style="pointer-events:all;visibility:hidden" width="236.66666666666666" x="148.33333333333334" y="15.0"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="285.0" y="25.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="330.0" y="32.0"></text></g><line style="" x1="148.33333333333334" x2="385.0" y1="118.33333333333334" y2="118.33333333333334"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="158.33333333333334" y="118.33333333333334">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="266.6666666666667" y="118.33333333333334">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="375.0" y="118.33333333333334">0.5</text></g><line style="" x1="148.33333333333334" x2="148.33333333333334" y1="15.0" y2="118.33333333333334"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 148.33333333333334, 108.33333333333334)" x="148.33333333333334" y="108.33333333333334">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 148.33333333333334, 66.66666666666667)" x="148.33333333333334" y="66.66666666666667">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 148.33333333333334, 25.0)" x="148.33333333333334" y="25.0">0.5</text></g></g><g class="toyplot-axes-Cartesian" id="t12bc675627b7435099ee99f3427ec1a8"><clipPath id="taef11709756349d6bb033d9426099d02"><rect height="236.66666666666666" width="236.66666666666669" x="15.0" y="148.33333333333334"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#taef11709756349d6bb033d9426099d02)" style="cursor:crosshair"><rect height="236.66666666666666" style="pointer-events:all;visibility:hidden" width="236.66666666666669" x="15.0" y="148.33333333333334"></rect></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="151.66666666666669" y="158.33333333333334"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="196.66666666666669" y="165.33333333333334"></text></g><line style="" x1="15.0" x2="251.66666666666669" y1="385.0" y2="385.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="25.0" y="385.0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="133.33333333333334" y="385.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="241.66666666666669" y="385.0">0.5</text></g><line style="" x1="15.0" x2="15.0" y1="148.33333333333334" y2="385.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 375.0)" x="15.0" y="375.0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 266.6666666666667)" x="15.0" y="266.6666666666667">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 158.33333333333334)" x="15.0" y="158.33333333333334">0.5</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t18156cc451f44c47979097bcae3cc61a text");
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
          var text = document.querySelectorAll("#t18156cc451f44c47979097bcae3cc61a text");
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
      var axes = {"t12bc675627b7435099ee99f3427ec1a8": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 241.66666666666669, "min": 25.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 158.33333333333334, "min": 375.0}, "scale": "linear"}]}, "t7af70aa7885b4d44a5ab45f2829ce68d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 375.0, "min": 291.6666666666667}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 291.6666666666667, "min": 375.0}, "scale": "linear"}]}, "t7c9d312dc30a464c94873a4c3be53af5": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 375.0, "min": 158.33333333333334}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 25.0, "min": 108.33333333333334}, "scale": "linear"}]}, "t89db1b066f13471abe01b4f9fd6abc71": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 108.33333333333334, "min": 25.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 25.0, "min": 108.33333333333334}, "scale": "linear"}]}};
    
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
-  axes.x.label.text - optional label below the X axis.
-  axes.x.label.style - styles the X axis label.
-  axes.x.spine.show - set to *False* to hide the X axis spine.
-  axes.x.spine.position - set to "low", "high", or a Y axis domain
   value to position the spine. Defaults to "low".
-  axes.x.spine.style - styles the X axis spine.
-  axes.x.ticks.show - set to *True* to display X axis tick marks.
-  axes.x.ticks.locator - :py:class:`toyplot.locator.Basic`,
   :py:class:`toyplot.locator.Extended`,
   :py:class:`toyplot.locator.Explicit`,
   :py:class:`toyplot.locator.Heckbert`,
   :py:class:`toyplot.locator.PositiveLog`,
   :py:class:`toyplot.locator.NegativeLog`, or
   :py:class:`toyplot.locator.SymmetricLog` to control the positioning
   and formatting of ticks and tick labels. By default, an appropriate
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

    <div align="center" class="toyplot" id="tfbb27ddc47b44acda5e2223251f66719"><svg height="300.0px" id="td4421fe2985f41f2a64626aed5f5eb3e" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t7e3881dac24c49cda76637d9a01439ee"><clipPath id="t4a108a5dc1b24631b44a02c9e6b34886"><rect height="200.0" width="500.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t4a108a5dc1b24631b44a02c9e6b34886)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t02eba8cfba2346bab2165b416a3652a4" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 150.0 L 69.795918367346943 138.49105544839446 L 79.591836734693871 127.17108744814433 L 89.387755102040813 116.22596956085634 L 99.183673469387742 105.83542031964561 L 108.97959183673468 96.170052255790551 L 118.77551020408163 87.388570445686213 L 128.57142857142856 79.635166577877328 L 138.36734693877551 73.037151329518849 L 148.16326530612244 67.702863928576889 L 157.95918367346937 63.719893226700549 L 167.75510204081633 61.153639492699497 L 177.55102040816325 60.04624054193809 L 187.34693877551018 60.415879834572159 L 197.14285714285714 62.256487903635886 L 206.9387755102041 65.537842015521576 L 216.73469387755102 70.20606242642998 L 226.53061224489795 76.18449708627395 L 236.32653061224488 83.374980263221573 L 246.12244897959181 91.659444422299003 L 255.91836734693874 100.90185889105058 L 265.71428571428572 110.95046347941975 L 275.51020408163265 121.64026037787411 L 285.30612244897958 132.79572341687648 L 295.10204081632651 144.23368020173581 L 304.89795918367349 155.76631979826411 L 314.69387755102036 167.20427658312349 L 324.48979591836735 178.3597396221258 L 334.28571428571428 189.04953652058023 L 344.08163265306121 199.09814110894936 L 353.87755102040819 208.34055557770094 L 363.67346938775506 216.6250197367784 L 373.46938775510199 223.81550291372602 L 383.26530612244892 229.79393757357002 L 393.0612244897959 234.46215798447844 L 402.85714285714289 237.74351209636413 L 412.65306122448976 239.58412016542783 L 422.44897959183675 239.95375945806191 L 432.24489795918362 238.84636050730055 L 442.0408163265306 236.28010677329945 L 451.83673469387747 232.29713607142313 L 461.63265306122446 226.96284867048118 L 471.42857142857139 220.3648334221227 L 481.22448979591832 212.61142955431384 L 491.0204081632653 203.82994774420948 L 500.81632653061223 194.16457968035448 L 510.61224489795916 183.7740304391437 L 520.40816326530603 172.82891255185575 L 530.20408163265301 161.50894455160562 L 540.0 150.00000000000003" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="540.0" y1="250.0" y2="250.0"></line><g><line style="" x1="60.0" x2="60.0" y1="250.0" y2="245.0"></line><line style="" x1="180.0" x2="180.0" y1="250.0" y2="245.0"></line><line style="" x1="300.0" x2="300.0" y1="250.0" y2="245.0"></line><line style="" x1="420.0" x2="420.0" y1="250.0" y2="245.0"></line><line style="" x1="540.0" x2="540.0" y1="250.0" y2="245.0"></line></g><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="180.0" y="250.0">&#960; / 2</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="300.0" y="250.0">&#960;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="420.0" y="250.0">3 &#960; / 2</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">2 &#960;</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="300.0" y="250.0">x</text><line style="" x1="50" x2="50" y1="60.04624054193809" y2="239.9537594580619"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">-1.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 195.0)" x="50" y="195.0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 105.0)" x="50" y="105.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">sin(x)</text><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="300.0" y="50">Trigonometry 101</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tfbb27ddc47b44acda5e2223251f66719 text");
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
          var text = document.querySelectorAll("#tfbb27ddc47b44acda5e2223251f66719 text");
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
      var data_tables = [{"data": [[0.0, 0.1282282715750936, 0.2564565431501872, 0.38468481472528077, 0.5129130863003744, 0.6411413578754679, 0.7693696294505615, 0.8975979010256552, 1.0258261726007487, 1.1540544441758422, 1.2822827157509358, 1.4105109873260295, 1.538739258901123, 1.6669675304762166, 1.7951958020513104, 1.9234240736264039, 2.0516523452014974, 2.179880616776591, 2.3081088883516845, 2.436337159926778, 2.5645654315018716, 2.6927937030769655, 2.821021974652059, 2.9492502462271526, 3.077478517802246, 3.2057067893773397, 3.333935060952433, 3.4621633325275267, 3.5903916041026207, 3.7186198756777142, 3.8468481472528078, 3.9750764188279013, 4.103304690402995, 4.231532961978089, 4.359761233553182, 4.487989505128276, 4.616217776703369, 4.744446048278463, 4.872674319853556, 5.00090259142865, 5.129130863003743, 5.257359134578837, 5.385587406153931, 5.513815677729024, 5.642043949304118, 5.770272220879211, 5.898500492454305, 6.026728764029398, 6.154957035604492, 6.283185307179586], [0.0, 0.127877161684506, 0.25365458390950735, 0.3752670048793741, 0.49071755200393785, 0.5981105304912159, 0.6956825506034864, 0.7818314824680297, 0.8551427630053461, 0.9144126230158124, 0.9586678530366606, 0.9871817834144501, 0.9994862162006879, 0.9953791129491982, 0.9749279121818236, 0.9384684220497604, 0.8865993063730001, 0.8201722545969561, 0.7402779970753157, 0.6482283953077888, 0.545534901210549, 0.43388373911755823, 0.3151082180236208, 0.19115862870137254, 0.06407021998071323, -0.06407021998071254, -0.19115862870137187, -0.3151082180236202, -0.433883739117558, -0.5455349012105485, -0.6482283953077882, -0.7402779970753153, -0.8201722545969556, -0.8865993063730001, -0.9384684220497602, -0.9749279121818235, -0.9953791129491981, -0.9994862162006879, -0.9871817834144503, -0.9586678530366608, -0.9144126230158128, -0.8551427630053465, -0.7818314824680299, -0.6956825506034869, -0.5981105304912162, -0.49071755200393863, -0.3752670048793746, -0.25365458390950835, -0.12787716168450664, -2.4492935982947064e-16], [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"], "id": "t02eba8cfba2346bab2165b416a3652a4", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tfbb27ddc47b44acda5e2223251f66719 .toyplot-mark-popup");
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
      var axes = {"t7e3881dac24c49cda76637d9a01439ee": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 6.2831853071795862, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -1.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="tf2c0ee184a5f472b8b1602c2e34d1587"><svg height="300.0px" id="t4f39f3bd9d004955991bd66f09368ef8" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t23089ff851bd439591e50fccde6c20ec"><clipPath id="tddaa0229dc4043ab9fd728e81b0b7d4e"><rect height="200.0" width="200.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tddaa0229dc4043ab9fd728e81b0b7d4e)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t139ef39d6f5f46f688ceb21fda3acbac" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 61.81818181818182 239.9833041155355 L 63.63636363636364 239.9332164621421 L 65.454545454545467 239.84973703981967 L 67.272727272727266 239.73286584856831 L 69.090909090909093 239.58260288838801 L 70.909090909090907 239.39894815927875 L 72.72727272727272 239.18190166124052 L 74.545454545454547 238.93146339427329 L 76.363636363636374 238.64763335837719 L 78.181818181818187 238.33041155355207 L 80.0 237.97979797979795 L 81.818181818181813 237.59579263711495 L 83.63636363636364 237.17839552550299 L 85.454545454545453 236.72760664496198 L 87.27272727272728 236.24342599549212 L 89.090909090909093 235.72585357709323 L 90.909090909090907 235.17488938976544 L 92.72727272727272 234.59053343350863 L 94.545454545454533 233.9727857083229 L 96.363636363636374 233.32164621420819 L 98.181818181818187 232.63711495116456 L 100.0 231.91919191919192 L 101.81818181818181 231.16787711829033 L 103.63636363636364 230.38317054845979 L 105.45454545454544 229.5650722097003 L 107.27272727272728 228.71358210201186 L 109.09090909090909 227.82870022539444 L 110.90909090909091 226.91042657984806 L 112.72727272727272 225.95876116537275 L 114.54545454545456 224.97370398196847 L 116.36363636363635 223.95525502963517 L 118.18181818181817 222.90341430837302 L 120.00000000000001 221.81818181818181 L 121.81818181818181 220.6995575590617 L 123.63636363636363 219.5475415310126 L 125.45454545454547 218.36213373403456 L 127.27272727272728 217.14333416812752 L 129.09090909090907 215.89114283329161 L 130.90909090909091 214.60555972952668 L 132.72727272727275 213.28658485683277 L 134.54545454545453 211.93421821520997 L 136.36363636363637 210.54845980465814 L 138.18181818181819 209.12930962517743 L 140.0 207.67676767676764 L 141.81818181818181 206.190833959429 L 143.63636363636363 204.67150847316137 L 145.45454545454547 203.11879121796477 L 147.27272727272728 201.53268219383921 L 149.09090909090909 199.91318140078468 L 150.90909090909088 198.26028883880127 L 152.72727272727272 196.57400450788884 L 154.54545454545456 194.85432840804739 L 156.36363636363637 193.10126053927706 L 158.18181818181819 191.31480090157777 L 160.0 189.49494949494948 L 161.81818181818181 187.64170631939228 L 163.63636363636363 185.75507137490609 L 165.45454545454544 183.83504466149094 L 167.27272727272728 181.88162617914685 L 169.09090909090909 179.89481592787379 L 170.90909090909091 177.87461390767174 L 172.72727272727272 175.82102011854079 L 174.54545454545453 173.73403456048084 L 176.36363636363635 171.61365723349195 L 178.18181818181816 169.4598881375741 L 180.00000000000003 167.27272727272725 L 181.81818181818181 165.0521746389515 L 183.63636363636363 162.79823023624675 L 185.45454545454547 160.51089406461304 L 187.27272727272725 158.19016612405042 L 189.09090909090909 155.83604641455881 L 190.90909090909093 153.44853493613826 L 192.72727272727272 151.02763168878874 L 194.54545454545456 148.57333667251024 L 196.36363636363637 146.08564988730279 L 198.18181818181816 143.56457133316638 L 200.0 141.01010101010104 L 201.81818181818181 138.4222389181067 L 203.63636363636363 135.80098505718342 L 205.45454545454547 133.14633942733116 L 207.27272727272725 130.45830202854995 L 209.09090909090907 127.73687286083984 L 210.90909090909091 124.98205192420068 L 212.72727272727272 122.19383921863263 L 214.54545454545456 119.37223474413555 L 216.36363636363637 116.5172385007096 L 218.18181818181816 113.62885048835464 L 220.0 110.7070707070707 L 221.81818181818181 107.75189915685786 L 223.63636363636363 104.76333583771606 L 225.45454545454547 101.7413807496452 L 227.27272727272728 98.686033892645469 L 229.09090909090909 95.597295266716742 L 230.90909090909091 92.475164871859064 L 232.72727272727272 89.319642708072465 L 234.54545454545456 86.130728775356843 L 236.36363636363637 82.908423073712342 L 238.18181818181819 79.652725603138776 L 240.0 76.363636363636374" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="240.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">10</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="250.0">Days</text><line style="" x1="50" x2="50" y1="76.36363636363637" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 223.63636363636365)" x="50" y="223.63636363636365">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 141.8181818181818)" x="50" y="141.8181818181818">100</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">150</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">Users</text><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="50">Toyplot Users</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tf2c0ee184a5f472b8b1602c2e34d1587 text");
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
          var text = document.querySelectorAll("#tf2c0ee184a5f472b8b1602c2e34d1587 text");
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
      var data_tables = [{"data": [[0.0, 0.10101010101010101, 0.20202020202020202, 0.30303030303030304, 0.40404040404040403, 0.5050505050505051, 0.6060606060606061, 0.7070707070707071, 0.8080808080808081, 0.9090909090909091, 1.0101010101010102, 1.1111111111111112, 1.2121212121212122, 1.3131313131313131, 1.4141414141414141, 1.5151515151515151, 1.6161616161616161, 1.7171717171717171, 1.8181818181818181, 1.9191919191919191, 2.0202020202020203, 2.121212121212121, 2.2222222222222223, 2.323232323232323, 2.4242424242424243, 2.525252525252525, 2.6262626262626263, 2.727272727272727, 2.8282828282828283, 2.929292929292929, 3.0303030303030303, 3.131313131313131, 3.2323232323232323, 3.3333333333333335, 3.4343434343434343, 3.5353535353535355, 3.6363636363636362, 3.7373737373737375, 3.8383838383838382, 3.9393939393939394, 4.040404040404041, 4.141414141414141, 4.242424242424242, 4.343434343434343, 4.444444444444445, 4.545454545454545, 4.646464646464646, 4.747474747474747, 4.848484848484849, 4.94949494949495, 5.05050505050505, 5.151515151515151, 5.252525252525253, 5.353535353535354, 5.454545454545454, 5.555555555555555, 5.656565656565657, 5.757575757575758, 5.858585858585858, 5.959595959595959, 6.0606060606060606, 6.161616161616162, 6.262626262626262, 6.363636363636363, 6.4646464646464645, 6.565656565656566, 6.666666666666667, 6.767676767676767, 6.8686868686868685, 6.96969696969697, 7.070707070707071, 7.171717171717171, 7.2727272727272725, 7.373737373737374, 7.474747474747475, 7.575757575757575, 7.6767676767676765, 7.777777777777778, 7.878787878787879, 7.979797979797979, 8.080808080808081, 8.181818181818182, 8.282828282828282, 8.383838383838384, 8.484848484848484, 8.585858585858587, 8.686868686868687, 8.787878787878787, 8.88888888888889, 8.98989898989899, 9.09090909090909, 9.191919191919192, 9.292929292929292, 9.393939393939394, 9.494949494949495, 9.595959595959595, 9.696969696969697, 9.797979797979798, 9.8989898989899, 10.0], [40.0, 40.01020304050607, 40.04081216202428, 40.09182736455464, 40.16324864809713, 40.25507601265177, 40.36730945821855, 40.49994898479747, 40.65299459238853, 40.82644628099173, 41.02030405060708, 41.23456790123457, 41.4692378328742, 41.72431384552597, 41.99979593918988, 42.29568411386593, 42.61197836955413, 42.94867870625446, 43.30578512396694, 43.68329762269156, 44.08121620242832, 44.499540863177224, 44.93827160493827, 45.397408427711454, 45.876951331496784, 46.376900316294254, 46.897255382103864, 47.438016528925615, 47.999183756759514, 48.58075706560555, 49.182736455463726, 49.805121926334046, 50.447913478216506, 51.111111111111114, 51.794714825017856, 52.49872461993674, 53.22314049586777, 53.96796245281094, 54.73319049076625, 55.5188246097337, 56.3248648097133, 57.15131109070502, 57.99816345270891, 58.86542189572492, 59.75308641975309, 60.66115702479338, 61.58963371084583, 62.53851647791042, 63.50780532598715, 64.49750025507602, 65.50760126517702, 66.53810835629017, 67.58902152841547, 68.6603407815529, 69.75206611570248, 70.8641975308642, 71.99673502703806, 73.14967860422406, 74.3230282624222, 75.51678400163249, 76.7309458218549, 77.96551372308949, 79.22048770533618, 80.49586776859505, 81.79165391286602, 83.10784613814917, 84.44444444444446, 85.80144883175186, 87.17885930007142, 88.57667584940313, 89.99489847974696, 91.43352719110294, 92.89256198347107, 94.37200285685134, 95.87184981124375, 97.3921028466483, 98.93276196306499, 100.49382716049382, 102.0752984389348, 103.6771757983879, 105.29945923885319, 106.94214876033058, 108.6052443628201, 110.2887460463218, 111.99265381083562, 113.7169676563616, 115.4616875828997, 117.22681359044994, 119.01234567901236, 120.81828384858687, 122.64462809917353, 124.49137843077237, 126.35853484338332, 128.24609733700643, 130.15406591164168, 132.08244056728904, 134.0312213039486, 136.00040812162024, 137.99000102030408, 140.0], [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"], "id": "t139ef39d6f5f46f688ceb21fda3acbac", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tf2c0ee184a5f472b8b1602c2e34d1587 .toyplot-mark-popup");
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
      var axes = {"t23089ff851bd439591e50fccde6c20ec": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 10.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 40.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


And the same properties can be used with Toyplot's convenience APIs, as
in the following example where we specify a minimum value for an axis -
for example, if we wanted the previous figure to include :math:`y = 0`:

.. code:: python

    toyplot.plot(x, y, label="Toyplot Users", xlabel="Days", ylabel="Users", ymin=0, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="tb4f298e74648488aa867cd6bd652c59a"><svg height="300.0px" id="t9404990cbea3439ab7d7f276d9660d4a" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tad3f97d690eb47459f017f4799dfcd59"><clipPath id="tab2abd0f0dd440658e1d4fd2a20f5160"><rect height="200.0" width="200.0" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tab2abd0f0dd440658e1d4fd2a20f5160)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50" y="50"></rect><g class="toyplot-mark-Plot" id="t4312ce17d30c4afbb69467c9d3fee642" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 192.0 L 61.81818181818182 191.98775635139273 L 63.63636363636364 191.95102540557085 L 65.454545454545467 191.88980716253442 L 67.272727272727266 191.80410162228341 L 69.090909090909093 191.69390878481786 L 70.909090909090907 191.55922865013775 L 72.72727272727272 191.40006121824302 L 74.545454545454547 191.21640648913376 L 76.363636363636374 191.00826446280993 L 78.181818181818187 190.77563513927151 L 80.0 190.5185185185185 L 81.818181818181813 190.23691460055096 L 83.63636363636364 189.93082338536885 L 85.454545454545453 189.60024487297213 L 87.27272727272728 189.24517906336089 L 89.090909090909093 188.86562595653504 L 90.909090909090907 188.46158555249465 L 92.72727272727272 188.03305785123968 L 94.545454545454533 187.58004285277013 L 96.363636363636374 187.102540557086 L 98.181818181818187 186.60055096418733 L 100.0 186.07407407407408 L 101.81818181818181 185.52310988674625 L 103.63636363636364 184.94765840220384 L 105.45454545454544 184.3477196204469 L 107.27272727272728 183.72329354147536 L 109.09090909090909 183.07438016528926 L 110.90909090909091 182.40097949188859 L 112.72727272727272 181.70309152127334 L 114.54545454545456 180.98071625344349 L 116.36363636363635 180.23385368839917 L 118.18181818181817 179.46250382614019 L 120.00000000000001 178.66666666666666 L 121.81818181818181 177.84634220997856 L 123.63636363636363 177.00153045607593 L 125.45454545454547 176.1322314049587 L 127.27272727272728 175.23844505662686 L 129.09090909090907 174.32017141108048 L 130.90909090909091 173.37741046831954 L 132.72727272727275 172.41016222834406 L 134.54545454545453 171.418426691154 L 136.36363636363637 170.40220385674931 L 138.18181818181819 169.36149372513012 L 140.0 168.2962962962963 L 141.81818181818181 167.20661157024793 L 143.63636363636363 166.09243954698499 L 145.45454545454547 164.95378022650749 L 147.27272727272728 163.79063360881543 L 149.09090909090909 162.6029996939088 L 150.90909090909088 161.39087848178758 L 152.72727272727272 160.1542699724518 L 154.54545454545456 158.89317416590143 L 156.36363636363637 157.60759106213649 L 158.18181818181819 156.29752066115705 L 160.0 154.96296296296293 L 161.81818181818181 153.60391796755434 L 163.63636363636363 152.22038567493112 L 165.45454545454544 150.81236608509337 L 167.27272727272728 149.37985919804103 L 169.09090909090909 147.92286501377413 L 170.90909090909091 146.4413835322926 L 172.72727272727272 144.93541475359658 L 174.54545454545453 143.40495867768595 L 176.36363636363635 141.85001530456077 L 178.18181818181816 140.270584634221 L 180.00000000000003 138.66666666666666 L 181.81818181818181 137.03826140189778 L 183.63636363636363 135.38536883991429 L 185.45454545454547 133.70798898071624 L 187.27272727272725 132.00612182430365 L 189.09090909090909 130.2797673706765 L 190.90909090909093 128.52892561983472 L 192.72727272727272 126.7535965717784 L 194.54545454545456 124.95378022650749 L 196.36363636363637 123.12947658402204 L 198.18181818181816 121.28068564432202 L 200.0 119.4074074074074 L 201.81818181818181 117.50964187327824 L 203.63636363636363 115.58738904193451 L 205.45454545454547 113.64064891337618 L 207.27272727272725 111.6694214876033 L 209.09090909090907 109.67370676461587 L 210.90909090909091 107.65350474441385 L 212.72727272727272 105.60881542699724 L 214.54545454545456 103.53963881236606 L 216.36363636363637 101.44597490052035 L 218.18181818181816 99.327823691460083 L 220.0 97.185185185185162 L 221.81818181818181 95.018059381695764 L 223.63636363636363 92.82644628099176 L 225.45454545454547 90.610345883073165 L 227.27272727272728 88.369758187940008 L 229.09090909090909 86.104683195592287 L 230.90909090909091 83.815120906029989 L 232.72727272727272 81.501071319253157 L 234.54545454545456 79.162534435261676 L 236.36363636363637 76.799510254055718 L 238.18181818181819 74.411998775635112 L 240.0 72.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="240.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="250.0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">10</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="250.0">Days</text><line style="" x1="50" x2="50" y1="72.0" y2="192.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 180.00000000000003)" x="50" y="180.00000000000003">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 120.00000000000001)" x="50" y="120.00000000000001">100</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">150</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">Users</text><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="50">Toyplot Users</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tb4f298e74648488aa867cd6bd652c59a text");
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
          var text = document.querySelectorAll("#tb4f298e74648488aa867cd6bd652c59a text");
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
      var data_tables = [{"data": [[0.0, 0.10101010101010101, 0.20202020202020202, 0.30303030303030304, 0.40404040404040403, 0.5050505050505051, 0.6060606060606061, 0.7070707070707071, 0.8080808080808081, 0.9090909090909091, 1.0101010101010102, 1.1111111111111112, 1.2121212121212122, 1.3131313131313131, 1.4141414141414141, 1.5151515151515151, 1.6161616161616161, 1.7171717171717171, 1.8181818181818181, 1.9191919191919191, 2.0202020202020203, 2.121212121212121, 2.2222222222222223, 2.323232323232323, 2.4242424242424243, 2.525252525252525, 2.6262626262626263, 2.727272727272727, 2.8282828282828283, 2.929292929292929, 3.0303030303030303, 3.131313131313131, 3.2323232323232323, 3.3333333333333335, 3.4343434343434343, 3.5353535353535355, 3.6363636363636362, 3.7373737373737375, 3.8383838383838382, 3.9393939393939394, 4.040404040404041, 4.141414141414141, 4.242424242424242, 4.343434343434343, 4.444444444444445, 4.545454545454545, 4.646464646464646, 4.747474747474747, 4.848484848484849, 4.94949494949495, 5.05050505050505, 5.151515151515151, 5.252525252525253, 5.353535353535354, 5.454545454545454, 5.555555555555555, 5.656565656565657, 5.757575757575758, 5.858585858585858, 5.959595959595959, 6.0606060606060606, 6.161616161616162, 6.262626262626262, 6.363636363636363, 6.4646464646464645, 6.565656565656566, 6.666666666666667, 6.767676767676767, 6.8686868686868685, 6.96969696969697, 7.070707070707071, 7.171717171717171, 7.2727272727272725, 7.373737373737374, 7.474747474747475, 7.575757575757575, 7.6767676767676765, 7.777777777777778, 7.878787878787879, 7.979797979797979, 8.080808080808081, 8.181818181818182, 8.282828282828282, 8.383838383838384, 8.484848484848484, 8.585858585858587, 8.686868686868687, 8.787878787878787, 8.88888888888889, 8.98989898989899, 9.09090909090909, 9.191919191919192, 9.292929292929292, 9.393939393939394, 9.494949494949495, 9.595959595959595, 9.696969696969697, 9.797979797979798, 9.8989898989899, 10.0], [40.0, 40.01020304050607, 40.04081216202428, 40.09182736455464, 40.16324864809713, 40.25507601265177, 40.36730945821855, 40.49994898479747, 40.65299459238853, 40.82644628099173, 41.02030405060708, 41.23456790123457, 41.4692378328742, 41.72431384552597, 41.99979593918988, 42.29568411386593, 42.61197836955413, 42.94867870625446, 43.30578512396694, 43.68329762269156, 44.08121620242832, 44.499540863177224, 44.93827160493827, 45.397408427711454, 45.876951331496784, 46.376900316294254, 46.897255382103864, 47.438016528925615, 47.999183756759514, 48.58075706560555, 49.182736455463726, 49.805121926334046, 50.447913478216506, 51.111111111111114, 51.794714825017856, 52.49872461993674, 53.22314049586777, 53.96796245281094, 54.73319049076625, 55.5188246097337, 56.3248648097133, 57.15131109070502, 57.99816345270891, 58.86542189572492, 59.75308641975309, 60.66115702479338, 61.58963371084583, 62.53851647791042, 63.50780532598715, 64.49750025507602, 65.50760126517702, 66.53810835629017, 67.58902152841547, 68.6603407815529, 69.75206611570248, 70.8641975308642, 71.99673502703806, 73.14967860422406, 74.3230282624222, 75.51678400163249, 76.7309458218549, 77.96551372308949, 79.22048770533618, 80.49586776859505, 81.79165391286602, 83.10784613814917, 84.44444444444446, 85.80144883175186, 87.17885930007142, 88.57667584940313, 89.99489847974696, 91.43352719110294, 92.89256198347107, 94.37200285685134, 95.87184981124375, 97.3921028466483, 98.93276196306499, 100.49382716049382, 102.0752984389348, 103.6771757983879, 105.29945923885319, 106.94214876033058, 108.6052443628201, 110.2887460463218, 111.99265381083562, 113.7169676563616, 115.4616875828997, 117.22681359044994, 119.01234567901236, 120.81828384858687, 122.64462809917353, 124.49137843077237, 126.35853484338332, 128.24609733700643, 130.15406591164168, 132.08244056728904, 134.0312213039486, 136.00040812162024, 137.99000102030408, 140.0], [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"], "id": "t4312ce17d30c4afbb69467c9d3fee642", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tb4f298e74648488aa867cd6bd652c59a .toyplot-mark-popup");
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
      var axes = {"tad3f97d690eb47459f017f4799dfcd59": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 10.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t9889860a16b545a1a4fc97230678d499"><svg height="700.0px" id="ta1103d2c35fc4cdca6463557f1983965" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="ta4dac84999484f83aec9351bba999911"><clipPath id="t63a06e3c98904582b0355962ada54377"><rect height="250.0" width="250.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t63a06e3c98904582b0355962ada54377)" style="cursor:crosshair"><rect height="250.0" style="pointer-events:all;visibility:hidden" width="250.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tce8a2d523f444c678202b40a206cb484" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 290.0 L 64.693877551020421 285.30612244897958 L 69.387755102040813 280.61224489795921 L 74.081632653061234 275.91836734693879 L 78.775510204081627 271.22448979591837 L 83.469387755102034 266.53061224489795 L 88.163265306122454 261.83673469387753 L 92.857142857142861 257.14285714285711 L 97.551020408163268 252.44897959183675 L 102.24489795918367 247.75510204081633 L 106.93877551020407 243.0612244897959 L 111.63265306122449 238.36734693877551 L 116.32653061224488 233.67346938775509 L 121.0204081632653 228.9795918367347 L 125.71428571428571 224.28571428571428 L 130.40816326530611 219.59183673469391 L 135.10204081632654 214.89795918367349 L 139.79591836734693 210.20408163265307 L 144.48979591836735 205.51020408163265 L 149.18367346938777 200.81632653061226 L 153.87755102040813 196.12244897959184 L 158.57142857142856 191.42857142857142 L 163.26530612244898 186.73469387755102 L 167.9591836734694 182.0408163265306 L 172.65306122448979 177.34693877551021 L 177.34693877551021 172.65306122448979 L 182.0408163265306 167.9591836734694 L 186.73469387755102 163.26530612244898 L 191.42857142857142 158.57142857142858 L 196.12244897959184 153.87755102040816 L 200.8163265306122 149.18367346938777 L 205.51020408163265 144.48979591836735 L 210.20408163265307 139.79591836734696 L 214.89795918367346 135.10204081632654 L 219.59183673469389 130.40816326530614 L 224.28571428571425 125.71428571428575 L 228.9795918367347 121.02040816326532 L 233.67346938775509 116.32653061224491 L 238.36734693877551 111.63265306122449 L 243.0612244897959 106.93877551020408 L 247.7551020408163 102.2448979591837 L 252.44897959183675 97.551020408163282 L 257.14285714285711 92.857142857142861 L 261.83673469387753 88.163265306122454 L 266.53061224489795 83.469387755102048 L 271.22448979591837 78.775510204081627 L 275.91836734693879 74.081632653061234 L 280.61224489795916 69.387755102040828 L 285.30612244897958 64.693877551020421 L 290.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="290.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="64.693877551020421" cy="285.30612244897958" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="69.387755102040813" cy="280.61224489795921" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="74.081632653061234" cy="275.91836734693879" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.775510204081627" cy="271.22448979591837" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="83.469387755102034" cy="266.53061224489795" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="88.163265306122454" cy="261.83673469387753" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="92.857142857142861" cy="257.14285714285711" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="97.551020408163268" cy="252.44897959183675" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="102.24489795918367" cy="247.75510204081633" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="106.93877551020407" cy="243.0612244897959" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="111.63265306122449" cy="238.36734693877551" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="116.32653061224488" cy="233.67346938775509" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="121.0204081632653" cy="228.9795918367347" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="125.71428571428571" cy="224.28571428571428" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="130.40816326530611" cy="219.59183673469391" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="135.10204081632654" cy="214.89795918367349" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="139.79591836734693" cy="210.20408163265307" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="144.48979591836735" cy="205.51020408163265" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="149.18367346938777" cy="200.81632653061226" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="153.87755102040813" cy="196.12244897959184" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="158.57142857142856" cy="191.42857142857142" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="163.26530612244898" cy="186.73469387755102" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="167.9591836734694" cy="182.0408163265306" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="172.65306122448979" cy="177.34693877551021" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="177.34693877551021" cy="172.65306122448979" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="182.0408163265306" cy="167.9591836734694" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.73469387755102" cy="163.26530612244898" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="191.42857142857142" cy="158.57142857142858" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="196.12244897959184" cy="153.87755102040816" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="200.8163265306122" cy="149.18367346938777" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="205.51020408163265" cy="144.48979591836735" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="210.20408163265307" cy="139.79591836734696" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="214.89795918367346" cy="135.10204081632654" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="219.59183673469389" cy="130.40816326530614" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="224.28571428571425" cy="125.71428571428575" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="228.9795918367347" cy="121.02040816326532" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="233.67346938775509" cy="116.32653061224491" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="238.36734693877551" cy="111.63265306122449" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="243.0612244897959" cy="106.93877551020408" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="247.7551020408163" cy="102.2448979591837" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="252.44897959183675" cy="97.551020408163282" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="257.14285714285711" cy="92.857142857142861" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="261.83673469387753" cy="88.163265306122454" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="266.53061224489795" cy="83.469387755102048" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="271.22448979591837" cy="78.775510204081627" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="275.91836734693879" cy="74.081632653061234" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="280.61224489795916" cy="69.387755102040828" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="285.30612244897958" cy="64.693877551020421" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="290.0" cy="60.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="200.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="245.0" y="67.0"></text></g><line style="" x1="60.0" x2="290.0" y1="300.0" y2="300.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="300.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="117.5" y="300.0">-500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="175.0" y="300.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="232.5" y="300.0">500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="290.0" y="300.0">1000</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="290.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 290.0)" x="50.0" y="290.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 232.5)" x="50.0" y="232.5">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 175.0)" x="50.0" y="175.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 117.5)" x="50.0" y="117.5">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1000</text></g></g><g class="toyplot-axes-Cartesian" id="tb27fdb3016b74a8d8d2955d1dc321ee3"><clipPath id="ta00e54533c0041829868568fac521aac"><rect height="250.0" width="250.0" x="400.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta00e54533c0041829868568fac521aac)" style="cursor:crosshair"><rect height="250.0" style="pointer-events:all;visibility:hidden" width="250.0" x="400.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tde9af95f87ef4fe1bc107bba3a1815ae" style="fill:none"><g class="toyplot-Series"><path d="M 410.0 290.0 L 410.5550121441791 285.30612244897958 L 411.1341626984306 280.61224489795921 L 411.73964714976711 275.91836734693879 L 412.3739748481359 271.22448979591837 L 413.04003183872845 266.53061224489795 L 413.7411602494866 261.83673469387753 L 414.48125976079928 257.14285714285711 L 415.2649189646192 252.44897959183675 L 416.09758784329006 247.75510204081633 L 416.98580785197305 243.0612244897959 L 417.93752435333215 238.36734693877551 L 418.96251952159855 233.67346938775509 L 420.07302614966829 228.9795918367347 L 421.28462141570083 224.28571428571428 L 422.61756935832096 219.59183673469391 L 424.09891286527397 214.89795918367349 L 425.76588117650022 210.20408163265307 L 427.67175031679807 205.51020408163265 L 429.89663744268887 200.81632653061226 L 432.56924283140177 196.12244897959184 L 435.9163398937705 191.42857142857142 L 440.39759965456983 186.73469387755102 L 447.20096130947144 182.0408163265306 L 461.83267978754105 177.34693877551021 L 588.16732021245889 172.65306122448979 L 602.7990386905285 167.9591836734694 L 609.60240034543017 163.26530612244898 L 614.08366010622944 158.57142857142858 L 617.43075716859823 153.87755102040816 L 620.10336255731113 149.18367346938777 L 622.32824968320188 144.48979591836735 L 624.23411882349978 139.79591836734696 L 625.90108713472591 135.10204081632654 L 627.38243064167909 130.40816326530614 L 628.71537858429906 125.71428571428575 L 629.92697385033171 121.02040816326532 L 631.03748047840145 116.32653061224491 L 632.06247564666785 111.63265306122449 L 633.01419214802695 106.93877551020408 L 633.90241215670994 102.2448979591837 L 634.73508103538074 97.551020408163282 L 635.51874023920072 92.857142857142861 L 636.2588397505134 88.163265306122454 L 636.9599681612716 83.469387755102048 L 637.62602515186416 78.775510204081627 L 638.26035285023283 74.081632653061234 L 638.8658373015694 69.387755102040828 L 639.44498785582084 64.693877551020421 L 640.0 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="410.0" cy="290.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="410.5550121441791" cy="285.30612244897958" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="411.1341626984306" cy="280.61224489795921" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="411.73964714976711" cy="275.91836734693879" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="412.3739748481359" cy="271.22448979591837" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="413.04003183872845" cy="266.53061224489795" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="413.7411602494866" cy="261.83673469387753" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="414.48125976079928" cy="257.14285714285711" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="415.2649189646192" cy="252.44897959183675" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="416.09758784329006" cy="247.75510204081633" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="416.98580785197305" cy="243.0612244897959" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="417.93752435333215" cy="238.36734693877551" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="418.96251952159855" cy="233.67346938775509" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="420.07302614966829" cy="228.9795918367347" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="421.28462141570083" cy="224.28571428571428" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="422.61756935832096" cy="219.59183673469391" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="424.09891286527397" cy="214.89795918367349" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="425.76588117650022" cy="210.20408163265307" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="427.67175031679807" cy="205.51020408163265" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="429.89663744268887" cy="200.81632653061226" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="432.56924283140177" cy="196.12244897959184" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="435.9163398937705" cy="191.42857142857142" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="440.39759965456983" cy="186.73469387755102" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="447.20096130947144" cy="182.0408163265306" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="461.83267978754105" cy="177.34693877551021" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="588.16732021245889" cy="172.65306122448979" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="602.7990386905285" cy="167.9591836734694" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="609.60240034543017" cy="163.26530612244898" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="614.08366010622944" cy="158.57142857142858" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="617.43075716859823" cy="153.87755102040816" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="620.10336255731113" cy="149.18367346938777" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="622.32824968320188" cy="144.48979591836735" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="624.23411882349978" cy="139.79591836734696" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="625.90108713472591" cy="135.10204081632654" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="627.38243064167909" cy="130.40816326530614" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="628.71537858429906" cy="125.71428571428575" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="629.92697385033171" cy="121.02040816326532" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="631.03748047840145" cy="116.32653061224491" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="632.06247564666785" cy="111.63265306122449" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="633.01419214802695" cy="106.93877551020408" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="633.90241215670994" cy="102.2448979591837" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="634.73508103538074" cy="97.551020408163282" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="635.51874023920072" cy="92.857142857142861" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="636.2588397505134" cy="88.163265306122454" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="636.9599681612716" cy="83.469387755102048" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="637.62602515186416" cy="78.775510204081627" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="638.26035285023283" cy="74.081632653061234" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="638.8658373015694" cy="69.387755102040828" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="639.44498785582084" cy="64.693877551020421" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="640.0" cy="60.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g><line style="" x1="410.0" x2="640.0" y1="300.0" y2="300.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="410.0" y="300.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="440.6666666666667" y="300.0">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="471.3333333333333" y="300.0">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="502.0" y="300.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="525.0" y="300.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="548.0" y="300.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="578.6666666666667" y="300.0">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="609.3333333333333" y="300.0">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="640.0" y="300.0">10&#8202;&#179;</text></g><line style="" x1="400.0" x2="400.0" y1="60.0" y2="290.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 290.0)" x="400.0" y="290.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 232.5)" x="400.0" y="232.5">-500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 175.0)" x="400.0" y="175.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 117.5)" x="400.0" y="117.5">500</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 60.0)" x="400.0" y="60.0">1000</text></g></g><g class="toyplot-axes-Cartesian" id="td64f3ee43619497a848e5fd125f53620"><clipPath id="tfcb5290706234df79b8c8a3df7c99271"><rect height="250.0" width="250.0" x="50.0" y="400.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tfcb5290706234df79b8c8a3df7c99271)" style="cursor:crosshair"><rect height="250.0" style="pointer-events:all;visibility:hidden" width="250.0" x="50.0" y="400.0"></rect><g class="toyplot-mark-Plot" id="td19f6f2b0bec42229944336d6100df9d" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 640.0 L 64.693877551020421 639.44498785582084 L 69.387755102040813 638.8658373015694 L 74.081632653061234 638.26035285023283 L 78.775510204081627 637.62602515186416 L 83.469387755102034 636.9599681612716 L 88.163265306122454 636.2588397505134 L 92.857142857142861 635.51874023920072 L 97.551020408163268 634.73508103538074 L 102.24489795918367 633.90241215670994 L 106.93877551020407 633.01419214802695 L 111.63265306122449 632.06247564666785 L 116.32653061224488 631.03748047840145 L 121.0204081632653 629.92697385033171 L 125.71428571428571 628.71537858429906 L 130.40816326530611 627.38243064167909 L 135.10204081632654 625.90108713472591 L 139.79591836734693 624.23411882349978 L 144.48979591836735 622.32824968320188 L 149.18367346938777 620.10336255731113 L 153.87755102040813 617.43075716859823 L 158.57142857142856 614.08366010622944 L 163.26530612244898 609.60240034543006 L 167.9591836734694 602.79903869052862 L 172.65306122448979 588.16732021245889 L 177.34693877551021 461.832679787541 L 182.0408163265306 447.20096130947144 L 186.73469387755102 440.39759965456983 L 191.42857142857142 435.91633989377056 L 196.12244897959184 432.56924283140177 L 200.8163265306122 429.89663744268887 L 205.51020408163265 427.67175031679812 L 210.20408163265307 425.76588117650022 L 214.89795918367346 424.09891286527397 L 219.59183673469389 422.61756935832102 L 224.28571428571425 421.28462141570088 L 228.9795918367347 420.07302614966829 L 233.67346938775509 418.96251952159855 L 238.36734693877551 417.93752435333215 L 243.0612244897959 416.98580785197305 L 247.7551020408163 416.09758784329006 L 252.44897959183675 415.2649189646192 L 257.14285714285711 414.48125976079928 L 261.83673469387753 413.7411602494866 L 266.53061224489795 413.04003183872845 L 271.22448979591837 412.3739748481359 L 275.91836734693879 411.73964714976711 L 280.61224489795916 411.1341626984306 L 285.30612244897958 410.55501214417905 L 290.0 410.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="60.0" cy="640.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="64.693877551020421" cy="639.44498785582084" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="69.387755102040813" cy="638.8658373015694" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="74.081632653061234" cy="638.26035285023283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="78.775510204081627" cy="637.62602515186416" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="83.469387755102034" cy="636.9599681612716" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="88.163265306122454" cy="636.2588397505134" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="92.857142857142861" cy="635.51874023920072" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="97.551020408163268" cy="634.73508103538074" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="102.24489795918367" cy="633.90241215670994" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="106.93877551020407" cy="633.01419214802695" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="111.63265306122449" cy="632.06247564666785" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="116.32653061224488" cy="631.03748047840145" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="121.0204081632653" cy="629.92697385033171" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="125.71428571428571" cy="628.71537858429906" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="130.40816326530611" cy="627.38243064167909" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="135.10204081632654" cy="625.90108713472591" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="139.79591836734693" cy="624.23411882349978" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="144.48979591836735" cy="622.32824968320188" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="149.18367346938777" cy="620.10336255731113" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="153.87755102040813" cy="617.43075716859823" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="158.57142857142856" cy="614.08366010622944" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="163.26530612244898" cy="609.60240034543006" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="167.9591836734694" cy="602.79903869052862" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="172.65306122448979" cy="588.16732021245889" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="177.34693877551021" cy="461.832679787541" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="182.0408163265306" cy="447.20096130947144" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="186.73469387755102" cy="440.39759965456983" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="191.42857142857142" cy="435.91633989377056" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="196.12244897959184" cy="432.56924283140177" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="200.8163265306122" cy="429.89663744268887" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="205.51020408163265" cy="427.67175031679812" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="210.20408163265307" cy="425.76588117650022" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="214.89795918367346" cy="424.09891286527397" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="219.59183673469389" cy="422.61756935832102" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="224.28571428571425" cy="421.28462141570088" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="228.9795918367347" cy="420.07302614966829" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="233.67346938775509" cy="418.96251952159855" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="238.36734693877551" cy="417.93752435333215" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="243.0612244897959" cy="416.98580785197305" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="247.7551020408163" cy="416.09758784329006" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="252.44897959183675" cy="415.2649189646192" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="257.14285714285711" cy="414.48125976079928" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="261.83673469387753" cy="413.7411602494866" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="266.53061224489795" cy="413.04003183872845" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="271.22448979591837" cy="412.3739748481359" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="275.91836734693879" cy="411.73964714976711" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="280.61224489795916" cy="411.1341626984306" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="285.30612244897958" cy="410.55501214417905" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="290.0" cy="410.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="200.0" y="410.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="245.0" y="417.0"></text></g><line style="" x1="60.0" x2="290.0" y1="650.0" y2="650.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="650.0">-1000</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="117.5" y="650.0">-500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="175.0" y="650.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="232.5" y="650.0">500</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="290.0" y="650.0">1000</text></g><line style="" x1="50.0" x2="50.0" y1="410.0" y2="640.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 640.0)" x="50.0" y="640.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 609.3333333333334)" x="50.0" y="609.3333333333334">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 578.6666666666667)" x="50.0" y="578.6666666666667">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 548.0)" x="50.0" y="548.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 525.0)" x="50.0" y="525.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 502.0)" x="50.0" y="502.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 471.33333333333337)" x="50.0" y="471.33333333333337">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 440.66666666666663)" x="50.0" y="440.66666666666663">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 410.0)" x="50.0" y="410.0">10&#8202;&#179;</text></g></g><g class="toyplot-axes-Cartesian" id="t02b05ae7e5a64dda930c451442d1ca1b"><clipPath id="t5eb7d6db58224b298e34f1aad93aa633"><rect height="250.0" width="250.0" x="400.0" y="400.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t5eb7d6db58224b298e34f1aad93aa633)" style="cursor:crosshair"><rect height="250.0" style="pointer-events:all;visibility:hidden" width="250.0" x="400.0" y="400.0"></rect><g class="toyplot-mark-Plot" id="t62a69fbbec4f4226a133b629d68583e1" style="fill:none"><g class="toyplot-Series"><path d="M 410.0 640.0 L 410.5550121441791 639.44498785582084 L 411.1341626984306 638.8658373015694 L 411.73964714976711 638.26035285023283 L 412.3739748481359 637.62602515186416 L 413.04003183872845 636.9599681612716 L 413.7411602494866 636.2588397505134 L 414.48125976079928 635.51874023920072 L 415.2649189646192 634.73508103538074 L 416.09758784329006 633.90241215670994 L 416.98580785197305 633.01419214802695 L 417.93752435333215 632.06247564666785 L 418.96251952159855 631.03748047840145 L 420.07302614966829 629.92697385033171 L 421.28462141570083 628.71537858429906 L 422.61756935832096 627.38243064167909 L 424.09891286527397 625.90108713472591 L 425.76588117650022 624.23411882349978 L 427.67175031679807 622.32824968320188 L 429.89663744268887 620.10336255731113 L 432.56924283140177 617.43075716859823 L 435.9163398937705 614.08366010622944 L 440.39759965456983 609.60240034543006 L 447.20096130947144 602.79903869052862 L 461.83267978754105 588.16732021245889 L 588.16732021245889 461.832679787541 L 602.7990386905285 447.20096130947144 L 609.60240034543017 440.39759965456983 L 614.08366010622944 435.91633989377056 L 617.43075716859823 432.56924283140177 L 620.10336255731113 429.89663744268887 L 622.32824968320188 427.67175031679812 L 624.23411882349978 425.76588117650022 L 625.90108713472591 424.09891286527397 L 627.38243064167909 422.61756935832102 L 628.71537858429906 421.28462141570088 L 629.92697385033171 420.07302614966829 L 631.03748047840145 418.96251952159855 L 632.06247564666785 417.93752435333215 L 633.01419214802695 416.98580785197305 L 633.90241215670994 416.09758784329006 L 634.73508103538074 415.2649189646192 L 635.51874023920072 414.48125976079928 L 636.2588397505134 413.7411602494866 L 636.9599681612716 413.04003183872845 L 637.62602515186416 412.3739748481359 L 638.26035285023283 411.73964714976711 L 638.8658373015694 411.1341626984306 L 639.44498785582084 410.55501214417905 L 640.0 410.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="410.0" cy="640.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="410.5550121441791" cy="639.44498785582084" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="411.1341626984306" cy="638.8658373015694" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="411.73964714976711" cy="638.26035285023283" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="412.3739748481359" cy="637.62602515186416" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="413.04003183872845" cy="636.9599681612716" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="413.7411602494866" cy="636.2588397505134" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="414.48125976079928" cy="635.51874023920072" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="415.2649189646192" cy="634.73508103538074" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="416.09758784329006" cy="633.90241215670994" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="416.98580785197305" cy="633.01419214802695" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="417.93752435333215" cy="632.06247564666785" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="418.96251952159855" cy="631.03748047840145" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="420.07302614966829" cy="629.92697385033171" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="421.28462141570083" cy="628.71537858429906" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="422.61756935832096" cy="627.38243064167909" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="424.09891286527397" cy="625.90108713472591" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="425.76588117650022" cy="624.23411882349978" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="427.67175031679807" cy="622.32824968320188" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="429.89663744268887" cy="620.10336255731113" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="432.56924283140177" cy="617.43075716859823" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="435.9163398937705" cy="614.08366010622944" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="440.39759965456983" cy="609.60240034543006" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="447.20096130947144" cy="602.79903869052862" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="461.83267978754105" cy="588.16732021245889" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="588.16732021245889" cy="461.832679787541" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="602.7990386905285" cy="447.20096130947144" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="609.60240034543017" cy="440.39759965456983" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="614.08366010622944" cy="435.91633989377056" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="617.43075716859823" cy="432.56924283140177" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="620.10336255731113" cy="429.89663744268887" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="622.32824968320188" cy="427.67175031679812" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="624.23411882349978" cy="425.76588117650022" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="625.90108713472591" cy="424.09891286527397" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="627.38243064167909" cy="422.61756935832102" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="628.71537858429906" cy="421.28462141570088" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="629.92697385033171" cy="420.07302614966829" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="631.03748047840145" cy="418.96251952159855" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="632.06247564666785" cy="417.93752435333215" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="633.01419214802695" cy="416.98580785197305" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="633.90241215670994" cy="416.09758784329006" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="634.73508103538074" cy="415.2649189646192" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="635.51874023920072" cy="414.48125976079928" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="636.2588397505134" cy="413.7411602494866" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="636.9599681612716" cy="413.04003183872845" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="637.62602515186416" cy="412.3739748481359" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="638.26035285023283" cy="411.73964714976711" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="638.8658373015694" cy="411.1341626984306" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="639.44498785582084" cy="410.55501214417905" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(40%,76.1%,64.7%,1);opacity:1.0;stroke:rgba(40%,76.1%,64.7%,1)"><circle cx="640.0" cy="410.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="550.0" y="410.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="417.0"></text></g><line style="" x1="410.0" x2="640.0" y1="650.0" y2="650.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="410.0" y="650.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="440.6666666666667" y="650.0">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="471.3333333333333" y="650.0">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="502.0" y="650.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="525.0" y="650.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="548.0" y="650.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="578.6666666666667" y="650.0">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="609.3333333333333" y="650.0">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="640.0" y="650.0">10&#8202;&#179;</text></g><line style="" x1="400.0" x2="400.0" y1="410.0" y2="640.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 640.0)" x="400.0" y="640.0">-10&#8202;&#179;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 609.3333333333334)" x="400.0" y="609.3333333333334">-10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 578.6666666666667)" x="400.0" y="578.6666666666667">-10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 548.0)" x="400.0" y="548.0">-10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 525.0)" x="400.0" y="525.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 502.0)" x="400.0" y="502.0">10&#8202;&#8304;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 471.33333333333337)" x="400.0" y="471.33333333333337">10&#8202;&#185;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 440.66666666666663)" x="400.0" y="440.66666666666663">10&#8202;&#178;</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 400.0, 410.0)" x="400.0" y="410.0">10&#8202;&#179;</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t9889860a16b545a1a4fc97230678d499 text");
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
          var text = document.querySelectorAll("#t9889860a16b545a1a4fc97230678d499 text");
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
      var data_tables = [{"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"], "id": "tce8a2d523f444c678202b40a206cb484", "title": "Plot Data"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"], "id": "tde9af95f87ef4fe1bc107bba3a1815ae", "title": "Plot Data"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"], "id": "td19f6f2b0bec42229944336d6100df9d", "title": "Plot Data"}, {"data": [[-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], [-1000.0, -959.1836734693877, -918.3673469387755, -877.5510204081633, -836.7346938775511, -795.9183673469388, -755.1020408163265, -714.2857142857142, -673.469387755102, -632.6530612244899, -591.8367346938776, -551.0204081632653, -510.2040816326531, -469.38775510204084, -428.57142857142856, -387.7551020408164, -346.9387755102041, -306.1224489795918, -265.30612244897964, -224.48979591836735, -183.67346938775518, -142.8571428571429, -102.0408163265306, -61.22448979591843, -20.408163265306143, 20.408163265306143, 61.224489795918316, 102.0408163265306, 142.8571428571429, 183.67346938775518, 224.48979591836724, 265.3061224489795, 306.1224489795918, 346.9387755102041, 387.7551020408164, 428.57142857142844, 469.3877551020407, 510.204081632653, 551.0204081632653, 591.8367346938776, 632.6530612244896, 673.4693877551019, 714.2857142857142, 755.1020408163265, 795.9183673469388, 836.7346938775511, 877.5510204081631, 918.3673469387754, 959.1836734693877, 1000.0], ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902, 0.7607843137254902], [0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 0.6470588235294118], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], "names": ["x", "y0", "marker0", "size0", "fill0:red", "fill0:green", "fill0:blue", "fill0:alpha", "stroke0:red", "stroke0:green", "stroke0:blue", "stroke0:alpha", "opacity0"], "id": "t62a69fbbec4f4226a133b629d68583e1", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t9889860a16b545a1a4fc97230678d499 .toyplot-mark-popup");
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
      var axes = {"t02b05ae7e5a64dda930c451442d1ca1b": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 502.0, "min": -Infinity}, "max": 502.0, "min": 410.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 548.0, "min": 502.0}, "max": 548.0, "min": 502.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 548.0}, "max": 640.0, "min": 548.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 548.0, "min": -Infinity}, "max": 548.0, "min": 640.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 502.0, "min": 548.0}, "max": 502.0, "min": 548.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 502.0}, "max": 410.0, "min": 502.0}, "scale": ["log", 10]}]}, "ta4dac84999484f83aec9351bba999911": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 290.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 290.0}, "scale": "linear"}]}, "tb27fdb3016b74a8d8d2955d1dc321ee3": {"x": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 502.0, "min": -Infinity}, "max": 502.0, "min": 410.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 548.0, "min": 502.0}, "max": 548.0, "min": 502.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 548.0}, "max": 640.0, "min": 548.0}, "scale": ["log", 10]}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 290.0}, "scale": "linear"}]}, "td64f3ee43619497a848e5fd125f53620": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1000.0, "min": -1000.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 290.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": -1, "min": -Infinity}, "max": -1, "min": -1000.0}, "range": {"bounds": {"max": 548.0, "min": -Infinity}, "max": 548.0, "min": 640.0}, "scale": ["log", 10]}, {"domain": {"bounds": {"max": 1, "min": -1}, "max": 1, "min": -1}, "range": {"bounds": {"max": 502.0, "min": 548.0}, "max": 502.0, "min": 548.0}, "scale": "linear"}, {"domain": {"bounds": {"max": Infinity, "min": 1}, "max": 1000.0, "min": 1}, "range": {"bounds": {"max": Infinity, "min": 502.0}, "max": 410.0, "min": 502.0}, "scale": ["log", 10]}]}};
    
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

