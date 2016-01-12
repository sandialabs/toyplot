
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _graph-visualization:

Graph Visualization
===================

Overview
--------

Toyplot now includes support for visualizing graphs - in the
mathematical sense of vertices connected by edges - using the
:meth:`toyplot.canvas.Canvas.graph` and :func:`toyplot.graph`
functions. As we will see, graph visualizations combine many of the
aspects and properties of line plots (for drawing the edges),
scatterplots (for drawing the vertices), and text (for drawing labels).

At a minimum, a graph can be specified as a collection of edges. For
example, consider a trivial social network:

.. code:: python

    sources = ["Tim", "Tim", "Fred", "Janet"]
    targets = ["Fred", "Janet", "Janet", "Pam"]

... here, we have specified a sequence of source (start) vertices and
target (end) vertices for each edge in the graph, which we can pass
directly to Toyplot for rendering:

.. code:: python

    import toyplot
    toyplot.graph(sources, targets, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="tc0ebd4c827334ef8aa6f1387a99ab82c"><svg height="300.0px" id="t3e223f349b55421691420364c9aa16ab" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc65fd05bb9664022921312503434ee93"><clipPath id="t9372e956bcf049d384eefe9dc77a28f8"><rect height="240.0" width="240.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9372e956bcf049d384eefe9dc77a28f8)" style="cursor:crosshair"><rect height="240.0" style="pointer-events:all;visibility:hidden" width="240.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t32acbdeac71f4c9e83886c5dbb46c9e3"><g class="toyplot-Edges"><path d="M 100.05418841 74.4927639832 L 50.0 139.983031773" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 100.05418841 74.4927639832 L 151.843314374 157.297286753" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 50.0 139.983031773 L 151.843314374 157.297286753" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 151.843314374 157.297286753 L 245.87745869 218.577192308" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="139.98303177344994" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="151.84331437387584" cy="157.29728675328977" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="245.87745869046307" cy="218.57719230842898" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.05418841029831" cy="74.492763983202948" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,139.98303177344994)"><tspan style="dominant-baseline:inherit">Fred</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(151.84331437387584,157.29728675328977)"><tspan style="dominant-baseline:inherit">Janet</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.87745869046307,218.57719230842898)"><tspan style="dominant-baseline:inherit">Pam</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.05418841029831,74.492763983202948)"><tspan style="dominant-baseline:inherit">Tim</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"tc65fd05bb9664022921312503434ee93": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.60806645552998795}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.90000000000000013, "min": -0.30000000000000004}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Simple as it is, Toyplot had to perform many steps to arrive at this
figure:

-  We specified a set of edges as input, and Toyplot *induced* a set of
   unique vertices from them.
-  Used a *layout algorithm* to calculate coordinates for each vertex.
-  Rendered the *vertices*.
-  Rendered a set of *vertex labels*.
-  Rendered an *edge* (line) between each pair of connected vertices.

We will examine each of these concepts in depth over the course of this
guide.

Inputs
------

At a minimum, you must specify the edges in a graph to create a
visualization. In the above example, we specified a sequence of edge
sources and a sequence of edge targets. We could also specify the edges
as a numpy matrix (2D array) containing a column of sources and a column
of targets:

.. code:: python

    import numpy
    edges = numpy.array([["Tim", "Fred"], ["Tim", "Janet"], ["Fred", "Janet"], ["Janet", "Pam"]])
    toyplot.graph(edges, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="ta3c068e0701b47b78160a0f32db03a54"><svg height="300.0px" id="t5ce8a711693b4fd9a93542c013e71acf" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tabf08ee494ac4f9180dc67160d7f3194"><clipPath id="t2ad63ecb91114ca2be7988f228326d78"><rect height="240.0" width="240.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t2ad63ecb91114ca2be7988f228326d78)" style="cursor:crosshair"><rect height="240.0" style="pointer-events:all;visibility:hidden" width="240.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="te4fc9ddf352d4549a472246c9c3f1657"><g class="toyplot-Edges"><path d="M 100.05418841 74.4927639832 L 50.0 139.983031773" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 100.05418841 74.4927639832 L 151.843314374 157.297286753" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 50.0 139.983031773 L 151.843314374 157.297286753" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 151.843314374 157.297286753 L 245.87745869 218.577192308" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="139.98303177344994" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="151.84331437387584" cy="157.29728675328977" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="245.87745869046307" cy="218.57719230842898" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.05418841029831" cy="74.492763983202948" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,139.98303177344994)"><tspan style="dominant-baseline:inherit">Fred</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(151.84331437387584,157.29728675328977)"><tspan style="dominant-baseline:inherit">Janet</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.87745869046307,218.57719230842898)"><tspan style="dominant-baseline:inherit">Pam</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.05418841029831,74.492763983202948)"><tspan style="dominant-baseline:inherit">Tim</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"tabf08ee494ac4f9180dc67160d7f3194": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.60806645552998795}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.90000000000000013, "min": -0.30000000000000004}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


In either case, Toyplot creates (*induces*) vertices using the edge
source / target values. Specifically, the source / target values are
used as *vertex identifiers*, with a vertex created for each unique
identifier. Note that vertex identifiers don't have to be strings, as in
the following example:

.. code:: python

    edges = numpy.array([[0, 1], [0, 2], [1, 2], [2, 3]])
    toyplot.graph(edges, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="t40acd3ff9fb04df6a9eca2d775798267"><svg height="300.0px" id="t558f0afddb2846ff85a6eea9e908a6eb" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td39b1230a0f54751a18d83c3e0387920"><clipPath id="tf9889301cca94d1585c1d0c9db05cdea"><rect height="240.0" width="240.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf9889301cca94d1585c1d0c9db05cdea)" style="cursor:crosshair"><rect height="240.0" style="pointer-events:all;visibility:hidden" width="240.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="tdaa1c0daa3034f9e8d821cf9ad00938e"><g class="toyplot-Edges"><path d="M 148.75186991 244.200479228 L 222.932811201 201.884905681" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 148.75186991 244.200479228 L 136.812576861 148.789569854" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 222.932811201 201.884905681 L 136.812576861 148.789569854" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 136.812576861 148.789569854 L 77.0671887993 58.3081774477" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="148.75186990991793" cy="244.20047922805043" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="222.93281120066445" cy="201.88490568070196" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="136.81257686053345" cy="148.78956985368015" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="77.067188799335554" cy="58.308177447718762" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(148.75186990991793,244.20047922805043)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(222.93281120066445,201.88490568070196)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(136.81257686053345,148.78956985368015)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(77.067188799335554,58.308177447718762)"><tspan style="dominant-baseline:inherit">3</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"td39b1230a0f54751a18d83c3e0387920": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.55600353574836558, "min": -0.55935027493362444}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.80000000000000016, "min": -0.40000000000000002}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Inducing vertices from edge data is sufficient for many problems, but
there may be occaisions when your graph contains disconnected vertices
without any edge connections. For this case, you may specify an optional
collection of extra vertex identifiers to add to your graph:

.. code:: python

    extra_vertices=[10]
    toyplot.graph(edges, extra_vertices, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="tfe14b7998fa64213af7c80ce595d2fbd"><svg height="300.0px" id="ta968d4b0c41a483da9fc601137829d0b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc56218850029481e9c4d9800f982637e"><clipPath id="t81848881faa94916bb72e77098c1a05a"><rect height="240.0" width="240.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t81848881faa94916bb72e77098c1a05a)" style="cursor:crosshair"><rect height="240.0" style="pointer-events:all;visibility:hidden" width="240.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="taf124d9fa552479aa4bf0b53ef9f476e"><g class="toyplot-Edges"><path d="M 93.7019082077 221.660534303 L 105.691261973 204.513821882" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 93.7019082077 221.660534303 L 80.6566425249 200.179955017" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 105.691261973 204.513821882 L 80.6566425249 200.179955017" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 80.6566425249 200.179955017 L 56.0368921333 186.388404621" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="93.701908207736096" cy="221.66053430268656" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.69126197336072" cy="204.5138218823418" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.656642524943436" cy="200.17995501714637" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="56.036892133326916" cy="186.38840462096147" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="250.0" cy="89.740360400960967" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(93.701908207736096,221.66053430268656)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(105.69126197336072,204.5138218823418)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(80.656642524943436,200.17995501714637)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(56.036892133326916,186.38840462096147)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,89.740360400960967)"><tspan style="dominant-baseline:inherit">10</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"tc56218850029481e9c4d9800f982637e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0285581576619944, "min": -1.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0, "min": -1.1431355639462386}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Layout Algorithms
-----------------

The next step in rendering a graph is using a layout algorithm to
determine the locations of the vertices and routing of edges. Graph
layout is an active area of research and there are many competing ideas
about what constitutes a good layout, so Toyplot provides a variety of
layouts to meet individual needs. By default, graphs are layed-out using
the classic force-directed layout of Fruchterman and Reingold:

.. code:: python

    import toyplot.generate
    edges = toyplot.generate.barabasi_albert_graph()
    toyplot.graph(edges, width=500);



