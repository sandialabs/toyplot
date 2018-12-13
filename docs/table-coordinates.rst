
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _table-coordinates:

Table Coordinates
=================

Data tables, with *rows* containing *observations* and *columns*
containing (depending on your field) *features*, *dimensions*,
*variables*, or *series*, are arguably the cornerstone of science. Much
of the functionality of Toyplot or any other plotting package can be
reduced to a process of mapping data series from tables to properties
like coordinates and colors. Nevertheless, much tabular information is
still best understood in its "native" tabular form, and we believe that
even a humble table benefits from good layout and design - which is why
Toyplot supports rendering tables as data graphics, treating them as
first-class objects instead of specialized markup. This means that you
can combine high-quality tables and plots in innovative ways, and save
them using any of the formats supported by Toyplot, including HTML, SVG,
PDF, and PNG.

To accomplish this, Toyplot provides
:class:`toyplot.coordinates.Table`, which is a specialized coordinate
system. Just like :ref:`cartesian-coordinates`, and
:ref:`numberline-coordinates`, tables map domain coordinates to canvas
coordinates. Unlike more traditional coordinate systems, tables map
integer coordinates that increase from left-to-right and top-to-bottom
to rectangular ``regions`` of the canvas called ``cells``.

Be careful not to confuse the ``table coordinates`` described in this
section with :ref:`data-tables`, which are purely a data storage
mechanism. To make this distinction clear, let's start by loading some
sample data into a data table:

.. code:: python

    import numpy
    import toyplot.data
    data_table = toyplot.data.temperatures()
    data_table = data_table[:10]

Now, we can display the data using a set of table coordinates:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table)
    table.cells.column[[0, 1]].width = 150



