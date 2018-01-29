
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _neural-networks-case-study:

Generating Neural Network Diagrams
==================================

The following explores how Toyplot's graph visualization can be used to
generate high-quality diagrams of neural networks.

Network Data
------------

First, we will define the edges (weights) in our network, by explicitly
listing the source and target for each edge:

.. code:: ipython3

    import numpy
    import toyplot
    
    numpy.random.seed(1234)
    
    edges = numpy.array([
        ["x0", "a0"],
        ["x0", "a1"],
        ["x0", "a2"],
        ["x0", "a3"],
        ["x1", "a0"],
        ["x1", "a1"],
        ["x1", "a2"],
        ["x1", "a3"],
        ["x2", "a0"],
        ["x2", "a1"],
        ["x2", "a2"],
        ["x2", "a3"],
        ["a0", "y0"],
        ["a0", "y1"],
        ["a1", "y0"],
        ["a1", "y1"],
        ["a2", "y0"],
        ["a2", "y1"],
        ["a3", "y0"],
        ["a3", "y1"],
    ])

Network Layout
--------------

As a straw-man, we can quickly render a graph using just the edge data:

.. code:: ipython3

    canvas, axes, mark = toyplot.graph(edges)



.. raw:: html

    <div class="toyplot" id="t59d3f4b67a4d4f358fe6f8e1f8e510f8" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="tbebf3e73fd494c00b42d3b60fbbfd44c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t7140092d24b845ca88d42cb4e4f6ba30"><clipPath id="t2d33301d406f4f1bae0b002f062cba3f"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#t2d33301d406f4f1bae0b002f062cba3f)"><g class="toyplot-mark-Graph" id="t6c1280681a8d4eec92110298bba957c6"><g class="toyplot-Edges"><path d="M 543.203231006 182.649283155 L 253.645454976 366.997277505" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 543.092832515 182.452107182 L 357.9419112 272.779307392" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 544.000734438 183.366444892 L 446.283456824 380.126269264" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 542.89576551 181.722503361 L 217.032582276 205.790860541" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 57.015362814 305.988724225 L 250.0526584 367.464478115" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 57.0986525554 305.172209599 L 354.155426393 273.865846656" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 57.0722861969 305.76670011 L 443.431240298 381.532655728" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 56.8081014653 304.325737423 L 213.339581553 206.99426816" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 353.036238148 51.9050149937 L 252.567383871 366.166361641" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 353.667615099 51.9998751526 L 356.122064653 271.656355397" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 354.178125528 51.927709341 L 444.861001772 379.989820791" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 352.31656464 51.4948398783 L 216.366719183 204.443339999" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.28016103 369.572318044 L 410.852397943 548.499058591" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 251.140889807 369.896685636 L 178.955686238 531.078505986" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 356.541832695 275.616346939 L 411.776784011 548.039883611" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 355.012332152 275.304986666 L 179.270301627 531.255058871" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 445.00608182 383.879577265 L 412.561982434 548.037952867" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 443.652534378 382.901292797 L 179.879546949 531.920052322" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 216.032305607 207.673514712 L 411.179915169 548.264665165" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 214.813728649 207.92556395 L 178.362509201 530.916430915" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(251.9583535981335, 368.07137663471906)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(356.14441133167776, 273.65623054938459)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(445.39385887905928, 381.91753013196353)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(215.03801540209946, 205.93817987752979)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(544.89033238370678, 181.57518402476808)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(55.109667616293159, 305.38182570555279)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(353.64526842119619, 50.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(412.17420537430002, 550.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(178.13822244773303, 532.90381498715863)"><circle r="2.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(251.9583535981335,368.07137663471906)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a0</text></g><g class="toyplot-Datum" transform="translate(356.14441133167776,273.65623054938459)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a1</text></g><g class="toyplot-Datum" transform="translate(445.39385887905928,381.91753013196353)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a2</text></g><g class="toyplot-Datum" transform="translate(215.03801540209946,205.93817987752979)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a3</text></g><g class="toyplot-Datum" transform="translate(544.89033238370678,181.57518402476808)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x0</text></g><g class="toyplot-Datum" transform="translate(55.109667616293159,305.38182570555279)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x1</text></g><g class="toyplot-Datum" transform="translate(353.64526842119619,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x2</text></g><g class="toyplot-Datum" transform="translate(412.17420537430002,550.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y0</text></g><g class="toyplot-Datum" transform="translate(178.13822244773303,532.90381498715863)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y1</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t59d3f4b67a4d4f358fe6f8e1f8e510f8";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tbebf3e73fd494c00b42d3b60fbbfd44c";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t6c1280681a8d4eec92110298bba957c6","vertex_data","graph vertex data",["x", "y"],[[0.0052388321082405005, 0.14884502685957032, 0.27186315255462973, -0.04565079163416516, 0.40900539847510853, -0.26609008992419375, 0.14540030103616036, 0.22607441522686922, -0.09651209657806446], [-0.017372385279453013, 0.11276594753741871, -0.03645740931181837, 0.20610599499207713, 0.23968704415803566, 0.06903656478017411, 0.42104539394632373, -0.26813604681133746, -0.2445712999741184]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t6c1280681a8d4eec92110298bba957c6","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Clearly, this needs work - Toyplot's default force-directed layout
