
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _labels-and-legends:

Labels and Legends
==================

Of course, most figures require proper labels before they can be of
value, so Toyplot provides several labelling mechanisms to help:

Axes Labels
-----------

First, both :ref:`cartesian-axes` and :ref:`table-axes` provide
labelling parameters that can be specified when they are created. In
either case the ``label`` parameter provides a top-level label for the
set of axes:

.. code:: python

    import numpy
    import toyplot
    
    canvas = toyplot.Canvas(width=600, height=300)
    canvas.axes(grid=(1,2,0), label="Cartesian Axes").plot(numpy.linspace(0, 1)**2)
    canvas.table(grid=(1,2,1), label="Table Axes", data = numpy.random.random((4, 3)));



.. raw:: html

    <div align="center" class="toyplot" id="tb856c658db234758ab20dc0b2e09f8bd"><svg height="300.0px" id="t5f03df5d6563449fb1750782767d8e28" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t476ff85fbd3646238d757860c7a405b3"><clipPath id="t06fc1c54287744d38577483991eb6d64"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t06fc1c54287744d38577483991eb6d64)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="td2c4ab51fc1a48a1978676735bbe6152" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 63.599999999999994 239.92503123698458 L 67.199999999999989 239.70012494793838 L 70.799999999999997 239.32528113286131 L 74.400000000000006 238.80049979175345 L 78.0 238.12578092461476 L 81.599999999999994 237.30112453144525 L 85.200000000000003 236.32653061224491 L 88.799999999999997 235.20199916701375 L 92.400000000000006 233.92753019575176 L 96.0 232.50312369845898 L 99.599999999999994 230.92877967513536 L 103.19999999999999 229.20449812578093 L 106.80000000000001 227.33027905039569 L 110.40000000000001 225.30612244897958 L 114.0 223.13202832153269 L 117.59999999999999 220.80799666805498 L 121.2 218.33402748854647 L 124.79999999999998 215.71012078300706 L 128.40000000000001 212.93627655143689 L 132.0 210.01249479383591 L 135.59999999999999 206.9387755102041 L 139.19999999999999 203.71511870054144 L 142.80000000000001 200.341524364848 L 146.39999999999998 196.81799250312369 L 150.0 193.1445231153686 L 153.60000000000002 189.3211162015827 L 157.20000000000002 185.34777176176596 L 160.80000000000001 181.2244897959184 L 164.39999999999998 176.95127030403995 L 168.0 172.5281132861308 L 171.60000000000002 167.95501874219076 L 175.19999999999999 163.2319866722199 L 178.80000000000001 158.35901707621824 L 182.40000000000001 153.33610995418576 L 186.0 148.16326530612247 L 189.59999999999999 142.84048313202834 L 193.19999999999999 137.36776343190337 L 196.80000000000001 131.74510620574762 L 200.40000000000001 125.97251145356105 L 204.0 120.04997917534362 L 207.59999999999999 113.97750937109539 L 211.19999999999999 107.75510204081634 L 214.80000000000001 101.38275718450647 L 218.39999999999998 94.860474802165797 L 222.0 88.188254893794294 L 225.60000000000002 81.366097459391938 L 229.19999999999999 74.39400249895877 L 232.79999999999998 67.271970012494791 L 236.39999999999998 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="236.39999999999998" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="96.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="132.0" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="168.0" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="204.0" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="50.0">Cartesian Axes</text></g><g class="toyplot-axes-Table" id="t288f0acb920c47dcb3c0d926cb829a51"><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="450.0" y="50.0">Table Axes</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="383.33333333333337" y="70.0">C0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="450.0" y="70.0">C1</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" x="516.66666666666674" y="70.0">C2</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="381.33333333333337" y="110.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="383.33333333333337" y="110.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="385.33333333333337" y="110.0">0632726</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="448.0" y="110.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="450.0" y="110.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="452.0" y="110.0">755392</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="514.66666666666674" y="110.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="516.66666666666674" y="110.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="518.66666666666674" y="110.0">187544</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="381.33333333333337" y="150.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="383.33333333333337" y="150.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="385.33333333333337" y="150.0">153811</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="448.0" y="150.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="450.0" y="150.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="452.0" y="150.0">449488</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="514.66666666666674" y="150.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="516.66666666666674" y="150.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="518.66666666666674" y="150.0">988924</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="381.33333333333337" y="190.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="383.33333333333337" y="190.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="385.33333333333337" y="190.0">340195</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="448.0" y="190.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="450.0" y="190.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="452.0" y="190.0">0454077</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="514.66666666666674" y="190.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="516.66666666666674" y="190.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="518.66666666666674" y="190.0">146675</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="381.33333333333337" y="230.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="383.33333333333337" y="230.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="385.33333333333337" y="230.0">130214</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="448.0" y="230.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="450.0" y="230.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="452.0" y="230.0">558287</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:end" x="514.66666666666674" y="230.0">0</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:middle" x="516.66666666666674" y="230.0">.</text><text style="alignment-baseline:middle;fill:#292724;font-size:12px;stroke:none;text-anchor:begin" x="518.66666666666674" y="230.0">570324</text><line style="stroke:#292724;stroke-width:0.5" x1="350.0" x2="550.0" y1="90.0" y2="90.0"></line></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tb856c658db234758ab20dc0b2e09f8bd text");
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
          var text = document.querySelectorAll("#tb856c658db234758ab20dc0b2e09f8bd text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "names": ["x", "y0"], "id": "td2c4ab51fc1a48a1978676735bbe6152", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tb856c658db234758ab20dc0b2e09f8bd .toyplot-mark-popup");
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
      var axes = {"t476ff85fbd3646238d757860c7a405b3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Naturally, some axes - such as Cartesian axes - allow you to specify
additional, axis-specific labels:

.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.axes(label="Cartesian Axes", xlabel="Days", ylabel="Users")
    axes.plot(numpy.linspace(0, 1)**2);



.. raw:: html

    <div align="center" class="toyplot" id="td546332989374c8184f2bf9af030f6f2"><svg height="300.0px" id="t4889113db3824e87bea9693b73c2e53b" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tfb35bd996c2f43078e721e3abe476289"><clipPath id="t7ad2c52227dc42399d679c234687b045"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t7ad2c52227dc42399d679c234687b045)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t887180998c3d42798522a186da7689ac" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 63.599999999999994 239.92503123698458 L 67.199999999999989 239.70012494793838 L 70.799999999999997 239.32528113286131 L 74.400000000000006 238.80049979175345 L 78.0 238.12578092461476 L 81.599999999999994 237.30112453144525 L 85.200000000000003 236.32653061224491 L 88.799999999999997 235.20199916701375 L 92.400000000000006 233.92753019575176 L 96.0 232.50312369845898 L 99.599999999999994 230.92877967513536 L 103.19999999999999 229.20449812578093 L 106.80000000000001 227.33027905039569 L 110.40000000000001 225.30612244897958 L 114.0 223.13202832153269 L 117.59999999999999 220.80799666805498 L 121.2 218.33402748854647 L 124.79999999999998 215.71012078300706 L 128.40000000000001 212.93627655143689 L 132.0 210.01249479383591 L 135.59999999999999 206.9387755102041 L 139.19999999999999 203.71511870054144 L 142.80000000000001 200.341524364848 L 146.39999999999998 196.81799250312369 L 150.0 193.1445231153686 L 153.60000000000002 189.3211162015827 L 157.20000000000002 185.34777176176596 L 160.80000000000001 181.2244897959184 L 164.39999999999998 176.95127030403995 L 168.0 172.5281132861308 L 171.60000000000002 167.95501874219076 L 175.19999999999999 163.2319866722199 L 178.80000000000001 158.35901707621824 L 182.40000000000001 153.33610995418576 L 186.0 148.16326530612247 L 189.59999999999999 142.84048313202834 L 193.19999999999999 137.36776343190337 L 196.80000000000001 131.74510620574762 L 200.40000000000001 125.97251145356105 L 204.0 120.04997917534362 L 207.59999999999999 113.97750937109539 L 211.19999999999999 107.75510204081634 L 214.80000000000001 101.38275718450647 L 218.39999999999998 94.860474802165797 L 222.0 88.188254893794294 L 225.60000000000002 81.366097459391938 L 229.19999999999999 74.39400249895877 L 232.79999999999998 67.271970012494791 L 236.39999999999998 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="236.39999999999998" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="96.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="132.0" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="168.0" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="204.0" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">50</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="250.0">Days</text><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">Users</text><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="50.0">Cartesian Axes</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#td546332989374c8184f2bf9af030f6f2 text");
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
          var text = document.querySelectorAll("#td546332989374c8184f2bf9af030f6f2 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "names": ["x", "y0"], "id": "t887180998c3d42798522a186da7689ac", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#td546332989374c8184f2bf9af030f6f2 .toyplot-mark-popup");
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
      var axes = {"tfb35bd996c2f43078e721e3abe476289": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Axes Text
---------

Another option for labelling a plot is to insert text labels using the
same domain as the data:

.. code:: python

    def series(x):
        return numpy.cumsum(numpy.random.normal(loc=0.05, size=len(x)))
    
    numpy.random.seed(1234)
    x = numpy.arange(100)
    y = numpy.column_stack([series(x) for i in range(5)])

.. code:: python

    label_style = {"text-anchor":"start", "-toyplot-anchor-shift":"5px"}
    canvas, axes, mark = toyplot.plot(x, y)
    for i in range(y.shape[1]):
        axes.text(x[-1], y[-1,i], "Series %s" % i, style=label_style)



.. raw:: html

    <div align="center" class="toyplot" id="t2de355270b654d4bb72e245fda1fd75e"><svg height="600px" id="t31774e4b1703407f8b9263636b0b1769" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tcd04d2690ddd4a96a3f9254ac86430f0"><clipPath id="tca11515c18ee4dcd9655ab0eca333940"><rect height="500.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tca11515c18ee4dcd9655ab0eca333940)" style="cursor:crosshair"><rect height="500.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t2d2e93d4638848fb871fa57adaf9991d" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 342.12524837162505 L 64.0 356.99663865434957 L 68.0 337.6711489838159 L 72.0 341.0945337880666 L 76.0 349.83493625179705 L 80.0 337.62002588299418 L 84.0 325.76451979308041 L 88.0 333.4092224669842 L 92.0 332.55294095774127 L 96.0 361.1322296069514 L 100.0 345.49105539235802 L 104.0 331.91041031492119 L 108.0 318.83316006457915 L 112.0 344.52634521640067 L 116.0 348.2289879606945 L 120.0 347.54968116590351 L 124.0 341.61333609695686 L 128.0 337.19363757100535 L 132.0 319.32206615268774 L 136.0 338.83261909586577 L 140.0 340.82219966214416 L 144.0 348.7203579295516 L 148.0 345.54762225302164 L 152.0 337.68244545893691 L 156.0 319.85006233059744 L 160.0 325.3152554678399 L 164.0 315.85843879668732 L 168.0 338.88973705197901 L 172.0 340.62466362416586 L 176.0 326.17044371711563 L 180.0 330.70416675222805 L 184.0 325.65433389089026 L 188.0 311.34857838779624 L 192.0 297.06420265497195 L 196.0 285.15488108417799 L 200.0 286.09451717864522 L 204.0 283.81732184925374 L 208.0 287.37290856343407 L 212.0 275.75088828401562 L 216.0 243.93559488330024 L 220.0 242.29071906959643 L 224.0 249.02203598327097 L 228.0 247.89926854301615 L 232.0 274.29267232308877 L 236.0 270.41127147804178 L 240.0 281.45304846813087 L 244.0 282.58432571263478 L 248.0 281.69424959501237 L 252.0 271.19654510667306 L 256.0 267.73905463107099 L 260.0 256.12571387697739 L 264.0 274.31859608524036 L 268.0 291.94011283997492 L 272.0 292.60377677904677 L 276.0 299.09783090452441 L 280.0 300.33109436828522 L 284.0 295.06512413757264 L 288.0 294.87630201269803 L 292.0 286.85081583979911 L 296.0 266.05312054116496 L 300.0 278.09954650509781 L 304.0 278.36472008335437 L 308.0 273.69898129533635 L 312.0 275.76484209886826 L 316.0 261.63866591710297 L 320.0 292.27429951739924 L 324.0 265.15587042842213 L 328.0 279.39714341045027 L 332.0 275.98377529805163 L 336.0 266.14680417700708 L 340.0 275.73241070002985 L 344.0 269.05826309571535 L 348.0 259.22770986383398 L 352.0 251.7526507014253 L 356.0 263.17368266896551 L 360.0 236.35191441960211 L 364.0 232.74200574848251 L 368.0 247.11398057542311 L 372.0 238.22511243346591 L 376.0 237.05841089438115 L 380.0 230.35386051722529 L 384.0 276.14876900425304 L 388.0 258.27788286610581 L 392.0 255.63681168552043 L 396.0 252.84064996627978 L 400.0 257.79478824462439 L 404.0 247.14126641180525 L 408.0 233.65220003485916 L 412.0 229.47045002324296 L 416.0 210.67571183159475 L 420.0 208.98335701551801 L 424.0 213.54476869923226 L 428.0 226.28999838625026 L 432.0 233.25947481579453 L 436.0 221.96435559623285 L 440.0 222.38075103594377 L 444.0 226.22270880980477 L 448.0 218.68534517928245 L 452.0 231.96676735431862 L 456.0 237.98689315032672" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 60.0 344.47434990651385 L 64.0 336.43849667715693 L 68.0 329.22302386275948 L 72.0 324.85280545088767 L 76.0 317.88893489257043 L 80.0 299.46572454179005 L 84.0 308.99489511132822 L 88.0 314.4433055288506 L 92.0 297.8306004840602 L 96.0 313.87677195370657 L 100.0 301.81419473578825 L 104.0 323.45983175218254 L 108.0 328.68337357527912 L 112.0 318.26713341101566 L 116.0 320.27348266082942 L 120.0 321.99624690706224 L 124.0 312.47293220896233 L 128.0 335.52341332151946 L 132.0 334.2581890218184 L 136.0 328.46012348667404 L 140.0 331.04647176647643 L 144.0 338.44591696730777 L 148.0 346.69487876251048 L 152.0 340.35703419172251 L 156.0 361.90227675930538 L 160.0 356.11898661299756 L 164.0 361.71476296873811 L 168.0 364.96042236064 L 172.0 355.26183679648716 L 176.0 345.76493313799051 L 180.0 341.99088235813286 L 184.0 339.36810980180354 L 188.0 328.07907342569797 L 192.0 302.7471932378503 L 196.0 293.75857234014944 L 200.0 305.64588665480613 L 204.0 332.17338398311239 L 208.0 306.36299847559235 L 212.0 328.32970731179404 L 216.0 311.90196212091735 L 220.0 300.85655342361935 L 224.0 305.15528205716998 L 228.0 295.34644336140605 L 232.0 305.77809569399028 L 236.0 289.78791568063815 L 240.0 295.9703763063647 L 244.0 286.18310214744059 L 248.0 272.70357362040414 L 252.0 273.63847623453694 L 256.0 242.1515319648914 L 260.0 235.03314667056949 L 264.0 223.99869367394837 L 268.0 229.52534965298705 L 272.0 229.61262111163512 L 276.0 211.26349889861052 L 280.0 221.10194415447853 L 284.0 248.12935250812885 L 288.0 251.82450171888604 L 292.0 262.73023801602938 L 296.0 257.72263145374905 L 300.0 250.07453578247043 L 304.0 259.11786794060208 L 308.0 262.6396847569938 L 312.0 273.92965472577589 L 316.0 284.48280966539659 L 320.0 280.88563585650024 L 324.0 272.03852344406022 L 328.0 268.95607411882025 L 332.0 255.88984773970967 L 336.0 242.35884157583067 L 340.0 242.65351661766829 L 344.0 249.17833698634391 L 348.0 260.75445049698146 L 352.0 276.25271865771174 L 356.0 273.78040131448375 L 360.0 276.03551754336712 L 364.0 247.7037830641469 L 368.0 245.45838424619274 L 372.0 263.17711397979662 L 376.0 243.97832728672648 L 380.0 271.32161002808601 L 384.0 288.23354995956635 L 388.0 282.84318103242111 L 392.0 282.38376274294518 L 396.0 265.14776603218763 L 400.0 283.38961058999956 L 404.0 298.32027977032692 L 408.0 305.38288048199541 L 412.0 310.13380884380001 L 416.0 328.06581258831221 L 420.0 324.68488068884392 L 424.0 331.76081550461083 L 428.0 350.30960642153178 L 432.0 361.34387366697229 L 436.0 346.29814324649652 L 440.0 351.27123056443747 L 444.0 352.71978055983232 L 448.0 340.47887332920425 L 452.0 336.06849527438834 L 456.0 349.12247748720063" style="fill:none;stroke:rgba(98.8%,55.3%,38.4%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 60.0 352.43503732134519 L 64.0 359.86428380335548 L 68.0 357.1662827343485 L 72.0 363.96289205468787 L 76.0 349.52608552677134 L 80.0 359.19059418123084 L 84.0 365.37685084988999 L 88.0 363.78830176967813 L 92.0 338.2319127695846 L 96.0 327.30994492759208 L 100.0 319.97077515346598 L 104.0 326.44102713244979 L 108.0 312.1826358318736 L 112.0 284.05822853526229 L 116.0 264.37794876993109 L 120.0 250.49153519777258 L 124.0 240.07502399299636 L 128.0 248.22802328931536 L 132.0 241.83792848989506 L 136.0 232.20622561105793 L 140.0 235.16031396757751 L 144.0 209.42439709886128 L 148.0 203.41309902851683 L 152.0 191.1512402593342 L 156.0 187.54914300930406 L 160.0 213.98999409117133 L 164.0 218.39397749770285 L 168.0 218.87762691732166 L 172.0 203.5447037312866 L 176.0 199.67217225752151 L 180.0 197.44113198708109 L 184.0 192.89250195760252 L 188.0 194.28842394821012 L 192.0 203.28794458966001 L 196.0 218.89806154883229 L 200.0 214.9949850877031 L 204.0 206.76962350331073 L 208.0 170.09419413148481 L 212.0 164.23772061650948 L 216.0 154.87300055511619 L 220.0 157.81571813447499 L 224.0 150.64076595088105 L 228.0 138.73994811726539 L 232.0 151.79508933128514 L 236.0 169.28731993664974 L 240.0 153.59548916999813 L 244.0 137.53842354466062 L 248.0 131.78562171059295 L 252.0 142.61742619932261 L 256.0 138.11968029243161 L 260.0 113.1753430462405 L 264.0 134.84129474205466 L 268.0 152.52943132553685 L 272.0 150.22527881053716 L 276.0 149.52457704991605 L 280.0 165.41285531786872 L 284.0 175.69457385984325 L 288.0 167.82311027664917 L 292.0 173.74106847414006 L 296.0 183.36584158312178 L 300.0 162.78005351417295 L 304.0 159.45047440922363 L 308.0 154.71898894123893 L 312.0 142.77312780143436 L 316.0 138.22336911167471 L 320.0 123.54012418216941 L 324.0 118.15480211104911 L 328.0 92.821027338681361 L 332.0 98.500595411045168 L 336.0 92.795979897458594 L 340.0 91.837235607385253 L 344.0 99.790920448382508 L 348.0 103.29293935148364 L 352.0 112.0603671389255 L 356.0 109.0966259612953 L 360.0 95.625899782347147 L 364.0 94.667846609660529 L 368.0 86.798263477269558 L 372.0 81.535565259364972 L 376.0 84.475935495665482 L 380.0 90.21716506997376 L 384.0 94.445847000580926 L 388.0 125.04303498747262 L 392.0 104.30567139364942 L 396.0 102.83173612791296 L 400.0 105.8874181419928 L 404.0 121.73146294192011 L 408.0 97.775376433889789 L 412.0 101.7443197367117 L 416.0 102.45807204294364 L 420.0 96.771974692834959 L 424.0 85.396286961156491 L 428.0 93.657055223196465 L 432.0 79.225851353376854 L 436.0 78.158634015677563 L 440.0 60.0 L 444.0 60.007034272463983 L 448.0 64.09981612099017 L 452.0 83.694265645153962 L 456.0 87.204272678369335" style="fill:none;stroke:rgba(55.3%,62.7%,79.6%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 60.0 341.40041509055959 L 64.0 331.48013406048284 L 68.0 333.66390908920636 L 72.0 298.63144321083621 L 76.0 320.68663617718289 L 80.0 321.26579607614184 L 84.0 301.96015988914587 L 88.0 293.58249526358003 L 92.0 290.71116231260726 L 96.0 312.8910679963646 L 100.0 308.47802483482536 L 104.0 314.89826873237939 L 108.0 312.00992016773881 L 112.0 298.54825126375567 L 116.0 298.22695073121758 L 120.0 301.32319125790997 L 124.0 288.62237716019285 L 128.0 288.76896057588215 L 132.0 297.64549728049496 L 136.0 310.32455563941562 L 140.0 296.69116295131568 L 144.0 283.58479746310104 L 148.0 273.62895504244261 L 152.0 271.23891189081434 L 156.0 281.10609153057806 L 160.0 284.9121378155574 L 164.0 259.38155297621091 L 168.0 256.69756487412525 L 172.0 246.14461545196576 L 176.0 251.00635021673381 L 180.0 247.9867453035327 L 184.0 243.75733385699357 L 188.0 242.22047317371982 L 192.0 242.05080817449084 L 196.0 243.62531960571104 L 200.0 239.49391465354989 L 204.0 220.81633768093531 L 208.0 220.4573948042754 L 212.0 218.09310140695754 L 216.0 211.77898404184285 L 220.0 207.67937095730775 L 224.0 199.6549270002719 L 228.0 191.3772868833868 L 232.0 192.99737953704636 L 236.0 206.30982099064292 L 240.0 206.289755298193 L 244.0 216.65550964879947 L 248.0 210.59342440325437 L 252.0 204.3953949019583 L 256.0 216.52638527295846 L 260.0 221.45094200669595 L 264.0 201.2669991849418 L 268.0 205.30955630122767 L 272.0 210.63053043518693 L 276.0 227.41781246590327 L 280.0 227.30554527943619 L 284.0 215.95237257790649 L 288.0 187.95810082559393 L 292.0 170.58475043166644 L 296.0 166.4094903116389 L 300.0 152.6829390633327 L 304.0 137.97189398029724 L 308.0 132.87885325072912 L 312.0 134.80885099378116 L 316.0 101.81401476218254 L 320.0 83.107012046857918 L 324.0 97.504296878775619 L 328.0 113.38051608616682 L 332.0 104.80599046852473 L 336.0 118.2321895549475 L 340.0 125.54789214454249 L 344.0 123.56627807329902 L 348.0 141.63877713288409 L 352.0 138.24061093253337 L 356.0 149.27909537435144 L 360.0 171.10300720692251 L 364.0 147.0900984713455 L 368.0 163.5481996927914 L 372.0 155.65123947437814 L 376.0 163.88713227201887 L 380.0 142.73642694800836 L 384.0 143.44875141109497 L 388.0 118.67911124146505 L 392.0 122.37227911744779 L 396.0 119.19898484148918 L 400.0 125.02182432759224 L 404.0 110.90969241796643 L 408.0 132.93446638184398 L 412.0 142.13462020475416 L 416.0 152.96726721213733 L 420.0 147.18160927403858 L 424.0 158.91247352861581 L 428.0 153.92691135556268 L 432.0 146.38099403581248 L 436.0 160.33408311683078 L 440.0 159.05331492974875 L 444.0 157.59366599717848 L 448.0 170.33453081257051 L 452.0 172.78927961826247 L 456.0 146.95372036270405" style="fill:none;stroke:rgba(90.6%,54.1%,76.5%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 60.0 351.22380643115855 L 64.0 362.61324946756656 L 68.0 357.32357489222807 L 72.0 373.22578932235126 L 76.0 375.12186566702712 L 80.0 380.51034262121334 L 84.0 366.96268868663668 L 88.0 348.21146831382305 L 92.0 333.38259414554358 L 96.0 327.01159572112653 L 100.0 338.89334988087558 L 104.0 322.00646866255238 L 108.0 314.79967958833549 L 112.0 322.37758697346237 L 116.0 330.9050583128269 L 120.0 333.38779318554958 L 124.0 325.1034401882664 L 128.0 319.85336837406078 L 132.0 342.86551283308802 L 136.0 354.07630151172071 L 140.0 363.18086164012078 L 144.0 363.93845750377767 L 148.0 359.7053148840177 L 152.0 355.96001994434937 L 156.0 358.69510667031994 L 160.0 362.11575801394457 L 164.0 355.61822000762476 L 168.0 355.74245890941546 L 172.0 361.21689998957464 L 176.0 356.00897712806977 L 180.0 368.74923161636832 L 184.0 372.09423806383131 L 188.0 353.1145491964171 L 192.0 368.75130553743622 L 196.0 388.43447110864747 L 200.0 367.4837725852351 L 204.0 374.56583844325354 L 208.0 376.13366974910844 L 212.0 353.68108316127166 L 216.0 360.07813046395341 L 220.0 368.34331079178321 L 224.0 359.87175447865889 L 228.0 362.05101513819085 L 232.0 357.0782275635321 L 236.0 361.42327610475894 L 240.0 370.96171124531799 L 244.0 366.83989697639669 L 248.0 362.54615720120046 L 252.0 377.79096940739481 L 256.0 386.57516824545064 L 260.0 408.53444035579992 L 264.0 404.34193819710663 L 268.0 402.39842352787906 L 272.0 406.47921351649325 L 276.0 413.49441968969018 L 280.0 412.50460118102615 L 284.0 419.31225023047767 L 288.0 404.25041779257799 L 292.0 419.34390480930261 L 296.0 436.15376991202686 L 300.0 408.45426522206071 L 304.0 427.21542161175972 L 308.0 441.56515999606239 L 312.0 435.45146997528815 L 316.0 429.41148090562132 L 320.0 419.40694164199255 L 324.0 415.34394382949995 L 328.0 417.85650989127566 L 332.0 423.73830435494551 L 336.0 432.18596809091082 L 340.0 413.48775956405848 L 344.0 416.56931039788049 L 348.0 409.39974533215343 L 352.0 383.31751819560918 L 356.0 386.29404229246859 L 360.0 385.16287680904708 L 364.0 378.69997301759378 L 368.0 396.43068115864139 L 372.0 389.91370229659356 L 376.0 382.54328517172081 L 380.0 396.93383113908453 L 384.0 414.27120983486759 L 388.0 420.08216326026081 L 392.0 424.81711501475638 L 396.0 446.57486129224782 L 400.0 446.30845965582768 L 404.0 455.64126894814501 L 408.0 453.68771738136138 L 412.0 462.32952112142607 L 416.0 490.69287241174203 L 420.0 480.58227323558907 L 424.0 467.97877802847995 L 428.0 474.67678427269277 L 432.0 493.86506046239566 L 436.0 493.39947291468911 L 440.0 495.96351692413555 L 444.0 497.46671253500438 L 448.0 495.26249376929889 L 452.0 521.65593515849832 L 456.0 534.07407407407402" style="fill:none;stroke:rgba(65.1%,84.7%,32.9%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g><g class="toyplot-mark-Text" id="tfc95f004caad4c38bb8c31595c12d3f8" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="5px" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:12px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 456.0, 237.98689315032672)" x="456.0" y="237.98689315032672">Series 0</text></g></g><g class="toyplot-mark-Text" id="tc1cdcb69a24d482a90961599886c7e59" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="5px" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;fill:rgba(98.8%,55.3%,38.4%,1);font-size:12px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 456.0, 349.12247748720063)" x="456.0" y="349.12247748720063">Series 1</text></g></g><g class="toyplot-mark-Text" id="t875aab5a1d6e40fb8f59f9efefb11973" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="5px" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;fill:rgba(55.3%,62.7%,79.6%,1);font-size:12px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 456.0, 87.204272678369335)" x="456.0" y="87.204272678369335">Series 2</text></g></g><g class="toyplot-mark-Text" id="t387a7254b09a4e3b90c72f8662cce81f" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="5px" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;fill:rgba(90.6%,54.1%,76.5%,1);font-size:12px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 456.0, 146.95372036270405)" x="456.0" y="146.95372036270405">Series 3</text></g></g><g class="toyplot-mark-Text" id="t598200cb12c54217878539d64c24a7be" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="5px" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;fill:rgba(65.1%,84.7%,32.9%,1);font-size:12px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 456.0, 534.07407407407402)" x="456.0" y="534.07407407407402">Series 4</text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="456.0" y1="550.0" y2="550.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="550.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="220.0" y="550.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="380.0" y="550.0">80</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="550.0">120</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="534.074074074074"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 479.26083274925907)" x="50.0" y="479.26083274925907">-10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 348.9215945716178)" x="50.0" y="348.9215945716178">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 218.58235639397648)" x="50.0" y="218.58235639397648">10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 88.24311821633526)" x="50.0" y="88.24311821633526">20</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t2de355270b654d4bb72e245fda1fd75e text");
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
          var text = document.querySelectorAll("#t2de355270b654d4bb72e245fda1fd75e text");
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
      var data_tables = [{"data": [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0], [0.5214351637324931, -0.6195405309739713, 0.8631664374521261, 0.6005145413604132, -0.07007419200459841, 0.8670887483031402, 1.7766771620205568, 1.190153657603208, 1.255850029717637, -0.9368349244677687, 0.2632008002520494, 1.3051468225947271, 2.3084709507071572, 0.3372161305121868, 0.05313876470408979, 0.10525712938757628, 0.5607105409577673, 0.8998024819378025, 2.2709606740671884, 0.7740551208379483, 0.6214087962087664, 0.015439452069832549, 0.2588608285401908, 0.8622997394969327, 2.2304512936770697, 1.8111460089711702, 2.536700094093551, 0.7696728675033542, 0.6365643273243555, 1.745533514895506, 1.3976932866955147, 1.785130940309487, 2.882709513202209, 3.978647768829874, 4.892365060514713, 4.820273485667039, 4.994986439435255, 4.722191633826959, 5.613866346823101, 8.054826862286134, 8.18102645012337, 7.664580519658414, 7.750722456342487, 5.725744855652458, 6.023537055401005, 5.176380270961306, 5.0895854376999585, 5.157874629049178, 5.963288611447313, 6.228557192416756, 7.119565987348147, 5.723755910303841, 4.371782628802997, 4.320864428854083, 3.822621979667228, 3.728002471297844, 4.132022803497081, 4.146509778218941, 4.762248084281536, 6.3579068889070935, 5.433670555139778, 5.413325678035675, 5.77129453325171, 5.61279577014583, 6.696596502701329, 4.346142868889033, 6.426746489727833, 5.334115200705069, 5.59599858748277, 6.350719211799879, 5.615284000036682, 6.12734373719873, 6.881571962660905, 7.455079930554715, 6.5788256170244885, 8.636668567802488, 8.913631109673384, 7.8109720004224314, 8.492951446231562, 8.582464132924928, 9.096856457975823, 5.583339797351088, 6.954445412821293, 7.157075965025828, 7.371605507958226, 6.991509817081739, 7.80887855283415, 8.843798394744047, 9.16463424357085, 10.606620437017257, 10.736462750025886, 10.386498169329364, 9.408647610647458, 8.87392939938667, 9.740523325934511, 9.708576274107847, 9.413810259853202, 9.992098405150596, 8.973109621670464, 8.511228312543649], [0.3412053597430635, 0.9577390560966359, 1.511330815207839, 1.8466264999896962, 2.380914612739446, 3.7943961251655915, 3.0632908415401996, 2.645273175202714, 3.919847530328888, 2.6887392551848457, 3.6142147594591703, 1.9534994354296413, 1.5527343322933669, 2.351898138212432, 2.1979652721111806, 2.0657898604454465, 2.796445864826903, 1.0279468744352886, 1.1250185097609997, 1.569862719088204, 1.3714306647073573, 0.8037240167103407, 0.17084002026100675, 0.6570976246019236, -0.9959151495113143, -0.5522045503726491, -0.9815285539481464, -1.2305448469142268, -0.4864415592354625, 0.24218811447439403, 0.5317441094782909, 0.7329707387727407, 1.5990979721327816, 3.5426324397289823, 4.232265202922685, 3.3202363710174936, 1.2849707288973837, 3.2652174963629594, 1.5798686218925668, 2.8402523267970814, 3.687687746224955, 3.357876962177576, 4.1104391861791765, 3.3100929145240614, 4.53690536462899, 4.062569261996534, 4.813476992912138, 5.847665063634553, 5.775936654967732, 8.19170528380777, 8.737848210055365, 9.584443076720317, 9.160422186594632, 9.153726470103702, 10.56152372821076, 9.806690004044057, 7.733069754951127, 7.449567314517879, 6.612847962032501, 6.99704589293151, 7.58382971783426, 6.8899993498980585, 6.6197954676571795, 5.753596606390639, 4.943928306408898, 5.219913793142653, 5.8986896196809475, 6.135183968454022, 7.137662313563144, 8.175799896156454, 8.153191582193777, 7.652588658630358, 6.764436044537254, 5.5753644819424615, 5.7650477559737565, 5.592028774091281, 7.765720662684833, 7.937994096943662, 6.578562357020893, 8.051548309793136, 5.9536932721495255, 4.656160758691771, 5.0697253154984185, 5.104973203693824, 6.4273682822400335, 5.027801673376646, 3.8822779317096754, 3.3404149585624263, 2.9759101150302367, 1.6001153815922153, 1.8595101691281393, 1.3166241652892139, -0.10649224817643343, -0.9530728634783044, 0.20127870638200818, -0.1802708091340366, -0.29140771737809545, 0.6477497766947783, 0.9861266244100437, -0.015412313159994362], [-0.2695613998402315, -0.8395544875614336, -0.6325561111147446, -1.1540114621945339, -0.04637827898991964, -0.7878670884678051, -1.2624944343962752, -1.1406163950259065, 0.8201430322512764, 1.6581077153888908, 2.221189859855883, 1.724773579582289, 2.818718235077612, 4.976503387870983, 6.486430869456276, 7.551836327268797, 8.351020928192995, 7.725499449756306, 8.215765841425036, 8.954737697751979, 8.72809157047499, 10.70262489049028, 11.163828911197506, 12.104593867370623, 12.38095709462233, 10.352339200920154, 10.014452968952979, 9.97734599898898, 11.153731821126254, 11.45084353728399, 11.622015342615532, 11.970999278157578, 11.863900141310927, 11.173431118530209, 9.975778195478975, 10.275233410631424, 10.90630673125203, 13.720150811101597, 14.169476248081173, 14.887964417286979, 14.662190688630673, 15.212673588785046, 16.12573844937567, 15.124110589910458, 13.782056512417372, 14.985978753029597, 16.21792285902883, 16.65929430745076, 15.828247215249192, 16.173327175035432, 18.087128237167935, 16.42485431269668, 15.067769766953456, 15.244550953280427, 15.298310801075923, 14.07931654500253, 13.29047362358224, 13.89439487502196, 13.440352156939998, 12.701911972422119, 14.28131264690605, 14.53676750083203, 14.89978062981289, 15.81630134198119, 16.165371871575566, 17.29191251542169, 17.70508986296614, 19.648769688517984, 19.213016944235175, 19.650691400012775, 19.72424901040533, 19.11401950836105, 18.845334578783035, 18.172672385108662, 18.40005910449326, 19.433571833836425, 19.50707641972182, 20.110853397585185, 20.514622691581824, 20.28902905781414, 19.84854546633546, 19.52410886614268, 17.176604890003862, 18.7676348732818, 18.880719412239106, 18.64627872831281, 17.4306781907116, 19.26865782316735, 18.964149115097975, 18.90938799203087, 19.34564168121992, 20.218417054985295, 19.584627232554286, 20.691830563768416, 20.773710537337447, 22.166892994866387, 22.166353305317614, 21.852343349010503, 20.349001009579442, 20.07970320775928], [0.5770464509549642, 1.338158850319787, 1.1706133698293109, 3.8584045805331746, 2.1662669499382092, 2.121832142196765, 3.603015894451329, 4.245774341001998, 4.466071236328286, 2.7643652885362617, 3.1029466108794694, 2.61036709397269, 2.8319694759586853, 3.86478730520179, 3.889438403139021, 3.651885953854913, 4.626328821198279, 4.615082521331964, 3.934049178746758, 2.9612754740516154, 4.007268444297368, 5.0128263769248225, 5.7766671481198655, 5.960038110313987, 5.202999801841174, 4.910989019961959, 6.869768678053146, 7.075691939506273, 7.885344471599235, 7.512338243179987, 7.7440109885036685, 8.068503559250072, 8.186415916630828, 8.19943310175491, 8.078632071057287, 8.395605302597154, 9.82860255145008, 9.856141677938654, 10.03753704516457, 10.521974230266801, 10.8365082985838, 11.452166642857625, 12.087250922359349, 11.962952769607261, 10.941584098152171, 10.943123595599788, 10.147833206033544, 10.612933764415125, 11.088464355812983, 10.157739998312397, 9.779913888340378, 11.328483843478915, 11.018327272609888, 10.610086883272395, 9.322118481321425, 9.330731941706553, 10.201779897814468, 12.34958067858616, 13.682513925460682, 14.002851851200054, 15.055992213244986, 16.18466576456539, 16.575418449695157, 16.42734349007159, 18.958801912947244, 20.39405678913645, 19.28945582374678, 18.0713867733697, 18.72924895957918, 17.699152476421588, 17.137870801625827, 17.289905913918158, 15.90333197714604, 16.164049029651697, 15.317144858954185, 13.642751779962351, 15.485090976609294, 14.222378270017064, 14.828255696402689, 14.196374390911558, 15.819117136667362, 15.764465561819597, 17.664863363429497, 17.381512936680096, 17.624977170499967, 17.178232232635057, 18.260955448370918, 16.57115165084836, 15.865289475225453, 15.034177742577517, 15.478070005490192, 14.578044470693909, 14.960551092856159, 15.539495501712207, 14.468974507719482, 14.56723871464514, 14.679227165166918, 13.70171149194905, 13.513376126481724, 15.49555429606307], [-0.17663229367683592, -1.050463013853759, -0.6446240163809387, -1.8646874947672272, -2.010159907463986, -2.4235793066814493, -1.3841644593955986, 0.0544829222361185, 1.1921966587602597, 1.6809979217946505, 0.7693956809134145, 2.0650056180612606, 2.617931135731893, 2.036532357353374, 1.3822803102651138, 1.1917977735067715, 1.8273970844366292, 2.2301976445450356, 0.46463995211294984, -0.39548389358219205, -1.0940118469212514, -1.1521367734015144, -0.8273579363493466, -0.5400081718399214, -0.74985186620331, -1.0122940433597098, -0.5137843008473031, -0.5233162655517036, -0.9433310789494903, -0.5437643073218248, -1.5212331544954376, -1.7778716383650484, -0.3216954988707805, -1.5213922716651334, -3.031541160550366, -1.4241435099013435, -1.9674999048778317, -2.087788417207332, -0.3651616087526257, -0.8559614164025009, -1.4900897451690853, -0.8401276591870923, -1.0073267843317304, -0.6258002659795775, -0.9591648461304054, -1.6909809342035165, -1.37474352737568, -1.0453155028429428, -2.214941198016713, -2.8888901147722175, -4.573668422316152, -4.252007637942128, -4.102895620993038, -4.415985527430296, -4.954212255718815, -4.878270542194683, -5.4005728929398416, -4.24498593014268, -5.403001522972327, -6.692702562947243, -4.567517156215461, -6.006926857546471, -7.107879923172435, -6.638820098498469, -6.175414822073972, -5.407837889485689, -5.096113049805784, -5.2888843209061465, -5.740152453657814, -6.388281432626669, -4.953701271787595, -5.19012668572335, -4.640057100695124, -2.638953864155063, -2.8673213257480716, -2.780535067117361, -2.2846825608563597, -3.645033318537029, -3.145032017841554, -2.5795524870476556, -3.683636427430258, -5.013809822502097, -5.4596428277152595, -5.822921900134131, -7.49223856806168, -7.471799470814765, -8.187839354337594, -8.037957277834966, -8.70098123446471, -10.877098855442297, -10.101384702320342, -9.134408419251107, -9.648298659662363, -11.120478216485534, -11.084757005113095, -11.28147781193198, -11.39680728844926, -11.227693305850918, -13.252673792020966, -14.205429009037882]], "names": ["x", "y0", "y1", "y2", "y3", "y4"], "id": "t2d2e93d4638848fb871fa57adaf9991d", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t2de355270b654d4bb72e245fda1fd75e .toyplot-mark-popup");
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
      var axes = {"tcd04d2690ddd4a96a3f9254ac86430f0": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 120.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 22.166892994866387, "min": -14.660083034086686}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 540.0}, "scale": "linear"}]}};
    
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


