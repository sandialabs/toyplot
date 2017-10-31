
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _communities-case-study:

Visualizing Community Detection in Graphs
=========================================

The following explores how Toyplot's graph visualization could be used
to support development of a hypothetical new community detection
algorithm:

Graph Data
----------

First, we will load some sample graph data provided by Toyplot in three
parts. The first part is an :math:`E \times 2` matrix containing the
source and target vertices for each of :math:`E` graph edges:

.. code:: python

    import toyplot.data
    
    edges, truth, assigned = toyplot.data.communities()
    edges




.. parsed-literal::

    array([[ 1,  2],
           [ 1,  3],
           [ 1,  4],
           [ 2,  3],
           [ 2,  4],
           [ 3,  4],
           [ 5,  6],
           [ 5,  7],
           [ 5,  8],
           [ 6,  7],
           [ 6,  8],
           [ 7,  8],
           [ 9, 10],
           [ 9, 11],
           [ 9, 12],
           [10, 11],
           [10, 12],
           [11, 12],
           [ 4,  5],
           [ 8,  9]])



Conveniently, Toyplot can display this matrix directly as a graph using
a force-directed layout, and inducing the vertex labels from the edge
data:

.. code:: python

    toyplot.graph(edges);



.. raw:: html

    <div class="toyplot" id="t6acbf1cc9bae4bb8a4feeca7d997b922" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t88ce4a705b7e4c65b020b1b7423b6cdc" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t5f4052243d9244a9bbd9c32418cc6338"><clipPath id="t6bc8a350bb7249ffbe2eecad25d3158a"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#t6bc8a350bb7249ffbe2eecad25d3158a)"><g class="toyplot-mark-Graph" id="t51e2a8de39eb40d88db70b450cebc19f"><g class="toyplot-Edges"><path d="M 211.683159957 50.0833032854 L 251.05908869 51.724799902" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.408108879 51.9807546865 L 204.254976874 88.8578543352" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 210.892222248 51.5944786897 L 264.043153594 121.789256034" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 251.491999676 53.0529600978 L 205.543543585 89.5937521113" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.393220568 53.7796997559 L 264.914612782 121.412138155" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 205.744490632 91.7767895607 L 263.484179824 122.445554184" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 337.934581351 230.666482776 L 390.65894536 252.490745365" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 337.536998577 231.27867918 L 394.57144914 285.432909996" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.558916258 231.844999696 L 360.596811008 330.761600386" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 392.71525477 255.244783224 L 395.813443857 284.820911675" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.771012701 255.115367539 L 361.804965476 330.845338265" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 394.810050397 288.401140506 L 362.280848786 331.113926334" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 346.37565378 461.459698412 L 309.266322259 514.757272819" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 348.116794929 461.72676309 L 368.567122483 526.953789361" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.158215156 461.785649014 L 331.364760227 548.032712053" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 310.083083667 516.798716396 L 367.205884826 528.462085151" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 309.249211731 518.051729527 L 329.878814734 548.346880637" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 367.415921144 529.831279368 L 332.754046693 549.030912015" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 266.357977878 125.049102266 L 334.979140294 228.236193666" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 360.857085131 334.69377068 L 347.730466714 457.829629259" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(209.68489556942228, 50.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(253.05735307750501, 51.808103187400434)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(203.97819018335846, 90.838609021709999)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(265.25048027263921, 123.38373472339872)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(336.08663789994222, 229.90156120908347)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(392.50688881059352, 253.25566693133214)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(396.02180981664145, 286.81002796763073)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(361.06908936632647, 332.70503887250106)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(347.51846247830969, 459.81836106732754)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(308.12351356081211, 516.39861016382122)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(369.16545493310974, 528.86219138304273)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(331.00451290448143, 550.0)"><circle r="2.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(209.68489556942228,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">1</text></g><g class="toyplot-Datum" transform="translate(253.05735307750501,51.808103187400434)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">2</text></g><g class="toyplot-Datum" transform="translate(203.97819018335846,90.838609021709999)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">3</text></g><g class="toyplot-Datum" transform="translate(265.25048027263921,123.38373472339872)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">4</text></g><g class="toyplot-Datum" transform="translate(336.08663789994222,229.90156120908347)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">5</text></g><g class="toyplot-Datum" transform="translate(392.50688881059352,253.25566693133214)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">6</text></g><g class="toyplot-Datum" transform="translate(396.02180981664145,286.81002796763073)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">7</text></g><g class="toyplot-Datum" transform="translate(361.06908936632647,332.70503887250106)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">8</text></g><g class="toyplot-Datum" transform="translate(347.51846247830969,459.81836106732754)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">9</text></g><g class="toyplot-Datum" transform="translate(308.12351356081211,516.39861016382122)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">10</text></g><g class="toyplot-Datum" transform="translate(369.16545493310974,528.86219138304273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">11</text></g><g class="toyplot-Datum" transform="translate(331.00451290448143,550.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">12</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t6acbf1cc9bae4bb8a4feeca7d997b922";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t88ce4a705b7e4c65b020b1b7423b6cdc";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t51e2a8de39eb40d88db70b450cebc19f","vertex_data","graph vertex data",["x", "y"],[[-0.22126767335038133, 0.0029659671685047504, -0.250771081679212, 0.06600388241149634, 0.4322236084249407, 0.7239137497623711, 0.7420857321356447, 0.5613817507863635, 0.4913256236267057, 0.2876555223376603, 0.6032395939964988, 0.40594925242166796], [1.3755143398163583, 1.3661665282456386, 1.1643805811871888, 0.9961237556228442, 0.44543141801220687, 0.3246917493829421, 0.15121722285762035, -0.08605790444950144, -0.7432280218883004, -1.0357453465985238, -1.100181496894319, -1.2094630098887935]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t51e2a8de39eb40d88db70b450cebc19f","edge_data","graph edge data",["source", "target"],[[0, 0, 0, 1, 1, 2, 4, 4, 4, 5, 5, 6, 8, 8, 8, 9, 9, 10, 3, 7], [1, 2, 3, 2, 3, 3, 5, 6, 7, 6, 7, 7, 9, 10, 11, 10, 11, 11, 4, 8]],"toyplot");
    })();</script></div></div>


