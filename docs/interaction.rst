
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

    <div align="center" class="toyplot" id="taf06e0ef7fba44269896bca81721eb8f"><svg height="300.0px" id="tb3235857bc3e456db410dfc2842d6d93" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tcc3b66024a934c58a1769f8cd703da3c"><clipPath id="tacee380a959940b39a0ce5e705cca241"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tacee380a959940b39a0ce5e705cca241)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarBoundaries" id="tb012f6b3d7c04bfb8fa1c9f3f08ff1c7" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="97.678913488510986" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="113.80008467423374" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="90.14285877392345" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="118.2145440939794" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="133.84987050060198" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="88.580423666484819" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="104.21287561873288" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="90.926617037695365" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="104.01593450275429" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="150.68872189008744" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="86.02832062773588" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="97.939888416950595" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="107.92339259707052" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="147.56257434430179" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="122.63726209990583" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="105.01053413958454" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="102.92346056264034" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="98.50817671215556" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="100.27355361155676" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="159.17154758256362" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee Schedule</title></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tb95ad879c1bf473aa4de3d7fef4b60da" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tbe382e60b74e4f7b99944b97ce20e526" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "title": "Bar Data", "names": ["left", "right", "boundary1"], "id": "tb012f6b3d7c04bfb8fa1c9f3f08ff1c7", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#taf06e0ef7fba44269896bca81721eb8f .toyplot-mark-popup");
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
      var axes = {"tcc3b66024a934c58a1769f8cd703da3c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t861785f33b0845bdbfc5df5c5dc1af87"><svg height="300.0px" id="t146ca81a849b47ff96d12fdb1eade44d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tb6232f5c9a944a76bd2188fc277873e2"><clipPath id="t14292d8c027b496e86846605a29c90c0"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t14292d8c027b496e86846605a29c90c0)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarBoundaries" id="t497917a7171840aea777a01c8ef89300" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Morning Schedule</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Afternoon Schedule</title></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t3d3d8e066bba417c91fba6579700b9e1" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t23e2c40071f1445fa5f11b168fe7e09d" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t497917a7171840aea777a01c8ef89300", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t861785f33b0845bdbfc5df5c5dc1af87 .toyplot-mark-popup");
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
      var axes = {"tb6232f5c9a944a76bd2188fc277873e2": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t832d0ca539f441bda81a91c4a6f4d50f"><svg height="300.0px" id="ta06bc23a75914ef0887f3de3e6b02b3d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t2f5ce4f61e8c4876a2bc706ba4fe7f55"><clipPath id="t9b7a1c227a6c4e2799c69d963b617d03"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9b7a1c227a6c4e2799c69d963b617d03)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarBoundaries" id="te65f0c93de2d4e7c83924d991266b953" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t13c1c979877049f8b36c5b68680ff0bf" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tc00c8421b3764f958f039fe9e0137744" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "te65f0c93de2d4e7c83924d991266b953", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t832d0ca539f441bda81a91c4a6f4d50f .toyplot-mark-popup");
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
      var axes = {"t2f5ce4f61e8c4876a2bc706ba4fe7f55": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t58ecacc7e9a74eae9c50085f3cc56829"><svg height="300.0px" id="t34ed95346ae54598a0d72b8e75094b02" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td692e1eb3abf46dab23672137d74f123"><clipPath id="tb6bcff3d427b4112a8c9198aceebfe69"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb6bcff3d427b4112a8c9198aceebfe69)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarBoundaries" id="t4635f2062f084168ab9d74614930ea3a" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-axes-Axis" id="tf0ea8ec312c24b1ba232f2d185c70059" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="t7adfcb50b1244f04a37d4fcc39d3a7b2" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t4635f2062f084168ab9d74614930ea3a", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t58ecacc7e9a74eae9c50085f3cc56829 .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="td166d9c63a124b9aa5ccc6a0eaf57032"><svg height="300.0px" id="tf66af4c93b5348d3abf45ef936b34b1b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t6f0380b7269d4aae93c62cf0d02dc342"><clipPath id="t4051d5fa039746d7b3e4b3bba273cb2f"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t4051d5fa039746d7b3e4b3bba273cb2f)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="420.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-BarBoundaries" id="t7cf99b8755894807a31e9f3bc41a3d4f" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="te6f8f50c8f0b4a58b0ec5cbd6ae5e880" transform="translate(50.0,250.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-axes-Axis" id="tf6a2a7a1da704057ae8ad3ace99f6516" transform="translate(50.0,250.0) rotate(-90.0) translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0)translate(0,-8.0)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t7cf99b8755894807a31e9f3bc41a3d4f", "filename": "employee-schedules"}];
    
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
          var popup = document.querySelector("#td166d9c63a124b9aa5ccc6a0eaf57032 .toyplot-mark-popup");
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
      var axes = {"t6f0380b7269d4aae93c62cf0d02dc342": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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
