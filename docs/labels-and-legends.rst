
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
labels that can be specified when they are created. In either case the
``label`` parameter provides a top-level label for the set of axes:

.. code:: python

    import numpy
    import toyplot
    
    canvas = toyplot.Canvas(width=600, height=300)
    canvas.axes(grid=(1,2,0), label="Cartesian Axes").plot(numpy.linspace(0, 1)**2)
    canvas.table(grid=(1,2,1), label="Table Axes", data = numpy.random.random((4, 3)));



.. raw:: html

    <div align="center" class="toyplot" id="t5944a16b2d1444898acd096ef49e175f"><svg height="300.0px" id="t19853a3a543d4b42a3ae2b95d921542d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t9a462bd4984847dd9125f4f1fda11223"><clipPath id="td3267e74de6048e698ad4a96c9026856"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td3267e74de6048e698ad4a96c9026856)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tb9ebefd3e0ee4aa4adfb21019f6447ca" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 54.0 249.9167013744273 L 58.0 249.66680549770928 L 62.0 249.25031236984589 L 66.0 248.66722199083716 L 70.0 247.91753436068305 L 74.0 247.0012494793836 L 78.0 245.91836734693877 L 82.0 244.6688879633486 L 86.0 243.25281132861306 L 90.0 241.6701374427322 L 94.0 239.92086630570594 L 98.0 238.00499791753435 L 102.0 235.92253227821743 L 106.0 233.67346938775512 L 110.0 231.25780924614745 L 114.0 228.67555185339444 L 118.0 225.92669720949604 L 122.0 223.01124531445231 L 126.0 219.92919616826322 L 130.0 216.68054977092879 L 134.0 213.26530612244898 L 138.0 209.68346522282383 L 142.0 205.93502707205332 L 146.0 202.01999167013744 L 150.0 197.93835901707621 L 154.0 193.69012911286964 L 158.0 189.27530195751771 L 162.0 184.69387755102045 L 166.0 179.94585589337777 L 170.0 175.03123698458978 L 174.0 169.95002082465641 L 178.0 164.7022074135777 L 182.0 159.2877967513536 L 186.0 153.70678883798416 L 190.0 147.9591836734694 L 194.0 142.04498125780927 L 198.0 135.96418159100375 L 202.0 129.7167846730529 L 206.0 123.30279050395671 L 210.0 116.72219908371514 L 214.0 109.97501041232822 L 218.0 103.06122448979593 L 222.0 95.980841316118301 L 226.0 88.733860891295336 L 230.0 81.320283215326981 L 234.0 73.740108288213264 L 238.0 65.993336109954186 L 242.0 58.079966680549774 L 246.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t2bbc9123bcb84ad98ccefa2e798b1dcd" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(40.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(80.0,0) rotate(0)" x="0" y="0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.0,0) rotate(0)" x="0" y="0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">50</text></g></g><g class="toyplot-axes-Axis" id="t861c19a6782a47a2be0217ee884dc779" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="50.0">Cartesian Axes</text></g><g class="toyplot-axes-Table" id="t142bb026aa1e495b816d3f9de6cd0879"><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="450.0" y="50.0">Table Axes</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(0,383.33333333333337,70.0)" x="383.33333333333337" y="70.0">C0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(0,450.0,70.0)" x="450.0" y="70.0">C1</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(0,516.66666666666674,70.0)" x="516.66666666666674" y="70.0">C2</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="381.33333333333337" y="110.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="383.33333333333337" y="110.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="385.33333333333337" y="110.0">829676</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="448.0" y="110.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="450.0" y="110.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="452.0" y="110.0">371061</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="514.66666666666674" y="110.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="516.66666666666674" y="110.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="518.66666666666674" y="110.0">0434714</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="381.33333333333337" y="150.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="383.33333333333337" y="150.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="385.33333333333337" y="150.0">0208749</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="448.0" y="150.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="450.0" y="150.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="452.0" y="150.0">359629</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="514.66666666666674" y="150.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="516.66666666666674" y="150.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="518.66666666666674" y="150.0">387285</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="381.33333333333337" y="190.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="383.33333333333337" y="190.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="385.33333333333337" y="190.0">773577</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="448.0" y="190.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="450.0" y="190.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="452.0" y="190.0">345967</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="514.66666666666674" y="190.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="516.66666666666674" y="190.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="518.66666666666674" y="190.0">463346</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="381.33333333333337" y="230.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="383.33333333333337" y="230.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="385.33333333333337" y="230.0">680361</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="448.0" y="230.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="450.0" y="230.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="452.0" y="230.0">535428</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="514.66666666666674" y="230.0">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="516.66666666666674" y="230.0">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="518.66666666666674" y="230.0">749271</text><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="350.0" x2="550.0" y1="90.0" y2="90.0"></line></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t5944a16b2d1444898acd096ef49e175f text");
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
          var text = document.querySelectorAll("#t5944a16b2d1444898acd096ef49e175f text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tb9ebefd3e0ee4aa4adfb21019f6447ca", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t5944a16b2d1444898acd096ef49e175f .toyplot-mark-popup");
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
      var axes = {"t9a462bd4984847dd9125f4f1fda11223": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="t8fb5a700cd714436a9eb754c8a9ddcb6"><svg height="300.0px" id="t0cd8372e3c7b4c97864c1368868ccd07" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t2037530fc8c8489a8a8e7f182ace468c"><clipPath id="tf8295ad89b604ef599339f7686738799"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf8295ad89b604ef599339f7686738799)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="te4eb43984f21488e807c7cd54735c7ea" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 54.0 249.9167013744273 L 58.0 249.66680549770928 L 62.0 249.25031236984589 L 66.0 248.66722199083716 L 70.0 247.91753436068305 L 74.0 247.0012494793836 L 78.0 245.91836734693877 L 82.0 244.6688879633486 L 86.0 243.25281132861306 L 90.0 241.6701374427322 L 94.0 239.92086630570594 L 98.0 238.00499791753435 L 102.0 235.92253227821743 L 106.0 233.67346938775512 L 110.0 231.25780924614745 L 114.0 228.67555185339444 L 118.0 225.92669720949604 L 122.0 223.01124531445231 L 126.0 219.92919616826322 L 130.0 216.68054977092879 L 134.0 213.26530612244898 L 138.0 209.68346522282383 L 142.0 205.93502707205332 L 146.0 202.01999167013744 L 150.0 197.93835901707621 L 154.0 193.69012911286964 L 158.0 189.27530195751771 L 162.0 184.69387755102045 L 166.0 179.94585589337777 L 170.0 175.03123698458978 L 174.0 169.95002082465641 L 178.0 164.7022074135777 L 182.0 159.2877967513536 L 186.0 153.70678883798416 L 190.0 147.9591836734694 L 194.0 142.04498125780927 L 198.0 135.96418159100375 L 202.0 129.7167846730529 L 206.0 123.30279050395671 L 210.0 116.72219908371514 L 214.0 109.97501041232822 L 218.0 103.06122448979593 L 222.0 95.980841316118301 L 226.0 88.733860891295336 L 230.0 81.320283215326981 L 234.0 73.740108288213264 L 238.0 65.993336109954186 L 242.0 58.079966680549774 L 246.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tdf3cf1ca904344cb840cc4cc7eeb8beb" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(40.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(80.0,0) rotate(0)" x="0" y="0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.0,0) rotate(0)" x="0" y="0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">50</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="100.0" y="0">Days</text></g><g class="toyplot-axes-Axis" id="t51f4ad9f70a940849aabbc02eb1c9202" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:200%;font-weight:bold;stroke:none;text-anchor:middle" x="100.0" y="0">Users</text></g><text style="alignment-baseline:middle;baseline-shift:100%;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="50.0">Cartesian Axes</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t8fb5a700cd714436a9eb754c8a9ddcb6 text");
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
          var text = document.querySelectorAll("#t8fb5a700cd714436a9eb754c8a9ddcb6 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "te4eb43984f21488e807c7cd54735c7ea", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t8fb5a700cd714436a9eb754c8a9ddcb6 .toyplot-mark-popup");
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
      var axes = {"t2037530fc8c8489a8a8e7f182ace468c": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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

    <div align="center" class="toyplot" id="tde079d87a64740fb9194a27a09cfb256"><svg height="600px" id="t2af07c375862470bab7e333aa1d51b58" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc2f1ab643a7d4f08aec22772d4437a99"><clipPath id="t10f423d0c49a4615ae5a2e73de2351ed"><rect height="520.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t10f423d0c49a4615ae5a2e73de2351ed)" style="cursor:crosshair"><rect height="520.0" style="pointer-events:all;visibility:hidden" width="520.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t63161e51cee948b0b39ddbf6d76e5657" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 344.02566491299245 L 54.166666666666671 359.52435012920887 L 58.333333333333329 339.38368571528491 L 62.5 342.95147342351925 L 66.666666666666671 352.06055763643002 L 70.833333333333343 339.33040617437791 L 75.0 326.97481913958944 L 79.166666666666671 334.94198549471088 L 83.333333333333329 334.04958489759656 L 87.5 363.83438578417156 L 91.666666666666657 347.53344613056089 L 95.833333333333329 333.37995146148069 L 100.0 319.75108547985252 L 104.16666666666666 346.52804320199868 L 108.33333333333334 350.38686831995557 L 112.5 349.67890746508289 L 116.66666666666666 343.49215950075029 L 120.83333333333334 338.88603223880403 L 125.0 320.26061427412338 L 129.16666666666666 340.59414817457599 L 133.33333333333331 342.66765188356493 L 137.5 350.89896492472712 L 141.66666666666666 347.59239905630801 L 145.83333333333334 339.39545869068428 L 150.0 320.81088202994266 L 154.16666666666669 326.50660425023466 L 158.33333333333334 316.6508865300209 L 162.5 340.65367544170857 L 166.66666666666669 342.46178351394502 L 170.83333333333331 327.39786547222866 L 175.0 332.12282694811319 L 179.16666666666669 326.85998545014661 L 183.33333333333331 311.9507942375285 L 187.5 297.06388462219934 L 191.66666666666669 284.65221209828951 L 195.83333333333334 285.63148328740351 L 200.0 283.25823284375969 L 204.16666666666669 286.9637989135345 L 208.33333333333331 274.85154642988908 L 212.5 241.69424182656198 L 216.66666666666666 239.97998297303855 L 220.83333333333331 246.99523574714044 L 225.0 245.82510848958731 L 229.16666666666669 273.33182098889097 L 233.33333333333331 269.28669751679564 L 237.5 280.79423128086148 L 241.66666666666669 281.97322729747481 L 245.83333333333331 281.04560659065186 L 250.0 270.10509502687177 L 254.16666666666669 266.50176302490871 L 258.33333333333337 254.39855618045905 L 262.5 273.35883824965606 L 266.66666666666669 291.72365391394374 L 270.83333333333331 292.41531207673006 L 275.0 299.18329400406679 L 279.16666666666663 300.4685781537064 L 283.33333333333337 294.98048232593499 L 287.5 294.78369543381172 L 291.66666666666663 286.41968362750799 L 295.83333333333331 264.74471400272722 L 300.0 277.29927416461987 L 304.16666666666663 277.57563311552661 L 308.33333333333337 272.71308728747539 L 312.5 274.86608883512861 L 316.66666666666663 260.14405183739575 L 320.83333333333331 292.07193702792193 L 325.0 263.80961669217044 L 329.16666666666663 278.65160542560204 L 333.33333333333337 275.09425692654531 L 337.5 264.84234933837666 L 341.66666666666669 274.83228943694439 L 345.83333333333337 267.87661744936986 L 350.0 257.63139846542725 L 354.16666666666663 249.84103140974256 L 358.33333333333337 261.74381762838391 L 362.5 233.79067167927286 L 366.66666666666663 230.02849228048683 L 370.83333333333337 245.00669603571302 L 375.0 235.74288366568288 L 379.16666666666663 234.5269691108376 L 383.33333333333331 227.53961192120653 L 387.5 275.26621028574425 L 391.66666666666663 256.64150650725895 L 395.83333333333337 253.88903144720589 L 400.0 250.97492392422006 L 404.16666666666669 256.13803431497257 L 408.33333333333337 245.03513282480321 L 412.5 230.97707976706079 L 416.66666666666663 226.61893800285478 L 420.83333333333337 207.03141286796946 L 425.0 205.26767228488558 L 429.16666666666663 210.02149035323276 L 433.33333333333337 223.30433070454387 L 437.5 230.56778887824439 L 441.66666666666663 218.79622657401373 L 445.83333333333331 219.23018612472529 L 450.0 223.23420276466501 L 454.16666666666663 215.37890315590357 L 458.33333333333337 229.22055330435566 L 462.5 235.49461597775218" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 346.47385466109324 L 54.166666666666671 338.0990385021629 L 58.333333333333329 330.57920749036964 L 62.5 326.02464747923227 L 66.666666666666671 318.7670316398299 L 70.833333333333343 299.56670588208419 L 75.0 309.49782948392198 L 79.166666666666671 315.17606106715374 L 83.333333333333329 297.86261012651403 L 87.5 314.58563035565709 L 91.666666666666657 302.01423765849967 L 95.833333333333329 324.57291630546456 L 100.0 330.01679403920679 L 104.16666666666666 319.16118307255982 L 108.33333333333334 321.25216279035925 L 112.5 323.04759551362866 L 116.66666666666666 313.12257479164037 L 120.83333333333334 337.14535571891309 L 125.0 335.82676258295362 L 129.16666666666666 329.78412696625645 L 133.33333333333331 332.47957084111226 L 137.5 340.19113443819907 L 141.66666666666666 348.78804836446176 L 145.83333333333334 342.1828651176703 L 150.0 364.63691454503942 L 154.16666666666669 358.60967756264409 L 158.33333333333334 364.441491174497 L 162.5 367.8240567771615 L 166.66666666666669 357.71637203191216 L 170.83333333333331 347.8188764021487 L 175.0 343.88563116313566 L 179.16666666666669 341.15222658753925 L 183.33333333333331 329.38700370915603 L 187.5 302.98659127277205 L 191.66666666666669 293.61881844367724 L 195.83333333333334 306.00755541624585 L 200.0 333.6540177072024 L 204.16666666666669 306.75491596316834 L 208.33333333333331 329.6482096644346 L 212.5 312.52752042925385 L 216.66666666666666 301.01620176776044 L 220.83333333333331 305.49625646706664 L 225.0 295.27366796712738 L 229.16666666666669 306.14534120776227 L 233.33333333333331 289.48067422867882 L 237.5 295.9239192298607 L 241.66666666666669 285.72380488747899 L 245.83333333333331 271.6756919987846 L 250.0 272.65003004309608 L 254.16666666666669 239.83492477195796 L 258.33333333333337 232.41627656039157 L 262.5 220.91637572553591 L 266.66666666666669 226.6761533716747 L 270.83333333333331 226.76710605600559 L 275.0 207.64399357176711 L 279.16666666666663 217.89743747571799 L 283.33333333333337 246.06489770100512 L 287.5 249.91591319825847 L 291.66666666666663 261.28166789281715 L 295.83333333333331 256.06283385511466 L 300.0 248.09213138149627 L 304.16666666666663 257.5169232644306 L 308.33333333333337 261.18729497741299 L 312.5 272.95349082864806 L 316.66666666666663 283.95179181716691 L 320.83333333333331 280.20288445395516 L 325.0 270.98258912540246 L 329.16666666666663 267.77011800611979 L 333.33333333333337 254.1527408972085 L 337.5 240.05097897678746 L 341.66666666666669 240.3580838020722 L 345.83333333333337 247.15812973348278 L 350.0 259.22253904005453 L 354.16666666666663 275.37454467322658 L 358.33333333333337 272.79794171083955 L 362.5 275.14818172828058 L 366.66666666666663 245.62137717437497 L 370.83333333333337 243.28126446112293 L 375.0 261.74739367644941 L 379.16666666666663 241.7387767393472 L 383.33333333333331 270.23543535226969 L 387.5 287.86074330334009 L 391.66666666666663 282.24300147740286 L 395.83333333333337 281.76420431615611 L 400.0 263.80117044177166 L 404.16666666666669 282.81248015725311 L 408.33333333333337 298.37294473346515 L 412.5 305.73345529481674 L 416.66666666666663 310.68478410567718 L 420.83333333333337 329.37318351209052 L 425.0 325.84963942837453 L 429.16666666666663 333.22404654399139 L 433.33333333333337 352.55525002244008 L 437.5 364.05495727088424 L 441.66666666666663 348.37457801906066 L 445.83333333333331 353.55743674499024 L 450.0 355.06708849723145 L 454.16666666666663 342.30984359129957 L 458.33333333333337 337.71342995030278 L 462.5 351.31804641776876" style="fill:none;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 354.77033441191327 L 54.166666666666671 362.51295634767934 L 58.333333333333329 359.70115002112965 L 62.5 366.78444932206384 L 66.666666666666671 351.7386791788702 L 70.833333333333343 361.81084960525374 L 75.0 368.25805077148556 L 79.166666666666671 366.60249458765554 L 83.333333333333329 339.96810326005061 L 87.5 328.58543235258861 L 91.666666666666657 320.93668667951698 L 95.833333333333329 327.6798624543041 L 100.0 312.82003332898137 L 104.16666666666666 283.50930129277123 L 108.33333333333334 262.99888126806991 L 112.5 248.52672038428932 L 116.66666666666666 237.67082694428206 L 120.83333333333334 246.16773054639313 L 125.0 239.50809308714045 L 129.16666666666666 229.47011222743348 L 133.33333333333331 232.54880794237087 L 137.5 205.72731602293013 L 141.66666666666666 199.46245344035464 L 145.83333333333334 186.6833732322298 L 150.0 182.9293347506179 L 154.16666666666669 210.48549594173144 L 158.33333333333334 215.07524519971196 L 162.5 215.57929559225565 L 166.66666666666669 199.5996094037464 L 170.83333333333331 195.56372942475764 L 175.0 193.23858092156578 L 179.16666666666669 188.49808365455428 L 183.33333333333331 189.95288748308081 L 187.5 199.33201982154847 L 191.66666666666669 215.60059218358109 L 195.83333333333334 211.53287878921628 L 200.0 202.96056056190517 L 204.16666666666669 164.73811301684827 L 208.33333333333331 158.63460569439215 L 212.5 148.87486934088352 L 216.66666666666666 151.94171464422348 L 220.83333333333331 144.46411347709471 L 225.0 132.06130338925726 L 229.16666666666669 145.66712774613623 L 233.33333333333331 163.8972038000843 L 237.5 147.54347083397474 L 241.66666666666669 130.80909691922849 L 245.83333333333331 124.81363428645355 L 250.0 136.10233863102579 L 254.16666666666669 131.41487184626877 L 258.33333333333337 105.41834942597012 L 262.5 127.99819965243159 L 266.66666666666669 146.43244525805551 L 270.83333333333331 144.03110053902014 L 275.0 143.30084225032942 L 279.16666666666663 159.85930913346309 L 283.33333333333337 170.57472417767138 L 287.5 162.37123183784925 L 291.66666666666663 168.53881734814186 L 295.83333333333331 178.56957613112525 L 300.0 157.11545226356651 L 304.16666666666663 153.64542710323923 L 308.33333333333337 148.71436131320451 L 312.5 136.26460793288078 L 316.66666666666663 131.52293439720304 L 320.83333333333331 116.22033075432982 L 325.0 110.60784866748736 L 329.16666666666663 84.205461730499479 L 333.33333333333337 90.124601504532279 L 337.5 84.179357755040385 L 341.66666666666669 83.180172361328204 L 345.83333333333337 91.46935416047765 L 350.0 95.11909285797222 L 354.16666666666663 104.25634235853316 L 358.33333333333337 101.16758665370924 L 362.5 87.128647407800642 L 366.66666666666663 86.130182283721723 L 370.83333333333337 77.928649714607459 L 375.0 72.443963917476765 L 379.16666666666663 75.508362863720151 L 383.33333333333331 81.491765103496107 L 387.5 85.898818437179017 L 391.66666666666663 117.78663632742098 L 395.83333333333337 96.174543278645956 L 400.0 94.638435471747229 L 404.16666666666669 97.82301019924212 L 408.33333333333337 114.33537778809918 L 412.5 89.368791830650281 L 416.66666666666663 93.505150417305572 L 420.83333333333337 94.2490097409013 L 425.0 88.323065275542859 L 429.16666666666663 76.467535972672707 L 433.33333333333337 85.076754378176915 L 437.5 70.036823220617237 L 441.66666666666663 68.924589242499962 L 445.83333333333331 50.0 L 450.0 50.007330987390645 L 454.16666666666663 54.272751793583936 L 458.33333333333337 74.693721143896568 L 462.5 78.351784921410768" style="fill:none;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 343.270257204372 L 54.166666666666671 332.93152558489669 L 58.333333333333329 335.20741513589167 L 62.5 298.69723345990985 L 66.666666666666671 321.68274366909338 L 70.833333333333343 322.28633329946229 L 75.0 302.16635981529993 L 79.166666666666671 293.43531420287258 L 83.333333333333329 290.4428646260651 L 87.5 313.55834810021321 L 91.666666666666657 308.95915693476269 L 95.833333333333329 315.6502152210291 L 100.0 312.64003228943881 L 104.16666666666666 298.61053236634621 L 108.33333333333334 298.27567895190816 L 112.5 301.5025230037815 L 116.66666666666666 288.26597175013922 L 120.83333333333334 288.41873824839496 L 125.0 297.66969902472539 L 129.16666666666666 310.88357685370181 L 133.33333333333331 296.67510960989694 L 137.5 283.01590027111109 L 141.66666666666666 272.64010723451207 L 145.83333333333334 270.1492488980665 L 150.0 280.43263924027326 L 154.16666666666669 284.39922959717967 L 158.33333333333334 257.79173088398954 L 162.5 254.99452860986065 L 166.66666666666669 243.99644180780155 L 170.83333333333331 249.06325098242235 L 175.0 245.91627513569131 L 179.16666666666669 241.50846151412838 L 183.33333333333331 239.90677401226057 L 187.5 239.7299523187088 L 191.66666666666669 241.37087872692527 L 195.83333333333334 237.06520564344459 L 200.0 217.5997837429461 L 204.16666666666669 217.22570018046861 L 208.33333333333331 214.76167775706574 L 212.5 208.18122256090038 L 216.66666666666666 203.90868236811809 L 220.83333333333331 195.54575673972263 L 225.0 186.91895480219569 L 229.16666666666669 188.60738510916852 L 233.33333333333331 202.48136297042362 L 237.5 202.46045088049704 L 241.66666666666669 213.26344647501796 L 245.83333333333331 206.94565444694402 L 250.0 200.48618385440631 L 254.16666666666669 213.12887546202899 L 258.33333333333337 218.26115651945366 L 262.5 197.22582826370387 L 266.66666666666669 201.43890579194772 L 270.83333333333331 206.98432566043601 L 275.0 224.47971747542726 L 279.16666666666663 224.36271471038083 L 283.33333333333337 212.53065015144347 L 287.5 183.35554294910435 L 291.66666666666663 165.24936163132233 L 295.83333333333331 160.89798351092551 L 300.0 146.5924281554928 L 304.16666666666663 131.26085171180307 L 308.33333333333337 125.95297978051225 L 312.5 127.96438738389683 L 316.66666666666663 93.577785271234632 L 320.83333333333331 74.081696411235754 L 325.0 89.086277780962135 L 329.16666666666663 105.63217693639234 L 333.33333333333337 96.695966474577247 L 337.5 110.68850041623887 L 341.66666666666669 118.31278902786281 L 345.83333333333337 116.24758785121793 L 350.0 135.08240885112522 L 354.16666666666663 131.54090350089555 L 358.33333333333337 143.04500583264456 L 362.5 165.78947916358806 L 366.66666666666663 140.76367414179563 L 370.83333333333337 157.9159998651096 L 375.0 149.6859354082344 L 379.16666666666663 158.26922906931321 L 383.33333333333331 136.22635898886122 L 387.5 136.96873024099727 L 391.66666666666663 111.15427385126755 L 395.83333333333337 115.00322443842217 L 400.0 111.69607640811086 L 404.16666666666669 117.76453097382156 L 408.33333333333337 103.0571306542233 L 412.5 126.01093874713544 L 416.66666666666663 135.59916724031791 L 420.83333333333337 146.88874964209592 L 425.0 140.85904499131675 L 429.16666666666663 153.08473263311458 L 433.33333333333337 147.88887284616609 L 437.5 140.02465874223913 L 441.66666666666663 154.56630759612895 L 445.83333333333331 153.23151491103692 L 450.0 151.71029605375409 L 454.16666666666663 164.98858741737456 L 458.33333333333337 167.54688077804965 L 462.5 140.62154342395206" style="fill:none;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 353.50801219897482 L 54.166666666666671 365.3778770235416 L 58.333333333333329 359.86507697050081 L 62.5 376.43806786157836 L 66.666666666666671 378.41412321708759 L 70.833333333333343 384.02989326414126 L 75.0 369.91078134801097 L 79.166666666666671 350.36860967118105 L 83.333333333333329 334.91423395541307 L 87.5 328.27449838154701 L 91.666666666666657 340.6574406645118 L 95.833333333333329 323.05824843630006 L 100.0 315.54746745634651 L 104.16666666666666 323.44502100896597 L 108.33333333333334 332.33219238074071 L 112.5 334.91965229781061 L 116.66666666666666 326.28585432170178 L 120.83333333333334 320.8143275266969 L 125.0 344.79715470963191 L 129.16666666666666 356.48082929905434 L 133.33333333333331 365.96943182911554 L 137.5 366.75898408944215 L 141.66666666666666 362.34728190883146 L 145.83333333333334 358.44400546942296 L 150.0 361.29446177505241 L 154.16666666666669 364.85940072167216 L 158.33333333333334 358.08778795878618 L 162.5 358.21726742196063 L 166.66666666666669 363.92262767564677 L 170.83333333333331 358.4950277319773 L 175.0 371.77268302409925 L 179.16666666666669 375.25878627267497 L 183.33333333333331 355.47850899762477 L 187.5 371.77484442590384 L 191.66666666666669 392.28827198359846 L 195.83333333333334 370.45384525542505 L 200.0 377.83464202877371 L 204.16666666666669 379.46860653509168 L 208.33333333333331 356.06894011527044 L 212.5 362.73582334357798 L 216.66666666666666 371.34963992164899 L 220.83333333333331 362.52074214595893 L 225.0 364.79192690569238 L 229.16666666666669 359.60938056661342 L 233.33333333333331 364.13770900863432 L 237.5 374.0784879733659 L 241.66666666666669 369.78281012084329 L 245.83333333333331 365.30795471654261 L 250.0 381.19581328741276 L 254.16666666666669 390.35054126370926 L 258.33333333333337 413.23608454817952 L 262.5 408.86673709709578 L 266.66666666666669 406.84124240569156 L 270.83333333333331 411.09416551944304 L 275.0 418.4052823779349 L 279.16666666666663 417.3737120139462 L 283.33333333333337 424.46851671438429 L 287.5 408.77135624072099 L 291.66666666666663 424.50150652525826 L 295.83333333333331 442.02043399613717 L 300.0 413.15252752113844 L 304.16666666666663 432.70505432920243 L 308.33333333333337 447.6600836791967 L 312.5 441.28851011814396 L 316.66666666666663 434.99374631190466 L 320.83333333333331 424.56720233501886 L 325.0 420.3328218949365 L 329.16666666666663 422.95137132011342 L 333.33333333333337 429.08126766240764 L 337.5 437.88526504039771 L 341.66666666666669 418.39834131938539 L 345.83333333333337 421.6098760476923 L 350.0 414.13788923419531 L 354.16666666666663 386.95547922127616 L 358.33333333333337 390.05755704578843 L 362.5 388.878677504488 L 366.66666666666663 382.14315987351125 L 370.83333333333337 400.62177276136811 L 375.0 393.8298991017179 L 379.16666666666663 386.14858802327007 L 383.33333333333331 401.1461462742127 L 387.5 419.21483855999196 L 391.66666666666663 425.27090569521374 L 395.83333333333337 430.20558398431405 L 400.0 452.88110080945421 L 404.16666666666669 452.6034619992646 L 408.33333333333337 462.32994154520418 L 412.5 460.29398658661523 L 416.66666666666663 469.30031305114034 L 420.83333333333337 498.860068055098 L 425.0 488.32299041814258 L 429.16666666666663 475.18786309477514 L 433.33333333333337 482.16840011127033 L 437.5 502.16606319805629 L 441.66666666666663 501.68083655109797 L 445.83333333333331 504.35303533194087 L 450.0 505.91963772407354 L 454.16666666666663 503.62244209220103 L 458.33333333333337 531.1291937870343 L 462.5 544.07114624505937" style="fill:none;stroke:rgb(65.1%,84.7%,32.9%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g><g class="toyplot-mark-Text" id="t093714a41ab24db7bb2cf9d1a9a80d52" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="5px" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:12px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 462.5, 235.49461597775218)" x="462.5" y="235.49461597775218">Series 0</text></g></g><g class="toyplot-mark-Text" id="t4e16a46c0daa4b6fa7946c7b66c7db16" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="5px" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:12px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 462.5, 351.31804641776876)" x="462.5" y="351.31804641776876">Series 1</text></g></g><g class="toyplot-mark-Text" id="tb2443abfe58f47c49fbb3ec117dbdf2d" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="5px" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:12px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 462.5, 78.351784921410768)" x="462.5" y="78.351784921410768">Series 2</text></g></g><g class="toyplot-mark-Text" id="t3e399c8b263d49dcb1bcf3b23d2ed735" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="5px" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:12px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 462.5, 140.62154342395206)" x="462.5" y="140.62154342395206">Series 3</text></g></g><g class="toyplot-mark-Text" id="t3602eed1df5b479294dc35585b41f8ca" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" dx="5px" style="-toyplot-anchor-shift:5px;alignment-baseline:middle;fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-size:12px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="rotate(-0.0, 462.5, 544.07114624505937)" x="462.5" y="544.07114624505937">Series 4</text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="tc11bcdace9a84188950aa74f26ad3f92" transform="translate(50.0,560.0) rotate(0.0)"><line style="" x1="0" x2="412.5" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(166.66666666666666,0) rotate(0)" x="0" y="0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(333.3333333333333,0) rotate(0)" x="0" y="0">80</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">120</text></g></g><g class="toyplot-axes-Axis" id="t32589c87b8bc4421b214fbe208edfdd4" transform="translate(40.0,550.0) rotate(-90.0)"><line style="" x1="5.928853754940725" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(63.05419017763426,0) rotate(0)" x="0" y="0">-10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(198.89131000518466,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(334.7284298327351,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(470.5655496602855,0) rotate(0)" x="0" y="0">20</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tde079d87a64740fb9194a27a09cfb256 text");
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
          var text = document.querySelectorAll("#tde079d87a64740fb9194a27a09cfb256 text");
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
      var data_tables = [{"data": [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0], [0.5214351637324931, -0.6195405309739713, 0.8631664374521261, 0.6005145413604132, -0.07007419200459841, 0.8670887483031402, 1.7766771620205568, 1.190153657603208, 1.255850029717637, -0.9368349244677687, 0.2632008002520494, 1.3051468225947271, 2.3084709507071572, 0.3372161305121868, 0.05313876470408979, 0.10525712938757628, 0.5607105409577673, 0.8998024819378025, 2.2709606740671884, 0.7740551208379483, 0.6214087962087664, 0.015439452069832549, 0.2588608285401908, 0.8622997394969327, 2.2304512936770697, 1.8111460089711702, 2.536700094093551, 0.7696728675033542, 0.6365643273243555, 1.745533514895506, 1.3976932866955147, 1.785130940309487, 2.882709513202209, 3.978647768829874, 4.892365060514713, 4.820273485667039, 4.994986439435255, 4.722191633826959, 5.613866346823101, 8.054826862286134, 8.18102645012337, 7.664580519658414, 7.750722456342487, 5.725744855652458, 6.023537055401005, 5.176380270961306, 5.0895854376999585, 5.157874629049178, 5.963288611447313, 6.228557192416756, 7.119565987348147, 5.723755910303841, 4.371782628802997, 4.320864428854083, 3.822621979667228, 3.728002471297844, 4.132022803497081, 4.146509778218941, 4.762248084281536, 6.3579068889070935, 5.433670555139778, 5.413325678035675, 5.77129453325171, 5.61279577014583, 6.696596502701329, 4.346142868889033, 6.426746489727833, 5.334115200705069, 5.59599858748277, 6.350719211799879, 5.615284000036682, 6.12734373719873, 6.881571962660905, 7.455079930554715, 6.5788256170244885, 8.636668567802488, 8.913631109673384, 7.8109720004224314, 8.492951446231562, 8.582464132924928, 9.096856457975823, 5.583339797351088, 6.954445412821293, 7.157075965025828, 7.371605507958226, 6.991509817081739, 7.80887855283415, 8.843798394744047, 9.16463424357085, 10.606620437017257, 10.736462750025886, 10.386498169329364, 9.408647610647458, 8.87392939938667, 9.740523325934511, 9.708576274107847, 9.413810259853202, 9.992098405150596, 8.973109621670464, 8.511228312543649], [0.3412053597430635, 0.9577390560966359, 1.511330815207839, 1.8466264999896962, 2.380914612739446, 3.7943961251655915, 3.0632908415401996, 2.645273175202714, 3.919847530328888, 2.6887392551848457, 3.6142147594591703, 1.9534994354296413, 1.5527343322933669, 2.351898138212432, 2.1979652721111806, 2.0657898604454465, 2.796445864826903, 1.0279468744352886, 1.1250185097609997, 1.569862719088204, 1.3714306647073573, 0.8037240167103407, 0.17084002026100675, 0.6570976246019236, -0.9959151495113143, -0.5522045503726491, -0.9815285539481464, -1.2305448469142268, -0.4864415592354625, 0.24218811447439403, 0.5317441094782909, 0.7329707387727407, 1.5990979721327816, 3.5426324397289823, 4.232265202922685, 3.3202363710174936, 1.2849707288973837, 3.2652174963629594, 1.5798686218925668, 2.8402523267970814, 3.687687746224955, 3.357876962177576, 4.1104391861791765, 3.3100929145240614, 4.53690536462899, 4.062569261996534, 4.813476992912138, 5.847665063634553, 5.775936654967732, 8.19170528380777, 8.737848210055365, 9.584443076720317, 9.160422186594632, 9.153726470103702, 10.56152372821076, 9.806690004044057, 7.733069754951127, 7.449567314517879, 6.612847962032501, 6.99704589293151, 7.58382971783426, 6.8899993498980585, 6.6197954676571795, 5.753596606390639, 4.943928306408898, 5.219913793142653, 5.8986896196809475, 6.135183968454022, 7.137662313563144, 8.175799896156454, 8.153191582193777, 7.652588658630358, 6.764436044537254, 5.5753644819424615, 5.7650477559737565, 5.592028774091281, 7.765720662684833, 7.937994096943662, 6.578562357020893, 8.051548309793136, 5.9536932721495255, 4.656160758691771, 5.0697253154984185, 5.104973203693824, 6.4273682822400335, 5.027801673376646, 3.8822779317096754, 3.3404149585624263, 2.9759101150302367, 1.6001153815922153, 1.8595101691281393, 1.3166241652892139, -0.10649224817643343, -0.9530728634783044, 0.20127870638200818, -0.1802708091340366, -0.29140771737809545, 0.6477497766947783, 0.9861266244100437, -0.015412313159994362], [-0.2695613998402315, -0.8395544875614336, -0.6325561111147446, -1.1540114621945339, -0.04637827898991964, -0.7878670884678051, -1.2624944343962752, -1.1406163950259065, 0.8201430322512764, 1.6581077153888908, 2.221189859855883, 1.724773579582289, 2.818718235077612, 4.976503387870983, 6.486430869456276, 7.551836327268797, 8.351020928192995, 7.725499449756306, 8.215765841425036, 8.954737697751979, 8.72809157047499, 10.70262489049028, 11.163828911197506, 12.104593867370623, 12.38095709462233, 10.352339200920154, 10.014452968952979, 9.97734599898898, 11.153731821126254, 11.45084353728399, 11.622015342615532, 11.970999278157578, 11.863900141310927, 11.173431118530209, 9.975778195478975, 10.275233410631424, 10.90630673125203, 13.720150811101597, 14.169476248081173, 14.887964417286979, 14.662190688630673, 15.212673588785046, 16.12573844937567, 15.124110589910458, 13.782056512417372, 14.985978753029597, 16.21792285902883, 16.65929430745076, 15.828247215249192, 16.173327175035432, 18.087128237167935, 16.42485431269668, 15.067769766953456, 15.244550953280427, 15.298310801075923, 14.07931654500253, 13.29047362358224, 13.89439487502196, 13.440352156939998, 12.701911972422119, 14.28131264690605, 14.53676750083203, 14.89978062981289, 15.81630134198119, 16.165371871575566, 17.29191251542169, 17.70508986296614, 19.648769688517984, 19.213016944235175, 19.650691400012775, 19.72424901040533, 19.11401950836105, 18.845334578783035, 18.172672385108662, 18.40005910449326, 19.433571833836425, 19.50707641972182, 20.110853397585185, 20.514622691581824, 20.28902905781414, 19.84854546633546, 19.52410886614268, 17.176604890003862, 18.7676348732818, 18.880719412239106, 18.64627872831281, 17.4306781907116, 19.26865782316735, 18.964149115097975, 18.90938799203087, 19.34564168121992, 20.218417054985295, 19.584627232554286, 20.691830563768416, 20.773710537337447, 22.166892994866387, 22.166353305317614, 21.852343349010503, 20.349001009579442, 20.07970320775928], [0.5770464509549642, 1.338158850319787, 1.1706133698293109, 3.8584045805331746, 2.1662669499382092, 2.121832142196765, 3.603015894451329, 4.245774341001998, 4.466071236328286, 2.7643652885362617, 3.1029466108794694, 2.61036709397269, 2.8319694759586853, 3.86478730520179, 3.889438403139021, 3.651885953854913, 4.626328821198279, 4.615082521331964, 3.934049178746758, 2.9612754740516154, 4.007268444297368, 5.0128263769248225, 5.7766671481198655, 5.960038110313987, 5.202999801841174, 4.910989019961959, 6.869768678053146, 7.075691939506273, 7.885344471599235, 7.512338243179987, 7.7440109885036685, 8.068503559250072, 8.186415916630828, 8.19943310175491, 8.078632071057287, 8.395605302597154, 9.82860255145008, 9.856141677938654, 10.03753704516457, 10.521974230266801, 10.8365082985838, 11.452166642857625, 12.087250922359349, 11.962952769607261, 10.941584098152171, 10.943123595599788, 10.147833206033544, 10.612933764415125, 11.088464355812983, 10.157739998312397, 9.779913888340378, 11.328483843478915, 11.018327272609888, 10.610086883272395, 9.322118481321425, 9.330731941706553, 10.201779897814468, 12.34958067858616, 13.682513925460682, 14.002851851200054, 15.055992213244986, 16.18466576456539, 16.575418449695157, 16.42734349007159, 18.958801912947244, 20.39405678913645, 19.28945582374678, 18.0713867733697, 18.72924895957918, 17.699152476421588, 17.137870801625827, 17.289905913918158, 15.90333197714604, 16.164049029651697, 15.317144858954185, 13.642751779962351, 15.485090976609294, 14.222378270017064, 14.828255696402689, 14.196374390911558, 15.819117136667362, 15.764465561819597, 17.664863363429497, 17.381512936680096, 17.624977170499967, 17.178232232635057, 18.260955448370918, 16.57115165084836, 15.865289475225453, 15.034177742577517, 15.478070005490192, 14.578044470693909, 14.960551092856159, 15.539495501712207, 14.468974507719482, 14.56723871464514, 14.679227165166918, 13.70171149194905, 13.513376126481724, 15.49555429606307], [-0.17663229367683592, -1.050463013853759, -0.6446240163809387, -1.8646874947672272, -2.010159907463986, -2.4235793066814493, -1.3841644593955986, 0.0544829222361185, 1.1921966587602597, 1.6809979217946505, 0.7693956809134145, 2.0650056180612606, 2.617931135731893, 2.036532357353374, 1.3822803102651138, 1.1917977735067715, 1.8273970844366292, 2.2301976445450356, 0.46463995211294984, -0.39548389358219205, -1.0940118469212514, -1.1521367734015144, -0.8273579363493466, -0.5400081718399214, -0.74985186620331, -1.0122940433597098, -0.5137843008473031, -0.5233162655517036, -0.9433310789494903, -0.5437643073218248, -1.5212331544954376, -1.7778716383650484, -0.3216954988707805, -1.5213922716651334, -3.031541160550366, -1.4241435099013435, -1.9674999048778317, -2.087788417207332, -0.3651616087526257, -0.8559614164025009, -1.4900897451690853, -0.8401276591870923, -1.0073267843317304, -0.6258002659795775, -0.9591648461304054, -1.6909809342035165, -1.37474352737568, -1.0453155028429428, -2.214941198016713, -2.8888901147722175, -4.573668422316152, -4.252007637942128, -4.102895620993038, -4.415985527430296, -4.954212255718815, -4.878270542194683, -5.4005728929398416, -4.24498593014268, -5.403001522972327, -6.692702562947243, -4.567517156215461, -6.006926857546471, -7.107879923172435, -6.638820098498469, -6.175414822073972, -5.407837889485689, -5.096113049805784, -5.2888843209061465, -5.740152453657814, -6.388281432626669, -4.953701271787595, -5.19012668572335, -4.640057100695124, -2.638953864155063, -2.8673213257480716, -2.780535067117361, -2.2846825608563597, -3.645033318537029, -3.145032017841554, -2.5795524870476556, -3.683636427430258, -5.013809822502097, -5.4596428277152595, -5.822921900134131, -7.49223856806168, -7.471799470814765, -8.187839354337594, -8.037957277834966, -8.70098123446471, -10.877098855442297, -10.101384702320342, -9.134408419251107, -9.648298659662363, -11.120478216485534, -11.084757005113095, -11.28147781193198, -11.39680728844926, -11.227693305850918, -13.252673792020966, -14.205429009037882]], "title": "Plot Data", "names": ["x", "y0", "y1", "y2", "y3", "y4"], "id": "t63161e51cee948b0b39ddbf6d76e5657", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tde079d87a64740fb9194a27a09cfb256 .toyplot-mark-popup");
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
      var axes = {"tc2f1ab643a7d4f08aec22772d4437a99": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 120.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 22.166892994866387, "min": -14.641896873084734}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 550.0}, "scale": "linear"}]}};
    
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
the text and offsets it slightly to avoid overlapping the data.

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

    <div align="center" class="toyplot" id="t99cdfe5d681e46b4ae5b0bea156248fb"><svg height="300.0px" id="ta97a8ba0b38f4f5897038a2217d07425" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t9513056a5fe8466eb98686fd2308b130"><clipPath id="t15612fb9fbcd499bbd24b999f9336b64"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t15612fb9fbcd499bbd24b999f9336b64)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="tcbd98b50d5c345a1aec1a3ea08fd263a" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 50.0 L 54.0 58.079966680549774 L 58.0 65.993336109954186 L 62.0 73.740108288213221 L 66.0 81.320283215326938 L 70.0 88.733860891295294 L 74.0 95.980841316118301 L 78.0 103.0612244897959 L 82.0 109.97501041232817 L 86.0 116.72219908371511 L 90.0 123.30279050395669 L 94.0 129.7167846730529 L 98.0 135.96418159100375 L 102.0 142.04498125780924 L 106.0 147.9591836734694 L 110.0 153.70678883798413 L 114.0 159.2877967513536 L 118.0 164.70220741357767 L 122.0 169.95002082465641 L 126.0 175.03123698458975 L 130.0 179.94585589337777 L 134.0 184.69387755102045 L 138.0 189.27530195751768 L 142.0 193.69012911286964 L 146.0 197.93835901707621 L 150.0 202.01999167013744 L 154.0 205.93502707205329 L 158.0 209.68346522282383 L 162.0 213.265306122449 L 166.0 216.68054977092876 L 170.0 219.92919616826322 L 174.0 223.01124531445231 L 178.0 225.92669720949601 L 182.0 228.67555185339441 L 186.0 231.25780924614742 L 190.0 233.67346938775509 L 194.0 235.9225322782174 L 198.0 238.00499791753435 L 202.0 239.92086630570594 L 206.0 241.67013744273217 L 210.0 243.25281132861306 L 214.0 244.6688879633486 L 218.0 245.91836734693877 L 222.0 247.00124947938357 L 226.0 247.91753436068305 L 230.0 248.66722199083716 L 234.0 249.25031236984589 L 238.0 249.66680549770925 L 242.0 249.9167013744273 L 246.0 250.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t0521d5b2951545a4888502f1338ecc8f" transform="translate(50.0,260.0) rotate(0.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(40.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(80.0,0) rotate(0)" x="0" y="0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.0,0) rotate(0)" x="0" y="0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">50</text></g></g><g class="toyplot-axes-Axis" id="t7896381f05344396b8269690d7225827" transform="translate(40.0,250.0) rotate(-90.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="t7382d212e3b342caa490f3af4f457e40"><clipPath id="t6c21de0e20304d8b8f8803619f4b9637"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t6c21de0e20304d8b8f8803619f4b9637)" style="cursor:crosshair"><rect height="220.0" style="pointer-events:all;visibility:hidden" width="220.0" x="340.0" y="40.0"></rect><g class="toyplot-mark-Plot" id="t91ff7fdbd2af4f77b4acf356e8c5eef7" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 354.0 249.9167013744273 L 358.0 249.66680549770928 L 362.0 249.25031236984589 L 366.0 248.66722199083716 L 370.0 247.91753436068305 L 374.0 247.0012494793836 L 378.0 245.91836734693877 L 382.0 244.6688879633486 L 386.0 243.25281132861306 L 390.0 241.6701374427322 L 394.0 239.92086630570594 L 398.0 238.00499791753435 L 402.0 235.92253227821743 L 406.0 233.67346938775512 L 410.0 231.25780924614745 L 414.0 228.67555185339444 L 418.0 225.92669720949604 L 422.0 223.01124531445231 L 426.0 219.92919616826322 L 430.0 216.68054977092879 L 434.0 213.26530612244898 L 438.0 209.68346522282383 L 442.0 205.93502707205332 L 446.0 202.01999167013744 L 450.0 197.93835901707621 L 454.0 193.69012911286964 L 458.0 189.27530195751771 L 462.0 184.69387755102045 L 466.0 179.94585589337777 L 470.0 175.03123698458978 L 474.0 169.95002082465641 L 478.0 164.7022074135777 L 482.0 159.2877967513536 L 486.0 153.70678883798416 L 490.0 147.9591836734694 L 494.0 142.04498125780927 L 498.0 135.96418159100375 L 502.0 129.7167846730529 L 506.0 123.30279050395671 L 510.0 116.72219908371514 L 514.0 109.97501041232822 L 518.0 103.06122448979593 L 522.0 95.980841316118301 L 526.0 88.733860891295336 L 530.0 81.320283215326981 L 534.0 73.740108288213264 L 538.0 65.993336109954186 L 542.0 58.079966680549774 L 546.0 50.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="te393e85acf2140bd912c84d35cdcd109" transform="translate(350.0,260.0) rotate(0.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(40.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(80.0,0) rotate(0)" x="0" y="0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(120.0,0) rotate(0)" x="0" y="0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.0,0) rotate(0)" x="0" y="0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">50</text></g></g></g><g class="toyplot-mark-Text" id="td82049917f4e4b3e9448d449be0b51b3" style="alignment-baseline:middle;font-size:18px;font-weight:bold;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:18px;font-weight:bold;opacity:1.0;stroke:none;text-anchor:middle" transform="rotate(-0.0, 300.0, 120.0)" x="300.0" y="120.0">This label overlaps two sets of axes!</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t99cdfe5d681e46b4ae5b0bea156248fb text");
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
          var text = document.querySelectorAll("#t99cdfe5d681e46b4ae5b0bea156248fb text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [1.0, 0.9596001665972511, 0.920033319450229, 0.8812994585589339, 0.8433985839233653, 0.8063306955435235, 0.7700957934194085, 0.7346938775510206, 0.7001249479383591, 0.6663890045814245, 0.6334860474802165, 0.6014160766347355, 0.5701790920449812, 0.5397750937109538, 0.5102040816326531, 0.4814660558100793, 0.4535610162432321, 0.4264889629321117, 0.40024989587671805, 0.3748438150770512, 0.3502707205331112, 0.32653061224489793, 0.3036234902124116, 0.2815493544356518, 0.2603082049146189, 0.23990004164931278, 0.22032486463973353, 0.20158267388588094, 0.18367346938775514, 0.16659725114535612, 0.15035401915868396, 0.1349437734277385, 0.12036651395251982, 0.10662224073302792, 0.0937109537692628, 0.08163265306122454, 0.070387338608913, 0.05997501041232822, 0.050395668471470235, 0.04164931278633907, 0.033735943356934646, 0.026655560183256998, 0.020408163265306135, 0.014993752603082056, 0.01041232819658478, 0.006663890045814259, 0.0037484381507705204, 0.0016659725114535648, 0.0004164931278633912, 0.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "tcbd98b50d5c345a1aec1a3ea08fd263a", "filename": "toyplot"}, {"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t91ff7fdbd2af4f77b4acf356e8c5eef7", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t99cdfe5d681e46b4ae5b0bea156248fb .toyplot-mark-popup");
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
      var axes = {"t7382d212e3b342caa490f3af4f457e40": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 550.0, "min": 350.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}, "t9513056a5fe8466eb98686fd2308b130": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 250.0}, "scale": "linear"}]}};
    
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
    
    color = ["blue", "blue", "red", "red"]
    opacity = [0.1, 0.2, 0.2, 0.1]
    
    canvas = toyplot.Canvas(800, 400)
    axes = canvas.axes(grid=(1,5,0,1,0,4))
    fill = axes.fill(x, boundaries, color=color, opacity=opacity)
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

    <div align="center" class="toyplot" id="t23e01197dc284af295438523286b5514"><svg height="400.0px" id="t80e26a495f524e3a8edb2ccd40f168d1" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 800.0 400.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tb61777aa87954811a7817aeda6aed0d8"><clipPath id="td3dcbbf1274e44ab8029c1a251c01821"><rect height="320.0" width="560.0" x="40.0" y="40.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#td3dcbbf1274e44ab8029c1a251c01821)" style="cursor:crosshair"><rect height="320.0" style="pointer-events:all;visibility:hidden" width="560.0" x="40.0" y="40.0"></rect><g class="toyplot-mark-FillBoundaries" id="t33a2cdb3c50749aca1c8f82059fcaf90" style="stroke:none"><polygon points="50.0,310.529681051571 60.799999999999997,338.2127767728843 71.599999999999994,311.53553288533789 82.400000000000006,322.17043210615105 93.200000000000003,299.81448759025807 104.0,327.32054709954076 114.8,309.40794168444785 125.60000000000001,325.92889561071263 136.40000000000001,301.59217273025746 147.19999999999999,337.66827765002898 158.0,299.90161002270065 168.80000000000001,308.77621001463456 179.59999999999999,296.5515581918126 190.40000000000001,315.32993678759516 201.20000000000002,329.77175301438626 212.0,307.00969965429613 222.80000000000001,345.47755682451844 233.60000000000002,318.59512358790397 244.40000000000001,326.85811079352749 255.19999999999999,278.87555671117883 266.0,323.82687058847671 276.80000000000001,330.85065229962754 287.60000000000002,336.00266120160171 298.40000000000003,331.27306243526573 309.19999999999999,295.41680020903141 320.0,295.03772432933994 330.80000000000001,304.86771847435369 341.60000000000002,335.6064233154388 352.40000000000003,326.83055695896473 363.19999999999999,329.94017522326396 374.0,321.61215724481508 384.80000000000001,308.77566069236133 395.60000000000002,300.72983043200446 406.40000000000003,321.00130270928418 417.20000000000005,309.30492377407103 428.0,308.49798899483767 438.80000000000001,348.03081885948359 449.60000000000002,310.55874250447903 460.39999999999998,307.74029875069022 471.19999999999999,295.76300155064314 482.0,284.7102771688584 492.79999999999995,275.3166503109411 503.59999999999997,290.26400117016368 514.39999999999998,328.0829003038271 525.20000000000005,321.65636423299139 536.0,294.2297217685454 546.80000000000007,320.28285540240495 557.60000000000002,305.47084318156624 568.39999999999998,279.59350772653613 579.20000000000005,339.89354855395294 579.20000000000005,177.05982692073246 568.39999999999998,201.82453339017701 557.60000000000002,228.78252611912851 546.80000000000007,176.84007381383924 536.0,199.7288409939153 525.20000000000005,184.88343792030861 514.39999999999998,208.54701216011208 503.59999999999997,202.76496591342072 492.79999999999995,190.16132728156785 482.0,162.55399241167672 471.19999999999999,194.56945380757668 460.39999999999998,229.90878304398768 449.60000000000002,186.84959820046427 438.80000000000001,215.53837396793469 428.0,219.10523540355584 417.20000000000005,187.98427903568549 406.40000000000003,219.97172833448474 395.60000000000002,190.88017296052618 384.80000000000001,202.86048393247731 374.0,151.41944680044713 363.19999999999999,207.89318183264487 352.40000000000003,187.8578033739974 341.60000000000002,184.77875137982295 330.80000000000001,170.54211777961092 320.0,170.67416705214276 309.19999999999999,226.61981088765177 298.40000000000003,217.12879767584374 287.60000000000002,240.30611862472537 276.80000000000001,238.35762112152938 266.0,188.66478780682553 255.19999999999999,197.04064040942421 244.40000000000001,215.05635258266966 233.60000000000002,222.22761081943116 222.80000000000001,210.32526377147644 212.0,217.27390304117682 201.20000000000002,217.20607871621601 190.40000000000001,241.27848064499705 179.59999999999999,205.43639938205806 168.80000000000001,182.49110182672266 158.0,198.47441917051052 147.19999999999999,253.42408685289939 136.40000000000001,205.45636907396658 125.60000000000001,223.52641820044244 114.8,200.03385763417586 104.0,187.00994987042787 93.200000000000003,155.54598387845036 82.400000000000006,211.8253325570285 71.599999999999994,185.58703931051519 60.799999999999997,169.57578085147924 50.0,225.0809880305612" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.1;stroke:none"></polygon><polygon points="50.0,225.0809880305612 60.799999999999997,169.57578085147924 71.599999999999994,185.58703931051519 82.400000000000006,211.8253325570285 93.200000000000003,155.54598387845036 104.0,187.00994987042787 114.8,200.03385763417586 125.60000000000001,223.52641820044244 136.40000000000001,205.45636907396658 147.19999999999999,253.42408685289939 158.0,198.47441917051052 168.80000000000001,182.49110182672266 179.59999999999999,205.43639938205806 190.40000000000001,241.27848064499705 201.20000000000002,217.20607871621601 212.0,217.27390304117682 222.80000000000001,210.32526377147644 233.60000000000002,222.22761081943116 244.40000000000001,215.05635258266966 255.19999999999999,197.04064040942421 266.0,188.66478780682553 276.80000000000001,238.35762112152938 287.60000000000002,240.30611862472537 298.40000000000003,217.12879767584374 309.19999999999999,226.61981088765177 320.0,170.67416705214276 330.80000000000001,170.54211777961092 341.60000000000002,184.77875137982295 352.40000000000003,187.8578033739974 363.19999999999999,207.89318183264487 374.0,151.41944680044713 384.80000000000001,202.86048393247731 395.60000000000002,190.88017296052618 406.40000000000003,219.97172833448474 417.20000000000005,187.98427903568549 428.0,219.10523540355584 438.80000000000001,215.53837396793469 449.60000000000002,186.84959820046427 460.39999999999998,229.90878304398768 471.19999999999999,194.56945380757668 482.0,162.55399241167672 492.79999999999995,190.16132728156785 503.59999999999997,202.76496591342072 514.39999999999998,208.54701216011208 525.20000000000005,184.88343792030861 536.0,199.7288409939153 546.80000000000007,176.84007381383924 557.60000000000002,228.78252611912851 568.39999999999998,201.82453339017701 579.20000000000005,177.05982692073246 579.20000000000005,128.48497627556466 568.39999999999998,157.64044481270375 557.60000000000002,121.69759968390767 546.80000000000007,138.93886754435746 536.0,142.56214970318112 525.20000000000005,125.18499008443452 514.39999999999998,138.61850469919125 503.59999999999997,135.122525766884 492.79999999999995,148.24083868664303 482.0,121.57645881502913 471.19999999999999,119.42300581145722 460.39999999999998,133.68984404213984 449.60000000000002,122.98351294150788 438.80000000000001,160.3757240017967 428.0,153.34269168978273 417.20000000000005,122.93869975953083 406.40000000000003,144.34883140701453 395.60000000000002,131.18126715388013 384.80000000000001,161.0969219163245 374.0,117.84161019250075 363.19999999999999,132.41708933609533 352.40000000000003,126.87833060627108 341.60000000000002,128.92611777419421 330.80000000000001,99.192604650626834 320.0,121.64234098569193 309.19999999999999,150.65044425727993 298.40000000000003,112.24237881456817 287.60000000000002,171.93232772771103 276.80000000000001,141.25263443105564 266.0,131.50013489728835 255.19999999999999,142.61747646863338 244.40000000000001,131.8023045138103 233.60000000000002,141.6339874677841 222.80000000000001,138.51970410763704 212.0,145.34409852546975 201.20000000000002,127.2381706333554 190.40000000000001,163.21969573239014 179.59999999999999,139.92062057588038 168.80000000000001,124.60747233381954 158.0,145.71338218863394 147.19999999999999,153.64361006151421 136.40000000000001,140.99194501162347 125.60000000000001,141.97697973081202 114.8,155.35973589535524 104.0,126.02934940940057 93.200000000000003,116.7430320382328 82.400000000000006,161.32828917090939 71.599999999999994,117.20755508330123 60.799999999999997,117.33062760385113 50.0,152.31565851979357" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.2;stroke:none"></polygon><polygon points="50.0,152.31565851979357 60.799999999999997,117.33062760385113 71.599999999999994,117.20755508330123 82.400000000000006,161.32828917090939 93.200000000000003,116.7430320382328 104.0,126.02934940940057 114.8,155.35973589535524 125.60000000000001,141.97697973081202 136.40000000000001,140.99194501162347 147.19999999999999,153.64361006151421 158.0,145.71338218863394 168.80000000000001,124.60747233381954 179.59999999999999,139.92062057588038 190.40000000000001,163.21969573239014 201.20000000000002,127.2381706333554 212.0,145.34409852546975 222.80000000000001,138.51970410763704 233.60000000000002,141.6339874677841 244.40000000000001,131.8023045138103 255.19999999999999,142.61747646863338 266.0,131.50013489728835 276.80000000000001,141.25263443105564 287.60000000000002,171.93232772771103 298.40000000000003,112.24237881456817 309.19999999999999,150.65044425727993 320.0,121.64234098569193 330.80000000000001,99.192604650626834 341.60000000000002,128.92611777419421 352.40000000000003,126.87833060627108 363.19999999999999,132.41708933609533 374.0,117.84161019250075 384.80000000000001,161.0969219163245 395.60000000000002,131.18126715388013 406.40000000000003,144.34883140701453 417.20000000000005,122.93869975953083 428.0,153.34269168978273 438.80000000000001,160.3757240017967 449.60000000000002,122.98351294150788 460.39999999999998,133.68984404213984 471.19999999999999,119.42300581145722 482.0,121.57645881502913 492.79999999999995,148.24083868664303 503.59999999999997,135.122525766884 514.39999999999998,138.61850469919125 525.20000000000005,125.18499008443452 536.0,142.56214970318112 546.80000000000007,138.93886754435746 557.60000000000002,121.69759968390767 568.39999999999998,157.64044481270375 579.20000000000005,128.48497627556466 579.20000000000005,89.074340481298307 568.39999999999998,119.91146738650599 557.60000000000002,90.950891871367787 546.80000000000007,87.036478338539808 536.0,70.620834601355256 525.20000000000005,89.947607316021418 514.39999999999998,96.847764806814638 503.59999999999997,95.278653506029656 492.79999999999995,101.36480336145445 482.0,83.389480462862736 471.19999999999999,87.210529190832062 460.39999999999998,87.992257614330669 449.60000000000002,87.457559598057202 438.80000000000001,116.09269020114877 428.0,97.815772847468793 417.20000000000005,85.120329420649995 406.40000000000003,91.925039238860506 395.60000000000002,71.277007493618356 384.80000000000001,107.49471354764972 374.0,81.813454458909888 363.19999999999999,76.043145611353793 352.40000000000003,96.715358257914716 341.60000000000002,92.329141619479074 330.80000000000001,78.434674738007061 320.0,82.984166293581467 309.19999999999999,108.04010252234025 298.40000000000003,69.649974470033655 287.60000000000002,102.16159230534217 276.80000000000001,108.21046552975855 266.0,85.199938479626098 255.19999999999999,87.49776189938683 244.40000000000001,85.54003932554744 233.60000000000002,112.93489025261817 222.80000000000001,87.913684152134977 212.0,113.52188990105878 201.20000000000002,74.711799575190469 190.40000000000001,108.85294059319446 179.59999999999999,89.526967510911078 168.80000000000001,91.094530433425348 158.0,87.662947917859071 147.19999999999999,110.99259765503312 136.40000000000001,91.900761542854951 125.60000000000001,91.660657542630162 114.8,82.24409417811745 104.0,85.34842641054523 93.200000000000003,81.107075978725064 82.400000000000006,107.10631628950067 71.599999999999994,74.126814152566737 60.799999999999997,81.008849580508183 50.0,101.45325820175026" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.2;stroke:none"></polygon><polygon points="50.0,101.45325820175026 60.799999999999997,81.008849580508183 71.599999999999994,74.126814152566737 82.400000000000006,107.10631628950067 93.200000000000003,81.107075978725064 104.0,85.34842641054523 114.8,82.24409417811745 125.60000000000001,91.660657542630162 136.40000000000001,91.900761542854951 147.19999999999999,110.99259765503312 158.0,87.662947917859071 168.80000000000001,91.094530433425348 179.59999999999999,89.526967510911078 190.40000000000001,108.85294059319446 201.20000000000002,74.711799575190469 212.0,113.52188990105878 222.80000000000001,87.913684152134977 233.60000000000002,112.93489025261817 244.40000000000001,85.54003932554744 255.19999999999999,87.49776189938683 266.0,85.199938479626098 276.80000000000001,108.21046552975855 287.60000000000002,102.16159230534217 298.40000000000003,69.649974470033655 309.19999999999999,108.04010252234025 320.0,82.984166293581467 330.80000000000001,78.434674738007061 341.60000000000002,92.329141619479074 352.40000000000003,96.715358257914716 363.19999999999999,76.043145611353793 374.0,81.813454458909888 384.80000000000001,107.49471354764972 395.60000000000002,71.277007493618356 406.40000000000003,91.925039238860506 417.20000000000005,85.120329420649995 428.0,97.815772847468793 438.80000000000001,116.09269020114877 449.60000000000002,87.457559598057202 460.39999999999998,87.992257614330669 471.19999999999999,87.210529190832062 482.0,83.389480462862736 492.79999999999995,101.36480336145445 503.59999999999997,95.278653506029656 514.39999999999998,96.847764806814638 525.20000000000005,89.947607316021418 536.0,70.620834601355256 546.80000000000007,87.036478338539808 557.60000000000002,90.950891871367787 568.39999999999998,119.91146738650599 579.20000000000005,89.074340481298307 579.20000000000005,53.422623380005355 568.39999999999998,60.773310556639636 557.60000000000002,55.865140514994827 546.80000000000007,54.991850206354108 536.0,52.175551768501649 525.20000000000005,52.871037670537412 514.39999999999998,58.496530072993238 503.59999999999997,50.34092995630386 492.79999999999995,52.610938869473912 482.0,54.256700689130057 471.19999999999999,50.618681568852878 460.39999999999998,51.181439285457891 449.60000000000002,51.38534021504325 438.80000000000001,57.57670828613125 428.0,51.131687873893924 417.20000000000005,50.44908361918985 406.40000000000003,52.945568324263824 395.60000000000002,52.618469689206393 384.80000000000001,52.696731607616996 374.0,50.589294818836073 363.19999999999999,50.917398722232548 352.40000000000003,62.947621617268076 341.60000000000002,50.843881846332387 330.80000000000001,51.64001927826537 320.0,53.494340248533618 309.19999999999999,54.135715573816277 298.40000000000003,51.491879931203172 287.60000000000002,56.214662402403441 276.80000000000001,58.64348328426734 266.0,50.36728250280489 255.19999999999999,55.867768014243865 244.40000000000001,53.308438233906315 233.60000000000002,50.289832627880436 222.80000000000001,55.494434598347034 212.0,51.639199565123441 201.20000000000002,51.542271963665065 190.40000000000001,50.97002042212052 179.59999999999999,53.917202462575716 168.80000000000001,50.607689328977216 158.0,60.353855635465926 147.19999999999999,56.562291714500482 136.40000000000001,53.975116705867364 125.60000000000001,52.657553344212872 114.8,50.329103317890997 104.0,52.024993466368478 93.200000000000003,50.205456449904084 82.400000000000006,52.613729728947632 71.599999999999994,50.00544148255365 60.799999999999997,54.382062228934636 50.0,59.129560466391617" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.1;stroke:none"></polygon></g><g class="toyplot-mark-Plot" id="tf2b00adf3ada40488bd081d067f1705d" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 163.49667814173617 L 60.799999999999997 137.71154754170277 L 71.599999999999994 139.90158895299604 L 82.400000000000006 159.84360929778228 L 93.200000000000003 126.70521032892651 L 104.0 147.6983684190605 L 114.8 148.88918754095593 L 125.60000000000001 157.61645449104185 L 136.40000000000001 151.27347123236322 L 147.19999999999999 177.87781141943779 L 158.0 154.65045556493641 L 168.80000000000001 137.27643129769862 L 179.59999999999999 151.12810991281049 L 190.40000000000001 173.75261142071071 L 201.20000000000002 147.97965404908931 L 212.0 162.69420943878464 L 222.80000000000001 152.75929313579127 L 233.60000000000002 167.35176858608597 L 244.40000000000001 149.78294773342697 L 255.19999999999999 148.66843657840053 L 266.0 149.54757028800805 L 276.80000000000001 167.29987457499024 L 287.60000000000002 175.23121548310593 L 298.40000000000003 147.42507457048487 L 309.19999999999999 161.6073086181612 L 320.0 137.87165369464151 L 330.80000000000001 132.29775976102169 L 341.60000000000002 146.18216413484359 L 352.40000000000003 146.38168973117547 L 363.19999999999999 149.79202673056622 L 374.0 128.48147974635066 L 384.80000000000001 161.24664087699065 L 395.60000000000002 140.04812154841591 L 406.40000000000003 152.31270593570531 L 417.20000000000005 145.72459407416423 L 428.0 161.94524974279014 L 438.80000000000001 171.5237978525154 L 449.60000000000002 142.18109227494182 L 460.39999999999998 157.03757114504492 L 471.19999999999999 140.47878190760736 L 482.0 135.97458774882278 L 492.79999999999995 148.43991202910274 L 503.59999999999997 151.64646140177766 L 514.39999999999998 157.59718751604669 L 525.20000000000005 140.12905158177691 L 536.0 145.17663656436693 L 546.80000000000007 145.14638335102191 L 557.60000000000002 154.56715103662162 L 568.39999999999998 162.22660535858168 L 579.20000000000005 140.87554354633366" style="fill:none;stroke:rgb(0%,0%,100%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="490.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="535.0" y="67.0"></text></g><g class="toyplot-axes-Axis" id="t76783f067ed04ec6af7761bb5101c732" transform="translate(50.0,360.0) rotate(0.0)"><line style="" x1="0" x2="529.2" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(108.0,0) rotate(0)" x="0" y="0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(216.0,0) rotate(0)" x="0" y="0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(324.0,0) rotate(0)" x="0" y="0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(432.0,0) rotate(0)" x="0" y="0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(540.0,0) rotate(0)" x="0" y="0">50</text></g></g><g class="toyplot-axes-Axis" id="t6256ade2bb684b689d10792112a5dc4b" transform="translate(40.0,350.0) rotate(-90.0)"><line style="" x1="1.9691811405164148" x2="299.99455851744636" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><rect class="toyplot-mark-Legend" height="125.0" id="t436f12de01b94af59759b8f2aaf658da" style="fill:none;stroke:none" width="100.0" x="600.0" y="137.5"></rect><line style="fill:none;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" x1="610.0" x2="623.0" y1="160.5" y2="147.5"></line><text style="alignment-baseline:middle;stroke:none" x="633.0" y="154.0">Mean</text><rect height="13.0" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.1;stroke:none" width="13.0" x="610.0" y="170.5"></rect><text style="alignment-baseline:middle;stroke:none" x="633.0" y="177.0">First Quartile</text><rect height="13.0" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.2;stroke:none" width="13.0" x="610.0" y="193.5"></rect><text style="alignment-baseline:middle;stroke:none" x="633.0" y="200.0">Second Quartile</text><rect height="13.0" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.2;stroke:none" width="13.0" x="610.0" y="216.5"></rect><text style="alignment-baseline:middle;stroke:none" x="633.0" y="223.0">Third Quartile</text><rect height="13.0" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.1;stroke:none" width="13.0" x="610.0" y="239.5"></rect><text style="alignment-baseline:middle;stroke:none" x="633.0" y="246.0">Fourth Quartile</text></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t23e01197dc284af295438523286b5514 text");
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
          var text = document.querySelectorAll("#t23e01197dc284af295438523286b5514 text");
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
      var data_tables = [{"data": [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0], [0.13156772982809672, 0.039290744090385535, 0.12821489038220688, 0.09276522631282974, 0.16728504136580646, 0.07559817633486413, 0.13530686105184053, 0.08023701463095784, 0.16135942423247518, 0.041105741166569905, 0.16699463325766464, 0.13741263328455153, 0.17816147269395805, 0.11556687737468288, 0.06742748995204582, 0.14330100115234617, 0.015074810584938663, 0.10468292137365344, 0.0771396306882418, 0.23708147762940388, 0.08724376470507762, 0.06383115900124144, 0.046657795994660925, 0.06242312521578101, 0.1819439993032287, 0.18320758556886693, 0.1504409384188211, 0.04797858894853724, 0.07723147680345079, 0.06686608258912034, 0.09462614251728298, 0.13741446435879556, 0.16423389855998521, 0.09666232430238615, 0.1356502540864299, 0.13834003668387446, 0.006563937135054716, 0.1314708583184031, 0.14086567083103252, 0.18078999483118946, 0.21763240943713863, 0.24894449896352963, 0.19911999609945458, 0.07305699898724302, 0.09447878589002875, 0.18590092743818212, 0.0990571486586501, 0.1484305227281125, 0.2346883075782129, 0.0336881714868235], [0.41639670656479594, 0.6014140638284026, 0.5480432022982826, 0.46058222480990507, 0.6481800537384989, 0.5433001670985738, 0.4998871412194138, 0.42157860599852515, 0.481812103086778, 0.3219197104903353, 0.5050852694316316, 0.5583629939109245, 0.48187866872647306, 0.3624050645166765, 0.4426464042792799, 0.44242032319607727, 0.46558245409507865, 0.4259079639352295, 0.4498121580577679, 0.5098645319685859, 0.5377840406439148, 0.37214126292823546, 0.3656462712509155, 0.4429040077471876, 0.41126729704116083, 0.5977527764928574, 0.5981929407346303, 0.5507374954005901, 0.5404739887533421, 0.4736893938911837, 0.6619351773318429, 0.49046505355840897, 0.5303994234649128, 0.4334275722183842, 0.5400524032143817, 0.43631588198814714, 0.4482054201068843, 0.5438346726651191, 0.4003040565200411, 0.5181018206414111, 0.6248200252944109, 0.5327955757281072, 0.4907834469552642, 0.47150995946629304, 0.550388540265638, 0.5009038633536156, 0.5771997539538691, 0.40405824626957165, 0.49391822203274327, 0.5764672435975585], [0.6589478049340214, 0.7755645746538296, 0.7759748163889959, 0.6289057027636353, 0.777523226539224, 0.7465688353019981, 0.6488008803488159, 0.69341006756396, 0.6966935166279218, 0.6545212997949527, 0.6809553927045535, 0.7513084255539348, 0.7002645980803988, 0.6226010142253663, 0.7425394312221487, 0.6821863382484341, 0.7049343196412099, 0.6945533751073864, 0.7273256516206323, 0.6912750784378887, 0.7283328836757055, 0.6958245518964812, 0.5935589075742966, 0.7925254039514394, 0.6644985191424002, 0.7611921967143602, 0.8360246511645772, 0.736912940752686, 0.7437388979790964, 0.7252763688796822, 0.7738612993583308, 0.6296769269455851, 0.7293957761537329, 0.6855038953099516, 0.7568710008015639, 0.6555243610340576, 0.632080919994011, 0.7567216235283071, 0.7210338531928672, 0.7685899806284759, 0.7614118039499029, 0.6725305377111899, 0.71625824744372, 0.7046049843360291, 0.7493833663852183, 0.6914595009893962, 0.7035371081854751, 0.7610080010536411, 0.6411985172909875, 0.7383834124147844], [0.8284891393274991, 0.8966371680649727, 0.9195772861581109, 0.8096456123683311, 0.8963097467375831, 0.8821719119648492, 0.8925196860729419, 0.8611311415245662, 0.8603307948571501, 0.7966913411498896, 0.8744568402738031, 0.8630182318885822, 0.8682434416302964, 0.8038235313560185, 0.9176273347493651, 0.7882603669964707, 0.8736210528262167, 0.7902170324912727, 0.8815332022481752, 0.8750074603353772, 0.8826668717345797, 0.8059651149008048, 0.8261280256488595, 0.9345000850998878, 0.8065329915921992, 0.8900527790213951, 0.9052177508733098, 0.8589028612684031, 0.8442821391402843, 0.9131895146288207, 0.8939551518036337, 0.8083509548411676, 0.9290766416879388, 0.8602498692037983, 0.8829322352645, 0.8406140905084374, 0.7796910326628375, 0.875141468006476, 0.8733591412855645, 0.8759649026972265, 0.8887017317904575, 0.8287839887951518, 0.8490711549799012, 0.8438407839772846, 0.8668413089465953, 0.9312638846621492, 0.8765450722048673, 0.8634970270954407, 0.7669617753783133, 0.8697521983956723], [0.9695681317786946, 0.9853931259035512, 0.9999818617248212, 0.9912875675701746, 0.9993151451669864, 0.9932500217787718, 0.9989029889403633, 0.9911414888526238, 0.9867496109804421, 0.9781256942849984, 0.9654871478817802, 0.9979743689034093, 0.9869426584580809, 0.9967665985929316, 0.9948590934544498, 0.9945360014495885, 0.9816852180055099, 0.9990338912403985, 0.9889718725536456, 0.9804407732858538, 0.9987757249906504, 0.9711883890524422, 0.9792844586586552, 0.9950270668959894, 0.9862142814206124, 0.9883521991715546, 0.9945332690724488, 0.9971870605122254, 0.9568412612757731, 0.9969420042592249, 0.9980356839372131, 0.9910108946412767, 0.9912717677026454, 0.9901814389191206, 0.9985030546027005, 0.9962277070870202, 0.9747443057128958, 0.9953821992831892, 0.9960618690484737, 0.9979377281038238, 0.9858109977028998, 0.991296870435087, 0.9988635668123205, 0.9716782330900225, 0.990429874431542, 0.9927481607716612, 0.983360499312153, 0.9804495316166839, 0.9640889648112012, 0.9885912553999822]], "title": "Fill Data", "names": ["x", "y0", "y1", "y2", "y3", "y4"], "id": "t33a2cdb3c50749aca1c8f82059fcaf90", "filename": "toyplot"}, {"data": [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0], [0.6216777395275461, 0.7076281748609907, 0.7003280368233465, 0.6338546356740591, 0.7443159655702449, 0.674338771936465, 0.6703693748634802, 0.6412784850298605, 0.6624217625587893, 0.573740628601874, 0.6511651481168786, 0.7090785623410046, 0.6629063002906317, 0.5874912952642977, 0.6734011531697023, 0.6243526352040513, 0.6574690228806958, 0.6088274380463801, 0.6673901742219102, 0.6711052114053315, 0.6681747657066398, 0.6090004180833659, 0.5825626150563136, 0.6752497514317171, 0.6279756379394626, 0.7070944876845283, 0.7256741341299277, 0.679392786217188, 0.6787277008960818, 0.6673599108981126, 0.7383950675121644, 0.6291778637433645, 0.6998395948386137, 0.6589576468809824, 0.6809180197527859, 0.6268491675240329, 0.5949206738249487, 0.6927296924168607, 0.6432080961831835, 0.6984040603079754, 0.7134180408372574, 0.6718669599029908, 0.6611784619940745, 0.6413427082798444, 0.6995698280607436, 0.6827445447854436, 0.682845388829927, 0.6514428298779279, 0.6259113154713943, 0.6970815215122211]], "title": "Plot Data", "names": ["x", "y0"], "id": "tf2b00adf3ada40488bd081d067f1705d", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t23e01197dc284af295438523286b5514 .toyplot-mark-popup");
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
      var axes = {"tb61777aa87954811a7817aeda6aed0d8": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 590.0, "min": 50.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 50.0, "min": 350.0}, "scale": "linear"}]}};
    
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
    m1 = canvas.axes(grid=(1,2,0), gutter=25).scatterplot(x, y1, marker="o", color="rgb(255,0,0)")
    m2 = canvas.axes(grid=(1,2,1), gutter=25, yshow=False).scatterplot(x, y2, marker="s", color=["green", "blue"])
    
    canvas.legend([
        ("Experiment 1", "o", {"fill":"rgb(255,0,0)", "stroke": "none"}),
        ("Experiment 2", "s", {"fill":"green", "stroke": "none"}),
        ("Experiment 3", "s", {"fill":"blue", "stroke": "none"}),
    
        ],
        corner=("top", 100, 100, 70),
        );
    




