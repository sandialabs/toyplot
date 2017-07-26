
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

First, we will define the weights (edges) in our network, by explicitly
listing the source and target for each edge:

.. code:: python

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

As a straw-man, we can quickly render a graph using just the edge data:

.. code:: python

    canvas, axes, mark = toyplot.graph(edges)



.. raw:: html

    <div class="toyplot" id="tf2f5b57eeabc4e76872210fcd436fe70" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t3eb221b827234e3a96e6282f59a59ece" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t72c719aaacae4a288136d29127aac62e"><clipPath id="t151b2129a83e4ec7a098d4169f5ccdb0"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#t151b2129a83e4ec7a098d4169f5ccdb0)"><g class="toyplot-mark-Graph" id="tbd2bcf8f38864d07a58be6c6c1173643"><g class="toyplot-Edges"><path d="M 543.203231006 182.649283155 L 253.645454976 366.997277505" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 543.092832515 182.452107182 L 357.9419112 272.779307392" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 544.000734438 183.366444892 L 446.283456824 380.126269264" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 542.89576551 181.722503361 L 217.032582276 205.790860541" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 57.015362814 305.988724225 L 250.0526584 367.464478115" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 57.0986525554 305.172209599 L 354.155426393 273.865846656" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 57.0722861969 305.76670011 L 443.431240298 381.532655728" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 56.8081014653 304.325737423 L 213.339581553 206.99426816" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 353.036238148 51.9050149937 L 252.567383871 366.166361641" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 353.667615099 51.9998751526 L 356.122064653 271.656355397" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 354.178125528 51.927709341 L 444.861001772 379.989820791" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 352.31656464 51.4948398783 L 216.366719183 204.443339999" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.28016103 369.572318044 L 410.852397943 548.499058591" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 251.140889807 369.896685636 L 178.955686238 531.078505986" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 356.541832695 275.616346939 L 411.776784011 548.039883611" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 355.012332152 275.304986666 L 179.270301627 531.255058871" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 445.00608182 383.879577265 L 412.561982434 548.037952867" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 443.652534378 382.901292797 L 179.879546949 531.920052322" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 216.032305607 207.673514712 L 411.179915169 548.264665165" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 214.813728649 207.92556395 L 178.362509201 530.916430915" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(251.9583535981335, 368.07137663471906)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(356.14441133167776, 273.65623054938459)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(445.39385887905928, 381.91753013196353)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(215.03801540209946, 205.93817987752979)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(544.89033238370678, 181.57518402476808)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(55.109667616293159, 305.38182570555279)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(353.64526842119619, 50.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(412.17420537430002, 550.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(178.13822244773303, 532.90381498715863)"><circle r="2.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(251.9583535981335,368.07137663471906)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a0</text></g><g class="toyplot-Datum" transform="translate(356.14441133167776,273.65623054938459)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a1</text></g><g class="toyplot-Datum" transform="translate(445.39385887905928,381.91753013196353)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a2</text></g><g class="toyplot-Datum" transform="translate(215.03801540209946,205.93817987752979)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a3</text></g><g class="toyplot-Datum" transform="translate(544.89033238370678,181.57518402476808)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x0</text></g><g class="toyplot-Datum" transform="translate(55.109667616293159,305.38182570555279)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x1</text></g><g class="toyplot-Datum" transform="translate(353.64526842119619,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x2</text></g><g class="toyplot-Datum" transform="translate(412.17420537430002,550.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y0</text></g><g class="toyplot-Datum" transform="translate(178.13822244773303,532.90381498715863)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y1</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tf2f5b57eeabc4e76872210fcd436fe70";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t3eb221b827234e3a96e6282f59a59ece";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tbd2bcf8f38864d07a58be6c6c1173643","vertex_data","graph vertex data",["x", "y"],[[0.0052388321082405005, 0.14884502685957032, 0.27186315255462973, -0.04565079163416516, 0.40900539847510853, -0.26609008992419375, 0.14540030103616036, 0.22607441522686922, -0.09651209657806446], [-0.017372385279453013, 0.11276594753741871, -0.03645740931181837, 0.20610599499207713, 0.23968704415803566, 0.06903656478017411, 0.42104539394632373, -0.26813604681133746, -0.2445712999741184]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tbd2bcf8f38864d07a58be6c6c1173643","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Clearly, this needs work - Toyplot's default force-directed layout
algorithm obscures the fact that our neural network is organized in
layers. What we want is to put all of the ``x`` vertices in the first
(input) layer, all of the ``a`` vertices in a second (hidden) layer, and
all of the ``y`` vertices in the last (output) layer. Since Toyplot
doesn't have a graph layout algorithm that can do that for us, we'll
have to compute the vertex coordinates ourselves:

.. code:: python

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

.. code:: python

    canvas, axes, mark = toyplot.graph(edges, vcoordinates=vcoordinates)



.. raw:: html

    <div class="toyplot" id="tee101f32e02f4313a908eaca65d555c9" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t0a764bd6293f410dbbe7c7b959b77ad6" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t605748c99b434facafb08f41155a586f"><clipPath id="tea64441a0b294085b496d1e02f390642"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#tea64441a0b294085b496d1e02f390642)"><g class="toyplot-mark-Graph" id="t53bde484578c436982eb122820e6e574"><g class="toyplot-Edges"><path d="M 132.438906142 135.122187715 L 50.894427191 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.227760524 135.122187715 L 215.772239476 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.997433922 134.442733726 L 381.669232745 298.890599608" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 135.190286715 134.076114686 L 548.143046618 299.257218647" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 298.335899411 134.442733726 L 51.6641005887 298.890599608" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 299.105572809 135.122187715 L 217.561093858 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 300.894427191 135.122187715 L 382.438906142 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 301.664100589 134.442733726 L 548.335899411 298.890599608" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 464.809713285 134.076114686 L 51.8569533818 299.257218647" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 465.002566078 134.442733726 L 218.330767255 298.890599608" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 465.772239476 135.122187715 L 384.227760524 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 467.561093858 135.122187715 L 549.105572809 298.211145618" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 51.4142135624 301.414213562 L 215.252453104 465.252453104" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 51.788854382 300.894427191 L 381.544478951 465.772239476" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 216.666666667 302.0 L 216.666666667 464.666666667" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.080880229 301.414213562 L 381.919119771 465.252453104" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 381.919119771 301.414213562 L 218.080880229 465.252453104" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 383.333333333 302.0 L 383.333333333 464.666666667" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 548.211145618 300.894427191 L 218.455521049 465.772239476" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 548.585786438 301.414213562 L 384.747546896 465.252453104" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(50.0, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(216.66666666666666, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(383.33333333333331, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(550.0, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(133.33333333333331, 133.33333333333331)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(300.0, 133.33333333333331)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(466.66666666666669, 133.33333333333331)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(216.66666666666666, 466.66666666666669)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(383.33333333333331, 466.66666666666669)"><circle r="2.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a0</text></g><g class="toyplot-Datum" transform="translate(216.66666666666666,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a1</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a2</text></g><g class="toyplot-Datum" transform="translate(550.0,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a3</text></g><g class="toyplot-Datum" transform="translate(133.33333333333331,133.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x0</text></g><g class="toyplot-Datum" transform="translate(300.0,133.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x1</text></g><g class="toyplot-Datum" transform="translate(466.66666666666669,133.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x2</text></g><g class="toyplot-Datum" transform="translate(216.66666666666666,466.66666666666669)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y0</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,466.66666666666669)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y1</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tee101f32e02f4313a908eaca65d555c9";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t0a764bd6293f410dbbe7c7b959b77ad6";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t53bde484578c436982eb122820e6e574","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t53bde484578c436982eb122820e6e574","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Now that the graph layout is looking better, we can begin to work on the
appearance of the vertices and edges:

.. code:: python

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

    <div class="toyplot" id="tc7aa3fd73ce84590b4fd6f91e7c4f653" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="t3d06e186e4784251a3efe5fa96e6ba8a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tad5d6c8f5870409c939370c35322c847"><clipPath id="t73b522364a2f43f5a6ecea84fb862989"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t73b522364a2f43f5a6ecea84fb862989)"><g class="toyplot-mark-Graph" id="td3171f5d8bf14a189af41f2ac3b9f92e"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a0</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a1</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a2</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">a3</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x0</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x1</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">x2</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y0</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336" y="3.066">y1</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tc7aa3fd73ce84590b4fd6f91e7c4f653";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t3d06e186e4784251a3efe5fa96e6ba8a";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"td3171f5d8bf14a189af41f2ac3b9f92e","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"td3171f5d8bf14a189af41f2ac3b9f92e","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


In many cases, we might not want to see the vertex labels:

.. code:: python

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

    <div class="toyplot" id="td3189b202b214dea90565abb4e454c72" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="t403d17d1ed784649b44bc0d6ad132177" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="ta03e6411c09e4209854ef26dbcde0997"><clipPath id="tc9348f9e080840568a192dc06123c17e"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#tc9348f9e080840568a192dc06123c17e)"><g class="toyplot-mark-Graph" id="t8c06d7a562d3425f96aa501b35785012"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "td3189b202b214dea90565abb4e454c72";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t403d17d1ed784649b44bc0d6ad132177";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t8c06d7a562d3425f96aa501b35785012","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t8c06d7a562d3425f96aa501b35785012","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Or we might want to substitute our own, explicit vertex labels, to
