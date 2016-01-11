
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _graph-visualization:

Graph Visualization
===================

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

    <div align="center" class="toyplot" id="t4df2e73e8e0644cabdd0327862371c4d"><svg height="300.0px" id="tb868903e796d4369b8d232ebfe9215bd" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t8672ce8c215546f0a9dce37cec6575c3"><clipPath id="t754afbffe6234ca8a608095e51b96d40"><rect height="240.0" width="240.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t754afbffe6234ca8a608095e51b96d40)" style="cursor:crosshair"><rect height="240.0" style="pointer-events:all;visibility:hidden" width="240.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="td2859cac9ac84d98bf3e7515482df1e9"><g class="toyplot-Edges"><path d="M 100.05418841 74.4927639832 L 50.0 139.983031773" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 100.05418841 74.4927639832 L 151.843314374 157.297286753" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 50.0 139.983031773 L 151.843314374 157.297286753" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 151.843314374 157.297286753 L 245.87745869 218.577192308" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="139.98303177344994" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="151.84331437387584" cy="157.29728675328977" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="245.87745869046307" cy="218.57719230842898" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.05418841029831" cy="74.492763983202948" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,139.98303177344994)"><tspan style="dominant-baseline:inherit">Fred</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(151.84331437387584,157.29728675328977)"><tspan style="dominant-baseline:inherit">Janet</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(245.87745869046307,218.57719230842898)"><tspan style="dominant-baseline:inherit">Pam</tspan></text><text class="toyplot-Datum" style="dominant-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.05418841029831,74.492763983202948)"><tspan style="dominant-baseline:inherit">Tim</tspan></text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      var axes = {"t8672ce8c215546f0a9dce37cec6575c3": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.60806645552998795}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.90000000000000013, "min": -0.30000000000000004}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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


Note that Toyplot has *induced* a set of unique vertices from the edge
source and target sequences, used a *layout algorithm* to specify
coordinates for each vertex, rendered *vertices*, rendered a set of
*vertex labels*, and rendered a straight line between each pair of
vertices that are connected by an edge. We will be examine each of these
concepts in depth in the rest of this guide.