Note that we are using the last coordinate in each series as the text
label coordinate - by default, Toyplot renders text centered on its
coordinate, so in this case we've chosen a text style that left-aligns
the text and offsets it slightly for clarity.

Canvas Text
-----------

When adding text to axes, you specify the text coordinates using the
same domain as your data. Naturally, this limits the added text to the
bounds defined by the axes. For the ultimate in labeling flexibility,
you can add text to the canvas directly, using canvas units, outside
and/or overlapping axes:

.. code:: python

    label_style={"font-size":"18px", "font-weight":"bold"}
    
    canvas = toyplot.Canvas(width=600, height=300)
    canvas.axes(grid=(1,2,0)).plot(numpy.linspace(1, 0)**2)
    canvas.axes(grid=(1,2,1), yshow=False).plot(numpy.linspace(0, 1)**2)
    canvas.text(300, 120, "This label overlaps two sets of axes!", style=label_style);



.. raw:: html

    <div align="center" class="toyplot" id="t2d07cd24b85c4b4a8eb05eb26e91c155"><svg height="300.0px" id="tedc4ec246ff74b1a8a2c8a63767358aa" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t43f9cebc98284b72b99057c8280310f3"><clipPath id="t7841a4d6170645b0ad0b9d02591e78ee"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t7841a4d6170645b0ad0b9d02591e78ee)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="td2fb3d3b79234e64829bbeda5c000809" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 60.0 L 63.599999999999994 67.271970012494791 L 67.199999999999989 74.39400249895877 L 70.799999999999997 81.366097459391909 L 74.400000000000006 88.188254893794237 L 78.0 94.860474802165754 L 81.599999999999994 101.38275718450647 L 85.200000000000003 107.7551020408163 L 88.799999999999997 113.97750937109537 L 92.400000000000006 120.04997917534359 L 96.0 125.97251145356103 L 99.599999999999994 131.74510620574762 L 103.19999999999999 137.36776343190337 L 106.80000000000001 142.84048313202834 L 110.40000000000001 148.16326530612244 L 114.0 153.33610995418573 L 117.59999999999999 158.35901707621821 L 121.2 163.2319866722199 L 124.79999999999998 167.95501874219076 L 128.40000000000001 172.52811328613078 L 132.0 176.95127030403995 L 135.59999999999999 181.2244897959184 L 139.19999999999999 185.34777176176593 L 142.80000000000001 189.3211162015827 L 146.39999999999998 193.1445231153686 L 150.0 196.81799250312369 L 153.60000000000002 200.34152436484797 L 157.20000000000002 203.71511870054144 L 160.80000000000001 206.9387755102041 L 164.39999999999998 210.01249479383588 L 168.0 212.93627655143689 L 171.60000000000002 215.71012078300708 L 175.19999999999999 218.33402748854644 L 178.80000000000001 220.80799666805495 L 182.40000000000001 223.13202832153269 L 186.0 225.30612244897955 L 189.59999999999999 227.33027905039566 L 193.19999999999999 229.20449812578093 L 196.80000000000001 230.92877967513536 L 200.40000000000001 232.50312369845895 L 204.0 233.92753019575176 L 207.59999999999999 235.20199916701375 L 211.19999999999999 236.32653061224491 L 214.80000000000001 237.30112453144523 L 218.39999999999998 238.12578092461476 L 222.0 238.80049979175345 L 225.60000000000002 239.32528113286131 L 229.19999999999999 239.70012494793835 L 232.79999999999998 239.92503123698458 L 236.39999999999998 240.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="236.39999999999998" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="96.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="132.0" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="168.0" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="204.0" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t57cb882666cd40c5b5c44106ac8387be"><clipPath id="t9af95ae94b3746c2b18d8dd6f74a6c81"><rect height="200.0" width="200.0" x="350.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9af95ae94b3746c2b18d8dd6f74a6c81)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="350.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t646d82c6b50541aaa1b03ee0e5589db1" style="fill:none"><g class="toyplot-Series"><path d="M 360.0 240.0 L 363.60000000000002 239.92503123698458 L 367.19999999999999 239.70012494793838 L 370.79999999999995 239.32528113286131 L 374.39999999999998 238.80049979175345 L 378.0 238.12578092461476 L 381.60000000000002 237.30112453144525 L 385.20000000000005 236.32653061224491 L 388.79999999999995 235.20199916701375 L 392.40000000000003 233.92753019575176 L 396.0 232.50312369845898 L 399.60000000000002 230.92877967513536 L 403.20000000000005 229.20449812578093 L 406.79999999999995 227.33027905039569 L 410.39999999999998 225.30612244897958 L 414.0 223.13202832153269 L 417.60000000000002 220.80799666805498 L 421.19999999999999 218.33402748854647 L 424.80000000000001 215.71012078300706 L 428.39999999999998 212.93627655143689 L 432.0 210.01249479383591 L 435.60000000000002 206.9387755102041 L 439.20000000000005 203.71511870054144 L 442.80000000000001 200.341524364848 L 446.39999999999998 196.81799250312369 L 450.0 193.1445231153686 L 453.60000000000002 189.3211162015827 L 457.20000000000005 185.34777176176596 L 460.80000000000001 181.2244897959184 L 464.39999999999998 176.95127030403995 L 468.0 172.5281132861308 L 471.60000000000002 167.95501874219076 L 475.20000000000005 163.2319866722199 L 478.80000000000001 158.35901707621824 L 482.40000000000003 153.33610995418576 L 486.0 148.16326530612247 L 489.60000000000002 142.84048313202834 L 493.20000000000005 137.36776343190337 L 496.79999999999995 131.74510620574762 L 500.39999999999998 125.97251145356105 L 504.0 120.04997917534362 L 507.59999999999997 113.97750937109539 L 511.19999999999999 107.75510204081634 L 514.79999999999995 101.38275718450647 L 518.39999999999998 94.860474802165797 L 522.0 88.188254893794294 L 525.60000000000002 81.366097459391938 L 529.19999999999993 74.39400249895877 L 532.79999999999995 67.271970012494791 L 536.40000000000009 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="360.0" x2="536.4000000000001" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="360.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="396.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="432.0" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="468.0" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="504.0" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">50</text></g></g><g class="toyplot-mark-Text" id="ta21d3c249f71495a96c048fbaaa3dae9" style="alignment-baseline:middle;font-size:18px;font-weight:bold;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(16.1%,15.3%,14.1%,1);font-size:18px;font-weight:bold;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 300.0, 120.0)" x="300.0" y="120.0">This label overlaps two sets of axes!</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t2d07cd24b85c4b4a8eb05eb26e91c155 text");
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
          var text = document.querySelectorAll("#t2d07cd24b85c4b4a8eb05eb26e91c155 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [1.0, 0.9596001665972511, 0.920033319450229, 0.8812994585589339, 0.8433985839233653, 0.8063306955435235, 0.7700957934194085, 0.7346938775510206, 0.7001249479383591, 0.6663890045814245, 0.6334860474802165, 0.6014160766347355, 0.5701790920449812, 0.5397750937109538, 0.5102040816326531, 0.4814660558100793, 0.4535610162432321, 0.4264889629321117, 0.40024989587671805, 0.3748438150770512, 0.3502707205331112, 0.32653061224489793, 0.3036234902124116, 0.2815493544356518, 0.2603082049146189, 0.23990004164931278, 0.22032486463973353, 0.20158267388588094, 0.18367346938775514, 0.16659725114535612, 0.15035401915868396, 0.1349437734277385, 0.12036651395251982, 0.10662224073302792, 0.0937109537692628, 0.08163265306122454, 0.070387338608913, 0.05997501041232822, 0.050395668471470235, 0.04164931278633907, 0.033735943356934646, 0.026655560183256998, 0.020408163265306135, 0.014993752603082056, 0.01041232819658478, 0.006663890045814259, 0.0037484381507705204, 0.0016659725114535648, 0.0004164931278633912, 0.0]], "names": ["x", "y0"], "id": "td2fb3d3b79234e64829bbeda5c000809", "title": "Plot Data"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "names": ["x", "y0"], "id": "t646d82c6b50541aaa1b03ee0e5589db1", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t2d07cd24b85c4b4a8eb05eb26e91c155 .toyplot-mark-popup");
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
      var axes = {"t43f9cebc98284b72b99057c8280310f3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}, "t57cb882666cd40c5b5c44106ac8387be": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 360.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Please keep in mind when placing labels in canvas coordinates that,
unlike Cartesian coordinates, canvas coordinates increase from
top-to-bottom.

Canvas Legends
--------------

Last-but-not-least, Toyplot provides (currently experimental) support
for graphical legends:

.. code:: python

    observations = numpy.random.power(2, size=(50, 50))
    
    x = numpy.arange(len(observations))
    
    boundaries = numpy.column_stack(
        (numpy.min(observations, axis=1),
         numpy.percentile(observations, 25, axis=1),
         numpy.percentile(observations, 50, axis=1),
         numpy.percentile(observations, 75, axis=1),
         numpy.max(observations, axis=1)))
    
    fill = ["blue", "blue", "red", "red"]
    opacity = [0.1, 0.2, 0.2, 0.1]
    
    canvas = toyplot.Canvas(800, 400)
    axes = canvas.axes(grid=(1,5,0,1,0,4))
    fill = axes.fill(x, boundaries, fill=fill, opacity=opacity)
    mean = axes.plot(x, numpy.mean(observations, axis=1), color="blue")
    
    canvas.legend([
        ("Mean", mean),
        ("First Quartile", "rect", {"fill":"blue", "opacity":0.1}),
        ("Second Quartile", "rect", {"fill":"blue", "opacity":0.2}),
        ("Third Quartile", "rect", {"fill":"red", "opacity":0.2}),
        ("Fourth Quartile", "rect", {"fill":"red", "opacity":0.1}),
        ],
        corner=("right", 100, 100, 125),
        );




.. raw:: html

    <div align="center" class="toyplot" id="t3d549e35cb41480cb6cbf1e3bd172d5b"><svg height="400.0px" id="t9306c26f688747ff97a64794477b3dab" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t477cbd6fd26f44409911e9ca256d5ab7"><clipPath id="tf245e2545b654b8cbffd01a1c7ac43ea"><rect height="300.0" width="540.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf245e2545b654b8cbffd01a1c7ac43ea)" style="cursor:crosshair"><rect height="300.0" style="pointer-events:all;visibility:hidden" width="540.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-FillBoundaries" id="t62435803645242ed89b77294c07eb1c0" style="stroke:none"><polygon points="60.0,303.16103564813289 70.399999999999991,328.99859165469201 80.799999999999997,304.09983069298204 91.199999999999989,314.02573663240764 101.59999999999999,293.1601884175742 112.0,318.83251062623805 122.39999999999999,302.11407890548463 132.80000000000001,317.53363590333174 143.19999999999999,294.81936121490696 153.59999999999999,328.49039247336037 164.0,293.24150268785388 174.40000000000001,301.52446268032554 184.79999999999998,290.11478764569176 195.20000000000002,307.64127433508884 205.59999999999999,321.1203028134272 216.0,299.87571967734311 226.39999999999998,335.77905303621714 236.80000000000001,310.68878201537706 247.19999999999999,318.40090340729228 257.60000000000002,273.61718626376688 268.0,315.57174588257828 278.39999999999998,322.12727547965238 288.80000000000001,326.93581712149495 299.20000000000005,322.52152493958135 309.59999999999997,289.05568019509599 320.0,288.70187604071725 330.40000000000003,297.87653724273008 340.80000000000007,326.56599509440957 351.19999999999999,318.37518649503374 361.59999999999997,321.27749687504627 372.0,313.50468009516078 382.40000000000003,301.52394997953724 392.80000000000001,294.01450840320416 403.19999999999999,312.93454919533184 413.60000000000002,302.01792885579965 424.0,301.2647897285151 434.39999999999998,338.16209760218464 444.80000000000001,303.18815967084714 455.19999999999999,300.55761216731088 465.60000000000002,289.37880144726694 476.0,279.06292535760122 486.39999999999998,270.2955402902117 496.80000000000001,284.24640109215278 507.19999999999999,319.54404028357192 517.60000000000002,313.54593995079193 528.0,287.94774031730901 538.39999999999998,312.26399837557796 548.79999999999995,298.43945363612846 559.19999999999993,274.28727387810039 569.60000000000002,330.56731198368942 569.60000000000002,178.5891717926836 559.19999999999993,201.70289783083189 548.79999999999995,226.86369104451992 538.39999999999998,178.38406889291664 528.0,199.74691826098763 517.60000000000002,185.89120872562137 507.19999999999999,207.97721134943797 496.80000000000001,202.58063485252603 486.39999999999998,190.81723879612997 476.0,165.05039291756492 465.60000000000002,194.9314902204049 455.19999999999999,227.9148641743885 444.80000000000001,187.72629165376665 434.39999999999998,214.50248237007239 424.0,217.83155304331879 413.60000000000002,188.7853270999731 403.19999999999999,218.6402797788524 392.80000000000001,191.48816142982443 382.40000000000003,202.6697850036455 372.0,154.65815034708399 361.59999999999997,207.36696971046857 351.19999999999999,188.66728314906422 340.80000000000007,185.79350128783477 330.40000000000003,172.50597659430355 320.0,172.62922258199995 309.59999999999997,224.84515682847498 299.20000000000005,215.98687783078751 288.80000000000001,237.61904404974368 278.39999999999998,235.80044638009409 268.0,189.42046861970385 257.60000000000002,197.23793104879593 247.19999999999999,214.05259574382501 236.80000000000001,220.74577009813575 226.39999999999998,209.63691285337802 216.0,216.12230950509837 205.59999999999999,216.05900680180162 195.20000000000002,238.52658193533057 184.79999999999998,205.07397275658752 174.40000000000001,183.65836170494114 164.0,198.57612455914315 153.59999999999999,249.86248106270611 143.19999999999999,205.09261113570216 132.80000000000001,221.95799032041296 122.39999999999999,200.03160045856413 112.0,187.87595321239934 101.59999999999999,158.50958495322033 91.199999999999989,211.03697705322656 80.799999999999997,186.54790335648084 70.399999999999991,171.6040621280473 60.0,223.40892216185711" style="fill:rgba(0%,0%,100%,1);opacity:0.1;stroke:none"></polygon><polygon points="60.0,223.40892216185711 70.399999999999991,171.6040621280473 80.799999999999997,186.54790335648084 91.199999999999989,211.03697705322656 101.59999999999999,158.50958495322033 112.0,187.87595321239934 122.39999999999999,200.03160045856413 132.80000000000001,221.95799032041296 143.19999999999999,205.09261113570216 153.59999999999999,249.86248106270611 164.0,198.57612455914315 174.40000000000001,183.65836170494114 184.79999999999998,205.07397275658752 195.20000000000002,238.52658193533057 205.59999999999999,216.05900680180162 216.0,216.12230950509837 226.39999999999998,209.63691285337802 236.80000000000001,220.74577009813575 247.19999999999999,214.05259574382501 257.60000000000002,197.23793104879593 268.0,189.42046861970385 278.39999999999998,235.80044638009409 288.80000000000001,237.61904404974368 299.20000000000005,215.98687783078751 309.59999999999997,224.84515682847498 320.0,172.62922258199995 330.40000000000003,172.50597659430355 340.80000000000007,185.79350128783477 351.19999999999999,188.66728314906422 361.59999999999997,207.36696971046857 372.0,154.65815034708399 382.40000000000003,202.6697850036455 392.80000000000001,191.48816142982443 403.19999999999999,218.6402797788524 413.60000000000002,188.7853270999731 424.0,217.83155304331879 434.39999999999998,214.50248237007239 444.80000000000001,187.72629165376665 455.19999999999999,227.9148641743885 465.60000000000002,194.9314902204049 476.0,165.05039291756492 486.39999999999998,190.81723879612997 496.80000000000001,202.58063485252603 507.19999999999999,207.97721134943797 517.60000000000002,185.89120872562137 528.0,199.74691826098763 538.39999999999998,178.38406889291664 548.79999999999995,226.86369104451992 559.19999999999993,201.70289783083189 569.60000000000002,178.5891717926836 569.60000000000002,133.25264452386037 559.19999999999993,160.46441515852348 548.79999999999995,126.91775970498051 538.39999999999998,143.00960970806699 528.0,146.39133972296906 517.60000000000002,130.17265741213888 507.19999999999999,142.71060438591184 496.80000000000001,139.4476907157584 486.39999999999998,151.69144944086685 476.0,126.80469489402716 465.60000000000002,124.79480542402673 455.19999999999999,138.11052110599718 444.80000000000001,128.11794541207402 434.39999999999998,163.01734240167696 424.0,156.45317891046386 413.60000000000002,128.07611977556212 403.19999999999999,148.05890931321358 392.80000000000001,135.76918267695481 382.40000000000003,163.69046045523618 372.0,123.31883617966739 361.59999999999997,136.922616713689 351.19999999999999,131.75310856585298 340.80000000000007,133.66437658924792 330.40000000000003,105.91309767391837 320.0,126.86618491997913 309.59999999999997,153.94041464012795 299.20000000000005,118.09288689359695 288.80000000000001,173.80350587919696 278.39999999999998,145.16912546898527 268.0,136.06679257080248 257.60000000000002,146.44297803739116 247.19999999999999,136.34881754622296 236.80000000000001,145.52505496993183 226.39999999999998,142.61839050046123 216.0,148.98782529043845 205.59999999999999,132.08895925779836 195.20000000000002,165.67171601689742 184.79999999999998,143.92591253748833 174.40000000000001,129.63364084489825 164.0,149.332490042725 153.59999999999999,156.73403605741328 143.19999999999999,144.9258153441819 132.80000000000001,145.84518108209122 122.39999999999999,158.33575350233156 112.0,130.96072611544051 101.59999999999999,122.29349656901728 91.199999999999989,163.90640322618211 80.799999999999997,122.72705141108115 70.399999999999991,122.84191909692774 60.0,155.494614618474" style="fill:rgba(0%,0%,100%,1);opacity:0.2;stroke:none"></polygon><polygon points="60.0,155.494614618474 70.399999999999991,122.84191909692774 80.799999999999997,122.72705141108115 91.199999999999989,163.90640322618211 101.59999999999999,122.29349656901728 112.0,130.96072611544051 122.39999999999999,158.33575350233156 132.80000000000001,145.84518108209122 143.19999999999999,144.9258153441819 153.59999999999999,156.73403605741328 164.0,149.332490042725 174.40000000000001,129.63364084489825 184.79999999999998,143.92591253748833 195.20000000000002,165.67171601689742 205.59999999999999,132.08895925779836 216.0,148.98782529043845 226.39999999999998,142.61839050046123 236.80000000000001,145.52505496993183 247.19999999999999,136.34881754622296 257.60000000000002,146.44297803739116 268.0,136.06679257080248 278.39999999999998,145.16912546898527 288.80000000000001,173.80350587919696 299.20000000000005,118.09288689359695 309.59999999999997,153.94041464012795 320.0,126.86618491997913 330.40000000000003,105.91309767391837 340.80000000000007,133.66437658924792 351.19999999999999,131.75310856585298 361.59999999999997,136.922616713689 372.0,123.31883617966739 382.40000000000003,163.69046045523618 392.80000000000001,135.76918267695481 403.19999999999999,148.05890931321358 413.60000000000002,128.07611977556212 424.0,156.45317891046386 434.39999999999998,163.01734240167696 444.80000000000001,128.11794541207402 455.19999999999999,138.11052110599718 465.60000000000002,124.79480542402673 476.0,126.80469489402716 486.39999999999998,151.69144944086685 496.80000000000001,139.4476907157584 507.19999999999999,142.71060438591184 517.60000000000002,130.17265741213888 528.0,146.39133972296906 538.39999999999998,143.00960970806699 548.79999999999995,126.91775970498051 559.19999999999993,160.46441515852348 569.60000000000002,133.25264452386037 569.60000000000002,96.469384449211759 559.19999999999993,125.25070289407226 548.79999999999995,98.220832413276582 538.39999999999998,94.567379782637147 528.0,79.246112294598234 517.60000000000002,97.284433494953319 507.19999999999999,103.72458048636031 496.80000000000001,102.26007660562767 486.39999999999998,107.94048313735749 476.0,91.163515098671894 465.60000000000002,94.729827244776573 455.19999999999999,95.459440440041945 444.80000000000001,94.960388958186741 434.39999999999998,121.6865108544055 424.0,104.62805465763753 413.60000000000002,92.778974125939982 403.19999999999999,99.130036622936473 392.80000000000001,79.858540327377142 382.40000000000003,113.66173264447308 372.0,89.692557494982552 361.59999999999997,84.30693590393021 351.19999999999999,103.6010010407204 340.80000000000007,99.507198844847125 330.40000000000003,86.539029755473251 320.0,90.785221874009366 309.59999999999997,114.17076235418423 299.20000000000005,78.339976172031413 288.80000000000001,108.68415281831935 278.39999999999998,114.32976782777465 268.0,92.853275914317692 257.60000000000002,94.997911106094364 247.19999999999999,93.17070337051095 236.80000000000001,118.73923090244364 226.39999999999998,95.38610520865933 216.0,119.28709724098819 205.59999999999999,83.064346270177765 195.20000000000002,114.92941122031482 184.79999999999998,96.891836343516999 174.40000000000001,98.354895071196992 164.0,95.152084723335122 153.59999999999999,116.92642447803091 143.19999999999999,99.107377439997961 132.80000000000001,98.883280373121465 122.39999999999999,90.094487899576279 112.0,92.991864649842213 101.59999999999999,89.033270913476727 91.199999999999989,113.29922853686729 80.799999999999997,82.518359875728962 70.399999999999991,88.941592941807627 60.0,108.02304098830025" style="fill:rgba(100%,0%,0%,1);opacity:0.2;stroke:none"></polygon><polygon points="60.0,108.02304098830025 70.399999999999991,88.941592941807627 80.799999999999997,82.518359875728962 91.199999999999989,113.29922853686729 101.59999999999999,89.033270913476727 112.0,92.991864649842213 122.39999999999999,90.094487899576279 132.80000000000001,98.883280373121465 143.19999999999999,99.107377439997961 153.59999999999999,116.92642447803091 164.0,95.152084723335122 174.40000000000001,98.354895071196992 184.79999999999998,96.891836343516999 195.20000000000002,114.92941122031482 205.59999999999999,83.064346270177765 216.0,119.28709724098819 226.39999999999998,95.38610520865933 236.80000000000001,118.73923090244364 247.19999999999999,93.17070337051095 257.60000000000002,94.997911106094364 268.0,92.853275914317692 278.39999999999998,114.32976782777465 288.80000000000001,108.68415281831935 299.20000000000005,78.339976172031413 309.59999999999997,114.17076235418423 320.0,90.785221874009366 330.40000000000003,86.539029755473251 340.80000000000007,99.507198844847125 351.19999999999999,103.6010010407204 361.59999999999997,84.30693590393021 372.0,89.692557494982552 382.40000000000003,113.66173264447308 392.80000000000001,79.858540327377142 403.19999999999999,99.130036622936473 413.60000000000002,92.778974125939982 424.0,104.62805465763753 434.39999999999998,121.6865108544055 444.80000000000001,94.960388958186741 455.19999999999999,95.459440440041945 465.60000000000002,94.729827244776573 476.0,91.163515098671894 486.39999999999998,107.94048313735749 496.80000000000001,102.26007660562767 507.19999999999999,103.72458048636031 517.60000000000002,97.284433494953319 528.0,79.246112294598234 538.39999999999998,94.567379782637147 548.79999999999995,98.220832413276582 559.19999999999993,125.25070289407226 569.60000000000002,96.469384449211759 569.60000000000002,63.194448488004994 559.19999999999993,70.055089852863659 548.79999999999995,65.474131147328507 538.39999999999998,64.659060192597167 528.0,62.030514983934872 517.60000000000002,62.679635159168257 507.19999999999999,67.930094734793684 496.80000000000001,60.31820129255027 486.39999999999998,62.436876278175646 476.0,63.972920643188047 465.60000000000002,60.577436130929343 455.19999999999999,61.102676666427364 444.80000000000001,61.292984200707039 434.39999999999998,67.071594400389159 424.0,61.056242015634339 413.60000000000002,60.41914471124386 403.19999999999999,62.749197102646235 392.80000000000001,62.443905043259299 382.40000000000003,62.516949500442536 372.0,60.550008497580336 361.59999999999997,60.856238807417043 351.19999999999999,72.084446842783535 340.80000000000007,60.787623056576891 330.40000000000003,61.530684659714346 320.0,63.261384231964712 309.59999999999997,63.860001202228531 299.20000000000005,61.392421269122963 288.80000000000001,65.800351575576542 278.39999999999998,68.067251065316185 268.0,60.342797002617893 257.60000000000002,65.476583479960951 247.19999999999999,63.087875684979238 236.80000000000001,60.270510452688413 226.39999999999998,65.128138958457228 216.0,61.529919594115206 205.59999999999999,61.439453832754062 195.20000000000002,60.905352393979157 184.79999999999998,63.656055631737345 174.40000000000001,60.567176707045391 164.0,69.663598593101526 153.59999999999999,66.124805600200446 143.19999999999999,63.710108925476206 132.80000000000001,62.480383121265348 122.39999999999999,60.307163096698268 112.0,61.88999390194391 101.59999999999999,60.19175935324381 91.199999999999989,62.439481080351129 80.799999999999997,60.005078717050068 70.399999999999991,64.089924747005654 60.0,68.520923101965508" style="fill:rgba(100%,0%,0%,1);opacity:0.1;stroke:none"></polygon></g><g class="toyplot-mark-Plot" id="tdb65a80bf2ca4d0e9df3981d70b323b8" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 165.93023293228708 L 70.399999999999991 141.8641110389226 L 80.799999999999997 143.90814968946296 L 91.199999999999989 162.52070201126344 L 101.59999999999999 131.59152964033143 L 112.0 151.1851438577898 L 122.39999999999999 152.29657503822551 L 132.80000000000001 160.44202419163906 L 143.19999999999999 154.521906483539 L 153.59999999999999 179.35262399147527 L 164.0 157.67375852727398 L 174.40000000000001 141.45800254451871 L 184.79999999999998 154.38623591862313 L 195.20000000000002 175.50243732599665 L 205.59999999999999 151.44767711248335 L 216.0 165.18126214286565 L 226.39999999999998 155.90867359340518 L 236.80000000000001 169.5283173470136 L 247.19999999999999 153.13075121786517 L 257.60000000000002 152.09054080650716 L 268.0 152.91106560214087 L 278.39999999999998 169.47988293665756 L 288.80000000000001 176.88246778423218 L 299.20000000000005 150.93006959911924 L 309.59999999999997 164.16682137695045 L 320.0 142.01354344833206 L 330.40000000000003 136.81124244362024 L 340.80000000000007 149.77001985918736 L 351.19999999999999 149.9562437490971 L 361.59999999999997 153.13922494852847 L 372.0 133.24938109659394 L 382.40000000000003 163.83019815185793 L 392.80000000000001 144.04491344518817 L 403.19999999999999 155.49185887332493 L 413.60000000000002 149.34295446921993 L 424.0 164.48223309327079 L 434.39999999999998 173.42221132901435 L 444.80000000000001 146.03568612327899 L 455.19999999999999 159.90173306870861 L 465.60000000000002 144.44686311376688 L 476.0 140.24294856556793 L 486.39999999999998 151.87725122716256 L 496.80000000000001 154.87003064165913 L 507.19999999999999 160.42404168164359 L 517.60000000000002 144.12044814299179 L 528.0 148.83152746007582 L 538.39999999999998 148.80329112762047 L 548.79999999999995 157.59600763418018 L 559.19999999999993 164.7448316680096 L 569.60000000000002 144.81717397657809" style="fill:none;stroke:rgba(0%,0%,100%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="490.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="535.0" y="67.0"></text></g><line style="" x1="60.0" x2="569.6" y1="350.0" y2="350.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="350.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="164.0" y="350.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="268.0" y="350.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="372.0" y="350.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="476.0" y="350.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="580.0" y="350.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="60.00507871705007" y2="338.16209760218464"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 340.0)" x="50.0" y="340.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 200.0)" x="50.0" y="200.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g><rect class="toyplot-mark-Legend" height="125.0" id="t90f8fdbdc15843bf8e049945889c51fb" style="fill:none;stroke:none" width="100.0" x="600.0" y="137.5"></rect><line style="fill:none;stroke:rgba(0%,0%,100%,1)" x1="610.0" x2="623.0" y1="160.5" y2="147.5"></line><text style="alignment-baseline:middle;stroke:none" x="633.0" y="154.0">Mean</text><rect height="13.0" style="fill:blue;opacity:0.1;stroke:none" width="13.0" x="610.0" y="170.5"></rect><text style="alignment-baseline:middle;stroke:none" x="633.0" y="177.0">First Quartile</text><rect height="13.0" style="fill:blue;opacity:0.2;stroke:none" width="13.0" x="610.0" y="193.5"></rect><text style="alignment-baseline:middle;stroke:none" x="633.0" y="200.0">Second Quartile</text><rect height="13.0" style="fill:red;opacity:0.2;stroke:none" width="13.0" x="610.0" y="216.5"></rect><text style="alignment-baseline:middle;stroke:none" x="633.0" y="223.0">Third Quartile</text><rect height="13.0" style="fill:red;opacity:0.1;stroke:none" width="13.0" x="610.0" y="239.5"></rect><text style="alignment-baseline:middle;stroke:none" x="633.0" y="246.0">Fourth Quartile</text></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t3d549e35cb41480cb6cbf1e3bd172d5b text");
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
          var text = document.querySelectorAll("#t3d549e35cb41480cb6cbf1e3bd172d5b text");
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
      var data_tables = [{"data": [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0], [0.13156772982809672, 0.039290744090385535, 0.12821489038220688, 0.09276522631282974, 0.16728504136580646, 0.07559817633486413, 0.13530686105184053, 0.08023701463095784, 0.16135942423247518, 0.041105741166569905, 0.16699463325766464, 0.13741263328455153, 0.17816147269395805, 0.11556687737468288, 0.06742748995204582, 0.14330100115234617, 0.015074810584938663, 0.10468292137365344, 0.0771396306882418, 0.23708147762940388, 0.08724376470507762, 0.06383115900124144, 0.046657795994660925, 0.06242312521578101, 0.1819439993032287, 0.18320758556886693, 0.1504409384188211, 0.04797858894853724, 0.07723147680345079, 0.06686608258912034, 0.09462614251728298, 0.13741446435879556, 0.16423389855998521, 0.09666232430238615, 0.1356502540864299, 0.13834003668387446, 0.006563937135054716, 0.1314708583184031, 0.14086567083103252, 0.18078999483118946, 0.21763240943713863, 0.24894449896352963, 0.19911999609945458, 0.07305699898724302, 0.09447878589002875, 0.18590092743818212, 0.0990571486586501, 0.1484305227281125, 0.2346883075782129, 0.0336881714868235], [0.41639670656479594, 0.6014140638284026, 0.5480432022982826, 0.46058222480990507, 0.6481800537384989, 0.5433001670985738, 0.4998871412194138, 0.42157860599852515, 0.481812103086778, 0.3219197104903353, 0.5050852694316316, 0.5583629939109245, 0.48187866872647306, 0.3624050645166765, 0.4426464042792799, 0.44242032319607727, 0.46558245409507865, 0.4259079639352295, 0.4498121580577679, 0.5098645319685859, 0.5377840406439148, 0.37214126292823546, 0.3656462712509155, 0.4429040077471876, 0.41126729704116083, 0.5977527764928574, 0.5981929407346303, 0.5507374954005901, 0.5404739887533421, 0.4736893938911837, 0.6619351773318429, 0.49046505355840897, 0.5303994234649128, 0.4334275722183842, 0.5400524032143817, 0.43631588198814714, 0.4482054201068843, 0.5438346726651191, 0.4003040565200411, 0.5181018206414111, 0.6248200252944109, 0.5327955757281072, 0.4907834469552642, 0.47150995946629304, 0.550388540265638, 0.5009038633536156, 0.5771997539538691, 0.40405824626957165, 0.49391822203274327, 0.5764672435975585], [0.6589478049340214, 0.7755645746538296, 0.7759748163889959, 0.6289057027636353, 0.777523226539224, 0.7465688353019981, 0.6488008803488159, 0.69341006756396, 0.6966935166279218, 0.6545212997949527, 0.6809553927045535, 0.7513084255539348, 0.7002645980803988, 0.6226010142253663, 0.7425394312221487, 0.6821863382484341, 0.7049343196412099, 0.6945533751073864, 0.7273256516206323, 0.6912750784378887, 0.7283328836757055, 0.6958245518964812, 0.5935589075742966, 0.7925254039514394, 0.6644985191424002, 0.7611921967143602, 0.8360246511645772, 0.736912940752686, 0.7437388979790964, 0.7252763688796822, 0.7738612993583308, 0.6296769269455851, 0.7293957761537329, 0.6855038953099516, 0.7568710008015639, 0.6555243610340576, 0.632080919994011, 0.7567216235283071, 0.7210338531928672, 0.7685899806284759, 0.7614118039499029, 0.6725305377111899, 0.71625824744372, 0.7046049843360291, 0.7493833663852183, 0.6914595009893962, 0.7035371081854751, 0.7610080010536411, 0.6411985172909875, 0.7383834124147844], [0.8284891393274991, 0.8966371680649727, 0.9195772861581109, 0.8096456123683311, 0.8963097467375831, 0.8821719119648492, 0.8925196860729419, 0.8611311415245662, 0.8603307948571501, 0.7966913411498896, 0.8744568402738031, 0.8630182318885822, 0.8682434416302964, 0.8038235313560185, 0.9176273347493651, 0.7882603669964707, 0.8736210528262167, 0.7902170324912727, 0.8815332022481752, 0.8750074603353772, 0.8826668717345797, 0.8059651149008048, 0.8261280256488595, 0.9345000850998878, 0.8065329915921992, 0.8900527790213951, 0.9052177508733098, 0.8589028612684031, 0.8442821391402843, 0.9131895146288207, 0.8939551518036337, 0.8083509548411676, 0.9290766416879388, 0.8602498692037983, 0.8829322352645, 0.8406140905084374, 0.7796910326628375, 0.875141468006476, 0.8733591412855645, 0.8759649026972265, 0.8887017317904575, 0.8287839887951518, 0.8490711549799012, 0.8438407839772846, 0.8668413089465953, 0.9312638846621492, 0.8765450722048673, 0.8634970270954407, 0.7669617753783133, 0.8697521983956723], [0.9695681317786946, 0.9853931259035512, 0.9999818617248212, 0.9912875675701746, 0.9993151451669864, 0.9932500217787718, 0.9989029889403633, 0.9911414888526238, 0.9867496109804421, 0.9781256942849984, 0.9654871478817802, 0.9979743689034093, 0.9869426584580809, 0.9967665985929316, 0.9948590934544498, 0.9945360014495885, 0.9816852180055099, 0.9990338912403985, 0.9889718725536456, 0.9804407732858538, 0.9987757249906504, 0.9711883890524422, 0.9792844586586552, 0.9950270668959894, 0.9862142814206124, 0.9883521991715546, 0.9945332690724488, 0.9971870605122254, 0.9568412612757731, 0.9969420042592249, 0.9980356839372131, 0.9910108946412767, 0.9912717677026454, 0.9901814389191206, 0.9985030546027005, 0.9962277070870202, 0.9747443057128958, 0.9953821992831892, 0.9960618690484737, 0.9979377281038238, 0.9858109977028998, 0.991296870435087, 0.9988635668123205, 0.9716782330900225, 0.990429874431542, 0.9927481607716612, 0.983360499312153, 0.9804495316166839, 0.9640889648112012, 0.9885912553999822]], "names": ["x", "y0", "y1", "y2", "y3", "y4"], "id": "t62435803645242ed89b77294c07eb1c0", "title": "Fill Data"}, {"data": [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0], [0.6216777395275461, 0.7076281748609907, 0.7003280368233465, 0.6338546356740591, 0.7443159655702449, 0.674338771936465, 0.6703693748634802, 0.6412784850298605, 0.6624217625587893, 0.573740628601874, 0.6511651481168786, 0.7090785623410046, 0.6629063002906317, 0.5874912952642977, 0.6734011531697023, 0.6243526352040513, 0.6574690228806958, 0.6088274380463801, 0.6673901742219102, 0.6711052114053315, 0.6681747657066398, 0.6090004180833659, 0.5825626150563136, 0.6752497514317171, 0.6279756379394626, 0.7070944876845283, 0.7256741341299277, 0.679392786217188, 0.6787277008960818, 0.6673599108981126, 0.7383950675121644, 0.6291778637433645, 0.6998395948386137, 0.6589576468809824, 0.6809180197527859, 0.6268491675240329, 0.5949206738249487, 0.6927296924168607, 0.6432080961831835, 0.6984040603079754, 0.7134180408372574, 0.6718669599029908, 0.6611784619940745, 0.6413427082798444, 0.6995698280607436, 0.6827445447854436, 0.682845388829927, 0.6514428298779279, 0.6259113154713943, 0.6970815215122211]], "names": ["x", "y0"], "id": "tdb65a80bf2ca4d0e9df3981d70b323b8", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t3d549e35cb41480cb6cbf1e3bd172d5b .toyplot-mark-popup");
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
      var axes = {"t477cbd6fd26f44409911e9ca256d5ab7": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 580.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 340.0}, "scale": "linear"}]}};
    
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


