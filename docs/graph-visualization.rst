
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

    <div align="center" class="toyplot" id="t90b4bebb4b62489d94270e35224aa054"><svg height="300.0px" id="t2996b4765c294499a6787f8c1311308c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t30cde691b2ac4cd6bf5eb8be6de6a467"><clipPath id="td7b462419c7d4496b25961737533ab17"><rect height="240.0" width="240.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td7b462419c7d4496b25961737533ab17)" style="cursor:crosshair"><rect height="240.0" style="pointer-events:all;visibility:hidden" width="240.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t788787a6dce34626ac9a34822cf23c83"><g class="toyplot-Edges"><path d="M 100.05418841 74.4927639832 L 50.0 139.983031773" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 100.05418841 74.4927639832 L 151.843314374 157.297286753" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 50.0 139.983031773 L 151.843314374 157.297286753" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 151.843314374 157.297286753 L 245.87745869 218.577192308" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="139.98303177344994" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="151.84331437387584" cy="157.29728675328977" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="245.87745869046307" cy="218.57719230842898" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.05418841029831" cy="74.492763983202948" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="50.0" y="139.98303177344994">Fred</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="151.84331437387584" y="157.29728675328977">Janet</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="245.87745869046307" y="218.57719230842898">Pam</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="100.05418841029831" y="74.492763983202948">Tim</text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t90b4bebb4b62489d94270e35224aa054 text");
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
          var text = document.querySelectorAll("#t90b4bebb4b62489d94270e35224aa054 text");
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
      var axes = {"t30cde691b2ac4cd6bf5eb8be6de6a467": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.60806645552998795}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.90000000000000013, "min": -0.30000000000000004}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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
concepts as we go.

Let's begin by generating a random graph and creating a visualization:

.. code:: python

    import toyplot.generate
    edges = toyplot.generate.barabasi_albert_graph()
    toyplot.graph(edges, width=500);