.. raw:: html

    <div align="center" class="toyplot" id="ta7eeec00977f4db294cde453275f6acf"><svg height="500.0px" id="t127e6593f04f4ed58956ba8ebe7e50ed" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tdfe9fb82ffa94946a2e19c395a2b19fc"><clipPath id="t9f99c6030fc54ec6af910452880cbda3"><rect height="440.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t9f99c6030fc54ec6af910452880cbda3)" style="cursor:crosshair"><rect height="440.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t86344618b16143a2abcfaef658e8b95b"><g class="toyplot-Edges"><path d="M 241.638150317 214.291901612 L 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 241.638150317 214.291901612 L 307.447903718 85.0873950754" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 L 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 L 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 L 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 L 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 L 160.458531878 152.900994205" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 L 239.427275963 371.918950041" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 L 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 L 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 L 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 L 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 L 144.071386038 257.868465164" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 L 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 L 258.616170797 187.581056846" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 L 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 L 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 L 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 L 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 L 175.560688403 329.698141992" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 L 120.923836904 102.624383799" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 L 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 L 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="357.93052405031693" cy="289.61945398457124" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="307.44790371831124" cy="85.087395075373749" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="241.63815031716516" cy="214.29190161189223" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.96078567750556" cy="276.37753088528734" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="286.98421366377096" cy="295.24448394853442" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="144.34467256099879" cy="230.93857122749455" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="179.1281750526795" cy="278.67789935387736" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.4585318781954" cy="152.90099420475144" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="194.92330348555154" cy="234.91919194066242" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.92383690433017" cy="102.62438379907093" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="239.42727596275199" cy="371.91895004143959" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="238.06432820560855" cy="335.51847153568144" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.32191838574221" cy="215.44961632176887" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="199.99843098026366" cy="127.64175314813249" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="245.77483967815132" cy="450.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="288.07425895370818" cy="335.56963579272133" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="384.97626356638671" cy="350.39993914200875" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.02332764711673" cy="249.73598123157626" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.93134768774621" cy="131.09731869914589" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="258.61617079683487" cy="187.58105684578322" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="144.07138603825376" cy="257.86846516387607" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.60151231920814" cy="267.76081525720156" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="320.36813918234088" cy="137.06079688462381" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="116.14575907780782" cy="129.80948433423811" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="129.39283273278926" cy="174.31712729178778" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="175.56068840339933" cy="329.69814199231229" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="121.49012323785709" cy="375.81657515604132" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.307745003459615" cy="50.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="232.55960046680676" cy="80.278490134534138" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.96743352739719" cy="176.02975578907311" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(357.93052405031693,289.61945398457124)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(307.44790371831124,85.087395075373749)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(241.63815031716516,214.29190161189223)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(218.96078567750556,276.37753088528734)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(286.98421366377096,295.24448394853442)"><tspan style="dominant-baseline:inherit">4</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.34467256099879,230.93857122749455)"><tspan style="dominant-baseline:inherit">5</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(179.1281750526795,278.67789935387736)"><tspan style="dominant-baseline:inherit">6</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.4585318781954,152.90099420475144)"><tspan style="dominant-baseline:inherit">7</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(194.92330348555154,234.91919194066242)"><tspan style="dominant-baseline:inherit">8</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.92383690433017,102.62438379907093)"><tspan style="dominant-baseline:inherit">9</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(239.42727596275199,371.91895004143959)"><tspan style="dominant-baseline:inherit">10</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(238.06432820560855,335.51847153568144)"><tspan style="dominant-baseline:inherit">11</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(310.32191838574221,215.44961632176887)"><tspan style="dominant-baseline:inherit">12</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(199.99843098026366,127.64175314813249)"><tspan style="dominant-baseline:inherit">13</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.77483967815132,450.0)"><tspan style="dominant-baseline:inherit">14</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(288.07425895370818,335.56963579272133)"><tspan style="dominant-baseline:inherit">15</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(384.97626356638671,350.39993914200875)"><tspan style="dominant-baseline:inherit">16</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(341.02332764711673,249.73598123157626)"><tspan style="dominant-baseline:inherit">17</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(265.93134768774621,131.09731869914589)"><tspan style="dominant-baseline:inherit">18</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(258.61617079683487,187.58105684578322)"><tspan style="dominant-baseline:inherit">19</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.07138603825376,257.86846516387607)"><tspan style="dominant-baseline:inherit">20</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.60151231920814,267.76081525720156)"><tspan style="dominant-baseline:inherit">21</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(320.36813918234088,137.06079688462381)"><tspan style="dominant-baseline:inherit">22</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(116.14575907780782,129.80948433423811)"><tspan style="dominant-baseline:inherit">23</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(129.39283273278926,174.31712729178778)"><tspan style="dominant-baseline:inherit">24</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(175.56068840339933,329.69814199231229)"><tspan style="dominant-baseline:inherit">25</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(121.49012323785709,375.81657515604132)"><tspan style="dominant-baseline:inherit">26</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(61.307745003459615,50.0)"><tspan style="dominant-baseline:inherit">27</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(232.55960046680676,80.278490134534138)"><tspan style="dominant-baseline:inherit">28</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(315.96743352739719,176.02975578907311)"><tspan style="dominant-baseline:inherit">29</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"tdfe9fb82ffa94946a2e19c395a2b19fc": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -0.56107222851723615}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.607281613294538, "min": -0.74139805852485086}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 450.0}, "scale": "linear"}]}};
    
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


To explicitly specify the layout, use the :mod:`toyplot.layout`
module:

.. code:: python

    import toyplot.layout
    layout = toyplot.layout.FruchtermanReingold()
    toyplot.graph(edges, layout=layout, width=500);



.. raw:: html

    <div align="center" class="toyplot" id="td127ff0f085c489f9f71e7ba2120c798"><svg height="500.0px" id="t47fb5503af5c4c2b8f38a4cc3510e49a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t900703c7d44e4da192de45cb70615147"><clipPath id="t90d7a6be3cda4173b604a0bf79d08690"><rect height="440.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t90d7a6be3cda4173b604a0bf79d08690)" style="cursor:crosshair"><rect height="440.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t99cb3f3b706f401a9c71d8d5813781c9"><g class="toyplot-Edges"><path d="M 241.638150317 214.291901612 L 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 241.638150317 214.291901612 L 307.447903718 85.0873950754" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 L 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 L 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 L 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 L 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 L 160.458531878 152.900994205" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 L 239.427275963 371.918950041" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 L 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 L 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 L 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 L 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 L 144.071386038 257.868465164" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 L 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 L 258.616170797 187.581056846" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 L 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 L 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 L 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 L 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 L 175.560688403 329.698141992" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 L 120.923836904 102.624383799" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 L 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 L 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="357.93052405031693" cy="289.61945398457124" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="307.44790371831124" cy="85.087395075373749" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="241.63815031716516" cy="214.29190161189223" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.96078567750556" cy="276.37753088528734" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="286.98421366377096" cy="295.24448394853442" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="144.34467256099879" cy="230.93857122749455" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="179.1281750526795" cy="278.67789935387736" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.4585318781954" cy="152.90099420475144" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="194.92330348555154" cy="234.91919194066242" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.92383690433017" cy="102.62438379907093" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="239.42727596275199" cy="371.91895004143959" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="238.06432820560855" cy="335.51847153568144" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.32191838574221" cy="215.44961632176887" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="199.99843098026366" cy="127.64175314813249" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="245.77483967815132" cy="450.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="288.07425895370818" cy="335.56963579272133" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="384.97626356638671" cy="350.39993914200875" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.02332764711673" cy="249.73598123157626" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.93134768774621" cy="131.09731869914589" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="258.61617079683487" cy="187.58105684578322" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="144.07138603825376" cy="257.86846516387607" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.60151231920814" cy="267.76081525720156" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="320.36813918234088" cy="137.06079688462381" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="116.14575907780782" cy="129.80948433423811" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="129.39283273278926" cy="174.31712729178778" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="175.56068840339933" cy="329.69814199231229" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="121.49012323785709" cy="375.81657515604132" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.307745003459615" cy="50.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="232.55960046680676" cy="80.278490134534138" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.96743352739719" cy="176.02975578907311" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(357.93052405031693,289.61945398457124)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(307.44790371831124,85.087395075373749)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(241.63815031716516,214.29190161189223)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(218.96078567750556,276.37753088528734)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(286.98421366377096,295.24448394853442)"><tspan style="dominant-baseline:inherit">4</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.34467256099879,230.93857122749455)"><tspan style="dominant-baseline:inherit">5</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(179.1281750526795,278.67789935387736)"><tspan style="dominant-baseline:inherit">6</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.4585318781954,152.90099420475144)"><tspan style="dominant-baseline:inherit">7</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(194.92330348555154,234.91919194066242)"><tspan style="dominant-baseline:inherit">8</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.92383690433017,102.62438379907093)"><tspan style="dominant-baseline:inherit">9</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(239.42727596275199,371.91895004143959)"><tspan style="dominant-baseline:inherit">10</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(238.06432820560855,335.51847153568144)"><tspan style="dominant-baseline:inherit">11</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(310.32191838574221,215.44961632176887)"><tspan style="dominant-baseline:inherit">12</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(199.99843098026366,127.64175314813249)"><tspan style="dominant-baseline:inherit">13</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.77483967815132,450.0)"><tspan style="dominant-baseline:inherit">14</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(288.07425895370818,335.56963579272133)"><tspan style="dominant-baseline:inherit">15</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(384.97626356638671,350.39993914200875)"><tspan style="dominant-baseline:inherit">16</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(341.02332764711673,249.73598123157626)"><tspan style="dominant-baseline:inherit">17</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(265.93134768774621,131.09731869914589)"><tspan style="dominant-baseline:inherit">18</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(258.61617079683487,187.58105684578322)"><tspan style="dominant-baseline:inherit">19</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.07138603825376,257.86846516387607)"><tspan style="dominant-baseline:inherit">20</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.60151231920814,267.76081525720156)"><tspan style="dominant-baseline:inherit">21</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(320.36813918234088,137.06079688462381)"><tspan style="dominant-baseline:inherit">22</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(116.14575907780782,129.80948433423811)"><tspan style="dominant-baseline:inherit">23</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(129.39283273278926,174.31712729178778)"><tspan style="dominant-baseline:inherit">24</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(175.56068840339933,329.69814199231229)"><tspan style="dominant-baseline:inherit">25</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(121.49012323785709,375.81657515604132)"><tspan style="dominant-baseline:inherit">26</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(61.307745003459615,50.0)"><tspan style="dominant-baseline:inherit">27</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(232.55960046680676,80.278490134534138)"><tspan style="dominant-baseline:inherit">28</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(315.96743352739719,176.02975578907311)"><tspan style="dominant-baseline:inherit">29</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"t900703c7d44e4da192de45cb70615147": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -0.56107222851723615}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.607281613294538, "min": -0.74139805852485086}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 450.0}, "scale": "linear"}]}};
    
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


