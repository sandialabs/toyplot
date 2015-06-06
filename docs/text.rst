
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _text:

Text
====

Alignment
---------

By default, a text datum in Toyplot is centered vertically and
horizontally on its coordinates. For example, in the following figure we
rendered some text, then plotted its coordinates using a black dot:

.. code:: python

    import toyplot
    
    canvas = toyplot.Canvas(width=500, height=150)
    axes = canvas.axes(show=False)
    axes.text(0, 0, "Text!", style={"font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7);



.. raw:: html

    <div align="center" class="toyplot" id="t9b7df1a5692e46c4a5c84a0e98702efd"><svg height="150.0px" id="t9d3b3dd5eb324f15b37c422548eaf1f4" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc1bd1b15dcf746f19c0732055d914175"><clipPath id="tcfb83131d0f740bcad7069ad16bd9816"><rect height="50.0" width="400.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tcfb83131d0f740bcad7069ad16bd9816)" style="cursor:crosshair"><rect height="50.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Text" id="t417cc3ee5c104d87a279cb23f3821def" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 250.0, 75.0)" x="250.0" y="75.0">Text!</text></g></g><g class="toyplot-mark-Plot" id="te3147f8c2f9b49a88d277e03ad04eb45" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="250.0" cy="75.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t9b7df1a5692e46c4a5c84a0e98702efd text");
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
          var text = document.querySelectorAll("#t9b7df1a5692e46c4a5c84a0e98702efd text");
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
      var data_tables = [{"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "te3147f8c2f9b49a88d277e03ad04eb45", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t9b7df1a5692e46c4a5c84a0e98702efd .toyplot-mark-popup");
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
      var axes = {"tc1bd1b15dcf746f19c0732055d914175": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 90.0}, "scale": "linear"}]}};
    
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