Ground Truth Communities
------------------------

The second part of the data we loaded is a set of ground truth community
assignments in the form of a :math:`V \times 2` matrix containing the
vertex ID and community ID for each of :math:`V` vertices (note that in
this case the assignments are already sorted in ID order, if they hadn't
been, we'd need to sort them explicitly):

.. code:: python

    truth




.. parsed-literal::

    array([[ 1,  1],
           [ 2,  1],
           [ 3,  1],
           [ 4,  1],
           [ 5,  2],
           [ 6,  2],
           [ 7,  2],
           [ 8,  2],
           [ 9,  3],
           [10,  3],
           [11,  3],
           [12,  3]])



We want to color each graph vertex by its community ID, so we create an
appropriate categorical colormap:

.. code:: python

    colormap = toyplot.color.brewer.map("Set2")
    colormap




.. raw:: html

    <div class="toyplot-color-CategoricalMap" style="overflow:hidden; height:auto"><div style="float:left;width:20px;height:20px;margin-right:0px;background-color:rgba(40.0%,76.1%,64.7%,1.000)"></div><div style="float:left;width:20px;height:20px;margin-right:0px;background-color:rgba(98.8%,55.3%,38.4%,1.000)"></div><div style="float:left;width:20px;height:20px;margin-right:0px;background-color:rgba(55.3%,62.7%,79.6%,1.000)"></div><div style="float:left;width:20px;height:20px;margin-right:0px;background-color:rgba(90.6%,54.1%,76.5%,1.000)"></div><div style="float:left;width:20px;height:20px;margin-right:0px;background-color:rgba(65.1%,84.7%,32.9%,1.000)"></div><div style="float:left;width:20px;height:20px;margin-right:0px;background-color:rgba(100.0%,85.1%,18.4%,1.000)"></div><div style="float:left;width:20px;height:20px;margin-right:0px;background-color:rgba(89.8%,76.9%,58.0%,1.000)"></div><div style="float:left;width:20px;height:20px;margin-right:0px;background-color:rgba(70.2%,70.2%,70.2%,1.000)"></div></div>



Now we can rerender the graph, overriding the default edge color, vertex
size, vertex label style, and vertex color:

.. code:: python

    ecolor = "lightgray"
    vlstyle = {"fill":"white"}
    vcolor = truth[:,1]
    toyplot.graph(edges, ecolor=ecolor, vsize=20, vlstyle=vlstyle, vcolor=(vcolor, colormap));



.. raw:: html

    <div class="toyplot" id="t703e0a8a20f2457297eb59a22b3d1886" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="tde03b5fd862a4b008b1f74257da9c2af" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t03ce541ec53c4ed8b589a7e4a3cec374"><clipPath id="t2e7c0e1a5eb64d43b045e15f48d0bc2a"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#t2e7c0e1a5eb64d43b045e15f48d0bc2a)"><g class="toyplot-mark-Graph" id="t89e7930435f54851b9d77f9fbc123493"><g class="toyplot-Edges"><path d="M 219.676217507 50.4165164272 L 243.06603114 51.3915867602" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 208.300962117 59.9037734323 L 205.362123636 80.9348355894" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 215.721528961 57.9723934483 L 259.213846881 115.411341275" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.230586068 58.0323877392 L 211.804957193 84.6143244699" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 254.736690529 61.6660860299 L 263.571142821 113.525751881" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 212.809692429 95.5295117166 L 256.418978027 118.692832028" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 345.326355153 233.726169042 L 383.267171557 249.431059098" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 343.338441284 236.787151066 L 388.770006433 279.924438111" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 338.448029692 239.618753643 L 358.707697574 322.987846438" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 393.548718609 263.201248396 L 394.979980018 276.864446503" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 388.827508262 262.554169971 L 364.748469915 323.406535833" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 389.96301272 294.76559066 L 367.127886463 324.74947618" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.804418985 468.02504779 L 313.837557054 508.191923442" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 350.51012473 469.360371179 L 366.173792681 519.320181271" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 345.717225866 469.654800803 L 332.805749516 540.163560265" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 317.921364094 518.399141326 L 359.3676044 526.861660221" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 313.752004413 524.66420698 L 325.376022052 541.734403184" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 360.417785989 533.707631306 L 339.752181849 545.154560077" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 270.787968301 131.710572439 L 330.549149872 221.574723494" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 360.009068188 342.648697912 L 348.578483656 449.874702027" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0" transform="translate(209.68489556942228, 50.0)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0" transform="translate(253.05735307750501, 51.808103187400434)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0" transform="translate(203.97819018335846, 90.838609021709999)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0" transform="translate(265.25048027263921, 123.38373472339872)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(336.08663789994222, 229.90156120908347)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(392.50688881059352, 253.25566693133214)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(396.02180981664145, 286.81002796763073)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(361.06908936632647, 332.70503887250106)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0" transform="translate(347.51846247830969, 459.81836106732754)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0" transform="translate(308.12351356081211, 516.39861016382122)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0" transform="translate(369.16545493310974, 528.86219138304273)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0" transform="translate(331.00451290448143, 550.0)"><circle r="10.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(209.68489556942228,50.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">1</text></g><g class="toyplot-Datum" transform="translate(253.05735307750501,51.808103187400434)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">2</text></g><g class="toyplot-Datum" transform="translate(203.97819018335846,90.838609021709999)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">3</text></g><g class="toyplot-Datum" transform="translate(265.25048027263921,123.38373472339872)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">4</text></g><g class="toyplot-Datum" transform="translate(336.08663789994222,229.90156120908347)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">5</text></g><g class="toyplot-Datum" transform="translate(392.50688881059352,253.25566693133214)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">6</text></g><g class="toyplot-Datum" transform="translate(396.02180981664145,286.81002796763073)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">7</text></g><g class="toyplot-Datum" transform="translate(361.06908936632647,332.70503887250106)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">8</text></g><g class="toyplot-Datum" transform="translate(347.51846247830969,459.81836106732754)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">9</text></g><g class="toyplot-Datum" transform="translate(308.12351356081211,516.39861016382122)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">10</text></g><g class="toyplot-Datum" transform="translate(369.16545493310974,528.86219138304273)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">11</text></g><g class="toyplot-Datum" transform="translate(331.00451290448143,550.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">12</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t703e0a8a20f2457297eb59a22b3d1886";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tde03b5fd862a4b008b1f74257da9c2af";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t89e7930435f54851b9d77f9fbc123493","vertex_data","graph vertex data",["x", "y"],[[-0.22126767335038133, 0.0029659671685047504, -0.250771081679212, 0.06600388241149634, 0.4322236084249407, 0.7239137497623711, 0.7420857321356447, 0.5613817507863635, 0.4913256236267057, 0.2876555223376603, 0.6032395939964988, 0.40594925242166796], [1.3755143398163583, 1.3661665282456386, 1.1643805811871888, 0.9961237556228442, 0.44543141801220687, 0.3246917493829421, 0.15121722285762035, -0.08605790444950144, -0.7432280218883004, -1.0357453465985238, -1.100181496894319, -1.2094630098887935]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t89e7930435f54851b9d77f9fbc123493","edge_data","graph edge data",["source", "target"],[[0, 0, 0, 1, 1, 2, 4, 4, 4, 5, 5, 6, 8, 8, 8, 9, 9, 10, 3, 7], [1, 2, 3, 2, 3, 3, 5, 6, 7, 6, 7, 7, 9, 10, 11, 10, 11, 11, 4, 8]],"toyplot");
    })();</script></div></div>


