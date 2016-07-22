
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _text:

Text
====

Alignment
---------

By default, text in Toyplot is centered vertically and horizontally
around its *anchor*. To illustrate this, the following figures display
the anchor as a small black dot:

.. code:: python

    import toyplot
    
    canvas = toyplot.Canvas(width=500, height=150)
    axes = canvas.cartesian(show=False)
    axes.text(0, 0, "Text!", style={"font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3);



.. raw:: html

    <div align="center" class="toyplot" id="tef5f0ba1f526463fa06e309220ecfa48"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t7e1a0ce0587742dda4544460901644da" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 150.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t1457cb24d3324c32936a02987a9a8291"><clipPath id="t1e20c67537624f2d8d82c9d1e8f48185"><rect height="70.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t1e20c67537624f2d8d82c9d1e8f48185)"><g class="toyplot-mark-Text" id="t246b32d3fe1a481d933489d11d0c4217" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(250.0,75.0)"><tspan style="dominant-baseline:inherit">Text!</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tc16f815bf3f54e368ff5ca2f246036fe" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="75.0" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tc16f815bf3f54e368ff5ca2f246036fe", "columns": [[0.0], [0.0]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
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
                  var popup = document.querySelector("#tef5f0ba1f526463fa06e309220ecfa48 .toyplot-mark-popup");
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
            </script></div></div>


To control horizontal alignment, use the CSS ``text-anchor`` attribute
to change the position of the text along its baseline, relative to the
anchor:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.cartesian(show=False, ymin=-1.5, ymax=1.5)
    
    axes.vlines(0, color="lightgray")
    
    axes.text(0, 1, "Centered", style={"text-anchor":"middle", "font-size":"24px"})
    axes.scatterplot(0, 1, color="black", size=3)
    
    axes.text(0, 0, "Left Justified", style={"text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes.text(0, -1, "Right Justified", style={"text-anchor":"end", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black", size=3);



.. raw:: html

    <div align="center" class="toyplot" id="t813965cb2a4c4580bab9e4c1e092af25"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tecb6da8377884d86a21d822e2788e49f" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tff41466b16474da5995d8f4a21437cde"><clipPath id="t38832122c077493db8de67b3da54b706"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t38832122c077493db8de67b3da54b706)"><g class="toyplot-mark-AxisLines" id="tccdb16909be84d708fcd16eb47af09ee" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="256.89655172413791" x2="256.89655172413791" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t25e2a60686c949e68a81dc6f50b8310c" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(256.89655172413791,83.333333333333329)"><tspan style="dominant-baseline:inherit">Centered</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t7b672bb5c2e74cdc870c7d32d9e4a161" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="256.89655172413791" cy="83.333333333333329" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tdee42e0469b24735b5a9b87e531fdb30" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(256.89655172413791,150.0)"><tspan style="dominant-baseline:inherit">Left Justified</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t138065b8c0a84c5fb5648d46fe213259" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="256.89655172413791" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t0cbb4653920a41e9b6fe7809b1d96d85" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:end"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:end" transform="translate(256.89655172413791,216.66666666666669)"><tspan style="dominant-baseline:inherit">Right Justified</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tc914ed6345b349fc9950743d4ea93820" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="256.89655172413791" cy="216.66666666666669" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t7b672bb5c2e74cdc870c7d32d9e4a161", "columns": [[0.0], [1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t138065b8c0a84c5fb5648d46fe213259", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tc914ed6345b349fc9950743d4ea93820", "columns": [[0.0], [-1.0]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
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
                  var popup = document.querySelector("#t813965cb2a4c4580bab9e4c1e092af25 .toyplot-mark-popup");
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
            </script></div></div>


In addition, the text can be shifted along its baseline in arbitrary
amounts, using the ``-toyplot-anchor-shift`` attribute (note that this
is non-standard CSS, provided by Toyplot for symmetry with the standard
``baseline-shift`` attribute which we will explore below):

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    axes = canvas.cartesian(show=False, ymin=-2.5, ymax=1.5)
    
    axes.vlines(0, color="lightgray")
    
    axes.text(0, 1, "Shifted +0px", style={"-toyplot-anchor-shift":"0", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 1, color="black", size=3)
    
    axes.text(0, 0, "Shifted +20px", style={"-toyplot-anchor-shift":"20px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes.text(0, -1, "Shifted +40px", style={"-toyplot-anchor-shift":"40px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, -1, color="black", size=3);
    
    axes.text(0, -2, "Shifted -20px", style={"-toyplot-anchor-shift":"-20px", "text-anchor":"start", "font-size":"24px"})
    axes.scatterplot(0, -2, color="black", size=3);




.. raw:: html

    <div align="center" class="toyplot" id="tef8e7d7926974e7d982f4e09e9cb6e52"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t193800f1ad5048d5b07226f15668da2d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t2f3a117d2647443bb78c2879890f37f3"><clipPath id="te60fa3de634b4eeeb2dad81c22854b6c"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#te60fa3de634b4eeeb2dad81c22854b6c)"><g class="toyplot-mark-AxisLines" id="t5caaa41d2d4846c4b15f447421663d30" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="194.92753623188409" x2="194.92753623188409" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="td31efafaa21c4c48a5bc94fb1da01d83" style="-toyplot-anchor-shift:0;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(194.92753623188409,75.0)"><tspan style="dominant-baseline:inherit">Shifted +0px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tedafb33fe4014a4ca4840ca686f2ce90" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="194.92753623188409" cy="75.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t9adce94288ac403f884bf52e8e55e1cc" style="-toyplot-anchor-shift:20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(194.92753623188409,125.0)translate(20.0,0)"><tspan style="dominant-baseline:inherit">Shifted +20px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t1d7f0894583a4920becca67ad4229051" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="194.92753623188409" cy="125.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tcb8b6a78ef5d4fd0a0407ed8fc554fa2" style="-toyplot-anchor-shift:40px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(194.92753623188409,175.0)translate(40.0,0)"><tspan style="dominant-baseline:inherit">Shifted +40px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t7e58388b07d74123a8da3f7c751e44d3" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="194.92753623188409" cy="175.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t1a499401d95746a0abfe57f37558153d" style="-toyplot-anchor-shift:-20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(194.92753623188409,225.0)translate(-20.0,0)"><tspan style="dominant-baseline:inherit">Shifted -20px</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t9a8faf6c9cec4700be7baef416bff312" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="194.92753623188409" cy="225.0" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tedafb33fe4014a4ca4840ca686f2ce90", "columns": [[0.0], [1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t1d7f0894583a4920becca67ad4229051", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t7e58388b07d74123a8da3f7c751e44d3", "columns": [[0.0], [-1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t9a8faf6c9cec4700be7baef416bff312", "columns": [[0.0], [-2.0]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
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
                  var popup = document.querySelector("#tef8e7d7926974e7d982f4e09e9cb6e52 .toyplot-mark-popup");
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
            </script></div></div>


Vertically, the text baseline always passes through its anchor point -
so to alter the vertical alongment of text, you change the baseline
using the CSS ``alignment-baseline`` attribute. Note that CSS typography
is a complex topic and there are many different types of baseline to
accomodate different writing modes and fonts. The following baselines
are the most useful for Western scripts. Note the subtle difference
between the "central" and "middle" baselines - the former centers
upper-case letters in Western scripts while the latter centers
lower-case letters, and is the Toyplot default:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.cartesian(show=False)
    
    axes.hlines(0, color="lightgray")
    
    axes.text(-1, 0, "Hanging", style={"alignment-baseline":"hanging", "font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=3)
    
    axes.text(0, 0, "Central", style={"alignment-baseline":"central", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes.text(1, 0, "Middle", style={"alignment-baseline":"middle", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black", size=3)
    
    axes.text(2, 0, "Alpha", style={"alignment-baseline":"alphabetic", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black", size=3);




.. raw:: html

    <div align="center" class="toyplot" id="tfb1107d67ec345de9b195e2aff6acd79"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t249f918741b24cabba89718514f86716" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t30fc95fc93704b7a8edd78ab23b3752c"><clipPath id="t19b90836d20644edaf2ab1c93daef10f"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t19b90836d20644edaf2ab1c93daef10f)"><g class="toyplot-mark-AxisLines" id="t63d078432bff43538972d3c15584bd65" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="550.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t7330d6a5db604d7ab80edb390221398c" style="alignment-baseline:hanging;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:hanging;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(115.21739130434783,150.0)"><tspan style="dominant-baseline:inherit">Hanging</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t8232609e4cb24cedb432834d39121b48" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="115.21739130434783" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tbc63644d96ff4a99b882e332537d5e4b" style="alignment-baseline:central;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:central;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(244.61697722567285,150.0)"><tspan style="dominant-baseline:inherit">Central</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t6bc7cced308f4050a78b32dfe9ba1bfd" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="244.61697722567285" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t7ebea5cb09f542989e9d9b442b15dfa1" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(374.0165631469979,150.0)"><tspan style="dominant-baseline:inherit">Middle</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="ta477615f96c145f7a53d88b7c7981716" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="374.0165631469979" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t01cabecbcaf74a239e402362fe43c74e" style="alignment-baseline:alphabetic;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:alphabetic;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(503.41614906832291,150.0)"><tspan style="dominant-baseline:inherit">Alpha</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t7a5a7906481a4eff947ee656f35d7b09" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="503.41614906832291" cy="150.0" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t8232609e4cb24cedb432834d39121b48", "columns": [[-1.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t6bc7cced308f4050a78b32dfe9ba1bfd", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "ta477615f96c145f7a53d88b7c7981716", "columns": [[1.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t7a5a7906481a4eff947ee656f35d7b09", "columns": [[2.0], [0.0]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
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
                  var popup = document.querySelector("#tfb1107d67ec345de9b195e2aff6acd79 .toyplot-mark-popup");
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
            </script></div></div>


As you might expect, you can also shift text perpendicular to its
baseline by arbitrary amounts, using ``baseline-shift``. While you are
free to use any of Toyplot's supported CSS length units for the shift,
percentages are especially useful, because they represent a distance
relative to the font height:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=300)
    axes = canvas.cartesian(show=False)
    
    axes.hlines(0, color="lightgray")
    
    axes.text(-1, 0, "Shift -100%", style={"baseline-shift":"-100%", "font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=3)
    
    axes.text(0, 0, "Shift 0%", style={"baseline-shift":"0", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes.text(1, 0, "Shift 66%", style={"baseline-shift":"66%", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black", size=3)
    
    axes.text(2, 0, "Shift 100%", style={"baseline-shift":"100%", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black", size=3);




.. raw:: html

    <div align="center" class="toyplot" id="ta3d4c61f7ae04c7da8b19c91cce8fab5"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t4699595f801648a0b390d45005b67ad9" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 300.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="td05866b2689d4fe5816c1a3c88de359f"><clipPath id="t58bebfa10d1a4a39ab0eb488cf4e0090"><rect height="220.0" width="620.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t58bebfa10d1a4a39ab0eb488cf4e0090)"><g class="toyplot-mark-AxisLines" id="tabc6ff470d0f467d8e99bbc0a2cf3082" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="650.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t2cb8b22bb4bb4456a12a7a5e349ea426" style="alignment-baseline:middle;baseline-shift:-100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(142.95774647887322,150.0)translate(0,24.0)"><tspan style="dominant-baseline:inherit">Shift -100%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tc03d13f97acd48a19b43b13b529b3b89" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="142.95774647887322" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tb45025994e0d4c839bbde0ed38f9cbe9" style="alignment-baseline:middle;baseline-shift:0;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(283.80281690140845,150.0)"><tspan style="dominant-baseline:inherit">Shift 0%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="ted25a1e8a69f49eca83e2b354dbfae76" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="283.80281690140845" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t40a9678fdafe462c9b074563851b08c6" style="alignment-baseline:middle;baseline-shift:66%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(424.64788732394368,150.0)translate(0,-15.84)"><tspan style="dominant-baseline:inherit">Shift 66%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tb10ebdb651bf48b0846dd52aab620142" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="424.64788732394368" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tc9708d66506f46bbbae87747ce343d2a" style="alignment-baseline:middle;baseline-shift:100%;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(565.49295774647896,150.0)translate(0,-24.0)"><tspan style="dominant-baseline:inherit">Shift 100%</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t552f092c5b6b475ca76d64912c31f9ab" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="565.49295774647896" cy="150.0" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tc03d13f97acd48a19b43b13b529b3b89", "columns": [[-1.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "ted25a1e8a69f49eca83e2b354dbfae76", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tb10ebdb651bf48b0846dd52aab620142", "columns": [[1.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t552f092c5b6b475ca76d64912c31f9ab", "columns": [[2.0], [0.0]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
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
                  var popup = document.querySelector("#ta3d4c61f7ae04c7da8b19c91cce8fab5 .toyplot-mark-popup");
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
            </script></div></div>


Of course, you're free to combine all four styles in any way that you
like.

One final thing to keep in mind is that ``-toyplot-anchor-shift`` and
``baseline-shift`` move the text relative to its baseline, not the
canvas. This is important because it affects their behavior when text is
rotated. In the following example, look carefully and note that the text
with ``-toyplot-anchor-shift`` is shifted *along its rotated baseline*,
not simply moved left or right on the canvas. Similarly, the
``baseline-shift`` text is shifted *perpendicular to its rotated
baseline*, not merely up or down:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=300)
    
    axes = canvas.cartesian(grid=(1,3,0), xshow=False, yshow=False, label="default")
    axes.vlines(0, color="lightgray")
    axes.text(0, 0, "a + b", angle=45, style={"font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes = canvas.cartesian(grid=(1,3,1), xshow=False, yshow=False, label="-toyplot-anchor-shift")
    axes.vlines(0, color="lightgray")
    axes.text(0, 0, "a + b", angle=45, style={"-toyplot-anchor-shift":"20px", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes = canvas.cartesian(grid=(1,3,2), xshow=False, yshow=False, label="baseline-shift")
    axes.vlines(0, color="lightgray")
    axes.text(0, 0, "a + b", angle=45, style={"baseline-shift":"-20px", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3);




.. raw:: html

    <div align="center" class="toyplot" id="t444e304f5a524a80b5ff1c2551949045"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t5a7a9c814a814e55b41b1d12d2b493ce" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="td9b2800d25e2495681d819c06ccf7b67"><clipPath id="t4638c3e73c204bbdb6fe95d2d3ccd185"><rect height="220.0" width="86.66666666666666" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t4638c3e73c204bbdb6fe95d2d3ccd185)"><g class="toyplot-mark-AxisLines" id="t5156d764ba614235b108d6f22bcab2a1" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="83.333333333333329" x2="83.333333333333329" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t1608180ae2584787b9c02f58f2b6e3d9" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(83.333333333333329,150.0)rotate(-45.0)"><tspan style="dominant-baseline:inherit">a + b</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tf4447cb5ebf94e6ea1613681b730be89" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="83.333333333333329" cy="150.0" r="1.5"></circle></g></g></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(83.33333333333333,50.0)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">default</tspan></text></g><g class="toyplot-coordinates-Cartesian" id="t4dd85c0c92e044cb90f5558cb99145e9"><clipPath id="t0a4118da921240d197c2c64154c754a2"><rect height="220.0" width="86.66666666666666" x="206.66666666666666" y="40.0"></rect></clipPath><g clip-path="url(#t0a4118da921240d197c2c64154c754a2)"><g class="toyplot-mark-AxisLines" id="t9bf5e9135b2b49bfa5319c3c225355bc" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="240.7407407407407" x2="240.7407407407407" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="tcd33e8eeefd849709e5d5517562c0b22" style="-toyplot-anchor-shift:20px;alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(240.7407407407407,150.0)rotate(-45.0)translate(20.0,0)"><tspan style="dominant-baseline:inherit">a + b</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="tc19d21cc661343f9a6c04baa79955d62" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="240.7407407407407" cy="150.0" r="1.5"></circle></g></g></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(250.0,50.0)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">-toyplot-anchor-shift</tspan></text></g><g class="toyplot-coordinates-Cartesian" id="t72bdd3948c0143e1b01889c297c31581"><clipPath id="t5d33c8bf521341a6bea381c6bc866ee1"><rect height="220.0" width="86.66666666666669" x="373.3333333333333" y="40.0"></rect></clipPath><g clip-path="url(#t5d33c8bf521341a6bea381c6bc866ee1)"><g class="toyplot-mark-AxisLines" id="t91c24ec32e7c4323aa798a4dfd6bace8" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="407.40740740740739" x2="407.40740740740739" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t7017e178ab8b4421acfd7dd82f43ba79" style="alignment-baseline:middle;baseline-shift:-20px;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(407.40740740740739,150.0)rotate(-45.0)translate(0,20.0)"><tspan style="dominant-baseline:inherit">a + b</tspan></text></g></g><g class="toyplot-mark-Scatterplot" id="t9c2a45c6f3a641c1a9fb9d17d6bd1c36" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="407.40740740740739" cy="150.0" r="1.5"></circle></g></g></g></g><text style="dominant-baseline:middle;font-size:14px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(416.66666666666663,50.0)translate(0,-14.0)"><tspan style="dominant-baseline:inherit">baseline-shift</tspan></text></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tf4447cb5ebf94e6ea1613681b730be89", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tc19d21cc661343f9a6c04baa79955d62", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t9c2a45c6f3a641c1a9fb9d17d6bd1c36", "columns": [[0.0], [0.0]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
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
                  var popup = document.querySelector("#t444e304f5a524a80b5ff1c2551949045 .toyplot-mark-popup");
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
            </script></div></div>


Rich Text
---------

In addition to positioning text using styles, you can use (a limited
subset of) HTML markup to format your text. For example, you can create
text with superscripts and subscripts:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "100<sup>-53</sup>", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="t223e01f2e1e84f8890f0ab2659ad73a3"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t65a88cbbb9b94fbd8bbd1ba849c46806" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="tf7c3957fdeaa42558f2bbc64a092fd98" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">100</tspan><tspan dy="-9.6" style="dominant-baseline:inherit;font-size:22.4px">-53</tspan></text></g></g></svg><div class="toyplot-interactive"></div></div>


.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "H<sub>2</sub>O", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="t865919494476496484b106759c5b9d89"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t01e25658e26745e9ace78c52d6cdbc80" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="td5c6bfc178b649afb2d3b5ffc2b5cd0b" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">H</tspan><tspan dy="6.4" style="dominant-baseline:inherit;font-size:22.4px">2</tspan><tspan dy="-6.4" style="dominant-baseline:inherit">O</tspan></text></g></g></svg><div class="toyplot-interactive"></div></div>


Note that you are free to nest superscripts and subscripts:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "W<sup>X<sub>Y</sub><sup>Z</sup></sup>", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="t5bc54c39ab324d5db7083083f83488d5"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t8d329d49aa6d427099781b10ee4f6fa0" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t59c31cc14ef04df4ba019d8c6a63da92" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">W</tspan><tspan dy="-9.6" style="dominant-baseline:inherit;font-size:22.4px">X</tspan><tspan dy="4.48" style="dominant-baseline:inherit;font-size:15.68px">Y</tspan><tspan dy="-11.2" style="dominant-baseline:inherit;font-size:15.68px">Z</tspan></text></g></g></svg><div class="toyplot-interactive"></div></div>


There are a variety of tags to alter the inline appearance of text:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(
        300,
        100,
        "normal <b>bold</b> <i>italic</i> <strong>strong</strong> <em>emphasis</em> <small>small</small> <code>code</code>",
        style={"font-size":"24px"});



.. raw:: html

    <div align="center" class="toyplot" id="t3bb3a075587f4f79af60814ebaf9b518"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t14511e22311f4414b989dfaf656c42f7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t8a0a2858b3004cadb9c4d26dbc84a87b" style="alignment-baseline:middle;font-size:24px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:24px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">normal </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">bold</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-style:italic">italic</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">strong</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-style:italic">emphasis</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-size:19.2px">small</tspan><tspan style="dominant-baseline:inherit"> </tspan><tspan style="dominant-baseline:inherit;font-family:monospace">code</tspan></text></g></g></svg><div class="toyplot-interactive"></div></div>


And these tags can be nested as well:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "foo <b>bar <i>baz <code>blah</code></i></b>", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="te89554e170f84b8eb4bef688bcdf8780"><svg class="toyplot-canvas-Canvas" height="150.0px" id="tb9e7e2f2076b408c8a06f3d7cf6f1bde" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="tdcaa7d8a42814e668312ae54b50bfe52" style="alignment-baseline:middle;font-size:32px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:32px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">foo </tspan><tspan style="dominant-baseline:inherit;font-weight:bold">bar </tspan><tspan style="dominant-baseline:inherit;font-style:italic;font-weight:bold">baz </tspan><tspan style="dominant-baseline:inherit;font-family:monospace;font-style:italic;font-weight:bold">blah</tspan></text></g></g></svg><div class="toyplot-interactive"></div></div>


Finally, you can insert line breaks into your text using the <br> tag:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    canvas.text(300, 100, "0.567832<br><small>(243, 128, 19)</small>", style={"font-size":"16px"});



.. raw:: html

    <div align="center" class="toyplot" id="td1b13b11348c424fb5b652ff8a6b54cb"><svg class="toyplot-canvas-Canvas" height="200.0px" id="t68f5f74dbbd8442089a55a478f3d046b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t9261753baf3f4ddb92bc5fafb64df28c" style="alignment-baseline:middle;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:16px;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(300.0,100.0)"><tspan style="dominant-baseline:inherit">0.567832</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(243, 128, 19)</tspan></text></g></g></svg><div class="toyplot-interactive"></div></div>


Note that additional tags and style attributes currently aren't allowed
in rich-text. We expect that the set of tags and attributes will expand
in the future.

Keep in mind that you can use rich text formatting anywhere that text is
displayed, including table cells, axis labels and tick labels. You can
also use rich text in format strings for tick locators - as an example,
the :class:`toyplot.locator.Log` locator uses superscript tags to
format tick labels for :ref:`log-scales`.

Coordinate System Text
----------------------

In addition to all the above, :ref:`cartesian-coordinates` and
:ref:`numberline-coordinates` provide additional parameters that
affect text layout and alignment.

First, ticks and labels have a parameter ``location`` that controls
whether they appear above or below an axis:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    
    numberline1 = canvas.numberline(grid=(2, 1, 0))
    numberline1.axis.ticks.location="above"
    
    numberline2 = canvas.numberline(grid=(2, 1, 1))
    numberline2.axis.ticks.location="below"



.. raw:: html

    <div align="center" class="toyplot" id="t25b8034863b14ff09d431155d36ca9ac"><svg class="toyplot-canvas-Canvas" height="200.0px" id="te7d6a996cd574dc9857cc2c417ed3f86" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t42a5577c6aed45de940b31afc58ef993"><clipPath id="t706647d77ee842f7817a0bacdb0c7767"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t706647d77ee842f7817a0bacdb0c7767)" transform="translate(50.0,50.0)"></g><g class="toyplot-coordinates-Axis" id="t0608c6cec1644c259f25fdf144330e5c" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="tce1021700b2041eb92baedc3b1aa905d"><clipPath id="tba356357936d49b49deafbde91517e72"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#tba356357936d49b49deafbde91517e72)" transform="translate(50.0,150.0)"></g><g class="toyplot-coordinates-Axis" id="t443d92e492b94293ac65dba45e84f1bc" transform="translate(50.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t25b8034863b14ff09d431155d36ca9ac";
                var axes = {"t0608c6cec1644c259f25fdf144330e5c": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "t443d92e492b94293ac65dba45e84f1bc": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Note that although the location can be specified explicitly, in most
cases the defaults should just work ... note how the location of the Y
axis ticks and labels automatically changes from "above" to "below" when
the Y axis spine is repositioned in the following example:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    
    axis1 = canvas.cartesian(grid=(1, 2, 0))
    
    axis2 = canvas.cartesian(grid=(1, 2, 1))
    axis2.y.spine.position="high"



.. raw:: html

    <div align="center" class="toyplot" id="t3d84cd237c7a43bd9feb717651d7919c"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t2ee6d0f6a4f1403d939e0a5acb64a94d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tdc2978bb9aae4504a8fddabd3ca9388c"><clipPath id="tdea4296afbed4fb99d0493ac53f86f97"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tdea4296afbed4fb99d0493ac53f86f97)"></g><g class="toyplot-coordinates-Axis" id="t3c3a5dee826d417899d004dbaada06aa" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="teb8084db1da545f5835a7257ca9bb7b9" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t3b26aac363844a6986f9e035cfd47a56"><clipPath id="t27af0d82b5e24d359b6c964cc989faec"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t27af0d82b5e24d359b6c964cc989faec)"></g><g class="toyplot-coordinates-Axis" id="t8ea3fc0e3cdb45f4b1e95dedba366a1d" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t2832ef57494c4dc6bd81c8d1b0e4aa26" transform="translate(550.0,250.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t3d84cd237c7a43bd9feb717651d7919c";
                var axes = {"t2832ef57494c4dc6bd81c8d1b0e4aa26": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t3c3a5dee826d417899d004dbaada06aa": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t8ea3fc0e3cdb45f4b1e95dedba366a1d": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "teb8084db1da545f5835a7257ca9bb7b9": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


In addition to positioning tick labels above or below an axis, you can
also adjust their ``offset`` - the distance from the axis spine to the
text anchor. The ``offset`` parameter is specified so that increasing
values move text further from the axis, whether its location is above or
below - in the following example, note that both offsets are positive:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    
    axis1 = canvas.cartesian(grid=(1, 2, 0))
    axis1.y.ticks.labels.offset=30
    
    axis2 = canvas.cartesian(grid=(1, 2, 1))
    axis2.y.spine.position="high"
    axis2.y.ticks.labels.offset=30



.. raw:: html

    <div align="center" class="toyplot" id="t816ba2e1198441e9b756cd3e5925d5e5"><svg class="toyplot-canvas-Canvas" height="300.0px" id="ted3eb201558244bf8d4f99ac49ed087f" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tca6da6b4f99e44d483c80e4b48b8ea89"><clipPath id="t81465fd730c54af79ec52130ec8724a5"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t81465fd730c54af79ec52130ec8724a5)"></g><g class="toyplot-coordinates-Axis" id="tf698a1246feb46ed9a6b9d19bd8d4c02" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t20e28e725031466886b69e521615f5b1" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-30.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-30.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-30.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="15.0" y2="-22.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="30.0"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="tb6a33af753f8411bb56c44aabfe78632"><clipPath id="t8dd3b8d8a5734b339b77df522dbdb3ee"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t8dd3b8d8a5734b339b77df522dbdb3ee)"></g><g class="toyplot-coordinates-Axis" id="te0d469bb978d491abd0e0178e039ffd0" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tf583c93efb9b45ec9256623ad36d604d" transform="translate(550.0,250.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,30.0)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,30.0)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,30.0)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-15.0" y2="22.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-30.0"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t816ba2e1198441e9b756cd3e5925d5e5";
                var axes = {"t20e28e725031466886b69e521615f5b1": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "te0d469bb978d491abd0e0178e039ffd0": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tf583c93efb9b45ec9256623ad36d604d": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tf698a1246feb46ed9a6b9d19bd8d4c02": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


The default text alignment parameters have been carefully chosen to
provide good quality layout even if you change the label font size, and
regardless of label location:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=400)
    
    numberline1 = canvas.numberline(grid=(4, 1, 0))
    numberline1.axis.ticks.location="above"
    
    numberline2 = canvas.numberline(grid=(4, 1, 1))
    numberline2.axis.ticks.location="above"
    numberline2.axis.ticks.labels.style = {"font-size":"16px"}
    
    numberline3 = canvas.numberline(grid=(4, 1, 2))
    numberline3.axis.ticks.location="below"
    
    numberline4 = canvas.numberline(grid=(4, 1, 3))
    numberline4.axis.ticks.location="below"
    numberline4.axis.ticks.labels.style = {"font-size":"16px"}



.. raw:: html

    <div align="center" class="toyplot" id="tdcaea476d9344d4ab30e9d9fd5b0c525"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t39c9045afed84a86909a03dc0d17b2cf" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 400.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t2fa3fdbda0b54b0287bc71b27fee0160"><clipPath id="t22624b5c9e124113a03a8f998ec5cd33"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t22624b5c9e124113a03a8f998ec5cd33)" transform="translate(50.0,50.0)"></g><g class="toyplot-coordinates-Axis" id="tfbb10fa79f7e4b0ab2fea77b34bd8ab4" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t25f2d1f055864833ab7a807694ec4591"><clipPath id="t1583602972c4414284f39c4256ebcaee"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t1583602972c4414284f39c4256ebcaee)" transform="translate(50.0,150.0)"></g><g class="toyplot-coordinates-Axis" id="tc755a18ce30e4b4098a1432abc7ca9cf" transform="translate(50.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t524460798cd34ba5b517cdb3d9aa82fd"><clipPath id="ta563b4ea128646dd94d5b38f3ba1745c"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#ta563b4ea128646dd94d5b38f3ba1745c)" transform="translate(50.0,250.0)"></g><g class="toyplot-coordinates-Axis" id="tf8b8c1e6fbe440cab971f0d4191dd9d5" transform="translate(50.0,250.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t69714f345d0642129c56e6947206d65c"><clipPath id="t69ab5b952af643559ffa22370ae8e70a"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t69ab5b952af643559ffa22370ae8e70a)" transform="translate(50.0,350.0)"></g><g class="toyplot-coordinates-Axis" id="t870931cf9e3a411cb8f6a2a47a9c7f8a" transform="translate(50.0,350.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:hanging;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "tdcaea476d9344d4ab30e9d9fd5b0c525";
                var axes = {"t870931cf9e3a411cb8f6a2a47a9c7f8a": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tc755a18ce30e4b4098a1432abc7ca9cf": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tf8b8c1e6fbe440cab971f0d4191dd9d5": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tfbb10fa79f7e4b0ab2fea77b34bd8ab4": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Similarly, alignment parameters are automatically adjusted when you
rotate tick labels, adjusting the anchor and baseline to provide good
results:

.. code:: python

    import numpy
    
    colormap = toyplot.color.brewer.map("BlueRed", domain_min=0, domain_max=1)
    
    canvas = toyplot.Canvas()
    numberline = canvas.color_scale(x1="50%", x2="50%", y1="-10%", y2="10%", colormap=colormap)
    numberline.axis.ticks.show = True
    numberline.axis.ticks.labels.angle=-90



.. raw:: html

    <div align="center" class="toyplot" id="t82aaabcd3a894608ae50073166204783"><svg class="toyplot-canvas-Canvas" height="600px" id="t8b731c2f7e894c9a814889f3b821bdf2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="tc8fbef799c194f0f9a87317755cd7d47"><clipPath id="te1582e093f8f424292008ce978bde2f0"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#te1582e093f8f424292008ce978bde2f0)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t9d194298120b493f90127e028387a5e8"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tbbd3d887a5174c13bcd991b75c99ed7b" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tbbd3d887a5174c13bcd991b75c99ed7b);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t7bef049d03a048cb88f0c58f41eab4dd" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="240.0" x2="240.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><text style="dominant-baseline:central;font-size:10px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(0.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:central;font-size:10px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(240.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:central;font-size:10px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(480.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t82aaabcd3a894608ae50073166204783";
                var axes = {"t7bef049d03a048cb88f0c58f41eab4dd": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Of-course, you are free to override any of these behaviors. For example,
suppose we use rich text to add multi-line tick labels to the preceding
example:

.. code:: python

    def format_color(color):
        return "(%.2f, %.2f, %.2f)" % (color["r"], color["g"], color["b"])
    
    values = numpy.linspace(colormap.domain.min, colormap.domain.max, 4)
    labels = ["%.4f<br><small>%s</small>" % (value, format_color(colormap.color(value))) for value in values]
    locator = toyplot.locator.Explicit(values, labels)

.. code:: python

    canvas = toyplot.Canvas()
    numberline = canvas.color_scale(x1="50%", x2="50%", y1="-10%", y2="10%", colormap=colormap)
    numberline.axis.ticks.show = True
    numberline.axis.ticks.labels.angle=-90
    
    numberline.axis.ticks.locator = locator
    numberline.axis.ticks.labels.style = {"font-size":"16px"}



.. raw:: html

    <div align="center" class="toyplot" id="t4d8f98481e894bc0874fe35c340cbe10"><svg class="toyplot-canvas-Canvas" height="600px" id="t30ec733a6aa24106aa656255163a5c79" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t0213b9d4115b480083e79c800cd95ade"><clipPath id="t7dfdf83dee2d4ba6b27c06dc56574573"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t7dfdf83dee2d4ba6b27c06dc56574573)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t166dc337caaa4381862408bc348a17a1"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tbc49a46c2c354cd59abaaf87fd14f219" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tbc49a46c2c354cd59abaaf87fd14f219);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="tb2b53709d9d045919e00131ef557be9a" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="160.0" x2="160.0" y1="3" y2="-3"></line><line style="" x1="320.0" x2="320.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(0.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">0.0000</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.02, 0.19, 0.38)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(160.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">0.3333</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.65, 0.81, 0.89)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(320.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">0.6667</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.97, 0.72, 0.60)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:start" transform="translate(480.0,6)rotate(90)"><tspan style="dominant-baseline:inherit">1.0000</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.40, 0.00, 0.12)</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t4d8f98481e894bc0874fe35c340cbe10";
                var axes = {"tb2b53709d9d045919e00131ef557be9a": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


We might choose to center the labels horizontally and vertically,
overriding the defaults:

.. code:: python

    canvas = toyplot.Canvas()
    numberline = canvas.color_scale(x1="50%", x2="50%", y1="-10%", y2="10%", colormap=colormap)
    numberline.axis.ticks.labels.angle=-90
    numberline.axis.ticks.show = True
    numberline.axis.ticks.locator = locator
    numberline.axis.ticks.labels.style = {"font-size":"16px"}
    
    numberline.axis.ticks.labels.style = {"baseline-shift":"10px"}
    numberline.axis.ticks.labels.style = {"text-anchor":"middle"}
    numberline.axis.ticks.labels.offset = 60



.. raw:: html

    <div align="center" class="toyplot" id="t2b72c7103d9c4f3d89e64e9b7d7e1a2c"><svg class="toyplot-canvas-Canvas" height="600px" id="t6e897bc43c4f482cbc64c7cc1615e70f" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t1cc1b8dbfb4f408b8812800fa6b27b0a"><clipPath id="t9b3ba992bbb44608b6d0311417fad7c9"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t9b3ba992bbb44608b6d0311417fad7c9)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t8dd17070ab144a6fa89dafbc99591abf"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tc9058cf8993b4e43af25c59f7273dd0c" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tc9058cf8993b4e43af25c59f7273dd0c);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t1d7fa47812d3445293a2a8b62386db2a" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="160.0" x2="160.0" y1="3" y2="-3"></line><line style="" x1="320.0" x2="320.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,60.0)rotate(90)translate(0,-10.0)"><tspan style="dominant-baseline:inherit">0.0000</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.02, 0.19, 0.38)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(160.0,60.0)rotate(90)translate(0,-10.0)"><tspan style="dominant-baseline:inherit">0.3333</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.65, 0.81, 0.89)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(320.0,60.0)rotate(90)translate(0,-10.0)"><tspan style="dominant-baseline:inherit">0.6667</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.97, 0.72, 0.60)</tspan></text><text style="dominant-baseline:central;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(480.0,60.0)rotate(90)translate(0,-10.0)"><tspan style="dominant-baseline:inherit">1.0000</tspan><tspan dy="19.2" style="dominant-baseline:inherit;font-size:12.8px" x="0">(0.40, 0.00, 0.12)</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-30.0" y2="45.0"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-60.0"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t2b72c7103d9c4f3d89e64e9b7d7e1a2c";
                var axes = {"t1d7fa47812d3445293a2a8b62386db2a": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>