algorithm obscures the fact that our neural network is organized in
layers. What we want is to put all of the ``x`` nodes in the first
(input) layer, all of the ``a`` nodes in a second (hidden) layer, and
all of the ``y`` nodes in the last (output) layer. Since Toyplot doesn't
have a graph layout algorithm that can do that for us, we'll have to
compute the vertex coordinates ourselves:

.. code:: ipython3

    vertex_ids = numpy.unique(edges)
    
    layer_map = {"x": 0, "a": -1, "y": -2}
    offset_map = {"x": 0.5, "a": 0, "y": 1}
    vcoordinates = []
    for vertex_id in vertex_ids:
        layer = vertex_id[0]
        column = int(vertex_id[1:])
        x = column + offset_map[layer]
        y = layer_map[layer]
        vcoordinates.append((x, y))
    vcoordinates = numpy.array(vcoordinates)

Now, we can see what the graph looks like with our explicitly defined
coordinates:

.. code:: ipython3

    canvas, axes, mark = toyplot.graph(edges, vcoordinates=vcoordinates)



.. raw:: html

    <div class="toyplot" id="ta055e429e44543db9d5bc93a1de30a00" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t88b098f432e045c29006a6f9fe06982d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t83c03e31a32e483bbfde4ca643426b6b"><clipPath id="t00af3425ad0649c8a82fe935abbde004"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#t00af3425ad0649c8a82fe935abbde004)"><g class="toyplot-mark-Graph" id="tea8dda41aa0644efa40aa0cd4501d487"><g class="toyplot-Edges"><path d="M 132.438906142 135.122187715 L 50.894427191 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.227760524 135.122187715 L 215.772239476 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.997433922 134.442733726 L 381.669232745 298.890599608" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 135.190286715 134.076114686 L 548.143046618 299.257218647" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 298.335899411 134.442733726 L 51.6641005887 298.890599608" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 299.105572809 135.122187715 L 217.561093858 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 300.894427191 135.122187715 L 382.438906142 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 301.664100589 134.442733726 L 548.335899411 298.890599608" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 464.809713285 134.076114686 L 51.8569533818 299.257218647" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 465.002566078 134.442733726 L 218.330767255 298.890599608" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 465.772239476 135.122187715 L 384.227760524 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 467.561093858 135.122187715 L 549.105572809 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 51.4142135624 301.414213562 L 215.252453104 465.252453104" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 51.788854382 300.894427191 L 381.544478951 465.772239476" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 216.666666667 302.0 L 216.666666667 464.666666667" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.080880229 301.414213562 L 381.919119771 465.252453104" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 381.919119771 301.414213562 L 218.080880229 465.252453104" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 383.333333333 302.0 L 383.333333333 464.666666667" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 548.211145618 300.894427191 L 218.455521049 465.772239476" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 548.585786438 301.414213562 L 384.747546896 465.252453104" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(50.0, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(216.66666666666666, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(383.33333333333331, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(550.0, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(133.33333333333331, 133.33333333333331)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(300.0, 133.33333333333331)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(466.66666666666669, 133.33333333333331)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(216.66666666666666, 466.66666666666669)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(383.33333333333331, 466.66666666666669)"><circle r="2.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a0</text></g><g class="toyplot-Datum" transform="translate(216.66666666666666,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a1</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a2</text></g><g class="toyplot-Datum" transform="translate(550.0,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a3</text></g><g class="toyplot-Datum" transform="translate(133.33333333333331,133.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x0</text></g><g class="toyplot-Datum" transform="translate(300.0,133.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x1</text></g><g class="toyplot-Datum" transform="translate(466.66666666666669,133.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x2</text></g><g class="toyplot-Datum" transform="translate(216.66666666666666,466.66666666666669)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y0</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,466.66666666666669)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y1</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "ta055e429e44543db9d5bc93a1de30a00";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t88b098f432e045c29006a6f9fe06982d";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tea8dda41aa0644efa40aa0cd4501d487","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tea8dda41aa0644efa40aa0cd4501d487","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Vertex and Edge Styles
----------------------

With the graph layout looking better, we can begin to work on the
appearance of the vertices and edges:

.. code:: ipython3

    canvas, axes, mark = toyplot.graph(
        edges,
        ecolor="black",
        tmarker=">",
        vcolor="white",
        vcoordinates=vcoordinates,
        vmarker="o",
        vsize=50,
        vstyle={"stroke":"black"},
        width=500,
        height=500,
    )
    
    # So we can control the aspect ratio of the figure using the canvas width & height
    axes.aspect=None
    
    # Prevent large vertex markers from falling outside the canvas
    axes.padding=50



.. raw:: html

    <div class="toyplot" id="t1fc445c0874a4afba0f08f94a68aed17" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="td9652d417ed04231803e714636221bc4" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t6a5df64023ce4e72a894e2aed608acc8"><clipPath id="td0a855bcf9d14e4085aaf5b14dfba966"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#td0a855bcf9d14e4085aaf5b14dfba966)"><g class="toyplot-mark-Graph" id="t260331f35a234e19af70dca64b23b2a5"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a0</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a1</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a2</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a3</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x0</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x1</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x2</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y0</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y1</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t1fc445c0874a4afba0f08f94a68aed17";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "td9652d417ed04231803e714636221bc4";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t260331f35a234e19af70dca64b23b2a5","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t260331f35a234e19af70dca64b23b2a5","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


In many cases, we might not want to see the vertex labels:

.. code:: ipython3

    canvas, axes, mark = toyplot.graph(
        edges,
        ecolor="black",
        tmarker=">",
        vcolor="white",
        vcoordinates=vcoordinates,
        vlshow=False,
        vmarker="o",
        vsize=50,
        vstyle={"stroke":"black"},
        width=500,
        height=500,
    )
    axes.aspect=None
    axes.padding=50



.. raw:: html

    <div class="toyplot" id="t4dae6b312d424194a44193c46a8e8c7c" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="t1bbbc0f82ad445caba61ed4bc701923b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t19499ceff3ff4d85a18feec133838e81"><clipPath id="t45a5497afb784c74aa34dd27e71c2980"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t45a5497afb784c74aa34dd27e71c2980)"><g class="toyplot-mark-Graph" id="tc89a8b1d7dfa44ae9d134b6ee24a97f7"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t4dae6b312d424194a44193c46a8e8c7c";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t1bbbc0f82ad445caba61ed4bc701923b";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tc89a8b1d7dfa44ae9d134b6ee24a97f7","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tc89a8b1d7dfa44ae9d134b6ee24a97f7","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Or we might want to substitute our own, explicit vertex labels, to
illustrate the values of individual activation units during network
evaluation:

.. code:: ipython3

    vertex_values = numpy.random.uniform(size=len(vertex_ids))
    vertex_labels = ["%.2f" % value for value in vertex_values]
    
    canvas, axes, mark = toyplot.graph(
        edges,
        ecolor="black",
        tmarker=">",
        vcolor="white",
        vcoordinates=vcoordinates,
        vlabel=vertex_labels,
        vmarker="o",
        vsize=50,
        vstyle={"stroke":"black"},
        width=500,
        height=500,
    )
    axes.aspect=None
    axes.padding=50



.. raw:: html

    <div class="toyplot" id="ta21106e52a134f4faf26e30ae49b6323" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="t2290a634f8b44d57b4425f402908dc3d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t5f9ccb8203d8456fa3bfa6df44bd9cca"><clipPath id="t95cf8794e21a46db9cdb556410b819cf"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t95cf8794e21a46db9cdb556410b819cf)"><g class="toyplot-mark-Graph" id="tcefdcfdbdb9a4f92a791492437df4d27"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "ta21106e52a134f4faf26e30ae49b6323";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t2290a634f8b44d57b4425f402908dc3d";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tcefdcfdbdb9a4f92a791492437df4d27","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tcefdcfdbdb9a4f92a791492437df4d27","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Edge Weights
------------

We might also want to display the network edge weights. Edge *middle*
markers are a good choice to do this:

.. code:: ipython3

    edge_weights = numpy.random.uniform(size=len(edges))
    mstyle = {"fill": "white"}
    lstyle = {"font-size": "12px"}
    mmarkers = [toyplot.marker.create(shape="s", label="%.1f" % weight, size=30, mstyle=mstyle, lstyle=lstyle) for weight in edge_weights]
    
    canvas, axes, mark = toyplot.graph(
        edges,
        ecolor="black",
        mmarker=mmarkers,
        tmarker=">",
        vcolor="white",
        vcoordinates=vcoordinates,
        vlabel=vertex_labels,
        vmarker="o",
        vsize=50,
        vstyle={"stroke":"black"},
        width=500,
        height=500,
    )
    axes.aspect=None
    axes.padding=50



.. raw:: html

    <div class="toyplot" id="t88cd94ea4c344e098779aac1c9d0abdd" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="td2fe08745e0541938e60a492dc1da780" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t508b850f9f234a33bd5584a244d47f4c"><clipPath id="t8defe6b4c27642d7b4290e1c2a0fec0e"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t8defe6b4c27642d7b4290e1c2a0fec0e)"><g class="toyplot-mark-Graph" id="t729a0be347d141f3b41830abbc34c634"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(83.333333333333343, 150.0) rotate(108.43494882292202)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0) rotate(71.565051177077976)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0) rotate(44.999999999999993)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333331, 150.0) rotate(30.963756532073521)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0) rotate(135.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0) rotate(108.43494882292202)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0) rotate(71.56505117707799)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0) rotate(45.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666663, 150.0) rotate(149.03624346792648)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.0</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0) rotate(135.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0) rotate(108.434948822922)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(416.66666666666663, 150.0) rotate(71.56505117707799)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(116.66666666666666, 350.0) rotate(56.309932474020215)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0) rotate(36.86989764584402)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.1</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0) rotate(90.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0) rotate(56.309932474020208)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0) rotate(123.69006752597979)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 350.0) rotate(90.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 350.0) rotate(143.13010235415598)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(383.33333333333337, 350.0) rotate(123.69006752597979)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.3</text></g></g></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t88cd94ea4c344e098779aac1c9d0abdd";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "td2fe08745e0541938e60a492dc1da780";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t729a0be347d141f3b41830abbc34c634","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t729a0be347d141f3b41830abbc34c634","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Note that the middle markers are aligned with the edges, making the
