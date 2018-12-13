
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

Network Layout
--------------

As a straw-man, we can quickly render a graph using just the edge data:

.. code:: python

    canvas, axes, mark = toyplot.graph(edges)



.. raw:: html

    <div class="toyplot" id="t77df7f98b9154a41a1033f4431202827" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t56e90251307c44b2b0632ca3b96505cf" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t0699d0edaf7845ebb8de4270482d41f3"><clipPath id="t502674236c1249da8373152b38b02a26"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#t502674236c1249da8373152b38b02a26)"><g class="toyplot-mark-Graph" id="tf1b8f726deaa41749d4fbf20523294c2"><g class="toyplot-Edges"><path d="M 543.2032310058288 182.64928315462635 L 253.64545497601145 366.9972775048608" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 543.0928325154524 182.45210718196358 L 357.94191119993206 272.7793073921891" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 544.0007344384172 183.36644489235175 L 446.28345682434883 380.12626926437986" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 542.8957655101465 181.72250336123136 L 217.03258227565973 205.7908605410665" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 57.01536281401664 305.98872422538426 L 250.05265840041002 367.4644781148876" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 57.09865255535797 305.1722095988879 L 354.1554263926129 273.8658466560495" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 57.072286196908905 305.76670010977034 L 443.4312402984435 381.532655727746" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 56.80810146530517 304.3257374230071 L 213.33958155308744 206.99426816007545" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 353.03623814801085 51.90501499373201 L 252.56738387131884 366.166361640987" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 353.66761509938704 51.99987515259674 L 356.1220646534869 271.65635539678783" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 354.178125528151 51.927709341049045 L 444.8610017721045 379.9898207909145" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 352.31656463999246 51.49483987831973 L 216.3667191833032 204.44333999921005" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.2801610295837 369.5723180440229 L 410.8523979428498 548.4990585906961" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 251.14088980746604 369.8966856362165 L 178.9556862384005 531.0785059856612" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 356.54183269498856 275.616346938782 L 411.7767840109892 548.0398836106026" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 355.01233215217644 275.3049866657765 L 179.27030162723435 531.2550588707668" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 445.00608181956244 383.8795772649672 L 412.56198243379686 548.0379528669963" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 443.65253437780694 382.9012927971112 L 179.87954694898534 531.920052322011" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 216.0323056070131 207.67351471219797 L 411.1799151693864 548.2646651653318" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 214.8137286486097 207.9255639501763 L 178.3625092012228 530.9164309145121" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(251.9583535981335, 368.07137663471906)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(356.14441133167776, 273.6562305493846)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(445.3938588790593, 381.91753013196353)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(215.03801540209946, 205.9381798775298)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(544.8903323837068, 181.57518402476808)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(55.10966761629316, 305.3818257055528)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(353.6452684211962, 50.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(412.1742053743, 550.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(178.13822244773303, 532.9038149871586)"><circle r="2.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(251.9583535981335,368.07137663471906)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a0</text></g><g class="toyplot-Datum" transform="translate(356.14441133167776,273.6562305493846)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a1</text></g><g class="toyplot-Datum" transform="translate(445.3938588790593,381.91753013196353)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a2</text></g><g class="toyplot-Datum" transform="translate(215.03801540209946,205.9381798775298)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a3</text></g><g class="toyplot-Datum" transform="translate(544.8903323837068,181.57518402476808)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">x0</text></g><g class="toyplot-Datum" transform="translate(55.10966761629316,305.3818257055528)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">x1</text></g><g class="toyplot-Datum" transform="translate(353.6452684211962,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">x2</text></g><g class="toyplot-Datum" transform="translate(412.1742053743,550.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">y0</text></g><g class="toyplot-Datum" transform="translate(178.13822244773303,532.9038149871586)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">y1</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t77df7f98b9154a41a1033f4431202827";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t56e90251307c44b2b0632ca3b96505cf";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tf1b8f726deaa41749d4fbf20523294c2","vertex_data","graph vertex data",["x", "y"],[[0.0052388321082405005, 0.14884502685957032, 0.27186315255462973, -0.04565079163416516, 0.40900539847510853, -0.26609008992419375, 0.14540030103616036, 0.22607441522686922, -0.09651209657806446], [-0.017372385279453013, 0.11276594753741871, -0.03645740931181837, 0.20610599499207713, 0.23968704415803566, 0.06903656478017411, 0.42104539394632373, -0.26813604681133746, -0.2445712999741184]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tf1b8f726deaa41749d4fbf20523294c2","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Clearly, this needs work - Toyplot's default force-directed layout