Assigned Communities
--------------------

Next, we render the graph again using the third part of the loaded data:
a different set of community ID values, generated using a hypothetical
community detection algorithm that we are working on:

.. code:: python

    assigned




.. parsed-literal::

    array([[ 1,  4],
           [ 2,  1],
           [ 3,  1],
           [ 4,  1],
           [ 5,  2],
           [ 6,  2],
           [ 7,  2],
           [ 8,  2],
           [ 9,  2],
           [10,  2],
           [11,  2],
           [12,  2]])



.. code:: python

    vcolor = assigned[:,1]
    toyplot.graph(edges, ecolor=ecolor, vsize=20, vlstyle=vlstyle, vcolor=(vcolor, colormap));



.. raw:: html

    <div class="toyplot" id="t10cfb9f2774b455e8368deec4022d853" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t6b552948c40e4afb9f7fb859a4790ae4" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t2e8558b8f24e4f119fffe80083cea5f1"><clipPath id="tac0116d192a74636a1405609760361c5"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#tac0116d192a74636a1405609760361c5)"><g class="toyplot-mark-Graph" id="t59ec408010834b91ad681994093a7c23"><g class="toyplot-Edges"><path d="M 219.676217507 50.4165164272 L 243.06603114 51.3915867602" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 208.300962117 59.9037734323 L 205.362123636 80.9348355894" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 215.721528961 57.9723934483 L 259.213846881 115.411341275" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.230586068 58.0323877392 L 211.804957193 84.6143244699" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 254.736690529 61.6660860299 L 263.571142821 113.525751881" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 212.809692429 95.5295117166 L 256.418978027 118.692832028" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 345.326355153 233.726169042 L 383.267171557 249.431059098" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 343.338441284 236.787151066 L 388.770006433 279.924438111" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 338.448029692 239.618753643 L 358.707697574 322.987846438" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 393.548718609 263.201248396 L 394.979980018 276.864446503" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 388.827508262 262.554169971 L 364.748469915 323.406535833" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 389.96301272 294.76559066 L 367.127886463 324.74947618" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.804418985 468.02504779 L 313.837557054 508.191923442" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 350.51012473 469.360371179 L 366.173792681 519.320181271" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 345.717225866 469.654800803 L 332.805749516 540.163560265" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 317.921364094 518.399141326 L 359.3676044 526.861660221" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 313.752004413 524.66420698 L 325.376022052 541.734403184" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 360.417785989 533.707631306 L 339.752181849 545.154560077" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 270.787968301 131.710572439 L 330.549149872 221.574723494" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 360.009068188 342.648697912 L 348.578483656 449.874702027" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(65.1%,84.7%,32.9%);stroke-opacity:1.0" transform="translate(209.68489556942228, 50.0)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0" transform="translate(253.05735307750501, 51.808103187400434)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0" transform="translate(203.97819018335846, 90.838609021709999)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0" transform="translate(265.25048027263921, 123.38373472339872)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(336.08663789994222, 229.90156120908347)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(392.50688881059352, 253.25566693133214)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(396.02180981664145, 286.81002796763073)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(361.06908936632647, 332.70503887250106)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(347.51846247830969, 459.81836106732754)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(308.12351356081211, 516.39861016382122)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(369.16545493310974, 528.86219138304273)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(331.00451290448143, 550.0)"><circle r="10.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(209.68489556942228,50.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">1</text></g><g class="toyplot-Datum" transform="translate(253.05735307750501,51.808103187400434)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">2</text></g><g class="toyplot-Datum" transform="translate(203.97819018335846,90.838609021709999)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">3</text></g><g class="toyplot-Datum" transform="translate(265.25048027263921,123.38373472339872)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">4</text></g><g class="toyplot-Datum" transform="translate(336.08663789994222,229.90156120908347)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">5</text></g><g class="toyplot-Datum" transform="translate(392.50688881059352,253.25566693133214)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">6</text></g><g class="toyplot-Datum" transform="translate(396.02180981664145,286.81002796763073)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">7</text></g><g class="toyplot-Datum" transform="translate(361.06908936632647,332.70503887250106)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">8</text></g><g class="toyplot-Datum" transform="translate(347.51846247830969,459.81836106732754)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">9</text></g><g class="toyplot-Datum" transform="translate(308.12351356081211,516.39861016382122)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">10</text></g><g class="toyplot-Datum" transform="translate(369.16545493310974,528.86219138304273)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">11</text></g><g class="toyplot-Datum" transform="translate(331.00451290448143,550.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">12</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t10cfb9f2774b455e8368deec4022d853";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t6b552948c40e4afb9f7fb859a4790ae4";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t59ec408010834b91ad681994093a7c23","vertex_data","graph vertex data",["x", "y"],[[-0.22126767335038133, 0.0029659671685047504, -0.250771081679212, 0.06600388241149634, 0.4322236084249407, 0.7239137497623711, 0.7420857321356447, 0.5613817507863635, 0.4913256236267057, 0.2876555223376603, 0.6032395939964988, 0.40594925242166796], [1.3755143398163583, 1.3661665282456386, 1.1643805811871888, 0.9961237556228442, 0.44543141801220687, 0.3246917493829421, 0.15121722285762035, -0.08605790444950144, -0.7432280218883004, -1.0357453465985238, -1.100181496894319, -1.2094630098887935]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t59ec408010834b91ad681994093a7c23","edge_data","graph edge data",["source", "target"],[[0, 0, 0, 1, 1, 2, 4, 4, 4, 5, 5, 6, 8, 8, 8, 9, 9, 10, 3, 7], [1, 2, 3, 2, 3, 3, 5, 6, 7, 6, 7, 7, 9, 10, 11, 10, 11, 11, 4, 8]],"toyplot");
    })();</script></div></div>