weight values difficult to read. To fix this, we can set an explicit
orientation for the middle markers:

.. code:: ipython3

    mmarkers = [toyplot.marker.create(angle=0, shape="s", label="%.1f" % weight, size=30, mstyle=mstyle, lstyle=lstyle) for weight in edge_weights]
    
    canvas, axes, mark = toyplot.graph(
        edges,
        ecolor="black",
        mmarker=mmarkers,
        tmarker=">",
        vcolor="white",
        vcoordinates=vcoordinates,
        vlabel=vertex_labels,
        vmarker="o",
        vsize=50,
        vstyle={"stroke":"black"},
        width=500,
        height=500,
    )
    axes.aspect=None
    axes.padding=50



.. raw:: html

    <div class="toyplot" id="t89e9979500dc4d23a657e39042f736af" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="t37fa05b4843b42d2920ac2a29be97e20" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="td5f8d86ddcd9414c8151868482d31b22"><clipPath id="tc4a7b1b9f5964a6dae25bf1af005d960"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#tc4a7b1b9f5964a6dae25bf1af005d960)"><g class="toyplot-mark-Graph" id="t237a85ee5f4f4fb7ac60b8c661763ac1"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(83.333333333333343, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333331, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666663, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.0</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(416.66666666666663, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(116.66666666666666, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.1</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(383.33333333333337, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.3</text></g></g></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t89e9979500dc4d23a657e39042f736af";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t37fa05b4843b42d2920ac2a29be97e20";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t237a85ee5f4f4fb7ac60b8c661763ac1","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t237a85ee5f4f4fb7ac60b8c661763ac1","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Now however, many of the middle markers overlap, making it appear as if
