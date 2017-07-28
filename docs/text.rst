
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

    <div class="toyplot" id="ted4c29dedbcf4fa58998a79c0fa3eaab" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="150.0px" id="tf76713af794c4af9a71079a6126c40fb" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="te4a752282d4d4443982f9368cd14aa85"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-42.872" y="8.176">100</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:22.4px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="10.504" y="1.456">-53</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "H<sub>2</sub>O", style={"font-size":"32px"});



.. raw:: html

    <div class="toyplot" id="t70c2a55f166641ed83e3c81bc9e08ee8" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t426a989fe1a54285b8f3d9a9a02edcb6" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t7938934a2fe54d229099e50ace0f418e"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-30.2272" y="8.176">H</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:22.4px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-7.1232" y="12.656">2</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="5.3312" y="8.176">O</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


There are a variety of tags to alter the inline appearance of text:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(
        300,
        100,
        "normal <b>bold</b> <i>italic</i> <strong>strong</strong> <em>emphasis</em> <small>small</small> <code>code</code>",
        style={"font-size":"24px"});



.. raw:: html

    <div class="toyplot" id="t9ab6c7865c7449ee902f792cde09e88b" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="150.0px" id="taa10750b5d0c41a88112168171d171a8" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t0c34072b88ca4ab6a9fafdc2a23b1275"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-245.8968" y="6.132">normal </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-165.8808" y="6.132">bold</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-115.2168" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-style:italic;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-108.5448" y="6.132">italic</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-60.5448" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-53.8728" y="6.132">strong</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="20.7912" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-style:italic;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="27.4632" y="6.132">emphasis</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="130.1592" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:19.2px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="136.8312" y="6.132">small</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="181.6248" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="188.2968" y="6.132">code</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


And these tags can be nested to combine effects:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(
        300,
        100,
        "foo <b>bar <i>baz <code>blah</code></i></b>",
        style={"font-size":"32px"},
    );



.. raw:: html

    <div class="toyplot" id="t6a52653391824d3598705275c57520f2" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="150.0px" id="tca959828ede0418d822b3cc333bf9742" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="ta48da266da8f4ad7bdff23142123c4af"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-125.552" y="8.176">foo </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-72.176" y="8.176">bar </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-style:italic;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-13.488" y="8.176">baz </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:32.0px;font-style:italic;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="48.752" y="8.176">blah</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


You can insert line breaks into your text using the ``<br/>`` tag:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    canvas.text(
        300,
        100,
        "0.567832<br/><small>(243, 128, 19)</small>",
        style={"font-size":"16px"},
    );



.. raw:: html

    <div class="toyplot" id="t522a56f1100f4ff19761d08917104b4e" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="200.0px" id="tfa076f8ce05a47748da88c32003f699a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t5e599054dcd044b4bc52461a7efcbc72"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-33.36" y="-3.592">0.567832</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-39.8464" y="15.608">(243, 128, 19)</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


And you can apply a limited subset of CSS styles within rich text:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    canvas.text(
        300,
        100,
        "This is a <span style='fill:red;font-size:120%'>special</span> word.",
        style={"font-size":"16px"},
    );



.. raw:: html

    <div class="toyplot" id="t8a53bf56139d4bf08dfc02d4878eb19c" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="200.0px" id="tbfd0977deb0f4a25ab1fccd37f2826e2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="td1b3577148e4470f96d8d5fba5e22e25"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-83.6672" y="4.9056">This is a </text><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:19.2px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-19.6512" y="4.9056">special</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="40.0992" y="4.9056"> word.</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


Finally, you can embed hyperlinks in rich text, using the <a> tag:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    canvas.text(
        300,
        100,
        "See <a style='fill: steelblue' href='http://toyplot.readthedocs.org'>Toyplot</a> for details.",
        style={"font-size":"16px"},
    );