Note that by default most layouts produce straight-line edges, but this
can be overridden by supplying an alternate edge-layout algorithm:

.. code:: python

    layout = toyplot.layout.FruchtermanReingold(edges=toyplot.layout.CurvedEdges())
    toyplot.graph(edges, layout=layout, width=500);



.. raw:: html

    <div align="center" class="toyplot" id="te715b01e7d21429bb1e1c474b9a700df"><svg height="500.0px" id="tea421dde244b419c9fa5c16d697ec3ec" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t1692c9d5acec4311a4b7d153be113be4"><clipPath id="td56c191a87ba4814817e65ba49cd6ea9"><rect height="440.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td56c191a87ba4814817e65ba49cd6ea9)" style="cursor:crosshair"><rect height="440.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t93ffcf71e0ce445f93780ecc8b93d8c3"><g class="toyplot-Edges"><path d="M 241.638150317 214.291901612 Q 309.546160188 231.764731184 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 241.638150317 214.291901612 Q 257.799199767 138.263609172 307.447903718 85.0873950754" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 Q 222.253687868 241.397420585 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 Q 222.253687868 241.397420585 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 Q 250.527499792 297.621389808 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 Q 253.820401982 262.641279508 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 Q 190.834141791 205.722921367 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 Q 187.541239601 240.703031667 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 Q 202.039273973 235.631776302 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 Q 155.549804743 260.847426162 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 Q 162.514621833 194.717507647 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 Q 209.004091063 169.501857786 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 Q 248.771413665 249.098013185 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 Q 215.607601983 216.494808744 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 Q 175.067874779 155.923832056 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 Q 147.206614092 120.898585278 160.458531878 152.900994205" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 Q 199.421262836 311.145951986 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 Q 253.269373016 325.32477323 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 Q 203.456987609 292.709074641 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 Q 224.141286107 274.284691445 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 Q 275.830004173 226.795791106 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 Q 275.830004173 226.795791106 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 Q 232.047427744 163.737244535 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 Q 232.047427744 163.737244535 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 Q 232.482404477 412.06155348 239.427275963 371.918950041" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 Q 227.083731947 394.097952319 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 Q 249.139621019 282.993111574 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 Q 263.062663118 344.226891666 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 Q 328.83255129 339.835814284 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 Q 363.576749479 324.705439415 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 Q 286.737481656 249.269422115 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 Q 319.901293338 281.872626555 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 Q 264.566073601 176.912450375 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 Q 264.566073601 176.912450375 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 Q 253.588663429 203.884241787 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 Q 230.677564509 246.930364839 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 Q 187.20760871 219.140419707 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 Q 187.20760871 219.140419707 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 Q 101.05448305 248.322410754 144.071386038 257.868465164" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 Q 97.701236492 234.810015158 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 Q 296.039159643 173.042444167 258.616170797 187.581056846" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 Q 291.011652275 189.345629108 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 Q 157.791175133 114.166926993 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 Q 169.155873399 168.686801576 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 Q 190.695889125 174.816226937 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 Q 117.001476307 154.363292892 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 Q 190.350830217 295.502612769 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 Q 193.643732408 260.522502469 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 Q 137.720786319 317.239987512 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 Q 142.548841236 343.369503983 175.560688403 329.698141992" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 Q 97.9354725204 65.9615103348 120.923836904 102.624383799" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 Q 99.0693960747 80.3836413497 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 Q 222.416899883 109.613465998 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 Q 254.465896646 145.708957385 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 Q 283.761247143 208.066048028 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 Q 283.761247143 208.066048028 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="357.93052405031693" cy="289.61945398457124" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="307.44790371831124" cy="85.087395075373749" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="241.63815031716516" cy="214.29190161189223" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.96078567750556" cy="276.37753088528734" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="286.98421366377096" cy="295.24448394853442" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="144.34467256099879" cy="230.93857122749455" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="179.1281750526795" cy="278.67789935387736" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.4585318781954" cy="152.90099420475144" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="194.92330348555154" cy="234.91919194066242" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.92383690433017" cy="102.62438379907093" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="239.42727596275199" cy="371.91895004143959" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="238.06432820560855" cy="335.51847153568144" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.32191838574221" cy="215.44961632176887" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="199.99843098026366" cy="127.64175314813249" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="245.77483967815132" cy="450.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="288.07425895370818" cy="335.56963579272133" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="384.97626356638671" cy="350.39993914200875" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.02332764711673" cy="249.73598123157626" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.93134768774621" cy="131.09731869914589" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="258.61617079683487" cy="187.58105684578322" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="144.07138603825376" cy="257.86846516387607" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.60151231920814" cy="267.76081525720156" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="320.36813918234088" cy="137.06079688462381" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="116.14575907780782" cy="129.80948433423811" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="129.39283273278926" cy="174.31712729178778" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="175.56068840339933" cy="329.69814199231229" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="121.49012323785709" cy="375.81657515604132" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.307745003459615" cy="50.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="232.55960046680676" cy="80.278490134534138" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.96743352739719" cy="176.02975578907311" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(357.93052405031693,289.61945398457124)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(307.44790371831124,85.087395075373749)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(241.63815031716516,214.29190161189223)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(218.96078567750556,276.37753088528734)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(286.98421366377096,295.24448394853442)"><tspan style="dominant-baseline:inherit">4</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.34467256099879,230.93857122749455)"><tspan style="dominant-baseline:inherit">5</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(179.1281750526795,278.67789935387736)"><tspan style="dominant-baseline:inherit">6</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.4585318781954,152.90099420475144)"><tspan style="dominant-baseline:inherit">7</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(194.92330348555154,234.91919194066242)"><tspan style="dominant-baseline:inherit">8</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.92383690433017,102.62438379907093)"><tspan style="dominant-baseline:inherit">9</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(239.42727596275199,371.91895004143959)"><tspan style="dominant-baseline:inherit">10</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(238.06432820560855,335.51847153568144)"><tspan style="dominant-baseline:inherit">11</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(310.32191838574221,215.44961632176887)"><tspan style="dominant-baseline:inherit">12</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(199.99843098026366,127.64175314813249)"><tspan style="dominant-baseline:inherit">13</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.77483967815132,450.0)"><tspan style="dominant-baseline:inherit">14</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(288.07425895370818,335.56963579272133)"><tspan style="dominant-baseline:inherit">15</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(384.97626356638671,350.39993914200875)"><tspan style="dominant-baseline:inherit">16</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(341.02332764711673,249.73598123157626)"><tspan style="dominant-baseline:inherit">17</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(265.93134768774621,131.09731869914589)"><tspan style="dominant-baseline:inherit">18</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(258.61617079683487,187.58105684578322)"><tspan style="dominant-baseline:inherit">19</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.07138603825376,257.86846516387607)"><tspan style="dominant-baseline:inherit">20</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.60151231920814,267.76081525720156)"><tspan style="dominant-baseline:inherit">21</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(320.36813918234088,137.06079688462381)"><tspan style="dominant-baseline:inherit">22</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(116.14575907780782,129.80948433423811)"><tspan style="dominant-baseline:inherit">23</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(129.39283273278926,174.31712729178778)"><tspan style="dominant-baseline:inherit">24</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(175.56068840339933,329.69814199231229)"><tspan style="dominant-baseline:inherit">25</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(121.49012323785709,375.81657515604132)"><tspan style="dominant-baseline:inherit">26</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(61.307745003459615,50.0)"><tspan style="dominant-baseline:inherit">27</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(232.55960046680676,80.278490134534138)"><tspan style="dominant-baseline:inherit">28</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(315.96743352739719,176.02975578907311)"><tspan style="dominant-baseline:inherit">29</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"t1692c9d5acec4311a4b7d153be113be4": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -0.56107222851723615}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.607281613294538, "min": -0.74139805852485086}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 450.0}, "scale": "linear"}]}};
    
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


