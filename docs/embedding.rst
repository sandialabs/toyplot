
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _embedding:

Embedding
=========

We like to say that "Toyplot figures are beautiful, scalable,
embeddable, and interactive", but what does *embeddable* really mean,
anyway? Scientists and engineers are already accustomed to embedding
static images in their publications and presentations, so what does
embedding in Toyplot have to offer that other tools don't?

In a word: interaction.

In their native HTML + Javascript format, Toyplot figures are
interactive - users can mouse over the figure to see interactive
coordinates and even extract the data from a figure in CSV format using
a context menu. This is just scratching the surface of what we want to
achieve in interactivity, but the key point is that each figure is
*completely self contained* and can be distributed as a single file
without any need for an external server, special libraries or
stylesheets.

Here are just a few examples of Toyplot embedding in-action:

Jupyter (IPython) Notebooks
---------------------------

To use Toyplot in a Jupyter (IPython) notebook, simply import the
library and create a plot - no magics or backends required. The library
knows that it's being executed in the Jupyter environment, and
automatically renders the plot into your notebook using the interactive
HTML format:

.. code:: python

    import numpy
    import toyplot
    toyplot.plot(numpy.linspace(0, 1) ** 2, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="td18946e8500245c3bbd74e96e869ac40"><svg height="300.0px" id="t4ba86c61372640969114a49b17d547de" style="background-color:transparent;fill:#292724;fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:#292724;stroke-opacity:1.0;stroke-width:1.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tad426aefbfe74a5189b4175e1b1b3f38"><clipPath id="t28113b924c8e4291b40a696a60115854"><rect height="200.0" width="200.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t28113b924c8e4291b40a696a60115854)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="200.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="te9ecd99bc2884c76aa3213793c064699" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 240.0 L 63.599999999999994 239.92503123698458 L 67.199999999999989 239.70012494793838 L 70.799999999999997 239.32528113286131 L 74.400000000000006 238.80049979175345 L 78.0 238.12578092461476 L 81.599999999999994 237.30112453144525 L 85.200000000000003 236.32653061224491 L 88.799999999999997 235.20199916701375 L 92.400000000000006 233.92753019575176 L 96.0 232.50312369845898 L 99.599999999999994 230.92877967513536 L 103.19999999999999 229.20449812578093 L 106.80000000000001 227.33027905039569 L 110.40000000000001 225.30612244897958 L 114.0 223.13202832153269 L 117.59999999999999 220.80799666805498 L 121.2 218.33402748854647 L 124.79999999999998 215.71012078300706 L 128.40000000000001 212.93627655143689 L 132.0 210.01249479383591 L 135.59999999999999 206.9387755102041 L 139.19999999999999 203.71511870054144 L 142.80000000000001 200.341524364848 L 146.39999999999998 196.81799250312369 L 150.0 193.1445231153686 L 153.60000000000002 189.3211162015827 L 157.20000000000002 185.34777176176596 L 160.80000000000001 181.2244897959184 L 164.39999999999998 176.95127030403995 L 168.0 172.5281132861308 L 171.60000000000002 167.95501874219076 L 175.19999999999999 163.2319866722199 L 178.80000000000001 158.35901707621824 L 182.40000000000001 153.33610995418576 L 186.0 148.16326530612247 L 189.59999999999999 142.84048313202834 L 193.19999999999999 137.36776343190337 L 196.80000000000001 131.74510620574762 L 200.40000000000001 125.97251145356105 L 204.0 120.04997917534362 L 207.59999999999999 113.97750937109539 L 211.19999999999999 107.75510204081634 L 214.80000000000001 101.38275718450647 L 218.39999999999998 94.860474802165797 L 222.0 88.188254893794294 L 225.60000000000002 81.366097459391938 L 229.19999999999999 74.39400249895877 L 232.79999999999998 67.271970012494791 L 236.39999999999998 60.0" style="fill:none;stroke:rgba(40%,76.1%,64.7%,1);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:white;opacity:0.75;stroke:none" width="90.0" x="150.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="236.39999999999998" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="96.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="132.0" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="168.0" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="204.0" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="240.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#td18946e8500245c3bbd74e96e869ac40 text");
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
          var text = document.querySelectorAll("#td18946e8500245c3bbd74e96e869ac40 text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "names": ["x", "y0"], "id": "te9ecd99bc2884c76aa3213793c064699", "title": "Plot Data"}];
    
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
          var popup = document.querySelector("#td18946e8500245c3bbd74e96e869ac40 .toyplot-mark-popup");
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
      var axes = {"tad426aefbfe74a5189b4175e1b1b3f38": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 240.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
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


Documentation
-------------

"This is all well and good", you may say, "and the interaction is nice,
but it's hardly a game-changer".

But wait! This is where the self-contained nature of Toyplot figures
really starts to shine. If you convert your notebook to restructured
text (the markup of choice for most Python documentation):

::

    $ ipython nbconvert --to rst mynotebook.ipynb --output mynotebook.rst

the HTML Toyplot figures will be embedded in the restructured text and
remain fully-interactive in the generated docs. This, by the way, is how
most of the Toyplot documentation is written, including this page - in
Jupyter notebooks, then converted to .rst files, then compiled into HTML
documentation using ``Sphinx <http://sphinx-doc.org>``\ \_

Slides
------

Similarly, you can convert your Jupyter notebook into an interactive
Reveal.js presentation using the nbconvert utility, and the embedded
Toyplot figures in your slides will retain their interaction for your
presentation:

``ipython nbconvert --to slides mynotebook.ipynb --output mynotebook.slides.html``

Imagine being able to respond to audience questions with a live figure!

Electronic Publication
----------------------

All of this leads to what is a key goal of the Toyplot authors:
supporting electronic publication.

E-Mail
------

Because a Toyplot figure is fully self-contained, it can be easily
shared through e-mail or other electronic communication channels. You
can e-mail a Toyplot .html file to a colleague, and they will be able to
easily view and interact with the file, in some cases right inside their
e-mail client!

PyQT / PySide
-------------

Because the Qt graphical user interface includes a fully-featured WebKit
browser and Python bindings (PyQt or PySide, take your pick), you can
embed interactive Toyplot plots in just a few lines of code, with all
the interaction intact:

.. code:: python

    window = QWebView()
    canvas, axes, mark = toyplot.plot(x, y)
    window.setHtml(xml.etree.ElementTree.tostring(toyplot.html.render(canvas), method="html"))

If you prefer, you could also embed static plots using the SVG or PNG
backends:

.. code:: python

    window.setContent(xml.tostring(toyplot.svg.render(canvas)), "image/svg+xml")

or

.. code:: python

    window.setContent(toyplot.png.render(canvas), "image/png")

Legacy Formats
--------------

Of course, Toyplot supports a variety of backends, including SVG, PDF,
PNG, MPEG4, and WebM formats, that you could use to write static figures
to disk:

.. code:: python

    toyplot.svg.render(canvas, "myfigure.svg")
    toyplot.pdf.render(canvas, "myfigure.pdf")
    toyplot.png.render(canvas, "myfigure.png")
    toyplot.mp4.render(canvas, "myfigure.mp4")
    toyplot.webm.render(canvas, "myfigure.webm")