.. raw:: html

    <div class="toyplot" id="tcc0b62918c7c410faa9976e2ed1a2b63" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="200.0px" id="t1701f0569a43465cb4dfc408a094f26b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="td7434904caf5413abaa5c543a12a44c0"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-81.816" y="4.088">See </text><a xlink:href="http://toyplot.readthedocs.org"><text style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-48.904" y="4.088">Toyplot</text></a><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="3.56" y="4.088"> for details.</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


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

    <div class="toyplot" id="t196d48de0357445ea9f61ee8914215d8" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="200.0px" id="t9e8b4360501649f1b5d8694cd930494c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t7b1cb2bd34d74f6d925b20afd130681c"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-45.816" y="4.088">3 &lt; 4 &amp; 5 &gt; 6</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


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

    <div class="toyplot" id="t9888cbd7695d44df833fdda18a21e1b2" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t3ceff4a46d8a436cb37165547e11183d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 150.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tbe4edcbaa6df4ad2b9568d8a2b66ff77"><clipPath id="tac99e349164b468bb0bc2fc18b9f69c8"><rect height="70.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tac99e349164b468bb0bc2fc18b9f69c8)"><g class="toyplot-mark-Text" id="t7204c2aee3454f4eb83851fc31c8c7fb"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,75.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-26.676" y="6.132">Text!</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t850a9ecf627f446db4a10e58a03156f1"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 75.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t9888cbd7695d44df833fdda18a21e1b2";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t3ceff4a46d8a436cb37165547e11183d";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t850a9ecf627f446db4a10e58a03156f1","data","scatterplot",["x", "y0"],[[0.0], [0.0]],"toyplot");
    })();</script></div></div>


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

    <div class="toyplot" id="tca1e84c28b9b4c2bbc04da8e5af3f9d4" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="td0cf19e210b94381a30c67802780fd59" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t485bb978f13f4d5c9657d35ab3cbc8fc"><clipPath id="tbd56384dbb5d47d1aecfd00788375d98"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tbd56384dbb5d47d1aecfd00788375d98)"><g class="toyplot-mark-AxisLines" id="te41e2c1a95da4dac93c23ffda7bc2389" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="250.0" x2="250.0" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="td5c1e71966db4029be530c6d7c995faf"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,83.333333333333329)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-49.356" y="6.132">Centered</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t0fbfd992dcac4334a0862a0abe9dc433"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 83.333333333333329)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t84e20d8e95bd44f7bfe7018ab87c960b"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="6.132">Left Justified</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t4e1f26e72cab489eb88d35a7aa8152e1"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tb2d16d71f7bf4b58ad378158d4d0b711"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,216.66666666666669)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-150.72" y="6.132">Right Justified</text></g></g></g><g class="toyplot-mark-Scatterplot" id="td6d3b5814cc54aa3987efd40c0486594"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 216.66666666666669)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tca1e84c28b9b4c2bbc04da8e5af3f9d4";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "td0cf19e210b94381a30c67802780fd59";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t0fbfd992dcac4334a0862a0abe9dc433","data","scatterplot",["x", "y0"],[[0.0], [1.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t4e1f26e72cab489eb88d35a7aa8152e1","data","scatterplot",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"td6d3b5814cc54aa3987efd40c0486594","data","scatterplot",["x", "y0"],[[0.0], [-1.0]],"toyplot");
    })();</script></div></div>


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

    <div class="toyplot" id="tabc3415b392246f0b7ffa7f1e48429bc" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t59314cff084946369ce1cf93fe1c6cda" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="te9881a9ba4fb4f1c96a4a1e51a62b1c3"><clipPath id="t0c0c727fb4154b2f8bfe850be5ba6c70"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t0c0c727fb4154b2f8bfe850be5ba6c70)"><g class="toyplot-mark-AxisLines" id="tad15ccd7729643b8b8d640ec02e9d01c" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="250.0" x2="250.0" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="te421c36cd729432b8a6d22623a22d585"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,75.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="6.132">Shifted +0px</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t744853ed8d6f48a3a38bc498c3233a9c"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 75.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t7eec425bb80a430b9b9ac52532d179dc"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,125.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="20.0" y="6.132">Shifted +20px</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t8c405405e73342a89897efd6856e38d3"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 125.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t55553c99c1b64f05bb933af4f461ee29"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,175.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="40.0" y="6.132">Shifted +40px</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tcabbb088f4da4b16bb616674a5ace8d2"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 175.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t223bea04c04c4ec2a0b451231a3e8c29"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,225.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-20.0" y="6.132">Shifted -20px</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t54b13b3f8a4646f4990d44f7b6902da1"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 225.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tabc3415b392246f0b7ffa7f1e48429bc";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t59314cff084946369ce1cf93fe1c6cda";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t744853ed8d6f48a3a38bc498c3233a9c","data","scatterplot",["x", "y0"],[[0.0], [1.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t8c405405e73342a89897efd6856e38d3","data","scatterplot",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tcabbb088f4da4b16bb616674a5ace8d2","data","scatterplot",["x", "y0"],[[0.0], [-1.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t54b13b3f8a4646f4990d44f7b6902da1","data","scatterplot",["x", "y0"],[[0.0], [-2.0]],"toyplot");
    })();</script></div></div>


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

    <div class="toyplot" id="td3fec7292f9541ea85077d5f676d772b" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t6b67f4de5af74033b94299043e4d5cb5" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 800.0 300.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t8ba1c2c9bab94e8fb23427ea7749392d"><clipPath id="t23eea8616142420fabff3cd100a7e42b"><rect height="220.0" width="720.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t23eea8616142420fabff3cd100a7e42b)"><g class="toyplot-mark-AxisLines" id="t98a275243eff496d9a50559317a5552d" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="750.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="tc951440cb1904b41a7f8ae6433067e2f"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(68.257828820555261,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-20.676" y="20.532">Top</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t363e68cd755e416c8c2c7d82e183b386"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(68.257828820555261, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t64c6446fb0984a8697eeff7ceed60561"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(222.79062257162749,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-35.34" y="6.132">Middle</text></g></g></g><g class="toyplot-mark-Scatterplot" id="teab18f6866554e07afda59d5336f15a3"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(222.79062257162749, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t98a186e7d5414645a86bb01e086a7a98"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(377.32341632269981,150.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-38.016" y="-8.268">Bottom</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t9a82201875424802848478a5acd023c1"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(377.32341632269981, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t11415b5f65f847fe968e7bfc69953adb"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(531.85621007377199,150.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-65.364" y="0">1st Baseline</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t6eca5c4a051b44b2ba17721b36efd8d3"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(531.85621007377199, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t65161343bb474440bb1745da2db5c907"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(686.38900382484428,150.0)"><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-72.036" y="0.0">Last Baseline</text></g></g></g><g class="toyplot-mark-Scatterplot" id="ta74d1c775b43482a917470fe3dec6384"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(686.38900382484428, 150.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "td3fec7292f9541ea85077d5f676d772b";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t6b67f4de5af74033b94299043e4d5cb5";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t363e68cd755e416c8c2c7d82e183b386","data","scatterplot",["x", "y0"],[[-1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"teab18f6866554e07afda59d5336f15a3","data","scatterplot",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t9a82201875424802848478a5acd023c1","data","scatterplot",["x", "y0"],[[1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t6eca5c4a051b44b2ba17721b36efd8d3","data","scatterplot",["x", "y0"],[[2.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"ta74d1c775b43482a917470fe3dec6384","data","scatterplot",["x", "y0"],[[3.0], [0.0]],"toyplot");
    })();</script></div></div>


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

    <div class="toyplot" id="tdc6e8500dbd14a7b8508460c2aa3f1b5" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t88a8f6d4453a4584bcd447a9b728dc78" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 800.0 300.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tca07be0a1d8948389bb71fbfa24826d5"><clipPath id="t5d060f94fc954138a48c73a30af528d1"><rect height="220.0" width="720.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t5d060f94fc954138a48c73a30af528d1)"><g class="toyplot-mark-AxisLines" id="tf1462a23363c420daf3e2f6fbab62725" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="750.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t5f6915f5ca354e2881ae2d9f91d95239"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(68.257828820555261,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-20.676" y="20.532">Top</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-20.676" y="49.332">Top</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tc5ddd78ea7d54f7b81ec9f493a3cc167"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(68.257828820555261, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t54ef2019e3ae466fba0ca749cdfda261"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(222.79062257162749,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-35.34" y="-8.268">Middle</text><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-35.34" y="20.532">Middle</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t9bad22259456451fae573477c71e4e32"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(222.79062257162749, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="td7d50d16cad245f9bf43be27b8c05394"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(377.32341632269981,150.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-38.016" y="-37.068">Bottom</text><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-38.016" y="-8.268">Bottom</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tac967776cba7491a832dc9e3ce4ae01e"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(377.32341632269981, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t929a9d93c2cf436fa3ee30b243e9364f"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(531.85621007377199,150.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-65.364" y="0">1st Baseline</text><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-65.364" y="28.8">1st Baseline</text></g></g></g><g class="toyplot-mark-Scatterplot" id="tec40e454eb884ac19b0894226ad6537c"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(531.85621007377199, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t547002ff6b1c4d10a72339a38ca31ddc"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(686.38900382484428,150.0)"><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-72.036" y="-28.8">Last Baseline</text><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-72.036" y="0.0">Last Baseline</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t57b14b90d27a4a6190b64d216c0e8cc0"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(686.38900382484428, 150.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tdc6e8500dbd14a7b8508460c2aa3f1b5";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t88a8f6d4453a4584bcd447a9b728dc78";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tc5ddd78ea7d54f7b81ec9f493a3cc167","data","scatterplot",["x", "y0"],[[-1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t9bad22259456451fae573477c71e4e32","data","scatterplot",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tac967776cba7491a832dc9e3ce4ae01e","data","scatterplot",["x", "y0"],[[1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tec40e454eb884ac19b0894226ad6537c","data","scatterplot",["x", "y0"],[[2.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t57b14b90d27a4a6190b64d216c0e8cc0","data","scatterplot",["x", "y0"],[[3.0], [0.0]],"toyplot");
    })();</script></div></div>


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

    <div class="toyplot" id="tb777b8b71f374454a587db788fe27d47" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t7974da63e78e4025a83bcc68ff70d2db" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="td6dad39df1034659b9683238387ad5b2"><clipPath id="tddb3d357581e49a99ffd7a02aec458c7"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tddb3d357581e49a99ffd7a02aec458c7)"><g class="toyplot-mark-AxisLines" id="t5cfbb83165b34310acf2003451223e43" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="550.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t951944db9fb545bf9a7044526387cd86"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-194.748" y="-2.484">Alphabetic</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-82.692" y="-2.484">  </text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-69.348" y="3.5472">Middle</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="1.332" y="-2.484">  </text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="14.676" y="6.132">Central</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="92.028" y="-2.484">  </text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="105.372" y="14.748">Hanging</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t796f906f47c14564af638b795c2e1122"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(300.0, 150.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tb777b8b71f374454a587db788fe27d47";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t7974da63e78e4025a83bcc68ff70d2db";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t796f906f47c14564af638b795c2e1122","data","scatterplot",["x", "y0"],[[-1.0], [0.0]],"toyplot");
    })();</script></div></div>


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

    <div class="toyplot" id="t7bc6dde8981d433f88227afffbbbd88f" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tcfdb22f021b445bd9197a425b09ca9a7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 300.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t70337e4b334045a89e72d829ae1727a0"><clipPath id="t5220ea190bdf48729bedea913b4e5380"><rect height="220.0" width="620.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t5220ea190bdf48729bedea913b4e5380)"><g class="toyplot-mark-AxisLines" id="tbeed7eb279e64df3b0b9a01f796ef424" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="650.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="td068200702e546d9978f592a8474f6ef"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(101.68569285892843,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-62.028" y="30.132">Shift -100%</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t2988fefb5ab441258453a6e3d579f152"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(101.68569285892843, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tf1446f71d644418fb566b2662315bad3"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(268.33847179401721,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-44.688" y="6.132">Shift 0%</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t4e106ba5b7b0474395f7cbb0eb1fce3c"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(268.33847179401721, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tb52ca7aecd3f40f99b441f17d93f868f"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(434.9912507291059,150.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-51.36" y="-9.708">Shift 66%</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t0990995e64fd4f049eff92046d3bb5c2"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(434.9912507291059, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="ta420f7cb78d74c5aaa70ff50eb7b409e"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(601.64402966419459,150.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-58.032" y="-17.868">Shift 100%</text></g></g></g><g class="toyplot-mark-Scatterplot" id="ted8a4a00dac146849461670fe584408b"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(601.64402966419459, 150.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t7bc6dde8981d433f88227afffbbbd88f";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tcfdb22f021b445bd9197a425b09ca9a7";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t2988fefb5ab441258453a6e3d579f152","data","scatterplot",["x", "y0"],[[-1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t4e106ba5b7b0474395f7cbb0eb1fce3c","data","scatterplot",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t0990995e64fd4f049eff92046d3bb5c2","data","scatterplot",["x", "y0"],[[1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"ted8a4a00dac146849461670fe584408b","data","scatterplot",["x", "y0"],[[2.0], [0.0]],"toyplot");
    })();</script></div></div>


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

    <div class="toyplot" id="ta5c5b6387eef455f95d194437002cf4b" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tf271dd284bca4c5f845ab59059d34ebf" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t9d1a437b89094878b537be3e55f99e6b"><clipPath id="tf33b92db58b34a48a7b7e795da9a1c2d"><rect height="220.0" width="86.66666666666666" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tf33b92db58b34a48a7b7e795da9a1c2d)"><g class="toyplot-mark-AxisLines" id="tae1b50a59bc34015941bb266bddc87e4" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="83.333333333333329" x2="83.333333333333329" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t3bf2dcd0d7d74c80afd0d5bd3eb9d02c"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(83.333333333333329,150.0)rotate(-45.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-27.024" y="6.132">a + b</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t72130e7b0e1e44d6b6014fac43985962"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(83.333333333333329, 150.0)"><circle r="1.5"></circle></g></g></g></g><g transform="translate(83.33333333333333,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-22.946" y="-4.823">default</text></g></g><g class="toyplot-coordinates-Cartesian" id="t367f2fd3533c4c13954c96e579c215ae"><clipPath id="tb34b054664ff427a82ce6b99c6c51d87"><rect height="220.0" width="86.66666666666666" x="206.66666666666666" y="40.0"></rect></clipPath><g clip-path="url(#tb34b054664ff427a82ce6b99c6c51d87)"><g class="toyplot-mark-AxisLines" id="t08b0d4b7b0b3448394e236b501ac661a" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="250.0" x2="250.0" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="td61912148196428fb66a91c5576fe6bb"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,150.0)rotate(-45.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-7.024" y="6.132">a + b</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t722c25c5a0694a93a5cf78b63aa67522"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 150.0)"><circle r="1.5"></circle></g></g></g></g><g transform="translate(250.0,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-68.439" y="-4.823">-toyplot-anchor-shift</text></g></g><g class="toyplot-coordinates-Cartesian" id="t75fe8212dde7481bb68ec8c44516a950"><clipPath id="t600cb3f3912340ccb69b3f9d390c2da2"><rect height="220.0" width="86.66666666666669" x="373.3333333333333" y="40.0"></rect></clipPath><g clip-path="url(#t600cb3f3912340ccb69b3f9d390c2da2)"><g class="toyplot-mark-AxisLines" id="tff5f66aafaa24b73a236383b1c4ec8ef" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="416.66666666666663" x2="416.66666666666663" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t118023652c824bffa870c3f731fe34b8"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(416.66666666666663,150.0)rotate(-45.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-27.024" y="26.132">a + b</text></g></g></g><g class="toyplot-mark-Scatterplot" id="t3a36962f72d64d00bf5a67344443913f"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(416.66666666666663, 150.0)"><circle r="1.5"></circle></g></g></g></g><g transform="translate(416.66666666666663,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-45.122" y="-4.823">baseline-shift</text></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "ta5c5b6387eef455f95d194437002cf4b";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tf271dd284bca4c5f845ab59059d34ebf";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t72130e7b0e1e44d6b6014fac43985962","data","scatterplot",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t722c25c5a0694a93a5cf78b63aa67522","data","scatterplot",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t3a36962f72d64d00bf5a67344443913f","data","scatterplot",["x", "y0"],[[0.0], [0.0]],"toyplot");
    })();</script></div></div>


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

    <div class="toyplot" id="tbf338aef60ce43aba353cd6020b3609c" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="200.0px" id="td84de3d3dbb04c8cb4afc8f25bf1292e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t9bf989e69d264069a61929937a25b8f6"><clipPath id="tccbf044e12f64f83a2f0f4746cb6a7fe"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#tccbf044e12f64f83a2f0f4746cb6a7fe)" transform="translate(50.0,50.0)"></g><g class="toyplot-coordinates-Axis" id="tf21efb965c5941f6bcbd2b92af7081d7" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.4408920985e-16">-0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(500.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t07f8c810684f450d9e569eb9555e8494"><clipPath id="ta5ff60c5243e46e7b96a2f5235a89e3a"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#ta5ff60c5243e46e7b96a2f5235a89e3a)" transform="translate(50.0,150.0)"></g><g class="toyplot-coordinates-Axis" id="t8316748c4ec64a73ad4a6ff71c21d5bc" transform="translate(50.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "td84de3d3dbb04c8cb4afc8f25bf1292e";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
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
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tf21efb965c5941f6bcbd2b92af7081d7",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t8316748c4ec64a73ad4a6ff71c21d5bc",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


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

    <div class="toyplot" id="tb5e8aae93e924b2c8ea5c4d090abf99c" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tb0da3c54711a46259f2b9ab772529fb2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t5ce53f06e73e4b98a65cc5f9451a05d9"><clipPath id="t794b4964eaef47cba6da1034e4da280f"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t794b4964eaef47cba6da1034e4da280f)"></g><g class="toyplot-coordinates-Axis" id="t4ad11fb8ac2443eda4206ff76801f071" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="te687cc21de4347dda1899c15ea444627" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.4408920985e-16">-0.5</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="tfa36db47447f463db4a045b7ef25e1dc"><clipPath id="tba1f9cf4ab8f486a97bf51b160c9e384"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#tba1f9cf4ab8f486a97bf51b160c9e384)"></g><g class="toyplot-coordinates-Axis" id="t9f576735648a4adbaad8b04c21e991fd" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t00a1b27424084b75b1ea8d73b2899834" transform="translate(550.0,250.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "tb0da3c54711a46259f2b9ab772529fb2";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
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
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t4ad11fb8ac2443eda4206ff76801f071",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"te687cc21de4347dda1899c15ea444627",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t9f576735648a4adbaad8b04c21e991fd",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t00a1b27424084b75b1ea8d73b2899834",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


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

    <div class="toyplot" id="t431de1171ef44d4896c33921c185610f" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t1fa8db41f11542c890e457fe81b9b9cb" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t76704c483f2b4e6280a4f32137604426"><clipPath id="t85b4c8816257482bb690d90ea965afbf"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t85b4c8816257482bb690d90ea965afbf)"></g><g class="toyplot-coordinates-Axis" id="td1983ff4fada4e1f8a5e7e0c7497049f" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t46b95d8925034e2a8a373b95041317de" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.4408920985e-16">-0.5</text></g><g transform="translate(100.0,-30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(200.0,-30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="15.0" y2="-22.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="30.0"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="td516a7a6fc894afd90a3844d5743a41e"><clipPath id="t5044269f18e841358b3c7b16c122bae5"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t5044269f18e841358b3c7b16c122bae5)"></g><g class="toyplot-coordinates-Axis" id="tf328fae62dc5413bb290f8ca6a9c0c9c" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t6a69937a634342c49b939a4941a7fc36" transform="translate(550.0,250.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-15.0" y2="22.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-30.0"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t1fa8db41f11542c890e457fe81b9b9cb";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
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
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"td1983ff4fada4e1f8a5e7e0c7497049f",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t46b95d8925034e2a8a373b95041317de",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tf328fae62dc5413bb290f8ca6a9c0c9c",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t6a69937a634342c49b939a4941a7fc36",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


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

    <div class="toyplot" id="tde49553e9610478b854cb209a8c7f145" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t64aa078cb79942deb9abe9efbee85533" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 400.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t95208efc563e4296a71497f0970e4938"><clipPath id="ta31abcbd9a79499b8d6c53c7a1b6ad6d"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#ta31abcbd9a79499b8d6c53c7a1b6ad6d)" transform="translate(50.0,50.0)"></g><g class="toyplot-coordinates-Axis" id="t097be5c3a7f24fb09a94f9c27e0f2928" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.4408920985e-16">-0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(500.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t5bfcf28360c44bbeb92d9cabc6be2950"><clipPath id="tb4c357372d4a4f00ac85f231a512cd0d"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#tb4c357372d4a4f00ac85f231a512cd0d)" transform="translate(50.0,150.0)"></g><g class="toyplot-coordinates-Axis" id="t646206e1daca4db0b0cf5c7e59443c1a" transform="translate(50.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.784" y="0.0">-0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="0.0">0.0</text></g><g transform="translate(500.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="0.0">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="td545786690494c0aaaa100be1fd20b35"><clipPath id="ted7d614c58a84e9fa6790914de288dd8"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#ted7d614c58a84e9fa6790914de288dd8)" transform="translate(50.0,250.0)"></g><g class="toyplot-coordinates-Axis" id="t777b0e5368204fbb8a92b6db31b8a0f4" transform="translate(50.0,250.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t86f9aa3e2af042748f90f0ea8b33d831"><clipPath id="tc63f652d2aef4f26a19c4d9b7843987d"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#tc63f652d2aef4f26a19c4d9b7843987d)" transform="translate(50.0,350.0)"></g><g class="toyplot-coordinates-Axis" id="t9378052466a54a8ba7e08bbaffdae61c" transform="translate(50.0,350.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.784" y="13.688">-0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="13.688">0.0</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="13.688">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t64aa078cb79942deb9abe9efbee85533";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
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
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t097be5c3a7f24fb09a94f9c27e0f2928",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t646206e1daca4db0b0cf5c7e59443c1a",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t777b0e5368204fbb8a92b6db31b8a0f4",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t9378052466a54a8ba7e08bbaffdae61c",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


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

    <div class="toyplot" id="tb97ba0c44f024b0abb8104764da634dd" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t147680b941634ecaba522e837875e6c1" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t4faf8f243d8a4d5995d90ae00a58a0c6"><clipPath id="t56a8429830c845b493c70a272369ef60"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t56a8429830c845b493c70a272369ef60)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="tcf22bc39174b495cb8dadd5c492b7eb2"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tfbaee0e58e544ff18d8102bc21d821f9" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tfbaee0e58e544ff18d8102bc21d821f9);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t65f33d7586bf460893c9ac541e17997c" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="240.0" x2="240.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><g transform="translate(0.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="2.555">0.0</text></g><g transform="translate(240.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="2.555">0.5</text></g><g transform="translate(480.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="2.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t147680b941634ecaba522e837875e6c1";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
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
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t65f33d7586bf460893c9ac541e17997c",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


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

    <div class="toyplot" id="ta3f5bb64551e4a7ca9ec81e5a294a4a5" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t6dae9264beb84f2aa96242a32f58d590" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="tc95772936c0b4f03b68950a0a0bdcf96"><clipPath id="t53437f0ca37e48ef918ea2a4d97a9b4a"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t53437f0ca37e48ef918ea2a4d97a9b4a)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t133aaaf99bfb4df2a321359549681115"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t22f13108479f4795a716e3b34e70bd9b" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t22f13108479f4795a716e3b34e70bd9b);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t2ee38f95f10949c086007aeadcee0214" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="160.0" x2="160.0" y1="3" y2="-3"></line><line style="" x1="320.0" x2="320.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><g transform="translate(0.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.592">0.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.608">(0.02, 0.19, 0.38)</text></g><g transform="translate(160.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.592">0.3333</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.608">(0.65, 0.81, 0.89)</text></g><g transform="translate(320.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.592">0.6667</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.608">(0.97, 0.72, 0.60)</text></g><g transform="translate(480.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.592">1.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.608">(0.40, 0.00, 0.12)</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t6dae9264beb84f2aa96242a32f58d590";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
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
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t2ee38f95f10949c086007aeadcee0214",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


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

    <div class="toyplot" id="t4f2e35ddd03a4e3f842a0e3d3756f6ba" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t4fe55ed5523545ca93fb92abe5f81d93" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t2635bf790ca44db4bc29822bb7cdfe8f"><clipPath id="tcc604d04db7c4948a7196eba2f8be44e"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#tcc604d04db7c4948a7196eba2f8be44e)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t9c6859d67c1749d2b66fa088a8b9ce66"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t7b1377c4c0eb471ca7d3be3b83db4abd" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t7b1377c4c0eb471ca7d3be3b83db4abd);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t194a5112a2ae4d9e8b040644b8b06c91" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="160.0" x2="160.0" y1="3" y2="-3"></line><line style="" x1="320.0" x2="320.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><g transform="translate(0.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464" y="-3.592">0.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.7424" y="15.608">(0.02, 0.19, 0.38)</text></g><g transform="translate(160.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464" y="-3.592">0.3333</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.7424" y="15.608">(0.65, 0.81, 0.89)</text></g><g transform="translate(320.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464" y="-3.592">0.6667</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.7424" y="15.608">(0.97, 0.72, 0.60)</text></g><g transform="translate(480.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464" y="-3.592">1.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.7424" y="15.608">(0.40, 0.00, 0.12)</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-30.0" y2="45.0"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-60.0"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t4fe55ed5523545ca93fb92abe5f81d93";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
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
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t194a5112a2ae4d9e8b040644b8b06c91",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>