If your graph is a *tree*, there are also tree-specific layouts to
choose from:

.. code:: python

    numpy.random.seed(1234)
    edges = toyplot.generate.prufer_tree(numpy.random.choice(4, 12))
    layout = toyplot.layout.Buchheim()
    toyplot.graph(edges, layout=layout, width=500, height=200);



.. raw:: html

    <div align="center" class="toyplot" id="t75b55a9df2dd4cff9bb34b4b8088ca16"><svg height="200.0px" id="t7b5b7ed07d0c4d2a9963b5e2aef2d5a8" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 200.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tb02d7d89840e4cb89cde0761b5eb3a49"><clipPath id="t3710e5df43a24d279c9d9bf77d4cf1c0"><rect height="140.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t3710e5df43a24d279c9d9bf77d4cf1c0)" style="cursor:crosshair"><rect height="140.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t7fbc2ea4381e45f2b3803064313a8765"><g class="toyplot-Edges"><path d="M 363.043478261 100.0 L 310.869565217 134.782608696" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 363.043478261 100.0 L 345.652173913 134.782608696" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 50.0 100.0 L 50.0 134.782608696" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.0 65.2173913043 L 50.0 100.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 154.347826087 100.0 L 119.565217391 134.782608696" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 154.347826087 100.0 L 154.347826087 134.782608696" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 154.347826087 100.0 L 189.130434783 134.782608696" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.0 65.2173913043 L 154.347826087 100.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 363.043478261 100.0 L 380.434782609 134.782608696" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.0 65.2173913043 L 250.0 100.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 363.043478261 100.0 L 415.217391304 134.782608696" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.0 65.2173913043 L 363.043478261 100.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.0 65.2173913043 L 450.0 100.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="154.3478260869565" cy="100.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="250.0" cy="65.217391304347828" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="100.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="363.04347826086956" cy="100.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.86956521739131" cy="134.78260869565219" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="345.65217391304344" cy="134.78260869565219" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="134.78260869565219" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="119.56521739130434" cy="134.78260869565219" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="154.3478260869565" cy="134.78260869565219" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="189.13043478260869" cy="134.78260869565219" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="380.43478260869568" cy="134.78260869565219" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="250.0" cy="100.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="415.21739130434776" cy="134.78260869565219" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="100.0" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(154.3478260869565,100.0)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,65.217391304347828)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,100.0)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(363.04347826086956,100.0)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(310.86956521739131,134.78260869565219)"><tspan style="dominant-baseline:inherit">4</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(345.65217391304344,134.78260869565219)"><tspan style="dominant-baseline:inherit">5</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,134.78260869565219)"><tspan style="dominant-baseline:inherit">6</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(119.56521739130434,134.78260869565219)"><tspan style="dominant-baseline:inherit">7</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(154.3478260869565,134.78260869565219)"><tspan style="dominant-baseline:inherit">8</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(189.13043478260869,134.78260869565219)"><tspan style="dominant-baseline:inherit">9</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(380.43478260869568,134.78260869565219)"><tspan style="dominant-baseline:inherit">10</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,100.0)"><tspan style="dominant-baseline:inherit">11</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(415.21739130434776,134.78260869565219)"><tspan style="dominant-baseline:inherit">12</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(450.0,100.0)"><tspan style="dominant-baseline:inherit">13</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"tb02d7d89840e4cb89cde0761b5eb3a49": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 5.75, "min": -5.75}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.4375, "min": -2.4375}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 150.0}, "scale": "linear"}]}};
    
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


When computing a layout, Toyplot doesn't have to compute the coordinates
for every vertex ... you can explicitly specify some or all of the
coordinates yourself. To do so, you can pass a matrix containing X and Y
coordinates for the vertices you want to control, that is masked
everywhere. Suppose we rendered our tree with the default force directed
layout:

.. code:: python

    toyplot.graph(edges, width=500);



.. raw:: html

    <div align="center" class="toyplot" id="tdfe236559e56442681abf748ed29c6f3"><svg height="500.0px" id="td83976311e9441258169087d4b660a85" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tba38401399cb40f8a05891cc7b554c1b"><clipPath id="tf0fd7ea77a51409f8621f2d9d1745205"><rect height="440.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf0fd7ea77a51409f8621f2d9d1745205)" style="cursor:crosshair"><rect height="440.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="tc7a8cba311034dfdb79def7f895fd009"><g class="toyplot-Edges"><path d="M 212.989824851 122.095325547 L 242.175277852 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 212.989824851 122.095325547 L 147.327040719 90.1252303481" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 299.703905632 263.884406472 L 370.941013351 276.443631658" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.584889652 248.57881015 L 299.703905632 263.884406472" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 191.254021979 367.292268811 L 129.686439009 408.899221032" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 191.254021979 367.292268811 L 179.547501952 442.798262908" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 191.254021979 367.292268811 L 237.326088756 422.891476261" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.584889652 248.57881015 L 191.254021979 367.292268811" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 212.989824851 122.095325547 L 186.817405218 50.5312712524" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.584889652 248.57881015 L 153.411500782 278.251914861" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 212.989824851 122.095325547 L 279.00535555 93.2506777738" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.584889652 248.57881015 L 212.989824851 122.095325547" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.584889652 248.57881015 L 149.12644901 222.081467898" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="191.25402197937558" cy="367.29226881073197" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="209.58488965157997" cy="248.57881014969223" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="299.70390563237885" cy="263.88440647176407" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="212.98982485142017" cy="122.09532554692672" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="242.17527785163463" cy="50.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="147.32704071921609" cy="90.125230348076045" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="370.94101335136196" cy="276.44363165784188" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="129.68643900922018" cy="408.89922103231294" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="179.54750195190888" cy="442.79826290811684" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="237.32608875615782" cy="422.89147626115852" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="186.81740521844029" cy="50.531271252380265" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="153.41150078152771" cy="278.25191486111942" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="279.00535554976119" cy="93.250677773770661" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="149.12644900951221" cy="222.08146789781793" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(191.25402197937558,367.29226881073197)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(209.58488965157997,248.57881014969223)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(299.70390563237885,263.88440647176407)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(212.98982485142017,122.09532554692672)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(242.17527785163463,50.0)"><tspan style="dominant-baseline:inherit">4</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(147.32704071921609,90.125230348076045)"><tspan style="dominant-baseline:inherit">5</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(370.94101335136196,276.44363165784188)"><tspan style="dominant-baseline:inherit">6</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(129.68643900922018,408.89922103231294)"><tspan style="dominant-baseline:inherit">7</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(179.54750195190888,442.79826290811684)"><tspan style="dominant-baseline:inherit">8</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(237.32608875615782,422.89147626115852)"><tspan style="dominant-baseline:inherit">9</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(186.81740521844029,50.531271252380265)"><tspan style="dominant-baseline:inherit">10</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(153.41150078152771,278.25191486111942)"><tspan style="dominant-baseline:inherit">11</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(279.00535554976119,93.250677773770661)"><tspan style="dominant-baseline:inherit">12</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(149.12644900951221,222.08146789781793)"><tspan style="dominant-baseline:inherit">13</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"tba38401399cb40f8a05891cc7b554c1b": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.3336607301180976, "min": -1.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.3727193297984146, "min": -1.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 450.0}, "scale": "linear"}]}};
    
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


... but we want to force vertices 0, 1, and 3 to lie on the X axis:

.. code:: python

    vcoordinates = numpy.ma.masked_all((14, 2)) # We know in advance there are 14 vertices
    vcoordinates[0] = (-1, 0)
    vcoordinates[1] = (0, 0)
    vcoordinates[3] = (1, 0)
    
    toyplot.graph(edges, vcoordinates=vcoordinates, width=500);