algorithm obscures the fact that our neural network is organized in
layers. What we want is to put all of the ``x`` nodes in the first
(input) layer, all of the ``a`` nodes in a second (hidden) layer, and
all of the ``y`` nodes in the last (output) layer. Since Toyplot doesn't
have a graph layout algorithm that can do that for us, we'll have to
compute the vertex coordinates ourselves:

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

    <div class="toyplot" id="tbe0f39a61ba84ebe995747ac43460797" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t090a5e44df2f4b65b7aa703f9db63277" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t3fb52849fc714cfc816ea31c21a78d22"><clipPath id="tbd265d8441514decbf2027d2330360c3"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#tbd265d8441514decbf2027d2330360c3)"><g class="toyplot-mark-Graph" id="t95b565bdb3384cc1989b3d315c5c6639"><g class="toyplot-Edges"><path d="M 132.4389061423334 135.12218771533315 L 50.89442719099991 298.21114561800016" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.22776052433323 135.12218771533315 L 215.77223947566674 298.21114561800016" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.997433922009 134.44273372578377 L 381.6692327446576 298.8905996075495" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 135.19028671510384 134.07611468604154 L 548.1430466182295 299.2572186472918" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 298.3358994113243 134.44273372578377 L 51.66410058867569 298.8905996075495" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 299.1055728090001 135.12218771533315 L 217.56109385766658 298.21114561800016" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 300.8944271909999 135.12218771533315 L 382.4389061423334 298.21114561800016" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 301.6641005886757 134.44273372578377 L 548.3358994113244 298.8905996075495" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 464.8097132848962 134.07611468604154 L 51.856953381770516 299.2572186472918" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 465.002566077991 134.44273372578377 L 218.33076725534235 298.8905996075495" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 465.77223947566677 135.12218771533315 L 384.22776052433323 298.21114561800016" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 467.5610938576666 135.12218771533315 L 549.1055728090001 298.21114561800016" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 51.41421356237309 301.4142135623731 L 215.25245310429355 465.2524531042936" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 51.78885438199983 300.8944271909999 L 381.5444789513335 465.77223947566677" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 216.66666666666666 302.0 L 216.66666666666666 464.6666666666667" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 218.08088022903976 301.4142135623731 L 381.9191197709602 465.2524531042936" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 381.9191197709602 301.4142135623731 L 218.08088022903976 465.2524531042936" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 383.3333333333333 302.0 L 383.3333333333333 464.6666666666667" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 548.2111456180002 300.8944271909999 L 218.4555210486665 465.77223947566677" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 548.5857864376269 301.4142135623731 L 384.7475468957064 465.2524531042936" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(50.0, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(216.66666666666666, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(383.3333333333333, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(550.0, 300.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(133.33333333333331, 133.33333333333331)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(300.0, 133.33333333333331)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(466.6666666666667, 133.33333333333331)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(216.66666666666666, 466.6666666666667)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(383.3333333333333, 466.6666666666667)"><circle r="2.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a0</text></g><g class="toyplot-Datum" transform="translate(216.66666666666666,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a1</text></g><g class="toyplot-Datum" transform="translate(383.3333333333333,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a2</text></g><g class="toyplot-Datum" transform="translate(550.0,300.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a3</text></g><g class="toyplot-Datum" transform="translate(133.33333333333331,133.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">x0</text></g><g class="toyplot-Datum" transform="translate(300.0,133.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">x1</text></g><g class="toyplot-Datum" transform="translate(466.6666666666667,133.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">x2</text></g><g class="toyplot-Datum" transform="translate(216.66666666666666,466.6666666666667)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">y0</text></g><g class="toyplot-Datum" transform="translate(383.3333333333333,466.6666666666667)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">y1</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tbe0f39a61ba84ebe995747ac43460797";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t090a5e44df2f4b65b7aa703f9db63277";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t95b565bdb3384cc1989b3d315c5c6639","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t95b565bdb3384cc1989b3d315c5c6639","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Vertex and Edge Styles
