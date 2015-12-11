
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

    <div align="center" class="toyplot" id="t2e106ef849964d80914734f648a96b36"><svg height="300.0px" id="t7af6bb095fd644e7897d7dfa47c80ed7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t55487ed2d2b048c78d9c5bbac8393557"><clipPath id="t1f12bd81e3fc4d46b788a9b4a68b3dfd"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t1f12bd81e3fc4d46b788a9b4a68b3dfd)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Scatterplot" id="ta6f8fcebccd14ff0b994c194585c7546" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="250.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.0" cy="249.4459833795014" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.0" cy="247.78393351800551" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.0" cy="245.01385041551248" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.0" cy="241.13573407202216" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.0" cy="236.14958448753461" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="110.0" cy="230.05540166204986" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.0" cy="222.85318559556785" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="130.0" cy="214.54293628808864" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="140.0" cy="205.1246537396122" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="150.0" cy="194.5983379501385" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.0" cy="182.96398891966757" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="170.0" cy="170.22160664819947" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="180.0" cy="156.37119113573411" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="190.0" cy="141.41274238227149" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="200.0" cy="125.34626038781163" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="210.0" cy="108.17174515235459" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="220.0" cy="89.889196675900322" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="230.0" cy="70.498614958448783" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="50.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="ta9b9754961fb4e5dbbdfe7d41506e190" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t9c50dc60e8374569a0019bcb1966a1c1" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t2e106ef849964d80914734f648a96b36 text");
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
          var text = document.querySelectorAll("#t2e106ef849964d80914734f648a96b36 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "ta6f8fcebccd14ff0b994c194585c7546", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t2e106ef849964d80914734f648a96b36 .toyplot-mark-popup");
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
      var axes = {"t55487ed2d2b048c78d9c5bbac8393557": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Markers can also be added to regular plots to highlight the datums (they
are turned-off by default):

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.axes(grid=(1, 2, 0)).plot(y)
    canvas.axes(grid=(1, 2, 1)).plot(y, marker="o");



.. raw:: html

    <div align="center" class="toyplot" id="t40bbe97b18334ef9bccc89f36d552644"><svg height="300.0px" id="tb7b17fd1c4404e9e8e3f28aec224bcbe" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td727e6fc5dbe4cc9acf81bc8f82ea092"><clipPath id="t74999a3aaafe4311b84ca5acdbddbfca"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t74999a3aaafe4311b84ca5acdbddbfca)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t55463a2091f44fd898fd806c64f11a48" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tba4f5acd80ef41ff95703fb7129f1e50" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="ta9aa3962c1994d43bbfce83e49b2e801" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="t7f207496100d42988e6bad678a276dd0"><clipPath id="tf51643f9e9324f39ae6e528a026de16d"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf51643f9e9324f39ae6e528a026de16d)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="te70c18c2a1df438f95c791bed102a03f" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t70bc87552de04c97b7ffe3e0f73a2f55" transform="translate(350.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t0aeae8067faf4d52a5c47a63253e000f" transform="translate(350.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t40bbe97b18334ef9bccc89f36d552644 text");
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
          var text = document.querySelectorAll("#t40bbe97b18334ef9bccc89f36d552644 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t55463a2091f44fd898fd806c64f11a48", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "te70c18c2a1df438f95c791bed102a03f", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t40bbe97b18334ef9bccc89f36d552644 .toyplot-mark-popup");
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
      var axes = {"t7f207496100d42988e6bad678a276dd0": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "td727e6fc5dbe4cc9acf81bc8f82ea092": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


You can use the ``size`` argument to control the size of the markers:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.axes(grid=(1, 2, 0)).plot(y, marker="o", size=6)
    canvas.axes(grid=(1, 2, 1)).plot(y, marker="o", size=10);



.. raw:: html

    <div align="center" class="toyplot" id="t57e8699bfef74f15b01e6ee0a268b94a"><svg height="300.0px" id="td72e24c8778f41aeadfca65e37f3432c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t8186440888e248eda5458ac3191fd05e"><clipPath id="t511d1aa7bb7b4264b00f0e8630affc69"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t511d1aa7bb7b4264b00f0e8630affc69)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t95c7850df149447fbe3fa218530b5625" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="250.0" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.0" cy="249.4459833795014" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.0" cy="247.78393351800551" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.0" cy="245.01385041551248" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.0" cy="241.13573407202216" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.0" cy="236.14958448753461" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="110.0" cy="230.05540166204986" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.0" cy="222.85318559556785" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="130.0" cy="214.54293628808864" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="140.0" cy="205.1246537396122" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="150.0" cy="194.5983379501385" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.0" cy="182.96398891966757" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="170.0" cy="170.22160664819947" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="180.0" cy="156.37119113573411" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="190.0" cy="141.41274238227149" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="200.0" cy="125.34626038781163" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="210.0" cy="108.17174515235459" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="220.0" cy="89.889196675900322" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="230.0" cy="70.498614958448783" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="50.0" r="3.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t29ed9f4dd9164345bd33abb197991293" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t8a662c27225c442bacb1f0820b6fc47f" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="tc21a6e6751ef481c835209a4760afc03"><clipPath id="t265b13919eed457382b9fc45ad9ac042"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t265b13919eed457382b9fc45ad9ac042)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="ta94bde4c06fa42a08d1365c11fa57643" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="5.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t6effc9551fd840f7a1887b59870a08a7" transform="translate(350.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="td1d1cc23345a43cfade8d12eaf5307da" transform="translate(350.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t57e8699bfef74f15b01e6ee0a268b94a text");
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
          var text = document.querySelectorAll("#t57e8699bfef74f15b01e6ee0a268b94a text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t95c7850df149447fbe3fa218530b5625", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "ta94bde4c06fa42a08d1365c11fa57643", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t57e8699bfef74f15b01e6ee0a268b94a .toyplot-mark-popup");
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
      var axes = {"t8186440888e248eda5458ac3191fd05e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "tc21a6e6751ef481c835209a4760afc03": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


You can use the ``area`` argument instead of ``size`` as an
approximation of the *area* of the markers (this is recommended if
you're using per-datum marker sizes to display data).

By default, the markers are small circles, but there are many
alternatives:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.axes(grid=(1, 2, 0)).scatterplot(y, marker="x", size=10)
    canvas.axes(grid=(1, 2, 1)).scatterplot(y, marker="^", size=10, mstyle={"stroke":toyplot.color.near_black});



.. raw:: html

    <div align="center" class="toyplot" id="t3f7d09c7d4a84cb3beb2b68ef2366ea5"><svg height="300.0px" id="t66ddaa1d73d34eb2af064a9ae205a6b8" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="ta3f3109a5d8a497c87c0262e693aa2c1"><clipPath id="t18abc853b36440488e71bb44aa14cf21"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t18abc853b36440488e71bb44aa14cf21)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Scatterplot" id="t43f4274b8428496982ee1047589de4e6" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 50.0, 250.0)" x1="50.0" x2="50.0" y1="245.0" y2="255.0"></line><line transform="rotate(-45, 50.0, 250.0)" x1="45.0" x2="55.0" y1="250.0" y2="250.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 60.0, 249.4459833795014)" x1="60.0" x2="60.0" y1="244.4459833795014" y2="254.4459833795014"></line><line transform="rotate(-45, 60.0, 249.4459833795014)" x1="55.0" x2="65.0" y1="249.4459833795014" y2="249.4459833795014"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 70.0, 247.78393351800551)" x1="70.0" x2="70.0" y1="242.78393351800551" y2="252.78393351800551"></line><line transform="rotate(-45, 70.0, 247.78393351800551)" x1="65.0" x2="75.0" y1="247.78393351800551" y2="247.78393351800551"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 80.0, 245.01385041551248)" x1="80.0" x2="80.0" y1="240.01385041551248" y2="250.01385041551248"></line><line transform="rotate(-45, 80.0, 245.01385041551248)" x1="75.0" x2="85.0" y1="245.01385041551248" y2="245.01385041551248"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 90.0, 241.13573407202216)" x1="90.0" x2="90.0" y1="236.13573407202216" y2="246.13573407202216"></line><line transform="rotate(-45, 90.0, 241.13573407202216)" x1="85.0" x2="95.0" y1="241.13573407202216" y2="241.13573407202216"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 100.0, 236.14958448753461)" x1="100.0" x2="100.0" y1="231.14958448753461" y2="241.14958448753461"></line><line transform="rotate(-45, 100.0, 236.14958448753461)" x1="95.0" x2="105.0" y1="236.14958448753461" y2="236.14958448753461"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 110.0, 230.05540166204986)" x1="110.0" x2="110.0" y1="225.05540166204986" y2="235.05540166204986"></line><line transform="rotate(-45, 110.0, 230.05540166204986)" x1="105.0" x2="115.0" y1="230.05540166204986" y2="230.05540166204986"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 120.0, 222.85318559556785)" x1="120.0" x2="120.0" y1="217.85318559556785" y2="227.85318559556785"></line><line transform="rotate(-45, 120.0, 222.85318559556785)" x1="115.0" x2="125.0" y1="222.85318559556785" y2="222.85318559556785"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 130.0, 214.54293628808864)" x1="130.0" x2="130.0" y1="209.54293628808864" y2="219.54293628808864"></line><line transform="rotate(-45, 130.0, 214.54293628808864)" x1="125.0" x2="135.0" y1="214.54293628808864" y2="214.54293628808864"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 140.0, 205.1246537396122)" x1="140.0" x2="140.0" y1="200.1246537396122" y2="210.1246537396122"></line><line transform="rotate(-45, 140.0, 205.1246537396122)" x1="135.0" x2="145.0" y1="205.1246537396122" y2="205.1246537396122"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 150.0, 194.5983379501385)" x1="150.0" x2="150.0" y1="189.5983379501385" y2="199.5983379501385"></line><line transform="rotate(-45, 150.0, 194.5983379501385)" x1="145.0" x2="155.0" y1="194.5983379501385" y2="194.5983379501385"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 160.0, 182.96398891966757)" x1="160.0" x2="160.0" y1="177.96398891966757" y2="187.96398891966757"></line><line transform="rotate(-45, 160.0, 182.96398891966757)" x1="155.0" x2="165.0" y1="182.96398891966757" y2="182.96398891966757"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 170.0, 170.22160664819947)" x1="170.0" x2="170.0" y1="165.22160664819947" y2="175.22160664819947"></line><line transform="rotate(-45, 170.0, 170.22160664819947)" x1="165.0" x2="175.0" y1="170.22160664819947" y2="170.22160664819947"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 180.0, 156.37119113573411)" x1="180.0" x2="180.0" y1="151.37119113573411" y2="161.37119113573411"></line><line transform="rotate(-45, 180.0, 156.37119113573411)" x1="175.0" x2="185.0" y1="156.37119113573411" y2="156.37119113573411"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 190.0, 141.41274238227149)" x1="190.0" x2="190.0" y1="136.41274238227149" y2="146.41274238227149"></line><line transform="rotate(-45, 190.0, 141.41274238227149)" x1="185.0" x2="195.0" y1="141.41274238227149" y2="141.41274238227149"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 200.0, 125.34626038781163)" x1="200.0" x2="200.0" y1="120.34626038781163" y2="130.34626038781164"></line><line transform="rotate(-45, 200.0, 125.34626038781163)" x1="195.0" x2="205.0" y1="125.34626038781163" y2="125.34626038781163"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 210.0, 108.17174515235459)" x1="210.0" x2="210.0" y1="103.17174515235459" y2="113.17174515235459"></line><line transform="rotate(-45, 210.0, 108.17174515235459)" x1="205.0" x2="215.0" y1="108.17174515235459" y2="108.17174515235459"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 220.0, 89.889196675900322)" x1="220.0" x2="220.0" y1="84.889196675900322" y2="94.889196675900322"></line><line transform="rotate(-45, 220.0, 89.889196675900322)" x1="215.0" x2="225.0" y1="89.889196675900322" y2="89.889196675900322"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 230.0, 70.498614958448783)" x1="230.0" x2="230.0" y1="65.498614958448783" y2="75.498614958448783"></line><line transform="rotate(-45, 230.0, 70.498614958448783)" x1="225.0" x2="235.0" y1="70.498614958448783" y2="70.498614958448783"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 240.0, 50.0)" x1="240.0" x2="240.0" y1="45.0" y2="55.0"></line><line transform="rotate(-45, 240.0, 50.0)" x1="235.0" x2="245.0" y1="50.0" y2="50.0"></line></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tcbf95e4d0d7848548bb467c19692ec0c" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="tbf1136e520ba4ff78fed667566fb233e" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="t78660879c5cc4e79b9e0cbefd6cc15a6"><clipPath id="tc82d5562111e4271830f75d983a0ed30"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tc82d5562111e4271830f75d983a0ed30)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect><g class="toyplot-mark-Scatterplot" id="tc4598fe3e929491e8c7bf354dd827e5c" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="345.0,255.0 350.0,245.0 355.0,255.0" transform="rotate(0, 350.0, 250.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="355.0,254.4459833795014 360.0,244.4459833795014 365.0,254.4459833795014" transform="rotate(0, 360.0, 249.4459833795014)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="365.0,252.78393351800551 370.0,242.78393351800551 375.0,252.78393351800551" transform="rotate(0, 370.0, 247.78393351800551)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="375.0,250.01385041551248 380.0,240.01385041551248 385.0,250.01385041551248" transform="rotate(0, 380.0, 245.01385041551248)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="385.0,246.13573407202216 390.0,236.13573407202216 395.0,246.13573407202216" transform="rotate(0, 390.0, 241.13573407202216)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="395.0,241.14958448753461 400.0,231.14958448753461 405.0,241.14958448753461" transform="rotate(0, 400.0, 236.14958448753461)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="405.0,235.05540166204986 410.0,225.05540166204986 415.0,235.05540166204986" transform="rotate(0, 410.0, 230.05540166204986)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="415.0,227.85318559556785 420.0,217.85318559556785 425.0,227.85318559556785" transform="rotate(0, 420.0, 222.85318559556785)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="425.0,219.54293628808864 430.0,209.54293628808864 435.0,219.54293628808864" transform="rotate(0, 430.0, 214.54293628808864)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="435.0,210.1246537396122 440.0,200.1246537396122 445.0,210.1246537396122" transform="rotate(0, 440.0, 205.1246537396122)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="445.0,199.5983379501385 450.0,189.5983379501385 455.0,199.5983379501385" transform="rotate(0, 450.0, 194.5983379501385)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="455.0,187.96398891966757 460.0,177.96398891966757 465.0,187.96398891966757" transform="rotate(0, 460.0, 182.96398891966757)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="465.0,175.22160664819947 470.0,165.22160664819947 475.0,175.22160664819947" transform="rotate(0, 470.0, 170.22160664819947)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="475.0,161.37119113573411 480.0,151.37119113573411 485.0,161.37119113573411" transform="rotate(0, 480.0, 156.37119113573411)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="485.0,146.41274238227149 490.0,136.41274238227149 495.0,146.41274238227149" transform="rotate(0, 490.0, 141.41274238227149)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="495.0,130.34626038781164 500.0,120.34626038781163 505.0,130.34626038781164" transform="rotate(0, 500.0, 125.34626038781163)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="505.0,113.17174515235459 510.0,103.17174515235459 515.0,113.17174515235459" transform="rotate(0, 510.0, 108.17174515235459)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="515.0,94.889196675900322 520.0,84.889196675900322 525.0,94.889196675900322" transform="rotate(0, 520.0, 89.889196675900322)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="525.0,75.498614958448783 530.0,65.498614958448783 535.0,75.498614958448783" transform="rotate(0, 530.0, 70.498614958448783)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="535.0,55.0 540.0,45.0 545.0,55.0" transform="rotate(0, 540.0, 50.0)"></polygon></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tec949ca2dccd4b15bc720f11462b4fc4" transform="translate(350.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="td05b006221fe4d37813a06b15f024ea1" transform="translate(350.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t3f7d09c7d4a84cb3beb2b68ef2366ea5 text");
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
          var text = document.querySelectorAll("#t3f7d09c7d4a84cb3beb2b68ef2366ea5 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t43f4274b8428496982ee1047589de4e6", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tc4598fe3e929491e8c7bf354dd827e5c", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t3f7d09c7d4a84cb3beb2b68ef2366ea5 .toyplot-mark-popup");
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
      var axes = {"t78660879c5cc4e79b9e0cbefd6cc15a6": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "ta3f3109a5d8a497c87c0262e693aa2c1": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Note the use of the *mstyle* argument to override the appearance of the
marker in the second example. For line plots, this allows you to style
the lines and the markers separately:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.axes(grid=(1, 2, 0)).plot(y, marker="o", size=8, style={"stroke":"darkgreen"})
    canvas.axes(grid=(1, 2, 1)).plot(y, marker="o", size=8, mstyle={"stroke":"darkgreen"});



.. raw:: html

    <div align="center" class="toyplot" id="t2ccafb5b42084115832530fd3ecdf4f7"><svg height="300.0px" id="tec45663b7a4c4e4ab4b8fed942a4eda2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tea09e0313ec4411cb92f5a03d6c8f2e1"><clipPath id="ta67aca7ad8d349e4b60d1fd6f918b4d5"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#ta67aca7ad8d349e4b60d1fd6f918b4d5)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t60057e5233054abda06a9068c67d6153" style="fill:none;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="fill:none;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="250.0" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.0" cy="249.4459833795014" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.0" cy="247.78393351800551" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.0" cy="245.01385041551248" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.0" cy="241.13573407202216" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.0" cy="236.14958448753461" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="110.0" cy="230.05540166204986" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.0" cy="222.85318559556785" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="130.0" cy="214.54293628808864" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="140.0" cy="205.1246537396122" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="150.0" cy="194.5983379501385" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.0" cy="182.96398891966757" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="170.0" cy="170.22160664819947" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="180.0" cy="156.37119113573411" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="190.0" cy="141.41274238227149" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="200.0" cy="125.34626038781163" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="210.0" cy="108.17174515235459" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="220.0" cy="89.889196675900322" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="230.0" cy="70.498614958448783" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="50.0" r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tbd31869d31764cbd8d14c88efaee19ca" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t6b4c1dd1419c488aa41cc2f1c4cea1a9" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="tca62716e86db495f81a39aa55bf035b3"><clipPath id="t50998b0e123f4084a122c3f17b2869d4"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t50998b0e123f4084a122c3f17b2869d4)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t4026dd7c359b465ca078eb030377a8b2" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t42569db64dc3472a8563ee678b1c0f7c" transform="translate(350.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t2744f1f52ce34eb2a282c84de2c74cf9" transform="translate(350.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t2ccafb5b42084115832530fd3ecdf4f7 text");
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
          var text = document.querySelectorAll("#t2ccafb5b42084115832530fd3ecdf4f7 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t60057e5233054abda06a9068c67d6153", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t4026dd7c359b465ca078eb030377a8b2", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t2ccafb5b42084115832530fd3ecdf4f7 .toyplot-mark-popup");
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
      var axes = {"tca62716e86db495f81a39aa55bf035b3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "tea09e0313ec4411cb92f5a03d6c8f2e1": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


So far, we've been using string codes to specify different marker
shapes. Here is every builtin marker shape in Toyplot, with their string
codes:

.. code:: python

    markers = [None, "","|","-","+","x","*","^",">","v","<","s","d","o","oo","o|","o-","o+","ox","o*"]
    labels = [repr(marker) for marker in markers]
    mstyle = {"stroke":toyplot.color.near_black, "fill":"#feb"}
    
    canvas = toyplot.Canvas(700, 150)
    axes = canvas.axes(xmin=-1, show=False)
    axes.scatterplot(numpy.repeat(0, len(markers)), marker=markers, mstyle=mstyle, size=15)
    axes.text(numpy.arange(len(markers)), numpy.repeat(-0.5, len(markers)), text=labels, color=toyplot.color.near_black, style={"font-size":"16px"});



.. raw:: html

    <div align="center" class="toyplot" id="td2980b77de634d57b004d13f506ab6c1"><svg height="150.0px" id="tcba2eea6844b4db6a2f7165b5de8a472" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 150.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t68173f7d473b4a11bb0c1f10cd8e47bc"><clipPath id="t77683238becd437495115e2be3559376"><rect height="70.0" width="620.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t77683238becd437495115e2be3559376)" style="cursor:crosshair"><rect height="70.0" style="pointer-events:all;visibility:hidden" width="620.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Scatterplot" id="tdaa876eecb934e11963b062eb874db3f" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(0, 135.65989847715736, 50.0)" x1="135.65989847715736" x2="135.65989847715736" y1="42.5" y2="57.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(-90, 164.21319796954316, 50.0)" x1="164.21319796954316" x2="164.21319796954316" y1="42.5" y2="57.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(0, 192.76649746192894, 50.0)" x1="192.76649746192894" x2="192.76649746192894" y1="42.5" y2="57.5"></line><line transform="rotate(0, 192.76649746192894, 50.0)" x1="185.26649746192894" x2="200.26649746192894" y1="50.0" y2="50.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(-45, 221.31979695431471, 50.0)" x1="221.31979695431471" x2="221.31979695431471" y1="42.5" y2="57.5"></line><line transform="rotate(-45, 221.31979695431471, 50.0)" x1="213.81979695431471" x2="228.81979695431471" y1="50.0" y2="50.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(0, 249.87309644670052, 50.0)" x1="249.87309644670052" x2="249.87309644670052" y1="42.5" y2="57.5"></line><line transform="rotate(60, 249.87309644670052, 50.0)" x1="249.87309644670052" x2="249.87309644670052" y1="42.5" y2="57.5"></line><line transform="rotate(-60, 249.87309644670052, 50.0)" x1="249.87309644670052" x2="249.87309644670052" y1="42.5" y2="57.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="270.92639593908632,57.5 278.42639593908632,42.5 285.92639593908632,57.5" transform="rotate(0, 278.42639593908632, 50.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="299.47969543147212,57.5 306.97969543147212,42.5 314.47969543147212,57.5" transform="rotate(-90, 306.97969543147212, 50.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="328.03299492385787,57.5 335.53299492385787,42.5 343.03299492385787,57.5" transform="rotate(-180, 335.53299492385787, 50.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="356.58629441624367,57.5 364.08629441624367,42.5 371.58629441624367,57.5" transform="rotate(90, 364.08629441624367, 50.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><rect height="15.0" transform="rotate(0, 392.63959390862942, 50.0)" width="15.0" x="385.13959390862942" y="42.5"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><rect height="15.0" transform="rotate(-45, 421.19289340101523, 50.0)" width="15.0" x="413.69289340101523" y="42.5"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="449.74619289340103" cy="50.0" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="478.29949238578683" cy="50.0" r="7.5"></circle><circle cx="478.29949238578683" cy="50.0" r="3.75"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="506.85279187817258" cy="50.0" r="7.5"></circle><line transform="rotate(0, 506.85279187817258, 50.0)" x1="506.85279187817258" x2="506.85279187817258" y1="42.5" y2="57.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="535.40609137055844" cy="50.0" r="7.5"></circle><line transform="rotate(-90, 535.40609137055844, 50.0)" x1="535.40609137055844" x2="535.40609137055844" y1="42.5" y2="57.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="563.95939086294425" cy="50.0" r="7.5"></circle><line transform="rotate(0, 563.95939086294425, 50.0)" x1="563.95939086294425" x2="563.95939086294425" y1="42.5" y2="57.5"></line><line transform="rotate(0, 563.95939086294425, 50.0)" x1="556.45939086294425" x2="571.45939086294425" y1="50.0" y2="50.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="592.51269035533005" cy="50.0" r="7.5"></circle><line transform="rotate(-45, 592.51269035533005, 50.0)" x1="592.51269035533005" x2="592.51269035533005" y1="42.5" y2="57.5"></line><line transform="rotate(-45, 592.51269035533005, 50.0)" x1="585.01269035533005" x2="600.01269035533005" y1="50.0" y2="50.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="621.06598984771574" cy="50.0" r="7.5"></circle><line transform="rotate(0, 621.06598984771574, 50.0)" x1="621.06598984771574" x2="621.06598984771574" y1="42.5" y2="57.5"></line><line transform="rotate(60, 621.06598984771574, 50.0)" x1="621.06598984771574" x2="621.06598984771574" y1="42.5" y2="57.5"></line><line transform="rotate(-60, 621.06598984771574, 50.0)" x1="621.06598984771574" x2="621.06598984771574" y1="42.5" y2="57.5"></line></g></g></g><g class="toyplot-mark-Text" id="t8f4a1d7fa1654738825223555d99a9a7" style="alignment-baseline:middle;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 78.55329949238579, 91.666666666666671)" x="78.55329949238579" y="91.666666666666671">None</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 107.10659898477158, 91.666666666666671)" x="107.10659898477158" y="91.666666666666671">''</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 135.65989847715736, 91.666666666666671)" x="135.65989847715736" y="91.666666666666671">'|'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 164.21319796954316, 91.666666666666671)" x="164.21319796954316" y="91.666666666666671">'-'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 192.76649746192894, 91.666666666666671)" x="192.76649746192894" y="91.666666666666671">'+'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 221.31979695431471, 91.666666666666671)" x="221.31979695431471" y="91.666666666666671">'x'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 249.87309644670052, 91.666666666666671)" x="249.87309644670052" y="91.666666666666671">'*'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 278.42639593908632, 91.666666666666671)" x="278.42639593908632" y="91.666666666666671">'^'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 306.97969543147212, 91.666666666666671)" x="306.97969543147212" y="91.666666666666671">'&gt;'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 335.53299492385787, 91.666666666666671)" x="335.53299492385787" y="91.666666666666671">'v'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 364.08629441624367, 91.666666666666671)" x="364.08629441624367" y="91.666666666666671">'&lt;'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 392.63959390862942, 91.666666666666671)" x="392.63959390862942" y="91.666666666666671">'s'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 421.19289340101523, 91.666666666666671)" x="421.19289340101523" y="91.666666666666671">'d'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 449.74619289340103, 91.666666666666671)" x="449.74619289340103" y="91.666666666666671">'o'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 478.29949238578683, 91.666666666666671)" x="478.29949238578683" y="91.666666666666671">'oo'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 506.85279187817258, 91.666666666666671)" x="506.85279187817258" y="91.666666666666671">'o|'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 535.40609137055844, 91.666666666666671)" x="535.40609137055844" y="91.666666666666671">'o-'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 563.95939086294425, 91.666666666666671)" x="563.95939086294425" y="91.666666666666671">'o+'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 592.51269035533005, 91.666666666666671)" x="592.51269035533005" y="91.666666666666671">'ox'</text><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 621.06598984771574, 91.666666666666671)" x="621.06598984771574" y="91.666666666666671">'o*'</text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#td2980b77de634d57b004d13f506ab6c1 text");
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
          var text = document.querySelectorAll("#td2980b77de634d57b004d13f506ab6c1 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "tdaa876eecb934e11963b062eb874db3f", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#td2980b77de634d57b004d13f506ab6c1 .toyplot-mark-popup");
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
      var axes = {"t68173f7d473b4a11bb0c1f10cd8e47bc": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.013333333333332, "min": -1.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 650.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.0, "min": -0.60000000000000009}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 100.0}, "scale": "linear"}]}};
    
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
    canvas.axes(grid=(1, 2, 0)).scatterplot(y, marker={"shape":"|", "angle":45}, size=10)
    canvas.axes(grid=(1, 2, 1)).scatterplot(y, marker={"shape":"o", "label":"A"}, size=15, mlstyle={"fill":"white"});