.. raw:: html

    <div align="center" class="toyplot" id="t3f0a24391d6c4b09a3b63df6a7f5bf04"><svg height="500.0px" id="t0afe8b2d32cf4cf19dc6152bcc26f227" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tba854305f93f4c1e8f323718d8c6b2f7"><clipPath id="tbe2378eeff294a3faf73b08f4dffc600"><rect height="440.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tbe2378eeff294a3faf73b08f4dffc600)" style="cursor:crosshair"><rect height="440.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t90e3ac7644c74080bee9f9c59fec698a"><g class="toyplot-Edges"><path d="M 390.65393643 197.974555392 L 447.134667341 173.795973568" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 390.65393643 197.974555392 L 413.309839497 244.486649351" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 247.225888154 260.689322709 L 244.584355251 311.689880552" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.93021098 197.974555392 L 247.225888154 260.689322709" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 111.20648553 197.974555392 L 50.0 195.047405158" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 111.20648553 197.974555392 L 72.2893895183 236.217116868" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 111.20648553 197.974555392 L 76.6371330858 156.054567401" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.93021098 197.974555392 L 111.20648553 197.974555392" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 390.65393643 197.974555392 L 407.407892719 149.058365741" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.93021098 197.974555392 L 216.542682765 165.892695431" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 390.65393643 197.974555392 L 450.0 215.948763441" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.93021098 197.974555392 L 390.65393643 197.974555392" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.93021098 197.974555392 L 267.476331694 152.974909145" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.20648552990062" cy="197.97455539213809" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="250.93021097992201" cy="197.97455539213809" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="247.22588815437075" cy="260.68932270873222" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="390.65393642994349" cy="197.97455539213809" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="447.13466734134477" cy="173.79597356764722" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="413.30983949707002" cy="244.48664935052108" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="244.58435525059298" cy="311.68988055155029" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="195.04740515768094" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="72.289389518258716" cy="236.21711686807151" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="76.63713308582382" cy="156.05456740135341" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="407.40789271881823" cy="149.05836574111012" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="216.54268276465334" cy="165.89269543103484" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="215.94876344088328" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="267.47633169374001" cy="152.97490914460931" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(111.20648552990062,197.97455539213809)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.93021097992201,197.97455539213809)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(247.22588815437075,260.68932270873222)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(390.65393642994349,197.97455539213809)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(447.13466734134477,173.79597356764722)"><tspan style="dominant-baseline:inherit">4</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(413.30983949707002,244.48664935052108)"><tspan style="dominant-baseline:inherit">5</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(244.58435525059298,311.68988055155029)"><tspan style="dominant-baseline:inherit">6</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,195.04740515768094)"><tspan style="dominant-baseline:inherit">7</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(72.289389518258716,236.21711686807151)"><tspan style="dominant-baseline:inherit">8</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(76.63713308582382,156.05456740135341)"><tspan style="dominant-baseline:inherit">9</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(407.40789271881823,149.05836574111012)"><tspan style="dominant-baseline:inherit">10</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(216.54268276465334,165.89269543103484)"><tspan style="dominant-baseline:inherit">11</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(450.0,215.94876344088328)"><tspan style="dominant-baseline:inherit">12</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(267.47633169374001,152.97490914460931)"><tspan style="dominant-baseline:inherit">13</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"tba854305f93f4c1e8f323718d8c6b2f7": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.4247386288829265, "min": -1.4380536328584648}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.1742826651680232, "min": -2.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 450.0}, "scale": "linear"}]}};
    
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


Note that we've "pinned" our three vertices of interest, and the layout
algorithm has placed the other vertices around them as normal. This is
particularly useful when there are vertices of special significance that
we wish to place explicitly, either to steer the layout, or to work with
a narrative flow.

Keep in mind that we aren't limited to explicitly constraining both
coordinates for a vertex. For example, if we had some other per-vertex
variable that we wanted to use for the visualization, we might map it to
the X axis:

.. code:: python

    numpy.random.seed(1234)
    data = numpy.random.uniform(0, 1, size=14)
    
    vcoordinates = numpy.ma.masked_all((14, 2))
    vcoordinates[:,0] = data
    
    canvas, axes, mark = toyplot.graph(edges, vcoordinates=vcoordinates, width=500)
    axes.show = True
    axes.aspect = None
    axes.y.show = False



.. raw:: html

    <div align="center" class="toyplot" id="tbe260b22c7bf49e580ba22ba7ae8a1cf"><svg height="500.0px" id="t1d6e7e79c3f44474ab1d1e162ff5592a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t8aa1f5a2cc344ec4b272beece3bfb431"><clipPath id="tae822774184f46d2b217149dcd995576"><rect height="440.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tae822774184f46d2b217149dcd995576)" style="cursor:crosshair"><rect height="440.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t251458d689494022a46d183760a8f9d9"><g class="toyplot-Edges"><path d="M 343.805031482 144.754580316 L 341.141874973 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 343.805031482 144.754580316 L 90.1113693789 159.050124913" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 171.812844474 218.975395688 L 92.0268884905 130.109318536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 263.036328883 273.477353361 L 171.812844474 218.975395688" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 50.0 387.936853036 L 351.975218794 450.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 50.0 387.936853036 L 429.289225283 430.556908344" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 50.0 387.936853036 L 388.61701914 388.968932598" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 263.036328883 273.477353361 L 50.0 387.936853036" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 343.805031482 144.754580316 L 132.276720031 65.672006215" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 263.036328883 273.477353361 L 203.114716385 341.822526034" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 343.805031482 144.754580316 L 293.391623966 215.998957656" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 263.036328883 273.477353361 L 343.805031482 144.754580316" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 263.036328883 273.477353361 L 307.857818273 192.721197594" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="387.93685303560619" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="263.03632888273398" cy="273.47735336083963" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="171.81284447404806" cy="218.97539568758143" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="343.8050314819215" cy="144.75458031561445" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.14187497309103" cy="50.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.11136937888935" cy="159.05012491335535" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="92.026888490521429" cy="130.10931853634028" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="351.9752187939053" cy="450.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="429.28922528270459" cy="430.5569083438113" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="388.61701913989191" cy="388.96893259841409" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="132.27672003088233" cy="65.672006215003265" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="203.11471638475479" cy="341.82252603354732" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="293.39162396611374" cy="215.99895765568829" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="307.85781827318357" cy="192.72119759408625" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,387.93685303560619)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(263.03632888273398,273.47735336083963)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(171.81284447404806,218.97539568758143)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(343.8050314819215,144.75458031561445)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(341.14187497309103,50.0)"><tspan style="dominant-baseline:inherit">4</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(90.11136937888935,159.05012491335535)"><tspan style="dominant-baseline:inherit">5</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(92.026888490521429,130.10931853634028)"><tspan style="dominant-baseline:inherit">6</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(351.9752187939053,450.0)"><tspan style="dominant-baseline:inherit">7</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(429.28922528270459,430.5569083438113)"><tspan style="dominant-baseline:inherit">8</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(388.61701913989191,388.96893259841409)"><tspan style="dominant-baseline:inherit">9</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(132.27672003088233,65.672006215003265)"><tspan style="dominant-baseline:inherit">10</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(203.11471638475479,341.82252603354732)"><tspan style="dominant-baseline:inherit">11</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(293.39162396611374,215.99895765568829)"><tspan style="dominant-baseline:inherit">12</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(307.85781827318357,192.72119759408625)"><tspan style="dominant-baseline:inherit">13</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t45e1fd0208534ea0bdf7f852cc0fc6aa" transform="translate(50.0,450.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="379.2892252827046" y1="0" y2="0"></line><g><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(28.933559204863723,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.2</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(152.62237280324248,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(276.3111864016212,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">0.8</tspan></text><text style="dominant-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0)translate(0,8.0)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"t8aa1f5a2cc344ec4b272beece3bfb431": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.19151945037889229}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.355279491966392, "min": -0.60169071581926181}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 450.0}, "scale": "linear"}]}};
    
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


Now, the X coordinate of every vertex is constrained, while the
force-directed layout places just the Y coordinates.


Vertex Rendering
----------------

As you might expect, you can treat graph vertices as a single series of
markers for rendering purposes. For example, you could specify a custom
vertex color, marker, size, and label style:

.. code:: python

    edges = toyplot.generate.barabasi_albert_graph()
    layout = toyplot.layout.FruchtermanReingold(edges=toyplot.layout.CurvedEdges())
    vlstyle = {"fill":"white"}
    
    toyplot.graph(edges, layout=layout, vcolor="steelblue", vmarker="d", vsize=18, vlstyle=vlstyle, width=500);



