
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

First, we load the structure of a graph from a text file into an
:math:`E \times 2` matrix containing the source and target vertices for
each of :math:`E` graph edges:

.. code:: python

    import numpy
    
    edges = numpy.array([row.split() for row in open("communities.edges")], dtype="int")
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
a force-directed layout, inducing the vertex labels from the edge data:

.. code:: python

    import toyplot
    toyplot.graph(edges);



.. raw:: html

    <div align="center" class="toyplot" id="t11dbf1c16fd046d895e248698fc2a18e"><svg class="toyplot-canvas-Canvas" height="600px" id="tc6d512178dc54e94a92094e827b8036e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t29b988e0773c46a0a4774bdf116fd99c"><clipPath id="t6f358d602e2a4c858fc5e9a4b3355b8f"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#t6f358d602e2a4c858fc5e9a4b3355b8f)"><g class="toyplot-mark-Graph" id="t11434b29f4ef4e888e16db75a6d71115"><g class="toyplot-Edges"><path d="M 209.684895569 50.0 L 253.057353078 51.8081031874" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.684895569 50.0 L 203.978190183 90.8386090217" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.684895569 50.0 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.057353078 51.8081031874 L 203.978190183 90.8386090217" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.057353078 51.8081031874 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 203.978190183 90.8386090217 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 392.506888811 253.255666931" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 396.021809817 286.810027968" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 392.506888811 253.255666931 L 396.021809817 286.810027968" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 392.506888811 253.255666931 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 396.021809817 286.810027968 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 308.123513561 516.398610164" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 369.165454933 528.862191383" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 331.004512904 550.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 308.123513561 516.398610164 L 369.165454933 528.862191383" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 308.123513561 516.398610164 L 331.004512904 550.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 369.165454933 528.862191383 L 331.004512904 550.0" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.250480273 123.383734723 L 336.0866379 229.901561209" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.069089366 332.705038873 L 347.518462478 459.818361067" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="209.68489556942228" cy="50.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="253.05735307750501" cy="51.808103187400434" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="203.97819018335846" cy="90.838609021709999" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.25048027263921" cy="123.38373472339872" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="336.08663789994222" cy="229.90156120908347" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="392.50688881059352" cy="253.25566693133214" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="396.02180981664145" cy="286.81002796763073" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="361.06908936632647" cy="332.70503887250106" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="347.51846247830969" cy="459.81836106732754" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="308.12351356081211" cy="516.39861016382122" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="369.16545493310974" cy="528.86219138304273" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="331.00451290448143" cy="550.0" r="2.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(209.68489556942228,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">1</text></g><g class="toyplot-Datum" transform="translate(253.05735307750501,51.808103187400434)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">2</text></g><g class="toyplot-Datum" transform="translate(203.97819018335846,90.838609021709999)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">3</text></g><g class="toyplot-Datum" transform="translate(265.25048027263921,123.38373472339872)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">4</text></g><g class="toyplot-Datum" transform="translate(336.08663789994222,229.90156120908347)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">5</text></g><g class="toyplot-Datum" transform="translate(392.50688881059352,253.25566693133214)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">6</text></g><g class="toyplot-Datum" transform="translate(396.02180981664145,286.81002796763073)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">7</text></g><g class="toyplot-Datum" transform="translate(361.06908936632647,332.70503887250106)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">8</text></g><g class="toyplot-Datum" transform="translate(347.51846247830969,459.81836106732754)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">9</text></g><g class="toyplot-Datum" transform="translate(308.12351356081211,516.39861016382122)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">10</text></g><g class="toyplot-Datum" transform="translate(369.16545493310974,528.86219138304273)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">11</text></g><g class="toyplot-Datum" transform="translate(331.00451290448143,550.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">12</text></g></g></g></g></g></svg><div class="toyplot-interactive"></div></div>


Ground Truth Communities
------------------------

Next, we load a set of ground truth community assignments from a text
file into a :math:`V \times 2` matrix containing the vertex ID and
community ID for each of :math:`V` vertices (note that in this case the
assignments are already sorted in ID order, if they hadn't been, we'd
need to sort them explicitly):