.. raw:: html

    <div align="center" class="toyplot" id="t0b458d19411d4deeb7aac440c2b62779"><svg height="300.0px" id="t91bfa41d213d4ad68fb936007d68c7f9" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t2def4807c330476691bc564f522059a3"><clipPath id="t35e28ea98ceb425fb85fbd98f8b1b185"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t35e28ea98ceb425fb85fbd98f8b1b185)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Scatterplot" id="t5f0cd539b33f4ac2800dae361fa0351a" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 50.0, 250.0)" x1="50.0" x2="50.0" y1="245.0" y2="255.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 60.0, 249.4459833795014)" x1="60.0" x2="60.0" y1="244.4459833795014" y2="254.4459833795014"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 70.0, 247.78393351800551)" x1="70.0" x2="70.0" y1="242.78393351800551" y2="252.78393351800551"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 80.0, 245.01385041551248)" x1="80.0" x2="80.0" y1="240.01385041551248" y2="250.01385041551248"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 90.0, 241.13573407202216)" x1="90.0" x2="90.0" y1="236.13573407202216" y2="246.13573407202216"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 100.0, 236.14958448753461)" x1="100.0" x2="100.0" y1="231.14958448753461" y2="241.14958448753461"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 110.0, 230.05540166204986)" x1="110.0" x2="110.0" y1="225.05540166204986" y2="235.05540166204986"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 120.0, 222.85318559556785)" x1="120.0" x2="120.0" y1="217.85318559556785" y2="227.85318559556785"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 130.0, 214.54293628808864)" x1="130.0" x2="130.0" y1="209.54293628808864" y2="219.54293628808864"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 140.0, 205.1246537396122)" x1="140.0" x2="140.0" y1="200.1246537396122" y2="210.1246537396122"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 150.0, 194.5983379501385)" x1="150.0" x2="150.0" y1="189.5983379501385" y2="199.5983379501385"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 160.0, 182.96398891966757)" x1="160.0" x2="160.0" y1="177.96398891966757" y2="187.96398891966757"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 170.0, 170.22160664819947)" x1="170.0" x2="170.0" y1="165.22160664819947" y2="175.22160664819947"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 180.0, 156.37119113573411)" x1="180.0" x2="180.0" y1="151.37119113573411" y2="161.37119113573411"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 190.0, 141.41274238227149)" x1="190.0" x2="190.0" y1="136.41274238227149" y2="146.41274238227149"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 200.0, 125.34626038781163)" x1="200.0" x2="200.0" y1="120.34626038781163" y2="130.34626038781164"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 210.0, 108.17174515235459)" x1="210.0" x2="210.0" y1="103.17174515235459" y2="113.17174515235459"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 220.0, 89.889196675900322)" x1="220.0" x2="220.0" y1="84.889196675900322" y2="94.889196675900322"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 230.0, 70.498614958448783)" x1="230.0" x2="230.0" y1="65.498614958448783" y2="75.498614958448783"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 240.0, 50.0)" x1="240.0" x2="240.0" y1="45.0" y2="55.0"></line></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t16456a00d81e42e8bdcbd4d12b0d9c9d" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="tc0337762334c45079b9d9bb28c33a8a5" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="t4f2bb858e87f43eea4524e7535706c31"><clipPath id="t2377b908cc904fa099a3cf1833f9a710"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2377b908cc904fa099a3cf1833f9a710)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect><g class="toyplot-mark-Scatterplot" id="t3e4fcbfafb2446c9823d6e2e89bfd2fd" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="350.0" y="250.0">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="360.0" y="249.4459833795014">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="370.0" y="247.78393351800551">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="380.0" y="245.01385041551248">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="390.0" y="241.13573407202216">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="400.0" y="236.14958448753461">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="410.0" y="230.05540166204986">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="420.0" y="222.85318559556785">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="430.0" y="214.54293628808864">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="440.0" y="205.1246537396122">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="450.0" y="194.5983379501385">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="460.0" y="182.96398891966757">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="470.0" y="170.22160664819947">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="480.0" y="156.37119113573411">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="490.0" y="141.41274238227149">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="500.0" y="125.34626038781163">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="510.0" y="108.17174515235459">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="520.0" y="89.889196675900322">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="530.0" y="70.498614958448783">A</text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="7.5"></circle><text style="alignment-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:11.25px;stroke:none;text-anchor:middle" x="540.0" y="50.0">A</text></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t049ccc6189e44605b9f54f72b0dd349b" transform="translate(350.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="tae6e691baefc4fb3b23349e82ad1e724" transform="translate(350.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t0b458d19411d4deeb7aac440c2b62779 text");
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
          var text = document.querySelectorAll("#t0b458d19411d4deeb7aac440c2b62779 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t5f0cd539b33f4ac2800dae361fa0351a", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t3e4fcbfafb2446c9823d6e2e89bfd2fd", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t0b458d19411d4deeb7aac440c2b62779 .toyplot-mark-popup");
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
      var axes = {"t2def4807c330476691bc564f522059a3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "t4f2bb858e87f43eea4524e7535706c31": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Using the full marker specification allows you to control additional
parameters such as the marker angle and label. Also note the *mlstyle*
argument which controls the style of the marker label, independently of
the marker itself.

You can also use custom marker shapes, specifying the shape as an SVG
path:

.. code:: python

    custom_marker = {"shape":"path", "path":"m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z"}
    canvas, axes, mark = toyplot.scatterplot(0, 0, size=0.5, marker=custom_marker, color="#004712", width=400);
    axes.hlines(0, style={"stroke-width":0.1})
    axes.vlines(0, style={"stroke-width":0.1});



.. raw:: html

    <div align="center" class="toyplot" id="tfd3277dc30254a3d9f743fb049c3c91a"><svg height="400.0px" id="t608f3fb1e86e4ce7882ab0a74b425f35" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 400.0 400.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t905c9ad37cf94806aa3f5957a7e6e46d"><clipPath id="t5bca29964b8a452da0098452f8f9125f"><rect height="320.0" width="320.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t5bca29964b8a452da0098452f8f9125f)" style="cursor:crosshair"><rect height="320.0" style="pointer-events:all;visibility:hidden" width="320.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Scatterplot" id="te49ae84ba06044569f7c5a6d945714e7" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 200.0 200.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(200.0, 200.0) scale(0.5) translate(-200.0, -200.0)"></path></g></g></g><g class="toyplot-mark-AxisLines" id="tf4ac0a01421b4b369ae8e3a47cfd8e80" style="stroke-width:0.1"><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.1" x1="50.0" x2="350.0" y1="200.0" y2="200.0"></line></g></g><g class="toyplot-mark-AxisLines" id="t1b46c6479e1c4b88972f9f07c504a487" style="stroke-width:0.1"><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.1" x1="200.0" x2="200.0" y1="50.0" y2="350.0"></line></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="250.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="295.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t8fb660d37acb4a1e948438b91facbdf7" transform="translate(50.0,350.0) rotate(0.0) translate(0,10.0)"><line style="" x1="150.0" x2="150.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,0) rotate(0)" x="0" y="0">0.5</text></g></g><g class="toyplot-axes-Axis" id="t584cf2db2e874863ab7b648b0280f02d" transform="translate(50.0,350.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="150.0" x2="150.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,0) rotate(0)" x="0" y="0">0.5</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tfd3277dc30254a3d9f743fb049c3c91a text");
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
          var text = document.querySelectorAll("#tfd3277dc30254a3d9f743fb049c3c91a text");
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
      var data_tables = [{"data": [[0.0], [0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "te49ae84ba06044569f7c5a6d945714e7", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tfd3277dc30254a3d9f743fb049c3c91a .toyplot-mark-popup");
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
      var axes = {"t905c9ad37cf94806aa3f5957a7e6e46d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 350.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 350.0}, "scale": "linear"}]}};
    
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


Note that the SVG path must contain only relative coordinates, or the
marker will not render correctly. In this example the marker was
exported as SVG from a drawing application, the path was run through an
`online conversion process <http://bl.ocks.org/themcmurder/6393419>`__
to convert absolute coordinates to relative coordinates, and the initial
"move" (m) command was adjusted to center the graphic. Note that, for
custom markers to be displayed with sizes similar to the builtin
markers, they should be defined within a unit square. Here is an
(admittedly silly) example of a custom marker at work:

.. code:: python

    x = numpy.linspace(0, 100, 10)
    y = 5 + (0.1 * x) ** 2
    
    canvas = toyplot.Canvas(width=600)
    axes = canvas.axes(xlabel="Years", ylabel="Oak Tree Population", gutter=75, padding=35)
    axes.scatterplot(x, y, size=.15, color="#004712", marker=custom_marker);



.. raw:: html

    <div align="center" class="toyplot" id="ta36120615df543adbb408c82774f8c40"><svg height="600.0px" id="t1c105515f8624c3bb2f5c73d1f173973" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 600.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t93e2320b15b4450daa19bce1fc635860"><clipPath id="tae89b856e1ff4889ae6478d1432b2c05"><rect height="520.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tae89b856e1ff4889ae6478d1432b2c05)" style="cursor:crosshair"><rect height="520.0" style="pointer-events:all;visibility:hidden" width="520.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Scatterplot" id="t1c3042b9d7fc4299aa3c7600f90f740d" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 75.0 503.57142857142856m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(75.0, 503.57142857142856) scale(0.14999999999999999) translate(-75.0, -503.57142857142856)"></path></g><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 124.99999999999999 498.28042328042324m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(124.99999999999999, 498.28042328042324) scale(0.14999999999999999) translate(-124.99999999999999, -498.28042328042324)"></path></g><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 175.0 482.40740740740745m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(175.0, 482.40740740740745) scale(0.14999999999999999) translate(-175.0, -482.40740740740745)"></path></g><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 224.99999999999997 455.95238095238096m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(224.99999999999997, 455.95238095238096) scale(0.14999999999999999) translate(-224.99999999999997, -455.95238095238096)"></path></g><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 275.0 418.91534391534395m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(275.0, 418.91534391534395) scale(0.14999999999999999) translate(-275.0, -418.91534391534395)"></path></g><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 325.0 371.29629629629619m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(325.0, 371.29629629629619) scale(0.14999999999999999) translate(-325.0, -371.29629629629619)"></path></g><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 374.99999999999994 313.09523809523813m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(374.99999999999994, 313.09523809523813) scale(0.14999999999999999) translate(-374.99999999999994, -313.09523809523813)"></path></g><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 424.99999999999994 244.31216931216932m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(424.99999999999994, 244.31216931216932) scale(0.14999999999999999) translate(-424.99999999999994, -244.31216931216932)"></path></g><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 474.99999999999994 164.94708994708992m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(474.99999999999994, 164.94708994708992) scale(0.14999999999999999) translate(-474.99999999999994, -164.94708994708992)"></path></g><g class="toyplot-Datum" style="fill:rgb(0%,27.8%,7.06%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,27.8%,7.06%);stroke-opacity:1.0"><path d="M 525.0 75.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(525.0, 75.0) scale(0.14999999999999999) translate(-525.0, -75.0)"></path></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="425.0" y="85.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="470.0" y="92.0"></text></g><g class="toyplot-axes-Axis" id="t14fdf20edc814c4b99ea16b6c9756531" transform="translate(75.0,525.0) rotate(0.0) translate(0,35.0)"><line style="" x1="0" x2="450.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(225.0,0) rotate(0)" x="0" y="0">50</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(450.0,0) rotate(0)" x="0" y="0">100</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="225.0" y="0">Years</text></g><g class="toyplot-axes-Axis" id="t5b1d515571474c91bed8f254bd9c7a7f" transform="translate(75.0,525.0) rotate(-90.0) translate(0,-35.0)"><line style="" x1="21.428571428571427" x2="450.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(214.28571428571428,0) rotate(0)" x="0" y="0">50</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(428.57142857142856,0) rotate(0)" x="0" y="0">100</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" x="225.0" y="0">Oak Tree Population</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#ta36120615df543adbb408c82774f8c40 text");
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
          var text = document.querySelectorAll("#ta36120615df543adbb408c82774f8c40 text");
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
      var data_tables = [{"data": [[0.0, 11.11111111111111, 22.22222222222222, 33.33333333333333, 44.44444444444444, 55.55555555555556, 66.66666666666666, 77.77777777777777, 88.88888888888889, 100.0], [5.0, 6.234567901234568, 9.938271604938272, 16.111111111111107, 24.75308641975309, 35.8641975308642, 49.444444444444436, 65.49382716049382, 84.01234567901236, 105.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "t1c3042b9d7fc4299aa3c7600f90f740d", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#ta36120615df543adbb408c82774f8c40 .toyplot-mark-popup");
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
      var axes = {"t93e2320b15b4450daa19bce1fc635860": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 100.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 525.0, "min": 75.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 105.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 75.0, "min": 525.0}, "scale": "linear"}]}};
    
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



