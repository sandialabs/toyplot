
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

Autorendering
~~~~~~~~~~~~~

For interactive environments such as
`Jupyter <http://www.ipython.org>`__, Toyplot's *autorender* feature
automatically renders a canvas into a notebook cell using Toyplot's
preferred interactive HTML representation. We use autorendering with few
exceptions throughout this documentation ... for example, executing the
following automatically inserts a figure into a Jupyter notebook:

.. code:: ipython3

    import numpy
    x = numpy.linspace(0, 1)
    y = x ** 2

.. code:: ipython3

    import toyplot
    canvas = toyplot.Canvas(width=300)
    canvas.cartesian().plot(x, y);



.. raw:: html

    <div class="toyplot" id="tb63dd4eacb1b4d9f885ea175e21c6b36" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t96ae5f3666ff4a70905add7b18fdf096" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t70463ca6a6df4adaa978745f2e0e8738"><clipPath id="t6b2b6b5bd48a4706b3e30f7769a4d8ba"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t6b2b6b5bd48a4706b3e30f7769a4d8ba)"><g class="toyplot-mark-Plot" id="t003a22eb23494005a1b2ec0e37293a37" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 54.08163265306122 249.9167013744273 L 58.16326530612244 249.66680549770928 L 62.244897959183675 249.25031236984589 L 66.326530612244909 248.66722199083716 L 70.408163265306115 247.91753436068305 L 74.489795918367349 247.0012494793836 L 78.571428571428584 245.91836734693877 L 82.65306122448979 244.6688879633486 L 86.734693877551024 243.25281132861306 L 90.81632653061223 241.6701374427322 L 94.897959183673464 239.92086630570594 L 98.979591836734699 238.00499791753435 L 103.06122448979592 235.92253227821743 L 107.14285714285714 233.67346938775512 L 111.22448979591837 231.25780924614745 L 115.30612244897959 228.67555185339444 L 119.38775510204081 225.92669720949604 L 123.46938775510203 223.01124531445231 L 127.55102040816327 219.92919616826322 L 131.63265306122449 216.68054977092879 L 135.71428571428572 213.26530612244898 L 139.79591836734693 209.68346522282383 L 143.87755102040816 205.93502707205332 L 147.9591836734694 202.01999167013744 L 152.0408163265306 197.93835901707621 L 156.12244897959184 193.69012911286964 L 160.20408163265307 189.27530195751771 L 164.28571428571428 184.69387755102045 L 168.36734693877551 179.94585589337777 L 172.44897959183672 175.03123698458978 L 176.53061224489795 169.95002082465641 L 180.61224489795919 164.7022074135777 L 184.69387755102042 159.2877967513536 L 188.77551020408163 153.70678883798416 L 192.85714285714283 147.9591836734694 L 196.93877551020407 142.04498125780927 L 201.0204081632653 135.96418159100375 L 205.10204081632654 129.7167846730529 L 209.18367346938774 123.30279050395671 L 213.26530612244898 116.72219908371514 L 217.34693877551018 109.97501041232822 L 221.42857142857142 103.06122448979593 L 225.51020408163265 95.980841316118301 L 229.59183673469386 88.733860891295336 L 233.67346938775509 81.320283215326981 L 237.75510204081633 73.740108288213264 L 241.83673469387753 65.993336109954186 L 245.91836734693877 58.079966680549774 L 250.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="tf87ccb27358646cea62a831c43bbd86b" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tee8889cd202b47b59f87dabd30f74617" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/tables"] = (function()
        {
            var tables = [];
    
            var module = {};
    
            module.set = function(owner, key, names, columns)
            {
                tables.push({owner: owner, key: key, names: names, columns: columns});
            }
    
            module.get = function(owner, key)
            {
                for(var i = 0; i != tables.length; ++i)
                {
                    var table = tables[i];
                    if(table.owner != owner)
                        continue;
                    if(table.key != key)
                        continue;
                    return {names: table.names, columns: table.columns};
                }
            }
    
            module.get_csv = function(owner, key)
            {
                var table = module.get(owner, key);
                if(table != undefined)
                {
                    var csv = "";
                    csv += table.names.join(",") + "\n";
                    for(var i = 0; i != table.columns[0].length; ++i)
                    {
                      for(var j = 0; j != table.columns.length; ++j)
                      {
                        if(j)
                          csv += ",";
                        csv += table.columns[j][i];
                      }
                      csv += "\n";
                    }
                    return csv;
                }
            }
    
            return module;
        })();
    modules["toyplot/root/id"] = "tb63dd4eacb1b4d9f885ea175e21c6b36";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t96ae5f3666ff4a70905add7b18fdf096";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
    modules["toyplot/menus/context"] = (function(root, canvas)
        {
            var wrapper = document.createElement("div");
            wrapper.innerHTML = "<ul class='toyplot-context-menu' style='background:#eee; border:1px solid #b8b8b8; border-radius:5px; box-shadow: 0px 0px 8px rgba(0%,0%,0%,0.25); margin:0; padding:3px 0; position:fixed; visibility:hidden;'></ul>"
            var menu = wrapper.firstChild;
    
            root.appendChild(menu);
    
            var items = [];
    
            var ignore_mouseup = null;
            function open_menu(e)
            {
                var show_menu = false;
                for(var index=0; index != items.length; ++index)
                {
                    var item = items[index];
                    if(item.show(e))
                    {
                        item.item.style.display = "block";
                        show_menu = true;
                    }
                    else
                    {
                        item.item.style.display = "none";
                    }
                }
    
                if(show_menu)
                {
                    ignore_mouseup = true;
                    menu.style.left = (e.clientX + 1) + "px";
                    menu.style.top = (e.clientY - 5) + "px";
                    menu.style.visibility = "visible";
                    e.stopPropagation();
                    e.preventDefault();
                }
            }
    
            function close_menu()
            {
                menu.style.visibility = "hidden";
            }
    
            function contextmenu(e)
            {
                open_menu(e);
            }
    
            function mousemove(e)
            {
                ignore_mouseup = false;
            }
    
            function mouseup(e)
            {
                if(ignore_mouseup)
                {
                    ignore_mouseup = false;
                    return;
                }
                close_menu();
            }
    
            function keydown(e)
            {
                if(e.key == "Escape" || e.key == "Esc" || e.keyCode == 27)
                {
                    close_menu();
                }
            }
    
            canvas.addEventListener("contextmenu", contextmenu);
            canvas.addEventListener("mousemove", mousemove);
            document.addEventListener("mouseup", mouseup);
            document.addEventListener("keydown", keydown);
    
            var module = {};
            module.add_item = function(label, show, activate)
            {
                var wrapper = document.createElement("div");
                wrapper.innerHTML = "<li class='toyplot-context-menu-item' style='background:#eee; color:#333; padding:2px 20px; list-style:none; margin:0; text-align:left;'>" + label + "</li>"
                var item = wrapper.firstChild;
    
                items.push({item: item, show: show});
    
                function mouseover()
                {
                    this.style.background = "steelblue";
                    this.style.color = "white";
                }
    
                function mouseout()
                {
                    this.style.background = "#eee";
                    this.style.color = "#333";
                }
    
                function choose_item(e)
                {
                    close_menu();
                    activate();
    
                    e.stopPropagation();
                    e.preventDefault();
                }
    
                item.addEventListener("mouseover", mouseover);
                item.addEventListener("mouseout", mouseout);
                item.addEventListener("mouseup", choose_item);
                item.addEventListener("contextmenu", choose_item);
    
                menu.appendChild(item);
            };
            return module;
        })(modules["toyplot/root"],modules["toyplot/canvas"]);
    modules["toyplot/io"] = (function()
        {
            var module = {};
            module.save_file = function(mime_type, charset, data, filename)
            {
                var uri = "data:" + mime_type + ";charset=" + charset + "," + data;
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = filename;
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
            };
            return module;
        })();
    modules["toyplot.coordinates.Axis"] = (
            function(canvas)
            {
                function sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function in_range(a, x, b)
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
                        if(in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                var axes = {};
    
                function display_coordinates(e)
                {
                    var current = canvas.createSVGPoint();
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
    
                canvas.addEventListener("click", display_coordinates);
    
                var module = {};
                module.show_coordinates = function(axis_id, projection)
                {
                    axes[axis_id] = projection;
                }
    
                return module;
            })(modules["toyplot/canvas"]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t003a22eb23494005a1b2ec0e37293a37","data","plot data",["x", "y0"],[[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tf87ccb27358646cea62a831c43bbd86b",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tee8889cd202b47b59f87dabd30f74617",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


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

.. code:: ipython3

    canvas = toyplot.Canvas(width=300, autorender=False)
    canvas.cartesian().plot(x, y);