.. code:: python

    ground_truth = numpy.array([row.split() for row in open("communities.ground-truth")], dtype="int")
    ground_truth




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
    vcolor = ground_truth[:,1]
    toyplot.graph(edges, ecolor=ecolor, vsize=20, vlstyle=vlstyle, vcolor=(vcolor, colormap));



.. raw:: html

    <div align="center" class="toyplot" id="tbd9f8211a0914c5db900b44a711314af"><svg class="toyplot-canvas-Canvas" height="600px" id="tdb059baafbb64aa7879cfffaedf6fd55" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="te740f94adff04623861c9fa5e337241d"><clipPath id="t00a0c5b43d8d49bd9b46e0f0439f17be"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#t00a0c5b43d8d49bd9b46e0f0439f17be)"><g class="toyplot-mark-Graph" id="t3dda5e9aa0f8489e93b34ab6690d14fb"><g class="toyplot-Edges"><path d="M 209.684895569 50.0 L 253.057353078 51.8081031874" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.684895569 50.0 L 203.978190183 90.8386090217" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.684895569 50.0 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.057353078 51.8081031874 L 203.978190183 90.8386090217" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.057353078 51.8081031874 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 203.978190183 90.8386090217 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 392.506888811 253.255666931" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 396.021809817 286.810027968" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 392.506888811 253.255666931 L 396.021809817 286.810027968" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 392.506888811 253.255666931 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 396.021809817 286.810027968 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 308.123513561 516.398610164" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 369.165454933 528.862191383" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 331.004512904 550.0" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 308.123513561 516.398610164 L 369.165454933 528.862191383" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 308.123513561 516.398610164 L 331.004512904 550.0" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 369.165454933 528.862191383 L 331.004512904 550.0" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.250480273 123.383734723 L 336.0866379 229.901561209" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.069089366 332.705038873 L 347.518462478 459.818361067" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="209.68489556942228" cy="50.0" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="253.05735307750501" cy="51.808103187400434" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="203.97819018335846" cy="90.838609021709999" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="265.25048027263921" cy="123.38373472339872" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="336.08663789994222" cy="229.90156120908347" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="392.50688881059352" cy="253.25566693133214" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="396.02180981664145" cy="286.81002796763073" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="361.06908936632647" cy="332.70503887250106" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="347.51846247830969" cy="459.81836106732754" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="308.12351356081211" cy="516.39861016382122" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="369.16545493310974" cy="528.86219138304273" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="331.00451290448143" cy="550.0" r="10.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(209.68489556942228,50.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">1</text></g><g class="toyplot-Datum" transform="translate(253.05735307750501,51.808103187400434)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">2</text></g><g class="toyplot-Datum" transform="translate(203.97819018335846,90.838609021709999)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">3</text></g><g class="toyplot-Datum" transform="translate(265.25048027263921,123.38373472339872)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">4</text></g><g class="toyplot-Datum" transform="translate(336.08663789994222,229.90156120908347)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">5</text></g><g class="toyplot-Datum" transform="translate(392.50688881059352,253.25566693133214)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">6</text></g><g class="toyplot-Datum" transform="translate(396.02180981664145,286.81002796763073)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">7</text></g><g class="toyplot-Datum" transform="translate(361.06908936632647,332.70503887250106)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">8</text></g><g class="toyplot-Datum" transform="translate(347.51846247830969,459.81836106732754)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">9</text></g><g class="toyplot-Datum" transform="translate(308.12351356081211,516.39861016382122)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">10</text></g><g class="toyplot-Datum" transform="translate(369.16545493310974,528.86219138304273)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">11</text></g><g class="toyplot-Datum" transform="translate(331.00451290448143,550.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">12</text></g></g></g></g></g></svg><div class="toyplot-interactive"></div></div>


Assigned Communities
--------------------

Next, we render the graph again using a different set of community ID
values, generated using a hypothetical community detection algorithm
that we are working on:

.. code:: python

    assigned = numpy.array([row.split() for row in open("communities.assigned")], dtype="int")
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

    <div align="center" class="toyplot" id="t3ffa1d1c34454f38ad36c194109f516a"><svg class="toyplot-canvas-Canvas" height="600px" id="t52b2ad82cb7f4749a46058c40809fe39" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tb326ce75ea9845aba572080d3b6d389f"><clipPath id="t93fd6e7a7ee9457395a86c6b11309456"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#t93fd6e7a7ee9457395a86c6b11309456)"><g class="toyplot-mark-Graph" id="t6c1ffdb8683d40d39a351ef689e14415"><g class="toyplot-Edges"><path d="M 209.684895569 50.0 L 253.057353078 51.8081031874" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.684895569 50.0 L 203.978190183 90.8386090217" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.684895569 50.0 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.057353078 51.8081031874 L 203.978190183 90.8386090217" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.057353078 51.8081031874 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 203.978190183 90.8386090217 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 392.506888811 253.255666931" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 396.021809817 286.810027968" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 392.506888811 253.255666931 L 396.021809817 286.810027968" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 392.506888811 253.255666931 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 396.021809817 286.810027968 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 308.123513561 516.398610164" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 369.165454933 528.862191383" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 331.004512904 550.0" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 308.123513561 516.398610164 L 369.165454933 528.862191383" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 308.123513561 516.398610164 L 331.004512904 550.0" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 369.165454933 528.862191383 L 331.004512904 550.0" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.250480273 123.383734723 L 336.0866379 229.901561209" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.069089366 332.705038873 L 347.518462478 459.818361067" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(65.1%,84.7%,32.9%);stroke-opacity:1.0"><circle cx="209.68489556942228" cy="50.0" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="253.05735307750501" cy="51.808103187400434" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="203.97819018335846" cy="90.838609021709999" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="265.25048027263921" cy="123.38373472339872" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="336.08663789994222" cy="229.90156120908347" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="392.50688881059352" cy="253.25566693133214" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="396.02180981664145" cy="286.81002796763073" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="361.06908936632647" cy="332.70503887250106" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="347.51846247830969" cy="459.81836106732754" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="308.12351356081211" cy="516.39861016382122" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="369.16545493310974" cy="528.86219138304273" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="331.00451290448143" cy="550.0" r="10.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(209.68489556942228,50.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">1</text></g><g class="toyplot-Datum" transform="translate(253.05735307750501,51.808103187400434)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">2</text></g><g class="toyplot-Datum" transform="translate(203.97819018335846,90.838609021709999)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">3</text></g><g class="toyplot-Datum" transform="translate(265.25048027263921,123.38373472339872)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">4</text></g><g class="toyplot-Datum" transform="translate(336.08663789994222,229.90156120908347)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">5</text></g><g class="toyplot-Datum" transform="translate(392.50688881059352,253.25566693133214)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">6</text></g><g class="toyplot-Datum" transform="translate(396.02180981664145,286.81002796763073)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">7</text></g><g class="toyplot-Datum" transform="translate(361.06908936632647,332.70503887250106)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">8</text></g><g class="toyplot-Datum" transform="translate(347.51846247830969,459.81836106732754)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">9</text></g><g class="toyplot-Datum" transform="translate(308.12351356081211,516.39861016382122)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">10</text></g><g class="toyplot-Datum" transform="translate(369.16545493310974,528.86219138304273)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">11</text></g><g class="toyplot-Datum" transform="translate(331.00451290448143,550.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">12</text></g></g></g></g></g></svg><div class="toyplot-interactive"></div></div>


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

    ground_truth_map = dict(ground_truth.tolist())
    assigned_map = dict(assigned.tolist())
    
    ground_truth_source = [ground_truth_map[vertex] for vertex in edges[:,0]]
    ground_truth_target = [ground_truth_map[vertex] for vertex in edges[:,1]]
    
    assigned_source = [assigned_map[vertex] for vertex in edges[:,0]]
    assigned_target = [assigned_map[vertex] for vertex in edges[:,1]]

.. code:: python

    # Default all edges to light gray.
    ecolor = numpy.repeat("lightgray", len(edges))
    
    selection = numpy.equal(ground_truth_source, ground_truth_target) & numpy.not_equal(assigned_source, assigned_target)
    ecolor[selection] = "red"
    
    selection = numpy.not_equal(ground_truth_source, ground_truth_target) & numpy.equal(assigned_source, assigned_target)
    ecolor[selection] = "green"
    
    canvas, axes, mark = toyplot.graph(edges, ecolor=ecolor, vsize=20, vlstyle=vlstyle, vcolor=(vcolor, colormap));



