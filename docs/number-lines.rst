
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _number-lines:

Number Lines
============

The :class:`toyplot.axes.NumberLine` class provides a single axis that
maps one-dimensional data values to canvas coordinates. The number line
*range* (its coordinates on the Toyplot the canvas) is specified at
creation time (see :ref:`canvas-layout`), while the *domain* is
implicitly defined to include all displayed data (but can be manually
overridden by the caller if desired).

If your data is two-dimensional, you should use :ref:`cartesian-axes`
instead.

Typically, you create number lines explicitly using
:meth:`toyplot.canvas.Canvas.numberline`:

.. code:: python

    import numpy
    numpy.random.seed(1234)
    events = numpy.random.uniform(size=(25, 4))

.. code:: python

    import toyplot
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.scatterplot(events.T[0]);



.. raw:: html

    <div align="center" class="toyplot" id="t2452da76f9d44f25b2bb13f443900386"><svg height="100.0px" id="t2c00c6705dfc4b55b50b9b40d5d81005" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="tf6c286a8be0543eea7eaa6e3eaa016b8"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="tebe440a8f12c4f09a36422c201a64e5f" style="stroke:none" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="95.759725189446144" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="389.98790405940179" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.06967684185258" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.73146758606816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="251.54158265390487" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.44299195068615" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="466.57005099126081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="158.41806108443564" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.07382104007957" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="109.39605283704429" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="29.90461138992595" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.31238996722442" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="164.8342228104575" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.97232152526567" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="395.2620665285167" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.62548001225488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="191.15872601575325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.971350243481496" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="235.81626716018388" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="208.37676890134659" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.44658608780509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.99878254088662" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.86288447548952" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.11213879253023" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="268.43909646220487" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-axes-Axis" id="t8b84bd04da9b4b639be7f87365bc8f5e" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="29.90461138992595" x2="479.0696768418526" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t2452da76f9d44f25b2bb13f443900386 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t2452da76f9d44f25b2bb13f443900386 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script><script>
    (function()
    {
      var data_tables = [{"data": [[0.1915194503788923, 0.7799758081188035, 0.9581393536837052, 0.6834629351721363, 0.5030831653078097, 0.3648859839013723, 0.9331401019825216, 0.31683612216887125, 0.8021476420801591, 0.21879210567408858, 0.0598092227798519, 0.5946247799344488, 0.329668445620915, 0.5659446430505314, 0.7905241330570334, 0.2852509600245098, 0.38231745203150647, 0.12394270048696299, 0.4716325343203678, 0.4167535378026932, 0.4368931721756102, 0.7059975650817732, 0.6337257689509791, 0.5282242775850605, 0.5368781929244097]], "title": "Scatterplot Data", "names": ["x0"], "id": "tebe440a8f12c4f09a36422c201a64e5f", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
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
          var popup = document.querySelector("#t2452da76f9d44f25b2bb13f443900386 .toyplot-mark-popup");
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


Note that when you add a scatterplot to a number line, it is a
one-dimensional scatterplot, so you can only supply one set of
coordinates.

When you add multiple marks to a number line, they "stack up" on top of
each other:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.scatterplot(events.T[0])
    numberline.scatterplot(events.T[1]);



.. raw:: html

    <div align="center" class="toyplot" id="t0e6e48fdc6054d7caf9b4c362080a365"><svg height="100.0px" id="t85b93893e9d84ad2b5f6f81624b140f2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t8a915cc4c37a46ff9eb1893548338f4a"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="t1958c8ce814d441f928cb35d68bdaf9c" style="stroke:none" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="95.759725189446144" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="389.98790405940179" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.06967684185258" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.73146758606816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="251.54158265390487" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.44299195068615" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="466.57005099126081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="158.41806108443564" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.07382104007957" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="109.39605283704429" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="29.90461138992595" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.31238996722442" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="164.8342228104575" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.97232152526567" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="395.2620665285167" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.62548001225488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="191.15872601575325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.971350243481496" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="235.81626716018388" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="208.37676890134659" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.44658608780509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.99878254088662" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.86288447548952" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.11213879253023" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="268.43909646220487" cy="0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="tb7b321338b2946008342bd1132e9011f" style="stroke:none" transform="translate(50.0,50.0) rotate(0.0) translate(0,-20.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="311.05438551991591" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="136.29630264132081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="437.96631737104735" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="356.35101349145009" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="6.8842247953411206" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="307.69808921674684" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="325.68907161328872" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="284.04932631303461" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="71.883412257282288" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="462.43381430778254" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="92.143541906906819" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="266.65508149937529" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="251.48341655630918" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="3.3820309950013949" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="496.04073309418072" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="312.45835265295551" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="26.936842573118291" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="59.690448963124197" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="53.563408596933151" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="267.92583126580791" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="306.07449853287875" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="74.916857994963621" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="219.15494056121375" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="475.71438187679661" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="409.60103353207916" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-axes-Axis" id="t119ed3aeacfa4c7b939e63188899a78e" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="3.382030995001395" x2="496.0407330941807" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t0e6e48fdc6054d7caf9b4c362080a365 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t0e6e48fdc6054d7caf9b4c362080a365 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script><script>
    (function()
    {
      var data_tables = [{"data": [[0.1915194503788923, 0.7799758081188035, 0.9581393536837052, 0.6834629351721363, 0.5030831653078097, 0.3648859839013723, 0.9331401019825216, 0.31683612216887125, 0.8021476420801591, 0.21879210567408858, 0.0598092227798519, 0.5946247799344488, 0.329668445620915, 0.5659446430505314, 0.7905241330570334, 0.2852509600245098, 0.38231745203150647, 0.12394270048696299, 0.4716325343203678, 0.4167535378026932, 0.4368931721756102, 0.7059975650817732, 0.6337257689509791, 0.5282242775850605, 0.5368781929244097]], "title": "Scatterplot Data", "names": ["x0"], "id": "t1958c8ce814d441f928cb35d68bdaf9c", "filename": "toyplot"}, {"data": [[0.6221087710398319, 0.2725926052826416, 0.8759326347420947, 0.7127020269829002, 0.013768449590682241, 0.6153961784334937, 0.6513781432265774, 0.5680986526260692, 0.14376682451456457, 0.924867628615565, 0.18428708381381365, 0.5333101629987506, 0.5029668331126184, 0.00676406199000279, 0.9920814661883615, 0.624916705305911, 0.05387368514623658, 0.1193808979262484, 0.1071268171938663, 0.5358516625316159, 0.6121489970657575, 0.14983371598992723, 0.4383098811224275, 0.9514287637535932, 0.8192020670641583]], "title": "Scatterplot Data", "names": ["x0"], "id": "tb7b321338b2946008342bd1132e9011f", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
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
          var popup = document.querySelector("#t0e6e48fdc6054d7caf9b4c362080a365 .toyplot-mark-popup");
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


You can specify the default spacing between marks (and the axis spine)
when you create the number line:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline(spacing=10)
    numberline.scatterplot(events.T[0])
    numberline.scatterplot(events.T[1]);



.. raw:: html

    <div align="center" class="toyplot" id="td4cbf797193c42afb34c8268181818e8"><svg height="100.0px" id="t104aa8f0ee7042ac881688546c9e0d27" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t35152ce6e40942109a1ca84ac1a8a240"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="tb8cc03abe100405ca8ee682b9c293989" style="stroke:none" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="95.759725189446144" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="389.98790405940179" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.06967684185258" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.73146758606816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="251.54158265390487" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.44299195068615" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="466.57005099126081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="158.41806108443564" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.07382104007957" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="109.39605283704429" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="29.90461138992595" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.31238996722442" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="164.8342228104575" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.97232152526567" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="395.2620665285167" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.62548001225488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="191.15872601575325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.971350243481496" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="235.81626716018388" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="208.37676890134659" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.44658608780509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.99878254088662" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.86288447548952" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.11213879253023" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="268.43909646220487" cy="0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t8340df86015c4e7d8786e73be1afbdc4" style="stroke:none" transform="translate(50.0,50.0) rotate(0.0) translate(0,-10.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="311.05438551991591" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="136.29630264132081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="437.96631737104735" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="356.35101349145009" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="6.8842247953411206" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="307.69808921674684" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="325.68907161328872" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="284.04932631303461" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="71.883412257282288" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="462.43381430778254" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="92.143541906906819" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="266.65508149937529" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="251.48341655630918" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="3.3820309950013949" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="496.04073309418072" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="312.45835265295551" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="26.936842573118291" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="59.690448963124197" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="53.563408596933151" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="267.92583126580791" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="306.07449853287875" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="74.916857994963621" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="219.15494056121375" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="475.71438187679661" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="409.60103353207916" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-axes-Axis" id="tc9c7b460a51f401fa2cc4664ef7b5684" transform="translate(50.0,50.0) rotate(0.0) translate(0,10.0)"><line style="" x1="3.382030995001395" x2="496.0407330941807" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#td4cbf797193c42afb34c8268181818e8 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#td4cbf797193c42afb34c8268181818e8 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script><script>
    (function()
    {
      var data_tables = [{"data": [[0.1915194503788923, 0.7799758081188035, 0.9581393536837052, 0.6834629351721363, 0.5030831653078097, 0.3648859839013723, 0.9331401019825216, 0.31683612216887125, 0.8021476420801591, 0.21879210567408858, 0.0598092227798519, 0.5946247799344488, 0.329668445620915, 0.5659446430505314, 0.7905241330570334, 0.2852509600245098, 0.38231745203150647, 0.12394270048696299, 0.4716325343203678, 0.4167535378026932, 0.4368931721756102, 0.7059975650817732, 0.6337257689509791, 0.5282242775850605, 0.5368781929244097]], "title": "Scatterplot Data", "names": ["x0"], "id": "tb8cc03abe100405ca8ee682b9c293989", "filename": "toyplot"}, {"data": [[0.6221087710398319, 0.2725926052826416, 0.8759326347420947, 0.7127020269829002, 0.013768449590682241, 0.6153961784334937, 0.6513781432265774, 0.5680986526260692, 0.14376682451456457, 0.924867628615565, 0.18428708381381365, 0.5333101629987506, 0.5029668331126184, 0.00676406199000279, 0.9920814661883615, 0.624916705305911, 0.05387368514623658, 0.1193808979262484, 0.1071268171938663, 0.5358516625316159, 0.6121489970657575, 0.14983371598992723, 0.4383098811224275, 0.9514287637535932, 0.8192020670641583]], "title": "Scatterplot Data", "names": ["x0"], "id": "t8340df86015c4e7d8786e73be1afbdc4", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
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
          var popup = document.querySelector("#td4cbf797193c42afb34c8268181818e8 .toyplot-mark-popup");
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


And you can individually control the offset of the individual marks, as
well as the padding (distance between the axis spine and the first
mark):

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    numberline = canvas.numberline(spacing=10, padding=20)
    numberline.scatterplot(events.T[0])
    numberline.scatterplot(events.T[1])
    numberline.scatterplot(events.T[2], offset=40)
    numberline.scatterplot(events.T[3], offset=50);



.. raw:: html

    <div align="center" class="toyplot" id="t9dcc8ab05cc845d7874ec412a06d2daa"><svg height="200.0px" id="t61027a0cc2454d478f012fc8690404c7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="tf5dee28ba2d7489a937dcc30842a5886"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="t498d8ad7f2e74274b3f3482ba850455f" style="stroke:none" transform="translate(50.0,100.0) rotate(0.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="95.759725189446144" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="389.98790405940179" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.06967684185258" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.73146758606816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="251.54158265390487" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.44299195068615" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="466.57005099126081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="158.41806108443564" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.07382104007957" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="109.39605283704429" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="29.90461138992595" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.31238996722442" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="164.8342228104575" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.97232152526567" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="395.2620665285167" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.62548001225488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="191.15872601575325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.971350243481496" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="235.81626716018388" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="208.37676890134659" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.44658608780509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.99878254088662" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.86288447548952" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.11213879253023" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="268.43909646220487" cy="0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t57c347b1689a4d1f9c998371dcd1c944" style="stroke:none" transform="translate(50.0,100.0) rotate(0.0) translate(0,-10.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="311.05438551991591" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="136.29630264132081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="437.96631737104735" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="356.35101349145009" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="6.8842247953411206" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="307.69808921674684" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="325.68907161328872" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="284.04932631303461" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="71.883412257282288" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="462.43381430778254" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="92.143541906906819" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="266.65508149937529" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="251.48341655630918" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="3.3820309950013949" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="496.04073309418072" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="312.45835265295551" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="26.936842573118291" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="59.690448963124197" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="53.563408596933151" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="267.92583126580791" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="306.07449853287875" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="74.916857994963621" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="219.15494056121375" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="475.71438187679661" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="409.60103353207916" cy="0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t51e682f591e94411a96c9f3099f8dd8d" style="stroke:none" transform="translate(50.0,100.0) rotate(0.0) translate(0,-40)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="218.86386950355725" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="138.23212757154835" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="178.90863497893332" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="185.12537739519746" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="386.41331080618704" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="37.690620821488274" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="198.60128886307709" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="434.56369478061293" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="352.13048555916771" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="221.07037770208831" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="23.677639400757567" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="21.662031347401744" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="55.947158787201914" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="308.72085440214852" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="479.40088107643322" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="239.04689783533729" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="225.82420413042954" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="369.26152807167341" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="114.60928273030896" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="3.104258293564699" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="459.09903769028654" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="373.03170456835835" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="76.286387337252677" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="240.17958925500804" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="28.557819044429944" cy="0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t7c043802146145039659871098328e54" style="stroke:none" transform="translate(50.0,100.0) rotate(0.0) translate(0,-50)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="392.67929185688462" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="400.93608876750966" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="250.49756276172934" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="280.59809303281247" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="441.32059531805828" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="184.41200300098726" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="394.36507147037275" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="218.08671194783969" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="352.29065409478625" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="454.65797948623629" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="337.44047179116512" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="280.71654003169891" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="303.59685310924226" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="456.06144321657717" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="395.98206764581988" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="97.837589332949122" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="491.00237076097727" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="293.65181673199231" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="449.98259741833766" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="150.32085288515057" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="312.86833498126765" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="415.50349621676889" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="284.20480762359506" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="251.27978169127519" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="334.71087153727439" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-axes-Axis" id="t7ea594758c0d4f65927be655a8863759" transform="translate(50.0,100.0) rotate(0.0) translate(0,20.0)"><line style="" x1="3.104258293564699" x2="496.0407330941807" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t9dcc8ab05cc845d7874ec412a06d2daa text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t9dcc8ab05cc845d7874ec412a06d2daa text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script><script>
    (function()
    {
      var data_tables = [{"data": [[0.1915194503788923, 0.7799758081188035, 0.9581393536837052, 0.6834629351721363, 0.5030831653078097, 0.3648859839013723, 0.9331401019825216, 0.31683612216887125, 0.8021476420801591, 0.21879210567408858, 0.0598092227798519, 0.5946247799344488, 0.329668445620915, 0.5659446430505314, 0.7905241330570334, 0.2852509600245098, 0.38231745203150647, 0.12394270048696299, 0.4716325343203678, 0.4167535378026932, 0.4368931721756102, 0.7059975650817732, 0.6337257689509791, 0.5282242775850605, 0.5368781929244097]], "title": "Scatterplot Data", "names": ["x0"], "id": "t498d8ad7f2e74274b3f3482ba850455f", "filename": "toyplot"}, {"data": [[0.6221087710398319, 0.2725926052826416, 0.8759326347420947, 0.7127020269829002, 0.013768449590682241, 0.6153961784334937, 0.6513781432265774, 0.5680986526260692, 0.14376682451456457, 0.924867628615565, 0.18428708381381365, 0.5333101629987506, 0.5029668331126184, 0.00676406199000279, 0.9920814661883615, 0.624916705305911, 0.05387368514623658, 0.1193808979262484, 0.1071268171938663, 0.5358516625316159, 0.6121489970657575, 0.14983371598992723, 0.4383098811224275, 0.9514287637535932, 0.8192020670641583]], "title": "Scatterplot Data", "names": ["x0"], "id": "t57c347b1689a4d1f9c998371dcd1c944", "filename": "toyplot"}, {"data": [[0.4377277390071145, 0.2764642551430967, 0.35781726995786667, 0.37025075479039493, 0.772826621612374, 0.07538124164297655, 0.3972025777261542, 0.8691273895612258, 0.7042609711183354, 0.44214075540417663, 0.04735527880151513, 0.04332406269480349, 0.11189431757440382, 0.617441708804297, 0.9588017621528665, 0.47809379567067456, 0.45164840826085906, 0.7385230561433468, 0.22921856546061792, 0.006208516587129398, 0.9181980753805731, 0.7460634091367166, 0.15257277467450536, 0.4803591785100161, 0.05711563808885989]], "title": "Scatterplot Data", "names": ["x0"], "id": "t51e682f591e94411a96c9f3099f8dd8d", "filename": "toyplot"}, {"data": [[0.7853585837137692, 0.8018721775350193, 0.5009951255234587, 0.5611961860656249, 0.8826411906361166, 0.3688240060019745, 0.7887301429407455, 0.43617342389567937, 0.7045813081895725, 0.9093159589724725, 0.6748809435823302, 0.5614330800633979, 0.6071937062184846, 0.9121228864331543, 0.7919641352916398, 0.19567517866589823, 0.9820047415219545, 0.5873036334639846, 0.8999651948366754, 0.30064170577030114, 0.6257366699625353, 0.8310069924335378, 0.5684096152471901, 0.5025595633825504, 0.6694217430745488]], "title": "Scatterplot Data", "names": ["x0"], "id": "t7c043802146145039659871098328e54", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
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
          var popup = document.querySelector("#t9dcc8ab05cc845d7874ec412a06d2daa .toyplot-mark-popup");
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


Of course, you have control over all the normal parameters of a
scatterplot, such as color and marker type:

.. code:: python

    timestamps = numpy.random.uniform(size=40)
    event_types = numpy.random.choice(2, size=timestamps.shape)

.. code:: python

    colormap = toyplot.color.CategoricalMap()
    
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.scatterplot(
        timestamps,
        color=(event_types, colormap),
        marker="|",
        size=15,
        mstyle={"stroke-width":1.5},
    );



.. raw:: html

    <div align="center" class="toyplot" id="teacde2383be24b71b676a42682225340"><svg height="100.0px" id="t678b1b7663d1434fb2036b1ddc058d0e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t9c386a9e010840b5b7856efe3f469b5f"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="t24d08712c7b945f4af676a92b1044be0" style="stroke:none" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 383.55831418973622, 0)" x1="383.55831418973622" x2="383.55831418973622" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 354.05768098880191, 0)" x1="354.05768098880191" x2="354.05768098880191" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 398.43359186259829, 0)" x1="398.43359186259829" x2="398.43359186259829" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 278.88041421372475, 0)" x1="278.88041421372475" x2="278.88041421372475" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 482.91826599606378, 0)" x1="482.91826599606378" x2="482.91826599606378" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 73.578449946498594, 0)" x1="73.578449946498594" x2="73.578449946498594" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 14.823500267707789, 0)" x1="14.823500267707789" x2="14.823500267707789" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 296.94674631238587, 0)" x1="296.94674631238587" x2="296.94674631238587" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 57.032849371331238, 0)" x1="57.032849371331238" x2="57.032849371331238" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 475.40492504206111, 0)" x1="475.40492504206111" x2="475.40492504206111" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 162.85370721267361, 0)" x1="162.85370721267361" x2="162.85370721267361" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 96.809345076888604, 0)" x1="96.809345076888604" x2="96.809345076888604" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 228.90582444871376, 0)" x1="228.90582444871376" x2="228.90582444871376" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 460.20128554654389, 0)" x1="460.20128554654389" x2="460.20128554654389" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 439.53458075733789, 0)" x1="439.53458075733789" x2="439.53458075733789" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 126.30787752326511, 0)" x1="126.30787752326511" x2="126.30787752326511" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 174.00439643467308, 0)" x1="174.00439643467308" x2="174.00439643467308" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 91.294365790154373, 0)" x1="91.294365790154373" x2="91.294365790154373" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 450.89802568549601, 0)" x1="450.89802568549601" x2="450.89802568549601" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 353.26408158589874, 0)" x1="353.26408158589874" x2="353.26408158589874" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 363.32923078107035, 0)" x1="363.32923078107035" x2="363.32923078107035" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 450.04391840485386, 0)" x1="450.04391840485386" x2="450.04391840485386" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 389.58190038466211, 0)" x1="389.58190038466211" x2="389.58190038466211" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 299.57739030214617, 0)" x1="299.57739030214617" x2="299.57739030214617" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 145.56262244893742, 0)" x1="145.56262244893742" x2="145.56262244893742" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 75.697632203716054, 0)" x1="75.697632203716054" x2="75.697632203716054" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 167.58732957471744, 0)" x1="167.58732957471744" x2="167.58732957471744" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 328.7758885789097, 0)" x1="328.7758885789097" x2="328.7758885789097" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 36.67127181630908, 0)" x1="36.67127181630908" x2="36.67127181630908" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 27.503197703111827, 0)" x1="27.503197703111827" x2="27.503197703111827" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 161.59740696058822, 0)" x1="161.59740696058822" x2="161.59740696058822" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 295.24090223149307, 0)" x1="295.24090223149307" x2="295.24090223149307" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 426.94928356282088, 0)" x1="426.94928356282088" x2="426.94928356282088" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 143.5312125000045, 0)" x1="143.5312125000045" x2="143.5312125000045" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 86.533613407396075, 0)" x1="86.533613407396075" x2="86.533613407396075" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 67.010602999421408, 0)" x1="67.010602999421408" x2="67.010602999421408" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 497.32691432214727, 0)" x1="497.32691432214727" x2="497.32691432214727" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 89.748934734695922, 0)" x1="89.748934734695922" x2="89.748934734695922" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 158.77341151359792, 0)" x1="158.77341151359792" x2="158.77341151359792" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 284.14570232955361, 0)" x1="284.14570232955361" x2="284.14570232955361" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-axes-Axis" id="t0b32b89733924cd1bd26c5a936f1a9bd" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="14.82350026770779" x2="497.3269143221473" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#teacde2383be24b71b676a42682225340 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#teacde2383be24b71b676a42682225340 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script><script>
    (function()
    {
      var data_tables = [{"data": [[0.7671166283794725, 0.7081153619776038, 0.7968671837251966, 0.5577608284274495, 0.9658365319921276, 0.14715689989299718, 0.02964700053541558, 0.5938934926247718, 0.11406569874266248, 0.9508098500841222, 0.32570741442534723, 0.1936186901537772, 0.45781164889742754, 0.9204025710930878, 0.8790691615146757, 0.2526157550465302, 0.34800879286934616, 0.18258873158030875, 0.9017960513709921, 0.7065281631717975, 0.7266584615621408, 0.9000878368097077, 0.7791638007693242, 0.5991547806042924, 0.29112524489787484, 0.15139526440743212, 0.3351746591494349, 0.6575517771578194, 0.07334254363261816, 0.05500639540622365, 0.32319481392117644, 0.5904818044629861, 0.8538985671256417, 0.287062425000009, 0.17306722681479214, 0.13402120599884282, 0.9946538286442945, 0.17949786946939184, 0.31754682302719583, 0.5682914046591072]], "title": "Scatterplot Data", "names": ["x0"], "id": "t24d08712c7b945f4af676a92b1044be0", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
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
          var popup = document.querySelector("#teacde2383be24b71b676a42682225340 .toyplot-mark-popup");
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


In addition to scatterplots, number lines can be used to display any
:class:`toyplot.color.Map`:

.. code:: python

    colormap = toyplot.color.diverging("BlueRed", domain_min=0, domain_max=1)
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.colormap(colormap, style={"stroke-width":1})



.. raw:: html

    <div align="center" class="toyplot" id="tcc7148fa1be44f6ab94db454cb2f1be8"><svg height="100.0px" id="t8e6ed26c0a044527bf23892699915003" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t9ef16c3581ab4f3ab88727f96196aa27"><g class="toyplot-coordinate-events"><g class="toyplot-color-Map" id="t526609719b704e68a52ab19d7f6a1e19" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><defs><linearGradient gradientUnits="userSpaceOnUse" id="taa70766feb3a4c249849019ee96fc210" x1="0.0" x2="500.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(33.5%,28.3%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(35.2%,31.2%,78.1%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(36.9%,34%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(38.6%,36.8%,82.8%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(40.3%,39.6%,84.9%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(42%,42.3%,86.9%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(43.8%,45%,88.8%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(45.5%,47.6%,90.6%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(47.3%,50.2%,92.2%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(49%,52.8%,93.7%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(50.8%,55.3%,95%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(52.6%,57.7%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(54.3%,60.1%,97.2%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(56.1%,62.4%,98.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(57.9%,64.6%,98.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(59.7%,66.7%,99.4%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(61.5%,68.8%,99.8%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(63.3%,70.7%,100%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(65.1%,72.6%,100%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(66.8%,74.3%,100%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(68.6%,76%,99.9%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(70.3%,77.6%,99.5%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(72.1%,79%,99%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.8%,80.3%,98.3%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(75.4%,81.5%,97.4%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(77.1%,82.6%,96.4%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(78.7%,83.6%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(80.2%,84.4%,94%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(81.7%,85.1%,92.6%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(83.2%,85.7%,91%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(84.6%,86.1%,89.3%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(85.9%,86.4%,87.5%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(87.3%,86.2%,85.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(88.7%,85.4%,83.2%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(90%,84.4%,80.8%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(91.1%,83.3%,78.5%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(92.2%,82.1%,76.1%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(93%,80.8%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(93.8%,79.3%,71.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(94.4%,77.7%,68.7%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(94.8%,76%,66.2%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(95.2%,74.2%,63.7%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(95.4%,72.3%,61.2%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(95.4%,70.2%,58.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.3%,68.1%,56.2%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(95.1%,65.8%,53.7%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(94.8%,63.5%,51.3%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(94.3%,61%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(93.6%,58.5%,46.4%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(92.9%,55.9%,44%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(92%,53.1%,41.6%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(91%,50.3%,39.3%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(89.8%,47.4%,37%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(88.5%,44.5%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(87.1%,41.4%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(85.6%,38.2%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(84%,34.9%,28.4%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(82.2%,31.5%,26.3%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(80.3%,28%,24.4%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(78.4%,24.2%,22.5%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(76.3%,20.1%,20.6%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(74.1%,15.5%,18.8%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(71.8%,9.83%,17.1%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(69.5%,0.296%,15.5%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#taa70766feb3a4c249849019ee96fc210);stroke:none;stroke-width:1" width="500.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-axes-Axis" id="t816499da7252443d8d6a28b397747767" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tcc7148fa1be44f6ab94db454cb2f1be8 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tcc7148fa1be44f6ab94db454cb2f1be8 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script></div></div>


Keep in mind that to display most color maps on a number line, you
*must* specify their domain (otherwise, there would be no way to map the
colors to coordinates on the axis). You can see above that we specified
:math:`[0, 1]` as the domain.

:class:`toyplot.color.CategoricalMap` is the one exception to this
rule, since it has an implicit :math:`[0, N)` domain where :math:`N` is
the number of colors in the map:

.. code:: python

    colormap = toyplot.color.CategoricalMap(toyplot.color.brewer("Set1"))
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.colormap(colormap)



.. raw:: html

    <div align="center" class="toyplot" id="tad397fc4bbcc41a98d50fd034b03dbc4"><svg height="100.0px" id="t1d7e30053e474af2aa69875703f360df" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t739399d1a0b74500bce0e6a3e514f6f6"><g class="toyplot-coordinate-events"><g class="toyplot-color-CategoricalMap" id="tb780bf26a0b14415b32c9317703d6aaf" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><rect height="10" style="fill:rgb(89.4%,10.2%,11%);fill-opacity:1.0;stroke:none" width="62.5" x="0.0" y="-5.0"></rect><rect height="10" style="fill:rgb(21.6%,49.4%,72.2%);fill-opacity:1.0;stroke:none" width="62.5" x="62.5" y="-5.0"></rect><rect height="10" style="fill:rgb(30.2%,68.6%,29%);fill-opacity:1.0;stroke:none" width="62.5" x="125.0" y="-5.0"></rect><rect height="10" style="fill:rgb(59.6%,30.6%,63.9%);fill-opacity:1.0;stroke:none" width="62.5" x="187.5" y="-5.0"></rect><rect height="10" style="fill:rgb(100%,49.8%,0%);fill-opacity:1.0;stroke:none" width="62.5" x="250.0" y="-5.0"></rect><rect height="10" style="fill:rgb(100%,100%,20%);fill-opacity:1.0;stroke:none" width="62.5" x="312.5" y="-5.0"></rect><rect height="10" style="fill:rgb(65.1%,33.7%,15.7%);fill-opacity:1.0;stroke:none" width="62.5" x="375.0" y="-5.0"></rect><rect height="10" style="fill:rgb(96.9%,50.6%,74.9%);fill-opacity:1.0;stroke:none" width="62.5" x="437.5" y="-5.0"></rect><rect height="10" style="fill:none;stroke:none;stroke-width:1.0" width="500.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-axes-Axis" id="t06e3b89196934cad80e36014eb506d18" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(166.66666666666666,0) rotate(0)" x="0" y="0">3</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(333.3333333333333,0) rotate(0)" x="0" y="0">6</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">9</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tad397fc4bbcc41a98d50fd034b03dbc4 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tad397fc4bbcc41a98d50fd034b03dbc4 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script></div></div>


Note that, unlike a scatterplot, a color map has a width that can be
varied:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.colormap(colormap, width=20)



.. raw:: html

    <div align="center" class="toyplot" id="tf371206226b54693bfe34b284606e4d1"><svg height="100.0px" id="tb3cf72d5d02a42058af1f33b454b94aa" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t594d804540cc4a739e35d3c35e572984"><g class="toyplot-coordinate-events"><g class="toyplot-color-CategoricalMap" id="t75d15ab6aadc40a2ba9812420b975391" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><rect height="20" style="fill:rgb(89.4%,10.2%,11%);fill-opacity:1.0;stroke:none" width="62.5" x="0.0" y="-10.0"></rect><rect height="20" style="fill:rgb(21.6%,49.4%,72.2%);fill-opacity:1.0;stroke:none" width="62.5" x="62.5" y="-10.0"></rect><rect height="20" style="fill:rgb(30.2%,68.6%,29%);fill-opacity:1.0;stroke:none" width="62.5" x="125.0" y="-10.0"></rect><rect height="20" style="fill:rgb(59.6%,30.6%,63.9%);fill-opacity:1.0;stroke:none" width="62.5" x="187.5" y="-10.0"></rect><rect height="20" style="fill:rgb(100%,49.8%,0%);fill-opacity:1.0;stroke:none" width="62.5" x="250.0" y="-10.0"></rect><rect height="20" style="fill:rgb(100%,100%,20%);fill-opacity:1.0;stroke:none" width="62.5" x="312.5" y="-10.0"></rect><rect height="20" style="fill:rgb(65.1%,33.7%,15.7%);fill-opacity:1.0;stroke:none" width="62.5" x="375.0" y="-10.0"></rect><rect height="20" style="fill:rgb(96.9%,50.6%,74.9%);fill-opacity:1.0;stroke:none" width="62.5" x="437.5" y="-10.0"></rect><rect height="20" style="fill:none;stroke:none;stroke-width:1.0" width="500.0" x="0.0" y="-10.0"></rect></g></g><g class="toyplot-axes-Axis" id="tfabdc8a672834ef4b67ff060fd1468e9" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(166.66666666666666,0) rotate(0)" x="0" y="0">3</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(333.3333333333333,0) rotate(0)" x="0" y="0">6</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">9</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tf371206226b54693bfe34b284606e4d1 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tf371206226b54693bfe34b284606e4d1 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script></div></div>


Also note that some colors may tend to blend-in with the canvas
background:

.. code:: python

    colormap = toyplot.color.LinearMap(toyplot.color.brewer("Greys"), domain_min=0, domain_max=1)
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.colormap(colormap)



.. raw:: html

    <div align="center" class="toyplot" id="t35612e29975e4488a8a0a61cb75dea6b"><svg height="100.0px" id="td06c2d7edd7e42908e9c5dafcefaeab1" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t507f31d25f394cd49f209ffe6ac8f1ca"><g class="toyplot-coordinate-events"><g class="toyplot-color-Map" id="t936f65048cfd465bb6141882da4ebb1b" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tdc1fb1c6df6f427b997172682aefcb0c" x1="0.0" x2="500.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(0%,0%,0%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(1.84%,1.84%,1.84%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(3.69%,3.69%,3.69%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(5.53%,5.53%,5.53%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(7.37%,7.37%,7.37%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(9.21%,9.21%,9.21%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(11.1%,11.1%,11.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(12.9%,12.9%,12.9%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(14.8%,14.8%,14.8%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(17%,17%,17%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(19.3%,19.3%,19.3%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(21.5%,21.5%,21.5%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(23.8%,23.8%,23.8%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(26%,26%,26%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(28.2%,28.2%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(30.5%,30.5%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(32.6%,32.6%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(34.2%,34.2%,34.2%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(35.9%,35.9%,35.9%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(37.5%,37.5%,37.5%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(39.1%,39.1%,39.1%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(40.8%,40.8%,40.8%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(42.4%,42.4%,42.4%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(44.1%,44.1%,44.1%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(45.8%,45.8%,45.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(47.5%,47.5%,47.5%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(49.2%,49.2%,49.2%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(51%,51%,51%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(52.7%,52.7%,52.7%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(54.5%,54.5%,54.5%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(56.2%,56.2%,56.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(58%,58%,58%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(59.8%,59.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(61.7%,61.7%,61.7%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(63.7%,63.7%,63.7%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(65.6%,65.6%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(67.6%,67.6%,67.6%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(69.5%,69.5%,69.5%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(71.4%,71.4%,71.4%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(73.4%,73.4%,73.4%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(75%,75%,75%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(76.4%,76.4%,76.4%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(77.8%,77.8%,77.8%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(79.2%,79.2%,79.2%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(80.6%,80.6%,80.6%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(82%,82%,82%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(83.4%,83.4%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(84.7%,84.7%,84.7%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(86%,86%,86%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(87.1%,87.1%,87.1%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(88.2%,88.2%,88.2%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(89.4%,89.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(90.5%,90.5%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(91.7%,91.7%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(92.8%,92.8%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(94%,94%,94%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(94.8%,94.8%,94.8%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(95.5%,95.5%,95.5%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(96.3%,96.3%,96.3%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(97%,97%,97%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(97.8%,97.8%,97.8%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(98.5%,98.5%,98.5%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(99.3%,99.3%,99.3%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(100%,100%,100%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tdc1fb1c6df6f427b997172682aefcb0c);stroke:none;stroke-width:1.0" width="500.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-axes-Axis" id="t0a9892f33c6b45f8b24b84dfed1533c3" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t35612e29975e4488a8a0a61cb75dea6b text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t35612e29975e4488a8a0a61cb75dea6b text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script></div></div>


To make the color map stand out from the background, you can use the
``style`` parameter to add a border:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.colormap(colormap, style={"stroke":"lightgrey"})



.. raw:: html

    <div align="center" class="toyplot" id="t8271cd745c454638982daf6f06534988"><svg height="100.0px" id="t6f158ab8b1294e61acad41c2b4a977ad" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t2e4a9362144448059a0c7d91d4b44853"><g class="toyplot-coordinate-events"><g class="toyplot-color-Map" id="tfb072e0212a2474f80f314ec9777f326" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><defs><linearGradient gradientUnits="userSpaceOnUse" id="td925f2adfe4f4a71aed6aadf937eb693" x1="0.0" x2="500.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(0%,0%,0%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(1.84%,1.84%,1.84%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(3.69%,3.69%,3.69%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(5.53%,5.53%,5.53%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(7.37%,7.37%,7.37%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(9.21%,9.21%,9.21%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(11.1%,11.1%,11.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(12.9%,12.9%,12.9%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(14.8%,14.8%,14.8%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(17%,17%,17%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(19.3%,19.3%,19.3%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(21.5%,21.5%,21.5%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(23.8%,23.8%,23.8%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(26%,26%,26%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(28.2%,28.2%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(30.5%,30.5%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(32.6%,32.6%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(34.2%,34.2%,34.2%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(35.9%,35.9%,35.9%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(37.5%,37.5%,37.5%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(39.1%,39.1%,39.1%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(40.8%,40.8%,40.8%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(42.4%,42.4%,42.4%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(44.1%,44.1%,44.1%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(45.8%,45.8%,45.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(47.5%,47.5%,47.5%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(49.2%,49.2%,49.2%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(51%,51%,51%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(52.7%,52.7%,52.7%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(54.5%,54.5%,54.5%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(56.2%,56.2%,56.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(58%,58%,58%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(59.8%,59.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(61.7%,61.7%,61.7%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(63.7%,63.7%,63.7%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(65.6%,65.6%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(67.6%,67.6%,67.6%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(69.5%,69.5%,69.5%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(71.4%,71.4%,71.4%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(73.4%,73.4%,73.4%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(75%,75%,75%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(76.4%,76.4%,76.4%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(77.8%,77.8%,77.8%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(79.2%,79.2%,79.2%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(80.6%,80.6%,80.6%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(82%,82%,82%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(83.4%,83.4%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(84.7%,84.7%,84.7%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(86%,86%,86%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(87.1%,87.1%,87.1%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(88.2%,88.2%,88.2%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(89.4%,89.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(90.5%,90.5%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(91.7%,91.7%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(92.8%,92.8%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(94%,94%,94%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(94.8%,94.8%,94.8%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(95.5%,95.5%,95.5%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(96.3%,96.3%,96.3%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(97%,97%,97%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(97.8%,97.8%,97.8%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(98.5%,98.5%,98.5%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(99.3%,99.3%,99.3%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(100%,100%,100%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#td925f2adfe4f4a71aed6aadf937eb693);stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0" width="500.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-axes-Axis" id="tc1207565ebe0408d8feac6b910eae4f8" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t8271cd745c454638982daf6f06534988 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t8271cd745c454638982daf6f06534988 text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script></div></div>


Functions like :meth:`toyplot.axes.Cartesian.color_scale`,
:meth:`toyplot.canvas.Canvas.color_scale`, and
:meth:`toyplot.canvas.Canvas.matrix` use number lines to conveniently
add color scales to visualizations, but by creating a number line object
of your own, you can create more complex scales. For example, you could
define a multi-range scale, or add marks to highlight critical values:

.. code:: python

    colormap1 = toyplot.color.diverging("BlueRed", domain_min=-1, domain_max=1)
    colormap2 = toyplot.color.diverging("PurpleGreen", domain_min=-0.5, domain_max=1.5)
    
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline(spacing=15, padding=10)
    numberline.colormap(colormap1)
    numberline.colormap(colormap2)
    numberline.scatterplot([0], marker="d", color="black");



.. raw:: html

    <div align="center" class="toyplot" id="td1e38c8a854c498191e4c7984a33e70a"><svg height="100.0px" id="t8959b8b9cacf47c9bbe1fc3a783e07f5" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="tc84a140a87f4494991b33523092e74f8"><g class="toyplot-coordinate-events"><g class="toyplot-color-Map" id="t79667964d5f7491d9d1e776d00c57986" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><defs><linearGradient gradientUnits="userSpaceOnUse" id="taf6a1b0b4a3b4d72adf58fb7b6ec470f" x1="0.0" x2="400.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(33.5%,28.3%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(35.2%,31.2%,78.1%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(36.9%,34%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(38.6%,36.8%,82.8%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(40.3%,39.6%,84.9%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(42%,42.3%,86.9%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(43.8%,45%,88.8%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(45.5%,47.6%,90.6%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(47.3%,50.2%,92.2%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(49%,52.8%,93.7%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(50.8%,55.3%,95%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(52.6%,57.7%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(54.3%,60.1%,97.2%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(56.1%,62.4%,98.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(57.9%,64.6%,98.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(59.7%,66.7%,99.4%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(61.5%,68.8%,99.8%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(63.3%,70.7%,100%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(65.1%,72.6%,100%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(66.8%,74.3%,100%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(68.6%,76%,99.9%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(70.3%,77.6%,99.5%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(72.1%,79%,99%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.8%,80.3%,98.3%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(75.4%,81.5%,97.4%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(77.1%,82.6%,96.4%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(78.7%,83.6%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(80.2%,84.4%,94%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(81.7%,85.1%,92.6%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(83.2%,85.7%,91%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(84.6%,86.1%,89.3%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(85.9%,86.4%,87.5%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(87.3%,86.2%,85.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(88.7%,85.4%,83.2%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(90%,84.4%,80.8%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(91.1%,83.3%,78.5%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(92.2%,82.1%,76.1%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(93%,80.8%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(93.8%,79.3%,71.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(94.4%,77.7%,68.7%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(94.8%,76%,66.2%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(95.2%,74.2%,63.7%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(95.4%,72.3%,61.2%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(95.4%,70.2%,58.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.3%,68.1%,56.2%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(95.1%,65.8%,53.7%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(94.8%,63.5%,51.3%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(94.3%,61%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(93.6%,58.5%,46.4%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(92.9%,55.9%,44%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(92%,53.1%,41.6%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(91%,50.3%,39.3%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(89.8%,47.4%,37%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(88.5%,44.5%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(87.1%,41.4%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(85.6%,38.2%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(84%,34.9%,28.4%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(82.2%,31.5%,26.3%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(80.3%,28%,24.4%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(78.4%,24.2%,22.5%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(76.3%,20.1%,20.6%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(74.1%,15.5%,18.8%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(71.8%,9.83%,17.1%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(69.5%,0.296%,15.5%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#taf6a1b0b4a3b4d72adf58fb7b6ec470f);stroke:none;stroke-width:1.0" width="400.0" x="0.0" y="-5.0"></rect></g><g class="toyplot-color-Map" id="tff13118cd7ba413a9a421c531352467a" transform="translate(50.0,50.0) rotate(0.0) translate(0,-15.0)"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t47632583f47d4116b2cbe6edfc821c6e" x1="100.0" x2="500.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(46.7%,29.8%,63.3%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(47.4%,32.3%,65.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(48.1%,34.7%,68%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(48.7%,37.1%,70.2%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(49.3%,39.4%,72.3%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(50%,41.8%,74.3%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(50.6%,44.2%,76.3%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(51.3%,46.5%,78.1%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(52%,48.8%,79.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(52.7%,51.1%,81.5%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(53.4%,53.3%,83%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(54.2%,55.5%,84.4%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(55.1%,57.7%,85.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(56%,59.8%,86.8%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(57%,61.9%,87.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(58.1%,64%,88.7%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(59.3%,65.9%,89.5%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(60.5%,67.9%,90.1%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(61.8%,69.7%,90.6%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(63.2%,71.5%,91%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(64.7%,73.2%,91.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(66.3%,74.9%,91.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(67.9%,76.4%,91.4%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(69.6%,77.9%,91.3%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(71.4%,79.3%,91.1%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(73.3%,80.6%,90.8%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(75.2%,81.8%,90.4%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(77.2%,82.9%,89.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(79.2%,83.9%,89.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(81.3%,84.8%,88.6%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(83.4%,85.6%,87.8%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(85.5%,86.3%,87%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(85.4%,86.6%,86.3%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(83.1%,86.8%,85.7%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(80.8%,86.9%,84.9%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(78.3%,86.8%,84%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(75.9%,86.7%,83%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(73.4%,86.4%,81.8%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(70.9%,86.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(68.3%,85.7%,79.1%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(65.7%,85.2%,77.5%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(63.1%,84.6%,75.9%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(60.4%,83.9%,74.1%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(57.8%,83.2%,72.2%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(55.1%,82.3%,70.2%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(52.4%,81.4%,68.1%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(49.7%,80.4%,66%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(47%,79.3%,63.7%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(44.3%,78.1%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(41.7%,76.9%,58.9%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(39%,75.6%,56.4%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(36.3%,74.2%,53.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(33.6%,72.8%,51.3%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(30.8%,71.3%,48.6%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(28.1%,69.7%,45.9%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(25.4%,68.1%,43.1%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(22.6%,66.5%,40.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(19.7%,64.7%,37.4%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(16.7%,63%,34.5%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(13.5%,61.2%,31.6%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(9.85%,59.3%,28.6%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(5.29%,57.5%,25.6%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(0%,55.5%,22.5%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(0%,53.6%,19.3%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t47632583f47d4116b2cbe6edfc821c6e);stroke:none;stroke-width:1.0" width="400.0" x="100.0" y="-5.0"></rect></g><g class="toyplot-mark-Scatterplot" id="tad204b94f41b435c97ab4914060af156" style="stroke:none" transform="translate(50.0,50.0) rotate(0.0) translate(0,-30.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><rect height="4.0" transform="rotate(-45, 200.0, 0)" width="4.0" x="198.0" y="-2.0"></rect></g></g></g></g><g class="toyplot-axes-Axis" id="td5d5a8cea8a14c4ba4e638d1339e1d13" transform="translate(50.0,50.0) rotate(0.0) translate(0,10.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">-1.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,0) rotate(0)" x="0" y="0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,0) rotate(0)" x="0" y="0">1.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.5</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#td1e38c8a854c498191e4c7984a33e70a text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#td1e38c8a854c498191e4c7984a33e70a text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script><script>
    (function()
    {
      var data_tables = [{"data": [[0.0]], "title": "Scatterplot Data", "names": ["x0"], "id": "tad204b94f41b435c97ab4914060af156", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
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
          var popup = document.querySelector("#td1e38c8a854c498191e4c7984a33e70a .toyplot-mark-popup");
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


Properties
----------

Number line objects contain sets of nested properties that can be used
to adjust their behavior. The list of available properties includes the
following:

-  numberline.show - set to *False* to hide the numberline completely
   (the plotted data will still be visible).
-  numberline.spacing - the space between each mark added to the
   numberline. Defaults to CSS pixels, supports all :ref:`units`.
-  numberline.padding - the space between the axis spine and the first
   mark. Defaults to the same value as ``spacing``. Uses CSS pixels as
   the default unit, supports all :ref:`units`.
-  numberline.axis.show - set to *False* to hide the axis completely.
-  numberline.axis.scale - "linear", "log" (base 10), "log10", "log2",
   or a ("log", base) tuple. See :ref:`log-scales` for details.
-  numberline.axis.domain.min - override the minimum domain value for
   the axis.
-  numberline.axis.domain.max - override the maximum domain value for
   the axis.
-  numberline.axis.label.text - optional label below the axis.
-  numberline.axis.label.style - styles the axis label.
-  numberline.axis.spine.show - set to *False* to hide the axis spine.
-  numberline.axis.spine.style - styles the axis spine.
-  numberline.axis.ticks.show - set to *True* to display axis tick
   marks.
-  numberline.axis.ticks.locator - assign an instance of
   :py:class:`toyplot.locator.TickLocator` to control the positioning
   and formatting of ticks and tick labels. By default, an appropriate
   locator is automatically chosen based on the axis scale and domain.
   See :ref:`tick-locators` for details.
-  numberline.axis.ticks.above - length of axis ticks above the axis.
   Defaults to CSS pixels, supports all :ref:`units`.
-  numberline.axis.ticks.below - length of axis ticks below the axis.
   Defaults to CSS pixels, supports all :ref:`units`.
-  numberline.axis.ticks.style - styles the axis ticks.
-  numberline.axis.ticks.labels.show - set to *False* to hide axis tick
   labels.
-  numberline.axis.ticks.labels.angle - set the angle of axis tick
   labels in degrees.
-  numberline.axis.ticks.labels.offset - offsets labels from the axis.
   Defaults to CSS pixels, supports all :ref:`units`.
-  numberline.axis.ticks.labels.style - style axis tick label text.

As a convenience, some of the most common properties can also be set
when the numberline is created.

Layout
------

Unlike cartesian or table axes that are defined over an area of the
canvas, number lines are defined by two endpoints in canvas coordinates.
When you use :ref:`canvas-layout` functions, you create number lines
that are horizontal and centered within the bounds of the area you
define:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200, style={"border":"1px solid lightgray"})
    
    numberline = canvas.numberline(grid=(2, 1, 0))
    numberline.scatterplot(numpy.linspace(0, 1))
    
    numberline = canvas.numberline(grid=(2, 1, 1))
    numberline.scatterplot(numpy.linspace(0, 1));



.. raw:: html

    <div align="center" class="toyplot" id="t5d19271afa2d4b4bb7a6f5b5f54840de"><svg height="200.0px" id="t1606eae3fea0407b86589bcfd1e04d5a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border:1px solid lightgray;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t96ce135690274fafa39ecb058f7206f3"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="tac2b7dd62bbb4c5d8ae004502a05d16d" style="stroke:none" transform="translate(50.0,50.0) rotate(0.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="0.0" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="10.204081632653061" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.408163265306122" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="30.612244897959183" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="40.816326530612244" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="51.020408163265301" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.224489795918366" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="71.428571428571431" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="81.632653061224488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.836734693877546" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="102.0408163265306" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.24489795918366" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="122.44897959183673" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="132.65306122448979" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.85714285714286" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="153.0612244897959" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="163.26530612244898" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="173.46938775510205" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="183.67346938775509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="193.87755102040816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="204.08163265306121" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="214.28571428571428" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="224.48979591836732" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="234.69387755102039" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="244.89795918367346" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="255.10204081632654" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.30612244897958" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="275.51020408163265" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="285.71428571428572" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="295.91836734693879" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.12244897959181" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.32653061224488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="326.53061224489795" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="336.73469387755102" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="346.9387755102041" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="357.14285714285711" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="367.34693877551018" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="377.55102040816325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="387.75510204081633" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="397.95918367346934" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="408.16326530612241" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="418.36734693877548" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="428.57142857142856" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="438.77551020408163" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="448.97959183673464" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="459.18367346938771" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="469.38775510204079" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.59183673469386" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="489.79591836734693" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-axes-Axis" id="t216a6ec5513045268d570ce70f6c5afa" transform="translate(50.0,50.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g><g class="toyplot-axes-NumberLine" id="t3dbdc3a7a2c7445c91ef878903af7e91"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="te901ac51514d48dbb486c94e62d3bc47" style="stroke:none" transform="translate(50.0,150.0) rotate(0.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="0.0" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="10.204081632653061" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.408163265306122" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="30.612244897959183" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="40.816326530612244" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="51.020408163265301" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.224489795918366" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="71.428571428571431" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="81.632653061224488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.836734693877546" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="102.0408163265306" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.24489795918366" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="122.44897959183673" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="132.65306122448979" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.85714285714286" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="153.0612244897959" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="163.26530612244898" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="173.46938775510205" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="183.67346938775509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="193.87755102040816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="204.08163265306121" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="214.28571428571428" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="224.48979591836732" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="234.69387755102039" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="244.89795918367346" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="255.10204081632654" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.30612244897958" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="275.51020408163265" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="285.71428571428572" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="295.91836734693879" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.12244897959181" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.32653061224488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="326.53061224489795" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="336.73469387755102" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="346.9387755102041" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="357.14285714285711" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="367.34693877551018" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="377.55102040816325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="387.75510204081633" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="397.95918367346934" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="408.16326530612241" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="418.36734693877548" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="428.57142857142856" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="438.77551020408163" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="448.97959183673464" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="459.18367346938771" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="469.38775510204079" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.59183673469386" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="489.79591836734693" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-axes-Axis" id="tc4daa022a66d49f99490e04666855fd6" transform="translate(50.0,150.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t5d19271afa2d4b4bb7a6f5b5f54840de text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t5d19271afa2d4b4bb7a6f5b5f54840de text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script><script>
    (function()
    {
      var data_tables = [{"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "title": "Scatterplot Data", "names": ["x0"], "id": "tac2b7dd62bbb4c5d8ae004502a05d16d", "filename": "toyplot"}, {"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "title": "Scatterplot Data", "names": ["x0"], "id": "te901ac51514d48dbb486c94e62d3bc47", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
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
          var popup = document.querySelector("#t5d19271afa2d4b4bb7a6f5b5f54840de .toyplot-mark-popup");
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


If you look carefully at the above plot, you will see that the *data* is
centered within each cell in the :math:`2 \times 1` grid defined by the
layout.

However, you can also specify the endpoints of a number line explicitly,
which allows you to create number lines in any orientation including
diagonal:

.. code:: python

    canvas = toyplot.Canvas(width=600, style={"border":"1px solid lightgray"})
    
    numberline = canvas.numberline(x1=-50, x2=50, y1=100, y2=100, label="Right to left")
    numberline.scatterplot(numpy.linspace(0, 1), marker="|", size=15)
    
    numberline = canvas.numberline(x1=50, x2=-50, y1=150, y2=150, label="Left to right")
    numberline.scatterplot(numpy.linspace(0, 1), marker="|", size=15)
    
    numberline = canvas.numberline(x1=100, x2=100, y1=250, y2=-50, label="Top to bottom")
    numberline.scatterplot(numpy.linspace(0, 1), marker="|", size=15)
    
    numberline = canvas.numberline(x1=150, x2=150, y1=-50, y2=250, label="Bottom to top")
    numberline.scatterplot(numpy.linspace(0, 1), marker="|", size=15)
    
    numberline = canvas.numberline(x1=250, x2=-50, y1=-50, y2=250, label="Diagonal")
    numberline.scatterplot(numpy.linspace(0, 1), marker="|", size=15);



.. raw:: html

    <div align="center" class="toyplot" id="t4605f4c19f0f48e1b4084e1b6919a6bc"><svg height="600.0px" id="td0e57f3d991c4753a158d9eb3cca5d4f" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border:1px solid lightgray;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 600.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-NumberLine" id="t5ab889c79116444895af76241c9a308f"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="t9b18db6afe8447d29a26ca2d5802a431" style="stroke:none" transform="translate(550.0,100.0) rotate(180.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 0.0, 0)" x1="0.0" x2="0.0" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 10.204081632653061, 0)" x1="10.204081632653061" x2="10.204081632653061" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 20.408163265306122, 0)" x1="20.408163265306122" x2="20.408163265306122" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 30.612244897959183, 0)" x1="30.612244897959183" x2="30.612244897959183" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 40.816326530612244, 0)" x1="40.816326530612244" x2="40.816326530612244" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 51.020408163265301, 0)" x1="51.020408163265301" x2="51.020408163265301" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 61.224489795918366, 0)" x1="61.224489795918366" x2="61.224489795918366" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 71.428571428571431, 0)" x1="71.428571428571431" x2="71.428571428571431" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 81.632653061224488, 0)" x1="81.632653061224488" x2="81.632653061224488" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 91.836734693877546, 0)" x1="91.836734693877546" x2="91.836734693877546" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 102.0408163265306, 0)" x1="102.0408163265306" x2="102.0408163265306" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 112.24489795918366, 0)" x1="112.24489795918366" x2="112.24489795918366" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 122.44897959183673, 0)" x1="122.44897959183673" x2="122.44897959183673" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 132.65306122448979, 0)" x1="132.65306122448979" x2="132.65306122448979" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 142.85714285714286, 0)" x1="142.85714285714286" x2="142.85714285714286" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 153.0612244897959, 0)" x1="153.0612244897959" x2="153.0612244897959" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 163.26530612244898, 0)" x1="163.26530612244898" x2="163.26530612244898" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 173.46938775510205, 0)" x1="173.46938775510205" x2="173.46938775510205" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 183.67346938775509, 0)" x1="183.67346938775509" x2="183.67346938775509" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 193.87755102040816, 0)" x1="193.87755102040816" x2="193.87755102040816" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 204.08163265306121, 0)" x1="204.08163265306121" x2="204.08163265306121" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 214.28571428571428, 0)" x1="214.28571428571428" x2="214.28571428571428" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 224.48979591836732, 0)" x1="224.48979591836732" x2="224.48979591836732" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 234.69387755102039, 0)" x1="234.69387755102039" x2="234.69387755102039" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 244.89795918367346, 0)" x1="244.89795918367346" x2="244.89795918367346" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 255.10204081632654, 0)" x1="255.10204081632654" x2="255.10204081632654" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 265.30612244897958, 0)" x1="265.30612244897958" x2="265.30612244897958" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 275.51020408163265, 0)" x1="275.51020408163265" x2="275.51020408163265" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 285.71428571428572, 0)" x1="285.71428571428572" x2="285.71428571428572" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 295.91836734693879, 0)" x1="295.91836734693879" x2="295.91836734693879" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 306.12244897959181, 0)" x1="306.12244897959181" x2="306.12244897959181" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 316.32653061224488, 0)" x1="316.32653061224488" x2="316.32653061224488" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 326.53061224489795, 0)" x1="326.53061224489795" x2="326.53061224489795" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 336.73469387755102, 0)" x1="336.73469387755102" x2="336.73469387755102" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 346.9387755102041, 0)" x1="346.9387755102041" x2="346.9387755102041" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 357.14285714285711, 0)" x1="357.14285714285711" x2="357.14285714285711" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 367.34693877551018, 0)" x1="367.34693877551018" x2="367.34693877551018" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 377.55102040816325, 0)" x1="377.55102040816325" x2="377.55102040816325" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 387.75510204081633, 0)" x1="387.75510204081633" x2="387.75510204081633" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 397.95918367346934, 0)" x1="397.95918367346934" x2="397.95918367346934" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 408.16326530612241, 0)" x1="408.16326530612241" x2="408.16326530612241" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 418.36734693877548, 0)" x1="418.36734693877548" x2="418.36734693877548" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 428.57142857142856, 0)" x1="428.57142857142856" x2="428.57142857142856" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 438.77551020408163, 0)" x1="438.77551020408163" x2="438.77551020408163" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 448.97959183673464, 0)" x1="448.97959183673464" x2="448.97959183673464" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 459.18367346938771, 0)" x1="459.18367346938771" x2="459.18367346938771" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 469.38775510204079, 0)" x1="469.38775510204079" x2="469.38775510204079" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 479.59183673469386, 0)" x1="479.59183673469386" x2="479.59183673469386" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 489.79591836734693, 0)" x1="489.79591836734693" x2="489.79591836734693" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 500.0, 0)" x1="500.0" x2="500.0" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-axes-Axis" id="t1bd0b1d4f4154d9eb46d0a7c452ca94a" transform="translate(550.0,100.0) rotate(180.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="250.0" y="0">Right to left</text></g></g><g class="toyplot-axes-NumberLine" id="tdb2c78aeaf104d1c8a8b4ac509fc5993"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="tb15ae97d4ec746338ad0ec72d1fb8f5c" style="stroke:none" transform="translate(50.0,150.0) rotate(0.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 0.0, 0)" x1="0.0" x2="0.0" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 10.204081632653061, 0)" x1="10.204081632653061" x2="10.204081632653061" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 20.408163265306122, 0)" x1="20.408163265306122" x2="20.408163265306122" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 30.612244897959183, 0)" x1="30.612244897959183" x2="30.612244897959183" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 40.816326530612244, 0)" x1="40.816326530612244" x2="40.816326530612244" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 51.020408163265301, 0)" x1="51.020408163265301" x2="51.020408163265301" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 61.224489795918366, 0)" x1="61.224489795918366" x2="61.224489795918366" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 71.428571428571431, 0)" x1="71.428571428571431" x2="71.428571428571431" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 81.632653061224488, 0)" x1="81.632653061224488" x2="81.632653061224488" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 91.836734693877546, 0)" x1="91.836734693877546" x2="91.836734693877546" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 102.0408163265306, 0)" x1="102.0408163265306" x2="102.0408163265306" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 112.24489795918366, 0)" x1="112.24489795918366" x2="112.24489795918366" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 122.44897959183673, 0)" x1="122.44897959183673" x2="122.44897959183673" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 132.65306122448979, 0)" x1="132.65306122448979" x2="132.65306122448979" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 142.85714285714286, 0)" x1="142.85714285714286" x2="142.85714285714286" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 153.0612244897959, 0)" x1="153.0612244897959" x2="153.0612244897959" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 163.26530612244898, 0)" x1="163.26530612244898" x2="163.26530612244898" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 173.46938775510205, 0)" x1="173.46938775510205" x2="173.46938775510205" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 183.67346938775509, 0)" x1="183.67346938775509" x2="183.67346938775509" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 193.87755102040816, 0)" x1="193.87755102040816" x2="193.87755102040816" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 204.08163265306121, 0)" x1="204.08163265306121" x2="204.08163265306121" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 214.28571428571428, 0)" x1="214.28571428571428" x2="214.28571428571428" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 224.48979591836732, 0)" x1="224.48979591836732" x2="224.48979591836732" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 234.69387755102039, 0)" x1="234.69387755102039" x2="234.69387755102039" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 244.89795918367346, 0)" x1="244.89795918367346" x2="244.89795918367346" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 255.10204081632654, 0)" x1="255.10204081632654" x2="255.10204081632654" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 265.30612244897958, 0)" x1="265.30612244897958" x2="265.30612244897958" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 275.51020408163265, 0)" x1="275.51020408163265" x2="275.51020408163265" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 285.71428571428572, 0)" x1="285.71428571428572" x2="285.71428571428572" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 295.91836734693879, 0)" x1="295.91836734693879" x2="295.91836734693879" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 306.12244897959181, 0)" x1="306.12244897959181" x2="306.12244897959181" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 316.32653061224488, 0)" x1="316.32653061224488" x2="316.32653061224488" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 326.53061224489795, 0)" x1="326.53061224489795" x2="326.53061224489795" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 336.73469387755102, 0)" x1="336.73469387755102" x2="336.73469387755102" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 346.9387755102041, 0)" x1="346.9387755102041" x2="346.9387755102041" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 357.14285714285711, 0)" x1="357.14285714285711" x2="357.14285714285711" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 367.34693877551018, 0)" x1="367.34693877551018" x2="367.34693877551018" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 377.55102040816325, 0)" x1="377.55102040816325" x2="377.55102040816325" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 387.75510204081633, 0)" x1="387.75510204081633" x2="387.75510204081633" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 397.95918367346934, 0)" x1="397.95918367346934" x2="397.95918367346934" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 408.16326530612241, 0)" x1="408.16326530612241" x2="408.16326530612241" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 418.36734693877548, 0)" x1="418.36734693877548" x2="418.36734693877548" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 428.57142857142856, 0)" x1="428.57142857142856" x2="428.57142857142856" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 438.77551020408163, 0)" x1="438.77551020408163" x2="438.77551020408163" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 448.97959183673464, 0)" x1="448.97959183673464" x2="448.97959183673464" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 459.18367346938771, 0)" x1="459.18367346938771" x2="459.18367346938771" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 469.38775510204079, 0)" x1="469.38775510204079" x2="469.38775510204079" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 479.59183673469386, 0)" x1="479.59183673469386" x2="479.59183673469386" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 489.79591836734693, 0)" x1="489.79591836734693" x2="489.79591836734693" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 500.0, 0)" x1="500.0" x2="500.0" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-axes-Axis" id="tce70148412834ee99edfaac712f5b803" transform="translate(50.0,150.0) rotate(0.0) translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,0) rotate(0)" x="0" y="0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="250.0" y="0">Left to right</text></g></g><g class="toyplot-axes-NumberLine" id="tbe48f829191b436bac1be1097a1e04eb"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="tc157e1643bb143b69b59a836d0b366c4" style="stroke:none" transform="translate(100.0,250.0) rotate(90.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 0.0, 0)" x1="0.0" x2="0.0" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 6.1224489795918364, 0)" x1="6.1224489795918364" x2="6.1224489795918364" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 12.244897959183673, 0)" x1="12.244897959183673" x2="12.244897959183673" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 18.367346938775508, 0)" x1="18.367346938775508" x2="18.367346938775508" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 24.489795918367346, 0)" x1="24.489795918367346" x2="24.489795918367346" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 30.612244897959179, 0)" x1="30.612244897959179" x2="30.612244897959179" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 36.734693877551017, 0)" x1="36.734693877551017" x2="36.734693877551017" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 42.857142857142854, 0)" x1="42.857142857142854" x2="42.857142857142854" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 48.979591836734691, 0)" x1="48.979591836734691" x2="48.979591836734691" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 55.102040816326522, 0)" x1="55.102040816326522" x2="55.102040816326522" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 61.224489795918359, 0)" x1="61.224489795918359" x2="61.224489795918359" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 67.346938775510196, 0)" x1="67.346938775510196" x2="67.346938775510196" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 73.469387755102034, 0)" x1="73.469387755102034" x2="73.469387755102034" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 79.591836734693871, 0)" x1="79.591836734693871" x2="79.591836734693871" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 85.714285714285708, 0)" x1="85.714285714285708" x2="85.714285714285708" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 91.836734693877531, 0)" x1="91.836734693877531" x2="91.836734693877531" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 97.959183673469383, 0)" x1="97.959183673469383" x2="97.959183673469383" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 104.08163265306122, 0)" x1="104.08163265306122" x2="104.08163265306122" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 110.20408163265304, 0)" x1="110.20408163265304" x2="110.20408163265304" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 116.32653061224489, 0)" x1="116.32653061224489" x2="116.32653061224489" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 122.44897959183672, 0)" x1="122.44897959183672" x2="122.44897959183672" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 128.57142857142856, 0)" x1="128.57142857142856" x2="128.57142857142856" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 134.69387755102039, 0)" x1="134.69387755102039" x2="134.69387755102039" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 140.81632653061223, 0)" x1="140.81632653061223" x2="140.81632653061223" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 146.93877551020407, 0)" x1="146.93877551020407" x2="146.93877551020407" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 153.06122448979593, 0)" x1="153.06122448979593" x2="153.06122448979593" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 159.18367346938774, 0)" x1="159.18367346938774" x2="159.18367346938774" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 165.30612244897958, 0)" x1="165.30612244897958" x2="165.30612244897958" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 171.42857142857142, 0)" x1="171.42857142857142" x2="171.42857142857142" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 177.55102040816325, 0)" x1="177.55102040816325" x2="177.55102040816325" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 183.67346938775506, 0)" x1="183.67346938775506" x2="183.67346938775506" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 189.79591836734693, 0)" x1="189.79591836734693" x2="189.79591836734693" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 195.91836734693877, 0)" x1="195.91836734693877" x2="195.91836734693877" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 202.0408163265306, 0)" x1="202.0408163265306" x2="202.0408163265306" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 208.16326530612244, 0)" x1="208.16326530612244" x2="208.16326530612244" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 214.28571428571425, 0)" x1="214.28571428571425" x2="214.28571428571425" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 220.40816326530609, 0)" x1="220.40816326530609" x2="220.40816326530609" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 226.53061224489795, 0)" x1="226.53061224489795" x2="226.53061224489795" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 232.65306122448979, 0)" x1="232.65306122448979" x2="232.65306122448979" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 238.7755102040816, 0)" x1="238.7755102040816" x2="238.7755102040816" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 244.89795918367344, 0)" x1="244.89795918367344" x2="244.89795918367344" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 251.02040816326527, 0)" x1="251.02040816326527" x2="251.02040816326527" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 257.14285714285711, 0)" x1="257.14285714285711" x2="257.14285714285711" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 263.26530612244898, 0)" x1="263.26530612244898" x2="263.26530612244898" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 269.38775510204079, 0)" x1="269.38775510204079" x2="269.38775510204079" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 275.51020408163265, 0)" x1="275.51020408163265" x2="275.51020408163265" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 281.63265306122446, 0)" x1="281.63265306122446" x2="281.63265306122446" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 287.75510204081633, 0)" x1="287.75510204081633" x2="287.75510204081633" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 293.87755102040813, 0)" x1="293.87755102040813" x2="293.87755102040813" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 300.0, 0)" x1="300.0" x2="300.0" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-axes-Axis" id="t9e5bb78e347e488c82f03a664e54ebd4" transform="translate(100.0,250.0) rotate(90.0) translate(0,20.0)"><line style="" x1="0" x2="300.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,0) rotate(0)" x="0" y="0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="0">Top to bottom</text></g></g><g class="toyplot-axes-NumberLine" id="t1c2dd764ded048cc9c65d74a5dbbe252"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="ta54dbd93f6184d2b8d0608eea6c4e62e" style="stroke:none" transform="translate(150.0,550.0) rotate(-90.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 0.0, 0)" x1="0.0" x2="0.0" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 6.1224489795918364, 0)" x1="6.1224489795918364" x2="6.1224489795918364" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 12.244897959183673, 0)" x1="12.244897959183673" x2="12.244897959183673" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 18.367346938775508, 0)" x1="18.367346938775508" x2="18.367346938775508" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 24.489795918367346, 0)" x1="24.489795918367346" x2="24.489795918367346" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 30.612244897959179, 0)" x1="30.612244897959179" x2="30.612244897959179" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 36.734693877551017, 0)" x1="36.734693877551017" x2="36.734693877551017" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 42.857142857142854, 0)" x1="42.857142857142854" x2="42.857142857142854" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 48.979591836734691, 0)" x1="48.979591836734691" x2="48.979591836734691" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 55.102040816326522, 0)" x1="55.102040816326522" x2="55.102040816326522" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 61.224489795918359, 0)" x1="61.224489795918359" x2="61.224489795918359" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 67.346938775510196, 0)" x1="67.346938775510196" x2="67.346938775510196" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 73.469387755102034, 0)" x1="73.469387755102034" x2="73.469387755102034" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 79.591836734693871, 0)" x1="79.591836734693871" x2="79.591836734693871" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 85.714285714285708, 0)" x1="85.714285714285708" x2="85.714285714285708" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 91.836734693877531, 0)" x1="91.836734693877531" x2="91.836734693877531" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 97.959183673469383, 0)" x1="97.959183673469383" x2="97.959183673469383" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 104.08163265306122, 0)" x1="104.08163265306122" x2="104.08163265306122" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 110.20408163265304, 0)" x1="110.20408163265304" x2="110.20408163265304" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 116.32653061224489, 0)" x1="116.32653061224489" x2="116.32653061224489" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 122.44897959183672, 0)" x1="122.44897959183672" x2="122.44897959183672" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 128.57142857142856, 0)" x1="128.57142857142856" x2="128.57142857142856" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 134.69387755102039, 0)" x1="134.69387755102039" x2="134.69387755102039" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 140.81632653061223, 0)" x1="140.81632653061223" x2="140.81632653061223" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 146.93877551020407, 0)" x1="146.93877551020407" x2="146.93877551020407" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 153.06122448979593, 0)" x1="153.06122448979593" x2="153.06122448979593" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 159.18367346938774, 0)" x1="159.18367346938774" x2="159.18367346938774" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 165.30612244897958, 0)" x1="165.30612244897958" x2="165.30612244897958" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 171.42857142857142, 0)" x1="171.42857142857142" x2="171.42857142857142" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 177.55102040816325, 0)" x1="177.55102040816325" x2="177.55102040816325" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 183.67346938775506, 0)" x1="183.67346938775506" x2="183.67346938775506" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 189.79591836734693, 0)" x1="189.79591836734693" x2="189.79591836734693" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 195.91836734693877, 0)" x1="195.91836734693877" x2="195.91836734693877" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 202.0408163265306, 0)" x1="202.0408163265306" x2="202.0408163265306" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 208.16326530612244, 0)" x1="208.16326530612244" x2="208.16326530612244" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 214.28571428571425, 0)" x1="214.28571428571425" x2="214.28571428571425" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 220.40816326530609, 0)" x1="220.40816326530609" x2="220.40816326530609" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 226.53061224489795, 0)" x1="226.53061224489795" x2="226.53061224489795" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 232.65306122448979, 0)" x1="232.65306122448979" x2="232.65306122448979" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 238.7755102040816, 0)" x1="238.7755102040816" x2="238.7755102040816" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 244.89795918367344, 0)" x1="244.89795918367344" x2="244.89795918367344" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 251.02040816326527, 0)" x1="251.02040816326527" x2="251.02040816326527" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 257.14285714285711, 0)" x1="257.14285714285711" x2="257.14285714285711" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 263.26530612244898, 0)" x1="263.26530612244898" x2="263.26530612244898" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 269.38775510204079, 0)" x1="269.38775510204079" x2="269.38775510204079" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 275.51020408163265, 0)" x1="275.51020408163265" x2="275.51020408163265" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 281.63265306122446, 0)" x1="281.63265306122446" x2="281.63265306122446" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 287.75510204081633, 0)" x1="287.75510204081633" x2="287.75510204081633" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 293.87755102040813, 0)" x1="293.87755102040813" x2="293.87755102040813" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 300.0, 0)" x1="300.0" x2="300.0" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-axes-Axis" id="t8f8ee66e80584de6a986e3c354139489" transform="translate(150.0,550.0) rotate(-90.0) translate(0,20.0)"><line style="" x1="0" x2="300.0" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,0) rotate(0)" x="0" y="0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="150.0" y="0">Bottom to top</text></g></g><g class="toyplot-axes-NumberLine" id="t9f03abeceb2e4e349cdb092265b23ef9"><g class="toyplot-coordinate-events"><g class="toyplot-mark-Scatterplot" id="te2ea4b20e3f746b6ba7218c52989b7c7" style="stroke:none" transform="translate(250.0,550.0) rotate(-45.0) translate(0,-0.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 0.0, 0)" x1="0.0" x2="0.0" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 8.6584503818760918, 0)" x1="8.6584503818760918" x2="8.6584503818760918" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 17.316900763752184, 0)" x1="17.316900763752184" x2="17.316900763752184" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 25.975351145628277, 0)" x1="25.975351145628277" x2="25.975351145628277" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 34.633801527504367, 0)" x1="34.633801527504367" x2="34.633801527504367" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 43.292251909380454, 0)" x1="43.292251909380454" x2="43.292251909380454" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 51.950702291256555, 0)" x1="51.950702291256555" x2="51.950702291256555" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 60.609152673132641, 0)" x1="60.609152673132641" x2="60.609152673132641" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 69.267603055008735, 0)" x1="69.267603055008735" x2="69.267603055008735" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 77.926053436884828, 0)" x1="77.926053436884828" x2="77.926053436884828" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 86.584503818760908, 0)" x1="86.584503818760908" x2="86.584503818760908" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 95.242954200637001, 0)" x1="95.242954200637001" x2="95.242954200637001" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 103.90140458251311, 0)" x1="103.90140458251311" x2="103.90140458251311" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 112.55985496438919, 0)" x1="112.55985496438919" x2="112.55985496438919" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 121.21830534626528, 0)" x1="121.21830534626528" x2="121.21830534626528" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 129.87675572814138, 0)" x1="129.87675572814138" x2="129.87675572814138" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 138.53520611001747, 0)" x1="138.53520611001747" x2="138.53520611001747" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 147.19365649189356, 0)" x1="147.19365649189356" x2="147.19365649189356" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 155.85210687376966, 0)" x1="155.85210687376966" x2="155.85210687376966" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 164.51055725564575, 0)" x1="164.51055725564575" x2="164.51055725564575" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 173.16900763752182, 0)" x1="173.16900763752182" x2="173.16900763752182" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 181.82745801939794, 0)" x1="181.82745801939794" x2="181.82745801939794" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 190.485908401274, 0)" x1="190.485908401274" x2="190.485908401274" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 199.14435878315012, 0)" x1="199.14435878315012" x2="199.14435878315012" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 207.80280916502622, 0)" x1="207.80280916502622" x2="207.80280916502622" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 216.46125954690231, 0)" x1="216.46125954690231" x2="216.46125954690231" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 225.11970992877838, 0)" x1="225.11970992877838" x2="225.11970992877838" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 233.77816031065447, 0)" x1="233.77816031065447" x2="233.77816031065447" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 242.43661069253056, 0)" x1="242.43661069253056" x2="242.43661069253056" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 251.09506107440669, 0)" x1="251.09506107440669" x2="251.09506107440669" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 259.75351145628275, 0)" x1="259.75351145628275" x2="259.75351145628275" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 268.41196183815885, 0)" x1="268.41196183815885" x2="268.41196183815885" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 277.07041222003494, 0)" x1="277.07041222003494" x2="277.07041222003494" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 285.72886260191103, 0)" x1="285.72886260191103" x2="285.72886260191103" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 294.38731298378713, 0)" x1="294.38731298378713" x2="294.38731298378713" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 303.04576336566322, 0)" x1="303.04576336566322" x2="303.04576336566322" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 311.70421374753931, 0)" x1="311.70421374753931" x2="311.70421374753931" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 320.36266412941541, 0)" x1="320.36266412941541" x2="320.36266412941541" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 329.0211145112915, 0)" x1="329.0211145112915" x2="329.0211145112915" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 337.67956489316754, 0)" x1="337.67956489316754" x2="337.67956489316754" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 346.33801527504363, 0)" x1="346.33801527504363" x2="346.33801527504363" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 354.99646565691978, 0)" x1="354.99646565691978" x2="354.99646565691978" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 363.65491603879588, 0)" x1="363.65491603879588" x2="363.65491603879588" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 372.31336642067197, 0)" x1="372.31336642067197" x2="372.31336642067197" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 380.97181680254801, 0)" x1="380.97181680254801" x2="380.97181680254801" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 389.6302671844241, 0)" x1="389.6302671844241" x2="389.6302671844241" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 398.28871756630025, 0)" x1="398.28871756630025" x2="398.28871756630025" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 406.94716794817634, 0)" x1="406.94716794817634" x2="406.94716794817634" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 415.60561833005244, 0)" x1="415.60561833005244" x2="415.60561833005244" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 424.26406871192853, 0)" x1="424.26406871192853" x2="424.26406871192853" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-axes-Axis" id="tbeb211d1753940d3b5c4c96822995c82" transform="translate(250.0,550.0) rotate(-45.0) translate(0,20.0)"><line style="" x1="0" x2="424.26406871192853" y1="0" y2="0"></line><g><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,0) rotate(0)" x="0" y="0">0.0</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(212.13203435596427,0) rotate(0)" x="0" y="0">0.5</text><text style="alignment-baseline:middle;baseline-shift:-100%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(424.26406871192853,0) rotate(0)" x="0" y="0">1.0</text></g><text style="alignment-baseline:middle;baseline-shift:-200%;font-weight:bold;stroke:none;text-anchor:middle" x="212.13203435596427" y="0">Diagonal</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t4605f4c19f0f48e1b4084e1b6919a6bc text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              if(match[1] == "middle")
              {
                var style = getComputedStyle(text[i]);
                var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
                var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
                dy += 0.4 * font_size;
                text[i].setAttribute("dy", dy);
              }
            }
          }
        }
        if(!window.CSS.supports("baseline-shift", "0"))
        {
          var re = /\s*baseline-shift\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t4605f4c19f0f48e1b4084e1b6919a6bc text");
          for(var i = 0; i != text.length; ++i)
          {
            var match = re.exec(text[i].attributes.style.value);
            if(match)
            {
              var style = getComputedStyle(text[i]);
              var font_size = style.fontSize.substr(0, style.fontSize.length - 2);
              var percent = 0.01 * match[1].substr(0, match[1].length-1);
              var dy = text[i].dy.baseVal.length ? text[i].dy.baseVal[0].value : 0;
              dy -= percent * font_size
              text[i].setAttribute("dy", dy);
            }
          }
        }
      }
    })();
    </script><script>
    (function()
    {
      var data_tables = [{"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "title": "Scatterplot Data", "names": ["x0"], "id": "t9b18db6afe8447d29a26ca2d5802a431", "filename": "toyplot"}, {"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "title": "Scatterplot Data", "names": ["x0"], "id": "tb15ae97d4ec746338ad0ec72d1fb8f5c", "filename": "toyplot"}, {"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "title": "Scatterplot Data", "names": ["x0"], "id": "tc157e1643bb143b69b59a836d0b366c4", "filename": "toyplot"}, {"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "title": "Scatterplot Data", "names": ["x0"], "id": "ta54dbd93f6184d2b8d0608eea6c4e62e", "filename": "toyplot"}, {"data": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "title": "Scatterplot Data", "names": ["x0"], "id": "te2ea4b20e3f746b6ba7218c52989b7c7", "filename": "toyplot"}];
    
      function save_csv(data_table)
      {
        var uri = "data:text/csv;charset=utf-8,";
        uri += data_table.names.join(",") + "\n";
        for(var i = 0; i != data_table.data[0].length; ++i)
        {
          for(var j = 0; j != data_table.data.length; ++j)
          {
            if(j)
              uri += ",";
            uri += data_table.data[j][i];
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
          var popup = document.querySelector("#t4605f4c19f0f48e1b4084e1b6919a6bc .toyplot-mark-popup");
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