The call to :func:`toyplot.canvas.Canvas.legend` always includes an
explicit list of items to add to the legend, plus a
:ref:`canvas-layout` specification of where the layout should appear
on the canvas. Currently, each item to be displayed should be either:

-  A (label, mark) tuple, which will get its appearance from the mark,
   or:
-  A (label, marker, style) tuple, which will render the given marker
   with the given style.

Of course, ``label`` is the text to be displayed next to an item in the
legend, while ``mark`` is a mark that has been added to the canvas.
However, not all marks can provide an unambiguous legend representation
- what to do when a mark represents multiple series, or has per-datum
colors, markers, or styles? In these cases there isn't a one-to-one
correspondence between marks and legend items, leading to the second
form of legend item with explicit ``marker`` and ``style`` parameters.
The ``marker`` parameter currently can be any of the following:

-  "line" - draw a line in the same style that would be used for a line
   plot.
-  "rect" - draw a filled rect in the same style that would be used for
   a fill plot.
-  marker - draw a marker shape using any of the :ref:`markers` that
   are available for line and scatter plots.

As is the case throughout Toyplot, the ``style`` parameter uses CSS
styles to control the appearance of the item.

There are some subtleties here worth noting, many of which are driven by
Toyplot's deliberate embrace of the philosophy that *explicit is better
than implicit*:

-  You can have as many or as few legends on your canvas as you like.
-  Callers explicitly specify the order and contents of each legend.
-  There is no relationship between axes and legends - you could combine
   marks from multiple axes in a single legend, for example.

Here's an example of all these ideas at work:

.. code:: python

    x = numpy.linspace(0, 1)
    y1 = (1 - x) ** 2
    y2 = numpy.column_stack((1 - (x ** 2), x ** 2))
    
    canvas = toyplot.Canvas(width=600, height=300)
    m1 = canvas.axes(grid=(1,2,0), gutter=15).scatterplot(x, y1, marker="o", color="rgb(255,0,0)")
    m2 = canvas.axes(grid=(1,2,1), gutter=15, yshow=False).scatterplot(x, y2, marker="s", color=["green", "blue"])
    
    canvas.legend([
        ("Experiment 1", "o", {"fill":"rgb(255,0,0)", "stroke": "none"}),
        ("Experiment 2", "s", {"fill":"green", "stroke": "none"}),
        ("Experiment 3", "s", {"fill":"blue", "stroke": "none"}),
    
        ],
        corner=("top", 100, 100, 70),
        );
    




.. raw:: html

    <div align="center" class="toyplot" id="t85ee8a7b9fff4e8386793f2483ca22e5"><svg height="300.0px" id="tbf48e323fd4248a2bfdd43e181e84220" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t6ee4af3a450e45ca936df26bb5491ec6"><clipPath id="td38cf1e5c458456eb906bdc9f394aec0"><rect height="270.0" width="270.0" x="15.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td38cf1e5c458456eb906bdc9f394aec0)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="15.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="t617ceb175664424aa66b463256d8d708" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="25.0" cy="25.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="30.102040816326529" cy="35.099958350687224" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="35.204081632653057" cy="44.991670137442739" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="40.306122448979593" cy="54.675135360266523" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="45.408163265306122" cy="64.150354019158669" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="50.510204081632651" cy="73.41732611411912" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="55.612244897959179" cy="82.476051645147891" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="60.714285714285715" cy="91.326530612244852" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="65.816326530612244" cy="99.968763015410218" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="70.918367346938766" cy="108.40274885464387" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="76.020408163265301" cy="116.62848812994588" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="81.122448979591823" cy="124.64598084131613" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="86.224489795918359" cy="132.4552269887547" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="91.326530612244895" cy="140.05622657226155" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="96.428571428571431" cy="147.44897959183672" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="101.53061224489795" cy="154.6334860474802" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="106.63265306122449" cy="161.60974593919198" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="111.73469387755101" cy="168.37775926697208" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="116.83673469387755" cy="174.93752603082049" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="121.93877551020408" cy="181.2890462307372" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="127.0408163265306" cy="187.4323198667222" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="132.14285714285714" cy="193.36734693877551" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="137.24489795918365" cy="199.09412744689712" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="142.34693877551018" cy="204.61266139108704" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="147.44897959183672" cy="209.92294877134526" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="152.55102040816328" cy="215.0249895876718" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="157.65306122448979" cy="219.9187838400666" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="162.75510204081633" cy="224.60433152852977" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="167.85714285714286" cy="229.08163265306123" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="172.9591836734694" cy="233.35068721366096" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="178.0612244897959" cy="237.41149521032901" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="183.16326530612244" cy="241.26405664306537" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="188.26530612244895" cy="244.90837151187003" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="193.36734693877548" cy="248.34443981674301" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="198.46938775510202" cy="251.5722615576843" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="203.57142857142856" cy="254.59183673469386" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="208.67346938775509" cy="257.40316534777173" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="213.77551020408163" cy="260.00624739691796" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="218.87755102040816" cy="262.40108288213241" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="223.97959183673467" cy="264.58767180341522" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="229.08163265306121" cy="266.56601416076637" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="234.18367346938774" cy="268.33610995418576" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="239.28571428571428" cy="269.89795918367344" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="244.38775510204081" cy="271.25156184922946" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="249.48979591836729" cy="272.39691795085383" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="254.59183673469386" cy="273.33402748854644" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="259.69387755102036" cy="274.06289046230739" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="264.79591836734693" cy="274.58350687213658" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="269.89795918367344" cy="274.89587671803417" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgba(100%,0%,0%,1);opacity:1.0;stroke:rgba(100%,0%,0%,1)"><circle cx="275.0" cy="275.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="185.0" y="25.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="230.0" y="32.0"></text></g><line style="" x1="25.0" x2="275.0" y1="285.0" y2="285.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="25.0" y="285.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="150.0" y="285.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="275.0" y="285.0">1.0</text></g><line style="" x1="15.0" x2="15.0" y1="25.0" y2="275.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 275.0)" x="15.0" y="275.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 150.0)" x="15.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 15.0, 25.0)" x="15.0" y="25.0">1.0</text></g></g><g class="toyplot-axes-Cartesian" id="t0659f3726f9f4706b232c6f906e45d6c"><clipPath id="t6e441f87b9f7417997a8d4e2824a0f64"><rect height="270.0" width="270.0" x="315.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t6e441f87b9f7417997a8d4e2824a0f64)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="315.0" y="15.0"></rect><g class="toyplot-mark-Plot" id="t1bbab30ced8a42249c53e2855c10e43e" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 325.0, 25.0)" width="4.4721359549995796" x="322.76393202250023" y="22.76393202250021"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 330.10204081632651, 25.104123281965848)" width="4.4721359549995796" x="327.86597283882674" y="22.868055304466058"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 335.20408163265307, 25.416493127863376)" width="4.4721359549995796" x="332.9680136551533" y="23.180425150363586"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 340.30612244897964, 25.937109537692631)" width="4.4721359549995796" x="338.07005447147986" y="23.701041560192841"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 345.40816326530614, 26.665972511453564)" width="4.4721359549995796" x="343.17209528780637" y="24.429904533953774"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 350.51020408163265, 27.603082049146195)" width="4.4721359549995796" x="348.27413610413288" y="25.367014071646405"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 355.61224489795916, 28.7484381507705)" width="4.4721359549995796" x="353.37617692045939" y="26.51237017327071"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 360.71428571428578, 30.102040816326536)" width="4.4721359549995796" x="358.47821773678601" y="27.865972838826746"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 365.81632653061229, 31.663890045814245)" width="4.4721359549995796" x="363.58025855311251" y="29.427822068314455"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 370.91836734693874, 33.433985839233657)" width="4.4721359549995796" x="368.68229936943897" y="31.197917861733867"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 376.0204081632653, 35.412328196584745)" width="4.4721359549995796" x="373.78434018576553" y="33.176260219084952"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 381.12244897959181, 37.598917117867565)" width="4.4721359549995796" x="378.88638100209204" y="35.362849140367771"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 386.22448979591832, 39.993752603082058)" width="4.4721359549995796" x="383.98842181841854" y="37.757684625582272"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 391.32653061224494, 42.596834652228225)" width="4.4721359549995796" x="389.09046263474517" y="40.360766674728438"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 396.42857142857144, 45.408163265306115)" width="4.4721359549995796" x="394.19250345107167" y="43.172095287806329"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 401.53061224489795, 48.427738442315686)" width="4.4721359549995796" x="399.29454426739818" y="46.1916704648159"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 406.63265306122452, 51.655560183256959)" width="4.4721359549995796" x="404.39658508372474" y="49.419492205757166"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 411.73469387755108, 55.091628488129928)" width="4.4721359549995796" x="409.49862590005131" y="52.855560510630141"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 416.83673469387753, 58.735943356934612)" width="4.4721359549995796" x="414.60066671637776" y="56.499875379434826"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 421.9387755102041, 62.588504789670964)" width="4.4721359549995796" x="419.70270753270432" y="60.352436812171177"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 427.0408163265306, 66.64931278633901)" width="4.4721359549995796" x="424.80474834903083" y="64.413244808839224"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 432.14285714285711, 70.918367346938766)" width="4.4721359549995796" x="429.90678916535734" y="68.682299369438979"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 437.24489795918362, 75.395668471470202)" width="4.4721359549995796" x="435.00882998168385" y="73.159600493970416"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 442.34693877551018, 80.081216159933362)" width="4.4721359549995796" x="440.11087079801041" y="77.845148182433576"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 447.44897959183675, 84.975010412328189)" width="4.4721359549995796" x="445.21291161433697" y="82.738942434828402"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 452.55102040816325, 90.077051228654724)" width="4.4721359549995796" x="450.31495243066348" y="87.840983251154938"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 457.65306122448976, 95.387338608912941)" width="4.4721359549995796" x="455.41699324698999" y="93.151270631413155"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 462.75510204081633, 100.90587255310285)" width="4.4721359549995796" x="460.51903406331655" y="98.669804575603067"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 467.85714285714289, 106.63265306122446)" width="4.4721359549995796" x="465.62107487964312" y="104.39658508372467"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 472.9591836734694, 112.5676801332778)" width="4.4721359549995796" x="470.72311569596962" y="110.33161215577802"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 478.0612244897959, 118.71095376926277)" width="4.4721359549995796" x="475.82515651229613" y="116.47488579176299"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 483.16326530612241, 125.06247396917951)" width="4.4721359549995796" x="480.92719732862264" y="122.82640599167972"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 488.26530612244898, 131.62224073302789)" width="4.4721359549995796" x="486.0292381449492" y="129.38617275552809"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 493.36734693877554, 138.39025406080799)" width="4.4721359549995796" x="491.13127896127577" y="136.15418608330819"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 498.46938775510205, 145.36651395251977)" width="4.4721359549995796" x="496.23331977760228" y="143.13044597501997"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 503.57142857142856, 152.55102040816323)" width="4.4721359549995796" x="501.33536059392878" y="150.31495243066342"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 508.67346938775506, 159.94377342773842)" width="4.4721359549995796" x="506.43740141025529" y="157.70770545023862"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 513.77551020408157, 167.5447730112453)" width="4.4721359549995796" x="511.5394422265818" y="165.3087050337455"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 518.87755102040819, 175.35401915868388)" width="4.4721359549995796" x="516.64148304290836" y="173.11795118118408"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 523.9795918367347, 183.37151187005409)" width="4.4721359549995796" x="521.74352385923487" y="181.13544389255429"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 529.08163265306121, 191.59725114535607)" width="4.4721359549995796" x="526.84556467556138" y="189.36118316785627"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 534.18367346938771, 200.03123698458973)" width="4.4721359549995796" x="531.94760549188788" y="197.79516900708992"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 539.28571428571422, 208.67346938775509)" width="4.4721359549995796" x="537.04964630821439" y="206.43740141025529"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 544.38775510204084, 217.52394835485214)" width="4.4721359549995796" x="542.15168712454101" y="215.28788037735234"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 549.48979591836735, 226.58267388588084)" width="4.4721359549995796" x="547.25372794086752" y="224.34660590838104"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 554.59183673469386, 235.84964598084127)" width="4.4721359549995796" x="552.35576875719403" y="233.61357800334147"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 559.69387755102036, 245.32486463973342)" width="4.4721359549995796" x="557.45780957352054" y="243.08879666223362"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 564.79591836734699, 255.00832986255728)" width="4.4721359549995796" x="562.55985038984716" y="252.77226188505747"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 569.89795918367338, 264.90004164931275)" width="4.4721359549995796" x="567.66189120617355" y="262.66397367181298"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,50.2%,0%,1);opacity:1.0;stroke:rgba(0%,50.2%,0%,1)"><rect height="4.4721359549995796" transform="rotate(0, 575.0, 275.0)" width="4.4721359549995796" x="572.76393202250017" y="272.76393202250023"></rect></g></g><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 325.0, 275.0)" width="4.4721359549995796" x="322.76393202250023" y="272.76393202250023"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 330.10204081632651, 274.89587671803417)" width="4.4721359549995796" x="327.86597283882674" y="272.6598087405344"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 335.20408163265307, 274.58350687213658)" width="4.4721359549995796" x="332.9680136551533" y="272.34743889463681"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 340.30612244897964, 274.06289046230739)" width="4.4721359549995796" x="338.07005447147986" y="271.82682248480762"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 345.40816326530614, 273.33402748854644)" width="4.4721359549995796" x="343.17209528780637" y="271.09795951104667"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 350.51020408163265, 272.39691795085383)" width="4.4721359549995796" x="348.27413610413288" y="270.16084997335406"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 355.61224489795916, 271.25156184922952)" width="4.4721359549995796" x="353.37617692045939" y="269.01549387172975"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 360.71428571428578, 269.89795918367344)" width="4.4721359549995796" x="358.47821773678601" y="267.66189120617366"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 365.81632653061229, 268.33610995418576)" width="4.4721359549995796" x="363.58025855311251" y="266.10004197668599"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 370.91836734693874, 266.56601416076637)" width="4.4721359549995796" x="368.68229936943897" y="264.3299461832666"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 376.0204081632653, 264.58767180341528)" width="4.4721359549995796" x="373.78434018576553" y="262.3516038259155"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 381.12244897959181, 262.40108288213241)" width="4.4721359549995796" x="378.88638100209204" y="260.16501490463264"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 386.22448979591832, 260.00624739691796)" width="4.4721359549995796" x="383.98842181841854" y="257.77017941941818"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 391.32653061224494, 257.40316534777179)" width="4.4721359549995796" x="389.09046263474517" y="255.16709737027199"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 396.42857142857144, 254.59183673469389)" width="4.4721359549995796" x="394.19250345107167" y="252.35576875719408"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 401.53061224489795, 251.57226155768433)" width="4.4721359549995796" x="399.29454426739818" y="249.33619358018453"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 406.63265306122452, 248.34443981674303)" width="4.4721359549995796" x="404.39658508372474" y="246.10837183924323"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 411.73469387755108, 244.90837151187006)" width="4.4721359549995796" x="409.49862590005131" y="242.67230353437026"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 416.83673469387753, 241.2640566430654)" width="4.4721359549995796" x="414.60066671637776" y="239.0279886655656"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 421.9387755102041, 237.41149521032904)" width="4.4721359549995796" x="419.70270753270432" y="235.17542723282924"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 427.0408163265306, 233.35068721366099)" width="4.4721359549995796" x="424.80474834903083" y="231.11461923616119"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 432.14285714285711, 229.08163265306123)" width="4.4721359549995796" x="429.90678916535734" y="226.84556467556143"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 437.24489795918362, 224.6043315285298)" width="4.4721359549995796" x="435.00882998168385" y="222.36826355103"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 442.34693877551018, 219.91878384006662)" width="4.4721359549995796" x="440.11087079801041" y="217.68271586256682"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 447.44897959183675, 215.0249895876718)" width="4.4721359549995796" x="445.21291161433697" y="212.788921610172"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 452.55102040816325, 209.92294877134526)" width="4.4721359549995796" x="450.31495243066348" y="207.68688079384546"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 457.65306122448976, 204.61266139108704)" width="4.4721359549995796" x="455.41699324698999" y="202.37659341358724"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 462.75510204081633, 199.09412744689715)" width="4.4721359549995796" x="460.51903406331655" y="196.85805946939735"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 467.85714285714289, 193.36734693877551)" width="4.4721359549995796" x="465.62107487964312" y="191.13127896127571"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 472.9591836734694, 187.4323198667222)" width="4.4721359549995796" x="470.72311569596962" y="185.1962518892224"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 478.0612244897959, 181.2890462307372)" width="4.4721359549995796" x="475.82515651229613" y="179.0529782532374"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 483.16326530612241, 174.93752603082049)" width="4.4721359549995796" x="480.92719732862264" y="172.70145805332069"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 488.26530612244898, 168.37775926697211)" width="4.4721359549995796" x="486.0292381449492" y="166.14169128947231"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 493.36734693877554, 161.60974593919201)" width="4.4721359549995796" x="491.13127896127577" y="159.37367796169221"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 498.46938775510205, 154.6334860474802)" width="4.4721359549995796" x="496.23331977760228" y="152.3974180699804"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 503.57142857142856, 147.44897959183677)" width="4.4721359549995796" x="501.33536059392878" y="145.21291161433697"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 508.67346938775506, 140.05622657226158)" width="4.4721359549995796" x="506.43740141025529" y="137.82015859476178"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 513.77551020408157, 132.4552269887547)" width="4.4721359549995796" x="511.5394422265818" y="130.2191590112549"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 518.87755102040819, 124.64598084131613)" width="4.4721359549995796" x="516.64148304290836" y="122.40991286381634"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 523.9795918367347, 116.62848812994591)" width="4.4721359549995796" x="521.74352385923487" y="114.39242015244612"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 529.08163265306121, 108.40274885464393)" width="4.4721359549995796" x="526.84556467556138" y="106.16668087714415"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 534.18367346938771, 99.968763015410275)" width="4.4721359549995796" x="531.94760549188788" y="97.732695037910489"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 539.28571428571422, 91.326530612244923)" width="4.4721359549995796" x="537.04964630821439" y="89.090462634745137"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 544.38775510204084, 82.476051645147891)" width="4.4721359549995796" x="542.15168712454101" y="80.239983667648104"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 549.48979591836735, 73.417326114119163)" width="4.4721359549995796" x="547.25372794086752" y="71.181258136619377"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 554.59183673469386, 64.150354019158726)" width="4.4721359549995796" x="552.35576875719403" y="61.91428604165894"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 559.69387755102036, 54.675135360266587)" width="4.4721359549995796" x="557.45780957352054" y="52.439067382766794"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 564.79591836734699, 44.991670137442739)" width="4.4721359549995796" x="562.55985038984716" y="42.755602159942953"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 569.89795918367338, 35.099958350687224)" width="4.4721359549995796" x="567.66189120617355" y="32.863890373187431"></rect></g><g class="toyplot-Datum" style="fill:rgba(0%,0%,100%,1);opacity:1.0;stroke:rgba(0%,0%,100%,1)"><rect height="4.4721359549995796" transform="rotate(0, 575.0, 25.0)" width="4.4721359549995796" x="572.76393202250017" y="22.76393202250021"></rect></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="485.0" y="25.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="530.0" y="32.0"></text></g><line style="" x1="325.0" x2="575.0" y1="285.0" y2="285.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="325.0" y="285.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="450.0" y="285.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="575.0" y="285.0">1.0</text></g></g><rect class="toyplot-mark-Legend" height="70.0" id="tb1aaf3150c7a40a8be52aef720a0aab1" style="fill:none;stroke:none" width="100.0" x="250.0" y="100.0"></rect><g style="fill:rgb(255,0,0);stroke:none"><circle cx="265.0" cy="115.0" r="5.0"></circle></g><text style="alignment-baseline:middle;stroke:none" x="280.0" y="115.0">Experiment 1</text><g style="fill:green;stroke:none"><rect height="10.0" transform="rotate(0, 265.0, 135.0)" width="10.0" x="260.0" y="130.0"></rect></g><text style="alignment-baseline:middle;stroke:none" x="280.0" y="135.0">Experiment 2</text><g style="fill:blue;stroke:none"><rect height="10.0" transform="rotate(0, 265.0, 155.0)" width="10.0" x="260.0" y="150.0"></rect></g><text style="alignment-baseline:middle;stroke:none" x="280.0" y="155.0">Experiment 3</text></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t85ee8a7b9fff4e8386793f2483ca22e5 text");
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
          var text = document.querySelectorAll("#t85ee8a7b9fff4e8386793f2483ca22e5 text");
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
      var data_tables = [{"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [1.0, 0.9596001665972511, 0.920033319450229, 0.8812994585589339, 0.8433985839233653, 0.8063306955435235, 0.7700957934194085, 0.7346938775510206, 0.7001249479383591, 0.6663890045814245, 0.6334860474802165, 0.6014160766347355, 0.5701790920449812, 0.5397750937109538, 0.5102040816326531, 0.4814660558100793, 0.4535610162432321, 0.4264889629321117, 0.40024989587671805, 0.3748438150770512, 0.3502707205331112, 0.32653061224489793, 0.3036234902124116, 0.2815493544356518, 0.2603082049146189, 0.23990004164931278, 0.22032486463973353, 0.20158267388588094, 0.18367346938775514, 0.16659725114535612, 0.15035401915868396, 0.1349437734277385, 0.12036651395251982, 0.10662224073302792, 0.0937109537692628, 0.08163265306122454, 0.070387338608913, 0.05997501041232822, 0.050395668471470235, 0.04164931278633907, 0.033735943356934646, 0.026655560183256998, 0.020408163265306135, 0.014993752603082056, 0.01041232819658478, 0.006663890045814259, 0.0037484381507705204, 0.0016659725114535648, 0.0004164931278633912, 0.0]], "names": ["x", "y0"], "id": "t617ceb175664424aa66b463256d8d708", "title": "Plot Data"}, {"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [1.0, 0.9995835068721366, 0.9983340274885465, 0.9962515618492295, 0.9933361099541858, 0.9895876718034152, 0.985006247396918, 0.9795918367346939, 0.973344439816743, 0.9662640566430654, 0.958350687213661, 0.9496043315285297, 0.9400249895876718, 0.9296126613910871, 0.9183673469387755, 0.9062890462307372, 0.8933777592669722, 0.8796334860474803, 0.8650562265722616, 0.8496459808413162, 0.8334027488546439, 0.8163265306122449, 0.7984173261141192, 0.7796751353602666, 0.7600999583506872, 0.7396917950853811, 0.7184506455643482, 0.6963765097875886, 0.6734693877551021, 0.6497292794668887, 0.6251561849229489, 0.599750104123282, 0.5735110370678884, 0.546438983756768, 0.5185339441899208, 0.48979591836734704, 0.46022490628904633, 0.4298209079550188, 0.3985839233652645, 0.3665139525197836, 0.33361099541857575, 0.2998750520616411, 0.26530612244897966, 0.22990420658059152, 0.19366930445647668, 0.15660141607663491, 0.11870054144106634, 0.07996668054977096, 0.040399833402748886, 0.0], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "names": ["x", "y0", "y1"], "id": "t1bbab30ced8a42249c53e2855c10e43e", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t85ee8a7b9fff4e8386793f2483ca22e5 .toyplot-mark-popup");
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
      var axes = {"t0659f3726f9f4706b232c6f906e45d6c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 575.0, "min": 325.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}, "t6ee4af3a450e45ca936df26bb5491ec6": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 275.0, "min": 25.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}};
    
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