.. raw:: html

    <div align="center" class="toyplot" id="tad6d793cd3dc42df9120bfc536a0e212"><svg height="500.0px" id="tf38df0dfce4c4e0b9ba321dfd7de8bb9" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="td2bad262f0e9483385e7f741d2cd43de"><clipPath id="tc1cb8c88fbe140069f1f995bc3a2ca53"><rect height="440.0" width="440.0" x="30.0" y="30.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tc1cb8c88fbe140069f1f995bc3a2ca53)" style="cursor:crosshair"><rect height="440.0" style="pointer-events:all;visibility:hidden" width="440.0" x="30.0" y="30.0"></rect><g class="toyplot-mark-Graph" id="t980eaf9911b94488b3d397967840d9c9"><g class="toyplot-Edges"><path d="M 241.638150317 214.291901612 L 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 241.638150317 214.291901612 L 307.447903718 85.0873950754" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.960785678 276.377530885 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 L 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 286.984213664 295.244483949 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.344672561 230.938571227 L 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 179.128175053 278.677899354 L 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 L 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 160.458531878 152.900994205 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 194.923303486 234.919191941 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 120.923836904 102.624383799 L 160.458531878 152.900994205" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 239.427275963 371.918950041 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 238.064328206 335.518471536 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.321918386 215.449616322 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 199.99843098 127.641753148 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 L 239.427275963 371.918950041" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.774839678 450.0 L 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 288.074258954 335.569635793 L 238.064328206 335.518471536" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 384.976263566 350.399939142 L 357.93052405 289.619453985" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.023327647 249.735981232 L 286.984213664 295.244483949" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.931347688 131.097318699 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 258.616170797 187.581056846 L 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 144.071386038 257.868465164 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 L 144.071386038 257.868465164" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 60.6015123192 267.760815257 L 144.344672561 230.938571227" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 L 258.616170797 187.581056846" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 320.368139182 137.060796885 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 L 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 116.145759078 129.809484334 L 194.923303486 234.919191941" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 129.392832733 174.317127292 L 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 L 218.960785678 276.377530885" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 175.560688403 329.698141992 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 L 179.128175053 278.677899354" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 121.490123238 375.816575156 L 175.560688403 329.698141992" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 L 120.923836904 102.624383799" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 61.3077450035 50.0 L 116.145759078 129.809484334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 L 199.99843098 127.641753148" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.559600467 80.2784901345 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 315.967433527 176.029755789 L 241.638150317 214.291901612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="357.93052405031693" cy="289.61945398457124" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="307.44790371831124" cy="85.087395075373749" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="241.63815031716516" cy="214.29190161189223" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.96078567750556" cy="276.37753088528734" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="286.98421366377096" cy="295.24448394853442" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="144.34467256099879" cy="230.93857122749455" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="179.1281750526795" cy="278.67789935387736" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.4585318781954" cy="152.90099420475144" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="194.92330348555154" cy="234.91919194066242" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.92383690433017" cy="102.62438379907093" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="239.42727596275199" cy="371.91895004143959" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="238.06432820560855" cy="335.51847153568144" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="310.32191838574221" cy="215.44961632176887" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="199.99843098026366" cy="127.64175314813249" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="245.77483967815132" cy="450.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="288.07425895370818" cy="335.56963579272133" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="384.97626356638671" cy="350.39993914200875" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.02332764711673" cy="249.73598123157626" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.93134768774621" cy="131.09731869914589" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="258.61617079683487" cy="187.58105684578322" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="144.07138603825376" cy="257.86846516387607" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.60151231920814" cy="267.76081525720156" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="320.36813918234088" cy="137.06079688462381" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="116.14575907780782" cy="129.80948433423811" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="129.39283273278926" cy="174.31712729178778" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="175.56068840339933" cy="329.69814199231229" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="121.49012323785709" cy="375.81657515604132" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.307745003459615" cy="50.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="232.55960046680676" cy="80.278490134534138" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.96743352739719" cy="176.02975578907311" r="2.0"></circle></g></g><g class="toyplot-Labels"><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="357.93052405031693" y="289.61945398457124">0</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="307.44790371831124" y="85.087395075373749">1</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="241.63815031716516" y="214.29190161189223">2</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="218.96078567750556" y="276.37753088528734">3</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="286.98421366377096" y="295.24448394853442">4</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="144.34467256099879" y="230.93857122749455">5</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="179.1281750526795" y="278.67789935387736">6</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="160.4585318781954" y="152.90099420475144">7</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="194.92330348555154" y="234.91919194066242">8</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="120.92383690433017" y="102.62438379907093">9</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="239.42727596275199" y="371.91895004143959">10</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="238.06432820560855" y="335.51847153568144">11</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="310.32191838574221" y="215.44961632176887">12</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="199.99843098026366" y="127.64175314813249">13</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="245.77483967815132" y="450.0">14</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="288.07425895370818" y="335.56963579272133">15</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="384.97626356638671" y="350.39993914200875">16</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="341.02332764711673" y="249.73598123157626">17</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="265.93134768774621" y="131.09731869914589">18</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="258.61617079683487" y="187.58105684578322">19</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="144.07138603825376" y="257.86846516387607">20</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="60.60151231920814" y="267.76081525720156">21</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="320.36813918234088" y="137.06079688462381">22</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="116.14575907780782" y="129.80948433423811">23</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="129.39283273278926" y="174.31712729178778">24</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="175.56068840339933" y="329.69814199231229">25</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="121.49012323785709" y="375.81657515604132">26</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="61.307745003459615" y="50.0">27</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="232.55960046680676" y="80.278490134534138">28</text><text class="toyplot-Datum" style="alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:middle" x="315.96743352739719" y="176.02975578907311">29</text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="350.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="395.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tad6d793cd3dc42df9120bfc536a0e212 text");
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
          var text = document.querySelectorAll("#tad6d793cd3dc42df9120bfc536a0e212 text");
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
      var axes = {"td2bad262f0e9483385e7f741d2cd43de": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -0.56107222851723615}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.607281613294538, "min": -0.74139805852485086}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 450.0}, "scale": "linear"}]}};
    
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



