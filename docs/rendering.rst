
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _rendering:

Rendering
---------

Of course, any plotting library needs a way to render figures for
display, and Toyplot is no exception. To integrate Toyplot into your
workflow as easily as possible, we provide three different rendering
mechanisms:

.. _backends:

Backends
~~~~~~~~

At the lowest level, Toyplot provides a large collection of rendering
``backends``. Each backend knows how to render a Toyplot canvas to a
specific file format, and can typically render the canvas directly to
disk, to a buffer you provide, or return the raw representation of the
canvas for further processing. You choose a backend that provides the
file format you want to generate, and use it to explicitly render your
canvas. For example, you could use the :mod:`toyplot.pdf` backend to
save a figure as a vector PDF image on disk:

.. code:: python

    import toyplot.pdf
    toyplot.pdf.render(canvas, "figure1.pdf")

Similarly, you could substitute the :mod:`toyplot.png` backend to save
a PNG bitmap image:

.. code:: python

    import toyplot.png
    toyplot.png.render(canvas, "figure1.png")

You could do the same with the :mod:`toyplot.svg` backend, but suppose
you wanted to add a custom CSS class to the SVG markup for inclusion in
a publishing workflow. To accomodate this, the SVG backend can return a
DOM for further editing, instead of saving it directly to disk:

.. code:: python

    import toyplot.svg
    svg = toyplot.svg.render(canvas)
    svg.attrib["class"] = "MyCustomClass"
    import xml.etree.ElementTree as xml
    with open("figure1.svg", "wb") as file:
        file.write(xml.tostring(svg))

Finally, there is Toyplot's most important backend,
:mod:`toyplot.html` which produces the preferred interactive HTML
representation of a canvas. Like the other backends, you can use it to
write directly to disk, or return a DOM object for editing as-needed:

.. code:: python

    import toyplot.html
    toyplot.html.render(canvas, "figure1.html")

Note that the file produced by this backend is a completely
self-contained HTML fragment that could be emailed directly to a
colleague, inserted into a larger HTML document, etc.

Displays
~~~~~~~~

While backends are useful when you wish to save a canvas to disk for
incorporation into a paper or some larger workflow, in many cases you
may find yourself simply wanting to display the results of some
computation. Writing files to disk and opening them in a separate
application can be time-consuming and frustrating, particularly when
running a script repeatedly during development. For this case, Toyplot
provides ``display`` modules, which provide convenient ways to display
figures interactively. The most portable of these modules is
:mod:`toyplot.browser`:

.. code:: python

    import toyplot.browser
    toyplot.browser.show(canvas)

This will open a new browser window containing your figure, with all of
Toyplot's interaction and features intact.

If you prefer, an experimental new Qt display is available. It also
displays figures in a popup window with full interaction; in the future
it may grow to include additional Toyplot-specific functionality:

.. code:: python

    import toyplot.qt
    toyplot.qt.show(canvas)

Autorendering
~~~~~~~~~~~~~

For interactive environments such as
`Jupyter <http://www.ipython.org>`__, Toyplot's *autorender* feature
automatically renders a canvas into a notebook cell using Toyplot's
preferred interactive HTML representation. We use autorendering with few
exceptions throughout this documentation ... for example, executing the
following automatically inserts a figure into a Jupyter notebook:

.. code:: python

    import numpy
    x = numpy.linspace(0, 1)
    y = x ** 2

.. code:: python

    import toyplot
    canvas = toyplot.Canvas(width=300)
    canvas.axes().plot(x, y);