.. raw:: html

    <div align="center" class="toyplot" id="t929698b9fc9a4f39896c66464764c6d5"><svg height="500.0px" id="t0538e09331cf4ee0b49469d144c0717c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="ta2de48b73860466d8cde3ba4950304fb"><clipPath id="te8a5df6eb2c74735816844b9185b96ce"><rect height="440.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te8a5df6eb2c74735816844b9185b96ce)" style="cursor:crosshair"><rect height="440.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t0172ed69b9644f16af795f0342e84432"><g class="toyplot-Edges"><path d="M 241.638150317 214.291901612 Q 309.546160188 231.764731184 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 241.638150317 214.291901612 Q 257.799199767 138.263609172 307.447903718 85.0873950754" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 Q 222.253687868 241.397420585 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 Q 222.253687868 241.397420585 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 Q 250.527499792 297.621389808 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 Q 253.820401982 262.641279508 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 Q 190.834141791 205.722921367 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 Q 187.541239601 240.703031667 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 Q 202.039273973 235.631776302 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 Q 155.549804743 260.847426162 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 Q 162.514621833 194.717507647 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 Q 209.004091063 169.501857786 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 Q 248.771413665 249.098013185 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 Q 215.607601983 216.494808744 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 Q 175.067874779 155.923832056 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 Q 147.206614092 120.898585278 160.458531878 152.900994205" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 Q 199.421262836 311.145951986 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 Q 253.269373016 325.32477323 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 Q 203.456987609 292.709074641 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 Q 224.141286107 274.284691445 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 Q 275.830004173 226.795791106 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 Q 275.830004173 226.795791106 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 Q 232.047427744 163.737244535 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 Q 232.047427744 163.737244535 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 Q 232.482404477 412.06155348 239.427275963 371.918950041" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 Q 227.083731947 394.097952319 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 Q 249.139621019 282.993111574 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 Q 263.062663118 344.226891666 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 Q 328.83255129 339.835814284 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 Q 363.576749479 324.705439415 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 Q 286.737481656 249.269422115 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 Q 319.901293338 281.872626555 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 Q 264.566073601 176.912450375 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 Q 264.566073601 176.912450375 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 Q 253.588663429 203.884241787 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 Q 230.677564509 246.930364839 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 Q 187.20760871 219.140419707 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 Q 187.20760871 219.140419707 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 Q 101.05448305 248.322410754 144.071386038 257.868465164" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 Q 97.701236492 234.810015158 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 Q 296.039159643 173.042444167 258.616170797 187.581056846" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 Q 291.011652275 189.345629108 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 Q 157.791175133 114.166926993 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 Q 169.155873399 168.686801576 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 Q 190.695889125 174.816226937 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 Q 117.001476307 154.363292892 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 Q 190.350830217 295.502612769 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 Q 193.643732408 260.522502469 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 Q 137.720786319 317.239987512 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 Q 142.548841236 343.369503983 175.560688403 329.698141992" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 Q 97.9354725204 65.9615103348 120.923836904 102.624383799" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 Q 99.0693960747 80.3836413497 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 Q 222.416899883 109.613465998 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 Q 254.465896646 145.708957385 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 Q 283.761247143 208.066048028 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 Q 283.761247143 208.066048028 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 357.93052405031693, 289.61945398457124)" width="18.0" x="348.93052405031693" y="280.61945398457124"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 307.44790371831124, 85.087395075373749)" width="18.0" x="298.44790371831124" y="76.087395075373749"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 241.63815031716516, 214.29190161189223)" width="18.0" x="232.63815031716516" y="205.29190161189223"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 218.96078567750556, 276.37753088528734)" width="18.0" x="209.96078567750556" y="267.37753088528734"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 286.98421366377096, 295.24448394853442)" width="18.0" x="277.98421366377096" y="286.24448394853442"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 144.34467256099879, 230.93857122749455)" width="18.0" x="135.34467256099879" y="221.93857122749455"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 179.1281750526795, 278.67789935387736)" width="18.0" x="170.1281750526795" y="269.67789935387736"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 160.4585318781954, 152.90099420475144)" width="18.0" x="151.4585318781954" y="143.90099420475144"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 194.92330348555154, 234.91919194066242)" width="18.0" x="185.92330348555154" y="225.91919194066242"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 120.92383690433017, 102.62438379907093)" width="18.0" x="111.92383690433017" y="93.624383799070927"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 239.42727596275199, 371.91895004143959)" width="18.0" x="230.42727596275199" y="362.91895004143959"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 238.06432820560855, 335.51847153568144)" width="18.0" x="229.06432820560855" y="326.51847153568144"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 310.32191838574221, 215.44961632176887)" width="18.0" x="301.32191838574221" y="206.44961632176887"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 199.99843098026366, 127.64175314813249)" width="18.0" x="190.99843098026366" y="118.64175314813249"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 245.77483967815132, 450.0)" width="18.0" x="236.77483967815132" y="441.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 288.07425895370818, 335.56963579272133)" width="18.0" x="279.07425895370818" y="326.56963579272133"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 384.97626356638671, 350.39993914200875)" width="18.0" x="375.97626356638671" y="341.39993914200875"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 341.02332764711673, 249.73598123157626)" width="18.0" x="332.02332764711673" y="240.73598123157626"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 265.93134768774621, 131.09731869914589)" width="18.0" x="256.93134768774621" y="122.09731869914589"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 258.61617079683487, 187.58105684578322)" width="18.0" x="249.61617079683487" y="178.58105684578322"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 144.07138603825376, 257.86846516387607)" width="18.0" x="135.07138603825376" y="248.86846516387607"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 60.60151231920814, 267.76081525720156)" width="18.0" x="51.60151231920814" y="258.76081525720156"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 320.36813918234088, 137.06079688462381)" width="18.0" x="311.36813918234088" y="128.06079688462381"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 116.14575907780782, 129.80948433423811)" width="18.0" x="107.14575907780782" y="120.80948433423811"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 129.39283273278926, 174.31712729178778)" width="18.0" x="120.39283273278926" y="165.31712729178778"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 175.56068840339933, 329.69814199231229)" width="18.0" x="166.56068840339933" y="320.69814199231229"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 121.49012323785709, 375.81657515604132)" width="18.0" x="112.49012323785709" y="366.81657515604132"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 61.307745003459615, 50.0)" width="18.0" x="52.307745003459615" y="41.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 232.55960046680676, 80.278490134534138)" width="18.0" x="223.55960046680676" y="71.278490134534138"></rect></g><g class="toyplot-Datum" style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0"><rect height="18.0" transform="rotate(-45, 315.96743352739719, 176.02975578907311)" width="18.0" x="306.96743352739719" y="167.02975578907311"></rect></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(357.93052405031693,289.61945398457124)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(307.44790371831124,85.087395075373749)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(241.63815031716516,214.29190161189223)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(218.96078567750556,276.37753088528734)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(286.98421366377096,295.24448394853442)"><tspan style="dominant-baseline:inherit">4</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.34467256099879,230.93857122749455)"><tspan style="dominant-baseline:inherit">5</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(179.1281750526795,278.67789935387736)"><tspan style="dominant-baseline:inherit">6</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.4585318781954,152.90099420475144)"><tspan style="dominant-baseline:inherit">7</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(194.92330348555154,234.91919194066242)"><tspan style="dominant-baseline:inherit">8</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.92383690433017,102.62438379907093)"><tspan style="dominant-baseline:inherit">9</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(239.42727596275199,371.91895004143959)"><tspan style="dominant-baseline:inherit">10</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(238.06432820560855,335.51847153568144)"><tspan style="dominant-baseline:inherit">11</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(310.32191838574221,215.44961632176887)"><tspan style="dominant-baseline:inherit">12</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(199.99843098026366,127.64175314813249)"><tspan style="dominant-baseline:inherit">13</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.77483967815132,450.0)"><tspan style="dominant-baseline:inherit">14</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(288.07425895370818,335.56963579272133)"><tspan style="dominant-baseline:inherit">15</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(384.97626356638671,350.39993914200875)"><tspan style="dominant-baseline:inherit">16</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(341.02332764711673,249.73598123157626)"><tspan style="dominant-baseline:inherit">17</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(265.93134768774621,131.09731869914589)"><tspan style="dominant-baseline:inherit">18</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(258.61617079683487,187.58105684578322)"><tspan style="dominant-baseline:inherit">19</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.07138603825376,257.86846516387607)"><tspan style="dominant-baseline:inherit">20</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.60151231920814,267.76081525720156)"><tspan style="dominant-baseline:inherit">21</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(320.36813918234088,137.06079688462381)"><tspan style="dominant-baseline:inherit">22</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(116.14575907780782,129.80948433423811)"><tspan style="dominant-baseline:inherit">23</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(129.39283273278926,174.31712729178778)"><tspan style="dominant-baseline:inherit">24</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(175.56068840339933,329.69814199231229)"><tspan style="dominant-baseline:inherit">25</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(121.49012323785709,375.81657515604132)"><tspan style="dominant-baseline:inherit">26</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(61.307745003459615,50.0)"><tspan style="dominant-baseline:inherit">27</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(232.55960046680676,80.278490134534138)"><tspan style="dominant-baseline:inherit">28</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(100%,100%,100%);fill-opacity:1.0;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(315.96743352739719,176.02975578907311)"><tspan style="dominant-baseline:inherit">29</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"ta2de48b73860466d8cde3ba4950304fb": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -0.56107222851723615}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.607281613294538, "min": -0.74139805852485086}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 450.0}, "scale": "linear"}]}};
    
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


Of course, you can assign a :math:`[0, N)` colormap to the vertices
based on their index, or some other variable:

.. code:: python

    colormap = toyplot.color.LinearMap(toyplot.color.Palette(["white", "yellow", "red"]))
    vstyle = {"stroke":toyplot.color.near_black}
    
    toyplot.graph(edges, layout=layout, vcolor=colormap, vsize=20, vstyle=vstyle, width=500);