there are fewer weights than edges. One way to address this is to
randomly reposition the markers so that they rarely overlap:

.. code:: ipython3

    mposition = numpy.random.uniform(0.1, 0.8, len(edges))
    
    canvas, axes, mark = toyplot.graph(
        edges,
        ecolor="black",
        mmarker=mmarkers,
        mposition=mposition,
        tmarker=">",
        vcolor="white",
        vcoordinates=vcoordinates,
        vlabel=vertex_labels,
        vmarker="o",
        vsize=50,
        vstyle={"stroke":"black"},
        width=500,
        height=500,
    )
    axes.aspect=None
    axes.padding=50



.. raw:: html

    <div class="toyplot" id="tc0734bb16c32452698c9f64ad96a08d3" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="t7bdc88c9a1934ffabc393ad98a05e4a5" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t7e280c59ea6f47d39b4fb31d0fd479bd"><clipPath id="t3313b5ae890740ed8ccac5b18e89b0e6"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t3313b5ae890740ed8ccac5b18e89b0e6)"><g class="toyplot-mark-Graph" id="t59253fa1d5b348f68794db0f01b76f6f"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(83.451874096679134, 149.64437770996261)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(160.59768938571924, 181.79306815715768)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.07834013244315, 134.41167346577646)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.24338417016236, 178.1460305020974)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(199.28855632256668, 100.71144367743332)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(211.93800660311027, 164.18598019066923)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(288.07339697853979, 164.2201909356194)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(309.3582020623752, 109.35820206237524)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(144.80505551532733, 193.11696669080359)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.0</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.23391737650093, 135.09941595683244)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(337.97164999510755, 186.08505001467745)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(398.45368559165581, 95.361056774967565)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(88.04962222609511, 307.07443333914267)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(100.18037090317375, 287.63527817738031)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.1</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 360.86249907614467)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(251.71463651120237, 352.57195476680351)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(252.81766801786313, 345.77349797320539)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 294.54902658295435)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(318.25261796327419, 348.81053652754434)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(401.20395811917496, 323.19406282123759)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.3</text></g></g></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tc0734bb16c32452698c9f64ad96a08d3";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t7bdc88c9a1934ffabc393ad98a05e4a5";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t59253fa1d5b348f68794db0f01b76f6f","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t59253fa1d5b348f68794db0f01b76f6f","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Note that the ``mposition`` argument is a value between zero and one