To control the horizontal alignment, use the ``text-anchor`` CSS
attribute to change the text justification relative to its X coordinate:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes(show=False)
    
    axes.plot([0, 0], [-2, 2], color="gray", style={"stroke-width":1})
    
    axes.text(0, 1, "Centered", style={"text-anchor":"middle", "font-size":"24px"})
    axes.scatterplot(0, 1, color="black", size=7)
    
    axes.text(0, 0, "Left Justified", style={"text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7)
    
    axes.text(0, -1, "Right Justified", style={"text-anchor":"end", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black", size=7);



.. raw:: html

    <div align="center" class="toyplot" id="t705ec1cf9df945bba4214d949f50c49c"><svg height="300.0px" id="t2b382cd30fe046a7b1619354879310f4" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t63ab5dc6088a4876be62d1a2c3162ee0"><clipPath id="t5b586a65bff14dd3be93707d6aca401a"><rect height="200.0" width="400.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t5b586a65bff14dd3be93707d6aca401a)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="tf2674744cac5439b86b24e184c8818d9" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 256.55172413793105 240.0 L 256.55172413793105 60.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t291c3496201d4430986a4f99515417e3" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 256.55172413793105, 105.0)" x="256.55172413793105" y="105.0">Centered</text></g></g><g class="toyplot-mark-Plot" id="t04ebaf2ffebe42f89785a3089edc7897" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="256.55172413793105" cy="105.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t845c89843bda48ef9303555730a61765" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 256.55172413793105, 150.0)" x="256.55172413793105" y="150.0">Left Justified</text></g></g><g class="toyplot-mark-Plot" id="t776dacb9012840b18867b993908e9a6f" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="256.55172413793105" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t2abf48f0ad38460da1c3d0f90253ecb7" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:end"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:end" transform="rotate(-0.0, 256.55172413793105, 195.0)" x="256.55172413793105" y="195.0">Right Justified</text></g></g><g class="toyplot-mark-Plot" id="t47c4e52c403946ed9040d6d819085a25" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="256.55172413793105" cy="195.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t705ec1cf9df945bba4214d949f50c49c text");
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
          var text = document.querySelectorAll("#t705ec1cf9df945bba4214d949f50c49c text");
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
      var data_tables = [{"data": [[0.0, 0.0], [-2.0, 2.0]], "names": ["x", "y0"], "id": "tf2674744cac5439b86b24e184c8818d9", "title": "Plot Data"}, {"data": [[0.0], [1.0]], "names": ["x", "y0"], "id": "t04ebaf2ffebe42f89785a3089edc7897", "title": "Plot Data"}, {"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "t776dacb9012840b18867b993908e9a6f", "title": "Plot Data"}, {"data": [[0.0], [-1.0]], "names": ["x", "y0"], "id": "t47c4e52c403946ed9040d6d819085a25", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t705ec1cf9df945bba4214d949f50c49c .toyplot-mark-popup");
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
      var axes = {"t63ab5dc6088a4876be62d1a2c3162ee0": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.88421052631578956, "min": -0.94736842105263164}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": -2.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


After the anchor has been established, the text can be shifted in
arbitrary amounts, using the ``-toyplot-anchor-shift`` attribute. Note
that this is non-standard CSS, provided by Toyplot for symmetry with the
standard ``baseline-shift`` attribute, below:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.axes(show=False)
    
    axes.plot([0, 0], [-3, 2], color="gray", style={"stroke-width":1})
    
    axes.text(0, 1, "Shifted +0px", style={"-toyplot-anchor-shift":"0", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 1, color="black", size=7)
    
    axes.text(0, 0, "Shifted +20px", style={"-toyplot-anchor-shift":"20px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7)
    
    axes.text(0, -1, "Shifted +40px", style={"-toyplot-anchor-shift":"40px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black", size=7);
    
    axes.text(0, -2, "Shifted -20px", style={"-toyplot-anchor-shift":"-20px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, -2, color="black", size=7);




.. raw:: html

    <div align="center" class="toyplot" id="t0ce807adf1554ca9959cccd81cd2cc6b"><svg height="300.0px" id="tb2a22e7f544347b3b7eab6e5475673e1" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t6f7efa4d137c4475aa72c186a6dfc5b3"><clipPath id="t9933de733f00403b8d5c55e1d25a44c8"><rect height="200.0" width="400.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9933de733f00403b8d5c55e1d25a44c8)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="400.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t44ef25bbb45f467e8b49d29ca0b32fac" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 193.21033210332104 240.0 L 193.21033210332104 60.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t29d4f4e3070c4b9aa018d6ad4031fe55" style="-toyplot-anchor-shift:0;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="0" style="-toyplot-anchor-shift:0;alignment-baseline:middle;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 193.21033210332104, 95.999999999999986)" x="193.21033210332104" y="95.999999999999986">Shifted +0px</text></g></g><g class="toyplot-mark-Plot" id="tedcc052a8f2b48feae2aa132243d5cc7" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="193.21033210332104" cy="95.999999999999986" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tef2b837a30f24d31a3050c526091aae3" style="-toyplot-anchor-shift:20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="20px" style="-toyplot-anchor-shift:20px;alignment-baseline:middle;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 193.21033210332104, 132.0)" x="193.21033210332104" y="132.0">Shifted +20px</text></g></g><g class="toyplot-mark-Plot" id="t41becde1f9b64eaf89728bb0141d483c" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="193.21033210332104" cy="132.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tb98d434c15174f1b949edf94f6673601" style="-toyplot-anchor-shift:40px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="40px" style="-toyplot-anchor-shift:40px;alignment-baseline:middle;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 193.21033210332104, 168.0)" x="193.21033210332104" y="168.0">Shifted +40px</text></g></g><g class="toyplot-mark-Plot" id="td94aff00a80e4b3e944899e44d505483" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="193.21033210332104" cy="168.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t6404922c192f4abab457b8b5d90b471a" style="-toyplot-anchor-shift:-20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="-20px" style="-toyplot-anchor-shift:-20px;alignment-baseline:middle;fill:rgba(90.6%,54.1%,76.5%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 193.21033210332104, 204.0)" x="193.21033210332104" y="204.0">Shifted -20px</text></g></g><g class="toyplot-mark-Plot" id="t13281de4e2ed4561bab98a9a07ea83e9" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="193.21033210332104" cy="204.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t0ce807adf1554ca9959cccd81cd2cc6b text");
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
          var text = document.querySelectorAll("#t0ce807adf1554ca9959cccd81cd2cc6b text");
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
      var data_tables = [{"data": [[0.0, 0.0], [-3.0, 2.0]], "names": ["x", "y0"], "id": "t44ef25bbb45f467e8b49d29ca0b32fac", "title": "Plot Data"}, {"data": [[0.0], [1.0]], "names": ["x", "y0"], "id": "tedcc052a8f2b48feae2aa132243d5cc7", "title": "Plot Data"}, {"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "t41becde1f9b64eaf89728bb0141d483c", "title": "Plot Data"}, {"data": [[0.0], [-1.0]], "names": ["x", "y0"], "id": "td94aff00a80e4b3e944899e44d505483", "title": "Plot Data"}, {"data": [[0.0], [-2.0]], "names": ["x", "y0"], "id": "t13281de4e2ed4561bab98a9a07ea83e9", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#t0ce807adf1554ca9959cccd81cd2cc6b .toyplot-mark-popup");
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
      var axes = {"t6f7efa4d137c4475aa72c186a6dfc5b3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.9263157894736842, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 440.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.0, "min": -3.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


To control vertical alignment, set the text baseline with
``alignment-baseline``. By default, the text baseline will line-up with
the text Y coordinate. CSS typography is a complex topic and there are
many baseline types to accomodate different writing modes and fonts. The
following baselines are likely to be the most useful for Western
scripts. Note the subtle difference between the "central" and "middle"
baselines - the former tends to center the upper-case letters in Western
scripts while the latter tends to center lower-case letters, and is the
Toyplot default:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.axes(show=False)
    
    axes.plot([-2, 3], [0, 0], color="gray", style={"stroke-width":1})
    
    axes.text(-1, 0, "Hanging", style={"alignment-baseline":"hanging", "font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=7)
    
    axes.text(0, 0, "Central", style={"alignment-baseline":"central", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7)
    
    axes.text(1, 0, "Middle", style={"alignment-baseline":"middle", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black", size=7)
    
    axes.text(2, 0, "Alpha", style={"alignment-baseline":"alphabetic", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black", size=7);




.. raw:: html

    <div align="center" class="toyplot" id="tc6a32eed84a04ff8af1bf70865850dfb"><svg height="300.0px" id="tcb7849601b8a441eb0c510d4455aeb1a" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tbd8ea7da8d8a4a3a90a7c0f7fd267e87"><clipPath id="tc1789e8e83474f80bc3f7d9de9630878"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tc1789e8e83474f80bc3f7d9de9630878)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t592e17576ddb43988a1684e12db5e545" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 60.0 150.0 L 540.0 150.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t7b0fb5fb6b244b428b2348c753f47fdc" style="alignment-baseline:hanging;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:hanging;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 156.0, 150.0)" x="156.0" y="150.0">Hanging</text></g></g><g class="toyplot-mark-Plot" id="tac91851862d94a2599c52522facf8606" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="156.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t47425469121648be9653e19dacfe779c" style="alignment-baseline:central;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:central;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 252.0, 150.0)" x="252.0" y="150.0">Central</text></g></g><g class="toyplot-mark-Plot" id="t964bd796d11f451e869fdf34b87e9323" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="252.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tab8367462727411faedb1c8c95ec25d5" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 348.0, 150.0)" x="348.0" y="150.0">Middle</text></g></g><g class="toyplot-mark-Plot" id="t75d2ee40c1b242a890e7a4c4f4b648ca" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="348.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tff6f9015f0854678a1c36f241ea64453" style="alignment-baseline:alphabetic;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:alphabetic;fill:rgba(90.6%,54.1%,76.5%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 444.0, 150.0)" x="444.0" y="150.0">Alpha</text></g></g><g class="toyplot-mark-Plot" id="t3e04ac3052b9482b995633a520d0a343" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="444.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tc6a32eed84a04ff8af1bf70865850dfb text");
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
          var text = document.querySelectorAll("#tc6a32eed84a04ff8af1bf70865850dfb text");
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
      var data_tables = [{"data": [[-2.0, 3.0], [0.0, 0.0]], "names": ["x", "y0"], "id": "t592e17576ddb43988a1684e12db5e545", "title": "Plot Data"}, {"data": [[-1.0], [0.0]], "names": ["x", "y0"], "id": "tac91851862d94a2599c52522facf8606", "title": "Plot Data"}, {"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "t964bd796d11f451e869fdf34b87e9323", "title": "Plot Data"}, {"data": [[1.0], [0.0]], "names": ["x", "y0"], "id": "t75d2ee40c1b242a890e7a4c4f4b648ca", "title": "Plot Data"}, {"data": [[2.0], [0.0]], "names": ["x", "y0"], "id": "t3e04ac3052b9482b995633a520d0a343", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tc6a32eed84a04ff8af1bf70865850dfb .toyplot-mark-popup");
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
      var axes = {"tbd8ea7da8d8a4a3a90a7c0f7fd267e87": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0, "min": -2.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Of course, you can shift the text relative to its baseline by arbitrary
amounts, using ``baseline-shift``. While you are free to use any CSS
length units for the shift, percentages are especially useful, because
they represent a distance relative to the font height:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=300)
    axes = canvas.axes(show=False)
    
    axes.plot([-2, 3], [0, 0], color="gray", style={"stroke-width":1})
    
    axes.text(-1, 0, "Shift -100%", style={"baseline-shift":"-100%", "font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=7)
    
    axes.text(0, 0, "Shift 0%", style={"baseline-shift":"0", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=7)
    
    axes.text(1, 0, "Shift 66%", style={"baseline-shift":"66%", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black", size=7);
    
    axes.text(2, 0, "Shift 100%", style={"baseline-shift":"100%", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black", size=7);




.. raw:: html

    <div align="center" class="toyplot" id="tfc8a8f7cc1e04118821e75641558288b"><svg height="300.0px" id="tb795cf6b8ef04208834b7a948b93ae27" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t01c76bf5ea394db591d277b6db3e986a"><clipPath id="t33d545441d4c4585b4075109196288c2"><rect height="200.0" width="600.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t33d545441d4c4585b4075109196288c2)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="600.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t0ab0582ef62a447eb402d14071bb8582" style="fill:none;stroke-width:1"><g class="toyplot-Series"><path d="M 75.466666666666697 150.0 L 636.13333333333333 150.0" style="fill:none;stroke:rgba(50.2%,50.2%,50.2%,1);stroke-opacity:1.0;stroke-width:1"></path></g></g><g class="toyplot-mark-Text" id="t455a13709d7442249c2166ee2afade49" style="alignment-baseline:middle;baseline-shift:-100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:-100%;fill:rgba(40%,76.1%,64.7%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 187.60000000000002, 150.0)" x="187.60000000000002" y="150.0">Shift -100%</text></g></g><g class="toyplot-mark-Plot" id="t4dec3d57be9844d9b4fb710f30613be3" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="187.60000000000002" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="tf1038a6d89594baaade274df2351fe36" style="alignment-baseline:middle;baseline-shift:0;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:0;fill:rgba(98.8%,55.3%,38.4%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 299.73333333333335, 150.0)" x="299.73333333333335" y="150.0">Shift 0%</text></g></g><g class="toyplot-mark-Plot" id="t1beda090c0294525a0e9d2a91e2a6a30" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="299.73333333333335" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t23837c984fd24e98bb55f63260c8ddf6" style="alignment-baseline:middle;baseline-shift:66%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:66%;fill:rgba(55.3%,62.7%,79.6%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 411.86666666666667, 150.0)" x="411.86666666666667" y="150.0">Shift 66%</text></g></g><g class="toyplot-mark-Plot" id="td8436b7b980548318923323cdd2eaf9d" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="411.86666666666667" cy="150.0" r="1.3228756555322954"></circle></g></g></g><g class="toyplot-mark-Text" id="t56cb6056d108427fbb273b067493d7c0" style="alignment-baseline:middle;baseline-shift:100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;baseline-shift:100%;fill:rgba(90.6%,54.1%,76.5%,1);font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 524.0, 150.0)" x="524.0" y="150.0">Shift 100%</text></g></g><g class="toyplot-mark-Plot" id="t9a3f7243bcdc43d7851fca56244891d3" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgba(0%,0%,0%,1);opacity:1.0;stroke:rgba(0%,0%,0%,1)"><circle cx="524.0" cy="150.0" r="1.3228756555322954"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="550.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="595.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tfc8a8f7cc1e04118821e75641558288b text");
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
          var text = document.querySelectorAll("#tfc8a8f7cc1e04118821e75641558288b text");
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
      var data_tables = [{"data": [[-2.0, 3.0], [0.0, 0.0]], "names": ["x", "y0"], "id": "t0ab0582ef62a447eb402d14071bb8582", "title": "Plot Data"}, {"data": [[-1.0], [0.0]], "names": ["x", "y0"], "id": "t4dec3d57be9844d9b4fb710f30613be3", "title": "Plot Data"}, {"data": [[0.0], [0.0]], "names": ["x", "y0"], "id": "t1beda090c0294525a0e9d2a91e2a6a30", "title": "Plot Data"}, {"data": [[1.0], [0.0]], "names": ["x", "y0"], "id": "td8436b7b980548318923323cdd2eaf9d", "title": "Plot Data"}, {"data": [[2.0], [0.0]], "names": ["x", "y0"], "id": "t9a3f7243bcdc43d7851fca56244891d3", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#tfc8a8f7cc1e04118821e75641558288b .toyplot-mark-popup");
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
      var axes = {"t01c76bf5ea394db591d277b6db3e986a": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0344827586206899, "min": -2.1379310344827589}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 640.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Of course, you're free to combine all four styles in any way that you
like.