----------------------

With the graph layout looking better, we can begin to work on the
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

    <div class="toyplot" id="t0696cbcc106f4bd3875f772974c27308" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="td4463e580fec4f05b474499b09b7d0f1" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t1d97da04af3a478bbc019ce9e999dfad"><clipPath id="t37118ad6910a44df94f98a241d027ad6"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t37118ad6910a44df94f98a241d027ad6)"><g class="toyplot-mark-Graph" id="t2812f9bd54b34b23993fb973d9ede9aa"><g class="toyplot-Edges"><path d="M 108.76097251624573 73.71708245126284 L 57.90569415042095 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.57236081708761 73.71708245126284 L 175.4276391829124 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.34433619633035 67.67766952966369 L 298.988997137003 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.10398980948028 62.862393885688164 L 428.5626768571864 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.3223304703363 67.67766952966369 L 67.67766952966369 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430584957906 73.71708245126284 L 191.23902748375428 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415042097 73.71708245126284 L 308.7609725162457 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766952966366 67.67766952966369 L 432.3223304703363 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.8960101905197 62.862393885688164 L 71.4373231428136 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.65566380366965 67.67766952966369 L 201.01100286299703 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.42763918291234 73.71708245126285 L 324.57236081708766 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.2390274837543 73.71708245126284 L 442.09430584957903 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.867504905630724 270.8012573584461 L 169.4658284277026 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.6666666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.33333333333334 275.0 L 183.33333333333334 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.20083823896408 270.8012573584461 L 302.799161761036 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761036 270.8012573584461 L 197.20083823896408 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.6666666666667 275.0 L 316.6666666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.33333333333334 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.1324950943693 270.8012573584461 L 330.5341715722974 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.90569415042095, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.56505117707798) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.988997137003, 232.3223304703363) rotate(44.99999999999999) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.5626768571864, 237.13760611431184) rotate(30.96375653207352) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.67766952966369, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.7609725162457, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.3223304703363, 232.3223304703363) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.4373231428136, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.1987426415539) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.6666666666667, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.799161761036, 429.1987426415539) rotate(56.30993247402021) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.3333333333333, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a0</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a1</text></g><g class="toyplot-Datum" transform="translate(316.6666666666667,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a2</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">a3</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">x0</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">x1</text></g><g class="toyplot-Datum" transform="translate(383.3333333333333,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">x2</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">y0</text></g><g class="toyplot-Datum" transform="translate(316.6666666666667,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.336000000000001" y="3.066">y1</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t0696cbcc106f4bd3875f772974c27308";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "td4463e580fec4f05b474499b09b7d0f1";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t2812f9bd54b34b23993fb973d9ede9aa","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t2812f9bd54b34b23993fb973d9ede9aa","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
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

    <div class="toyplot" id="t063d01d16952413093cfc85d7c18c147" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="t529a193df77f4373adb4f4d8d2dd2722" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="ta4b1795cefed4d31b82eecfe9fa75e5e"><clipPath id="t53f321ec21234f27b518fc5aa0f38b70"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t53f321ec21234f27b518fc5aa0f38b70)"><g class="toyplot-mark-Graph" id="tea92f00a8e4c4eb5acd1a11d31b4962d"><g class="toyplot-Edges"><path d="M 108.76097251624573 73.71708245126284 L 57.90569415042095 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.57236081708761 73.71708245126284 L 175.4276391829124 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.34433619633035 67.67766952966369 L 298.988997137003 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.10398980948028 62.862393885688164 L 428.5626768571864 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.3223304703363 67.67766952966369 L 67.67766952966369 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430584957906 73.71708245126284 L 191.23902748375428 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415042097 73.71708245126284 L 308.7609725162457 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766952966366 67.67766952966369 L 432.3223304703363 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.8960101905197 62.862393885688164 L 71.4373231428136 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.65566380366965 67.67766952966369 L 201.01100286299703 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.42763918291234 73.71708245126285 L 324.57236081708766 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.2390274837543 73.71708245126284 L 442.09430584957903 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.867504905630724 270.8012573584461 L 169.4658284277026 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.6666666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.33333333333334 275.0 L 183.33333333333334 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.20083823896408 270.8012573584461 L 302.799161761036 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761036 270.8012573584461 L 197.20083823896408 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.6666666666667 275.0 L 316.6666666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.33333333333334 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.1324950943693 270.8012573584461 L 330.5341715722974 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.90569415042095, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.56505117707798) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.988997137003, 232.3223304703363) rotate(44.99999999999999) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.5626768571864, 237.13760611431184) rotate(30.96375653207352) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.67766952966369, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.7609725162457, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.3223304703363, 232.3223304703363) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.4373231428136, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.1987426415539) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.6666666666667, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.799161761036, 429.1987426415539) rotate(56.30993247402021) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.3333333333333, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 450.0)"><circle r="25.0"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t063d01d16952413093cfc85d7c18c147";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t529a193df77f4373adb4f4d8d2dd2722";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tea92f00a8e4c4eb5acd1a11d31b4962d","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tea92f00a8e4c4eb5acd1a11d31b4962d","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Or we might want to substitute our own, explicit vertex labels, to
