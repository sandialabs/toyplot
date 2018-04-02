
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

    <div class="toyplot" id="t5880c3b4f6494088a53eb2615a5756f2" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tc12b138241244546a30dfcaebb2067b2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tcfe7214ab4194e098c322b60e4f7ee79"><clipPath id="t77a22469b9484e379baafa0a6ec18728"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t77a22469b9484e379baafa0a6ec18728)"><g class="toyplot-mark-BarBoundaries" id="t383446da0ee34f5b94133fa4bc40046c" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="97.67891348851099" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="113.80008467423374" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.51219512195122" y="112.07959125518579"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="90.14285877392345" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="89.02439024390245" y="100.7543816470619"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="118.2145440939794" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.9541478539101"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="133.84987050060198" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="128.0487804878049" y="85.75797927759818"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="88.58042366648482" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="147.5609756097561" y="109.59073712941199"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="104.21287561873288" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="167.0731707317073" y="94.32594553170156"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="90.92661703769537" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="104.01593450275429" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="206.09756097560978" y="105.77478053571998"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="150.68872189008744" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="225.609756097561" y="89.213744165718"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="86.02832062773588" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="245.1219512195122" y="108.6378697093332"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="97.9398884169506" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="264.6341463414634" y="98.83416461848037"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="107.92339259707052" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.1463414634146" y="89.36561902809706"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="147.5625743443018" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="303.6585365853659" y="89.38748992496448"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="122.63726209990583" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="323.1707317073171" y="91.81710277753547"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="105.01053413958454" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="102.92346056264034" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195115" x="362.19512195121956" y="101.67049394975712"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="98.50817671215556" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.7073170731707" y="107.63726407477729"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="100.27355361155676" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="401.219512195122" y="92.1110038267181"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="159.17154758256362" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="420.7317073170732" y="71.45385979382624"><title>Employee Schedule</title></rect></g></g></g><g class="toyplot-coordinates-Axis" id="t9e8cf5b096974154a3d842cc0d0ebb63" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><g transform="translate(9.75609756097561,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(204.8780487804878,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(400.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t0a3c49d7c3154d569fb4d65588f65a71" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="-4.440892098500626e-16">5</text></g><g transform="translate(66.66666666666666,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">10</text></g><g transform="translate(133.33333333333331,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">15</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t5880c3b4f6494088a53eb2615a5756f2";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tc12b138241244546a30dfcaebb2067b2";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t383446da0ee34f5b94133fa4bc40046c","data","bar data",["left", "right", "boundary1"],[[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t9e8cf5b096974154a3d842cc0d0ebb63",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t0a3c49d7c3154d569fb4d65588f65a71",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


If your plot includes multiple series, you can assign a per-series title
instead. Hover the mouse over both series in the following plot to see
"Morning Schedule" and "Afternoon Schedule":

.. code:: python

    lunch = numpy.random.normal(loc=12, scale=0.5, size=20)
    boundaries = numpy.column_stack((start, lunch, end))
    title = ["Morning Schedule", "Afternoon Schedule"]
    
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);



.. raw:: html

    <div class="toyplot" id="taf4545d87b2b405aa23fde2cb5a76e22" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t0d7e9b37113441c5ba0a5892a5798521" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="te6b0069bf7d242c0bf22c3abae19a8b8"><clipPath id="t7707c03684384b73b9e66d17ee402b46"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t7707c03684384b73b9e66d17ee402b46)"><g class="toyplot-mark-BarBoundaries" id="t40b36709e5874ec5a556fa49ebeeeab0" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="65.43670305965315" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.51219512195122" y="160.44297286976638"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="34.47151999887919" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="89.02439024390245" y="156.42572042210617"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="43.66884127662263" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="64.59313110985713" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="128.0487804878049" y="155.01471866834305"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="35.52344889963217" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="147.5609756097561" y="162.64771189626464"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="167.0731707317073" y="157.57863222174234"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="61.94224133455944" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="58.16014158779518" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="206.09756097560978" y="151.6305734506791"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="84.67092326226842" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="225.609756097561" y="155.23154279353702"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="43.60624896994503" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="245.1219512195122" y="151.05994136712405"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="264.6341463414634" y="166.30540051362874"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.1463414634146" y="166.0131552100056"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="79.6106096029402" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="303.6585365853659" y="157.33945466632608"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="54.13274854952891" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="323.1707317073171" y="160.32161632791238"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="52.34095841509097" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195115" x="362.19512195121956" y="154.30653111867178"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="49.24202061841194" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.7073170731707" y="156.9034201685209"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="401.219512195122" y="152.8950779595827"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="84.26313274056022" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="420.7317073170732" y="146.36227463582964"><title>Morning Schedule</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.1233850860293" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="48.36338161458059" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.51219512195122" y="112.07959125518579"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="55.67133877504426" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="89.02439024390245" y="100.7543816470619"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="74.54570281735677" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.9541478539101"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="69.25673939074487" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="128.0487804878049" y="85.75797927759818"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="53.05697476685265" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="147.5609756097561" y="109.59073712941199"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="167.0731707317073" y="94.32594553170156"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="206.09756097560978" y="105.77478053571998"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="66.01779862781902" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="225.609756097561" y="89.213744165718"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="42.42207165779085" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="245.1219512195122" y="108.6378697093332"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="67.47123589514837" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="264.6341463414634" y="98.83416461848037"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="76.64753618190855" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.1463414634146" y="89.36561902809706"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="67.95196474136159" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="303.6585365853659" y="89.38748992496448"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="68.50451355037691" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="323.1707317073171" y="91.81710277753547"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="52.66957572449357" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="52.63603716891467" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195115" x="362.19512195121956" y="101.67049394975712"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="49.26615609374362" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.7073170731707" y="107.63726407477729"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="60.78407413286459" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="401.219512195122" y="92.1110038267181"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="74.9084148420034" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="420.7317073170732" y="71.45385979382624"><title>Afternoon Schedule</title></rect></g></g></g><g class="toyplot-coordinates-Axis" id="teebff9e77bdb45e1a378597139a4a384" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><g transform="translate(9.75609756097561,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(204.8780487804878,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(400.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t90aec955c4be4dcab9166d5f08ca2c69" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="-4.440892098500626e-16">5</text></g><g transform="translate(66.66666666666666,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">10</text></g><g transform="translate(133.33333333333331,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">15</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "taf4545d87b2b405aa23fde2cb5a76e22";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t0d7e9b37113441c5ba0a5892a5798521";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t40b36709e5874ec5a556fa49ebeeeab0","data","bar data",["left", "right", "boundary1", "boundary2"],[[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"teebff9e77bdb45e1a378597139a4a384",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t90aec955c4be4dcab9166d5f08ca2c69",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Finally, you can assign a title for every datum:

.. code:: python

    title = numpy.column_stack((
            ["Employee %s Morning" % i for i in range(20)],
            ["Employee %s Afternoon" % i for i in range(20)]
            ))
    
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);



.. raw:: html

    <div class="toyplot" id="tb9fb1ce5d4974085a6db6ca066a15ee1" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tff71e1cc689e4ef49ad3f4e3665ba177" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t30df19d39f7e469fb80e8bd21962e006"><clipPath id="t35c5e73213af4533905916c34c38c757"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t35c5e73213af4533905916c34c38c757)"><g class="toyplot-mark-BarBoundaries" id="t5829251762ec47c19135704c61ef1c96" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.43670305965315" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.51219512195122" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.47151999887919" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="89.02439024390245" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.66884127662263" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.59313110985713" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="128.0487804878049" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.52344889963217" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="167.0731707317073" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.94224133455944" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.16014158779518" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="206.09756097560978" y="151.6305734506791"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.67092326226842" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="225.609756097561" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.60624896994503" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="264.6341463414634" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.1463414634146" y="166.0131552100056"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.6106096029402" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="303.6585365853659" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.13274854952891" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="323.1707317073171" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.34095841509097" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195115" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.24202061841194" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.7073170731707" y="156.9034201685209"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="401.219512195122" y="152.8950779595827"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.26313274056022" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="420.7317073170732" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.1233850860293" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.36338161458059" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.51219512195122" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.67133877504426" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="89.02439024390245" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.54570281735677" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.9541478539101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.25673939074487" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="128.0487804878049" y="85.75797927759818"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.05697476685265" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="167.0731707317073" y="94.32594553170156"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.01779862781902" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="225.609756097561" y="89.213744165718"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.42207165779085" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.47123589514837" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="264.6341463414634" y="98.83416461848037"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.64753618190855" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.1463414634146" y="89.36561902809706"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.95196474136159" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="303.6585365853659" y="89.38748992496448"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.50451355037691" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="323.1707317073171" y="91.81710277753547"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.66957572449357" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.63603716891467" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195115" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.26615609374362" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.7073170731707" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.78407413286459" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="401.219512195122" y="92.1110038267181"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.9084148420034" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="420.7317073170732" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-coordinates-Axis" id="t42711f5610c742f0acd75090f94f1d4a" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><g transform="translate(9.75609756097561,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(204.8780487804878,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(400.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="ta9d6efb18594434ba618efe57ec47349" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="-4.440892098500626e-16">5</text></g><g transform="translate(66.66666666666666,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">10</text></g><g transform="translate(133.33333333333331,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">15</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tb9fb1ce5d4974085a6db6ca066a15ee1";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tff71e1cc689e4ef49ad3f4e3665ba177";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t5829251762ec47c19135704c61ef1c96","data","bar data",["left", "right", "boundary1", "boundary2"],[[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t42711f5610c742f0acd75090f94f1d4a",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"ta9d6efb18594434ba618efe57ec47349",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Of course, the title attribute works with all types of visualizations.

Coordinates
~~~~~~~~~~~

When you click or tap the above figures, you should also see the domain
values for the point you chose displayed along each of the axes. If you
wish to disable display of either or both of the values, you can do so
using the individual axes:

.. code:: python

    canvas, axes, mark = toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300)
    axes.x.interactive.coordinates.show = False
    axes.y.interactive.coordinates.show = False



.. raw:: html

    <div class="toyplot" id="t9bd1cee87521464f8646d58b60f25f29" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t18f0894a00d1466e882049e6875c8716" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tbe9ec4d9264c41debbecc7501d423a17"><clipPath id="t0a4a27e2331e4560bfe859768e9d03c2"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t0a4a27e2331e4560bfe859768e9d03c2)"><g class="toyplot-mark-BarBoundaries" id="t018b6807cb5b4494be3ffe5c5c753fa4" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.43670305965315" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.51219512195122" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.47151999887919" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="89.02439024390245" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.66884127662263" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.59313110985713" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="128.0487804878049" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.52344889963217" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="167.0731707317073" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.94224133455944" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.16014158779518" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="206.09756097560978" y="151.6305734506791"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.67092326226842" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="225.609756097561" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.60624896994503" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="264.6341463414634" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.1463414634146" y="166.0131552100056"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.6106096029402" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="303.6585365853659" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.13274854952891" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="323.1707317073171" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.34095841509097" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195115" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.24202061841194" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.7073170731707" y="156.9034201685209"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="401.219512195122" y="152.8950779595827"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.26313274056022" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="420.7317073170732" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.1233850860293" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.36338161458059" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.51219512195122" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.67133877504426" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="89.02439024390245" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.54570281735677" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.9541478539101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.25673939074487" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="128.0487804878049" y="85.75797927759818"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.05697476685265" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="167.0731707317073" y="94.32594553170156"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.01779862781902" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="225.609756097561" y="89.213744165718"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.42207165779085" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.47123589514837" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="264.6341463414634" y="98.83416461848037"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.64753618190855" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.1463414634146" y="89.36561902809706"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.95196474136159" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="303.6585365853659" y="89.38748992496448"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.50451355037691" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="323.1707317073171" y="91.81710277753547"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.66957572449357" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.63603716891467" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195115" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.26615609374362" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.7073170731707" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.78407413286459" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="401.219512195122" y="92.1110038267181"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.9084148420034" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="420.7317073170732" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-coordinates-Axis" id="t08dbfb6995b548b09fadce55c2359968" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><g transform="translate(9.75609756097561,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(204.8780487804878,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(400.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g></g><g class="toyplot-coordinates-Axis" id="te4d75bf760eb4c629b0a6e93b4a1c8e9" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="-4.440892098500626e-16">5</text></g><g transform="translate(66.66666666666666,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">10</text></g><g transform="translate(133.33333333333331,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">15</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">20</text></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t9bd1cee87521464f8646d58b60f25f29";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t18f0894a00d1466e882049e6875c8716";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t018b6807cb5b4494be3ffe5c5c753fa4","data","bar data",["left", "right", "boundary1", "boundary2"],[[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t08dbfb6995b548b09fadce55c2359968",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"te4d75bf760eb4c629b0a6e93b4a1c8e9",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Now when you click or tap, nothing happens.

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

    toyplot.bars(boundaries, baseline=None, filename="employee-schedules", title=title, width=500, height=300);



.. raw:: html

    <div class="toyplot" id="t6f12da43a96c4a9ca11ae9d9f7fc43e7" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t15807cf8981343afa5f3ee8ef66b7318" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t65e274fceb49460699012f0375d76e25"><clipPath id="t48ab9e7b301b459ea5b2516f885ff3f0"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t48ab9e7b301b459ea5b2516f885ff3f0)"><g class="toyplot-mark-BarBoundaries" id="t8399e811b5d04578b8c79259485afb43" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.43670305965315" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.51219512195122" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.47151999887919" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="89.02439024390245" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.66884127662263" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.59313110985713" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="128.0487804878049" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.52344889963217" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="167.0731707317073" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.94224133455944" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.16014158779518" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="206.09756097560978" y="151.6305734506791"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.67092326226842" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="225.609756097561" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.60624896994503" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="264.6341463414634" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.1463414634146" y="166.0131552100056"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.6106096029402" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="303.6585365853659" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.13274854952891" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="323.1707317073171" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.34095841509097" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195115" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.24202061841194" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.7073170731707" y="156.9034201685209"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="401.219512195122" y="152.8950779595827"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.26313274056022" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="420.7317073170732" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.1233850860293" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.36338161458059" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.51219512195122" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.67133877504426" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="89.02439024390245" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.54570281735677" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.9541478539101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.25673939074487" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="128.0487804878049" y="85.75797927759818"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.05697476685265" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="167.0731707317073" y="94.32594553170156"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.01779862781902" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="225.609756097561" y="89.213744165718"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.42207165779085" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.47123589514837" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="264.6341463414634" y="98.83416461848037"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.64753618190855" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.1463414634146" y="89.36561902809706"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.95196474136159" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="303.6585365853659" y="89.38748992496448"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.50451355037691" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="323.1707317073171" y="91.81710277753547"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.66957572449357" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.63603716891467" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195115" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.26615609374362" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.7073170731707" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.78407413286459" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="401.219512195122" y="92.1110038267181"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.9084148420034" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.51219512195121" x="420.7317073170732" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-coordinates-Axis" id="t03bcc69e6939421d96b26ef164d75773" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><g transform="translate(9.75609756097561,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(204.8780487804878,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(400.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t32da9ee9fbf64aa7ab3d7563e095ad57" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="-4.440892098500626e-16">5</text></g><g transform="translate(66.66666666666666,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">10</text></g><g transform="translate(133.33333333333331,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">15</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t6f12da43a96c4a9ca11ae9d9f7fc43e7";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t15807cf8981343afa5f3ee8ef66b7318";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t8399e811b5d04578b8c79259485afb43","data","bar data",["left", "right", "boundary1", "boundary2"],[[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]],"employee-schedules");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t03bcc69e6939421d96b26ef164d75773",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t32da9ee9fbf64aa7ab3d7563e095ad57",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Note that the filename you specify should not include a file extension,
as the file extension is added for you (and other file formats may
become available in the future).
