
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _interaction:

Interaction
-----------

A key goal for the Toyplot team is to explore interactive features for
plots, making them truly useful and embeddable, so that they become a
ubiquitous part of every data graphic user's experience. The following
examples of interaction are just scratching the surface of what we have
planned for Toyplot:

Titles
~~~~~~

Most of the visualization types in Toyplot accept a ``title`` parameter,
allowing you to specify per-series or per-datum titles for a figure.
With Toyplot's preferred embeddable HTML output, those titles are
displayed via a popup when hovering over the data. For example, the
following figure has a global title "Employee Schedule", which you
should see as a popup when you hover the mouse over any of the bars:

.. code:: python

    import numpy
    numpy.random.seed(1234)
    start = numpy.random.normal(loc=8, scale=1, size=20)
    end = numpy.random.normal(loc=16, scale=1, size=20)
    boundaries = numpy.column_stack((start, end))
    title = "Employee Schedule"

.. code:: python

    import toyplot
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="td8a79f32de2f486286f2fb37d3dc94a5"><svg height="300.0px" id="tc0eb15faffdb4fd38227cdbc5f868696" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t9b2210a59e8b48878f4c6b1954f78cd2"><clipPath id="t7209292061c64aed8198b1d49d137f1f"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t7209292061c64aed8198b1d49d137f1f)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarBoundaries" id="t2634c12c457048aa8bf3175b7036b724" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="97.678913488510986" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="113.80008467423374" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="90.14285877392345" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="118.2145440939794" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="133.84987050060198" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="88.580423666484819" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="104.21287561873288" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="90.926617037695365" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="104.01593450275429" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="150.68872189008744" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="86.02832062773588" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="97.939888416950595" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="107.92339259707052" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="147.56257434430179" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="122.63726209990583" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="105.01053413958454" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="102.92346056264034" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="98.50817671215556" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="100.27355361155676" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="159.17154758256362" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee Schedule</title></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="ta9963f0372804f57a3c61203bdfc120e" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t6efa53c8b0bf4f65bd9044d1d981a2fa" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#td8a79f32de2f486286f2fb37d3dc94a5 text");
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
          var text = document.querySelectorAll("#td8a79f32de2f486286f2fb37d3dc94a5 text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "title": "Bar Data", "names": ["left", "right", "boundary1"], "id": "t2634c12c457048aa8bf3175b7036b724", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#td8a79f32de2f486286f2fb37d3dc94a5 .toyplot-mark-popup");
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
      var axes = {"t9b2210a59e8b48878f4c6b1954f78cd2": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


If your plot includes multiple series, you can assign a per-series title
instead. Hover the mouse over both series in the following plot to see
"Morning Schedule" and "Afternoon Schedule":

.. code:: python

    lunch = numpy.random.normal(loc=12, scale=0.5, size=20)
    boundaries = numpy.column_stack((start, lunch, end))
    title = ["Morning Schedule", "Afternoon Schedule"]
    
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t81374c312bd3428e8f4fcc84ba557f0f"><svg height="300.0px" id="t82ad331649ce4e738b05cab68eed4f3c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td465e71c354f4e58ad1a7da69e1889af"><clipPath id="t74b91c39a9f0468ebd660ac14845f82a"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t74b91c39a9f0468ebd660ac14845f82a)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarBoundaries" id="t2e54f8543be64f3989488a6564eaba94" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Morning Schedule</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Afternoon Schedule</title></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t1f3ed5b397aa4d10acb9c224ffa11272" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="tcda469bb1a00448cac179518d86e9f0d" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t81374c312bd3428e8f4fcc84ba557f0f text");
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
          var text = document.querySelectorAll("#t81374c312bd3428e8f4fcc84ba557f0f text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t2e54f8543be64f3989488a6564eaba94", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t81374c312bd3428e8f4fcc84ba557f0f .toyplot-mark-popup");
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
      var axes = {"td465e71c354f4e58ad1a7da69e1889af": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Finally, you can assign a title for every datum:

.. code:: python

    title = numpy.column_stack((
            ["Employee %s Morning" % i for i in range(20)],
            ["Employee %s Afternoon" % i for i in range(20)]
            ))
    
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t1fdbc4045fed4e1bafc3c898f1885c04"><svg height="300.0px" id="t0f5f77b4d10048adbf6ea46a3867e88a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t6dbc90ab14fd4c75be6f6a9fdd85a1ed"><clipPath id="t38f955fe3fd042398966d2a8d86c63aa"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t38f955fe3fd042398966d2a8d86c63aa)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarBoundaries" id="t943ffdb1a70c49bca06898df27bf6257" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tad4a20ef7e824f21a4d097f7da00a22f" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="ta73c1658824441feb2bcec0703e77614" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t1fdbc4045fed4e1bafc3c898f1885c04 text");
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
          var text = document.querySelectorAll("#t1fdbc4045fed4e1bafc3c898f1885c04 text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t943ffdb1a70c49bca06898df27bf6257", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t1fdbc4045fed4e1bafc3c898f1885c04 .toyplot-mark-popup");
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
      var axes = {"t6dbc90ab14fd4c75be6f6a9fdd85a1ed": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Of course, the title attribute works with all types of visualizations.

Coordinates
~~~~~~~~~~~

As you mouse over the above figures, you should also see the interactive
mouse coordinates in the upper-right-hand corner of the axes. These
coordinates show the domain values where the crosshair mouse cursor is
located.

If you wish to disable the mouse coordinates altogether, you can do so
using the axes:

.. code:: python

    canvas, axes, mark = toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300)
    axes.coordinates.show = False



.. raw:: html

    <div align="center" class="toyplot" id="t779e5022e0934c77bf1234f1dceb8f41"><svg height="300.0px" id="tb65f941cb6f548b69ab4ababd983e8f7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t156573ebdd9c4eb3a6144d3fe2eebdcc"><clipPath id="t2f74791d1bef4d64a89ea0ec3b558bdd"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2f74791d1bef4d64a89ea0ec3b558bdd)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarBoundaries" id="t0a906109099e483887c0feab847fb675" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-axes-Axis" id="ta7589059fc8146aaa041f3d12a932f89" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t195e5826c55b43c881ce62990d0f6de4" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t779e5022e0934c77bf1234f1dceb8f41 text");
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
          var text = document.querySelectorAll("#t779e5022e0934c77bf1234f1dceb8f41 text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t0a906109099e483887c0feab847fb675", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t779e5022e0934c77bf1234f1dceb8f41 .toyplot-mark-popup");
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
    </script></div></div>


Now when you mouse over the axes, the coordinates are no longer there.

Data Export
~~~~~~~~~~~

If you right-click the mouse over any of the above plots, a small popup
menu will appear, giving you the option to "Save as .csv". If you choose
that option, the raw data from the plot will be extracted in CSV format
and you can save it.

Note that different browsers, browser versions, and platforms will
behave differently when extracting the file:

-  Safari on OSX will open the file in a separate tab, which you can
   save to disk using ``File > Save As``.
-  Chrome on OSX will immediately open a file dialog, prompting you to
   save the file.
-  Firefox on OSX will prompt you to open the file with Microsoft Excel
   (if installed), or save it to disk.

Note that, on the browsers that support it, the default filename for the
saved data is ``toyplot.csv``. You can override this default on a
per-data-table basis by specifying the filename when you create your
figure. For example, when exporting data from the following figure
(again, for browsers that support setting a default filename), the
filename will default to ``employee-schedules.csv``:

.. code:: python

    canvas, axes, mark = toyplot.bars(boundaries, baseline=None, filename="employee-schedules", title=title, width=500, height=300)



.. raw:: html

    <div align="center" class="toyplot" id="t0b2f1e6a252e46e0b791085757381960"><svg height="300.0px" id="t7424be3a8f9f4edc860edf5f5a232838" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t23331aa1517744f5b22ae5a263205b5d"><clipPath id="t2311400e37024ab1bdedac48065caa16"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2311400e37024ab1bdedac48065caa16)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarBoundaries" id="t86b63367d5f04a929795be7178acb763" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t4b6177106eef4d249ae3943eb0b159f2" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0) rotate(0)" x="0" y="0">20</text></g></g><g class="toyplot-axes-Axis" id="t17a772f6dbfd4025b758e41f8e9b6edf" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0) rotate(0)" x="0" y="0">15</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">20</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t0b2f1e6a252e46e0b791085757381960 text");
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
          var text = document.querySelectorAll("#t0b2f1e6a252e46e0b791085757381960 text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t86b63367d5f04a929795be7178acb763", "filename": "employee-schedules"}];
    
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
          var popup = document.querySelector("#t0b2f1e6a252e46e0b791085757381960 .toyplot-mark-popup");
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
      var axes = {"t23331aa1517744f5b22ae5a263205b5d": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Note that the filename you specify should not include a file extension,
as the file extension is added for you (and other file formats may
become available in the future).