.. raw:: html

    <div align="center" class="toyplot" id="t8d009e2b72684a5692d90cc021acdb1d"><svg height="500.0px" id="t5457f7a614bc4cb7a8d26e895a95b167" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t4c47b3ae1a95461a9f3bd185a27423c2"><clipPath id="tceab367d922048cb90df30cf04d30da8"><rect height="440.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tceab367d922048cb90df30cf04d30da8)" style="cursor:crosshair"><rect height="440.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t66e91c9f3f484fffa99d9b186e95b1cd"><g class="toyplot-Edges"><path d="M 241.638150317 214.291901612 Q 309.546160188 231.764731184 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 241.638150317 214.291901612 Q 257.799199767 138.263609172 307.447903718 85.0873950754" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 Q 222.253687868 241.397420585 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 Q 222.253687868 241.397420585 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 Q 250.527499792 297.621389808 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 Q 253.820401982 262.641279508 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 Q 190.834141791 205.722921367 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 Q 187.541239601 240.703031667 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 Q 202.039273973 235.631776302 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 Q 155.549804743 260.847426162 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 Q 162.514621833 194.717507647 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 Q 209.004091063 169.501857786 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 Q 248.771413665 249.098013185 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 Q 215.607601983 216.494808744 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 Q 175.067874779 155.923832056 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 Q 147.206614092 120.898585278 160.458531878 152.900994205" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 Q 199.421262836 311.145951986 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 Q 253.269373016 325.32477323 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 Q 203.456987609 292.709074641 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 Q 224.141286107 274.284691445 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 Q 275.830004173 226.795791106 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 Q 275.830004173 226.795791106 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 Q 232.047427744 163.737244535 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 Q 232.047427744 163.737244535 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 Q 232.482404477 412.06155348 239.427275963 371.918950041" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 Q 227.083731947 394.097952319 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 Q 249.139621019 282.993111574 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 Q 263.062663118 344.226891666 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 Q 328.83255129 339.835814284 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 Q 363.576749479 324.705439415 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 Q 286.737481656 249.269422115 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 Q 319.901293338 281.872626555 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 Q 264.566073601 176.912450375 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 Q 264.566073601 176.912450375 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 Q 253.588663429 203.884241787 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 Q 230.677564509 246.930364839 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 Q 187.20760871 219.140419707 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 Q 187.20760871 219.140419707 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 Q 101.05448305 248.322410754 144.071386038 257.868465164" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 Q 97.701236492 234.810015158 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 Q 296.039159643 173.042444167 258.616170797 187.581056846" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 Q 291.011652275 189.345629108 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 Q 157.791175133 114.166926993 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 Q 169.155873399 168.686801576 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 Q 190.695889125 174.816226937 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 Q 117.001476307 154.363292892 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 Q 190.350830217 295.502612769 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 Q 193.643732408 260.522502469 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 Q 137.720786319 317.239987512 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 Q 142.548841236 343.369503983 175.560688403 329.698141992" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 Q 97.9354725204 65.9615103348 120.923836904 102.624383799" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 Q 99.0693960747 80.3836413497 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 Q 222.416899883 109.613465998 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 Q 254.465896646 145.708957385 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 Q 283.761247143 208.066048028 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 Q 283.761247143 208.066048028 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="357.93052405031693" cy="289.61945398457124" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,93.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="307.44790371831124" cy="85.087395075373749" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,86.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="241.63815031716516" cy="214.29190161189223" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,79.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="218.96078567750556" cy="276.37753088528734" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,72.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="286.98421366377096" cy="295.24448394853442" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,65.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="144.34467256099879" cy="230.93857122749455" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,58.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="179.1281750526795" cy="278.67789935387736" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,51.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="160.4585318781954" cy="152.90099420475144" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,44.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="194.92330348555154" cy="234.91919194066242" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,37.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="120.92383690433017" cy="102.62438379907093" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,31%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="239.42727596275199" cy="371.91895004143959" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,24.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="238.06432820560855" cy="335.51847153568144" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,17.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="310.32191838574221" cy="215.44961632176887" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,10.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="199.99843098026366" cy="127.64175314813249" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,3.45%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="245.77483967815132" cy="450.0" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,96.6%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="288.07425895370818" cy="335.56963579272133" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,89.7%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="384.97626356638671" cy="350.39993914200875" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,82.8%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="341.02332764711673" cy="249.73598123157626" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,75.9%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="265.93134768774621" cy="131.09731869914589" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,69%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="258.61617079683487" cy="187.58105684578322" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,62.1%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="144.07138603825376" cy="257.86846516387607" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,55.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="60.60151231920814" cy="267.76081525720156" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,48.3%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="320.36813918234088" cy="137.06079688462381" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,41.4%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="116.14575907780782" cy="129.80948433423811" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,34.5%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="129.39283273278926" cy="174.31712729178778" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,27.6%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="175.56068840339933" cy="329.69814199231229" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,20.7%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="121.49012323785709" cy="375.81657515604132" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,13.8%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="61.307745003459615" cy="50.0" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,6.9%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="232.55960046680676" cy="80.278490134534138" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="315.96743352739719" cy="176.02975578907311" r="10.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(357.93052405031693,289.61945398457124)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(307.44790371831124,85.087395075373749)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(241.63815031716516,214.29190161189223)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(218.96078567750556,276.37753088528734)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(286.98421366377096,295.24448394853442)"><tspan style="dominant-baseline:inherit">4</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.34467256099879,230.93857122749455)"><tspan style="dominant-baseline:inherit">5</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(179.1281750526795,278.67789935387736)"><tspan style="dominant-baseline:inherit">6</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.4585318781954,152.90099420475144)"><tspan style="dominant-baseline:inherit">7</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(194.92330348555154,234.91919194066242)"><tspan style="dominant-baseline:inherit">8</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.92383690433017,102.62438379907093)"><tspan style="dominant-baseline:inherit">9</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(239.42727596275199,371.91895004143959)"><tspan style="dominant-baseline:inherit">10</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(238.06432820560855,335.51847153568144)"><tspan style="dominant-baseline:inherit">11</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(310.32191838574221,215.44961632176887)"><tspan style="dominant-baseline:inherit">12</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(199.99843098026366,127.64175314813249)"><tspan style="dominant-baseline:inherit">13</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.77483967815132,450.0)"><tspan style="dominant-baseline:inherit">14</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(288.07425895370818,335.56963579272133)"><tspan style="dominant-baseline:inherit">15</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(384.97626356638671,350.39993914200875)"><tspan style="dominant-baseline:inherit">16</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(341.02332764711673,249.73598123157626)"><tspan style="dominant-baseline:inherit">17</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(265.93134768774621,131.09731869914589)"><tspan style="dominant-baseline:inherit">18</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(258.61617079683487,187.58105684578322)"><tspan style="dominant-baseline:inherit">19</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.07138603825376,257.86846516387607)"><tspan style="dominant-baseline:inherit">20</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.60151231920814,267.76081525720156)"><tspan style="dominant-baseline:inherit">21</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(320.36813918234088,137.06079688462381)"><tspan style="dominant-baseline:inherit">22</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(116.14575907780782,129.80948433423811)"><tspan style="dominant-baseline:inherit">23</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(129.39283273278926,174.31712729178778)"><tspan style="dominant-baseline:inherit">24</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(175.56068840339933,329.69814199231229)"><tspan style="dominant-baseline:inherit">25</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(121.49012323785709,375.81657515604132)"><tspan style="dominant-baseline:inherit">26</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(61.307745003459615,50.0)"><tspan style="dominant-baseline:inherit">27</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(232.55960046680676,80.278490134534138)"><tspan style="dominant-baseline:inherit">28</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(315.96743352739719,176.02975578907311)"><tspan style="dominant-baseline:inherit">29</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"t4c47b3ae1a95461a9f3bd185a27423c2": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -0.56107222851723615}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.607281613294538, "min": -0.74139805852485086}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 450.0}, "scale": "linear"}]}};
    
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


Edge Rendering
--------------

Much like vertices, there are color, width, and style controls for
edges:

.. code:: python

    estyle = {"stroke-dasharray":"3,3"}
    toyplot.graph(
        edges,
        layout=layout,
        ecolor="black",
        ewidth=1.2,
        eopacity=0.4,
        estyle=estyle,
        vcolor=colormap,
        vsize=20,
        vstyle=vstyle,
        width=500,
    );



