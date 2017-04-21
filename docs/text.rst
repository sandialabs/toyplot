
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _text:

Text
====

Rich Text
---------

Toyplot provides a limited subset of HTML5 markup that you can use to
format your text (technically, Toyplot uses the *XHTML5 Syntax* for
HTML5, but this distinction only shows-up when using the <br/> tag,
discussed below). For example, you can create text with superscripts and
subscripts:

.. code:: python

    import toyplot
    
    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "100<sup>-53</sup>", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="tbc19b8d7b4f249f29e360d97d87ad863"><svg class="toyplot-canvas-Canvas" height="150.0px" id="tc31047d6a0cd49889a0dd392dba0f36a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t7e69cce87f194a83b46240c7e609775b"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-42.872" y="8.176">100</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:22.4;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="10.504" y="1.456">-53</text></g></g></g></svg><div class="toyplot-interactive"></div></div>


.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "H<sub>2</sub>O", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="t91ddee7fd3044d179361d6ccff92ea40"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t8ebb9b437f9c42209a67cd73b074a8cb" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t9cacaba156f1480a821d91fe6b3ae56f"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-30.2272" y="8.176">H</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:22.4;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-7.1232" y="12.656">2</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="5.3312" y="8.176">O</text></g></g></g></svg><div class="toyplot-interactive"></div></div>


There are a variety of tags to alter the inline appearance of text:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(
        300,
        100,
        "normal <b>bold</b> <i>italic</i> <strong>strong</strong> <em>emphasis</em> <small>small</small> <code>code</code>",
        style={"font-size":"24px"});



.. raw:: html

    <div align="center" class="toyplot" id="tef8ab2645865417198d0846811bb5fd9"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t31148c887bba4e9e90759f8d8ed7375c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t111ce41c3e3d44e78354b90a01308d5a"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-245.8968" y="6.132">normal </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-165.8808" y="6.132">bold</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-115.2168" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-style:italic;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-108.5448" y="6.132">italic</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-60.5448" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-53.8728" y="6.132">strong</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="20.7912" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-style:italic;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="27.4632" y="6.132">emphasis</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="130.1592" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:19.2;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="136.8312" y="6.132">small</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="181.6248" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="188.2968" y="6.132">code</text></g></g></g></svg><div class="toyplot-interactive"></div></div>


And these tags can be nested to combine effects:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "foo <b>bar <i>baz <code>blah</code></i></b>", style={"font-size":"32px"});



.. raw:: html

    <div align="center" class="toyplot" id="tbe4d1d0edf314c41b129fca6f3115266"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t0314d65143e94d92b82feaf6beeb15a6" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="tbcd7fe44dcf04ec0bfa18d9425b1d2f1"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-125.552" y="8.176">foo </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-72.176" y="8.176">bar </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0;font-style:italic;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-13.488" y="8.176">baz </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:32.0;font-style:italic;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="48.752" y="8.176">blah</text></g></g></g></svg><div class="toyplot-interactive"></div></div>


You can insert line breaks into your text using the ``<br/>`` tag:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    canvas.text(300, 100, "0.567832<br/><small>(243, 128, 19)</small>", style={"font-size":"16px"});



.. raw:: html

    <div align="center" class="toyplot" id="t1875c62b541047bcb829d2c695d67a3d"><svg class="toyplot-canvas-Canvas" height="200.0px" id="t458d8c348c87458c8fddd5df03b9cf17" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t69b2a653b7864d1bbfb6369e21869d7d"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-33.36" y="-3.592">0.567832</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-39.8464" y="15.608">(243, 128, 19)</text></g></g></g></svg><div class="toyplot-interactive"></div></div>


Finally, you can apply a limited subset of CSS styles within rich text:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    canvas.text(300, 100, "This is a <span style='fill:red;font-size:120%'>special</span> word.", style={"font-size":"16px"});



.. raw:: html

    <div align="center" class="toyplot" id="tbbb99587b2484831be8c126fa380fb9c"><svg class="toyplot-canvas-Canvas" height="200.0px" id="te53187d74f9c492bae453ed9794f30aa" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t6c3b5ddb759c4f5eb3d753bb7ce99aca"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-83.6672" y="4.9056">This is a </text><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:19.2;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-19.6512" y="4.9056">special</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="40.0992" y="4.9056"> word.</text></g></g></g></svg><div class="toyplot-interactive"></div></div>


Note that additional tags or style attributes currently aren't allowed
in rich-text. We expect that rich text capabilities will continue to
expand in the future.