that positions each middle marker anywhere along its edge from beginning
to end, respectively.

Layer-Only Diagrams
-------------------

Once a network reaches a certain level of complexity, it is typical to
only diagram the layers in the network, instead of all the activation
units. Here, we define per-layer data for a simple layer-only diagram:

.. code:: ipython3

    layers = [
        "<b>conv1</b><br/>3&#215;3 convolutional",
        "<b>pool1</b><br/>max pooling",
        "<b>fc_1</b><br/>4096 dense",
        "<b>fc_2</b><br/>1000 dense softmax",
    ]
    
    vertex_ids = numpy.arange(len(layers))
    
    edges = numpy.column_stack((
        vertex_ids[:-1],
        vertex_ids[1:],
    ))
    
    vcoordinates = numpy.column_stack((
        numpy.zeros_like(layers, dtype="float"),
        numpy.arange(0, -len(layers), -1),
        ))

In this case, it's useful to use Toyplot's special rectangular markers
for the graph nodes:

.. code:: ipython3

    canvas, axes, mark = toyplot.graph(
        edges,
        ecolor="black",
        tmarker=">",
        vcoordinates=vcoordinates,
        vlabel=layers,
        vmarker=toyplot.marker.create("r3x1", lstyle={"font-size":"12px"}, size=50),
        vstyle={"stroke":"black", "fill":"white"},
        width=200,
        height=400,
    )
    axes.padding = 50