.. raw:: html

    <div class="toyplot" id="t78e0581129714c61a1eb253b99514cbf" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t96427d6f49d3406da0e94ed0a2f5f587" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="ta06d570764d240368dc4b40dd4934acf"><g transform="translate(55.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(205.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(355.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(430.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">TMAX</text></g><g transform="translate(505.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">TMIN</text></g><g transform="translate(580.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">TOBS</text></g><g transform="translate(55.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(430.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">39</text></g><g transform="translate(505.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-72</text></g><g transform="translate(580.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-67</text></g><g transform="translate(55.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(430.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(505.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-133</text></g><g transform="translate(580.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-133</text></g><g transform="translate(55.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(430.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">11</text></g><g transform="translate(505.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-139</text></g><g transform="translate(580.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-89</text></g><g transform="translate(55.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(430.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">11</text></g><g transform="translate(505.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-139</text></g><g transform="translate(580.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-89</text></g><g transform="translate(55.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(430.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">22</text></g><g transform="translate(505.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-144</text></g><g transform="translate(580.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-111</text></g><g transform="translate(55.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(430.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">44</text></g><g transform="translate(505.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-122</text></g><g transform="translate(580.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-100</text></g><g transform="translate(55.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(430.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">56</text></g><g transform="translate(505.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-122</text></g><g transform="translate(580.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-11</text></g><g transform="translate(55.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(430.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">100</text></g><g transform="translate(505.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-83</text></g><g transform="translate(580.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-78</text></g><g transform="translate(55.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(430.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">72</text></g><g transform="translate(505.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-83</text></g><g transform="translate(580.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-33</text></g><g transform="translate(55.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(430.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">89</text></g><g transform="translate(505.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-50</text></g><g transform="translate(580.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">22</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t78e0581129714c61a1eb253b99514cbf";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t96427d6f49d3406da0e94ed0a2f5f587";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"ta06d570764d240368dc4b40dd4934acf","data","table data",["STATION", "STATION_NAME", "DATE", "TMAX", "TMIN", "TOBS"],[["GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], ["39", "0", "11", "11", "22", "44", "56", "100", "72", "89"], ["-72", "-133", "-139", "-139", "-144", "-122", "-122", "-83", "-83", "-50"], ["-67", "-133", "-89", "-89", "-111", "-100", "-11", "-78", "-33", "22"]],"toyplot");
    })();</script></div></div>


With surprisingly little effort, this produces a very clean, easy to
read table. Note that, like regular Cartesian coordinates, the table
coordinates fill the available Canvas by default, so you can adjust your
canvas width and height to expand or contract the rows and columns in
your table. By default, each row and column in the table receives an
equal amount of the available space, unless they are individually
overridden as we've done here. Of course, you're free to use all of the
mechanisms outlined in :ref:`canvas-layout` to add multiple tables to
a canvas.

In this case, the data file contains a series ``TOBS`` that we don't
need, so let's discard it and reorder the ``TMIN`` and ``TMAX`` columns
to put them in a more natural order:

.. code:: python

    data_table = data_table[["STATION", "STATION_NAME", "DATE", "TMIN", "TMAX"]]

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table)
    table.cells.column[[0, 1]].width = 170



.. raw:: html

    <div class="toyplot" id="t53e0fcabc7f7435d83a04d603e8e6ae2" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t6c964e5caceb436589a13fbf730e7ccc" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="tce30069ab5054ed0ab358b71fa0ff135"><g transform="translate(55.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(481.6666666666667,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">TMIN</text></g><g transform="translate(568.3333333333334,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">TMAX</text></g><g transform="translate(55.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(481.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-72</text></g><g transform="translate(568.3333333333334,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">39</text></g><g transform="translate(55.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(481.6666666666667,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-133</text></g><g transform="translate(568.3333333333334,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(55.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(481.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-139</text></g><g transform="translate(568.3333333333334,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">11</text></g><g transform="translate(55.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(481.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-139</text></g><g transform="translate(568.3333333333334,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">11</text></g><g transform="translate(55.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(481.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-144</text></g><g transform="translate(568.3333333333334,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">22</text></g><g transform="translate(55.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(481.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-122</text></g><g transform="translate(568.3333333333334,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">44</text></g><g transform="translate(55.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(481.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-122</text></g><g transform="translate(568.3333333333334,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">56</text></g><g transform="translate(55.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(481.6666666666667,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-83</text></g><g transform="translate(568.3333333333334,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">100</text></g><g transform="translate(55.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(481.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-83</text></g><g transform="translate(568.3333333333334,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">72</text></g><g transform="translate(55.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(481.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">-50</text></g><g transform="translate(568.3333333333334,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">89</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t53e0fcabc7f7435d83a04d603e8e6ae2";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t6c964e5caceb436589a13fbf730e7ccc";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tce30069ab5054ed0ab358b71fa0ff135","data","table data",["STATION", "STATION_NAME", "DATE", "TMIN", "TMAX"],[["GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], ["-72", "-133", "-139", "-139", "-144", "-122", "-122", "-83", "-83", "-50"], ["39", "0", "11", "11", "22", "44", "56", "100", "72", "89"]],"toyplot");
    })();</script></div></div>


As it happens, all of the columns in our data table contain string
values. Note that the labels and columns in the graphic are all
left-justified, the default for string data. Let's see what happens when
we convert ``TMIN`` and ``TMAX`` to integers:

.. code:: python

    data_table["TMIN"] = data_table["TMIN"].astype("int")
    data_table["TMAX"] = data_table["TMAX"].astype("int")

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table)
    table.cells.column[[0, 1]].width = 170



.. raw:: html

    <div class="toyplot" id="t703cb9d3af6d44478313b3765b0b8523" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="tddfe2028d68345bf88ee4ebd5e0fe453" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="tcacea38e576743458626732cbbbe0c88"><g transform="translate(55.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(558.3333333333334,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-29.328" y="3.066">TMIN</text></g><g transform="translate(645.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-33.996" y="3.066">TMAX</text></g><g transform="translate(55.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(558.3333333333334,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-72</text></g><g transform="translate(645.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">39</text></g><g transform="translate(55.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(558.3333333333334,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.012" y="3.066">-133</text></g><g transform="translate(645.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(55.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(558.3333333333334,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.012" y="3.066">-139</text></g><g transform="translate(645.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">11</text></g><g transform="translate(55.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(558.3333333333334,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.012" y="3.066">-139</text></g><g transform="translate(645.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">11</text></g><g transform="translate(55.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(558.3333333333334,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.012" y="3.066">-144</text></g><g transform="translate(645.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">22</text></g><g transform="translate(55.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(558.3333333333334,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.012" y="3.066">-122</text></g><g transform="translate(645.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">44</text></g><g transform="translate(55.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(558.3333333333334,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-24.012" y="3.066">-122</text></g><g transform="translate(645.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">56</text></g><g transform="translate(55.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(558.3333333333334,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-83</text></g><g transform="translate(645.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-20.016" y="3.066">100</text></g><g transform="translate(55.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(558.3333333333334,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-83</text></g><g transform="translate(645.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">72</text></g><g transform="translate(55.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(558.3333333333334,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-50</text></g><g transform="translate(645.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">89</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t703cb9d3af6d44478313b3765b0b8523";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tddfe2028d68345bf88ee4ebd5e0fe453";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tcacea38e576743458626732cbbbe0c88","data","table data",["STATION", "STATION_NAME", "DATE", "TMIN", "TMAX"],[["GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], [-72, -133, -139, -139, -144, -122, -122, -83, -83, -50], [39, 0, 11, 11, 22, 44, 56, 100, 72, 89]],"toyplot");
    })();</script></div></div>


After converting ``TMIN`` and ``TMAX`` to integers, they are
right-justified within the table, so their digits all align, making it
easy to judge magnitudes. It turns out that the data in these columns
are actually integers representing tenths-of-a-degree Celsius, so let's
convert them to floating-point Celsius degrees and see what happens:

.. code:: python

    data_table["TMIN"] = data_table["TMIN"] * 0.1
    data_table["TMAX"] = data_table["TMAX"] * 0.1

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table)
    table.cells.column[[0, 1]].width = 170



.. raw:: html

    <div class="toyplot" id="ta27eec498a6a4f9a9e4c428532047a70" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="td3af8932c75c4d4690a17b3ec15857be" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t1b7dd5fe3b074cb8a294be66a7d8a5b2"><g transform="translate(55.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(520.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(606.6666666666667,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(518.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(520.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(606.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(518.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(55.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(518.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(518.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(518.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(520.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(604.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(606.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(518.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(606.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(55.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(518.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(606.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(55.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(518.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(55.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(518.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(606.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(518.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(604.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(606.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "ta27eec498a6a4f9a9e4c428532047a70";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "td3af8932c75c4d4690a17b3ec15857be";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t1b7dd5fe3b074cb8a294be66a7d8a5b2","data","table data",["STATION", "STATION_NAME", "DATE", "TMIN", "TMAX"],[["GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], [-7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], [3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


Now, all of the decimal points are properly aligned within each column,
even for values without a decimal point!

If you ever want to change the way data in a table is formatted, you can
do so by assigning a different format object. For example, you could
switch to a fixed number of digits to the right of the decimal point:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table)
    table.cells.column[[0, 1]].width = 170
    table.cells.column[3:5].format = toyplot.format.FloatFormatter("{:.1f}")



.. raw:: html

    <div class="toyplot" id="t7028d0391ca64448999ff22e699c38fd" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t7547f926f22c4f938cfc384dfd66749a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t5dc2f3c4b2434aa6a19b801a51af920a"><g transform="translate(55.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(520.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(606.6666666666667,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(518.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(520.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(606.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(518.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(606.6666666666667,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(55.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(518.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(518.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(518.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(520.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(604.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(606.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(518.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(606.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(55.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(518.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(606.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(55.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(518.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(606.6666666666667,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(55.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(518.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(606.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(518.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(520.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(604.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(606.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t7028d0391ca64448999ff22e699c38fd";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t7547f926f22c4f938cfc384dfd66749a";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t5dc2f3c4b2434aa6a19b801a51af920a","data","table data",["STATION", "STATION_NAME", "DATE", "TMIN", "TMAX"],[["GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], [-7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], [3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


Next, let's title our figure. As with the other coordinate systems,
tables have a ``label`` property that can be set at construction time:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, label="Temperature Readings")
    table.cells.column[[0, 1]].width = 170



.. raw:: html

    <div class="toyplot" id="t6615367637184f04b2db1b381d71b3b4" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t3ae128420a574af1b5e60371e09eaef9" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="te7fd3818030346978625d4df3da979f9"><g transform="translate(350.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-75.852" y="-10.423">Temperature Readings</text></g><g transform="translate(55.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(520.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(606.6666666666667,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(518.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(520.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(606.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(518.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(55.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(518.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(518.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(518.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(520.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(604.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(606.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(518.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(606.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(55.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(518.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(606.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(55.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(518.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(55.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(518.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(606.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(518.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(604.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(606.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t6615367637184f04b2db1b381d71b3b4";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t3ae128420a574af1b5e60371e09eaef9";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"te7fd3818030346978625d4df3da979f9","data","table data",["STATION", "STATION_NAME", "DATE", "TMIN", "TMAX"],[["GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], [-7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], [3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


You also have complete control over the gridlines that separate the
cells in a table:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, label="Temperature Readings")
    table.cells.column[[0, 1]].width = 170
    table.cells.grid.hlines[...] = "single"
    table.cells.grid.vlines[...] = "single"
    table.cells.grid.hlines[1,...] = "double"



.. raw:: html

    <div class="toyplot" id="t2113316bc33f4666a76188d507f52706" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="tdf1db5dc6bc44bfebc55f1487d92c695" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t96600f36377f4974bd7a22e49b719dc6"><g transform="translate(350.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-75.852" y="-10.423">Temperature Readings</text></g><g transform="translate(55.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(520.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(606.6666666666667,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(518.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(520.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(606.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(518.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(55.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(518.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(518.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(518.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(520.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(604.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(606.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(518.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(606.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(55.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(518.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(606.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(55.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(518.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(55.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(518.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(606.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(518.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(604.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(606.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="50.0" y2="50.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="76.27272727272728" y2="76.27272727272728"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="78.27272727272728" y2="78.27272727272728"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="104.54545454545455" y2="104.54545454545455"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="131.8181818181818" y2="131.8181818181818"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="159.0909090909091" y2="159.0909090909091"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="186.36363636363637" y2="186.36363636363637"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="213.63636363636365" y2="213.63636363636365"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="240.90909090909093" y2="240.90909090909093"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="268.18181818181824" y2="268.18181818181824"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="295.4545454545455" y2="295.4545454545455"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="322.72727272727275" y2="322.72727272727275"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="350.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="50.0" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="220.0" x2="220.0" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="390.0" x2="390.0" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="476.6666666666667" x2="476.6666666666667" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="563.3333333333334" x2="563.3333333333334" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="650.0" x2="650.0" y1="50.0" y2="350.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t2113316bc33f4666a76188d507f52706";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tdf1db5dc6bc44bfebc55f1487d92c695";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t96600f36377f4974bd7a22e49b719dc6","data","table data",["STATION", "STATION_NAME", "DATE", "TMIN", "TMAX"],[["GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], [-7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], [3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


For a table with :math:`M` rows and :math:`N` columns, the
``table.cells.grid.hlines`` matrix controls the appearance of
:math:`M+1 \times N` horizontal lines, and ``table.cells.grid.vlines``
controls :math:`M \times N+1` vertical lines. Use "single" for single
lines, "double" for double lines, or any value that evaluates to False
to hide the lines.

Suppose you wanted to highlight the observations in the dataset with the
highest high temperature and the lowest low temperature. You could do so
by changing the style of the given rows:

.. code:: python

    low_index = numpy.argsort(data_table["TMIN"])[0]
    high_index = numpy.argsort(data_table["TMAX"])[-1]
    
    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, label="Temperature Readings")
    table.cells.column[[0, 1]].width = 170
    table.cells.row[low_index].lstyle = {"font-weight":"bold", "fill":"blue"}
    table.cells.row[high_index].lstyle = {"font-weight":"bold", "fill":"red"}



.. raw:: html

    <div class="toyplot" id="t48d40855f1074d95846a8f28fafb971b" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t05afe822e29346ea9910b78a3ab969f3" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t68472a5596494ff4bd2848b9190eb7b9"><g transform="translate(350.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-75.852" y="-10.423">Temperature Readings</text></g><g transform="translate(55.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(520.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(606.6666666666667,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(518.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(520.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(606.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(518.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(55.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(518.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,172.72727272727275)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,172.72727272727275)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,172.72727272727275)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(518.0,172.72727272727275)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,172.72727272727275)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,172.72727272727275)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,172.72727272727275)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,172.72727272727275)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,172.72727272727275)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(518.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(520.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(604.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(606.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(518.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(606.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(55.0,254.5454545454546)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,254.5454545454546)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,254.5454545454546)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(518.0,254.5454545454546)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,254.5454545454546)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,254.5454545454546)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,254.5454545454546)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(606.6666666666667,254.5454545454546)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,254.5454545454546)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(55.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(518.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(55.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(518.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(606.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(518.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(604.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(606.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t48d40855f1074d95846a8f28fafb971b";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t05afe822e29346ea9910b78a3ab969f3";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t68472a5596494ff4bd2848b9190eb7b9","data","table data",["STATION", "STATION_NAME", "DATE", "TMIN", "TMAX"],[["GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], [-7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], [3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


Wait a second ... those colored rows are both off-by-one! The actual
minimum and maximum values are in the rows immediately following the
colored rows. What happened? Note that the table has an "extra" row for
the column headers, so row zero in the data is actually row one in the
table, so that the data rows have "one-based" indices instead of the
"zero-based" indices that all good programmers should expect. We could
fix the problem by offsetting the indices we calculated from the raw
data, but that would be error-prone and annoying. The offset would also
change if we ever changed the number of extra rows before the body of
the table (which we'll see an example of in a moment).

What we really need is a way to refer to the "top" rows and the "body"
rows in the table separately, using zero-based indices for each.
Fortunately, Toyplot does just that - we can use special accessor
attributes to target our changes to the top or the body, using
coordinates that won't be affected by changes to other parts of the
table:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, label="Temperature Readings")
    table.cells.column[[0, 1]].width = 170
    table.body.row[low_index].lstyle = {"font-weight":"bold", "fill":"blue"}
    table.body.row[high_index].lstyle = {"font-weight":"bold", "fill":"red"}



.. raw:: html

    <div class="toyplot" id="tdd6818196d634a14adfcc50093865150" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t81f59ae47f4748a6ab3a50f6c5db608b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t6d04db1cde564a518a2a780a3194dda8"><g transform="translate(350.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-75.852" y="-10.423">Temperature Readings</text></g><g transform="translate(55.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(520.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(606.6666666666667,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(518.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(520.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(606.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(518.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(55.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(518.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(518.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,200.0)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,200.0)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,200.0)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(518.0,200.0)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(520.0,200.0)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,200.0)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(604.6666666666667,200.0)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(606.6666666666667,200.0)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,200.0)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(518.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(606.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(55.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(518.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(606.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(55.0,281.81818181818187)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,281.81818181818187)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,281.81818181818187)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(518.0,281.81818181818187)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,281.81818181818187)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,281.81818181818187)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,281.81818181818187)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(55.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(518.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(606.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(518.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(604.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(606.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tdd6818196d634a14adfcc50093865150";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t81f59ae47f4748a6ab3a50f6c5db608b";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t6d04db1cde564a518a2a780a3194dda8","data","table data",["STATION", "STATION_NAME", "DATE", "TMIN", "TMAX"],[["GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], [-7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], [3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


Now the correct rows have been highlighted. Let's add another row of
headers to verify that the highlighting isn't affected:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, trows=2, label="Temperature Readings")
    table.cells.column[[0, 1]].width = 170
    table.top.grid.hlines[...] = "single"
    table.top.grid.vlines[...] = "single"
    table.body.row[low_index].lstyle = {"font-weight":"bold", "fill":"blue"}
    table.body.row[high_index].lstyle = {"font-weight":"bold", "fill":"red"}



.. raw:: html

    <div class="toyplot" id="t4b4b4cacb3e446e1a8b2c1f4be6cea29" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t721e9c64fe864931a6e0d5ff63e3fcca" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t9bb67a4fcc324e34b5cb3f991c075454"><g transform="translate(350.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-75.852" y="-10.423">Temperature Readings</text></g><g transform="translate(55.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(520.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(606.6666666666667,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(518.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(520.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(606.6666666666667,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(518.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(55.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(518.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(518.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(518.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(520.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(604.6666666666667,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(606.6666666666667,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(518.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(606.6666666666667,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(55.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(518.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(606.6666666666667,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(55.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(518.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(55.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(518.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(606.6666666666667,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(518.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(604.6666666666667,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(606.6666666666667,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="50.0" y2="50.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="75.0" y2="75.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="100.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="50.0" y1="50.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="220.0" x2="220.0" y1="50.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="390.0" x2="390.0" y1="50.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="476.6666666666667" x2="476.6666666666667" y1="50.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="563.3333333333334" x2="563.3333333333334" y1="50.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="650.0" x2="650.0" y1="50.0" y2="100.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t4b4b4cacb3e446e1a8b2c1f4be6cea29";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t721e9c64fe864931a6e0d5ff63e3fcca";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t9bb67a4fcc324e34b5cb3f991c075454","data","table data",[null, null, null, null, null],[["STATION", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["STATION_NAME", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["DATE", "20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], ["TMIN", -7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], ["TMAX", 3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


Sure enough, the correct rows are still highlighted, the top section of
the table contains a second row, and we made the extra row obvious with
some grid lines. Note that by accessing the grid via the "top" accessor,
we were able to easily alter just the grid lines for the top cells.
Let's take things a step further and provide some additional labels in
the new top row:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, trows=2, label="Temperature Readings")
    table.cells.column[[0, 1]].width = 170
    table.body.row[low_index].lstyle = {"font-weight":"bold", "fill":"blue"}
    table.body.row[high_index].lstyle = {"font-weight":"bold", "fill":"red"}
    table.top.grid.hlines[...] = "single"
    table.top.grid.vlines[...] = "single"
    table.top.cell[0, 0:2].merge().data = "Location"
    table.top.cell[0, 3:6].merge().data = u"Temperature \u00b0C"



.. raw:: html

    <div class="toyplot" id="t65e20c75635142d6a84ed6ddc844bbf1" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t30341ac35bd14b8ca5f4be8e1e6b4013" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t0e69ef9becbf452b88eb8f61def32a24"><g transform="translate(350.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-75.852" y="-10.423">Temperature Readings</text></g><g transform="translate(55.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(520.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(606.6666666666667,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(518.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(520.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(606.6666666666667,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(518.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(55.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(518.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(518.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(518.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(520.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(604.6666666666667,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(606.6666666666667,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(518.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(606.6666666666667,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(55.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(518.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(606.6666666666667,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(55.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(518.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(55.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(518.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(606.6666666666667,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(518.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(604.6666666666667,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(606.6666666666667,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,62.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Location</text></g><g transform="translate(563.3333333333334,62.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-44.742" y="3.066">Temperature °C</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="50.0" y2="50.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="75.0" y2="75.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="100.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="50.0" y1="50.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="220.0" x2="220.0" y1="75.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="390.0" x2="390.0" y1="50.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="476.6666666666667" x2="476.6666666666667" y1="50.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="563.3333333333334" x2="563.3333333333334" y1="75.0" y2="100.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="650.0" x2="650.0" y1="50.0" y2="100.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t65e20c75635142d6a84ed6ddc844bbf1";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t30341ac35bd14b8ca5f4be8e1e6b4013";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t0e69ef9becbf452b88eb8f61def32a24","data","table data",["Location", "Location", null, "Temperature \u00b0C", "Temperature \u00b0C"],[["STATION", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["STATION_NAME", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["DATE", "20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], ["TMIN", -7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], ["TMAX", 3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


Note the use of ``merge()`` to merge together ranges of cells, along
with the ``data`` attribute to assign new cell contents.

Also, you may have noticed that the merged cells took on the attributes
(alignment, style, etc.) of the cells that were merged, which is why the
"Location" label is left-justified, while the "Temperature" label is
centered. Let's center-justify the Location label, make both labels a
little more prominent, and lose the gridlines:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, trows=2, label="Temperature Readings")
    table.cells.column[[0, 1]].width = 170
    table.body.row[low_index].lstyle = {"font-weight":"bold", "fill":"blue"}
    table.body.row[high_index].lstyle = {"font-weight":"bold", "fill":"red"}
    merged = table.top.cell[0, 0:2].merge()
    merged.data = "Location"
    merged.align = "center"
    merged.lstyle = {"font-size":"14px"}
    merged = table.top.cell[0, 3:6].merge()
    merged.data = u"Temperature \u00b0C"
    merged.lstyle = {"font-size":"14px"}



.. raw:: html

    <div class="toyplot" id="ta07c1b1bbe47412cb6b83c14e21d4218" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t7a14a71f11d943ec88c5c857a9117a41" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="tb402dee3a04441459e770893ba96aad9"><g transform="translate(350.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-75.852" y="-10.423">Temperature Readings</text></g><g transform="translate(55.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(225.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(395.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(520.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(606.6666666666667,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(518.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(520.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(606.6666666666667,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(518.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(55.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(518.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(518.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(520.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(604.6666666666667,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(606.6666666666667,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(518.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(520.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(604.6666666666667,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(606.6666666666667,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(518.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(606.6666666666667,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(55.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(518.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(520.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(604.6666666666667,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(606.6666666666667,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(55.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(518.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(55.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(518.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(520.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(522.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(604.6666666666667,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(606.6666666666667,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(225.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(395.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(518.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(604.6666666666667,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(606.6666666666667,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(608.6666666666667,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(220.0,62.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-29.168999999999997" y="3.577">Location</text></g><g transform="translate(563.3333333333334,62.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-52.199000000000005" y="3.577">Temperature °C</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="100.0" y2="100.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "ta07c1b1bbe47412cb6b83c14e21d4218";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t7a14a71f11d943ec88c5c857a9117a41";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tb402dee3a04441459e770893ba96aad9","data","table data",["Location", "Location", null, "Temperature \u00b0C", "Temperature \u00b0C"],[["STATION", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["STATION_NAME", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["DATE", "20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], ["TMIN", -7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], ["TMAX", 3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


Finally, let's finish-off our grid by plotting the minimum and maximum
temperatures vertically along the right-hand side of the table. This
will provide an intuitive guide to trends in the data. To do this, we'll
begin by adding two extra columns to the table using the ``rcolumns``
parameter, duplicating the ``TMIN`` and ``TMAX`` data in the new cells,
and readjusting column widths to accomodate the new columns:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, trows=2, rcolumns=2, label="Temperature Readings")
    table.body.column[[0, 1]].width = 150
    table.body.column[2].width = 70
    table.body.row[low_index].lstyle = {"font-weight":"bold", "fill":"blue"}
    table.body.row[high_index].lstyle = {"font-weight":"bold", "fill":"red"}
    merged = table.top.cell[0, 0:2].merge()
    merged.data = "Location"
    merged.align = "center"
    merged.lstyle = {"font-size":"14px"}
    merged = table.cells.cell[0, 3:6].merge()
    merged.data = u"Temperature \u00b0C"
    merged.lstyle = {"font-size":"14px"}
    
    table.right.column[0].data = data_table["TMIN"]
    table.right.column[1].data = data_table["TMAX"]



.. raw:: html

    <div class="toyplot" id="tba1766c707d240f280ebca844db40f41" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t4ae9e47637504e36ac94ac635838a000" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t1e7c6f5f63a34a3db36fc381027b7025"><g transform="translate(350.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-75.852" y="-10.423">Temperature Readings</text></g><g transform="translate(55.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(205.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(355.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(448.75,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(506.25,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(446.75,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(448.75,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(450.75,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(504.25,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(506.25,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(508.25,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(563.75,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.338000000000001" y="3.066">-7.2</text></g><g transform="translate(621.25,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-58.38" y="3.066">3.9000000000000004</text></g><g transform="translate(55.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(446.75,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(448.75,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(450.75,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(504.25,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(563.75,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.674" y="3.066">-13.3</text></g><g transform="translate(621.25,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">0.0</text></g><g transform="translate(55.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(446.75,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(448.75,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(450.75,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(504.25,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(506.25,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(508.25,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(563.75,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.674" y="3.066">-13.9</text></g><g transform="translate(621.25,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">1.1</text></g><g transform="translate(55.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(446.75,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(448.75,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(450.75,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(504.25,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(506.25,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(508.25,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(563.75,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.674" y="3.066">-13.9</text></g><g transform="translate(621.25,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">1.1</text></g><g transform="translate(55.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(446.75,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(448.75,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(450.75,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(504.25,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(506.25,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(508.25,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(563.75,212.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-13.674" y="3.066">-14.4</text></g><g transform="translate(621.25,212.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">2.2</text></g><g transform="translate(55.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(446.75,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(448.75,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(450.75,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(504.25,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(506.25,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(508.25,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(563.75,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-60.37800000000001" y="3.066">-12.200000000000001</text></g><g transform="translate(621.25,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">4.4</text></g><g transform="translate(55.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(446.75,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(448.75,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(450.75,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(504.25,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(506.25,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(508.25,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(563.75,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-60.37800000000001" y="3.066">-12.200000000000001</text></g><g transform="translate(621.25,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-58.38" y="3.066">5.6000000000000005</text></g><g transform="translate(55.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(446.75,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(448.75,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(450.75,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(504.25,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(563.75,287.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.338000000000001" y="3.066">-8.3</text></g><g transform="translate(621.25,287.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.676" y="3.066">10.0</text></g><g transform="translate(55.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(446.75,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(448.75,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(450.75,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(504.25,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(506.25,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(508.25,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(563.75,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.338000000000001" y="3.066">-8.3</text></g><g transform="translate(621.25,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">7.2</text></g><g transform="translate(55.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(446.75,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(504.25,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(506.25,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(508.25,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(563.75,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.338000000000001" y="3.066">-5.0</text></g><g transform="translate(621.25,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.340000000000002" y="3.066">8.9</text></g><g transform="translate(200.0,62.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-29.168999999999997" y="3.577">Location</text></g><g transform="translate(506.25,62.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-52.199000000000005" y="3.577">Temperature °C</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="100.0" y2="100.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tba1766c707d240f280ebca844db40f41";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t4ae9e47637504e36ac94ac635838a000";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t1e7c6f5f63a34a3db36fc381027b7025","data","table data",["Location", "Location", null, "Temperature \u00b0C", "Temperature \u00b0C", "Temperature \u00b0C", null],[["STATION", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["STATION_NAME", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["DATE", "20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], ["TMIN", -7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], ["TMAX", 3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9], [null, -7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], [null, 3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


Now, we can replace the new cells with a line plot that uses their data.
First, we embed a set of cartesian coordinates in the two columns, then
we use ``cell_plot()`` to create a line plot based on the data in the
underlying cells:

.. code:: python

    canvas = toyplot.Canvas(width=700, height=400)
    table = canvas.table(data_table, trows=2, rcolumns=2, label="Temperature Readings")
    table.body.column[[0, 1]].width = 150
    table.body.column[2].width = 70
    table.body.row[low_index].lstyle = {"font-weight":"bold", "fill":"blue"}
    table.body.row[high_index].lstyle = {"font-weight":"bold", "fill":"red"}
    merged = table.top.cell[0, 0:2].merge()
    merged.data = "Location"
    merged.align = "center"
    merged.lstyle = {"font-size":"14px"}
    merged = table.cells.cell[0, 3:6].merge()
    merged.data = u"Temperature \u00b0C"
    merged.lstyle = {"font-size":"14px"}
    
    table.right.column[0].data = data_table["TMIN"]
    table.right.column[1].data = data_table["TMAX"]
    table.right.column[0:2].width = 40
    
    axes = table.right.column[0:2].cartesian()
    mark = axes.cell_plot(color=["blue", "red"], marker="o", style={"stroke-width":1.0})



.. raw:: html

    <div class="toyplot" id="tfb965fd3c7a64a4db7fb59efa5d8ee05" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t1d5c13ccffb5460cb4c0256a821de701" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 400.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="te3cf6eb8b0e245fcbc0ff1e288d5efb4"><g transform="translate(350.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-75.852" y="-10.423">Temperature Readings</text></g><g transform="translate(55.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION</text></g><g transform="translate(205.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">STATION_NAME</text></g><g transform="translate(355.0,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">DATE</text></g><g transform="translate(457.5,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.664" y="3.066">TMIN</text></g><g transform="translate(532.5,87.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.998" y="3.066">TMAX</text></g><g transform="translate(55.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130101</text></g><g transform="translate(455.5,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-7</text></g><g transform="translate(457.5,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(459.5,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(530.5,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(532.5,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(534.5,112.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(55.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130102</text></g><g transform="translate(455.5,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(457.5,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(459.5,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(530.5,137.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(55.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130103</text></g><g transform="translate(455.5,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(457.5,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(459.5,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(530.5,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(532.5,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(534.5,162.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130104</text></g><g transform="translate(455.5,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-13</text></g><g transform="translate(457.5,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(459.5,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(530.5,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(532.5,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(534.5,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(55.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130105</text></g><g transform="translate(455.5,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-14</text></g><g transform="translate(457.5,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(459.5,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(530.5,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(532.5,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(534.5,212.5)"><text style="fill:rgb(0%,0%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130106</text></g><g transform="translate(455.5,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(457.5,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(459.5,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(530.5,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(532.5,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(534.5,237.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(55.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130107</text></g><g transform="translate(455.5,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-17.34" y="3.066">-12</text></g><g transform="translate(457.5,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(459.5,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(530.5,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(532.5,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(534.5,262.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(55.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130108</text></g><g transform="translate(455.5,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(457.5,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(459.5,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(530.5,287.5)"><text style="fill:rgb(100%,0%,0%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.344000000000001" y="3.066">10</text></g><g transform="translate(55.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130109</text></g><g transform="translate(455.5,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-8</text></g><g transform="translate(457.5,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(459.5,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(530.5,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><g transform="translate(532.5,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(534.5,312.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(55.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">GHCND:USC00294366</text></g><g transform="translate(205.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">JEMEZ DAM NM US</text></g><g transform="translate(355.0,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">20130111</text></g><g transform="translate(455.5,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-5</text></g><g transform="translate(530.5,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><g transform="translate(532.5,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(534.5,337.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(200.0,62.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-29.168999999999997" y="3.577">Location</text></g><g transform="translate(515.0,62.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-52.199000000000005" y="3.577">Temperature °C</text></g><g class="toyplot-coordinates-Cartesian" id="t2078f52824784dd5a4eb2f628932501a"><clipPath id="t54e5e169ba0d413496be797acfae7bce"><rect height="250.0" width="80.0" x="570.0" y="100.0"></rect></clipPath><g clip-path="url(#t54e5e169ba0d413496be797acfae7bce)"><g class="toyplot-mark-Plot" id="tfdbb8589ffe543a980ec917f165fe00f" style="fill:none;stroke-width:1.0"><g class="toyplot-Series"><path d="M 594.8360655737705 112.5 L 576.3360655737705 137.5 L 574.516393442623 162.5 L 574.516393442623 187.5 L 573.0 212.5 L 579.672131147541 237.5 L 579.672131147541 262.5 L 591.5 287.5 L 591.5 312.5 L 601.5081967213115 337.5" style="stroke:rgb(0%,0%,100%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(594.8360655737705, 112.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(576.3360655737705, 137.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(574.516393442623, 162.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(574.516393442623, 187.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(573.0, 212.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(579.672131147541, 237.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(579.672131147541, 262.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(591.5, 287.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(591.5, 312.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(601.5081967213115, 337.5)"><circle r="2.0"></circle></g></g><g class="toyplot-Series"><path d="M 628.5 112.5 L 616.672131147541 137.5 L 620.0081967213115 162.5 L 620.0081967213115 187.5 L 623.344262295082 212.5 L 630.016393442623 237.5 L 633.655737704918 262.5 L 647.0 287.5 L 638.5081967213115 312.5 L 643.6639344262295 337.5" style="stroke:rgb(100%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(628.5, 112.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(616.672131147541, 137.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(620.0081967213115, 162.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(620.0081967213115, 187.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(623.344262295082, 212.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(630.016393442623, 237.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(633.655737704918, 262.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(647.0, 287.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(638.5081967213115, 312.5)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(643.6639344262295, 337.5)"><circle r="2.0"></circle></g></g></g></g></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="650.0" y1="100.0" y2="100.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tfb965fd3c7a64a4db7fb59efa5d8ee05";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t1d5c13ccffb5460cb4c0256a821de701";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"te3cf6eb8b0e245fcbc0ff1e288d5efb4","data","table data",["Location", "Location", null, "Temperature \u00b0C", "Temperature \u00b0C", "Temperature \u00b0C", null],[["STATION", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366", "GHCND:USC00294366"], ["STATION_NAME", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US", "JEMEZ DAM NM US"], ["DATE", "20130101", "20130102", "20130103", "20130104", "20130105", "20130106", "20130107", "20130108", "20130109", "20130111"], ["TMIN", -7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], ["TMAX", 3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9], [null, -7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], [null, 3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tfdbb8589ffe543a980ec917f165fe00f","data","plot data",["y", "x0", "x1"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [-7.2, -13.3, -13.9, -13.9, -14.4, -12.200000000000001, -12.200000000000001, -8.3, -8.3, -5.0], [3.9000000000000004, 0.0, 1.1, 1.1, 2.2, 4.4, 5.6000000000000005, 10.0, 7.2, 8.9]],"toyplot");
    })();</script></div></div>


Because the axes were embedded across two columns, the plot contains two
series. When embedding coordinates in table cells the axes, ticks, and
labels are hidden by default to avoid visual clutter. The combination of
tabular and plotted data demonstrates how Toyplot makes it easy to
display data in innovative ways that other libraries can't.

Regions
-------

In the above examples we accessed four distinct regions of the table:

-  ``cells`` - a special region containing every cell in the table.
-  ``body`` - to access the cells that make up the bulk of the table.
-  ``top`` - to access "header" cells above the ``body`` region,
   typically used for column labels.
-  ``right`` - to access additional cells to right of the ``body``
   region that we used to embed a plot.

As you might imagine, tables actually contain nine distinct regions that
include ``body``, ``top``, ``right``, ``bottom``, ``left``,
``top.left``, ``top.right``, ``bottom.right``, and ``bottom.left``.
Below, we demonstrate using explicit row and column counts to create an
empty table so we can highlight all nine regions:

.. code:: python

    canvas, table = toyplot.table(rows=4, columns=4, trows=2, brows=2, lcolumns=2, rcolumns=2, width=400, height=400)
    
    table.cells.grid.hlines[...] = "single"
    table.cells.grid.vlines[...] = "single"
    
    table.top.left.cells.style = {"fill":"red", "opacity":0.5}
    table.top.cells.style = {"fill":"orange", "opacity":0.5}
    table.top.right.cells.style = {"fill":"yellow", "opacity":0.5}
    table.right.cells.style = {"fill":"greenyellow", "opacity":0.5}
    table.bottom.right.cells.style = {"fill":"green", "opacity":0.5}
    table.bottom.cells.style = {"fill":"aqua", "opacity":0.5}
    table.bottom.left.cells.style = {"fill":"blue", "opacity":0.5}
    table.left.cells.style = {"fill":"purple", "opacity":0.5}
    table.body.cells.style = {"fill":"white"}



.. raw:: html

    <div class="toyplot" id="t7b6e41a73ab841db8f8160498dc5800f" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t92bd12b301ca410db25c85a2bc0d2ab7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 400.0 400.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t0736e374149546a08cc59ae3271b7a4a"><rect height="37.5" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="50.0" y="50.0"></rect><rect height="37.5" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="87.5" y="50.0"></rect><rect height="37.5" style="fill:rgb(100%,64.7%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="125.0" y="50.0"></rect><rect height="37.5" style="fill:rgb(100%,64.7%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="162.5" y="50.0"></rect><rect height="37.5" style="fill:rgb(100%,64.7%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="200.0" y="50.0"></rect><rect height="37.5" style="fill:rgb(100%,64.7%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="237.5" y="50.0"></rect><rect height="37.5" style="fill:rgb(100%,100%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="275.0" y="50.0"></rect><rect height="37.5" style="fill:rgb(100%,100%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="312.5" y="50.0"></rect><rect height="37.5" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="50.0" y="87.5"></rect><rect height="37.5" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="87.5" y="87.5"></rect><rect height="37.5" style="fill:rgb(100%,64.7%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="125.0" y="87.5"></rect><rect height="37.5" style="fill:rgb(100%,64.7%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="162.5" y="87.5"></rect><rect height="37.5" style="fill:rgb(100%,64.7%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="200.0" y="87.5"></rect><rect height="37.5" style="fill:rgb(100%,64.7%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="237.5" y="87.5"></rect><rect height="37.5" style="fill:rgb(100%,100%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="275.0" y="87.5"></rect><rect height="37.5" style="fill:rgb(100%,100%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="312.5" y="87.5"></rect><rect height="37.5" style="fill:rgb(50.2%,0%,50.2%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="50.0" y="125.0"></rect><rect height="37.5" style="fill:rgb(50.2%,0%,50.2%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="87.5" y="125.0"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="125.0" y="125.0"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="162.5" y="125.0"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="200.0" y="125.0"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="237.5" y="125.0"></rect><rect height="37.5" style="fill:rgb(67.8%,100%,18.4%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="275.0" y="125.0"></rect><rect height="37.5" style="fill:rgb(67.8%,100%,18.4%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="312.5" y="125.0"></rect><rect height="37.5" style="fill:rgb(50.2%,0%,50.2%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="50.0" y="162.5"></rect><rect height="37.5" style="fill:rgb(50.2%,0%,50.2%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="87.5" y="162.5"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="125.0" y="162.5"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="162.5" y="162.5"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="200.0" y="162.5"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="237.5" y="162.5"></rect><rect height="37.5" style="fill:rgb(67.8%,100%,18.4%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="275.0" y="162.5"></rect><rect height="37.5" style="fill:rgb(67.8%,100%,18.4%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="312.5" y="162.5"></rect><rect height="37.5" style="fill:rgb(50.2%,0%,50.2%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="50.0" y="200.0"></rect><rect height="37.5" style="fill:rgb(50.2%,0%,50.2%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="87.5" y="200.0"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="125.0" y="200.0"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="162.5" y="200.0"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="200.0" y="200.0"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="237.5" y="200.0"></rect><rect height="37.5" style="fill:rgb(67.8%,100%,18.4%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="275.0" y="200.0"></rect><rect height="37.5" style="fill:rgb(67.8%,100%,18.4%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="312.5" y="200.0"></rect><rect height="37.5" style="fill:rgb(50.2%,0%,50.2%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="50.0" y="237.5"></rect><rect height="37.5" style="fill:rgb(50.2%,0%,50.2%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="87.5" y="237.5"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="125.0" y="237.5"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="162.5" y="237.5"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="200.0" y="237.5"></rect><rect height="37.5" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none" width="37.5" x="237.5" y="237.5"></rect><rect height="37.5" style="fill:rgb(67.8%,100%,18.4%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="275.0" y="237.5"></rect><rect height="37.5" style="fill:rgb(67.8%,100%,18.4%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="312.5" y="237.5"></rect><rect height="37.5" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="50.0" y="275.0"></rect><rect height="37.5" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="87.5" y="275.0"></rect><rect height="37.5" style="fill:rgb(0%,100%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="125.0" y="275.0"></rect><rect height="37.5" style="fill:rgb(0%,100%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="162.5" y="275.0"></rect><rect height="37.5" style="fill:rgb(0%,100%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="200.0" y="275.0"></rect><rect height="37.5" style="fill:rgb(0%,100%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="237.5" y="275.0"></rect><rect height="37.5" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="275.0" y="275.0"></rect><rect height="37.5" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="312.5" y="275.0"></rect><rect height="37.5" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="50.0" y="312.5"></rect><rect height="37.5" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="87.5" y="312.5"></rect><rect height="37.5" style="fill:rgb(0%,100%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="125.0" y="312.5"></rect><rect height="37.5" style="fill:rgb(0%,100%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="162.5" y="312.5"></rect><rect height="37.5" style="fill:rgb(0%,100%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="200.0" y="312.5"></rect><rect height="37.5" style="fill:rgb(0%,100%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="237.5" y="312.5"></rect><rect height="37.5" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="275.0" y="312.5"></rect><rect height="37.5" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="37.5" x="312.5" y="312.5"></rect><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="350.0" y1="50.0" y2="50.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="350.0" y1="87.5" y2="87.5"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="350.0" y1="125.0" y2="125.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="350.0" y1="162.5" y2="162.5"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="350.0" y1="200.0" y2="200.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="350.0" y1="237.5" y2="237.5"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="350.0" y1="275.0" y2="275.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="350.0" y1="312.5" y2="312.5"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="350.0" y1="350.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="50.0" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="87.5" x2="87.5" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="125.0" x2="125.0" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="162.5" x2="162.5" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="200.0" x2="200.0" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="237.5" x2="237.5" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="275.0" x2="275.0" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="312.5" x2="312.5" y1="50.0" y2="350.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="350.0" x2="350.0" y1="50.0" y2="350.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t7b6e41a73ab841db8f8160498dc5800f";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t92bd12b301ca410db25c85a2bc0d2ab7";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t0736e374149546a08cc59ae3271b7a4a","data","table data",[null, null, null, null, null, null, null, null],[[null, null, null, null, null, null, null], [null, null, null, null, null, null, null], [null, null, null, null, null, null, null], [null, null, null, null, null, null, null], [null, null, null, null, null, null, null], [null, null, null, null, null, null, null], [null, null, null, null, null, null, null], [null, null, null, null, null, null, null]],"toyplot");
    })();</script></div></div>


Note how the ``hrows``, ``brows``, ``lcolumns``, and ``rcolumns``
parameters control the number of cells in the top, bottom, left, and
right regions respectively. Typically, you would use these regions to
display header, label, and summary information for the data in the body
region, although you are free to use any region for any purpose you
like.

Indexing
--------

When accessing table cells, rows, columns and other objects, you can use
any of the indexing techniques provided by ``numpy``, including
individual indices, slicing, and advanced indexing. In the following we
will call-out examples of each. To begin, you can use individual indices
for one-at-a-time indexing of rows, columns, and cells:

.. code:: python

    canvas, table = toyplot.table(rows=9, columns=9, width=300, height=300)
    table.cells.grid.hlines[...] = "single"
    table.cells.grid.vlines[...] = "single"
    
    table.cells.column[1].style = {"fill":"red", "opacity":0.5}
    table.cells.row[2].style = {"fill":"green", "opacity":0.5}
    table.cells.cell[4, 3].style = {"fill":"blue", "opacity":0.5}



.. raw:: html

    <div class="toyplot" id="t93f416202e934f769a8a57c541981bee" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tb50a292309b441809134486f209a994d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="teeb7223fa8964c8a93c67bba924ace54"><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="50.0"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="161.11111111111111" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="94.44444444444444"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="227.7777777777778"></rect><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="50.0" y2="50.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="72.22222222222223" y2="72.22222222222223"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="94.44444444444444" y2="94.44444444444444"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="116.66666666666666" y2="116.66666666666666"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="138.88888888888889" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="161.11111111111111" y2="161.11111111111111"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="183.33333333333334" y2="183.33333333333334"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="205.55555555555557" y2="205.55555555555557"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="227.7777777777778" y2="227.7777777777778"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="250.00000000000003" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="50.0" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="72.22222222222223" x2="72.22222222222223" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="94.44444444444444" x2="94.44444444444444" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666666" x2="116.66666666666666" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="138.88888888888889" x2="138.88888888888889" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="161.11111111111111" x2="161.11111111111111" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="183.33333333333334" x2="183.33333333333334" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="205.55555555555557" x2="205.55555555555557" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="227.7777777777778" x2="227.7777777777778" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="250.00000000000003" x2="250.00000000000003" y1="50.0" y2="250.00000000000003"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t93f416202e934f769a8a57c541981bee";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tb50a292309b441809134486f209a994d";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"teeb7223fa8964c8a93c67bba924ace54","data","table data",[null, null, null, null, null, null, null, null, null],[[null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null]],"toyplot");
    })();</script></div></div>


Note above that overlapping assignments overwrite cell parameters. As is
normal in Python, negative indices are interpreted relative to the end
of a range:

.. code:: python

    canvas, table = toyplot.table(rows=9, columns=9, width=300, height=300)
    table.cells.grid.hlines[...] = "single"
    table.cells.grid.vlines[...] = "single"
    
    table.cells.column[-1].style = {"fill":"red", "opacity":0.5}
    table.cells.row[-2].style = {"fill":"green", "opacity":0.5}
    table.cells.cell[-4, -3].style = {"fill":"blue", "opacity":0.5}



.. raw:: html

    <div class="toyplot" id="t539157e98d854bf590c6cfe548f3962e" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tc6916e1cfbf249d496d23d29db534462" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t6c6a0978199c44768a4e33e9d74bb9a7"><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="50.0"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="94.44444444444444"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="161.11111111111111" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="227.7777777777778"></rect><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="50.0" y2="50.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="72.22222222222223" y2="72.22222222222223"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="94.44444444444444" y2="94.44444444444444"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="116.66666666666666" y2="116.66666666666666"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="138.88888888888889" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="161.11111111111111" y2="161.11111111111111"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="183.33333333333334" y2="183.33333333333334"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="205.55555555555557" y2="205.55555555555557"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="227.7777777777778" y2="227.7777777777778"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="250.00000000000003" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="50.0" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="72.22222222222223" x2="72.22222222222223" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="94.44444444444444" x2="94.44444444444444" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666666" x2="116.66666666666666" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="138.88888888888889" x2="138.88888888888889" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="161.11111111111111" x2="161.11111111111111" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="183.33333333333334" x2="183.33333333333334" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="205.55555555555557" x2="205.55555555555557" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="227.7777777777778" x2="227.7777777777778" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="250.00000000000003" x2="250.00000000000003" y1="50.0" y2="250.00000000000003"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t539157e98d854bf590c6cfe548f3962e";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tc6916e1cfbf249d496d23d29db534462";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t6c6a0978199c44768a4e33e9d74bb9a7","data","table data",[null, null, null, null, null, null, null, null, null],[[null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null]],"toyplot");
    })();</script></div></div>


Of course, you can use slices to access ranges of rows, columns, and
cells:

.. code:: python

    canvas, table = toyplot.table(rows=9, columns=9, width=300, height=300)
    table.cells.grid.hlines[...] = "single"
    table.cells.grid.vlines[...] = "single"
    
    table.cells.column[0:2].style = {"fill":"red", "opacity":0.5}
    table.cells.row[0:2].style = {"fill":"green", "opacity":0.5}
    table.cells.cell[3:5, 3:5].style = {"fill":"blue", "opacity":0.5}



.. raw:: html

    <div class="toyplot" id="t5ee73c1da7b4431fb0c8913fe2386ff6" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tb9da311c43114318938c31dbb612a394" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t94f1c1c695c049b7b807419cd74de839"><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="161.11111111111111" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="50.0"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="161.11111111111111" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="94.44444444444444"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="227.7777777777778"></rect><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="50.0" y2="50.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="72.22222222222223" y2="72.22222222222223"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="94.44444444444444" y2="94.44444444444444"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="116.66666666666666" y2="116.66666666666666"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="138.88888888888889" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="161.11111111111111" y2="161.11111111111111"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="183.33333333333334" y2="183.33333333333334"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="205.55555555555557" y2="205.55555555555557"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="227.7777777777778" y2="227.7777777777778"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="250.00000000000003" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="50.0" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="72.22222222222223" x2="72.22222222222223" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="94.44444444444444" x2="94.44444444444444" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666666" x2="116.66666666666666" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="138.88888888888889" x2="138.88888888888889" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="161.11111111111111" x2="161.11111111111111" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="183.33333333333334" x2="183.33333333333334" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="205.55555555555557" x2="205.55555555555557" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="227.7777777777778" x2="227.7777777777778" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="250.00000000000003" x2="250.00000000000003" y1="50.0" y2="250.00000000000003"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t5ee73c1da7b4431fb0c8913fe2386ff6";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tb9da311c43114318938c31dbb612a394";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t94f1c1c695c049b7b807419cd74de839","data","table data",[null, null, null, null, null, null, null, null, null],[[null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null]],"toyplot");
    })();</script></div></div>


And you can use slicing with steps to access every-other-column,
every-third-row, etc:

.. code:: python

    canvas, table = toyplot.table(rows=9, columns=9, width=300, height=300)
    table.cells.grid.hlines[...] = "single"
    table.cells.grid.vlines[...] = "single"
    
    table.cells.column[0:6:2].style = {"fill":"red", "opacity":0.5}
    table.cells.row[0:8:3].style = {"fill":"green", "opacity":0.5}
    table.cells.cell[5:9:2, 6:9:2].style = {"fill":"blue", "opacity":0.5}



.. raw:: html

    <div class="toyplot" id="t58025be6ceee4db792fbd112652e1007" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="td0b0d9d2d53c475a806a90ff4e27ca0d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="te983c53fe1d848c5908e6c4cefd9ea7d"><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="161.11111111111111" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="50.0"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="94.44444444444444"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="161.11111111111111" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="161.11111111111111" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="227.7777777777778"></rect><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="50.0" y2="50.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="72.22222222222223" y2="72.22222222222223"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="94.44444444444444" y2="94.44444444444444"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="116.66666666666666" y2="116.66666666666666"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="138.88888888888889" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="161.11111111111111" y2="161.11111111111111"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="183.33333333333334" y2="183.33333333333334"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="205.55555555555557" y2="205.55555555555557"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="227.7777777777778" y2="227.7777777777778"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="250.00000000000003" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="50.0" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="72.22222222222223" x2="72.22222222222223" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="94.44444444444444" x2="94.44444444444444" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666666" x2="116.66666666666666" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="138.88888888888889" x2="138.88888888888889" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="161.11111111111111" x2="161.11111111111111" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="183.33333333333334" x2="183.33333333333334" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="205.55555555555557" x2="205.55555555555557" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="227.7777777777778" x2="227.7777777777778" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="250.00000000000003" x2="250.00000000000003" y1="50.0" y2="250.00000000000003"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t58025be6ceee4db792fbd112652e1007";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "td0b0d9d2d53c475a806a90ff4e27ca0d";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"te983c53fe1d848c5908e6c4cefd9ea7d","data","table data",[null, null, null, null, null, null, null, null, null],[[null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null]],"toyplot");
    })();</script></div></div>


Plus, you can use advanced slicing, such as an explicit list of indices:

.. code:: python

    canvas, table = toyplot.table(rows=9, columns=9, width=300, height=300)
    table.cells.grid.hlines[...] = "single"
    table.cells.grid.vlines[...] = "single"
    
    table.cells.column[[1,2,4]].style = {"fill":"red", "opacity":0.5}
    table.cells.row[[1,7,8]].style = {"fill":"green", "opacity":0.5}
    table.cells.cell[[3,4,6], 6:9].style = {"fill":"blue", "opacity":0.5}



.. raw:: html

    <div class="toyplot" id="t817b05e966b94937aa38cca05574485c" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t2293fbf33b8a414390c190a0db5e1f0b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="tc25533934f904ae786dbc4df45206ba8"><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="50.0"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="50.0"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="161.11111111111111" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="72.22222222222223"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="94.44444444444444"></rect><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="94.44444444444444"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="116.66666666666666"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="138.88888888888889"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="161.11111111111111"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="183.33333333333334"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="161.11111111111111" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="205.55555555555557"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="50.0" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="72.22222222222223" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.222222222222214" x="94.44444444444444" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="116.66666666666666" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="138.88888888888889" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="161.11111111111111" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="183.33333333333334" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="205.55555555555557" y="227.7777777777778"></rect><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="22.22222222222223" x="227.7777777777778" y="227.7777777777778"></rect><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="50.0" y2="50.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="72.22222222222223" y2="72.22222222222223"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="94.44444444444444" y2="94.44444444444444"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="116.66666666666666" y2="116.66666666666666"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="138.88888888888889" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="161.11111111111111" y2="161.11111111111111"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="183.33333333333334" y2="183.33333333333334"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="205.55555555555557" y2="205.55555555555557"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="227.7777777777778" y2="227.7777777777778"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000003" y1="250.00000000000003" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="50.0" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="72.22222222222223" x2="72.22222222222223" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="94.44444444444444" x2="94.44444444444444" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666666" x2="116.66666666666666" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="138.88888888888889" x2="138.88888888888889" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="161.11111111111111" x2="161.11111111111111" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="183.33333333333334" x2="183.33333333333334" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="205.55555555555557" x2="205.55555555555557" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="227.7777777777778" x2="227.7777777777778" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="250.00000000000003" x2="250.00000000000003" y1="50.0" y2="250.00000000000003"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t817b05e966b94937aa38cca05574485c";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t2293fbf33b8a414390c190a0db5e1f0b";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tc25533934f904ae786dbc4df45206ba8","data","table data",[null, null, null, null, null, null, null, null, null],[[null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null]],"toyplot");
    })();</script></div></div>


Of course, you can use any indexing technique to set any property of a
cell, and you can use all of these techniques when working with
gridlines and other properties of the table:

.. code:: python

    canvas, table = toyplot.table(rows=9, columns=9, width=300, height=300)
    
    table.cells.column[3].data = "A"
    table.cells.column[3].style = {"fill":"red", "opacity":0.5}
    table.cells.column[2:5].width = 35
    
    table.cells.row[2:4].data = "B"
    table.cells.row[2:4].style = {"fill":"green", "opacity":0.5}
    
    table.cells.cell[1:5, 1:6].lstyle = {"fill":"white"}
    
    table.cells.grid.hlines[..., 3] = "single"
    table.cells.grid.hlines[2:5, ...] = "single"
    
    table.cells.grid.vlines[2:4, ...] = "single"
    table.cells.grid.vlines[..., 3:5] = "single"



.. raw:: html

    <div class="toyplot" id="t6c419c1a09974d2995866e95bf0eb9f7" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t213f57c28ed249afb767f4d217a8a061" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="tef8db3b2266c4648bb728a680eaf527b"><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.000000000000014" x="116.66666666666667" y="50.0"></rect><g transform="translate(134.16666666666669,61.111111111111114)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">A</text></g><rect height="22.222222222222214" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.000000000000014" x="116.66666666666667" y="72.22222222222223"></rect><g transform="translate(134.16666666666669,83.33333333333334)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">A</text></g><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333329" x="50.0" y="94.44444444444444"></rect><g transform="translate(57.916666666666664,105.55555555555554)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333343" x="65.83333333333333" y="94.44444444444444"></rect><g transform="translate(73.75,105.55555555555554)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.0" x="81.66666666666667" y="94.44444444444444"></rect><g transform="translate(99.16666666666667,105.55555555555554)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.000000000000014" x="116.66666666666667" y="94.44444444444444"></rect><g transform="translate(134.16666666666669,105.55555555555554)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.0" x="151.66666666666669" y="94.44444444444444"></rect><g transform="translate(169.16666666666669,105.55555555555554)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333343" x="186.66666666666669" y="94.44444444444444"></rect><g transform="translate(194.58333333333337,105.55555555555554)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333343" x="202.50000000000003" y="94.44444444444444"></rect><g transform="translate(210.41666666666669,105.55555555555554)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333343" x="218.33333333333337" y="94.44444444444444"></rect><g transform="translate(226.25000000000006,105.55555555555554)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.222222222222214" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333343" x="234.1666666666667" y="94.44444444444444"></rect><g transform="translate(242.08333333333337,105.55555555555554)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333329" x="50.0" y="116.66666666666666"></rect><g transform="translate(57.916666666666664,127.77777777777777)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333343" x="65.83333333333333" y="116.66666666666666"></rect><g transform="translate(73.75,127.77777777777777)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.0" x="81.66666666666667" y="116.66666666666666"></rect><g transform="translate(99.16666666666667,127.77777777777777)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.000000000000014" x="116.66666666666667" y="116.66666666666666"></rect><g transform="translate(134.16666666666669,127.77777777777777)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.0" x="151.66666666666669" y="116.66666666666666"></rect><g transform="translate(169.16666666666669,127.77777777777777)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333343" x="186.66666666666669" y="116.66666666666666"></rect><g transform="translate(194.58333333333337,127.77777777777777)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333343" x="202.50000000000003" y="116.66666666666666"></rect><g transform="translate(210.41666666666669,127.77777777777777)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333343" x="218.33333333333337" y="116.66666666666666"></rect><g transform="translate(226.25000000000006,127.77777777777777)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.22222222222223" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="15.833333333333343" x="234.1666666666667" y="116.66666666666666"></rect><g transform="translate(242.08333333333337,127.77777777777777)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">B</text></g><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.000000000000014" x="116.66666666666667" y="138.88888888888889"></rect><g transform="translate(134.16666666666669,150.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">A</text></g><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.000000000000014" x="116.66666666666667" y="161.11111111111111"></rect><g transform="translate(134.16666666666669,172.22222222222223)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">A</text></g><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.000000000000014" x="116.66666666666667" y="183.33333333333334"></rect><g transform="translate(134.16666666666669,194.44444444444446)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">A</text></g><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.000000000000014" x="116.66666666666667" y="205.55555555555557"></rect><g transform="translate(134.16666666666669,216.66666666666669)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">A</text></g><rect height="22.22222222222223" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.5;stroke:none" width="35.000000000000014" x="116.66666666666667" y="227.7777777777778"></rect><g transform="translate(134.16666666666669,238.8888888888889)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.002" y="3.066">A</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666667" x2="151.66666666666669" y1="50.0" y2="50.0"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666667" x2="151.66666666666669" y1="72.22222222222223" y2="72.22222222222223"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000006" y1="94.44444444444444" y2="94.44444444444444"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000006" y1="116.66666666666666" y2="116.66666666666666"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.00000000000006" y1="138.88888888888889" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666667" x2="151.66666666666669" y1="161.11111111111111" y2="161.11111111111111"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666667" x2="151.66666666666669" y1="183.33333333333334" y2="183.33333333333334"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666667" x2="151.66666666666669" y1="205.55555555555557" y2="205.55555555555557"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666667" x2="151.66666666666669" y1="227.7777777777778" y2="227.7777777777778"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666667" x2="151.66666666666669" y1="250.00000000000003" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="50.0" y1="94.44444444444444" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="65.83333333333333" x2="65.83333333333333" y1="94.44444444444444" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="81.66666666666667" x2="81.66666666666667" y1="94.44444444444444" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="116.66666666666667" x2="116.66666666666667" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="151.66666666666669" x2="151.66666666666669" y1="50.0" y2="250.00000000000003"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="186.66666666666669" x2="186.66666666666669" y1="94.44444444444444" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="202.50000000000003" x2="202.50000000000003" y1="94.44444444444444" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="218.33333333333337" x2="218.33333333333337" y1="94.44444444444444" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="234.1666666666667" x2="234.1666666666667" y1="94.44444444444444" y2="138.88888888888889"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="250.00000000000006" x2="250.00000000000006" y1="94.44444444444444" y2="138.88888888888889"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t6c419c1a09974d2995866e95bf0eb9f7";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t213f57c28ed249afb767f4d217a8a061";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tef8db3b2266c4648bb728a680eaf527b","data","table data",[null, null, null, "A", null, null, null, null, null],[[null, "B", "B", null, null, null, null, null], [null, "B", "B", null, null, null, null, null], [null, "B", "B", null, null, null, null, null], ["A", "B", "B", "A", "A", "A", "A", "A"], [null, "B", "B", null, null, null, null, null], [null, "B", "B", null, null, null, null, null], [null, "B", "B", null, null, null, null, null], [null, "B", "B", null, null, null, null, null], [null, "B", "B", null, null, null, null, null]],"toyplot");
    })();</script></div></div>


Grouping Data
-------------

It's common to group-together subsets of data within a table. Toyplot
currently provides three mechanisms that you may find useful for
grouping. First, as we've already seen, you can use horizontal or
vertical grid lines to separate groups:

.. code:: python

    numpy.random.seed(1234)
    data = toyplot.data.Table(numpy.random.normal(size=(10, 4)))

.. code:: python

    canvas, table = toyplot.table(data, width=500, height=400)
    table.body.grid.hlines[[3, 7],...] = "single"



.. raw:: html

    <div class="toyplot" id="t760df06cfd0a48a5909ace02d872abd5" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t89d3b7fd6a594b13af3119be1439ab34" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 400.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="teb08535a966e4eba9bcc7cecee26ae63"><g transform="translate(100.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">0</text></g><g transform="translate(200.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">1</text></g><g transform="translate(300.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">2</text></g><g transform="translate(400.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">3</text></g><g transform="translate(98.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">471435</text></g><g transform="translate(198.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-1</text></g><g transform="translate(200.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">19098</text></g><g transform="translate(298.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(300.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">43271</text></g><g transform="translate(398.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(400.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">312652</text></g><g transform="translate(98.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(100.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">720589</text></g><g transform="translate(198.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(200.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">887163</text></g><g transform="translate(298.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">859588</text></g><g transform="translate(398.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(400.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">636524</text></g><g transform="translate(98.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0156964</text></g><g transform="translate(198.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-2</text></g><g transform="translate(200.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">24268</text></g><g transform="translate(298.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(300.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">15004</text></g><g transform="translate(398.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">991946</text></g><g transform="translate(98.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">953324</text></g><g transform="translate(198.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-2</text></g><g transform="translate(200.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">02125</text></g><g transform="translate(298.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(300.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">334077</text></g><g transform="translate(398.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">00211836</text></g><g transform="translate(98.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">405453</text></g><g transform="translate(198.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(200.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">289092</text></g><g transform="translate(298.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(300.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">32116</text></g><g transform="translate(398.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-1</text></g><g transform="translate(400.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">54691</text></g><g transform="translate(98.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(100.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">202646</text></g><g transform="translate(198.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(200.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">655969</text></g><g transform="translate(298.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">193421</text></g><g transform="translate(398.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">553439</text></g><g transform="translate(98.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(100.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">31815</text></g><g transform="translate(198.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(200.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">469305</text></g><g transform="translate(298.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">675554</text></g><g transform="translate(398.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-1</text></g><g transform="translate(400.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">81703</text></g><g transform="translate(98.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(100.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">183109</text></g><g transform="translate(198.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(200.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">05897</text></g><g transform="translate(298.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(300.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">39784</text></g><g transform="translate(398.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">337438</text></g><g transform="translate(98.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(100.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">04758</text></g><g transform="translate(198.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(200.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">04594</text></g><g transform="translate(298.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">863717</text></g><g transform="translate(398.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(400.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">122092</text></g><g transform="translate(98.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">124713</text></g><g transform="translate(198.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(200.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">322795</text></g><g transform="translate(298.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">841675</text></g><g transform="translate(398.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(400.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">39096</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="450.0" y1="77.27272727272728" y2="77.27272727272728"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="450.0" y1="159.0909090909091" y2="159.0909090909091"></line><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="450.0" y1="268.18181818181824" y2="268.18181818181824"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t760df06cfd0a48a5909ace02d872abd5";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t89d3b7fd6a594b13af3119be1439ab34";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"teb08535a966e4eba9bcc7cecee26ae63","data","table data",["0", "1", "2", "3"],[[0.47143516373249306, -0.7205887333650116, 0.015696372114428918, 0.9533241281124304, 0.405453411570191, -0.2026463246291819, 1.3181515541801367, -0.1831085401789987, 1.0475785728927218, 0.12471295376821585], [-1.1909756947064645, 0.8871629403077386, -2.2426849541854055, -2.0212548201949705, 0.2890919409800353, -0.6559693441389339, -0.4693052847058996, 1.0589691875711504, 1.0459382556276653, -0.32279480560829565], [1.4327069684260973, 0.8595884137174165, 1.150035724719818, -0.334077365808097, 1.3211581921293856, 0.19342137647035826, 0.6755540851223808, -0.3978402281999914, 0.8637172916848387, 0.8416747129961416], [-0.3126518960917129, -0.6365235044173491, 0.9919460223426778, 0.002118364683486495, -1.5469055532292402, 0.5534389109567419, -1.8170272265901968, 0.3374376536139724, -0.12209157484767426, 2.390960515463033]],"toyplot");
    })();</script></div></div>


Second, you could change the background colors of cells to highlight
groups:

.. code:: python

    canvas, table = toyplot.table(data, width=500, height=400)
    table.body.row[3:7].style = {"fill":"#eee", "stroke":"none"}



.. raw:: html

    <div class="toyplot" id="tad369264fdcb4a52a1bf641dca29ca6c" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="tc46523b257ab424482de56b44315a104" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 400.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t4b0e6ac9dcac4689bb75d3211090c0bf"><g transform="translate(100.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">0</text></g><g transform="translate(200.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">1</text></g><g transform="translate(300.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">2</text></g><g transform="translate(400.0,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">3</text></g><g transform="translate(98.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">471435</text></g><g transform="translate(198.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-1</text></g><g transform="translate(200.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">19098</text></g><g transform="translate(298.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(300.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">43271</text></g><g transform="translate(398.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(400.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">312652</text></g><g transform="translate(98.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(100.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">720589</text></g><g transform="translate(198.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(200.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">887163</text></g><g transform="translate(298.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">859588</text></g><g transform="translate(398.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(400.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">636524</text></g><g transform="translate(98.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0156964</text></g><g transform="translate(198.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-2</text></g><g transform="translate(200.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">24268</text></g><g transform="translate(298.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(300.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">15004</text></g><g transform="translate(398.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">991946</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="50.0" y="159.0909090909091"></rect><g transform="translate(98.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">953324</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="150.0" y="159.0909090909091"></rect><g transform="translate(198.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-2</text></g><g transform="translate(200.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">02125</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="250.0" y="159.0909090909091"></rect><g transform="translate(298.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(300.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">334077</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="350.0" y="159.0909090909091"></rect><g transform="translate(398.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">00211836</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="50.0" y="186.36363636363637"></rect><g transform="translate(98.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">405453</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="150.0" y="186.36363636363637"></rect><g transform="translate(198.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(200.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">289092</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="250.0" y="186.36363636363637"></rect><g transform="translate(298.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(300.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">32116</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="350.0" y="186.36363636363637"></rect><g transform="translate(398.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-1</text></g><g transform="translate(400.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">54691</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="50.0" y="213.63636363636365"></rect><g transform="translate(98.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(100.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">202646</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="150.0" y="213.63636363636365"></rect><g transform="translate(198.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(200.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">655969</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="250.0" y="213.63636363636365"></rect><g transform="translate(298.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">193421</text></g><rect height="27.27272727272728" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="350.0" y="213.63636363636365"></rect><g transform="translate(398.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">553439</text></g><rect height="27.27272727272731" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="50.0" y="240.90909090909093"></rect><g transform="translate(98.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(100.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">31815</text></g><rect height="27.27272727272731" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="150.0" y="240.90909090909093"></rect><g transform="translate(198.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(200.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">469305</text></g><rect height="27.27272727272731" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="250.0" y="240.90909090909093"></rect><g transform="translate(298.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">675554</text></g><rect height="27.27272727272731" style="fill:rgb(93.3%,93.3%,93.3%);fill-opacity:1.0;stroke:none" width="100.0" x="350.0" y="240.90909090909093"></rect><g transform="translate(398.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-1</text></g><g transform="translate(400.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">81703</text></g><g transform="translate(98.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(100.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">183109</text></g><g transform="translate(198.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(200.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">05897</text></g><g transform="translate(298.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(300.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">39784</text></g><g transform="translate(398.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">337438</text></g><g transform="translate(98.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(100.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">04758</text></g><g transform="translate(198.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(200.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">04594</text></g><g transform="translate(298.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">863717</text></g><g transform="translate(398.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(400.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">122092</text></g><g transform="translate(98.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">124713</text></g><g transform="translate(198.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(200.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">322795</text></g><g transform="translate(298.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">841675</text></g><g transform="translate(398.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(400.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">39096</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="450.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tad369264fdcb4a52a1bf641dca29ca6c";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tc46523b257ab424482de56b44315a104";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t4b0e6ac9dcac4689bb75d3211090c0bf","data","table data",["0", "1", "2", "3"],[[0.47143516373249306, -0.7205887333650116, 0.015696372114428918, 0.9533241281124304, 0.405453411570191, -0.2026463246291819, 1.3181515541801367, -0.1831085401789987, 1.0475785728927218, 0.12471295376821585], [-1.1909756947064645, 0.8871629403077386, -2.2426849541854055, -2.0212548201949705, 0.2890919409800353, -0.6559693441389339, -0.4693052847058996, 1.0589691875711504, 1.0459382556276653, -0.32279480560829565], [1.4327069684260973, 0.8595884137174165, 1.150035724719818, -0.334077365808097, 1.3211581921293856, 0.19342137647035826, 0.6755540851223808, -0.3978402281999914, 0.8637172916848387, 0.8416747129961416], [-0.3126518960917129, -0.6365235044173491, 0.9919460223426778, 0.002118364683486495, -1.5469055532292402, 0.5534389109567419, -1.8170272265901968, 0.3374376536139724, -0.12209157484767426, 2.390960515463033]],"toyplot");
    })();</script></div></div>


Finally, you can use the ``gaps`` property to insert whitespace between
groups:

.. code:: python

    canvas, table = toyplot.table(data, width=500, height=400)
    table.body.gaps.rows[[2,6]] = "0.5cm"



.. raw:: html

    <div class="toyplot" id="t5efca85635e546f18faf80f2c8392158" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t561bed4dd1f64e45a72e490df8eed5ef" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 400.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t537f37d34dd04980848a2abb8fd78e44"><g transform="translate(100.0,61.918396563636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">0</text></g><g transform="translate(200.0,61.918396563636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">1</text></g><g transform="translate(300.0,61.918396563636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">2</text></g><g transform="translate(400.0,61.918396563636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">3</text></g><g transform="translate(98.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">471435</text></g><g transform="translate(198.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-1</text></g><g transform="translate(200.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">19098</text></g><g transform="translate(298.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(300.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">43271</text></g><g transform="translate(398.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(400.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,85.75518969090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">312652</text></g><g transform="translate(98.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(100.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">720589</text></g><g transform="translate(198.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(200.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">887163</text></g><g transform="translate(298.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">859588</text></g><g transform="translate(398.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(400.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,109.5919828181818)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">636524</text></g><g transform="translate(98.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0156964</text></g><g transform="translate(198.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-2</text></g><g transform="translate(200.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">24268</text></g><g transform="translate(298.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(300.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">15004</text></g><g transform="translate(398.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,133.42877594545453)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">991946</text></g><g transform="translate(98.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">953324</text></g><g transform="translate(198.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-2</text></g><g transform="translate(200.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">02125</text></g><g transform="translate(298.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(300.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">334077</text></g><g transform="translate(398.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,176.16320687272724)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">00211836</text></g><g transform="translate(98.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">405453</text></g><g transform="translate(198.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(200.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">289092</text></g><g transform="translate(298.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(300.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">32116</text></g><g transform="translate(398.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-1</text></g><g transform="translate(400.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">54691</text></g><g transform="translate(98.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(100.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">202646</text></g><g transform="translate(198.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(200.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">655969</text></g><g transform="translate(298.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">193421</text></g><g transform="translate(398.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,223.8367931272727)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">553439</text></g><g transform="translate(98.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(100.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">31815</text></g><g transform="translate(198.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(200.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">469305</text></g><g transform="translate(298.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">675554</text></g><g transform="translate(398.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-1</text></g><g transform="translate(400.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,247.67358625454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">81703</text></g><g transform="translate(98.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(100.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">183109</text></g><g transform="translate(198.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(200.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">05897</text></g><g transform="translate(298.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(300.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">39784</text></g><g transform="translate(398.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(400.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,290.4080171818182)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">337438</text></g><g transform="translate(98.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(100.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">04758</text></g><g transform="translate(198.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(200.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">04594</text></g><g transform="translate(298.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">863717</text></g><g transform="translate(398.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(400.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,314.2448103090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">122092</text></g><g transform="translate(98.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(100.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(102.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">124713</text></g><g transform="translate(198.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-10.668" y="3.066">-0</text></g><g transform="translate(200.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(202.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">322795</text></g><g transform="translate(298.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(300.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(302.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">841675</text></g><g transform="translate(398.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(400.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(402.0,338.0816034363636)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">39096</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="450.0" y1="73.83679312727273" y2="73.83679312727273"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t5efca85635e546f18faf80f2c8392158";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t561bed4dd1f64e45a72e490df8eed5ef";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t537f37d34dd04980848a2abb8fd78e44","data","table data",["0", "1", "2", "3"],[[0.47143516373249306, -0.7205887333650116, 0.015696372114428918, 0.9533241281124304, 0.405453411570191, -0.2026463246291819, 1.3181515541801367, -0.1831085401789987, 1.0475785728927218, 0.12471295376821585], [-1.1909756947064645, 0.8871629403077386, -2.2426849541854055, -2.0212548201949705, 0.2890919409800353, -0.6559693441389339, -0.4693052847058996, 1.0589691875711504, 1.0459382556276653, -0.32279480560829565], [1.4327069684260973, 0.8595884137174165, 1.150035724719818, -0.334077365808097, 1.3211581921293856, 0.19342137647035826, 0.6755540851223808, -0.3978402281999914, 0.8637172916848387, 0.8416747129961416], [-0.3126518960917129, -0.6365235044173491, 0.9919460223426778, 0.002118364683486495, -1.5469055532292402, 0.5534389109567419, -1.8170272265901968, 0.3374376536139724, -0.12209157484767426, 2.390960515463033]],"toyplot");
    })();</script></div></div>


Because a ref:\ ``matrix-visualization`` is actually a table, you can
use gaps to adjust its appearance, too:

.. code:: python

    canvas, table = toyplot.matrix(data, width=400, height=700)
    table.body.gaps.columns[...] = 10
    table.body.gaps.rows[...] = 10



.. raw:: html

    <div class="toyplot" id="t3d3a606c3f1e4888a60ed481572a8d8f" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="700.0px" id="t8f2d1a6aaaac4e4e93b6534945e94f4c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 400.0 700.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t939021bd328146dcb16fc60f9a2cf2f8"><g transform="translate(113.75,80.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">0</text></g><g transform="translate(171.25,80.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">1</text></g><g transform="translate(228.75,80.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">2</text></g><g transform="translate(286.25,80.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">3</text></g><g transform="translate(85.0,111.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><rect height="43.0" style="fill:rgb(98.9%,87.4%,80.7%);fill-opacity:1.0;stroke:none" width="47.5" x="90.0" y="90.0"><title>0.471435</title></rect><rect height="43.0" style="fill:rgb(34.6%,62.9%,79.3%);fill-opacity:1.0;stroke:none" width="47.5" x="147.5" y="90.0"><title>-1.190976</title></rect><rect height="43.0" style="fill:rgb(84.7%,39.5%,31.6%);fill-opacity:1.0;stroke:none" width="47.5" x="205.0" y="90.0"><title>1.432707</title></rect><rect height="43.0" style="fill:rgb(84.4%,91%,94.6%);fill-opacity:1.0;stroke:none" width="47.5" x="262.5" y="90.0"><title>-0.312652</title></rect><g transform="translate(85.0,164.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><rect height="43.0" style="fill:rgb(64.3%,80.8%,89.1%);fill-opacity:1.0;stroke:none" width="47.5" x="90.0" y="143.0"><title>-0.720589</title></rect><rect height="43.0" style="fill:rgb(96.6%,69.9%,57.6%);fill-opacity:1.0;stroke:none" width="47.5" x="147.5" y="143.0"><title>0.887163</title></rect><rect height="43.0" style="fill:rgb(96.8%,71.2%,59.2%);fill-opacity:1.0;stroke:none" width="47.5" x="205.0" y="143.0"><title>0.859588</title></rect><rect height="43.0" style="fill:rgb(68.8%,83.1%,90.4%);fill-opacity:1.0;stroke:none" width="47.5" x="262.5" y="143.0"><title>-0.636524</title></rect><g transform="translate(85.0,217.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><rect height="43.0" style="fill:rgb(95%,96%,96.5%);fill-opacity:1.0;stroke:none" width="47.5" x="90.0" y="196.0"><title>0.015696</title></rect><rect height="43.0" style="fill:rgb(2%,18.8%,38%);fill-opacity:1.0;stroke:none" width="47.5" x="147.5" y="196.0"><title>-2.242685</title></rect><rect height="43.0" style="fill:rgb(91.9%,56%,44.3%);fill-opacity:1.0;stroke:none" width="47.5" x="205.0" y="196.0"><title>1.150036</title></rect><rect height="43.0" style="fill:rgb(95.8%,65.1%,51.5%);fill-opacity:1.0;stroke:none" width="47.5" x="262.5" y="196.0"><title>0.991946</title></rect><g transform="translate(85.0,270.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><rect height="43.0" style="fill:rgb(96%,66.9%,53.8%);fill-opacity:1.0;stroke:none" width="47.5" x="90.0" y="249.0"><title>0.953324</title></rect><rect height="43.0" style="fill:rgb(7.2%,28.9%,52.1%);fill-opacity:1.0;stroke:none" width="47.5" x="147.5" y="249.0"><title>-2.021255</title></rect><rect height="43.0" style="fill:rgb(83.7%,90.6%,94.4%);fill-opacity:1.0;stroke:none" width="47.5" x="205.0" y="249.0"><title>-0.334077</title></rect><rect height="43.0" style="fill:rgb(94.5%,95.8%,96.4%);fill-opacity:1.0;stroke:none" width="47.5" x="262.5" y="249.0"><title>0.002118</title></rect><g transform="translate(85.0,323.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><rect height="43.0" style="fill:rgb(98.5%,89%,83.4%);fill-opacity:1.0;stroke:none" width="47.5" x="90.0" y="302.0"><title>0.405453</title></rect><rect height="43.0" style="fill:rgb(98%,91.8%,88.1%);fill-opacity:1.0;stroke:none" width="47.5" x="147.5" y="302.0"><title>0.289092</title></rect><rect height="43.0" style="fill:rgb(87.6%,46%,36.6%);fill-opacity:1.0;stroke:none" width="47.5" x="205.0" y="302.0"><title>1.321158</title></rect><rect height="43.0" style="fill:rgb(19.6%,48.9%,72%);fill-opacity:1.0;stroke:none" width="47.5" x="262.5" y="302.0"><title>-1.546906</title></rect><g transform="translate(85.0,376.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><rect height="43.0" style="fill:rgb(88%,92.6%,95.2%);fill-opacity:1.0;stroke:none" width="47.5" x="90.0" y="355.0"><title>-0.202646</title></rect><rect height="43.0" style="fill:rgb(67.7%,82.6%,90.1%);fill-opacity:1.0;stroke:none" width="47.5" x="147.5" y="355.0"><title>-0.655969</title></rect><rect height="43.0" style="fill:rgb(97.5%,94%,92%);fill-opacity:1.0;stroke:none" width="47.5" x="205.0" y="355.0"><title>0.193421</title></rect><rect height="43.0" style="fill:rgb(99.1%,85.2%,77.1%);fill-opacity:1.0;stroke:none" width="47.5" x="262.5" y="355.0"><title>0.553439</title></rect><g transform="translate(85.0,429.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">6</text></g><rect height="43.0" style="fill:rgb(87.6%,46.2%,36.7%);fill-opacity:1.0;stroke:none" width="47.5" x="90.0" y="408.0"><title>1.318152</title></rect><rect height="43.0" style="fill:rgb(77.7%,87.6%,92.9%);fill-opacity:1.0;stroke:none" width="47.5" x="147.5" y="408.0"><title>-0.469305</title></rect><rect height="43.0" style="fill:rgb(98.2%,79.6%,70%);fill-opacity:1.0;stroke:none" width="47.5" x="205.0" y="408.0"><title>0.675554</title></rect><rect height="43.0" style="fill:rgb(12%,38.3%,65.1%);fill-opacity:1.0;stroke:none" width="47.5" x="262.5" y="408.0"><title>-1.817027</title></rect><g transform="translate(85.0,482.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">7</text></g><rect height="43.0" style="fill:rgb(88.6%,92.9%,95.3%);fill-opacity:1.0;stroke:none" width="47.5" x="90.0" y="461.0"><title>-0.183109</title></rect><rect height="43.0" style="fill:rgb(94.2%,61.3%,48.4%);fill-opacity:1.0;stroke:none" width="47.5" x="147.5" y="461.0"><title>1.058969</title></rect><rect height="43.0" style="fill:rgb(81.5%,89.6%,94%);fill-opacity:1.0;stroke:none" width="47.5" x="205.0" y="461.0"><title>-0.397840</title></rect><rect height="43.0" style="fill:rgb(98.2%,90.6%,86.2%);fill-opacity:1.0;stroke:none" width="47.5" x="262.5" y="461.0"><title>0.337438</title></rect><g transform="translate(85.0,535.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">8</text></g><rect height="43.0" style="fill:rgb(94.5%,62%,48.9%);fill-opacity:1.0;stroke:none" width="47.5" x="90.0" y="514.0"><title>1.047579</title></rect><rect height="43.0" style="fill:rgb(94.5%,62.1%,49%);fill-opacity:1.0;stroke:none" width="47.5" x="147.5" y="514.0"><title>1.045938</title></rect><rect height="43.0" style="fill:rgb(96.7%,71%,59%);fill-opacity:1.0;stroke:none" width="47.5" x="205.0" y="514.0"><title>0.863717</title></rect><rect height="43.0" style="fill:rgb(90.6%,93.9%,95.7%);fill-opacity:1.0;stroke:none" width="47.5" x="262.5" y="514.0"><title>-0.122092</title></rect><g transform="translate(85.0,588.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">9</text></g><rect height="43.0" style="fill:rgb(97.1%,95.7%,94.8%);fill-opacity:1.0;stroke:none" width="47.5" x="90.0" y="567.0"><title>0.124713</title></rect><rect height="43.0" style="fill:rgb(84.1%,90.8%,94.5%);fill-opacity:1.0;stroke:none" width="47.5" x="147.5" y="567.0"><title>-0.322795</title></rect><rect height="43.0" style="fill:rgb(96.9%,72%,60.3%);fill-opacity:1.0;stroke:none" width="47.5" x="205.0" y="567.0"><title>0.841675</title></rect><rect height="43.0" style="fill:rgb(40.4%,0%,12.2%);fill-opacity:1.0;stroke:none" width="47.5" x="262.5" y="567.0"><title>2.390961</title></rect></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t3d3a606c3f1e4888a60ed481572a8d8f";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t8f2d1a6aaaac4e4e93b6534945e94f4c";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t939021bd328146dcb16fc60f9a2cf2f8","data","table data",[null, null, null, null, null, null, null, null],[[null, null, null, null, null, null, null, null, null, null, null, null, null], [null, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", null, null], ["0", 0.47143516373249306, -0.7205887333650116, 0.015696372114428918, 0.9533241281124304, 0.405453411570191, -0.2026463246291819, 1.3181515541801367, -0.1831085401789987, 1.0475785728927218, 0.12471295376821585, null, null], ["1", -1.1909756947064645, 0.8871629403077386, -2.2426849541854055, -2.0212548201949705, 0.2890919409800353, -0.6559693441389339, -0.4693052847058996, 1.0589691875711504, 1.0459382556276653, -0.32279480560829565, null, null], ["2", 1.4327069684260973, 0.8595884137174165, 1.150035724719818, -0.334077365808097, 1.3211581921293856, 0.19342137647035826, 0.6755540851223808, -0.3978402281999914, 0.8637172916848387, 0.8416747129961416, null, null], ["3", -0.3126518960917129, -0.6365235044173491, 0.9919460223426778, 0.002118364683486495, -1.5469055532292402, 0.5534389109567419, -1.8170272265901968, 0.3374376536139724, -0.12209157484767426, 2.390960515463033, null, null], [null, null, null, null, null, null, null, null, null, null, null, null, null], [null, null, null, null, null, null, null, null, null, null, null, null, null]],"toyplot");
    })();</script></div></div>


Plot Embedding
--------------

Nearly any type of plot can be embedded in a table, but the fact that
they're embedded introduces additional considerations. As an example,
assume we have the following table:

.. code:: python

    data = toyplot.data.Table(numpy.random.normal(loc=4, size=(10, 2)))
    
    canvas, table = toyplot.table(data, width=250, height=400)
    table.cells.cell[...].format = toyplot.format.FloatFormatter(format="{:.1f}")



.. raw:: html

    <div class="toyplot" id="tab48a39993254b879ca47bf0550a4bba" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t1a3a3c51476f46e7b6ccff4f20840a40" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 250.0 400.0" width="250.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t1d03d74694624504bf234b7f39f4f340"><g transform="translate(87.5,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">0</text></g><g transform="translate(162.5,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">1</text></g><g transform="translate(85.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(160.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(162.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(164.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(85.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(160.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(162.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(164.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(85.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(160.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(162.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(164.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(85.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(87.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(160.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(162.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(164.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(85.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">8</text></g><g transform="translate(160.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(162.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(164.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(85.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">8</text></g><g transform="translate(160.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(162.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(164.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(85.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(87.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(160.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(162.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(164.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(85.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(87.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">5</text></g><g transform="translate(160.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(162.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(164.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(85.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(160.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(162.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(164.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(85.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(160.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(162.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(164.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">5</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="200.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tab48a39993254b879ca47bf0550a4bba";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t1a3a3c51476f46e7b6ccff4f20840a40";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t1d03d74694624504bf234b7f39f4f340","data","table data",["0", "1"],[[4.076199587837237, 4.036141936684072, 4.247792199748547, 3.8632051667386524, 4.755413982398135, 4.841008794931391, 2.598026718499156, 3.451757550813145, 4.354020332199238, 4.565738306062595], [3.433554069535043, 1.9250223993099707, 3.102843215560301, 4.018289191349219, 4.215268580969443, 2.5541899229556937, 3.899081800051086, 3.8553804916306156, 3.9644869747218596, 5.545658804625558]],"toyplot");
    })();</script></div></div>


As we saw earlier, we can create a set of axes that are "contained"
within a range of cells, and add a plot that uses the underlying data:

.. code:: python

    canvas, table = toyplot.table(data, width=250, height=400)
    table.cells.cell[...].format = toyplot.format.FloatFormatter(format="{:.1f}")
    
    axes = table.body.column[1].cartesian()
    axes.cell_plot();



.. raw:: html

    <div class="toyplot" id="tb0001d7562f54c1f8d51659e66e794b9" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t0c183af6c1bf4050820176fb93dba874" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 250.0 400.0" width="250.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t8a7d2fdd5c584cb3863b563039d18849"><g transform="translate(87.5,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">0</text></g><g transform="translate(162.5,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">1</text></g><g transform="translate(85.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(85.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(85.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(85.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(87.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(85.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">8</text></g><g transform="translate(85.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">8</text></g><g transform="translate(85.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(87.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(85.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(87.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">5</text></g><g transform="translate(85.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(85.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g class="toyplot-coordinates-Cartesian" id="t89898f208ec94a669e942e0c7575bd24"><clipPath id="tf83f4a78a5f048edbb0537bda138f27f"><rect height="272.72727272727275" width="75.0" x="125.0" y="77.27272727272728"></rect></clipPath><g clip-path="url(#tf83f4a78a5f048edbb0537bda138f27f)"><g class="toyplot-mark-Plot" id="ta7a6a19dd45a4c29beb7cb067cfc8c51" style="fill:none"><g class="toyplot-Series"><path d="M 156.74872635449216 90.9090909090909 L 128.0 118.18181818181819 L 150.44622967441796 145.45454545454544 L 167.89227099375603 172.72727272727275 L 171.6461905709445 200.0 L 139.9903117219446 227.2727272727273 L 165.62048529677324 254.5454545454546 L 164.7876509705798 281.81818181818187 L 166.86693938579964 309.0909090909091 L 197.0 336.3636363636364" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="200.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tb0001d7562f54c1f8d51659e66e794b9";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t0c183af6c1bf4050820176fb93dba874";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t8a7d2fdd5c584cb3863b563039d18849","data","table data",["0", "1"],[[4.076199587837237, 4.036141936684072, 4.247792199748547, 3.8632051667386524, 4.755413982398135, 4.841008794931391, 2.598026718499156, 3.451757550813145, 4.354020332199238, 4.565738306062595], [3.433554069535043, 1.9250223993099707, 3.102843215560301, 4.018289191349219, 4.215268580969443, 2.5541899229556937, 3.899081800051086, 3.8553804916306156, 3.9644869747218596, 5.545658804625558]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"ta7a6a19dd45a4c29beb7cb067cfc8c51","data","plot data",["y", "x0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [3.433554069535043, 1.9250223993099707, 3.102843215560301, 4.018289191349219, 4.215268580969443, 2.5541899229556937, 3.899081800051086, 3.8553804916306156, 3.9644869747218596, 5.545658804625558]],"toyplot");
    })();</script></div></div>


And as you might imagine, other plot types are supported:

.. code:: python

    canvas, table = toyplot.table(data, width=250, height=400)
    table.cells.cell[...].format = toyplot.format.FloatFormatter(format="{:.1f}")
    
    axes = table.body.column[1].cartesian()
    axes.cell_bars();



.. raw:: html

    <div class="toyplot" id="t8da99975c6ff47f58dc378e7a7dda375" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="tf644ddc1e934495a8e9f3da14f8eb6db" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 250.0 400.0" width="250.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t63ec49e625254fecb9ded58b933594f1"><g transform="translate(87.5,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">0</text></g><g transform="translate(162.5,63.63636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">1</text></g><g transform="translate(85.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,90.9090909090909)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">1</text></g><g transform="translate(85.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,118.18181818181819)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(85.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,145.45454545454544)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(85.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(87.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,172.72727272727275)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(85.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,200.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">8</text></g><g transform="translate(85.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,227.2727272727273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">8</text></g><g transform="translate(85.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(87.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,254.5454545454546)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(85.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(87.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,281.81818181818187)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">5</text></g><g transform="translate(85.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,309.0909090909091)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">4</text></g><g transform="translate(85.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(87.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(89.5,336.3636363636364)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g class="toyplot-coordinates-Cartesian" id="t6c9d4be190624506a3cedc47df994685"><clipPath id="t53a78c4ac27648beaaa186434a47139b"><rect height="272.72727272727275" width="75.0" x="125.0" y="77.27272727272728"></rect></clipPath><g clip-path="url(#t53a78c4ac27648beaaa186434a47139b)"><g class="toyplot-mark-BarMagnitudes" id="t85622d0c163b49cc9b12ee534dfc3ae1" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="13.636363636363626" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="42.72084510505954" x="128.0" y="84.0909090909091"></rect><rect class="toyplot-Datum" height="13.63636363636364" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="23.951445668024007" x="128.0" y="111.36363636363636"></rect><rect class="toyplot-Datum" height="13.636363636363626" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="38.60608620477808" x="128.0" y="138.63636363636363"></rect><rect class="toyplot-Datum" height="13.636363636363654" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="49.996215773649055" x="128.0" y="165.9090909090909"></rect><rect class="toyplot-Datum" height="13.636363636363654" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="52.447065774096075" x="128.0" y="193.1818181818182"></rect><rect class="toyplot-Datum" height="13.636363636363598" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="31.779651596478345" x="128.0" y="220.4545454545455"></rect><rect class="toyplot-Datum" height="13.636363636363683" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="48.51301778232826" x="128.0" y="247.72727272727275"></rect><rect class="toyplot-Datum" height="13.636363636363626" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="47.969278907066496" x="128.0" y="275.00000000000006"></rect><rect class="toyplot-Datum" height="13.636363636363626" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="49.32679973525316" x="128.0" y="302.2727272727273"></rect><rect class="toyplot-Datum" height="13.636363636363626" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="69.0" x="128.0" y="329.54545454545456"></rect></g></g></g></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="200.0" y1="77.27272727272728" y2="77.27272727272728"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t8da99975c6ff47f58dc378e7a7dda375";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tf644ddc1e934495a8e9f3da14f8eb6db";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t63ec49e625254fecb9ded58b933594f1","data","table data",["0", "1"],[[4.076199587837237, 4.036141936684072, 4.247792199748547, 3.8632051667386524, 4.755413982398135, 4.841008794931391, 2.598026718499156, 3.451757550813145, 4.354020332199238, 4.565738306062595], [3.433554069535043, 1.9250223993099707, 3.102843215560301, 4.018289191349219, 4.215268580969443, 2.5541899229556937, 3.899081800051086, 3.8553804916306156, 3.9644869747218596, 5.545658804625558]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t85622d0c163b49cc9b12ee534dfc3ae1","data","bar data",["left", "right", "baseline", "magnitude0"],[[-0.25, 0.75, 1.75, 2.75, 3.75, 4.75, 5.75, 6.75, 7.75, 8.75], [0.25, 1.25, 2.25, 3.25, 4.25, 5.25, 6.25, 7.25, 8.25, 9.25], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [3.433554069535043, 1.9250223993099707, 3.102843215560301, 4.018289191349219, 4.215268580969443, 2.5541899229556937, 3.899081800051086, 3.8553804916306156, 3.9644869747218596, 5.545658804625558]],"toyplot");
    })();</script></div></div>


You can also plot data along rows instead of columns:

.. code:: python

    data = toyplot.data.Table(numpy.random.normal(loc=4, size=(2, 10)))
    
    canvas, table = toyplot.table(data, width=500, height=250)
    table.cells.cell[...].format = toyplot.format.FloatFormatter(format="{:.1f}")
    
    axes = table.body.row[1].cartesian()
    axes.cell_bars(series="rows");



.. raw:: html

    <div class="toyplot" id="t475dfc459a034c9d94cc722b348076e3" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="250.0px" id="tf92ea24d2fcd402e9dbeb8affd8ef82f" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 250.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t653af2adaead4013bd9d7ea33bd02366"><g transform="translate(70.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">0</text></g><g transform="translate(110.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">1</text></g><g transform="translate(150.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">2</text></g><g transform="translate(190.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">3</text></g><g transform="translate(230.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">4</text></g><g transform="translate(270.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">5</text></g><g transform="translate(310.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">6</text></g><g transform="translate(350.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">7</text></g><g transform="translate(390.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">8</text></g><g transform="translate(430.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">9</text></g><g transform="translate(68.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(70.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(72.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(108.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(110.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(112.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(148.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(150.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(152.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(188.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(190.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(192.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">8</text></g><g transform="translate(228.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(230.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(232.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(268.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(270.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(272.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(308.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">6</text></g><g transform="translate(310.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(312.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(348.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(350.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(352.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(388.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(390.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(392.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(428.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(430.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(432.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">7</text></g><g class="toyplot-coordinates-Cartesian" id="t9768408e87f14a27bfd7d698bdaab098"><clipPath id="tdc877de96b5d41f380f0e1bdca313877"><rect height="50.0" width="400.0" x="50.0" y="150.0"></rect></clipPath><g clip-path="url(#tdc877de96b5d41f380f0e1bdca313877)"><g class="toyplot-mark-BarMagnitudes" id="tb702db6050dc4fcaa065401195c4d582" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="23.542701072787395" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="20.0" x="60.0" y="173.4572989272126"></rect><rect class="toyplot-Datum" height="32.679054702937236" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="20.0" x="100.0" y="164.32094529706276"></rect><rect class="toyplot-Datum" height="34.45263859527677" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="20.0" x="140.0" y="162.54736140472323"></rect><rect class="toyplot-Datum" height="33.12908679837466" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="20.0" x="180.0" y="163.87091320162534"></rect><rect class="toyplot-Datum" height="22.511375765432774" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="20.0" x="220.0" y="174.48862423456723"></rect><rect class="toyplot-Datum" height="44.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="20.0" x="260.0" y="153.0"></rect><rect class="toyplot-Datum" height="30.957259263615498" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="20.0" x="300.0" y="166.0427407363845"></rect><rect class="toyplot-Datum" height="20.85324137454927" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="20.0" x="340.0" y="176.14675862545073"></rect><rect class="toyplot-Datum" height="33.92350587147243" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="20.0" x="380.0" y="163.07649412852757"></rect><rect class="toyplot-Datum" height="29.58442150880316" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="20.0" x="420.0" y="167.41557849119684"></rect></g></g></g></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="450.0" y1="100.0" y2="100.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t475dfc459a034c9d94cc722b348076e3";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tf92ea24d2fcd402e9dbeb8affd8ef82f";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t653af2adaead4013bd9d7ea33bd02366","data","table data",["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],[[3.0257636662326846, 3.214564788236803], [3.9296551228958974, 4.462059737162049], [4.307968855216034, 4.704228225462174], [3.79150123689412, 4.523507967893809], [5.033800732555499, 3.073745686469774], [1.5995463661877043, 6.0078429507780005], [6.0306036208388, 4.226962541870895], [2.8573687109772363, 2.847340890749048], [4.211883386777701, 4.6319794458091295], [4.704720624317109, 4.039512686693366]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tb702db6050dc4fcaa065401195c4d582","data","bar data",["left", "right", "baseline", "magnitude0"],[[-0.25, 0.75, 1.75, 2.75, 3.75, 4.75, 5.75, 6.75, 7.75, 8.75], [0.25, 1.25, 2.25, 3.25, 4.25, 5.25, 6.25, 7.25, 8.25, 9.25], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [3.214564788236803, 4.462059737162049, 4.704228225462174, 4.523507967893809, 3.073745686469774, 6.0078429507780005, 4.226962541870895, 2.847340890749048, 4.6319794458091295, 4.039512686693366]],"toyplot");
    })();</script></div></div>


Most importantly, you will need to decide whether you want to display
data stored within the table, or data from without. For example, we can
also embed a plot that contains its own, arbitrary data:

.. code:: python

    plot_data = numpy.random.normal(loc=4, size=(25, 3))
    
    canvas, table = toyplot.table(data, width=500, height=250)
    table.cells.cell[...].format = toyplot.format.FloatFormatter(format="{:.1f}")
    
    axes = table.body.row[1].cartesian()
    axes.bars(plot_data);



.. raw:: html

    <div class="toyplot" id="t6c220c7d73c943a4b241d9356a438715" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="250.0px" id="tc45021693a664527b096d3d5e9eed603" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 250.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t3a0e1b4b4fcf4d20b70151917652f262"><g transform="translate(70.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">0</text></g><g transform="translate(110.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">1</text></g><g transform="translate(150.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">2</text></g><g transform="translate(190.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">3</text></g><g transform="translate(230.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">4</text></g><g transform="translate(270.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">5</text></g><g transform="translate(310.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">6</text></g><g transform="translate(350.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">7</text></g><g transform="translate(390.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">8</text></g><g transform="translate(430.0,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">9</text></g><g transform="translate(68.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(70.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(72.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(108.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(110.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(112.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(148.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(150.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(152.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">3</text></g><g transform="translate(188.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">3</text></g><g transform="translate(190.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(192.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">8</text></g><g transform="translate(228.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">5</text></g><g transform="translate(230.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(232.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(268.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">1</text></g><g transform="translate(270.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(272.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">6</text></g><g transform="translate(308.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">6</text></g><g transform="translate(310.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(312.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0</text></g><g transform="translate(348.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">2</text></g><g transform="translate(350.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(352.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">9</text></g><g transform="translate(388.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(390.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(392.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">2</text></g><g transform="translate(428.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">4</text></g><g transform="translate(430.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(432.0,125.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">7</text></g><g class="toyplot-coordinates-Cartesian" id="tec6cb971b9c54ab293a3ae0245c2c662"><clipPath id="td0bcbe50030743248aa9dc644a5a967b"><rect height="50.0" width="400.0" x="50.0" y="150.0"></rect></clipPath><g clip-path="url(#td0bcbe50030743248aa9dc644a5a967b)"><g class="toyplot-mark-BarMagnitudes" id="t4b4643fcf6c04fba907149a5c1178664" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="12.544827521311788" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="53.0" y="184.4551724786882"></rect><rect class="toyplot-Datum" height="11.668784964265399" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.76000000000002" x="68.75999999999999" y="185.3312150357346"></rect><rect class="toyplot-Datum" height="13.39618343686368" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="84.52000000000001" y="183.60381656313632"></rect><rect class="toyplot-Datum" height="15.151342415523175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="100.28" y="181.84865758447683"></rect><rect class="toyplot-Datum" height="8.351663427894124" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.76000000000002" x="116.03999999999999" y="188.64833657210588"></rect><rect class="toyplot-Datum" height="11.009627934892876" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="131.8" y="185.99037206510712"></rect><rect class="toyplot-Datum" height="8.236066075096318" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="147.56" y="188.76393392490368"></rect><rect class="toyplot-Datum" height="12.831842145584943" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="163.32" y="184.16815785441506"></rect><rect class="toyplot-Datum" height="12.600734172634162" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="179.07999999999998" y="184.39926582736584"></rect><rect class="toyplot-Datum" height="9.92477944545601" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="194.83999999999997" y="187.075220554544"></rect><rect class="toyplot-Datum" height="13.699960673775422" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="210.60000000000002" y="183.30003932622458"></rect><rect class="toyplot-Datum" height="13.345028052621274" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="226.36" y="183.65497194737873"></rect><rect class="toyplot-Datum" height="13.152522893670294" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="242.12" y="183.8474771063297"></rect><rect class="toyplot-Datum" height="12.349399106275285" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="257.88" y="184.65060089372471"></rect><rect class="toyplot-Datum" height="9.321010588434717" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999934" x="273.64000000000004" y="187.67898941156528"></rect><rect class="toyplot-Datum" height="12.346213690824243" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="289.4" y="184.65378630917576"></rect><rect class="toyplot-Datum" height="13.190309413606798" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="305.15999999999997" y="183.8096905863932"></rect><rect class="toyplot-Datum" height="11.664839977024599" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999934" x="320.92" y="185.3351600229754"></rect><rect class="toyplot-Datum" height="13.03724864185827" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000105" x="336.67999999999995" y="183.96275135814173"></rect><rect class="toyplot-Datum" height="16.663840773855895" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="352.44000000000005" y="180.3361592261441"></rect><rect class="toyplot-Datum" height="13.480670044084604" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999934" x="368.20000000000005" y="183.5193299559154"></rect><rect class="toyplot-Datum" height="8.850445905533803" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="383.96" y="188.1495540944662"></rect><rect class="toyplot-Datum" height="13.209429723958067" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="399.72" y="183.79057027604193"></rect><rect class="toyplot-Datum" height="17.887645994119794" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="415.48" y="179.1123540058802"></rect><rect class="toyplot-Datum" height="9.907910541132281" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="431.24" y="187.09208945886772"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="1.2265069486979883" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="53.0" y="183.22866552999022"></rect><rect class="toyplot-Datum" height="11.702220821934304" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.76000000000002" x="68.75999999999999" y="173.6289942138003"></rect><rect class="toyplot-Datum" height="14.007496445467922" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="84.52000000000001" y="169.5963201176684"></rect><rect class="toyplot-Datum" height="11.464251885671729" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="100.28" y="170.3844056988051"></rect><rect class="toyplot-Datum" height="9.59685391805752" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.76000000000002" x="116.03999999999999" y="179.05148265404836"></rect><rect class="toyplot-Datum" height="10.271113415349276" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="131.8" y="175.71925864975785"></rect><rect class="toyplot-Datum" height="9.801523738254588" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="147.56" y="178.9624101866491"></rect><rect class="toyplot-Datum" height="12.654976922039936" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="163.32" y="171.51318093237512"></rect><rect class="toyplot-Datum" height="15.071244995557919" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="179.07999999999998" y="169.32802083180792"></rect><rect class="toyplot-Datum" height="14.680919458972369" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="194.83999999999997" y="172.39430109557162"></rect><rect class="toyplot-Datum" height="6.4328310139956955" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="210.60000000000002" y="176.86720831222888"></rect><rect class="toyplot-Datum" height="10.666850936658534" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="226.36" y="172.9881210107202"></rect><rect class="toyplot-Datum" height="6.129961685836548" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="242.12" y="177.71751542049316"></rect><rect class="toyplot-Datum" height="10.541809362988232" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="257.88" y="174.10879153073648"></rect><rect class="toyplot-Datum" height="12.465769680295807" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999934" x="273.64000000000004" y="175.21321973126948"></rect><rect class="toyplot-Datum" height="9.89300892883881" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="289.4" y="174.76077738033695"></rect><rect class="toyplot-Datum" height="13.146828956640235" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="305.15999999999997" y="170.66286162975297"></rect><rect class="toyplot-Datum" height="13.533193560112466" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999934" x="320.92" y="171.80196646286294"></rect><rect class="toyplot-Datum" height="8.53662078590574" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000105" x="336.67999999999995" y="175.426130572236"></rect><rect class="toyplot-Datum" height="6.363611371316864" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="352.44000000000005" y="173.97254785482724"></rect><rect class="toyplot-Datum" height="10.172638514273245" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999934" x="368.20000000000005" y="173.34669144164215"></rect><rect class="toyplot-Datum" height="14.546709735239375" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="383.96" y="173.60284435922682"></rect><rect class="toyplot-Datum" height="14.005440187266629" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="399.72" y="169.7851300887753"></rect><rect class="toyplot-Datum" height="12.63404589342386" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="415.48" y="166.47830811245635"></rect><rect class="toyplot-Datum" height="11.080583537224697" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="431.24" y="176.01150592164302"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="14.952169815854262" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="53.0" y="168.27649571413596"></rect><rect class="toyplot-Datum" height="10.031339220401463" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.76000000000002" x="68.75999999999999" y="163.59765499339883"></rect><rect class="toyplot-Datum" height="12.00093880520609" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="84.52000000000001" y="157.5953813124623"></rect><rect class="toyplot-Datum" height="10.11600686444163" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="100.28" y="160.26839883436347"></rect><rect class="toyplot-Datum" height="13.534504955957658" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.76000000000002" x="116.03999999999999" y="165.5169776980907"></rect><rect class="toyplot-Datum" height="12.724373131545747" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="131.8" y="162.9948855182121"></rect><rect class="toyplot-Datum" height="12.05817660657587" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="147.56" y="166.90423358007322"></rect><rect class="toyplot-Datum" height="12.041570572048045" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="163.32" y="159.47161036032708"></rect><rect class="toyplot-Datum" height="9.045011299655641" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="179.07999999999998" y="160.28300953215228"></rect><rect class="toyplot-Datum" height="7.640015763410986" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="194.83999999999997" y="164.75428533216063"></rect><rect class="toyplot-Datum" height="9.973258703975745" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="210.60000000000002" y="166.89394960825314"></rect><rect class="toyplot-Datum" height="10.727988823592142" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="226.36" y="162.26013218712805"></rect><rect class="toyplot-Datum" height="11.372167124889842" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="242.12" y="166.34534829560332"></rect><rect class="toyplot-Datum" height="9.50415725994091" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="257.88" y="164.60463427079557"></rect><rect class="toyplot-Datum" height="6.454474980999237" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999934" x="273.64000000000004" y="168.75874475027024"></rect><rect class="toyplot-Datum" height="10.399668954586417" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="289.4" y="164.36110842575053"></rect><rect class="toyplot-Datum" height="11.913043221097496" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="305.15999999999997" y="158.74981840865547"></rect><rect class="toyplot-Datum" height="16.560680156186237" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999934" x="320.92" y="155.2412863066767"></rect><rect class="toyplot-Datum" height="5.380354260970819" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000105" x="336.67999999999995" y="170.04577631126517"></rect><rect class="toyplot-Datum" height="14.641044097112484" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="352.44000000000005" y="159.33150375771476"></rect><rect class="toyplot-Datum" height="13.214078806943547" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999934" x="368.20000000000005" y="160.1326126346986"></rect><rect class="toyplot-Datum" height="9.766526089086312" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.760000000000048" x="383.96" y="163.8363182701405"></rect><rect class="toyplot-Datum" height="10.897843346131879" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="399.72" y="158.88728674264343"></rect><rect class="toyplot-Datum" height="13.478308112456347" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="415.48" y="153.0"></rect><rect class="toyplot-Datum" height="15.055272387232264" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="15.759999999999991" x="431.24" y="160.95623353441076"></rect></g></g></g></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="450.0" y1="100.0" y2="100.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t6c220c7d73c943a4b241d9356a438715";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tc45021693a664527b096d3d5e9eed603";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t3a0e1b4b4fcf4d20b70151917652f262","data","table data",["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],[[3.0257636662326846, 3.214564788236803], [3.9296551228958974, 4.462059737162049], [4.307968855216034, 4.704228225462174], [3.79150123689412, 4.523507967893809], [5.033800732555499, 3.073745686469774], [1.5995463661877043, 6.0078429507780005], [6.0306036208388, 4.226962541870895], [2.8573687109772363, 2.847340890749048], [4.211883386777701, 4.6319794458091295], [4.704720624317109, 4.039512686693366]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t4b4643fcf6c04fba907149a5c1178664","data","bar data",["left", "right", "baseline", "magnitude0", "magnitude1", "magnitude2"],[[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [4.464392325050896, 4.152630552204535, 4.767368735752411, 5.3919861934464075, 2.972149441318094, 3.918052948173335, 2.9310112165198676, 4.566533696353573, 4.48428811274975, 3.5319823336625147, 4.875475504274324, 4.749163805919065, 4.680656004381456, 4.394844209327204, 3.317116003550666, 4.393710599138665, 4.6941032876787645, 4.15122662929445, 4.639632763193703, 5.930246767465576, 4.797435419427874, 3.149653728344885, 4.700907730915604, 6.365768628840039, 3.525979109874315], [0.43648333937526473, 4.1645295429323985, 4.984919841909897, 4.079842313008629, 3.415281788739212, 3.6552339857453555, 3.488118690873185, 4.503591759111203, 5.363481512426146, 5.224574355126174, 2.289284675970471, 3.796067133898749, 2.181501009608386, 3.7515679456191533, 4.436257604340917, 3.5206759964245027, 4.678629673709857, 4.8161272333600404, 3.0379711680948085, 2.2646511255296073, 3.620189215952621, 5.176812450104929, 4.984188070722415, 4.496142926247595, 3.9433042835090704], [5.321105615470206, 3.5699043091235123, 4.270835848826804, 3.6000354193034774, 4.816593926547842, 4.528288145297394, 4.2912053597430635, 4.2852956847818575, 3.2188947163746082, 2.7188917248559576, 3.5492348968637257, 3.8178245883342656, 4.047071635325711, 3.3822933520029834, 2.2969872258867623, 3.7009837070339198, 4.239555995003897, 5.893534467596201, 1.9147343578798903, 5.2103837049045145, 4.702562224001601, 3.4756638973675438, 3.8782715913331796, 4.796594866664952, 5.357797258107058]],"toyplot");
    })();</script></div></div>


Note that when you do this there is no-longer any relationship between
the plot and the underlying table - you are simply displaying the plot,
constrained to fit in the table cells you selected when you created the
axes.