illustrate the values of individual activation units during network
evaluation:

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

    <div class="toyplot" id="taca2ae6e5f264fdca9ac08b1debbb228" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="tea959544e1c843ceb89d6a1ed1288f14" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t0c89fd56c7c64577959ff17402efdfda"><clipPath id="t46917112deb4453aaf7e29bd65e59f7a"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t46917112deb4453aaf7e29bd65e59f7a)"><g class="toyplot-mark-Graph" id="t82e7ec8980ac4e18849ec08ae7d0dca1"><g class="toyplot-Edges"><path d="M 108.76097251624573 73.71708245126284 L 57.90569415042095 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.57236081708761 73.71708245126284 L 175.4276391829124 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.34433619633035 67.67766952966369 L 298.988997137003 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.10398980948028 62.862393885688164 L 428.5626768571864 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.3223304703363 67.67766952966369 L 67.67766952966369 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430584957906 73.71708245126284 L 191.23902748375428 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415042097 73.71708245126284 L 308.7609725162457 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766952966366 67.67766952966369 L 432.3223304703363 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.8960101905197 62.862393885688164 L 71.4373231428136 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.65566380366965 67.67766952966369 L 201.01100286299703 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.42763918291234 73.71708245126285 L 324.57236081708766 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.2390274837543 73.71708245126284 L 442.09430584957903 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.867504905630724 270.8012573584461 L 169.4658284277026 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.6666666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.33333333333334 275.0 L 183.33333333333334 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.20083823896408 270.8012573584461 L 302.799161761036 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761036 270.8012573584461 L 197.20083823896408 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.6666666666667 275.0 L 316.6666666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.33333333333334 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.1324950943693 270.8012573584461 L 330.5341715722974 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.90569415042095, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.56505117707798) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.988997137003, 232.3223304703363) rotate(44.99999999999999) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.5626768571864, 237.13760611431184) rotate(30.96375653207352) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.67766952966369, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.7609725162457, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.3223304703363, 232.3223304703363) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.4373231428136, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.1987426415539) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.6666666666667, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.799161761036, 429.1987426415539) rotate(56.30993247402021) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.3333333333333, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.6666666666667,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.3333333333333,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.6666666666667,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "taca2ae6e5f264fdca9ac08b1debbb228";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tea959544e1c843ceb89d6a1ed1288f14";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t82e7ec8980ac4e18849ec08ae7d0dca1","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t82e7ec8980ac4e18849ec08ae7d0dca1","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Edge Weights