.. raw:: html

    <div class="toyplot" id="t4d724b2bf1524830aefbb71b50839ed2" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t072992b2c512407191313702f0a184a4" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 200.0 400.0" width="200.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t4c529e2905b2461c8e3b96aeb628e221"><clipPath id="tb047c7c4ca06461f80e87dda0c501944"><rect height="400.0" width="200.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#tb047c7c4ca06461f80e87dda0c501944)"><g class="toyplot-mark-Graph" id="t7fd9629a184f45f69d495a78d2b200a0"><g class="toyplot-Edges"><path d="M 100.0 75.0 L 100.0 125.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 100.0 175.0 L 100.0 225.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 100.0 275.0 L 100.0 325.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(100.0, 125.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(100.0, 225.00000000000003) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(100.0, 325.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(100.0, 50.0)"><rect height="50.0" width="150.0" x="-75.0" y="-25.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(100.0, 150.0)"><rect height="50.0" width="150.0" x="-75.0" y="-25.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(100.0, 250.00000000000003)"><rect height="50.0" width="150.0" x="-75.0" y="-25.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(100.0, 350.0)"><rect height="50.0" width="150.0" x="-75.0" y="-25.0"></rect></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(100.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="-4.134">conv1</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-46.86" y="10.266">3×3 convolutional</text></g><g class="toyplot-Datum" transform="translate(100.0,150.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.002" y="-4.134">pool1</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-32.346" y="10.266">max pooling</text></g><g class="toyplot-Datum" transform="translate(100.0,250.00000000000003)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-12.006" y="-4.134">fc_1</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-31.356" y="10.266">4096 dense</text></g><g class="toyplot-Datum" transform="translate(100.0,350.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-12.006" y="-4.134">fc_2</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-54.03" y="10.266">1000 dense softmax</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t4d724b2bf1524830aefbb71b50839ed2";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t072992b2c512407191313702f0a184a4";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t7fd9629a184f45f69d495a78d2b200a0","vertex_data","graph vertex data",["x", "y"],[[0.0, 0.0, 0.0, 0.0], [0.0, -1.0, -2.0, -3.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t7fd9629a184f45f69d495a78d2b200a0","edge_data","graph edge data",["source", "target"],[[0, 1, 2], [1, 2, 3]],"toyplot");
    })();</script></div></div>