We want to compare the ground truth communities with the communities
assigned by our algorithm, but there are two challenges:

-  Flipping back-and-forth between the two visualizations and trying to
   understand what changed is extremely difficult.
-  Even if the algorithm we're testing arrives at identical community
   memberships across the graph, it is unlikely that it would happen to
   assign the same ID for each community ... so even in the best case,
   the vertex colors won't match the ground truth.

What we need is a way to highlight the *differences* between the two
sets of communities, so we only have to look at a single visualization.
The following is suggested by Jon Berry at Sandia National Laboratories:

Highlighting Edge Types
-----------------------

We will render the graph using the vertex colors assigned by the
algorithm, but with the edges colored using a set of rules that
highlight the differences between the ground truth and assigned
communities:

-  Edges that are intra-community in both ground truth and assigned
   communities remain light gray.
-  Edges that are inter-community in both ground truth and assigned
   communities remain light gray.
-  Edges that are intra-community in the ground truth but
   inter-community for the assigned communities are displayed red (i.e.
   the assignment split up a ground truth community).
-  Edges that are inter-community in the ground truth but
   intra-community for the assigned communities are displayed green
   (i.e. the assignment merged two ground-truth communities).

.. code:: python

    truth_map = dict(truth.tolist())
    assigned_map = dict(assigned.tolist())
    
    truth_source = [truth_map[vertex] for vertex in edges[:,0]]
    truth_target = [truth_map[vertex] for vertex in edges[:,1]]
    
    assigned_source = [assigned_map[vertex] for vertex in edges[:,0]]
    assigned_target = [assigned_map[vertex] for vertex in edges[:,1]]