Keep in mind that you can use rich text formatting anywhere that text is
displayed, including table cells, axis labels and tick labels. You can
also use rich text in format strings for tick locators - as an example,
the :class:`toyplot.locator.Log` locator uses the ``<sup>`` tag to
format tick labels for :ref:`log-scales`.

Caveats
~~~~~~~

Because all text in Toyplot is parsed as XHTML5, there are a few
important caveats to be aware of:

-  You must use ``<br/>`` or ``<br></br>`` to insert a line break ...
   ``<br>`` is not allowed.
-  You must escape ``<`` as ``&lt;`` and ``>`` as ``&gt;`` because
   otherwise they will be confused with XHTML5 tags.
-  You must escape ``&`` as ``&amp;`` because otherwise it will be
   confused with an XHTML5 entity.

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    canvas.text(300, 100, "3 &lt; 4 &amp; 5 &gt; 6", style={"font-size":"16px"});



.. raw:: html

    <div align="center" class="toyplot" id="td1e72b9560454564968508c9448898bb"><svg class="toyplot-canvas-Canvas" height="200.0px" id="teee98c6d9b5a4b4192621e11c32540fe" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="td2f0829475c74031b98be02a567c8bb1"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-45.816" y="4.088">3 &lt; 4 &amp; 5 &gt; 6</text></g></g></g></svg><div class="toyplot-interactive"></div></div>


Alignment
---------

By default, blocks of text in Toyplot are centered vertically and
horizontally around their *anchor*. To illustrate this, the following
figures display the anchor as a small black dot:

.. code:: python

    canvas = toyplot.Canvas(width=500, height=150)
    axes = canvas.cartesian(show=False)
    axes.text(0, 0, "Text!", style={"font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3);



.. raw:: html

    <div align="center" class="toyplot" id="t44ffa65f60fc4b4886b6ebb6b934ae1a"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t8851e7553548435d958faa0298436e10" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 150.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t6bb8c97c01f94c1b8b9bbb725eed374e"><clipPath id="t2c311e5982f54e0cb15b85515baea1f2"><rect height="70.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t2c311e5982f54e0cb15b85515baea1f2)"><g class="toyplot-mark-Text" id="t95d360a3b0c048dba06dc6d6c34d2a4b"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,75.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-26.676" y="6.132">Text!</text></g></g></g><g class="toyplot-mark-Scatterplot" id="td4c1afc2d50b4fb0b0ef04a28ce07668" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="75.0" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "td4c1afc2d50b4fb0b0ef04a28ce07668", "columns": [[0.0], [0.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t44ffa65f60fc4b4886b6ebb6b934ae1a .toyplot-mark-popup");
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


To control horizontal alignment, use the CSS ``text-anchor`` property to
alter the position of a line of text along its baseline, relative to the
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

    <div align="center" class="toyplot" id="t1152d177d24b41ee8fb8655bbc35376f"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t64ccd67825d84a798679df373357469a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tadd35b803dac4cda8401cdfb0ffe71a3"><clipPath id="t1fcafc9da4bb4612bc602596c6fbd4a0"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t1fcafc9da4bb4612bc602596c6fbd4a0)"><g class="toyplot-mark-AxisLines" id="tf18c88fc71074d31a9c1c559d664d513" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="250.0" x2="250.0" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t4970c9b4f0374eb498d4a55973f3055a"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,83.333333333333329)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-49.356" y="6.132">Centered</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tf62720bb1ea045208a50803f4e81e789" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="83.333333333333329" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="ta8e8ab4ea4704049ae7e82dae65208ce"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="6.132">Left Justified</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tb80c0c648fb74c23ae8d959e40fb38cb" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tc020b89b42b040eb8e6ece99af81f07b"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,216.66666666666669)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-150.72" y="6.132">Right Justified</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tda91a4456a5a45168ac11c8384f5c826" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="216.66666666666669" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tf62720bb1ea045208a50803f4e81e789", "columns": [[0.0], [1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tb80c0c648fb74c23ae8d959e40fb38cb", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tda91a4456a5a45168ac11c8384f5c826", "columns": [[0.0], [-1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t1152d177d24b41ee8fb8655bbc35376f .toyplot-mark-popup");
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
amounts, using the ``-toyplot-anchor-shift`` property (note that this is
non-standard CSS, provided by Toyplot for symmetry with the standard
``baseline-shift`` property which we will see below):

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

    <div align="center" class="toyplot" id="t6e74db624e6d4ca7bcb506c0c0c1f60a"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tabe4ac5a96c040aca33a717826605235" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t8214f5ff4e1d4136a18e98bff3353519"><clipPath id="t153f9867ab8640cea52f3451767352d2"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t153f9867ab8640cea52f3451767352d2)"><g class="toyplot-mark-AxisLines" id="ta67630b1edcf44ee91cc4f1c155bf074" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="250.0" x2="250.0" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t10ac35537855435f8a09fe679257df2e"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,75.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="6.132">Shifted +0px</text></g></g></g><g class="toyplot-mark-Scatterplot" id="td1f2823d77ac4c088d37791c08c663ea" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="75.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t2b249160423e45cb9836b673c70c5984"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,125.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="20.0" y="6.132">Shifted +20px</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t9a38667cd8e040a7a9aea3b7b9ab64ce" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="125.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t949983c00c6c427d8631f6ffb034989b"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,175.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="40.0" y="6.132">Shifted +40px</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tc37d8b8fcfa7491e96a74ecbd51a65b9" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="175.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t7de99de6749041c9bb818d26970c2982"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,225.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-20.0" y="6.132">Shifted -20px</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t425ede1d3a3a4130803599bd87bda162" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="225.0" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "td1f2823d77ac4c088d37791c08c663ea", "columns": [[0.0], [1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t9a38667cd8e040a7a9aea3b7b9ab64ce", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tc37d8b8fcfa7491e96a74ecbd51a65b9", "columns": [[0.0], [-1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t425ede1d3a3a4130803599bd87bda162", "columns": [[0.0], [-2.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t6e74db624e6d4ca7bcb506c0c0c1f60a .toyplot-mark-popup");
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


Vertically, you can use the ``-toyplot-vertical-align`` property to
alter the vertical position of a block of text relative to its anchor:

.. code:: python

    canvas = toyplot.Canvas(width=800, height=300)
    axes = canvas.cartesian(show=False)
    
    axes.hlines(0, color="lightgray")
    
    axes.text(-1, 0, "Top", style={"-toyplot-vertical-align":"top", "font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=3)
    
    axes.text(0, 0, "Middle", style={"-toyplot-vertical-align":"middle", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes.text(1, 0, "Bottom", style={"-toyplot-vertical-align":"bottom", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black", size=3)
    
    axes.text(2, 0, "1st Baseline", style={"-toyplot-vertical-align":"first-baseline", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black", size=3)
    
    axes.text(3, 0, "Last Baseline", style={"-toyplot-vertical-align":"last-baseline", "font-size":"24px"})
    axes.scatterplot(3, 0, color="black", size=3);
    




.. raw:: html

    <div align="center" class="toyplot" id="tb7c905da9e85449b9b6e886f06c8bcea"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t34dfbc7f01ce4f85bcc4a8119252da52" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 800.0 300.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t31137e3d590048cd8f9b7cbb60d22c70"><clipPath id="tdf463d7f8a07436eb38c5276a2a4a3fe"><rect height="220.0" width="720.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tdf463d7f8a07436eb38c5276a2a4a3fe)"><g class="toyplot-mark-AxisLines" id="t9006ddaa4d274904a6179512dc756d1b" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="750.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t5a5b11ceb69046d29aa0aafbdd927acd"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(68.257828820555261,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-20.676" y="20.532">Top</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t019c15c3a05b42a382f08f9beb75132b" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="68.257828820555261" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tf91d3b1cf65543bdabf3502644108612"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(222.79062257162749,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-35.34" y="6.132">Middle</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t0be4d015dc1b4d31ac58926aa972984a" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="222.79062257162749" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t6efcca33346a461588fab9672dc39e97"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(377.32341632269981,150.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-38.016" y="-8.268">Bottom</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tc8f24289fee441a19521052473bd5208" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="377.32341632269981" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="te95d6aa733da4be28d718d936d1190a3"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(531.85621007377199,150.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-65.364" y="0">1st Baseline</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tc0cadda844c9491e9a67b8d8d3445dc4" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="531.85621007377199" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tc405890376924446859dfd25fb264b78"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(686.38900382484428,150.0)"><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-72.036" y="0.0">Last Baseline</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tb583d2e2f66f449b845c256e5ec45574" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="686.38900382484428" cy="150.0" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t019c15c3a05b42a382f08f9beb75132b", "columns": [[-1.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t0be4d015dc1b4d31ac58926aa972984a", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tc8f24289fee441a19521052473bd5208", "columns": [[1.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tc0cadda844c9491e9a67b8d8d3445dc4", "columns": [[2.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tb583d2e2f66f449b845c256e5ec45574", "columns": [[3.0], [0.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tb7c905da9e85449b9b6e886f06c8bcea .toyplot-mark-popup");
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


Note that to see the difference between ``first-baseline`` and
``last-baseline`` requires a block of text with more than one line,
since they align the anchor with the first and last line's baselines
respectively:

.. code:: python

    canvas = toyplot.Canvas(width=800, height=300)
    axes = canvas.cartesian(show=False)
    
    axes.hlines(0, color="lightgray")
    
    axes.text(-1, 0, "Top<br/>Top", style={"-toyplot-vertical-align":"top", "font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=3)
    
    axes.text(0, 0, "Middle<br/>Middle", style={"-toyplot-vertical-align":"middle", "font-size":"24px"})
    axes.scatterplot(0, 0, color="black", size=3)
    
    axes.text(1, 0, "Bottom<br/>Bottom", style={"-toyplot-vertical-align":"bottom", "font-size":"24px"})
    axes.scatterplot(1, 0, color="black", size=3)
    
    axes.text(2, 0, "1st Baseline<br/>1st Baseline", style={"-toyplot-vertical-align":"first-baseline", "font-size":"24px"})
    axes.scatterplot(2, 0, color="black", size=3)
    
    axes.text(3, 0, "Last Baseline<br/>Last Baseline", style={"-toyplot-vertical-align":"last-baseline", "font-size":"24px"})
    axes.scatterplot(3, 0, color="black", size=3);



.. raw:: html

    <div align="center" class="toyplot" id="tcaa040667c6d4dfbab7f3576f33ff8d3"><svg class="toyplot-canvas-Canvas" height="300.0px" id="td0949c8015ac4bc095b68bb541d94f73" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 800.0 300.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t5ee058a484254930925756206e459080"><clipPath id="tdfa4be50634a4c35879cfa5d4a71573f"><rect height="220.0" width="720.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tdfa4be50634a4c35879cfa5d4a71573f)"><g class="toyplot-mark-AxisLines" id="tb072f585199647d9a6138772c0891742" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="750.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="te1f6182b727e4fa28f3806a4a4c4bd08"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(68.257828820555261,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-20.676" y="20.532">Top</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-20.676" y="49.332">Top</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t1cc3c91f1e674525a7d7c66158d86fb9" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="68.257828820555261" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t0ac165a3d62e4bceb68751166db80186"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(222.79062257162749,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-35.34" y="-8.268">Middle</text><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-35.34" y="20.532">Middle</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t20d27c7a2d2f4586b0204ca616a2dfbd" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="222.79062257162749" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tdb5f29488ed840eebd1a318cbf0632c1"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(377.32341632269981,150.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-38.016" y="-37.068">Bottom</text><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-38.016" y="-8.268">Bottom</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t326b6c25f6504c49a7badca3d92565c9" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="377.32341632269981" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="ta84283d3e5474ab08b272150fcffa661"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(531.85621007377199,150.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-65.364" y="0">1st Baseline</text><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-65.364" y="28.8">1st Baseline</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t172d4b7de5ba463aa674a4b3c0596c4a" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="531.85621007377199" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="te3b198af59af4890aedc698b8bfc7037"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(686.38900382484428,150.0)"><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-72.036" y="-28.8">Last Baseline</text><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-72.036" y="0.0">Last Baseline</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tcd9e5c5f082640f0a6ef577fb03ca028" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="686.38900382484428" cy="150.0" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t1cc3c91f1e674525a7d7c66158d86fb9", "columns": [[-1.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t20d27c7a2d2f4586b0204ca616a2dfbd", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t326b6c25f6504c49a7badca3d92565c9", "columns": [[1.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t172d4b7de5ba463aa674a4b3c0596c4a", "columns": [[2.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tcd9e5c5f082640f0a6ef577fb03ca028", "columns": [[3.0], [0.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tcaa040667c6d4dfbab7f3576f33ff8d3 .toyplot-mark-popup");
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


As you can see, ``-toyplot-vertical-align`` alters the alignment of an
entire block of text. If you wish to alter the vertical alignment of
text **within** the block, you can use the standard CSS
``alignment-baseline`` property:

.. code:: python

    text = """<span style="alignment-baseline:alphabetic">Alphabetic</span>"""
    text += """  <span style="alignment-baseline:middle">Middle</span>"""
    text += """  <span style="alignment-baseline:central">Central</span>"""
    text += """  <span style="alignment-baseline:hanging">Hanging</span>"""
    
    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.cartesian(show=False)
    
    axes.hlines(0, color="lightgray")
    
    axes.text(-1, 0, text, style={"font-size":"24px"})
    axes.scatterplot(-1, 0, color="black", size=3);



.. raw:: html

    <div align="center" class="toyplot" id="tfff51ff31d9d4de28bc522cc8d779ff5"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t56568a675e8f4fefb40cc46a83d722e7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t15f4df3217c24fbd96b9763954921ec4"><clipPath id="t99a0490fa5b84119a255a159fcd803b9"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t99a0490fa5b84119a255a159fcd803b9)"><g class="toyplot-mark-AxisLines" id="t76f358f4bc7546329d9ba6bceda4368b" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="550.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="tc547303f981441f4b5dd8bdf499a887c"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-194.748" y="-2.484">Alphabetic</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-82.692" y="-2.484">  </text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-69.348" y="3.5472">Middle</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="1.332" y="-2.484">  </text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="14.676" y="6.132">Central</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="92.028" y="-2.484">  </text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="105.372" y="14.748">Hanging</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t80eaba1f1c4e4504963dd06fce52e505" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="300.0" cy="150.0" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t80eaba1f1c4e4504963dd06fce52e505", "columns": [[-1.0], [0.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tfff51ff31d9d4de28bc522cc8d779ff5 .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="tb27b935c440241999694b7332f7426a0"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tb4c4d6b3ab7f4f97a734736ccc83d162" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 300.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tc50e20536d364ef08de3a7f6c59594dd"><clipPath id="t2a8cb3b6267d44769d650686adc4ea1e"><rect height="220.0" width="620.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t2a8cb3b6267d44769d650686adc4ea1e)"><g class="toyplot-mark-AxisLines" id="t23aebd9d89bb48b8aa0cd3fd40654079" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="650.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t462ea9e0fc374a8b904c91b7f6717050"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(101.68569285892843,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-62.028" y="30.132">Shift -100%</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tfb3d5f9b24a344c2bed5e8d267951a45" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="101.68569285892843" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="td2ab3f5f667e4872a94cfd945501f769"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(268.33847179401721,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-44.688" y="6.132">Shift 0%</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t4343b5c49bfb4d8cbcae767b1b5c07bd" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="268.33847179401721" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tc645525382774a798ec8e43afdd81cb2"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(434.9912507291059,150.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-51.36" y="-9.708">Shift 66%</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t125c0fb4bfa143238f3395e9b0d1f57d" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="434.9912507291059" cy="150.0" r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t384c8e9680874a2f91db3387df1a5b72"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(601.64402966419459,150.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-58.032" y="-17.868">Shift 100%</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t99e9ce63461d47d1bee3ac6f9bfab90f" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="601.64402966419459" cy="150.0" r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tfb3d5f9b24a344c2bed5e8d267951a45", "columns": [[-1.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t4343b5c49bfb4d8cbcae767b1b5c07bd", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t125c0fb4bfa143238f3395e9b0d1f57d", "columns": [[1.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t99e9ce63461d47d1bee3ac6f9bfab90f", "columns": [[2.0], [0.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tb27b935c440241999694b7332f7426a0 .toyplot-mark-popup");
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


Of course, you're free to combine all these style properties in any way
that you like.

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

    <div align="center" class="toyplot" id="t9ce2b0a15f9f4842b5ba9d776a7456d6"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t4560cffb8575463a97a59d3476095a81" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tcaca1469e1d445dd96de24feebe77098"><clipPath id="t2de50922aba741da9e2c91cde8497fb9"><rect height="220.0" width="86.66666666666666" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t2de50922aba741da9e2c91cde8497fb9)"><g class="toyplot-mark-AxisLines" id="t2cb47afe1a70471d973f8a6533f99ffc" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="83.333333333333329" x2="83.333333333333329" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="te64e9271a9bb462293f14868caa1816e"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(83.333333333333329,150.0)rotate(-45.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-27.024" y="6.132">a + b</text></g></g></g><g class="toyplot-mark-Scatterplot" id="te455ccf6a8d6410ea998bd426fb24237" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="83.333333333333329" cy="150.0" r="1.5"></circle></g></g></g></g><g transform="translate(83.33333333333333,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-22.946" y="-4.823">default</text></g></g><g class="toyplot-coordinates-Cartesian" id="t36310c69f7124ce1ba253c259b9ef4bd"><clipPath id="t1432c6f613044303a4b603b768dd1573"><rect height="220.0" width="86.66666666666666" x="206.66666666666666" y="40.0"></rect></clipPath><g clip-path="url(#t1432c6f613044303a4b603b768dd1573)"><g class="toyplot-mark-AxisLines" id="t8f15c35a98664859b6e6817d45d588c1" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="250.0" x2="250.0" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="te9a5748de11c4880ac720aebd5702fc8"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,150.0)rotate(-45.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-7.024" y="6.132">a + b</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tee663739b172400a929790ed5dc40230" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="250.0" cy="150.0" r="1.5"></circle></g></g></g></g><g transform="translate(250.0,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-68.439" y="-4.823">-toyplot-anchor-shift</text></g></g><g class="toyplot-coordinates-Cartesian" id="t851fbfc064604556a1ec399cb3f388dd"><clipPath id="t2308beef0ba348aa8de5c01a7bdf4b63"><rect height="220.0" width="86.66666666666669" x="373.3333333333333" y="40.0"></rect></clipPath><g clip-path="url(#t2308beef0ba348aa8de5c01a7bdf4b63)"><g class="toyplot-mark-AxisLines" id="t07de00d55e144b8cb52fb0e07b6465d3" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="416.66666666666663" x2="416.66666666666663" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t61bcc2e5f9a54649aff6cb908f4b59ef"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(416.66666666666663,150.0)rotate(-45.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-27.024" y="26.132">a + b</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t3891a7de2467407eb86f8e5a5cbea145" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><circle cx="416.66666666666663" cy="150.0" r="1.5"></circle></g></g></g></g><g transform="translate(416.66666666666663,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-45.122" y="-4.823">baseline-shift</text></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "te455ccf6a8d6410ea998bd426fb24237", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tee663739b172400a929790ed5dc40230", "columns": [[0.0], [0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t3891a7de2467407eb86f8e5a5cbea145", "columns": [[0.0], [0.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t9ce2b0a15f9f4842b5ba9d776a7456d6 .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="t9ae659adfb404c19af958ad0a7a6a5e6"><svg class="toyplot-canvas-Canvas" height="200.0px" id="t84a57caa11d949639f93df2d0d93451c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t81fc7703408a445ea472673fe9479b8e"><clipPath id="t8b46afc2787d445686feb0138a047140"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t8b46afc2787d445686feb0138a047140)" transform="translate(50.0,50.0)"></g><g class="toyplot-coordinates-Axis" id="te5a21ecef9a24690842685599bf04caf" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.4408920985e-16">-0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(500.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t7b6dfb39afe7493f9d1a30e8f6570cfc"><clipPath id="t27ce85c0cb7e42e884d7b64e055b74f9"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t27ce85c0cb7e42e884d7b64e055b74f9)" transform="translate(50.0,150.0)"></g><g class="toyplot-coordinates-Axis" id="tfea816ec0b0f4114a7fb869c8390d7d6" transform="translate(50.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t9ae659adfb404c19af958ad0a7a6a5e6";
                var axes = {"te5a21ecef9a24690842685599bf04caf": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tfea816ec0b0f4114a7fb869c8390d7d6": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
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

    <div align="center" class="toyplot" id="t3f3089a706c948a09371dc63873886b2"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tc2c74867699441f6b45bb6c0c0432332" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t727e8c2169244418aa9c9881355ef127"><clipPath id="t3a985ace74de4bb186655acf4d0d8cab"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t3a985ace74de4bb186655acf4d0d8cab)"></g><g class="toyplot-coordinates-Axis" id="t801a59baa5c24d40acfa2c3a2c844a96" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t2d67cb70cd01429d850bb413054d0f2b" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.4408920985e-16">-0.5</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t543a5f06fe10493bbe29bb42838fa58f"><clipPath id="t612d80c059194710890ff7eb69f8c57b"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t612d80c059194710890ff7eb69f8c57b)"></g><g class="toyplot-coordinates-Axis" id="tcfb51aefa55a4611a8490efa28e0f704" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t7ed144e74509472eb34af824b87291f9" transform="translate(550.0,250.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t3f3089a706c948a09371dc63873886b2";
                var axes = {"t2d67cb70cd01429d850bb413054d0f2b": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t7ed144e74509472eb34af824b87291f9": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t801a59baa5c24d40acfa2c3a2c844a96": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tcfb51aefa55a4611a8490efa28e0f704": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
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

    <div align="center" class="toyplot" id="td6e5de80d59c4f42a710dc6b109ead3d"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t9349cb76e2924025a5c37e40011866fd" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t479cfd75934e44c586150763e2e394f0"><clipPath id="t482a1db545cd49a7aa9a7e1e25409026"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t482a1db545cd49a7aa9a7e1e25409026)"></g><g class="toyplot-coordinates-Axis" id="tb2d306f395b34d549dfd4c681973095c" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t64c35b4613a740109480fb80ce61cf6e" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.4408920985e-16">-0.5</text></g><g transform="translate(100.0,-30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(200.0,-30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="15.0" y2="-22.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="30.0"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t259b71aa1f0c42e980105fa30d7f5875"><clipPath id="t21d3f49155b7467f92d57ee9cd831738"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t21d3f49155b7467f92d57ee9cd831738)"></g><g class="toyplot-coordinates-Axis" id="t0cb5653e087b4057be8ea0f7c087ec27" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t9d77fc7b056d47649294f2d086bda760" transform="translate(550.0,250.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-15.0" y2="22.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-30.0"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "td6e5de80d59c4f42a710dc6b109ead3d";
                var axes = {"t0cb5653e087b4057be8ea0f7c087ec27": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t64c35b4613a740109480fb80ce61cf6e": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t9d77fc7b056d47649294f2d086bda760": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tb2d306f395b34d549dfd4c681973095c": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
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

    <div align="center" class="toyplot" id="t1bd480960b964418852df26eba05697e"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t67bcd3c646354ead89738c324dc55767" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 400.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="te230464def2e4c70bf7e93d07b4aaad4"><clipPath id="td5271621e9b6415ba97e8b3d92d3649b"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#td5271621e9b6415ba97e8b3d92d3649b)" transform="translate(50.0,50.0)"></g><g class="toyplot-coordinates-Axis" id="t4ebb467df5574b4d81508a928b7dd9d7" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.4408920985e-16">-0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(500.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t01b03c6b240b45db85c51047cfd4f232"><clipPath id="t5f9ef035568f41169b29910d50c6c097"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t5f9ef035568f41169b29910d50c6c097)" transform="translate(50.0,150.0)"></g><g class="toyplot-coordinates-Axis" id="t3b83dc9f9bda4c88977ba59566cb45fc" transform="translate(50.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.784" y="0.0">-0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="0.0">0.0</text></g><g transform="translate(500.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="0.0">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="tb1b713e167e84a9d9ff051e66bc50fd7"><clipPath id="t502452ace45948318b2bbe594001c050"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t502452ace45948318b2bbe594001c050)" transform="translate(50.0,250.0)"></g><g class="toyplot-coordinates-Axis" id="ta3af931b4f2a436784196a735a156ac6" transform="translate(50.0,250.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="tc926f5b24ce842abb6940f0e620ee697"><clipPath id="tf7e5b9bb9a02452fb08bec5903959f26"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#tf7e5b9bb9a02452fb08bec5903959f26)" transform="translate(50.0,350.0)"></g><g class="toyplot-coordinates-Axis" id="ta4c680026cdf400b80781c9a24ceef9a" transform="translate(50.0,350.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.784" y="13.688">-0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="13.688">0.0</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="13.688">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t1bd480960b964418852df26eba05697e";
                var axes = {"t3b83dc9f9bda4c88977ba59566cb45fc": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "t4ebb467df5574b4d81508a928b7dd9d7": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "ta3af931b4f2a436784196a735a156ac6": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "ta4c680026cdf400b80781c9a24ceef9a": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
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

    <div align="center" class="toyplot" id="t1214b4eaffc84ece966413e40fb33409"><svg class="toyplot-canvas-Canvas" height="600px" id="t3805580cd25e40d4ab7a4b591d2ae91e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t06f30f2cfe054692848acaf80557d156"><clipPath id="tbda42b196dc94127978fc6a37a011eac"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#tbda42b196dc94127978fc6a37a011eac)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="tf9da9566ea2d415294c1267218f8850d"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tbe5a64fdefa247fe9b72ff6b47920115" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tbe5a64fdefa247fe9b72ff6b47920115);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="tb6667be11cec492f857e4ddf923bf7f6" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="240.0" x2="240.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><g transform="translate(0.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="2.555">0.0</text></g><g transform="translate(240.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="2.555">0.5</text></g><g transform="translate(480.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="2.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t1214b4eaffc84ece966413e40fb33409";
                var axes = {"tb6667be11cec492f857e4ddf923bf7f6": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]};
    
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
    labels = ["%.4f<br/><small>%s</small>" % (value, format_color(colormap.color(value))) for value in values]
    locator = toyplot.locator.Explicit(values, labels)

.. code:: python

    canvas = toyplot.Canvas()
    numberline = canvas.color_scale(x1="50%", x2="50%", y1="-10%", y2="10%", colormap=colormap)
    numberline.axis.ticks.show = True
    numberline.axis.ticks.labels.angle=-90
    
    numberline.axis.ticks.locator = locator
    numberline.axis.ticks.labels.style = {"font-size":"16px"}



.. raw:: html

    <div align="center" class="toyplot" id="t84595b2467b9468b86f909dc8b6035e4"><svg class="toyplot-canvas-Canvas" height="600px" id="tc159f17d50c949bb8487d319b32ff484" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t1624ff32bc634598bc134bb4a473efba"><clipPath id="t78233ded1c234bb88f1db9fb93cdf64d"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t78233ded1c234bb88f1db9fb93cdf64d)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t2250d29af89f4540a39898b69725ea37"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t23c55df352224ba0bf3dd51b0cf8a176" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t23c55df352224ba0bf3dd51b0cf8a176);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t248880f09bc941399803aaa31ff0ca70" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="160.0" x2="160.0" y1="3" y2="-3"></line><line style="" x1="320.0" x2="320.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><g transform="translate(0.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.592">0.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.608">(0.02, 0.19, 0.38)</text></g><g transform="translate(160.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.592">0.3333</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.608">(0.65, 0.81, 0.89)</text></g><g transform="translate(320.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.592">0.6667</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.608">(0.97, 0.72, 0.60)</text></g><g transform="translate(480.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.592">1.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.608">(0.40, 0.00, 0.12)</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "t84595b2467b9468b86f909dc8b6035e4";
                var axes = {"t248880f09bc941399803aaa31ff0ca70": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


We might choose to override the defaults to center each line of text
within the label:

.. code:: python

    canvas = toyplot.Canvas()
    numberline = canvas.color_scale(x1="50%", x2="50%", y1="-10%", y2="10%", colormap=colormap)
    numberline.axis.ticks.labels.angle=-90
    numberline.axis.ticks.show = True
    numberline.axis.ticks.locator = locator
    numberline.axis.ticks.labels.style = {"font-size":"16px"}
    
    numberline.axis.ticks.labels.style = {"text-anchor":"middle"}
    numberline.axis.ticks.labels.offset = 60



.. raw:: html

    <div align="center" class="toyplot" id="tdbc61c30db464611a8a3d652eff7dcef"><svg class="toyplot-canvas-Canvas" height="600px" id="tf46cea42d8ea44eeb80e3fe3a281bf05" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="taf871b60bf7b46ac88f2c90c16c82f5f"><clipPath id="tcecf7fbc8e5743af97605c4de1ea35e2"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#tcecf7fbc8e5743af97605c4de1ea35e2)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="tf5d2b57ee17643e788566acd4caadd51"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tc36d6e859fc8428ca31970f8e6ecf4ad" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tc36d6e859fc8428ca31970f8e6ecf4ad);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t2817c561650a430096f7b4baa68c2f9f" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="160.0" x2="160.0" y1="3" y2="-3"></line><line style="" x1="320.0" x2="320.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><g transform="translate(0.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464" y="-3.592">0.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.7424" y="15.608">(0.02, 0.19, 0.38)</text></g><g transform="translate(160.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464" y="-3.592">0.3333</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.7424" y="15.608">(0.65, 0.81, 0.89)</text></g><g transform="translate(320.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464" y="-3.592">0.6667</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.7424" y="15.608">(0.97, 0.72, 0.60)</text></g><g transform="translate(480.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464" y="-3.592">1.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.7424" y="15.608">(0.40, 0.00, 0.12)</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-30.0" y2="45.0"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-60.0"></text></g></g></g></svg><div class="toyplot-interactive"><script>
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
    
                var root_id = "tdbc61c30db464611a8a3d652eff7dcef";
                var axes = {"t2817c561650a430096f7b4baa68c2f9f": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


