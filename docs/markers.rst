
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _markers:

Markers
=======

In Toyplot, markers are used to show the individual datums in
scatterplots:

.. code:: python

    import numpy
    import toyplot
    
    import logging
    logging.basicConfig()

.. code:: python

    y = numpy.linspace(0, 1, 20) ** 2
    toyplot.scatterplot(y, width=300);



.. raw:: html

    <div class="toyplot" id="tf3cdddd9b5a7402f99dfa1e8a7386212" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t821e9274ee3e43b4bcdafcc800bf8391" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t001181cf151c4f38a9e127f197904a80"><clipPath id="t2ccdaa2cce894caaa7cc87a20447d885"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t2ccdaa2cce894caaa7cc87a20447d885)"><g class="toyplot-mark-Scatterplot" id="t350480c85085434e94e401efe5edce94"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(60.0, 249.4459833795014)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(70.0, 247.78393351800551)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(80.0, 245.01385041551248)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(90.0, 241.13573407202216)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(100.0, 236.14958448753461)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(110.0, 230.05540166204986)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(120.0, 222.85318559556785)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(130.0, 214.54293628808864)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(140.0, 205.1246537396122)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(150.0, 194.5983379501385)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(160.0, 182.96398891966757)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(170.0, 170.22160664819947)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(180.0, 156.37119113573411)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(190.0, 141.41274238227149)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(200.0, 125.34626038781163)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(210.0, 108.17174515235459)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(220.0, 89.889196675900322)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(230.0, 70.498614958448783)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(240.0, 50.0)"><circle r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="tcef34dd3decf401ba5dd6c1e0cceaff7" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tb656300a385b4645a093222c683beb71" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tf3cdddd9b5a7402f99dfa1e8a7386212";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t821e9274ee3e43b4bcdafcc800bf8391";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t350480c85085434e94e401efe5edce94","data","scatterplot",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tcef34dd3decf401ba5dd6c1e0cceaff7",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tb656300a385b4645a093222c683beb71",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Markers can also be added to regular plots to highlight the datums (they
are turned-off by default):

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.cartesian(grid=(1, 2, 0)).plot(y)
    canvas.cartesian(grid=(1, 2, 1)).plot(y, marker="o");