.. raw:: html

    <div align="center" class="toyplot" id="tefd8998405a9418499d14366dc80eb95"><svg class="toyplot-canvas-Canvas" height="600px" id="t52c70c29136f4093aa0aa0595dadfdd5" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t7ad5704796264409ae18f92d6dd0c040"><clipPath id="t53ba44c69cb84b898920b23112a11050"><rect height="540.0" width="540.0" x="30.0" y="30.0"></rect></clipPath><g clip-path="url(#t53ba44c69cb84b898920b23112a11050)"><g class="toyplot-mark-Graph" id="tc3adb95371ee4e999dee4b3dcefaf4e2"><g class="toyplot-Edges"><path d="M 209.684895569 50.0 L 253.057353078 51.8081031874" style="fill:none;stroke:rgb(100%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.684895569 50.0 L 203.978190183 90.8386090217" style="fill:none;stroke:rgb(100%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 209.684895569 50.0 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(100%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.057353078 51.8081031874 L 203.978190183 90.8386090217" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 253.057353078 51.8081031874 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 203.978190183 90.8386090217 L 265.250480273 123.383734723" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 392.506888811 253.255666931" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 396.021809817 286.810027968" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 336.0866379 229.901561209 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 392.506888811 253.255666931 L 396.021809817 286.810027968" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 392.506888811 253.255666931 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 396.021809817 286.810027968 L 361.069089366 332.705038873" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 308.123513561 516.398610164" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 369.165454933 528.862191383" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 347.518462478 459.818361067 L 331.004512904 550.0" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 308.123513561 516.398610164 L 369.165454933 528.862191383" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 308.123513561 516.398610164 L 331.004512904 550.0" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 369.165454933 528.862191383 L 331.004512904 550.0" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 265.250480273 123.383734723 L 336.0866379 229.901561209" style="fill:none;stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0"></path><path d="M 361.069089366 332.705038873 L 347.518462478 459.818361067" style="fill:none;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0;stroke-width:1.0"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(65.1%,84.7%,32.9%);stroke-opacity:1.0"><circle cx="209.68489556942228" cy="50.0" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="253.05735307750501" cy="51.808103187400434" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="203.97819018335846" cy="90.838609021709999" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="265.25048027263921" cy="123.38373472339872" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="336.08663789994222" cy="229.90156120908347" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="392.50688881059352" cy="253.25566693133214" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="396.02180981664145" cy="286.81002796763073" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="361.06908936632647" cy="332.70503887250106" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="347.51846247830969" cy="459.81836106732754" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="308.12351356081211" cy="516.39861016382122" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="369.16545493310974" cy="528.86219138304273" r="10.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="331.00451290448143" cy="550.0" r="10.0"></circle></g></g><g class="toyplot-Labels"><g class="toyplot-Datum" transform="translate(209.68489556942228,50.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">1</text></g><g class="toyplot-Datum" transform="translate(253.05735307750501,51.808103187400434)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">2</text></g><g class="toyplot-Datum" transform="translate(203.97819018335846,90.838609021709999)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">3</text></g><g class="toyplot-Datum" transform="translate(265.25048027263921,123.38373472339872)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">4</text></g><g class="toyplot-Datum" transform="translate(336.08663789994222,229.90156120908347)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">5</text></g><g class="toyplot-Datum" transform="translate(392.50688881059352,253.25566693133214)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">6</text></g><g class="toyplot-Datum" transform="translate(396.02180981664145,286.81002796763073)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">7</text></g><g class="toyplot-Datum" transform="translate(361.06908936632647,332.70503887250106)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">8</text></g><g class="toyplot-Datum" transform="translate(347.51846247830969,459.81836106732754)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">9</text></g><g class="toyplot-Datum" transform="translate(308.12351356081211,516.39861016382122)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">10</text></g><g class="toyplot-Datum" transform="translate(369.16545493310974,528.86219138304273)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">11</text></g><g class="toyplot-Datum" transform="translate(331.00451290448143,550.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">12</text></g></g></g></g></g></svg><div class="toyplot-interactive"></div></div>


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
