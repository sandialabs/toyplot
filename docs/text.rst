
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

    <div class="toyplot" id="t06e7c84d118e4be28a3e07e16f7dba43" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t1a545e32e3864c59b8e08292722e60de" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t41e21645986f4372a68688c6b2b7ae65"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-42.872" y="8.175999999999998">100</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:22.4px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="10.503999999999998" y="1.4559999999999986">-53</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


.. code:: python

    canvas = toyplot.Canvas(width=600, height=150)
    canvas.text(300, 100, "H<sub>2</sub>O", style={"font-size":"32px"});



.. raw:: html

    <div class="toyplot" id="te188811a2901447ebc7b29d86e3698e7" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t80737af948f1477092c0044c94fbd10a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="ta48209306dbb47fc86ddd89c5f2feb37"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-30.2272" y="8.175999999999998">H</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:22.4px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-7.123200000000001" y="12.655999999999999">2</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="5.331199999999999" y="8.175999999999998">O</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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

    <div class="toyplot" id="tf9405122d71c4f30b526f0f29b12477f" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t89fc5768b87d40a09e297c806ed53ad9" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="tf4aa4822324d4fa4bbe5ee1b3a139424"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-245.89680000000004" y="6.132">normal </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:bold;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-165.88080000000002" y="6.132">bold</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-115.2168" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-style:italic;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-108.54480000000001" y="6.132">italic</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-60.54480000000001" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:bold;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-53.87280000000001" y="6.132">strong</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="20.79119999999999" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-style:italic;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="27.46319999999999" y="6.132">emphasis</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="130.15919999999997" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:19.200000000000003px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="136.83119999999997" y="6.132">small</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="181.62479999999996" y="6.132"> </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="188.29679999999996" y="6.132">code</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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

    <div class="toyplot" id="tc4531ce1626d44579bdc0d3c7c13dde4" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t81ebf2dc98034aa889812ff6be37394b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 150.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="t6965bb3f9c8740e48c53c7e3e52b2763"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-125.55199999999999" y="8.175999999999998">foo </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-weight:bold;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-72.17599999999999" y="8.175999999999998">bar </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:32.0px;font-style:italic;font-weight:bold;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-13.487999999999978" y="8.175999999999998">baz </text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:32.0px;font-style:italic;font-weight:bold;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="48.752000000000024" y="8.175999999999998">blah</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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

    <div class="toyplot" id="t6c717c0ddf1b41b6b9ebcf825c4a34dd" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="200.0px" id="t42a96de3878c4b14860f541f8a21efae" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="ta2b16755796947fa8b164f79ef0a515f"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-33.36" y="-3.5920000000000023">0.567832</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-39.84640000000001" y="15.607999999999997">(243, 128, 19)</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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

    <div class="toyplot" id="t2bda6185d7ab45428cddec77cdeb363f" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="200.0px" id="tcf89444f439343c6923db9a12925591b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="tbd902767058147d9919d76c167acee33"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-83.66720000000001" y="4.9056">This is a </text><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:19.2px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-19.651200000000003" y="4.9056">special</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="40.09919999999999" y="4.9056"> word.</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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

    <div class="toyplot" id="t977aa5e6ccde4ad089d1dab17e2a2418" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="200.0px" id="tcaff5a33dea04b9dbdaf580550baa330" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="tdb51e398d64949e195a1dedca170b879"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-81.816" y="4.087999999999999">See </text><a xlink:href="http://toyplot.readthedocs.org"><text style="fill:rgb(27.5%,51%,70.6%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-48.904" y="4.087999999999999">Toyplot</text></a><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="3.559999999999995" y="4.087999999999999"> for details.</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    })();</script></div></div>


Note that additional tags or style attributes currently aren’t allowed
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

-  You must use ``<br/>`` or ``<br></br>`` to insert a line break …
   ``<br>`` is not allowed.
-  You must escape ``<`` as ``&lt;`` and ``>`` as ``&gt;`` because
   otherwise they will be confused with XHTML5 tags.
-  You must escape ``&`` as ``&amp;`` because otherwise it will be
   confused with an XHTML5 entity.

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    canvas.text(300, 100, "3 &lt; 4 &amp; 5 &gt; 6", style={"font-size":"16px"});