illustrate how the network is evaluated:

.. code:: python

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

    <div class="toyplot" id="tc6dc770571a246c19a4dc58f391d411a" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="t5172f9ed6a3a420ca2c96450527b2a8c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tad304c82f1564cdd84cf364d5efaee1a"><clipPath id="t0187ced8af714036bd59578e5310fca0"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t0187ced8af714036bd59578e5310fca0)"><g class="toyplot-mark-Graph" id="t37479da17242455a83b44d5f933a909f"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tc6dc770571a246c19a4dc58f391d411a";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t5172f9ed6a3a420ca2c96450527b2a8c";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t37479da17242455a83b44d5f933a909f","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t37479da17242455a83b44d5f933a909f","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


We might also want to display the network edge weights. Edge ``middle``
markers are a good choice to do this:

.. code:: python

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

    <div class="toyplot" id="t802c3397395a4301ae8a64ed7eb6e2cf" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="t140bf04186a54194911da41231481689" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t4f98f462e61f417b8aa1441ae83b08dd"><clipPath id="taaba3d0a3e6d4deb802c9b929997b87b"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#taaba3d0a3e6d4deb802c9b929997b87b)"><g class="toyplot-mark-Graph" id="te4a88eee50264f3098f541d8d744b040"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(83.333333333333343, 150.0) rotate(108.43494882292202)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0) rotate(71.565051177077976)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0) rotate(44.999999999999993)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333331, 150.0) rotate(30.963756532073521)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0) rotate(135.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0) rotate(108.43494882292202)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0) rotate(71.56505117707799)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0) rotate(45.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666663, 150.0) rotate(149.03624346792648)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.0</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0) rotate(135.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0) rotate(108.434948822922)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(416.66666666666663, 150.0) rotate(71.56505117707799)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(116.66666666666666, 350.0) rotate(56.309932474020215)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0) rotate(36.86989764584402)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.1</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0) rotate(90.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0) rotate(56.309932474020208)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0) rotate(123.69006752597979)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 350.0) rotate(90.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 350.0) rotate(143.13010235415598)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(383.33333333333337, 350.0) rotate(123.69006752597979)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.3</text></g></g></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t802c3397395a4301ae8a64ed7eb6e2cf";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t140bf04186a54194911da41231481689";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"te4a88eee50264f3098f541d8d744b040","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"te4a88eee50264f3098f541d8d744b040","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Note that the middle markers are aligned with the edges, making the
weight values difficult to read. To fix this, we can set an explicit
orientation for the middle markers:

.. code:: python

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

    <div class="toyplot" id="t12071c41c6c54af493ffd6600b98b2ed" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="td1077f385c84408390beb1885e30da3e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tb625a43cf9f0413285b895ede48d0615"><clipPath id="t9ee8cab35d8f472fb9e87270844c472d"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t9ee8cab35d8f472fb9e87270844c472d)"><g class="toyplot-mark-Graph" id="tcae5df4a71f94617a7b6992df20ebe36"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(83.333333333333343, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333331, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666663, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.0</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(416.66666666666663, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(116.66666666666666, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.1</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(383.33333333333337, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.3</text></g></g></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t12071c41c6c54af493ffd6600b98b2ed";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "td1077f385c84408390beb1885e30da3e";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tcae5df4a71f94617a7b6992df20ebe36","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tcae5df4a71f94617a7b6992df20ebe36","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Now however, many of the middle markers overlap, making it appear as if
there are fewer weights than edges. One way to address this is to
randomly reposition the markers so that they rarely overlap:

.. code:: python

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

    <div class="toyplot" id="t85a6b0dccec8433dad1031754a709cab" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="td3a4b8801b9a4d5a9fba605744d4823c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tfc244dd7a877492990fb325fb8294eaa"><clipPath id="t6125f6d6434e4629a48de48d80eca6b0"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t6125f6d6434e4629a48de48d80eca6b0)"><g class="toyplot-mark-Graph" id="t766d081c71b441aa803348730d8009a4"><g class="toyplot-Edges"><path d="M 108.760972516 73.7170824513 L 57.9056941504 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.572360817 73.7170824513 L 175.427639183 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.344336196 67.6776695297 L 298.988997137 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.103989809 62.8623938857 L 428.562676857 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.32233047 67.6776695297 L 67.6776695297 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430585 73.7170824513 L 191.239027484 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415 73.7170824513 L 308.760972516 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766953 67.6776695297 L 432.32233047 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.896010191 62.8623938857 L 71.4373231428 237.137606114" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.655663804 67.6776695297 L 201.011002863 232.32233047" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.427639183 73.7170824513 L 324.572360817 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.239027484 73.7170824513 L 442.09430585 226.282917549" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.8675049056 270.801257358 L 169.465828428 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.333333333 275.0 L 183.333333333 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.200838239 270.801257358 L 302.799161761 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761 270.801257358 L 197.200838239 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.666666667 275.0 L 316.666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.333333333 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.132495094 270.801257358 L 330.534171572 429.198742642" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(83.451874096679134, 149.64437770996261)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(160.59768938571924, 181.79306815715768)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.07834013244315, 134.41167346577646)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.24338417016236, 178.1460305020974)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(199.28855632256668, 100.71144367743332)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(211.93800660311027, 164.18598019066923)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(288.07339697853979, 164.2201909356194)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(309.3582020623752, 109.35820206237524)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(144.80505551532733, 193.11696669080359)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.0</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.23391737650093, 135.09941595683244)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(337.97164999510755, 186.08505001467745)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(398.45368559165581, 95.361056774967565)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(88.04962222609511, 307.07443333914267)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(100.18037090317375, 287.63527817738031)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.1</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 360.86249907614467)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(251.71463651120237, 352.57195476680351)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(252.81766801786313, 345.77349797320539)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 294.54902658295435)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(318.25261796327419, 348.81053652754434)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(401.20395811917496, 323.19406282123759)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="3.066">0.3</text></g></g></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.905694150420949, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.565051177077976) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.98899713700303, 232.32233047033631) rotate(44.999999999999993) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.56267685718637, 237.13760611431184) rotate(30.963756532073521) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.677669529663689, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.76097251624572, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.32233047033628, 232.32233047033631) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.437323142813597, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.32233047033631) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.19874264155391) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.66666666666669, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.79916176103598, 429.19874264155391) rotate(56.309932474020208) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.66666666666669, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.19874264155391) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.33333333333331, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.66666666666669, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.33333333333331,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t85a6b0dccec8433dad1031754a709cab";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "td3a4b8801b9a4d5a9fba605744d4823c";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t766d081c71b441aa803348730d8009a4","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t766d081c71b441aa803348730d8009a4","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Note that the ``mposition`` argument is a value between zero and one
that positions each middle marker anywhere along its edge from beginning
to end.

.. code:: python

    edges = numpy.array([
        ["a", "b"],
        ["b", "c"],
    ])
    
    vcoordinates = numpy.array([
        [0, 0],
        [0, -1],
        [0, -2],
    ])
    
    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.cartesian(show=False, padding=50)
    axes.aspect = "fit-range"
    mark = axes.graph(
        edges,
        ecolor="black",
        tmarker=">",
        vcoordinates=vcoordinates,
        vlshow=False,
        vmarker=toyplot.marker.create("r2x1", label="Convolutional<br/>5&#215;5", angle=0, lstyle={"font-size":"12px"}, size=50),
        vstyle={"stroke":"black", "fill":"white"},
    )
    
    #axes.scatterplot(vcoordinates[:,0], vcoordinates[:,1], color="red")



.. raw:: html

    <div class="toyplot" id="tecc67a987245497889fb2cdf8de9159b" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t7dc94f6aa7d14ad9a995921edf48cc7d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tc8b12d65e6524f648a3ab068f45b6c92"><clipPath id="t642cdeab9d5e401dbc45e54dd6f11940"><rect height="300.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t642cdeab9d5e401dbc45e54dd6f11940)"><g class="toyplot-mark-Graph" id="t04d5cdd8b22649f396d6de8f407db56d"><g class="toyplot-Edges"><path d="M 250.0 75.0 L 250.0 125.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 250.0 175.0 L 250.0 225.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.0, 125.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.0, 225.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><rect height="50.0" width="100.0" x="-50.0" y="-25.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-36.348" y="-4.134">Convolutional</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.176" y="10.266">5×5</text></g></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 150.0)"><rect height="50.0" width="100.0" x="-50.0" y="-25.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-36.348" y="-4.134">Convolutional</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.176" y="10.266">5×5</text></g></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 250.0)"><rect height="50.0" width="100.0" x="-50.0" y="-25.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-36.348" y="-4.134">Convolutional</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.176" y="10.266">5×5</text></g></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tecc67a987245497889fb2cdf8de9159b";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t7dc94f6aa7d14ad9a995921edf48cc7d";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t04d5cdd8b22649f396d6de8f407db56d","vertex_data","graph vertex data",["x", "y"],[[0.0, 0.0, 0.0], [0.0, -1.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t04d5cdd8b22649f396d6de8f407db56d","edge_data","graph edge data",["source", "target"],[[0, 1], [1, 2]],"toyplot");
    })();</script></div></div>