.. raw:: html

    <div class="toyplot" id="tea22bdeadcf74742be5dcbbd65a9a0e8" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t4dfdb24050794ff7a8fb52a031e930c5" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tf3d505e288f94ab5b256976afef0e27f"><clipPath id="tabaa1bd7ab5b47e991206edb45e74b7f"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tabaa1bd7ab5b47e991206edb45e74b7f)"><g class="toyplot-mark-Plot" id="t302d57e8363743d5aa1efeae9aadf6d2" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t8334470f16f54f22bea9ac1d917c2208" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t8f16fda55d314118b8f55efb6311eba4" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="ta7817518b3a548e891cc6bb17609d0dd"><clipPath id="tb4be502a84f347bfbd68fcb1638b8f0f"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#tb4be502a84f347bfbd68fcb1638b8f0f)"><g class="toyplot-mark-Plot" id="t71f05f7271bf4cb9bbf898eade113340" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(350.0, 250.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(360.0, 249.4459833795014)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(370.0, 247.78393351800551)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(380.0, 245.01385041551248)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(390.0, 241.13573407202216)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(400.0, 236.14958448753461)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(410.0, 230.05540166204986)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(420.0, 222.85318559556785)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(430.0, 214.54293628808864)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(440.0, 205.1246537396122)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(450.0, 194.5983379501385)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(460.0, 182.96398891966757)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(470.0, 170.22160664819947)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(480.0, 156.37119113573411)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(490.0, 141.41274238227149)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(500.0, 125.34626038781163)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(510.0, 108.17174515235459)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(520.0, 89.889196675900322)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(530.0, 70.498614958448783)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(540.0, 50.0)"><circle r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t4b2139c9f4584ceeb4ffc853250773f0" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="td704a8838f51442397d251472e569c96" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tea22bdeadcf74742be5dcbbd65a9a0e8";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t4dfdb24050794ff7a8fb52a031e930c5";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t302d57e8363743d5aa1efeae9aadf6d2","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t8334470f16f54f22bea9ac1d917c2208",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t8f16fda55d314118b8f55efb6311eba4",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t71f05f7271bf4cb9bbf898eade113340","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t4b2139c9f4584ceeb4ffc853250773f0",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"td704a8838f51442397d251472e569c96",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


You can use the ``size`` argument to control the size of the markers:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.cartesian(grid=(1, 2, 0)).plot(y, marker="o", size=6)
    canvas.cartesian(grid=(1, 2, 1)).plot(y, marker="o", size=10);



.. raw:: html

    <div class="toyplot" id="t3f76440fe9634e6daa3aae713d99e5cd" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t640473d654f24bde906ff22206ff77f2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tde47996318014d8e95f438477261a16e"><clipPath id="te0157016cb5d4f6b8b4579df85cbb76c"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#te0157016cb5d4f6b8b4579df85cbb76c)"><g class="toyplot-mark-Plot" id="t061435c8b1df4fc7a95d821e225d036b" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(60.0, 249.4459833795014)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(70.0, 247.78393351800551)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(80.0, 245.01385041551248)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(90.0, 241.13573407202216)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(100.0, 236.14958448753461)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(110.0, 230.05540166204986)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(120.0, 222.85318559556785)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(130.0, 214.54293628808864)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(140.0, 205.1246537396122)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(150.0, 194.5983379501385)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(160.0, 182.96398891966757)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(170.0, 170.22160664819947)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(180.0, 156.37119113573411)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(190.0, 141.41274238227149)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(200.0, 125.34626038781163)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(210.0, 108.17174515235459)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(220.0, 89.889196675900322)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(230.0, 70.498614958448783)"><circle r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(240.0, 50.0)"><circle r="3.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="tba5ed162fa824d4fa94cf0cb3b792efe" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="ta8d9d1e09bc84203b47ae6735e661ef3" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t8f88f3780f374007bd949570a4021611"><clipPath id="tccef2a5cde224f319cc0c37377fe52e8"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#tccef2a5cde224f319cc0c37377fe52e8)"><g class="toyplot-mark-Plot" id="t85c0f170d6b7483e9a21c7ae009f8ed5" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(350.0, 250.0)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(360.0, 249.4459833795014)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(370.0, 247.78393351800551)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(380.0, 245.01385041551248)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(390.0, 241.13573407202216)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(400.0, 236.14958448753461)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(410.0, 230.05540166204986)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(420.0, 222.85318559556785)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(430.0, 214.54293628808864)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(440.0, 205.1246537396122)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(450.0, 194.5983379501385)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(460.0, 182.96398891966757)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(470.0, 170.22160664819947)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(480.0, 156.37119113573411)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(490.0, 141.41274238227149)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(500.0, 125.34626038781163)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(510.0, 108.17174515235459)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(520.0, 89.889196675900322)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(530.0, 70.498614958448783)"><circle r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(540.0, 50.0)"><circle r="5.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="tdb76b875b2c341ee9577acf128ac47e8" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="td30952c4db50484c909068e2e8f5d10d" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t3f76440fe9634e6daa3aae713d99e5cd";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t640473d654f24bde906ff22206ff77f2";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t061435c8b1df4fc7a95d821e225d036b","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tba5ed162fa824d4fa94cf0cb3b792efe",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"ta8d9d1e09bc84203b47ae6735e661ef3",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t85c0f170d6b7483e9a21c7ae009f8ed5","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tdb76b875b2c341ee9577acf128ac47e8",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"td30952c4db50484c909068e2e8f5d10d",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Or you can use the ``area`` argument instead of ``size`` as an
approximation of the *area* of the markers (this is recommended if
you're using per-datum marker sizes to display data).

By default, plot and scatterplot markers are small circles, but many
other shapes can be specified using a string *shape code*:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.cartesian(grid=(1, 2, 0)).scatterplot(y, marker="x", size=10)
    canvas.cartesian(grid=(1, 2, 1)).scatterplot(y, marker="^", size=10, mstyle={"stroke":toyplot.color.near_black});



.. raw:: html

    <div class="toyplot" id="t4a27b48465c64d30868ef1b79b56d624" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t3376777ceb174bb89c90e14e66dfcb56" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t80ae7f8e065d49e1b1663f9b94250dc9"><clipPath id="t40b6f733c12f461b9550b7ec5519542d"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t40b6f733c12f461b9550b7ec5519542d)"><g class="toyplot-mark-Scatterplot" id="ta61de77161994bef9d56a6d7fd9c0693"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(60.0, 249.4459833795014)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(70.0, 247.78393351800551)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(80.0, 245.01385041551248)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(90.0, 241.13573407202216)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(100.0, 236.14958448753461)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(110.0, 230.05540166204986)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(120.0, 222.85318559556785)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(130.0, 214.54293628808864)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(140.0, 205.1246537396122)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(150.0, 194.5983379501385)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(160.0, 182.96398891966757)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(170.0, 170.22160664819947)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(180.0, 156.37119113573411)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(190.0, 141.41274238227149)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(200.0, 125.34626038781163)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(210.0, 108.17174515235459)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(220.0, 89.889196675900322)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(230.0, 70.498614958448783)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(240.0, 50.0)"><line transform="rotate(45)" y1="-5.0" y2="5.0"></line><line transform="rotate(-45)" y1="-5.0" y2="5.0"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="tb790ce24ad1c426d9213201949af9138" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t4744f41aa13d460c90b14eb6e682785e" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="tda5d7bd3249d40d3b52c887665c194d5"><clipPath id="tbb09afea8cad45b3b0fa3f0a72b2252c"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#tbb09afea8cad45b3b0fa3f0a72b2252c)"><g class="toyplot-mark-Scatterplot" id="t568a273a4338443cb4d6322e63a0f9d2"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(350.0, 250.0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(360.0, 249.4459833795014)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(370.0, 247.78393351800551)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(380.0, 245.01385041551248)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(390.0, 241.13573407202216)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(400.0, 236.14958448753461)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(410.0, 230.05540166204986)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(420.0, 222.85318559556785)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(430.0, 214.54293628808864)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(440.0, 205.1246537396122)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(450.0, 194.5983379501385)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(460.0, 182.96398891966757)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(470.0, 170.22160664819947)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(480.0, 156.37119113573411)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(490.0, 141.41274238227149)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(500.0, 125.34626038781163)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(510.0, 108.17174515235459)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(520.0, 89.889196675900322)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(530.0, 70.498614958448783)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(540.0, 50.0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0"></polygon></g></g></g></g><g class="toyplot-coordinates-Axis" id="te9f3c0115ce446e7b4a793e6d99c4112" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="te1f142f5a5af444185913eede9389ccf" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t4a27b48465c64d30868ef1b79b56d624";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t3376777ceb174bb89c90e14e66dfcb56";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"ta61de77161994bef9d56a6d7fd9c0693","data","scatterplot",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tb790ce24ad1c426d9213201949af9138",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t4744f41aa13d460c90b14eb6e682785e",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t568a273a4338443cb4d6322e63a0f9d2","data","scatterplot",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"te9f3c0115ce446e7b4a793e6d99c4112",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"te1f142f5a5af444185913eede9389ccf",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Note the use of the *mstyle* argument to override the appearance of the
marker in the second example. For line plots, this allows you to style
the lines and the markers separately:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.cartesian(grid=(1, 2, 0)).plot(y, marker="o", size=8, style={"stroke":"darkgreen"})
    canvas.cartesian(grid=(1, 2, 1)).plot(y, marker="o", size=8, mstyle={"stroke":"darkgreen"});



.. raw:: html

    <div class="toyplot" id="t557213473cc44f7fa0bec8cfbf9898cc" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="te45e8f074e714468be0bfda9948edfe5" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tc567efd7bb914577b855214c8d8ab813"><clipPath id="tc986c11e058e4cb4917d2320a7952315"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tc986c11e058e4cb4917d2320a7952315)"><g class="toyplot-mark-Plot" id="t8355f22ad88440349c916e9f0165a3c4" style="fill:none;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(60.0, 249.4459833795014)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(70.0, 247.78393351800551)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(80.0, 245.01385041551248)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(90.0, 241.13573407202216)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(100.0, 236.14958448753461)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(110.0, 230.05540166204986)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(120.0, 222.85318559556785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(130.0, 214.54293628808864)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(140.0, 205.1246537396122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(150.0, 194.5983379501385)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(160.0, 182.96398891966757)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(170.0, 170.22160664819947)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(180.0, 156.37119113573411)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(190.0, 141.41274238227149)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(200.0, 125.34626038781163)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(210.0, 108.17174515235459)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(220.0, 89.889196675900322)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(230.0, 70.498614958448783)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(240.0, 50.0)"><circle r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t1c1698515cbd455386d6f4f77863d616" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t73cdd635282043219eea79b5f4fd5406" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t2b071005b5f34d80a8d729fc9765857d"><clipPath id="tdeb4e8e9bcda4d068b6727542623d4c8"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#tdeb4e8e9bcda4d068b6727542623d4c8)"><g class="toyplot-mark-Plot" id="tf783662ac72543bba11e973f28711d3a" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(350.0, 250.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(360.0, 249.4459833795014)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(370.0, 247.78393351800551)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(380.0, 245.01385041551248)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(390.0, 241.13573407202216)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(400.0, 236.14958448753461)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(410.0, 230.05540166204986)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(420.0, 222.85318559556785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(430.0, 214.54293628808864)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(440.0, 205.1246537396122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(450.0, 194.5983379501385)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(460.0, 182.96398891966757)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(470.0, 170.22160664819947)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(480.0, 156.37119113573411)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(490.0, 141.41274238227149)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(500.0, 125.34626038781163)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(510.0, 108.17174515235459)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(520.0, 89.889196675900322)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(530.0, 70.498614958448783)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0" transform="translate(540.0, 50.0)"><circle r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t3bcec7bef2134067998971bf445486a0" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t1827d5903bc5439d9f327c7b737fb1db" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t557213473cc44f7fa0bec8cfbf9898cc";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "te45e8f074e714468be0bfda9948edfe5";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t8355f22ad88440349c916e9f0165a3c4","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t1c1698515cbd455386d6f4f77863d616",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t73cdd635282043219eea79b5f4fd5406",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tf783662ac72543bba11e973f28711d3a","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t3bcec7bef2134067998971bf445486a0",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t1827d5903bc5439d9f327c7b737fb1db",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Note that you can pass a sequence of shape codes to the *marker*
argument, to specify markers on a per-series or per-datum basis.

The string shape code is actually a shortcut for a full marker
specification, which is an instance of :class:`toyplot.marker.Marker`
that contains a set of explicit marker attributes:

-  "shape" - marker shape code.
-  "mstyle" - dictionary of CSS styles to apply to the marker *shape*.
-  "size" - size of the marker.
-  "angle" - angle (in degrees) to rotate the marker.
-  "label" - text label superimposed on the marker.
-  "lstyle" - dictionary of CSS styles to apply to the marker *label*.

Using the full marker specification allows you to override the size,
style, and appearance of individual markers in a series, if necessary.

You can use :func:`toyplot.marker.create` to create instances of
:class:`toyplot.marker.Marker`, as in the following examples:

.. code:: python

    import toyplot.marker
    
    marker_a = toyplot.marker.create(shape="^", angle=-30, size=15)
    marker_b = toyplot.marker.create(shape="o", label="B", lstyle={"fill":"white"})
    
    canvas = toyplot.Canvas(600, 300)
    canvas.cartesian(grid=(1, 2, 0)).scatterplot(y, marker=marker_a, size=10)
    canvas.cartesian(grid=(1, 2, 1)).scatterplot(y, marker=marker_b, size=15);



.. raw:: html

    <div class="toyplot" id="t7c98a47255f94b78b60c154889ba9639" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t824c3a6748444671a66e4ca71ee435ec" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t8ebce0300e9c4986bfef13c47fa27484"><clipPath id="t5cf3db5670dc49b18717c136801ca6c7"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t5cf3db5670dc49b18717c136801ca6c7)"><g class="toyplot-mark-Scatterplot" id="t0a1f09d5354f464cba1c800f822ef855"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(50.0, 250.0) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(60.0, 249.4459833795014) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(70.0, 247.78393351800551) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(80.0, 245.01385041551248) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(90.0, 241.13573407202216) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(100.0, 236.14958448753461) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(110.0, 230.05540166204986) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(120.0, 222.85318559556785) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(130.0, 214.54293628808864) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(140.0, 205.1246537396122) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(150.0, 194.5983379501385) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(160.0, 182.96398891966757) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(170.0, 170.22160664819947) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(180.0, 156.37119113573411) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(190.0, 141.41274238227149) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(200.0, 125.34626038781163) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(210.0, 108.17174515235459) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(220.0, 89.889196675900322) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(230.0, 70.498614958448783) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(240.0, 50.0) rotate(30)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g></g></g></g><g class="toyplot-coordinates-Axis" id="teb2bda1e14104cc29b2bba4c16f47e39" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tcaa76dd399fe4be69cc44a2f2f4a0415" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t5198aa327cc744c8aaee00b758ad6979"><clipPath id="t96d64f75594c4595a62eddc441502c09"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t96d64f75594c4595a62eddc441502c09)"><g class="toyplot-mark-Scatterplot" id="tce2e547d05334d0bb24cbcf43e3765ed"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(350.0, 250.0)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(360.0, 249.4459833795014)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(370.0, 247.78393351800551)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(380.0, 245.01385041551248)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(390.0, 241.13573407202216)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(400.0, 236.14958448753461)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(410.0, 230.05540166204986)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(420.0, 222.85318559556785)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(430.0, 214.54293628808864)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(440.0, 205.1246537396122)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(450.0, 194.5983379501385)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(460.0, 182.96398891966757)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(470.0, 170.22160664819947)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(480.0, 156.37119113573411)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(490.0, 141.41274238227149)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(500.0, 125.34626038781163)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(510.0, 108.17174515235459)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(520.0, 89.889196675900322)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(530.0, 70.498614958448783)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(540.0, 50.0)"><circle r="7.5"></circle><g><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">B</text></g></g></g></g></g><g class="toyplot-coordinates-Axis" id="t4e071edc75664186bbc1901259f4a0a3" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t58445b0bba3342579c67025f1449663b" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t7c98a47255f94b78b60c154889ba9639";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t824c3a6748444671a66e4ca71ee435ec";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t0a1f09d5354f464cba1c800f822ef855","data","scatterplot",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"teb2bda1e14104cc29b2bba4c16f47e39",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tcaa76dd399fe4be69cc44a2f2f4a0415",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tce2e547d05334d0bb24cbcf43e3765ed","data","scatterplot",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t4e071edc75664186bbc1901259f4a0a3",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t58445b0bba3342579c67025f1449663b",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


In addition to using markers in plots and scatterplots, markers can be
embedded in any figure text, using custom HTML markup. The markup itself
can be fairly verbose, to :class:`toyplot.marker.Marker` provides API
to make it easier:

.. code:: python

    marker_a = toyplot.marker.create(shape="s", label="A", mstyle={"fill":"none"})
    marker_b = toyplot.marker.create(shape="*")
    text = marker_a + " is a marker and so is " + marker_b
    
    style = {"font-size": "18px"}
    
    canvas = toyplot.Canvas(width="5in", height="1.25in")
    axes = canvas.cartesian(show=False)
    axes.text(0, 0, text=text, style=style);



.. raw:: html

    <div class="toyplot" id="t71fa6e9d2b504bdd880d23750a0f8c2e" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="120.0px" id="td9f965803fd34c3bb4b91d7edcf4c784" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 480.0 120.0" width="480.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t0b132e8cfde0463a92392cd61911839e"><clipPath id="t12145491ed674093b886f1d569b21924"><rect height="40.0" width="400.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t12145491ed674093b886f1d569b21924)"><g class="toyplot-mark-Text" id="t836db4dbdb31444d80d6cd82da2c51cd"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(240.0,60.0)"><g style="fill:none" transform="translate(-96.353999999999999, 0.0)"><rect height="16.65" width="16.65" x="-8.325" y="-8.325"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.4875px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.16458125" y="3.19055625">A</text></g></g><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:18.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-88.029" y="4.599"> is a marker and so is </text><g transform="translate(96.353999999999999, 0.0)"><line y1="-8.325" y2="8.325"></line><line transform="rotate(60)" y1="-8.325" y2="8.325"></line><line transform="rotate(-60)" y1="-8.325" y2="8.325"></line></g></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


You can also convert markers to HTML explicitly, if you prefer:

.. code:: python

    print marker_a.to_html()


.. parsed-literal::

    <marker shape='s' mstyle='fill:none' label='A'/>


This makes it easy to create a table documenting all of the available
marker shape codes:

.. code:: python

    markers = [None, "|","/","-","\\","+","x","*","^",">","v","<","s","d",
               "o","oo","o|", "o/", "o-", "o\\", "o+","ox","o*","r3x1","r2x1","r1x1", "r1x2", "r0.5x1.5"]
    mstyle = {"stroke":toyplot.color.near_black, "fill":"#feb"}
    labels = [str(marker) for marker in markers]
    markers = [toyplot.marker.create(shape=marker, mstyle=mstyle, size=15).to_html() for marker in markers]
    
    # This is necessary because "<" and ">" are interpreted as tags when rendering text.
    from xml.sax.saxutils import escape
    labels = [escape(label) for label in labels]
    
    canvas, table = toyplot.table(trows=1, rows=len(markers), columns=2, width=400, height=1200)
    table.cells.grid.vlines[...,1] = "single"
    table.cells.grid.hlines[1,...] = "single"
    table.top.cell[0,...].data = ["Shape Code", "Marker"]
    table.top.cell[0,...].lstyle = {"font-size":"16px", "font-weight":"bold"}
    table.body.column[0].data = labels
    table.body.column[0].lstyle = {"font-size":"16px", "font-family":"monospace"}
    table.body.column[1].data = markers



.. raw:: html

    <div class="toyplot" id="t4750a492f5994e31adf1e76aae607892" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="1200.0px" id="tc314ffeebaa74f3896fa1aa146634f44" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 400.0 1200.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t02c60f418bdf48d6ba67282d1e694370"><g transform="translate(125.0,68.965517241379303)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-46.232" y="4.088">Shape Code</text></g><g transform="translate(275.0,68.965517241379303)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-26.232" y="4.088">Marker</text></g><g transform="translate(125.0,106.89655172413794)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-19.2" y="3.776">None</text></g><g transform="translate(275.0,106.89655172413794)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"></g></g><g transform="translate(125.0,144.82758620689657)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">|</text></g><g transform="translate(275.0,144.82758620689657)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><line y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,182.75862068965517)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">/</text></g><g transform="translate(275.0,182.75862068965517)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><line transform="rotate(45)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,220.68965517241378)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">-</text></g><g transform="translate(275.0,220.68965517241378)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><line transform="rotate(-90)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,258.62068965517238)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">\</text></g><g transform="translate(275.0,258.62068965517238)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><line transform="rotate(-45)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,296.55172413793099)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">+</text></g><g transform="translate(275.0,296.55172413793099)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><line y1="-7.5" y2="7.5"></line><line transform="rotate(-90)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,334.48275862068959)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">x</text></g><g transform="translate(275.0,334.48275862068959)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><line transform="rotate(45)" y1="-7.5" y2="7.5"></line><line transform="rotate(-45)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,372.4137931034482)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">*</text></g><g transform="translate(275.0,372.4137931034482)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><line y1="-7.5" y2="7.5"></line><line transform="rotate(60)" y1="-7.5" y2="7.5"></line><line transform="rotate(-60)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,410.3448275862068)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">^</text></g><g transform="translate(275.0,410.3448275862068)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5"></polygon></g></g><g transform="translate(125.0,448.27586206896541)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">&gt;</text></g><g transform="translate(275.0,448.27586206896541)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5" transform="rotate(90)"></polygon></g></g><g transform="translate(125.0,486.20689655172401)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">v</text></g><g transform="translate(275.0,486.20689655172401)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5" transform="rotate(-180)"></polygon></g></g><g transform="translate(125.0,524.13793103448256)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">&lt;</text></g><g transform="translate(275.0,524.13793103448256)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><polygon points="-7.5,7.5 0,-7.5 7.5,7.5" transform="rotate(-90)"></polygon></g></g><g transform="translate(125.0,562.06896551724117)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">s</text></g><g transform="translate(275.0,562.06896551724117)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><rect height="15.0" width="15.0" x="-7.5" y="-7.5"></rect></g></g><g transform="translate(125.0,599.99999999999989)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">d</text></g><g transform="translate(275.0,599.99999999999989)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><rect height="15.0" transform="rotate(-45)" width="15.0" x="-7.5" y="-7.5"></rect></g></g><g transform="translate(125.0,637.93103448275849)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">o</text></g><g transform="translate(275.0,637.93103448275849)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><circle r="7.5"></circle></g></g><g transform="translate(125.0,675.8620689655171)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">oo</text></g><g transform="translate(275.0,675.8620689655171)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><circle r="7.5"></circle><circle r="3.75"></circle></g></g><g transform="translate(125.0,713.7931034482757)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">o|</text></g><g transform="translate(275.0,713.7931034482757)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><circle r="7.5"></circle><line y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,751.72413793103431)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">o/</text></g><g transform="translate(275.0,751.72413793103431)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><circle r="7.5"></circle><line transform="rotate(45)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,789.65517241379291)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">o-</text></g><g transform="translate(275.0,789.65517241379291)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><circle r="7.5"></circle><line transform="rotate(-90)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,827.58620689655152)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">o\</text></g><g transform="translate(275.0,827.58620689655152)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><circle r="7.5"></circle><line transform="rotate(-45)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,865.51724137931012)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">o+</text></g><g transform="translate(275.0,865.51724137931012)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><circle r="7.5"></circle><line y1="-7.5" y2="7.5"></line><line transform="rotate(-90)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,903.44827586206873)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">ox</text></g><g transform="translate(275.0,903.44827586206873)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><circle r="7.5"></circle><line transform="rotate(45)" y1="-7.5" y2="7.5"></line><line transform="rotate(-45)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,941.37931034482733)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">o*</text></g><g transform="translate(275.0,941.37931034482733)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><circle r="7.5"></circle><line y1="-7.5" y2="7.5"></line><line transform="rotate(60)" y1="-7.5" y2="7.5"></line><line transform="rotate(-60)" y1="-7.5" y2="7.5"></line></g></g><g transform="translate(125.0,979.31034482758594)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-19.2" y="3.776">r3x1</text></g><g transform="translate(275.0,979.31034482758594)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><rect height="15.0" width="45.0" x="-22.5" y="-7.5"></rect></g></g><g transform="translate(125.0,1017.2413793103444)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-19.2" y="3.776">r2x1</text></g><g transform="translate(275.0,1017.2413793103444)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><rect height="15.0" width="30.0" x="-15.0" y="-7.5"></rect></g></g><g transform="translate(125.0,1055.1724137931033)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-19.2" y="3.776">r1x1</text></g><g transform="translate(275.0,1055.1724137931033)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><rect height="15.0" width="15.0" x="-7.5" y="-7.5"></rect></g></g><g transform="translate(125.0,1093.1034482758619)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-19.2" y="3.776">r1x2</text></g><g transform="translate(275.0,1093.1034482758619)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><rect height="30.0" width="15.0" x="-7.5" y="-15.0"></rect></g></g><g transform="translate(125.0,1131.0344827586205)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-38.4" y="3.776">r0.5x1.5</text></g><g transform="translate(275.0,1131.0344827586205)"><g style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0" transform="translate(0.0, -4.4408920985006262e-16)"><rect height="22.5" width="7.5" x="-3.75" y="-11.25"></rect></g></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="350.0" y1="87.931034482758619" y2="87.931034482758619"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="200.0" x2="200.0" y1="50.0" y2="1149.9999999999998"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t4750a492f5994e31adf1e76aae607892";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tc314ffeebaa74f3896fa1aa146634f44";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t02c60f418bdf48d6ba67282d1e694370","data","table data",["Shape Code", "Marker"],[["None", "|", "/", "-", "\\", "+", "x", "*", "^", "&gt;", "v", "&lt;", "s", "d", "o", "oo", "o|", "o/", "o-", "o\\", "o+", "ox", "o*", "r3x1", "r2x1", "r1x1", "r1x2", "r0.5x1.5"], ["<marker mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='|' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='/' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='-' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='\\' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='+' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='x' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='*' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='^' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='&gt;' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='v' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='&lt;' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='s' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='d' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='o' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='oo' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='o|' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='o/' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='o-' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='o\\' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='o+' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='ox' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='o*' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='r3x1' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='r2x1' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='r1x1' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='r1x2' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>", "<marker shape='r0.5x1.5' mstyle='fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0' size='15'/>"]],"toyplot");
    })();</script></div></div>