.. raw:: html

    <div align="center" class="toyplot" id="t25e6ab11f0b141be8bfea65b5969b232"><svg class="toyplot-canvas-Canvas" height="300.0px" id="td896e7f9a3eb45cc8ba4f326c5c610e7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-coordinates-Cartesian" id="tb2bc27f7f65e461c86d6d7e29c41281f"><clipPath id="t31ddbd14bc2b4a0eb1b81cb999318765"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t31ddbd14bc2b4a0eb1b81cb999318765)"><g class="toyplot-mark-Plot" id="t78bb8d80e4a14f299555dad4b49068cd" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 54.08163265306122 249.9167013744273 L 58.16326530612244 249.66680549770928 L 62.244897959183675 249.25031236984589 L 66.326530612244909 248.66722199083716 L 70.408163265306115 247.91753436068305 L 74.489795918367349 247.0012494793836 L 78.571428571428584 245.91836734693877 L 82.65306122448979 244.6688879633486 L 86.734693877551024 243.25281132861306 L 90.81632653061223 241.6701374427322 L 94.897959183673464 239.92086630570594 L 98.979591836734699 238.00499791753435 L 103.06122448979592 235.92253227821743 L 107.14285714285714 233.67346938775512 L 111.22448979591837 231.25780924614745 L 115.30612244897959 228.67555185339444 L 119.38775510204081 225.92669720949604 L 123.46938775510203 223.01124531445231 L 127.55102040816327 219.92919616826322 L 131.63265306122449 216.68054977092879 L 135.71428571428572 213.26530612244898 L 139.79591836734693 209.68346522282383 L 143.87755102040816 205.93502707205332 L 147.9591836734694 202.01999167013744 L 152.0408163265306 197.93835901707621 L 156.12244897959184 193.69012911286964 L 160.20408163265307 189.27530195751771 L 164.28571428571428 184.69387755102045 L 168.36734693877551 179.94585589337777 L 172.44897959183672 175.03123698458978 L 176.53061224489795 169.95002082465641 L 180.61224489795919 164.7022074135777 L 184.69387755102042 159.2877967513536 L 188.77551020408163 153.70678883798416 L 192.85714285714283 147.9591836734694 L 196.93877551020407 142.04498125780927 L 201.0204081632653 135.96418159100375 L 205.10204081632654 129.7167846730529 L 209.18367346938774 123.30279050395671 L 213.26530612244898 116.72219908371514 L 217.34693877551018 109.97501041232822 L 221.42857142857142 103.06122448979593 L 225.51020408163265 95.980841316118301 L 229.59183673469386 88.733860891295336 L 233.67346938775509 81.320283215326981 L 237.75510204081633 73.740108288213264 L 241.83673469387753 65.993336109954186 L 245.91836734693877 58.079966680549774 L 250.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t5dba4183deb947829b4f21c7047f92a1" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tfb99e031486b40bb8c171f81900688d8" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "title": "Plot Data", "names": ["x", "y0"], "id": "t78bb8d80e4a14f299555dad4b49068cd", "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t25e6ab11f0b141be8bfea65b5969b232 .toyplot-mark-popup");
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
                function _sign(x)
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
    
                function inside(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
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
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
                    current.x = e.clientX;
                    current.y = e.clientY;
    
                    for(var axis_id in axes)
                    {
                        var axis = document.querySelector("#" + axis_id);
                        var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                        if(coordinates)
                        {
                            var projection = axes[axis_id];
                            var local = current.matrixTransform(axis.getScreenCTM().inverse());
                            if(inside(local.x, projection))
                            {
                                var domain = to_domain(local.x, projection);
                                coordinates.style.visibility = "visible";
                                coordinates.setAttribute("transform", "translate(" + local.x + ")");
                                var text = coordinates.querySelector("text");
                                text.textContent = domain.toFixed(2);
                            }
                            else
                            {
                                coordinates.style.visibility= "hidden";
                            }
                        }
                    }
                }
    
                var root_id = "t25e6ab11f0b141be8bfea65b5969b232";
                var axes = {"t5dba4183deb947829b4f21c7047f92a1": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tfb99e031486b40bb8c171f81900688d8": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Note that no special import statements, magics, backends, or
configuration is required - Toyplot Just Works. In this case,
autorendering is enabled by default when you create a new canvas.
Toyplot knows that it's being run in the Jupyter notebook environment,
and when you execute a notebook cell that contains a canvas with
autorendering enabled, it inserts the rendered canvas in the cell
output. Note that this is not the same as Jupyter's rich output system -
a Toyplot canvas doesn't have to be the result of an expression to be
rendered, and you can create multiple Toyplot canvases in a single
notebook cell (handy when producing multiple figures in a loop), and
they will all be rendered.

Autorendering for a canvas is automatically disabled if you pass it to a
rendering backend or a display. So while the above example automatically
rendered the canvas into a notebook cell, the following will not:

.. code:: python

    canvas = toyplot.Canvas(width=300)
    canvas.axes().plot(x, y)
    toyplot.pdf.render(canvas, "figure2.pdf")

In some circumstances you may want to disable autorendering yourself,
which you can do when the canvas is created:

.. code:: python

    canvas = toyplot.Canvas(width=300, autorender=False)
    canvas.axes().plot(x, y);