------------

We might also want to display the network edge weights. Edge *middle*
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

    <div class="toyplot" id="t9bc7c8c5b97d4fd2a4e5ca2acf88c5c6" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="t3eb53b68739d4f37b36bbd560e2f850e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t0ab80ffe18d245929c006ec97d9b89cc"><clipPath id="taff666ba0b0740188df5364bc5e1de96"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#taff666ba0b0740188df5364bc5e1de96)"><g class="toyplot-mark-Graph" id="t6d3cff72b3cc4bff874fd44120411990"><g class="toyplot-Edges"><path d="M 108.76097251624573 73.71708245126284 L 57.90569415042095 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.57236081708761 73.71708245126284 L 175.4276391829124 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.34433619633035 67.67766952966369 L 298.988997137003 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.10398980948028 62.862393885688164 L 428.5626768571864 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.3223304703363 67.67766952966369 L 67.67766952966369 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430584957906 73.71708245126284 L 191.23902748375428 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415042097 73.71708245126284 L 308.7609725162457 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766952966366 67.67766952966369 L 432.3223304703363 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.8960101905197 62.862393885688164 L 71.4373231428136 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.65566380366965 67.67766952966369 L 201.01100286299703 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.42763918291234 73.71708245126285 L 324.57236081708766 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.2390274837543 73.71708245126284 L 442.09430584957903 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.867504905630724 270.8012573584461 L 169.4658284277026 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.6666666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.33333333333334 275.0 L 183.33333333333334 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.20083823896408 270.8012573584461 L 302.799161761036 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761036 270.8012573584461 L 197.20083823896408 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.6666666666667 275.0 L 316.6666666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.33333333333334 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.1324950943693 270.8012573584461 L 330.5341715722974 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(83.33333333333334, 150.0) rotate(108.43494882292202)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0) rotate(71.56505117707798)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0) rotate(44.99999999999999)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.3333333333333, 150.0) rotate(30.96375653207352)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0) rotate(135.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0) rotate(108.43494882292202)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0) rotate(71.56505117707799)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0) rotate(45.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666663, 150.0) rotate(149.03624346792648)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.0</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0) rotate(135.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0) rotate(108.434948822922)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(416.66666666666663, 150.0) rotate(71.56505117707799)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(116.66666666666666, 350.0) rotate(56.309932474020215)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0) rotate(36.86989764584402)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.1</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0) rotate(90.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0) rotate(56.30993247402021)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0) rotate(123.69006752597979)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 350.0) rotate(90.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 350.0) rotate(143.13010235415598)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(383.33333333333337, 350.0) rotate(123.69006752597979)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.3</text></g></g></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.90569415042095, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.56505117707798) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.988997137003, 232.3223304703363) rotate(44.99999999999999) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.5626768571864, 237.13760611431184) rotate(30.96375653207352) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.67766952966369, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.7609725162457, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.3223304703363, 232.3223304703363) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.4373231428136, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.1987426415539) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.6666666666667, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.799161761036, 429.1987426415539) rotate(56.30993247402021) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.3333333333333, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.6666666666667,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.3333333333333,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.6666666666667,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t9bc7c8c5b97d4fd2a4e5ca2acf88c5c6";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t3eb53b68739d4f37b36bbd560e2f850e";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t6d3cff72b3cc4bff874fd44120411990","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t6d3cff72b3cc4bff874fd44120411990","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
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

    <div class="toyplot" id="tf0903c1dc88b48159ee97dd214dea743" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="tafac6c9e7e01436c8f59a9fa08d55fe6" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tb3c817bcc44344bf9756997ea0724a20"><clipPath id="t0890a3d635c6401b86bf73c663968353"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t0890a3d635c6401b86bf73c663968353)"><g class="toyplot-mark-Graph" id="t1709a06789d44a98988828392f23a854"><g class="toyplot-Edges"><path d="M 108.76097251624573 73.71708245126284 L 57.90569415042095 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.57236081708761 73.71708245126284 L 175.4276391829124 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.34433619633035 67.67766952966369 L 298.988997137003 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.10398980948028 62.862393885688164 L 428.5626768571864 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.3223304703363 67.67766952966369 L 67.67766952966369 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430584957906 73.71708245126284 L 191.23902748375428 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415042097 73.71708245126284 L 308.7609725162457 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766952966366 67.67766952966369 L 432.3223304703363 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.8960101905197 62.862393885688164 L 71.4373231428136 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.65566380366965 67.67766952966369 L 201.01100286299703 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.42763918291234 73.71708245126285 L 324.57236081708766 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.2390274837543 73.71708245126284 L 442.09430584957903 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.867504905630724 270.8012573584461 L 169.4658284277026 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.6666666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.33333333333334 275.0 L 183.33333333333334 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.20083823896408 270.8012573584461 L 302.799161761036 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761036 270.8012573584461 L 197.20083823896408 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.6666666666667 275.0 L 316.6666666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.33333333333334 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.1324950943693 270.8012573584461 L 330.5341715722974 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(83.33333333333334, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.3333333333333, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(150.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666669, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(216.66666666666663, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.0</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(283.33333333333337, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(350.0, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(416.66666666666663, 150.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(116.66666666666666, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.1</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(250.00000000000003, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(383.33333333333337, 350.0)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.3</text></g></g></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.90569415042095, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.56505117707798) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.988997137003, 232.3223304703363) rotate(44.99999999999999) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.5626768571864, 237.13760611431184) rotate(30.96375653207352) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.67766952966369, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.7609725162457, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.3223304703363, 232.3223304703363) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.4373231428136, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.1987426415539) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.6666666666667, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.799161761036, 429.1987426415539) rotate(56.30993247402021) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.3333333333333, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.6666666666667,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.3333333333333,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.6666666666667,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tf0903c1dc88b48159ee97dd214dea743";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tafac6c9e7e01436c8f59a9fa08d55fe6";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t1709a06789d44a98988828392f23a854","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t1709a06789d44a98988828392f23a854","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
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

    <div class="toyplot" id="tcada36a0b8d6498e9326c1d42832da32" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="500.0px" id="ta0560f16a4ba4972bb6bebe0b736bd63" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 500.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t48633a5b5398474186b1959683f6a593"><clipPath id="t6485f6fd85054f6a985a1d7791906ba3"><rect height="500.0" width="500.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t6485f6fd85054f6a985a1d7791906ba3)"><g class="toyplot-mark-Graph" id="t21fc7dc06a8d44eeab35d6f0ec27eab9"><g class="toyplot-Edges"><path d="M 108.76097251624573 73.71708245126284 L 57.90569415042095 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 124.57236081708761 73.71708245126284 L 175.4276391829124 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 134.34433619633035 67.67766952966369 L 298.988997137003 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 138.10398980948028 62.862393885688164 L 428.5626768571864 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 232.3223304703363 67.67766952966369 L 67.67766952966369 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 242.09430584957906 73.71708245126284 L 191.23902748375428 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 257.90569415042097 73.71708245126284 L 308.7609725162457 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 267.67766952966366 67.67766952966369 L 432.3223304703363 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.8960101905197 62.862393885688164 L 71.4373231428136 237.13760611431184" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 365.65566380366965 67.67766952966369 L 201.01100286299703 232.3223304703363" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 375.42763918291234 73.71708245126285 L 324.57236081708766 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 391.2390274837543 73.71708245126284 L 442.09430584957903 226.28291754873715" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 63.867504905630724 270.8012573584461 L 169.4658284277026 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 70.0 265.0 L 296.6666666666667 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 183.33333333333334 275.0 L 183.33333333333334 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 197.20083823896408 270.8012573584461 L 302.799161761036 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 302.799161761036 270.8012573584461 L 197.20083823896408 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 316.6666666666667 275.0 L 316.6666666666667 425.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 430.0 265.0 L 203.33333333333334 435.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 436.1324950943693 270.8012573584461 L 330.5341715722974 429.1987426415539" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(83.45187409667913, 149.6443777099626)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(160.59768938571924, 181.79306815715768)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.07834013244315, 134.41167346577646)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.24338417016236, 178.1460305020974)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(199.28855632256668, 100.71144367743332)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(211.93800660311027, 164.18598019066923)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(288.0733969785398, 164.2201909356194)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(309.3582020623752, 109.35820206237524)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.5</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(144.80505551532733, 193.1169666908036)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.0</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.2339173765009, 135.09941595683244)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(337.97164999510755, 186.08505001467745)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(398.4536855916558, 95.36105677496757)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(88.04962222609511, 307.0744333391427)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.6</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(100.18037090317375, 287.6352781773803)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.1</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 360.8624990761447)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(251.71463651120237, 352.5719547668035)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.9</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(252.81766801786313, 345.7734979732054)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.7</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 294.54902658295435)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.4</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(318.2526179632742, 348.81053652754434)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.8</text></g></g><g style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(401.20395811917496, 323.1940628212376)"><rect height="30" width="30" x="-15.0" y="-15.0"></rect><g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.3</text></g></g></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(57.90569415042095, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(175.4276391829124, 226.28291754873715) rotate(71.56505117707798) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(298.988997137003, 232.3223304703363) rotate(44.99999999999999) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(428.5626768571864, 237.13760611431184) rotate(30.96375653207352) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(67.67766952966369, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(191.23902748375428, 226.28291754873715) rotate(108.43494882292202) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(308.7609725162457, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(432.3223304703363, 232.3223304703363) rotate(45.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(71.4373231428136, 237.13760611431184) rotate(149.03624346792648) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(201.01100286299703, 232.3223304703363) rotate(135.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(324.57236081708766, 226.28291754873715) rotate(108.434948822922) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(442.09430584957903, 226.28291754873715) rotate(71.56505117707799) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(169.4658284277026, 429.1987426415539) rotate(56.309932474020215) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(296.6666666666667, 435.0) rotate(36.86989764584402) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(183.33333333333334, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(302.799161761036, 429.1987426415539) rotate(56.30993247402021) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(197.20083823896408, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(316.6666666666667, 425.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(203.33333333333334, 435.0) rotate(143.13010235415598) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(330.5341715722974, 429.1987426415539) rotate(123.69006752597979) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(50.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(450.0, 250.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(116.66666666666667, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(383.3333333333333, 50.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(183.33333333333334, 450.0)"><circle r="25.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(316.6666666666667, 450.0)"><circle r="25.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(50.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.19</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.62</text></g><g class="toyplot-Datum" transform="translate(316.6666666666667,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.44</text></g><g class="toyplot-Datum" transform="translate(450.0,250.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.79</text></g><g class="toyplot-Datum" transform="translate(116.66666666666667,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.78</text></g><g class="toyplot-Datum" transform="translate(250.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.27</text></g><g class="toyplot-Datum" transform="translate(383.3333333333333,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.28</text></g><g class="toyplot-Datum" transform="translate(183.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.80</text></g><g class="toyplot-Datum" transform="translate(316.6666666666667,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">0.96</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tcada36a0b8d6498e9326c1d42832da32";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "ta0560f16a4ba4972bb6bebe0b736bd63";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t21fc7dc06a8d44eeab35d6f0ec27eab9","vertex_data","graph vertex data",["x", "y"],[[0.0, 1.0, 2.0, 3.0, 0.5, 1.5, 2.5, 1.0, 2.0], [-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, -2.0, -2.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t21fc7dc06a8d44eeab35d6f0ec27eab9","edge_data","graph edge data",["source", "target"],[[4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 7, 8, 7, 8, 7, 8, 7, 8]],"toyplot");
    })();</script></div></div>


Note that the ``mposition`` argument is a value between zero and one
that positions each middle marker anywhere along its edge from beginning
to end, respectively.

Layer-Only Diagrams
-------------------

Once a network reaches a certain level of complexity, it is typical to
only diagram the layers in the network, instead of all the activation
units. Here, we define per-layer data for a simple layer-only diagram:

.. code:: python

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

.. code:: python

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

    <div class="toyplot" id="t318dd616ec0044e78d7c3f2a5cc2f1aa" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t0a617dbc8cb64a42b902065597897484" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 200.0 400.0" width="200.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t40d996f8b5294733a911080fcbfd1166"><clipPath id="t2d99992019c44f83b826c470cb1d6ee0"><rect height="400.0" width="200.0" x="0.0" y="0.0"></rect></clipPath><g clip-path="url(#t2d99992019c44f83b826c470cb1d6ee0)"><g class="toyplot-mark-Graph" id="t3185b58212aa4640965a5deca9002a0a"><g class="toyplot-Edges"><path d="M 100.0 75.0 L 100.0 125.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 100.0 175.0 L 100.0 225.00000000000003" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 100.0 275.0 L 100.0 325.0" style="fill:none;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-HeadMarkers"></g><g class="toyplot-MiddleMarkers"></g><g class="toyplot-TailMarkers"><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(100.0, 125.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(100.0, 225.00000000000003) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g><g style="fill:rgb(0%,0%,0%);fill-opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0;stroke-width:1.0" transform="translate(100.0, 325.0) rotate(90.0) translate(-5.0, 0)"><polygon points="-5.0,5.0 0,-5.0 5.0,5.0" transform="rotate(90)"></polygon></g></g></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(100.0, 50.0)"><rect height="50.0" width="150.0" x="-75.0" y="-25.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(100.0, 150.0)"><rect height="50.0" width="150.0" x="-75.0" y="-25.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(100.0, 250.00000000000003)"><rect height="50.0" width="150.0" x="-75.0" y="-25.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(100.0, 350.0)"><rect height="50.0" width="150.0" x="-75.0" y="-25.0"></rect></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(100.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="-4.133999999999999">conv1</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-46.86000000000001" y="10.265999999999998">3×3 convolutional</text></g><g class="toyplot-Datum" transform="translate(100.0,150.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.002000000000002" y="-4.133999999999999">pool1</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-32.346" y="10.265999999999998">max pooling</text></g><g class="toyplot-Datum" transform="translate(100.0,250.00000000000003)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-12.006" y="-4.133999999999999">fc_1</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-31.355999999999998" y="10.265999999999998">4096 dense</text></g><g class="toyplot-Datum" transform="translate(100.0,350.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-12.006" y="-4.133999999999999">fc_2</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-54.03" y="10.265999999999998">1000 dense softmax</text></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t318dd616ec0044e78d7c3f2a5cc2f1aa";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t0a617dbc8cb64a42b902065597897484";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t3185b58212aa4640965a5deca9002a0a","vertex_data","graph vertex data",["x", "y"],[[0.0, 0.0, 0.0, 0.0], [0.0, -1.0, -2.0, -3.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t3185b58212aa4640965a5deca9002a0a","edge_data","graph edge data",["source", "target"],[[0, 1, 2], [1, 2, 3]],"toyplot");
    })();</script></div></div>