There are several items here worth noting - first, you can pass *None*
or an empty string to produce an invisible marker, if you need to hide a
datum or declutter the display. Second, observe that several of the
marker shapes contain internal details that require a contrasting stroke
and fill to be visible. Finally, the rectangular ``rWxH`` markers can be
specified using any values (including floating point values) for their
width and height.

Keep in mind that you can embed markers in *any* text string in Toyplot,
including labels, tick marks, and more. And because
:class:`toyplot.mark.Mark` objects have a public ``markers`` attribute
that is used when creating legends, you can be very creative when
annotating figures:

.. code:: python

    import toyplot.data
    data = toyplot.data.read_csv("deliveries.csv")
    
    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.cartesian(xlabel="Date", ylabel="Deliveries", ymin=0)
    deliveries = axes.plot(data["Delivered"], color="darkred")
    
    axes = axes.share("x", ylabel="On Time")
    on_time = axes.plot(data["On Time"], color="steelblue")
    
    axes.label.text = "Deliveries (" + deliveries.markers[0] + ") vs. On Time (" + on_time.markers[0] + ")"



.. raw:: html

    <div class="toyplot" id="t7289ce7c41904dc2816bc7cecefaac0b" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t26a541bd774941d89e22bda14a90dc49" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tb769c57945584fbca7e3440206077f1d"><clipPath id="t3a402f4651ac4e8f8fc6a29649b70ab2"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t3a402f4651ac4e8f8fc6a29649b70ab2)"><g class="toyplot-mark-Plot" id="tf03c747c4e754002802c5e84ccffc132" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 127.11111111111111 L 91.666666666666657 137.33333333333331 L 133.33333333333331 119.77777777777779 L 175.0 141.55555555555554 L 216.66666666666666 160.22222222222223 L 258.33333333333337 181.99999999999997 L 300.0 178.22222222222223 L 341.66666666666669 132.0 L 383.33333333333331 99.555555555555557 L 425.0 95.555555555555543 L 466.66666666666669 57.333333333333329 L 508.33333333333331 126.22222222222221" style="stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t0bfc71f6fc49461781e6b32ff33d70b3" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="458.3333333333333" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(166.66666666666666,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">4</text></g><g transform="translate(333.3333333333333,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">8</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">12</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t94abafa8429e4a77970c389ca7663c55" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="68.0" x2="192.66666666666669" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="-4.4408920985e-16">0</text></g><g transform="translate(66.66666666666666,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">300</text></g><g transform="translate(133.33333333333331,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">600</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">900</text></g></g><g transform="translate(100.0,-22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-28.35" y="0.0">Deliveries</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t4b9c1ae128f74913ba96e37f9a26a8b3"><clipPath id="tdf6f0c6ddeb446fa985f7201c37f817a"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tdf6f0c6ddeb446fa985f7201c37f817a)"><g class="toyplot-mark-Plot" id="t23e38f852c2c4baeacbf494c5b5d4526" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 50.0 L 91.666666666666657 50.0 L 133.33333333333331 50.0 L 175.0 50.0 L 216.66666666666666 50.0 L 258.33333333333337 50.0 L 300.0 74.643320363164605 L 341.66666666666669 60.635538261997389 L 383.33333333333331 153.76134889753581 L 425.0 147.53566796368352 L 466.66666666666669 250.0 L 508.33333333333331 79.053177691309969" style="stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="tbd5fa32649844a8485e0e099313c8567" transform="translate(550.0,250.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(5.447470817120602,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.73" y="8.555">0.93</text></g><g transform="translate(70.29831387808049,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.73" y="8.555">0.95</text></g><g transform="translate(135.14915693904038,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.73" y="8.555">0.98</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-9.73" y="8.555">1.00</text></g></g><g transform="translate(100.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-24.006" y="10.266">On Time</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g transform="translate(300.0,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-100.87" y="-4.823">Deliveries (</text><g style="fill:rgb(54.5%,0%,0%);fill-opacity:1.0;stroke:rgb(54.5%,0%,0%);stroke-opacity:1.0;stroke-width:2.0" transform="translate(-19.690999999999995, -8.4000000000000004)"><line transform="rotate(45)" y1="-6.4750000000000005" y2="6.4750000000000005"></line></g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.216" y="-4.823">) vs. On Time (</text><g style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;stroke:rgb(27.5%,51%,70.6%);stroke-opacity:1.0;stroke-width:2.0" transform="translate(89.733000000000004, -8.4000000000000004)"><line transform="rotate(45)" y1="-6.4750000000000005" y2="6.4750000000000005"></line></g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="96.208" y="-4.823">)</text></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t7289ce7c41904dc2816bc7cecefaac0b";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t26a541bd774941d89e22bda14a90dc49";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tf03c747c4e754002802c5e84ccffc132","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [553.0, 507.0, 586.0, 488.0, 404.0, 306.0, 323.0, 531.0, 677.0, 695.0, 867.0, 557.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t0bfc71f6fc49461781e6b32ff33d70b3",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 12.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t94abafa8429e4a77970c389ca7663c55",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 900.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t23e38f852c2c4baeacbf494c5b5d4526","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9905, 0.9959, 0.96, 0.9624, 0.9229, 0.9888]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tbd5fa32649844a8485e0e099313c8567",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.9229}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>