.. code:: python

    import numpy
    
    # Default all edges to light gray.
    ecolor = numpy.repeat("lightgray", len(edges))
    
    selection = numpy.equal(truth_source, truth_target) & numpy.not_equal(assigned_source, assigned_target)
    ecolor[selection] = "red"
    
    selection = numpy.not_equal(truth_source, truth_target) & numpy.equal(assigned_source, assigned_target)
    ecolor[selection] = "green"
    
    canvas, axes, mark = toyplot.graph(edges, ecolor=ecolor, vsize=20, vlstyle=vlstyle, vcolor=(vcolor, colormap));



.. raw:: html

    <div class="toyplot" id="t45775f23dfa242baa18b3da8ee325a6e" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="tf1b31ff3cfa04753addd71da71ed8103" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t264cbf71487046b1aebe18e3adf4cdbb"><clipPath id="te6013b6793b246ac98312d1dacc743e9"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#te6013b6793b246ac98312d1dacc743e9)"><g class="toyplot-mark-Graph" id="tfb1dedb4e38947c59e3ce7a8e8048c80"><g class="toyplot-Edges"><path d="M 219.676217507 50.4165164272 L 243.06603114 51.3915867602" style="fill:none;stroke:rgb(100%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 208.300962117 59.9037734323 L 205.362123636 80.9348355894" style="fill:none;stroke:rgb(100%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 215.721528961 57.9723934483 L 259.213846881 115.411341275" style="fill:none;stroke:rgb(100%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 245.230586068 58.0323877392 L 211.804957193 84.6143244699" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 254.736690529 61.6660860299 L 263.571142821 113.525751881" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 212.809692429 95.5295117166 L 256.418978027 118.692832028" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 345.326355153 233.726169042 L 383.267171557 249.431059098" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 343.338441284 236.787151066 L 388.770006433 279.924438111" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 338.448029692 239.618753643 L 358.707697574 322.987846438" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 393.548718609 263.201248396 L 394.979980018 276.864446503" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 388.827508262 262.554169971 L 364.748469915 323.406535833" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 389.96301272 294.76559066 L 367.127886463 324.74947618" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 341.804418985 468.02504779 L 313.837557054 508.191923442" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 350.51012473 469.360371179 L 366.173792681 519.320181271" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 345.717225866 469.654800803 L 332.805749516 540.163560265" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 317.921364094 518.399141326 L 359.3676044 526.861660221" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 313.752004413 524.66420698 L 325.376022052 541.734403184" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 360.417785989 533.707631306 L 339.752181849 545.154560077" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 270.787968301 131.710572439 L 330.549149872 221.574723494" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 360.009068188 342.648697912 L 348.578483656 449.874702027" style="fill:none;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(65.1%,84.7%,32.9%);stroke-opacity:1.0" transform="translate(209.68489556942228, 50.0)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0" transform="translate(253.05735307750501, 51.808103187400434)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0" transform="translate(203.97819018335846, 90.838609021709999)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0" transform="translate(265.25048027263921, 123.38373472339872)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(336.08663789994222, 229.90156120908347)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(392.50688881059352, 253.25566693133214)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(396.02180981664145, 286.81002796763073)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(361.06908936632647, 332.70503887250106)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(347.51846247830969, 459.81836106732754)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(308.12351356081211, 516.39861016382122)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(369.16545493310974, 528.86219138304273)"><circle r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0" transform="translate(331.00451290448143, 550.0)"><circle r="10.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(209.68489556942228,50.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">1</text></g><g class="toyplot-Datum" transform="translate(253.05735307750501,51.808103187400434)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">2</text></g><g class="toyplot-Datum" transform="translate(203.97819018335846,90.838609021709999)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">3</text></g><g class="toyplot-Datum" transform="translate(265.25048027263921,123.38373472339872)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">4</text></g><g class="toyplot-Datum" transform="translate(336.08663789994222,229.90156120908347)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">5</text></g><g class="toyplot-Datum" transform="translate(392.50688881059352,253.25566693133214)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">6</text></g><g class="toyplot-Datum" transform="translate(396.02180981664145,286.81002796763073)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">7</text></g><g class="toyplot-Datum" transform="translate(361.06908936632647,332.70503887250106)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">8</text></g><g class="toyplot-Datum" transform="translate(347.51846247830969,459.81836106732754)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">9</text></g><g class="toyplot-Datum" transform="translate(308.12351356081211,516.39861016382122)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">10</text></g><g class="toyplot-Datum" transform="translate(369.16545493310974,528.86219138304273)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">11</text></g><g class="toyplot-Datum" transform="translate(331.00451290448143,550.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">12</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t45775f23dfa242baa18b3da8ee325a6e";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tf1b31ff3cfa04753addd71da71ed8103";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tfb1dedb4e38947c59e3ce7a8e8048c80","vertex_data","graph vertex data",["x", "y"],[[-0.22126767335038133, 0.0029659671685047504, -0.250771081679212, 0.06600388241149634, 0.4322236084249407, 0.7239137497623711, 0.7420857321356447, 0.5613817507863635, 0.4913256236267057, 0.2876555223376603, 0.6032395939964988, 0.40594925242166796], [1.3755143398163583, 1.3661665282456386, 1.1643805811871888, 0.9961237556228442, 0.44543141801220687, 0.3246917493829421, 0.15121722285762035, -0.08605790444950144, -0.7432280218883004, -1.0357453465985238, -1.100181496894319, -1.2094630098887935]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tfb1dedb4e38947c59e3ce7a8e8048c80","edge_data","graph edge data",["source", "target"],[[0, 0, 0, 1, 1, 2, 4, 4, 4, 5, 5, 6, 8, 8, 8, 9, 9, 10, 3, 7], [1, 2, 3, 2, 3, 3, 5, 6, 7, 6, 7, 7, 9, 10, 11, 10, 11, 11, 4, 8]],"toyplot");
    })();</script></div></div>


Now, we have a single visualization that emphasizes the differences
between the two sets of community assignments, and we can clearly see
the behavior of the tested algorithm: the green edge connecting vertices
8 and 9 indicate that two ground truth communities were merged together
into one, while the red edges adjacent to vertex 1 show that it was
"split" from its neighbors into its own community.

Now that that's taken care of, we can create a publication-quality PDF
version of the plot for incorporation into a paper:

.. code:: python

    import toyplot.pdf
    toyplot.pdf.render(canvas, "communities.pdf")