.. raw:: html

    <div align="center" class="toyplot" id="tdf709b8d460641dca59c46c1a8884653"><svg height="300.0px" id="t3075f53b7bb145aa830449b893d05402" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t697877bdb802484da072009c1f319758"><clipPath id="t03dc60632e52499f99bf250e866983ee"><rect height="270.0" width="270.0" x="15.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t03dc60632e52499f99bf250e866983ee)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="15.0" y="15.0"></rect><g class="toyplot-mark-Scatterplot" id="td00df82e73164d109a1a4a8233ea9345" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="25.0" cy="25.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="30.102040816326529" cy="35.099958350687224" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="35.204081632653057" cy="44.991670137442739" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="40.306122448979593" cy="54.675135360266523" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="45.408163265306122" cy="64.150354019158669" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="50.510204081632651" cy="73.41732611411912" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="55.612244897959179" cy="82.476051645147891" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="60.714285714285715" cy="91.326530612244852" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="65.816326530612244" cy="99.968763015410218" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="70.918367346938766" cy="108.40274885464387" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="76.020408163265301" cy="116.62848812994588" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="81.122448979591823" cy="124.64598084131613" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="86.224489795918359" cy="132.4552269887547" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="91.326530612244895" cy="140.05622657226155" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="96.428571428571431" cy="147.44897959183672" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="101.53061224489795" cy="154.6334860474802" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="106.63265306122449" cy="161.60974593919198" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="111.73469387755101" cy="168.37775926697208" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="116.83673469387755" cy="174.93752603082049" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="121.93877551020408" cy="181.2890462307372" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="127.0408163265306" cy="187.4323198667222" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="132.14285714285714" cy="193.36734693877551" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="137.24489795918365" cy="199.09412744689712" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="142.34693877551018" cy="204.61266139108704" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="147.44897959183672" cy="209.92294877134526" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="152.55102040816328" cy="215.0249895876718" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="157.65306122448979" cy="219.9187838400666" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="162.75510204081633" cy="224.60433152852977" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="167.85714285714286" cy="229.08163265306123" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="172.9591836734694" cy="233.35068721366096" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="178.0612244897959" cy="237.41149521032901" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="183.16326530612244" cy="241.26405664306537" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="188.26530612244895" cy="244.90837151187003" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="193.36734693877548" cy="248.34443981674301" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="198.46938775510202" cy="251.5722615576843" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="203.57142857142856" cy="254.59183673469386" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="208.67346938775509" cy="257.40316534777173" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="213.77551020408163" cy="260.00624739691796" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="218.87755102040816" cy="262.40108288213241" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="223.97959183673467" cy="264.58767180341522" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="229.08163265306121" cy="266.56601416076637" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="234.18367346938774" cy="268.33610995418576" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="239.28571428571428" cy="269.89795918367344" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="244.38775510204081" cy="271.25156184922946" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="249.48979591836729" cy="272.39691795085383" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="254.59183673469386" cy="273.33402748854644" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="259.69387755102036" cy="274.06289046230739" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="264.79591836734693" cy="274.58350687213658" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="269.89795918367344" cy="274.89587671803417" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0"><circle cx="275.0" cy="275.0" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="175.0" y="35.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="220.0" y="42.0"></text></g><g class="toyplot-axes-Axis" id="t2724e848128844a29b159d78570f920d" transform="translate(25.0,285.0) rotate(0.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1.0</text></g></g><g class="toyplot-axes-Axis" id="tb85194a96aa64171b9fa1c50ac016e89" transform="translate(15.0,275.0) rotate(-90.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-Cartesian" id="t5f821d702d614d7e9a6cb84c9417e96e"><clipPath id="t4f5547dfc0214b6d99d55a453d40084d"><rect height="270.0" width="270.0" x="315.0" y="15.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t4f5547dfc0214b6d99d55a453d40084d)" style="cursor:crosshair"><rect height="270.0" style="pointer-events:all;visibility:hidden" width="270.0" x="315.0" y="15.0"></rect><g class="toyplot-mark-Scatterplot" id="t3d317cccfad446c39f9d155a3c18ccb0" style="stroke:none"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 325.0, 25.0)" width="4.4721359549995796" x="322.76393202250023" y="22.76393202250021"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 330.10204081632651, 25.104123281965848)" width="4.4721359549995796" x="327.86597283882674" y="22.868055304466058"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 335.20408163265307, 25.416493127863376)" width="4.4721359549995796" x="332.9680136551533" y="23.180425150363586"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 340.30612244897964, 25.937109537692631)" width="4.4721359549995796" x="338.07005447147986" y="23.701041560192841"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 345.40816326530614, 26.665972511453564)" width="4.4721359549995796" x="343.17209528780637" y="24.429904533953774"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 350.51020408163265, 27.603082049146195)" width="4.4721359549995796" x="348.27413610413288" y="25.367014071646405"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 355.61224489795916, 28.7484381507705)" width="4.4721359549995796" x="353.37617692045939" y="26.51237017327071"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 360.71428571428578, 30.102040816326536)" width="4.4721359549995796" x="358.47821773678601" y="27.865972838826746"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 365.81632653061229, 31.663890045814245)" width="4.4721359549995796" x="363.58025855311251" y="29.427822068314455"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 370.91836734693874, 33.433985839233657)" width="4.4721359549995796" x="368.68229936943897" y="31.197917861733867"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 376.0204081632653, 35.412328196584745)" width="4.4721359549995796" x="373.78434018576553" y="33.176260219084952"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 381.12244897959181, 37.598917117867565)" width="4.4721359549995796" x="378.88638100209204" y="35.362849140367771"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 386.22448979591832, 39.993752603082058)" width="4.4721359549995796" x="383.98842181841854" y="37.757684625582272"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 391.32653061224494, 42.596834652228225)" width="4.4721359549995796" x="389.09046263474517" y="40.360766674728438"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 396.42857142857144, 45.408163265306115)" width="4.4721359549995796" x="394.19250345107167" y="43.172095287806329"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 401.53061224489795, 48.427738442315686)" width="4.4721359549995796" x="399.29454426739818" y="46.1916704648159"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 406.63265306122452, 51.655560183256959)" width="4.4721359549995796" x="404.39658508372474" y="49.419492205757166"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 411.73469387755108, 55.091628488129928)" width="4.4721359549995796" x="409.49862590005131" y="52.855560510630141"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 416.83673469387753, 58.735943356934612)" width="4.4721359549995796" x="414.60066671637776" y="56.499875379434826"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 421.9387755102041, 62.588504789670964)" width="4.4721359549995796" x="419.70270753270432" y="60.352436812171177"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 427.0408163265306, 66.64931278633901)" width="4.4721359549995796" x="424.80474834903083" y="64.413244808839224"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 432.14285714285711, 70.918367346938766)" width="4.4721359549995796" x="429.90678916535734" y="68.682299369438979"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 437.24489795918362, 75.395668471470202)" width="4.4721359549995796" x="435.00882998168385" y="73.159600493970416"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 442.34693877551018, 80.081216159933362)" width="4.4721359549995796" x="440.11087079801041" y="77.845148182433576"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 447.44897959183675, 84.975010412328189)" width="4.4721359549995796" x="445.21291161433697" y="82.738942434828402"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 452.55102040816325, 90.077051228654724)" width="4.4721359549995796" x="450.31495243066348" y="87.840983251154938"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 457.65306122448976, 95.387338608912941)" width="4.4721359549995796" x="455.41699324698999" y="93.151270631413155"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 462.75510204081633, 100.90587255310285)" width="4.4721359549995796" x="460.51903406331655" y="98.669804575603067"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 467.85714285714289, 106.63265306122446)" width="4.4721359549995796" x="465.62107487964312" y="104.39658508372467"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 472.9591836734694, 112.5676801332778)" width="4.4721359549995796" x="470.72311569596962" y="110.33161215577802"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 478.0612244897959, 118.71095376926277)" width="4.4721359549995796" x="475.82515651229613" y="116.47488579176299"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 483.16326530612241, 125.06247396917951)" width="4.4721359549995796" x="480.92719732862264" y="122.82640599167972"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 488.26530612244898, 131.62224073302789)" width="4.4721359549995796" x="486.0292381449492" y="129.38617275552809"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 493.36734693877554, 138.39025406080799)" width="4.4721359549995796" x="491.13127896127577" y="136.15418608330819"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 498.46938775510205, 145.36651395251977)" width="4.4721359549995796" x="496.23331977760228" y="143.13044597501997"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 503.57142857142856, 152.55102040816323)" width="4.4721359549995796" x="501.33536059392878" y="150.31495243066342"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 508.67346938775506, 159.94377342773842)" width="4.4721359549995796" x="506.43740141025529" y="157.70770545023862"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 513.77551020408157, 167.5447730112453)" width="4.4721359549995796" x="511.5394422265818" y="165.3087050337455"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 518.87755102040819, 175.35401915868388)" width="4.4721359549995796" x="516.64148304290836" y="173.11795118118408"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 523.9795918367347, 183.37151187005409)" width="4.4721359549995796" x="521.74352385923487" y="181.13544389255429"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 529.08163265306121, 191.59725114535607)" width="4.4721359549995796" x="526.84556467556138" y="189.36118316785627"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 534.18367346938771, 200.03123698458973)" width="4.4721359549995796" x="531.94760549188788" y="197.79516900708992"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 539.28571428571422, 208.67346938775509)" width="4.4721359549995796" x="537.04964630821439" y="206.43740141025529"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 544.38775510204084, 217.52394835485214)" width="4.4721359549995796" x="542.15168712454101" y="215.28788037735234"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 549.48979591836735, 226.58267388588084)" width="4.4721359549995796" x="547.25372794086752" y="224.34660590838104"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 554.59183673469386, 235.84964598084127)" width="4.4721359549995796" x="552.35576875719403" y="233.61357800334147"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 559.69387755102036, 245.32486463973342)" width="4.4721359549995796" x="557.45780957352054" y="243.08879666223362"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 564.79591836734699, 255.00832986255728)" width="4.4721359549995796" x="562.55985038984716" y="252.77226188505747"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 569.89795918367338, 264.90004164931275)" width="4.4721359549995796" x="567.66189120617355" y="262.66397367181298"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 575.0, 275.0)" width="4.4721359549995796" x="572.76393202250017" y="272.76393202250023"></rect></g></g><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 325.0, 275.0)" width="4.4721359549995796" x="322.76393202250023" y="272.76393202250023"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 330.10204081632651, 274.89587671803417)" width="4.4721359549995796" x="327.86597283882674" y="272.6598087405344"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 335.20408163265307, 274.58350687213658)" width="4.4721359549995796" x="332.9680136551533" y="272.34743889463681"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 340.30612244897964, 274.06289046230739)" width="4.4721359549995796" x="338.07005447147986" y="271.82682248480762"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 345.40816326530614, 273.33402748854644)" width="4.4721359549995796" x="343.17209528780637" y="271.09795951104667"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 350.51020408163265, 272.39691795085383)" width="4.4721359549995796" x="348.27413610413288" y="270.16084997335406"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 355.61224489795916, 271.25156184922952)" width="4.4721359549995796" x="353.37617692045939" y="269.01549387172975"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 360.71428571428578, 269.89795918367344)" width="4.4721359549995796" x="358.47821773678601" y="267.66189120617366"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 365.81632653061229, 268.33610995418576)" width="4.4721359549995796" x="363.58025855311251" y="266.10004197668599"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 370.91836734693874, 266.56601416076637)" width="4.4721359549995796" x="368.68229936943897" y="264.3299461832666"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 376.0204081632653, 264.58767180341528)" width="4.4721359549995796" x="373.78434018576553" y="262.3516038259155"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 381.12244897959181, 262.40108288213241)" width="4.4721359549995796" x="378.88638100209204" y="260.16501490463264"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 386.22448979591832, 260.00624739691796)" width="4.4721359549995796" x="383.98842181841854" y="257.77017941941818"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 391.32653061224494, 257.40316534777179)" width="4.4721359549995796" x="389.09046263474517" y="255.16709737027199"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 396.42857142857144, 254.59183673469389)" width="4.4721359549995796" x="394.19250345107167" y="252.35576875719408"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 401.53061224489795, 251.57226155768433)" width="4.4721359549995796" x="399.29454426739818" y="249.33619358018453"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 406.63265306122452, 248.34443981674303)" width="4.4721359549995796" x="404.39658508372474" y="246.10837183924323"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 411.73469387755108, 244.90837151187006)" width="4.4721359549995796" x="409.49862590005131" y="242.67230353437026"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 416.83673469387753, 241.2640566430654)" width="4.4721359549995796" x="414.60066671637776" y="239.0279886655656"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 421.9387755102041, 237.41149521032904)" width="4.4721359549995796" x="419.70270753270432" y="235.17542723282924"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 427.0408163265306, 233.35068721366099)" width="4.4721359549995796" x="424.80474834903083" y="231.11461923616119"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 432.14285714285711, 229.08163265306123)" width="4.4721359549995796" x="429.90678916535734" y="226.84556467556143"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 437.24489795918362, 224.6043315285298)" width="4.4721359549995796" x="435.00882998168385" y="222.36826355103"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 442.34693877551018, 219.91878384006662)" width="4.4721359549995796" x="440.11087079801041" y="217.68271586256682"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 447.44897959183675, 215.0249895876718)" width="4.4721359549995796" x="445.21291161433697" y="212.788921610172"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 452.55102040816325, 209.92294877134526)" width="4.4721359549995796" x="450.31495243066348" y="207.68688079384546"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 457.65306122448976, 204.61266139108704)" width="4.4721359549995796" x="455.41699324698999" y="202.37659341358724"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 462.75510204081633, 199.09412744689715)" width="4.4721359549995796" x="460.51903406331655" y="196.85805946939735"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 467.85714285714289, 193.36734693877551)" width="4.4721359549995796" x="465.62107487964312" y="191.13127896127571"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 472.9591836734694, 187.4323198667222)" width="4.4721359549995796" x="470.72311569596962" y="185.1962518892224"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 478.0612244897959, 181.2890462307372)" width="4.4721359549995796" x="475.82515651229613" y="179.0529782532374"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 483.16326530612241, 174.93752603082049)" width="4.4721359549995796" x="480.92719732862264" y="172.70145805332069"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 488.26530612244898, 168.37775926697211)" width="4.4721359549995796" x="486.0292381449492" y="166.14169128947231"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 493.36734693877554, 161.60974593919201)" width="4.4721359549995796" x="491.13127896127577" y="159.37367796169221"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 498.46938775510205, 154.6334860474802)" width="4.4721359549995796" x="496.23331977760228" y="152.3974180699804"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 503.57142857142856, 147.44897959183677)" width="4.4721359549995796" x="501.33536059392878" y="145.21291161433697"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 508.67346938775506, 140.05622657226158)" width="4.4721359549995796" x="506.43740141025529" y="137.82015859476178"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 513.77551020408157, 132.4552269887547)" width="4.4721359549995796" x="511.5394422265818" y="130.2191590112549"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 518.87755102040819, 124.64598084131613)" width="4.4721359549995796" x="516.64148304290836" y="122.40991286381634"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 523.9795918367347, 116.62848812994591)" width="4.4721359549995796" x="521.74352385923487" y="114.39242015244612"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 529.08163265306121, 108.40274885464393)" width="4.4721359549995796" x="526.84556467556138" y="106.16668087714415"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 534.18367346938771, 99.968763015410275)" width="4.4721359549995796" x="531.94760549188788" y="97.732695037910489"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 539.28571428571422, 91.326530612244923)" width="4.4721359549995796" x="537.04964630821439" y="89.090462634745137"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 544.38775510204084, 82.476051645147891)" width="4.4721359549995796" x="542.15168712454101" y="80.239983667648104"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 549.48979591836735, 73.417326114119163)" width="4.4721359549995796" x="547.25372794086752" y="71.181258136619377"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 554.59183673469386, 64.150354019158726)" width="4.4721359549995796" x="552.35576875719403" y="61.91428604165894"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 559.69387755102036, 54.675135360266587)" width="4.4721359549995796" x="557.45780957352054" y="52.439067382766794"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 564.79591836734699, 44.991670137442739)" width="4.4721359549995796" x="562.55985038984716" y="42.755602159942953"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 569.89795918367338, 35.099958350687224)" width="4.4721359549995796" x="567.66189120617355" y="32.863890373187431"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0"><rect height="4.4721359549995796" transform="rotate(0, 575.0, 25.0)" width="4.4721359549995796" x="572.76393202250017" y="22.76393202250021"></rect></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="475.0" y="35.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="520.0" y="42.0"></text></g><g class="toyplot-axes-Axis" id="t89ff5d96a14a4a92ad57ecd59a32db3f" transform="translate(325.0,285.0) rotate(0.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(125.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><rect class="toyplot-mark-Legend" height="70.0" id="tc2552570710f445c8733acbe01f62684" style="fill:none;stroke:none" width="100.0" x="250.0" y="100.0"></rect><g style="fill:rgb(100%,0%,0%);fill-opacity:1.0;stroke:none"><circle cx="265.0" cy="115.0" r="5.0"></circle></g><text style="alignment-baseline:middle;stroke:none" x="280.0" y="115.0">Experiment 1</text><g style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;stroke:none"><rect height="10.0" transform="rotate(0, 265.0, 135.0)" width="10.0" x="260.0" y="130.0"></rect></g><text style="alignment-baseline:middle;stroke:none" x="280.0" y="135.0">Experiment 2</text><g style="fill:rgb(0%,0%,100%);fill-opacity:1.0;stroke:none"><rect height="10.0" transform="rotate(0, 265.0, 155.0)" width="10.0" x="260.0" y="150.0"></rect></g><text style="alignment-baseline:middle;stroke:none" x="280.0" y="155.0">Experiment 3</text></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tdf709b8d460641dca59c46c1a8884653 text");
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
          var text = document.querySelectorAll("#tdf709b8d460641dca59c46c1a8884653 text");
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
      var data_tables = [{"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [1.0, 0.9596001665972511, 0.920033319450229, 0.8812994585589339, 0.8433985839233653, 0.8063306955435235, 0.7700957934194085, 0.7346938775510206, 0.7001249479383591, 0.6663890045814245, 0.6334860474802165, 0.6014160766347355, 0.5701790920449812, 0.5397750937109538, 0.5102040816326531, 0.4814660558100793, 0.4535610162432321, 0.4264889629321117, 0.40024989587671805, 0.3748438150770512, 0.3502707205331112, 0.32653061224489793, 0.3036234902124116, 0.2815493544356518, 0.2603082049146189, 0.23990004164931278, 0.22032486463973353, 0.20158267388588094, 0.18367346938775514, 0.16659725114535612, 0.15035401915868396, 0.1349437734277385, 0.12036651395251982, 0.10662224073302792, 0.0937109537692628, 0.08163265306122454, 0.070387338608913, 0.05997501041232822, 0.050395668471470235, 0.04164931278633907, 0.033735943356934646, 0.026655560183256998, 0.020408163265306135, 0.014993752603082056, 0.01041232819658478, 0.006663890045814259, 0.0037484381507705204, 0.0016659725114535648, 0.0004164931278633912, 0.0]], "title": "Scatterplot Data", "names": ["x", "y0"], "id": "td00df82e73164d109a1a4a8233ea9345", "filename": "toyplot"}, {"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [1.0, 0.9995835068721366, 0.9983340274885465, 0.9962515618492295, 0.9933361099541858, 0.9895876718034152, 0.985006247396918, 0.9795918367346939, 0.973344439816743, 0.9662640566430654, 0.958350687213661, 0.9496043315285297, 0.9400249895876718, 0.9296126613910871, 0.9183673469387755, 0.9062890462307372, 0.8933777592669722, 0.8796334860474803, 0.8650562265722616, 0.8496459808413162, 0.8334027488546439, 0.8163265306122449, 0.7984173261141192, 0.7796751353602666, 0.7600999583506872, 0.7396917950853811, 0.7184506455643482, 0.6963765097875886, 0.6734693877551021, 0.6497292794668887, 0.6251561849229489, 0.599750104123282, 0.5735110370678884, 0.546438983756768, 0.5185339441899208, 0.48979591836734704, 0.46022490628904633, 0.4298209079550188, 0.3985839233652645, 0.3665139525197836, 0.33361099541857575, 0.2998750520616411, 0.26530612244897966, 0.22990420658059152, 0.19366930445647668, 0.15660141607663491, 0.11870054144106634, 0.07996668054977096, 0.040399833402748886, 0.0], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "title": "Scatterplot Data", "names": ["x", "y0", "y1"], "id": "t3d317cccfad446c39f9d155a3c18ccb0", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tdf709b8d460641dca59c46c1a8884653 .toyplot-mark-popup");
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
      var axes = {"t5f821d702d614d7e9a6cb84c9417e96e": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 575.0, "min": 325.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}, "t697877bdb802484da072009c1f319758": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 275.0, "min": 25.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 25.0, "min": 275.0}, "scale": "linear"}]}};
    
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