.. raw:: html

    <div align="center" class="toyplot" id="tf66d603b22bc443aafd4c55c4d3a2d39"><svg height="500.0px" id="t90a8876657d94ce79ec2498bf712fa9d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t7ac09e1ca2154eb8b11f67c5f21bc4fb"><clipPath id="tb641f19769ae46dca15a63dea4968403"><rect height="440.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb641f19769ae46dca15a63dea4968403)" style="cursor:crosshair"><rect height="440.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="ta82c893538ca402d9a80f0bdceb2d80b"><g class="toyplot-Edges"><path d="M 241.638150317 214.291901612 Q 309.546160188 231.764731184 357.93052405 289.619453985" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 241.638150317 214.291901612 Q 257.799199767 138.263609172 307.447903718 85.0873950754" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 218.960785678 276.377530885 Q 222.253687868 241.397420585 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 218.960785678 276.377530885 Q 222.253687868 241.397420585 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 286.984213664 295.244483949 Q 250.527499792 297.621389808 218.960785678 276.377530885" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 286.984213664 295.244483949 Q 253.820401982 262.641279508 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 144.344672561 230.938571227 Q 190.834141791 205.722921367 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 144.344672561 230.938571227 Q 187.541239601 240.703031667 218.960785678 276.377530885" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 179.128175053 278.677899354 Q 202.039273973 235.631776302 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 179.128175053 278.677899354 Q 155.549804743 260.847426162 144.344672561 230.938571227" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 160.458531878 152.900994205 Q 162.514621833 194.717507647 144.344672561 230.938571227" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 160.458531878 152.900994205 Q 209.004091063 169.501857786 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 194.923303486 234.919191941 Q 248.771413665 249.098013185 286.984213664 295.244483949" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 194.923303486 234.919191941 Q 215.607601983 216.494808744 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 120.923836904 102.624383799 Q 175.067874779 155.923832056 194.923303486 234.919191941" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 120.923836904 102.624383799 Q 147.206614092 120.898585278 160.458531878 152.900994205" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 239.427275963 371.918950041 Q 199.421262836 311.145951986 194.923303486 234.919191941" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 239.427275963 371.918950041 Q 253.269373016 325.32477323 286.984213664 295.244483949" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 238.064328206 335.518471536 Q 203.456987609 292.709074641 194.923303486 234.919191941" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 238.064328206 335.518471536 Q 224.141286107 274.284691445 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 310.321918386 215.449616322 Q 275.830004173 226.795791106 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 310.321918386 215.449616322 Q 275.830004173 226.795791106 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 199.99843098 127.641753148 Q 232.047427744 163.737244535 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 199.99843098 127.641753148 Q 232.047427744 163.737244535 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 245.774839678 450.0 Q 232.482404477 412.06155348 239.427275963 371.918950041" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 245.774839678 450.0 Q 227.083731947 394.097952319 238.064328206 335.518471536" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 288.074258954 335.569635793 Q 249.139621019 282.993111574 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 288.074258954 335.569635793 Q 263.062663118 344.226891666 238.064328206 335.518471536" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 384.976263566 350.399939142 Q 328.83255129 339.835814284 286.984213664 295.244483949" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 384.976263566 350.399939142 Q 363.576749479 324.705439415 357.93052405 289.619453985" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 341.023327647 249.735981232 Q 286.737481656 249.269422115 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 341.023327647 249.735981232 Q 319.901293338 281.872626555 286.984213664 295.244483949" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 265.931347688 131.097318699 Q 264.566073601 176.912450375 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 265.931347688 131.097318699 Q 264.566073601 176.912450375 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 258.616170797 187.581056846 Q 253.588663429 203.884241787 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 258.616170797 187.581056846 Q 230.677564509 246.930364839 179.128175053 278.677899354" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 144.071386038 257.868465164 Q 187.20760871 219.140419707 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 144.071386038 257.868465164 Q 187.20760871 219.140419707 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 60.6015123192 267.760815257 Q 101.05448305 248.322410754 144.071386038 257.868465164" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 60.6015123192 267.760815257 Q 97.701236492 234.810015158 144.344672561 230.938571227" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 320.368139182 137.060796885 Q 296.039159643 173.042444167 258.616170797 187.581056846" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 320.368139182 137.060796885 Q 291.011652275 189.345629108 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 116.145759078 129.809484334 Q 157.791175133 114.166926993 199.99843098 127.641753148" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 116.145759078 129.809484334 Q 169.155873399 168.686801576 194.923303486 234.919191941" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 129.392832733 174.317127292 Q 190.695889125 174.816226937 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 129.392832733 174.317127292 Q 117.001476307 154.363292892 116.145759078 129.809484334" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 175.560688403 329.698141992 Q 190.350830217 295.502612769 218.960785678 276.377530885" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 175.560688403 329.698141992 Q 193.643732408 260.522502469 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 121.490123238 375.816575156 Q 137.720786319 317.239987512 179.128175053 278.677899354" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 121.490123238 375.816575156 Q 142.548841236 343.369503983 175.560688403 329.698141992" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 61.3077450035 50.0 Q 97.9354725204 65.9615103348 120.923836904 102.624383799" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 61.3077450035 50.0 Q 99.0693960747 80.3836413497 116.145759078 129.809484334" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 232.559600467 80.2784901345 Q 222.416899883 109.613465998 199.99843098 127.641753148" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 232.559600467 80.2784901345 Q 254.465896646 145.708957385 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 315.967433527 176.029755789 Q 283.761247143 208.066048028 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path><path d="M 315.967433527 176.029755789 Q 283.761247143 208.066048028 241.638150317 214.291901612" style="fill:none;stroke:rgb(0%,0%,0%);stroke-dasharray:3,3;stroke-opacity:0.4;stroke-width:1.2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="357.93052405031693" cy="289.61945398457124" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,93.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="307.44790371831124" cy="85.087395075373749" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,86.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="241.63815031716516" cy="214.29190161189223" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,79.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="218.96078567750556" cy="276.37753088528734" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,72.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="286.98421366377096" cy="295.24448394853442" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,65.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="144.34467256099879" cy="230.93857122749455" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,58.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="179.1281750526795" cy="278.67789935387736" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,51.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="160.4585318781954" cy="152.90099420475144" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,44.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="194.92330348555154" cy="234.91919194066242" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,37.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="120.92383690433017" cy="102.62438379907093" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,31%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="239.42727596275199" cy="371.91895004143959" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,24.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="238.06432820560855" cy="335.51847153568144" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,17.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="310.32191838574221" cy="215.44961632176887" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,10.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="199.99843098026366" cy="127.64175314813249" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,3.45%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="245.77483967815132" cy="450.0" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,96.6%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="288.07425895370818" cy="335.56963579272133" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,89.7%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="384.97626356638671" cy="350.39993914200875" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,82.8%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="341.02332764711673" cy="249.73598123157626" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,75.9%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="265.93134768774621" cy="131.09731869914589" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,69%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="258.61617079683487" cy="187.58105684578322" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,62.1%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="144.07138603825376" cy="257.86846516387607" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,55.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="60.60151231920814" cy="267.76081525720156" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,48.3%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="320.36813918234088" cy="137.06079688462381" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,41.4%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="116.14575907780782" cy="129.80948433423811" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,34.5%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="129.39283273278926" cy="174.31712729178778" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,27.6%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="175.56068840339933" cy="329.69814199231229" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,20.7%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="121.49012323785709" cy="375.81657515604132" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,13.8%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="61.307745003459615" cy="50.0" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,6.9%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="232.55960046680676" cy="80.278490134534138" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="315.96743352739719" cy="176.02975578907311" r="10.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(357.93052405031693,289.61945398457124)"><tspan style="dominant-baseline:inherit">0</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(307.44790371831124,85.087395075373749)"><tspan style="dominant-baseline:inherit">1</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(241.63815031716516,214.29190161189223)"><tspan style="dominant-baseline:inherit">2</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(218.96078567750556,276.37753088528734)"><tspan style="dominant-baseline:inherit">3</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(286.98421366377096,295.24448394853442)"><tspan style="dominant-baseline:inherit">4</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.34467256099879,230.93857122749455)"><tspan style="dominant-baseline:inherit">5</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(179.1281750526795,278.67789935387736)"><tspan style="dominant-baseline:inherit">6</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.4585318781954,152.90099420475144)"><tspan style="dominant-baseline:inherit">7</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(194.92330348555154,234.91919194066242)"><tspan style="dominant-baseline:inherit">8</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.92383690433017,102.62438379907093)"><tspan style="dominant-baseline:inherit">9</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(239.42727596275199,371.91895004143959)"><tspan style="dominant-baseline:inherit">10</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(238.06432820560855,335.51847153568144)"><tspan style="dominant-baseline:inherit">11</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(310.32191838574221,215.44961632176887)"><tspan style="dominant-baseline:inherit">12</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(199.99843098026366,127.64175314813249)"><tspan style="dominant-baseline:inherit">13</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.77483967815132,450.0)"><tspan style="dominant-baseline:inherit">14</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(288.07425895370818,335.56963579272133)"><tspan style="dominant-baseline:inherit">15</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(384.97626356638671,350.39993914200875)"><tspan style="dominant-baseline:inherit">16</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(341.02332764711673,249.73598123157626)"><tspan style="dominant-baseline:inherit">17</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(265.93134768774621,131.09731869914589)"><tspan style="dominant-baseline:inherit">18</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(258.61617079683487,187.58105684578322)"><tspan style="dominant-baseline:inherit">19</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(144.07138603825376,257.86846516387607)"><tspan style="dominant-baseline:inherit">20</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(60.60151231920814,267.76081525720156)"><tspan style="dominant-baseline:inherit">21</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(320.36813918234088,137.06079688462381)"><tspan style="dominant-baseline:inherit">22</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(116.14575907780782,129.80948433423811)"><tspan style="dominant-baseline:inherit">23</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(129.39283273278926,174.31712729178778)"><tspan style="dominant-baseline:inherit">24</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(175.56068840339933,329.69814199231229)"><tspan style="dominant-baseline:inherit">25</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(121.49012323785709,375.81657515604132)"><tspan style="dominant-baseline:inherit">26</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(61.307745003459615,50.0)"><tspan style="dominant-baseline:inherit">27</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(232.55960046680676,80.278490134534138)"><tspan style="dominant-baseline:inherit">28</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(315.96743352739719,176.02975578907311)"><tspan style="dominant-baseline:inherit">29</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"t7ac09e1ca2154eb8b11f67c5f21bc4fb": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -0.56107222851723615}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.607281613294538, "min": -0.74139805852485086}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 450.0}, "scale": "linear"}]}};
    
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