.. raw:: html

    <div class="toyplot" id="t2bf74aa3a4074d40a6744d19c8bc9aec" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="200.0px" id="tc219d5942aa04b7fa6b82292739a81ba" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-mark-Text" id="tf7fc3d774a6f466486dd16c79bc848bc"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,100.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-45.816" y="4.087999999999999">3 &lt; 4 &amp; 5 &gt; 6</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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

    <div class="toyplot" id="t182372054b264cf48c62238a07daf4ab" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="150.0px" id="tda377ad00e004e6b9b15446508bab180" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 150.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t5a08713109614d9caf43aa6f2dcd86c6"><clipPath id="t45dd9cbaea364904a1c7b6bf777b596c"><rect height="70.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t45dd9cbaea364904a1c7b6bf777b596c)"><g class="toyplot-mark-Text" id="t8fc63656f8114949a0d09438e6ea8012"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,75.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-26.676" y="6.132">Text!</text></g></g></g><g class="toyplot-mark-Point" id="t8f57a8a2ba0d4db6822cb7a4139e889b"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 75.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t182372054b264cf48c62238a07daf4ab";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tda377ad00e004e6b9b15446508bab180";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t8f57a8a2ba0d4db6822cb7a4139e889b","data","point",["x", "y0"],[[0.0], [0.0]],"toyplot");
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

    <div class="toyplot" id="t3adadc4b67b5480c9c02c828d4cdfc9b" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t6d05757e3dda42238e4aeed238ef3928" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tf4bb68781f004001ac41a67f8806d73d"><clipPath id="t5ad3682c79ad4e1884fd98cc77deda8f"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t5ad3682c79ad4e1884fd98cc77deda8f)"><g class="toyplot-mark-AxisLines" id="tcfa92f2c52224dd88c99b65b00e2a031" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="250.0" x2="250.0" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="tae9ab0b14fbd4d29a7ca89c2ecce1658"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,83.33333333333333)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-49.356" y="6.132">Centered</text></g></g></g><g class="toyplot-mark-Point" id="tac7b03f15ca643098278438f058d1921"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 83.33333333333333)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t40af74bdab42473fa0baad7d756d90e4"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="6.132">Left Justified</text></g></g></g><g class="toyplot-mark-Point" id="t890ead57f114484eb5fa5157e0fd23fb"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t692df9383c6e4dbbbf9a4abdf1305636"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,216.66666666666669)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-150.72" y="6.132">Right Justified</text></g></g></g><g class="toyplot-mark-Point" id="tef2d8ad0d44f473ba64ca61ec13580f6"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 216.66666666666669)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t3adadc4b67b5480c9c02c828d4cdfc9b";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t6d05757e3dda42238e4aeed238ef3928";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tac7b03f15ca643098278438f058d1921","data","point",["x", "y0"],[[0.0], [1.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t890ead57f114484eb5fa5157e0fd23fb","data","point",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tef2d8ad0d44f473ba64ca61ec13580f6","data","point",["x", "y0"],[[0.0], [-1.0]],"toyplot");
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

    <div class="toyplot" id="td58094a9322349099da5e888a8916df9" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t463d88d53d31466ebc786a8dceef7c32" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t193df1657a844a4bbb635978b9a6a09b"><clipPath id="t0b123da2823949c291af67fd6726fa13"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t0b123da2823949c291af67fd6726fa13)"><g class="toyplot-mark-AxisLines" id="t55eb7ed350fc4bfd8fd94ef89820e8cf" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="250.0" x2="250.0" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="t79a886ef1f3049f5a308f9c3b7d5daf6"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,75.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="6.132">Shifted +0px</text></g></g></g><g class="toyplot-mark-Point" id="tad47882d1bda46fbaff0ea9bb25e495d"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 75.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="ta3fd5cb5fb41445c804bafebea415f2a"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,125.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="20.0" y="6.132">Shifted +20px</text></g></g></g><g class="toyplot-mark-Point" id="t6559d657783845b5ad9e7d387a7f526e"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 125.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="td1f4ba5f0a2b4f588daac2621e3a8172"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,175.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="40.0" y="6.132">Shifted +40px</text></g></g></g><g class="toyplot-mark-Point" id="tb45c3355d4be467c89d0304e4faa7354"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 175.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t915dc2140dcf4cf2848fa40b5a1f02d4"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(250.0,225.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-20.0" y="6.132">Shifted -20px</text></g></g></g><g class="toyplot-mark-Point" id="t7c45609f4dd74723a7b685a106ecf5ba"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(250.0, 225.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "td58094a9322349099da5e888a8916df9";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t463d88d53d31466ebc786a8dceef7c32";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tad47882d1bda46fbaff0ea9bb25e495d","data","point",["x", "y0"],[[0.0], [1.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t6559d657783845b5ad9e7d387a7f526e","data","point",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tb45c3355d4be467c89d0304e4faa7354","data","point",["x", "y0"],[[0.0], [-1.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t7c45609f4dd74723a7b685a106ecf5ba","data","point",["x", "y0"],[[0.0], [-2.0]],"toyplot");
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

    <div class="toyplot" id="t08fe059ff2034f31b92ec6b4089c47b2" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tc50aa1d280a44ba1b997f978dc0a3463" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 800.0 300.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t16d4621bfd6a47de90139f1f01eb1eb7"><clipPath id="t76a880706f3841cd80978ece8977e908"><rect height="220.0" width="720.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t76a880706f3841cd80978ece8977e908)"><g class="toyplot-mark-AxisLines" id="t164eecda366e4773aacdaba5d6b5ec08" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="750.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t71e9518e300d4465aa0626c1f3c90107"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(68.25782882055526,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-20.676000000000002" y="20.531999999999996">Top</text></g></g></g><g class="toyplot-mark-Point" id="td136fb6b722f4fdab817592003fc7754"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(68.25782882055526, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t0786eb3240054a90b625b55450ce4e2c"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(222.7906225716275,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-35.339999999999996" y="6.132">Middle</text></g></g></g><g class="toyplot-mark-Point" id="t610d0a28e74047d99151a5b7d1d9df7b"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(222.7906225716275, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t6f87f64577964921b078da9c99a276b3"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(377.3234163226998,150.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-38.016" y="-8.267999999999997">Bottom</text></g></g></g><g class="toyplot-mark-Point" id="t7face2c7c6614998b35232e58244b6c2"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(377.3234163226998, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="td5766d9039d3469d8f9a6c32f1af834e"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(531.856210073772,150.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-65.364" y="0">1st Baseline</text></g></g></g><g class="toyplot-mark-Point" id="te572e6940cd04ff9882e9edbdbeb2087"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(531.856210073772, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t6da938c35fcd432693a2ccddd680c707"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(686.3890038248443,150.0)"><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-72.036" y="0.0">Last Baseline</text></g></g></g><g class="toyplot-mark-Point" id="t0e29369db4724dda90a7b8709644587d"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(686.3890038248443, 150.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t08fe059ff2034f31b92ec6b4089c47b2";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tc50aa1d280a44ba1b997f978dc0a3463";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"td136fb6b722f4fdab817592003fc7754","data","point",["x", "y0"],[[-1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t610d0a28e74047d99151a5b7d1d9df7b","data","point",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t7face2c7c6614998b35232e58244b6c2","data","point",["x", "y0"],[[1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"te572e6940cd04ff9882e9edbdbeb2087","data","point",["x", "y0"],[[2.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t0e29369db4724dda90a7b8709644587d","data","point",["x", "y0"],[[3.0], [0.0]],"toyplot");
    })();</script></div></div>


Note that to see the difference between ``first-baseline`` and
``last-baseline`` requires a block of text with more than one line,
since they align the anchor with the first and last line’s baselines
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

    <div class="toyplot" id="tf6f80f110665482292b048c0d37be820" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tf88b59e597d444a7925da11de1218472" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 800.0 300.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t422a6657f77d40088af6863058334a8d"><clipPath id="t2ab74d203bac4f62a56d65d7b1170ff4"><rect height="220.0" width="720.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t2ab74d203bac4f62a56d65d7b1170ff4)"><g class="toyplot-mark-AxisLines" id="td117a631d06d4e50b6697075c614c168" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="750.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t08f8abb383a544598fd218ebbb38b895"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(68.25782882055526,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-20.676000000000002" y="20.531999999999996">Top</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-20.676000000000002" y="49.331999999999994">Top</text></g></g></g><g class="toyplot-mark-Point" id="ta7c5b910a6824ed1b312b01f572407a8"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(68.25782882055526, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t4899377d28ff4a3e8b0ff37a22a7ffe1"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(222.7906225716275,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-35.339999999999996" y="-8.267999999999997">Middle</text><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-35.339999999999996" y="20.531999999999996">Middle</text></g></g></g><g class="toyplot-mark-Point" id="te0c4546e76ad4632938839fcdad14f7c"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(222.7906225716275, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t5bfa56b9487a45f3bc750ce10ee3fd36"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(377.3234163226998,150.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-38.016" y="-37.06799999999999">Bottom</text><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-38.016" y="-8.267999999999997">Bottom</text></g></g></g><g class="toyplot-mark-Point" id="tb4ac9b1536e544fb838f12308a8da061"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(377.3234163226998, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t01178264cd3d492e87c9ec472fcbd75a"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(531.856210073772,150.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-65.364" y="0">1st Baseline</text><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-65.364" y="28.799999999999994">1st Baseline</text></g></g></g><g class="toyplot-mark-Point" id="t3539b402db7e460e974c3684c6fefae6"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(531.856210073772, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t5b488443bd6b406dad0d2c132e7a4379"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(686.3890038248443,150.0)"><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-72.036" y="-28.799999999999994">Last Baseline</text><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-72.036" y="0.0">Last Baseline</text></g></g></g><g class="toyplot-mark-Point" id="t53fb14c292e74ba5b268caf681e0481c"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(686.3890038248443, 150.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tf6f80f110665482292b048c0d37be820";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tf88b59e597d444a7925da11de1218472";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"ta7c5b910a6824ed1b312b01f572407a8","data","point",["x", "y0"],[[-1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"te0c4546e76ad4632938839fcdad14f7c","data","point",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tb4ac9b1536e544fb838f12308a8da061","data","point",["x", "y0"],[[1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t3539b402db7e460e974c3684c6fefae6","data","point",["x", "y0"],[[2.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t53fb14c292e74ba5b268caf681e0481c","data","point",["x", "y0"],[[3.0], [0.0]],"toyplot");
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

    <div class="toyplot" id="t064d24fc08194605bd0f226f756af325" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t9a546f38f5fd4b049bebf5f986a69b12" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t4245df585a1a46818c51284d6d060ea4"><clipPath id="tb9275bcf9dd04b1aaf06ce84c21bb73f"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tb9275bcf9dd04b1aaf06ce84c21bb73f)"><g class="toyplot-mark-AxisLines" id="t0f18c13cb4374657bb5a0848b6cb1c17" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="550.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t0398c8ceb63e4591b752baa0432ff9f6"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-194.748" y="-2.4840000000000018">Alphabetic</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-82.692" y="-2.4840000000000018">  </text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-69.34799999999998" y="3.5471999999999975">Middle</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="1.3320000000000078" y="-2.4840000000000018">  </text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="14.676000000000009" y="6.131999999999998">Central</text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="92.02799999999999" y="-2.4840000000000018">  </text><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="105.37199999999999" y="14.747999999999998">Hanging</text></g></g></g><g class="toyplot-mark-Point" id="t53683bf76261409880a580130dfdde4d"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(300.0, 150.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t064d24fc08194605bd0f226f756af325";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t9a546f38f5fd4b049bebf5f986a69b12";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t53683bf76261409880a580130dfdde4d","data","point",["x", "y0"],[[-1.0], [0.0]],"toyplot");
    })();</script></div></div>


As you might expect, you can also shift text perpendicular to its
baseline by arbitrary amounts, using ``baseline-shift``. While you are
free to use any of Toyplot’s supported CSS length units for the shift,
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

    <div class="toyplot" id="t27ae74a75ab34dd499f8e04d110d1980" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t74c0868536cf477f8fc16811723fa2de" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 300.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t208d4909238f44bea20126684eb052f1"><clipPath id="te5c1e47b927f4f8f9d89317d1cfe44c8"><rect height="220.0" width="620.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#te5c1e47b927f4f8f9d89317d1cfe44c8)"><g class="toyplot-mark-AxisLines" id="ta721002212364616bbb0793625b99c1b" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="50.0" x2="650.0" y1="150.0" y2="150.0"></line></g></g><g class="toyplot-mark-Text" id="t8fc099e9194b4328864c5ef200adccca"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(101.68569285892843,150.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-62.028" y="30.131999999999998">Shift -100%</text></g></g></g><g class="toyplot-mark-Point" id="ta008a4b203f24d80b80ad03db5698955"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(101.68569285892843, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="td6b8987f6b944a67a016adccf4b99716"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(268.3384717940172,150.0)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-44.68800000000001" y="6.132">Shift 0%</text></g></g></g><g class="toyplot-mark-Point" id="t5746f56d3a2e4c9bae4cd2cb0cd0f1a2"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(268.3384717940172, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t43f40540d37a4f5f84a9248d2aefc7cc"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(434.9912507291059,150.0)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-51.36000000000001" y="-9.708">Shift 66%</text></g></g></g><g class="toyplot-mark-Point" id="t1f97607f8fdc484488dfa2aade35eaa6"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(434.9912507291059, 150.0)"><circle r="1.5"></circle></g></g></g><g class="toyplot-mark-Text" id="t20744ceeb8e2477db9904c4246e86442"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(601.6440296641946,150.0)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-58.032000000000004" y="-17.868000000000002">Shift 100%</text></g></g></g><g class="toyplot-mark-Point" id="t7032ecb07a9646fea4daa6befaa07636"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(601.6440296641946, 150.0)"><circle r="1.5"></circle></g></g></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t27ae74a75ab34dd499f8e04d110d1980";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t74c0868536cf477f8fc16811723fa2de";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"ta008a4b203f24d80b80ad03db5698955","data","point",["x", "y0"],[[-1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t5746f56d3a2e4c9bae4cd2cb0cd0f1a2","data","point",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t1f97607f8fdc484488dfa2aade35eaa6","data","point",["x", "y0"],[[1.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t7032ecb07a9646fea4daa6befaa07636","data","point",["x", "y0"],[[2.0], [0.0]],"toyplot");
    })();</script></div></div>


Of course, you’re free to combine all these style properties in any way
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

    <div class="toyplot" id="t9e52e42971d04f008673dc3ee567592c" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t4c7834836b5c471783967531a3e6cf86" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tdff5194c2ae744dd8e3853063f441211"><clipPath id="tc85bb6f2483a42238654076d971f246a"><rect height="220.0" width="86.66666666666666" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tc85bb6f2483a42238654076d971f246a)"><g class="toyplot-mark-AxisLines" id="tec703b4a0ee74a29b477bc3c4adfe1f3" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="83.33333333333333" x2="83.33333333333333" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="tb79484f3cf524bff89e8885a82b1fa6e"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(83.33333333333333,150.0)rotate(-45.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-27.024" y="6.132">a + b</text></g></g></g><g class="toyplot-mark-Point" id="t287d808447a7478296293fe64f13bd02"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(83.33333333333333, 150.0)"><circle r="1.5"></circle></g></g></g></g><g transform="translate(83.33333333333333,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-22.945999999999998" y="-4.823">default</text></g></g><g class="toyplot-coordinates-Cartesian" id="tfd4d231c161f4548b8f5de085162f374"><clipPath id="t7c51a7a7c2e148edb2e2e2af08f7345b"><rect height="220.0" width="86.66666666666666" x="206.66666666666666" y="40.0"></rect></clipPath><g clip-path="url(#t7c51a7a7c2e148edb2e2e2af08f7345b)"><g class="toyplot-mark-AxisLines" id="teaa98f32e9244946aaf9e35f25ea3b48" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="245.61441839467875" x2="245.61441839467875" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="tb22c8af9ee6848d4b8287c185ffac56d"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(245.61441839467875,150.0)rotate(-45.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-7.024000000000001" y="6.132">a + b</text></g></g></g><g class="toyplot-mark-Point" id="tf235d7aa18054b72b21b76a040e29531"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(245.61441839467875, 150.0)"><circle r="1.5"></circle></g></g></g></g><g transform="translate(250.0,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-68.43900000000001" y="-4.823">-toyplot-anchor-shift</text></g></g><g class="toyplot-coordinates-Cartesian" id="tf7a80d1171c3412aa1a5332516b0920e"><clipPath id="tadbbc39b28894be29680a4e99757f62b"><rect height="220.0" width="86.66666666666669" x="373.3333333333333" y="40.0"></rect></clipPath><g clip-path="url(#tadbbc39b28894be29680a4e99757f62b)"><g class="toyplot-mark-AxisLines" id="t5de9d0a27550439fa378809337675736" style=""><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0" x1="416.66666666666663" x2="416.66666666666663" y1="50.0" y2="250.0"></line></g></g><g class="toyplot-mark-Text" id="ta1550011828a4549a17f53430822b28e"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(416.66666666666663,150.0)rotate(-45.0)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:24.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-27.024" y="26.131999999999998">a + b</text></g></g></g><g class="toyplot-mark-Point" id="t5b966d83e75c4efc89d5da385fd564c1"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0" transform="translate(416.66666666666663, 150.0)"><circle r="1.5"></circle></g></g></g></g><g transform="translate(416.66666666666663,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-45.12199999999999" y="-4.823">baseline-shift</text></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t9e52e42971d04f008673dc3ee567592c";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t4c7834836b5c471783967531a3e6cf86";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t287d808447a7478296293fe64f13bd02","data","point",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tf235d7aa18054b72b21b76a040e29531","data","point",["x", "y0"],[[0.0], [0.0]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t5b966d83e75c4efc89d5da385fd564c1","data","point",["x", "y0"],[[0.0], [0.0]],"toyplot");
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

    <div class="toyplot" id="tbaeaece41d4a485091eab7c7268ccd2d" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="200.0px" id="t2f7a71cd0f4f4f55bd72c7749df5a170" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="te49264f2d12144e98070ac85a2001f8d"><clipPath id="t900cc08527dd483d90f3c69686e046e7"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t900cc08527dd483d90f3c69686e046e7)" transform="translate(50.0,50.0)"></g><g class="toyplot-coordinates-Axis" id="t28a3eb1def5c40e2b6f1e9fbdf5b1a6d" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.440892098500626e-16">-0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.0</text></g><g transform="translate(500.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t6bfee2f442c44bc982f47e5fbed67f30"><clipPath id="t88f1d68115b142eca0b30b133a3c2699"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t88f1d68115b142eca0b30b133a3c2699)" transform="translate(50.0,150.0)"></g><g class="toyplot-coordinates-Axis" id="t46889fd543984acb96ae97fec4a3e96b" transform="translate(50.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t2f7a71cd0f4f4f55bd72c7749df5a170";
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
            })(modules["toyplot.coordinates.Axis"],"t28a3eb1def5c40e2b6f1e9fbdf5b1a6d",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t46889fd543984acb96ae97fec4a3e96b",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Note that although the location can be specified explicitly, in most
cases the defaults should just work … note how the location of the Y
axis ticks and labels automatically changes from “above” to “below” when
the Y axis spine is repositioned in the following example:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    
    axis1 = canvas.cartesian(grid=(1, 2, 0))
    
    axis2 = canvas.cartesian(grid=(1, 2, 1))
    axis2.y.spine.position="high"



.. raw:: html

    <div class="toyplot" id="t03a715064dda4a4a987bab71be6ba8f2" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t5b76a711b3e14fe693e67d90092fde69" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t3d31bed95e75434b8a71e40d6ae033e8"><clipPath id="taa8b1f89cc3c454986980edf3ba17dde"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#taa8b1f89cc3c454986980edf3ba17dde)"></g><g class="toyplot-coordinates-Axis" id="t28d88f32f4e9474f96ab9ee32ade4b45" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t770b0790cc19414ca89c7193f73bb014" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.440892098500626e-16">-0.5</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.0</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="tc5618cdb36504d5e89142801a3f9595d"><clipPath id="t93b1919229d74c25aa6427cf07f4ffa8"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t93b1919229d74c25aa6427cf07f4ffa8)"></g><g class="toyplot-coordinates-Axis" id="t0714bba91d85440ea519b4453ba1c8b5" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t4f21361e8f7a45b39f4f10a037a0ee1f" transform="translate(550.0,250.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t5b76a711b3e14fe693e67d90092fde69";
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
            })(modules["toyplot.coordinates.Axis"],"t28d88f32f4e9474f96ab9ee32ade4b45",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t770b0790cc19414ca89c7193f73bb014",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t0714bba91d85440ea519b4453ba1c8b5",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t4f21361e8f7a45b39f4f10a037a0ee1f",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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

    <div class="toyplot" id="tc918f5663a174e26bfb2109bebba8498" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tce3462a2bb7d46cf937955c7c4fe9b42" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tf2032f6440c646d6817549c1c489207a"><clipPath id="tbf61dfac50b34962be9328ca5e3955f5"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tbf61dfac50b34962be9328ca5e3955f5)"></g><g class="toyplot-coordinates-Axis" id="tfa51b69a353743cdb6068ae2aff4802d" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t5286609bd7624743ba673299e8c063f4" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.440892098500626e-16">-0.5</text></g><g transform="translate(100.0,-30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.0</text></g><g transform="translate(200.0,-30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="15.0" y2="-22.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="30.0"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="tcdf470973c23421aabeee1e1929dc48b"><clipPath id="t36c265fd8ebd46049d94657c222f9807"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t36c265fd8ebd46049d94657c222f9807)"></g><g class="toyplot-coordinates-Axis" id="t91f02f36c26d41f5ae8ac3c31e161a94" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t132dcfaa7b994bddadf563b40dd4f761" transform="translate(550.0,250.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(100.0,30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(200.0,30.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-15.0" y2="22.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-30.0"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "tce3462a2bb7d46cf937955c7c4fe9b42";
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
            })(modules["toyplot.coordinates.Axis"],"tfa51b69a353743cdb6068ae2aff4802d",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t5286609bd7624743ba673299e8c063f4",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t91f02f36c26d41f5ae8ac3c31e161a94",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t132dcfaa7b994bddadf563b40dd4f761",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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

    <div class="toyplot" id="tbfd73c84a1a541a1bff3ba0cb82e9dbb" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t7c5662fad64f463e98d591b3f60bf897" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 400.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t0b2d6b3d66e043b7bc86122baa0764eb"><clipPath id="ta5e311d34b474bd8913bdd21ed593b47"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#ta5e311d34b474bd8913bdd21ed593b47)" transform="translate(50.0,50.0)"></g><g class="toyplot-coordinates-Axis" id="t2cfe0d07585443dcb70747dabb1836e2" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="-4.440892098500626e-16">-0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.0</text></g><g transform="translate(500.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="tc74a9c37dd57487f8d630bc39a211326"><clipPath id="t95401eb0eb2b4b99adc144363f2d0b47"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t95401eb0eb2b4b99adc144363f2d0b47)" transform="translate(50.0,150.0)"></g><g class="toyplot-coordinates-Axis" id="td8cc8c466cfa4016bdf26de401a89cf0" transform="translate(50.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.784" y="0.0">-0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="0.0">0.0</text></g><g transform="translate(500.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="0.0">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="tbaaad532d53e4c3280e533c9493fabaf"><clipPath id="t704f51abfd8e480ca7290691dd6d07cb"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t704f51abfd8e480ca7290691dd6d07cb)" transform="translate(50.0,250.0)"></g><g class="toyplot-coordinates-Axis" id="t3aafcc2c37fe4994b1d3861507d4288b" transform="translate(50.0,250.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t01c285c8466a47f2a2194e3ca820ad42"><clipPath id="tb37c92a04d224433a97b0c9346068e83"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#tb37c92a04d224433a97b0c9346068e83)" transform="translate(50.0,350.0)"></g><g class="toyplot-coordinates-Axis" id="t2471c45973b2482887d4a5c59f561c91" transform="translate(50.0,350.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.784" y="13.687999999999999">-0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="13.687999999999999">0.0</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="13.687999999999999">0.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t7c5662fad64f463e98d591b3f60bf897";
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
            })(modules["toyplot.coordinates.Axis"],"t2cfe0d07585443dcb70747dabb1836e2",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"td8cc8c466cfa4016bdf26de401a89cf0",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t3aafcc2c37fe4994b1d3861507d4288b",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t2471c45973b2482887d4a5c59f561c91",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
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

    <div class="toyplot" id="t02cd9fc3f3cc437fa1aa534d2f54a59d" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="tf73404843e9d4f9fb484c849a0d4d9d7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t6e7d940bc2b14f9cb0282f150bb77305"><clipPath id="t8e71e3c5112746c5b0f3934e719fe0ef"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t8e71e3c5112746c5b0f3934e719fe0ef)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t05331f9a7f31404996d03fdb11f639be"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tc86f3d684fbd4e348c19718dbad70a97" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873015872" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746031744" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.04761904761904761" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.06349206349206349" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.07936507936507936" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.09523809523809522" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.1111111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.12698412698412698" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.14285714285714285" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873015872" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.1746031746031746" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.19047619047619044" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.20634920634920634" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.2222222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.23809523809523808" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.25396825396825395" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.2698412698412698" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.2857142857142857" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.30158730158730157" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746031744" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.3333333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.3492063492063492" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.36507936507936506" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.3809523809523809" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.3968253968253968" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.4126984126984127" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.42857142857142855" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.4444444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.4603174603174603" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619047616" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.49206349206349204" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.5079365079365079" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.5238095238095237" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.5396825396825397" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.5555555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.5714285714285714" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.5873015873015872" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.6031746031746031" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.6190476190476191" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.6349206349206349" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.6507936507936507" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.6666666666666666" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.6825396825396826" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.6984126984126984" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.7142857142857142" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.7301587301587301" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.7460317460317459" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.7619047619047618" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.7777777777777776" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.7936507936507936" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.8095238095238095" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.8253968253968254" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.8412698412698412" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.8571428571428571" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873015873" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.8888888888888888" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.9047619047619047" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.9206349206349206" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.9365079365079365" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.9523809523809523" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.9682539682539681" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.9841269841269841" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tc86f3d684fbd4e348c19718dbad70a97);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t0b52725b91664ddeb35739172673a1ce" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="240.0" x2="240.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><g transform="translate(0.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="2.5549999999999997">0.0</text></g><g transform="translate(240.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="2.5549999999999997">0.5</text></g><g transform="translate(480.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="2.5549999999999997">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "tf73404843e9d4f9fb484c849a0d4d9d7";
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
            })(modules["toyplot.coordinates.Axis"],"t0b52725b91664ddeb35739172673a1ce",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]);
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

    <div class="toyplot" id="t980befebd25147fb9ace3cb3592fe66a" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t478f7b80ff324a07af5cf6f5a0654c1d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="tbc6518335291451fbc4c500f5cde9ae3"><clipPath id="tcb2aed54488047cb8460ab7c749c6abe"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#tcb2aed54488047cb8460ab7c749c6abe)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="tca212b3138704ce09e8d987cbdc7c17a"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t89adcc211f24489a9a7ebf236220239d" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873015872" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746031744" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.04761904761904761" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.06349206349206349" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.07936507936507936" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.09523809523809522" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.1111111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.12698412698412698" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.14285714285714285" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873015872" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.1746031746031746" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.19047619047619044" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.20634920634920634" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.2222222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.23809523809523808" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.25396825396825395" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.2698412698412698" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.2857142857142857" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.30158730158730157" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746031744" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.3333333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.3492063492063492" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.36507936507936506" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.3809523809523809" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.3968253968253968" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.4126984126984127" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.42857142857142855" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.4444444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.4603174603174603" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619047616" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.49206349206349204" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.5079365079365079" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.5238095238095237" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.5396825396825397" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.5555555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.5714285714285714" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.5873015873015872" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.6031746031746031" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.6190476190476191" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.6349206349206349" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.6507936507936507" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.6666666666666666" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.6825396825396826" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.6984126984126984" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.7142857142857142" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.7301587301587301" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.7460317460317459" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.7619047619047618" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.7777777777777776" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.7936507936507936" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.8095238095238095" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.8253968253968254" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.8412698412698412" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.8571428571428571" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873015873" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.8888888888888888" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.9047619047619047" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.9206349206349206" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.9365079365079365" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.9523809523809523" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.9682539682539681" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.9841269841269841" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t89adcc211f24489a9a7ebf236220239d);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="tc3c71d4a56bc44319c2dd50e7917cabd" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="160.0" x2="160.0" y1="3" y2="-3"></line><line style="" x1="320.0" x2="320.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><g transform="translate(0.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.5920000000000023">0.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.607999999999997">(0.02, 0.19, 0.38)</text></g><g transform="translate(160.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.5920000000000023">0.3333</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.607999999999997">(0.65, 0.81, 0.89)</text></g><g transform="translate(320.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.5920000000000023">0.6667</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.607999999999997">(0.97, 0.72, 0.60)</text></g><g transform="translate(480.0,6)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="-3.5920000000000023">1.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="15.607999999999997">(0.40, 0.00, 0.12)</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t478f7b80ff324a07af5cf6f5a0654c1d";
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
            })(modules["toyplot.coordinates.Axis"],"tc3c71d4a56bc44319c2dd50e7917cabd",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]);
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

    <div class="toyplot" id="t6bfa076f270d4bea90f5ff7d32c04919" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t98ddecf843ec46169f314df3e081b282" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t102f5fe85e3f4fb4bee2f52f989c2303"><clipPath id="t3a9bfa10987f46719af26b9a5d4d884c"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t3a9bfa10987f46719af26b9a5d4d884c)" transform="translate(300.0,540.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t1eb214872acc4263abb4191bca976d96"><defs><linearGradient gradientUnits="userSpaceOnUse" id="ta00bfd5574f74ce7ad2c90d788d5871c" x1="0.0" x2="480.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(1.96%,18.8%,38%)" stop-opacity="1.0"></stop><stop offset="0.015873015873015872" stop-color="rgb(3.7%,22.2%,42.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746031744" stop-color="rgb(5.45%,25.5%,47.4%)" stop-opacity="1.0"></stop><stop offset="0.04761904761904761" stop-color="rgb(7.19%,28.9%,52%)" stop-opacity="1.0"></stop><stop offset="0.06349206349206349" stop-color="rgb(8.93%,32.3%,56.7%)" stop-opacity="1.0"></stop><stop offset="0.07936507936507936" stop-color="rgb(10.7%,35.6%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.09523809523809522" stop-color="rgb(12.4%,39%,66.1%)" stop-opacity="1.0"></stop><stop offset="0.1111111111111111" stop-color="rgb(14.4%,42%,68.5%)" stop-opacity="1.0"></stop><stop offset="0.12698412698412698" stop-color="rgb(16.5%,44.8%,69.9%)" stop-opacity="1.0"></stop><stop offset="0.14285714285714285" stop-color="rgb(18.7%,47.6%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.15873015873015872" stop-color="rgb(20.8%,50.4%,72.7%)" stop-opacity="1.0"></stop><stop offset="0.1746031746031746" stop-color="rgb(22.9%,53.2%,74.2%)" stop-opacity="1.0"></stop><stop offset="0.19047619047619044" stop-color="rgb(25%,56%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.20634920634920634" stop-color="rgb(28.2%,58.9%,77.1%)" stop-opacity="1.0"></stop><stop offset="0.2222222222222222" stop-color="rgb(33.2%,62%,78.8%)" stop-opacity="1.0"></stop><stop offset="0.23809523809523808" stop-color="rgb(38.1%,65.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.25396825396825395" stop-color="rgb(43%,68.2%,82.2%)" stop-opacity="1.0"></stop><stop offset="0.2698412698412698" stop-color="rgb(47.9%,71.3%,83.9%)" stop-opacity="1.0"></stop><stop offset="0.2857142857142857" stop-color="rgb(52.8%,74.5%,85.5%)" stop-opacity="1.0"></stop><stop offset="0.30158730158730157" stop-color="rgb(57.6%,77.5%,87.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746031744" stop-color="rgb(61.6%,79.4%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.3333333333333333" stop-color="rgb(65.5%,81.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.3492063492063492" stop-color="rgb(69.4%,83.4%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.36507936507936506" stop-color="rgb(73.3%,85.4%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.3809523809523809" stop-color="rgb(77.3%,87.4%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.3968253968253968" stop-color="rgb(81.2%,89.4%,93.9%)" stop-opacity="1.0"></stop><stop offset="0.4126984126984127" stop-color="rgb(83.9%,90.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.42857142857142855" stop-color="rgb(86.2%,91.8%,94.9%)" stop-opacity="1.0"></stop><stop offset="0.4444444444444444" stop-color="rgb(88.6%,92.9%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.4603174603174603" stop-color="rgb(90.9%,94.1%,95.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619047616" stop-color="rgb(93.3%,95.2%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.49206349206349204" stop-color="rgb(95.7%,96.3%,96.6%)" stop-opacity="1.0"></stop><stop offset="0.5079365079365079" stop-color="rgb(97%,96%,95.4%)" stop-opacity="1.0"></stop><stop offset="0.5238095238095237" stop-color="rgb(97.4%,94.2%,92.4%)" stop-opacity="1.0"></stop><stop offset="0.5396825396825397" stop-color="rgb(97.8%,92.5%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.5555555555555556" stop-color="rgb(98.2%,90.8%,86.4%)" stop-opacity="1.0"></stop><stop offset="0.5714285714285714" stop-color="rgb(98.5%,89%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.5873015873015872" stop-color="rgb(98.9%,87.3%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.6031746031746031" stop-color="rgb(99.1%,85.2%,77.2%)" stop-opacity="1.0"></stop><stop offset="0.6190476190476191" stop-color="rgb(98.5%,81.8%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.6349206349206349" stop-color="rgb(98%,78.5%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.6507936507936507" stop-color="rgb(97.4%,75.1%,64.3%)" stop-opacity="1.0"></stop><stop offset="0.6666666666666666" stop-color="rgb(96.9%,71.8%,60%)" stop-opacity="1.0"></stop><stop offset="0.6825396825396826" stop-color="rgb(96.3%,68.4%,55.7%)" stop-opacity="1.0"></stop><stop offset="0.6984126984126984" stop-color="rgb(95.7%,65%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.7142857142857142" stop-color="rgb(94%,60.8%,48%)" stop-opacity="1.0"></stop><stop offset="0.7301587301587301" stop-color="rgb(92.1%,56.5%,44.7%)" stop-opacity="1.0"></stop><stop offset="0.7460317460317459" stop-color="rgb(90.3%,52.3%,41.4%)" stop-opacity="1.0"></stop><stop offset="0.7619047619047618" stop-color="rgb(88.4%,48%,38.1%)" stop-opacity="1.0"></stop><stop offset="0.7777777777777776" stop-color="rgb(86.5%,43.7%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.7936507936507936" stop-color="rgb(84.7%,39.4%,31.5%)" stop-opacity="1.0"></stop><stop offset="0.8095238095238095" stop-color="rgb(82.6%,35%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.8253968253968254" stop-color="rgb(80.3%,30.5%,26.8%)" stop-opacity="1.0"></stop><stop offset="0.8412698412698412" stop-color="rgb(78.1%,26%,24.7%)" stop-opacity="1.0"></stop><stop offset="0.8571428571428571" stop-color="rgb(75.9%,21.5%,22.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873015873" stop-color="rgb(73.6%,17%,20.5%)" stop-opacity="1.0"></stop><stop offset="0.8888888888888888" stop-color="rgb(71.4%,12.5%,18.3%)" stop-opacity="1.0"></stop><stop offset="0.9047619047619047" stop-color="rgb(68.4%,8.96%,16.6%)" stop-opacity="1.0"></stop><stop offset="0.9206349206349206" stop-color="rgb(63.7%,7.47%,15.9%)" stop-opacity="1.0"></stop><stop offset="0.9365079365079365" stop-color="rgb(59.1%,5.98%,15.1%)" stop-opacity="1.0"></stop><stop offset="0.9523809523809523" stop-color="rgb(54.4%,4.48%,14.4%)" stop-opacity="1.0"></stop><stop offset="0.9682539682539681" stop-color="rgb(49.7%,2.99%,13.7%)" stop-opacity="1.0"></stop><stop offset="0.9841269841269841" stop-color="rgb(45.1%,1.49%,12.9%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(40.4%,0%,12.2%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#ta00bfd5574f74ce7ad2c90d788d5871c);stroke:none;stroke-width:1.0" width="480.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t81f25dee60c546fb9d430ed4a5c1991e" transform="translate(300.0,540.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="480.0" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="3" y2="-3"></line><line style="" x1="160.0" x2="160.0" y1="3" y2="-3"></line><line style="" x1="320.0" x2="320.0" y1="3" y2="-3"></line><line style="" x1="480.0" x2="480.0" y1="3" y2="-3"></line></g><g><g transform="translate(0.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464000000000002" y="-3.5920000000000023">0.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.74240000000001" y="15.607999999999997">(0.02, 0.19, 0.38)</text></g><g transform="translate(160.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464000000000002" y="-3.5920000000000023">0.3333</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.74240000000001" y="15.607999999999997">(0.65, 0.81, 0.89)</text></g><g transform="translate(320.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464000000000002" y="-3.5920000000000023">0.6667</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.74240000000001" y="15.607999999999997">(0.97, 0.72, 0.60)</text></g><g transform="translate(480.0,60.0)rotate(90)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:16.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.464000000000002" y="-3.5920000000000023">1.0000</text><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.8px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-48.74240000000001" y="15.607999999999997">(0.40, 0.00, 0.12)</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-30.0" y2="45.0"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-60.0"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t98ddecf843ec46169f314df3e081b282";
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
            })(modules["toyplot.coordinates.Axis"],"t81f25dee60c546fb9d430ed4a5c1991e",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>

